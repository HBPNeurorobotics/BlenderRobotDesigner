# #####
# This file is part of the RobotDesigner of the Neurorobotics subproject (SP10)
# in the Human Brain Project (HBP).
# It has been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
# developed at the Karlsruhe Institute of Technology in the
# High Performance Humanoid Technologies Laboratory (H2T).
# #####

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# #####
#
# Copyright (c) 2016, TU Munich
#
# Changes:
#   2016-12-08: Guang Chen (TUM), Initial version of SDF support
#   2016-1-16: Guang Chen,  v1.0, support exporting kinematic chain&mesh&dynamic
# ######

"""
:term:`Operators <operator>` (and functions) exporting to SDF. It supports the creation of ROS packages, zipped
ROS packages and 'plain' SDF files with absolute or relative file paths.

Note: modify :meth:`pyxb.binding.basis._TypeBinding_mixin.toxml` to call :meth:`xml.dom.minidom.Node.toprettyxml`

"""

# ######
# System imports
import os
import sys
from math import radians
import tempfile
from pathlib import Path
import pyxb

# ######
# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty
from mathutils import Vector

# ######
# RobotDesigner imports
from .generic import sdf_tree
from .generic.helpers import list_to_string, string_to_list, localpose2globalpose
from ...core import config, PluginManager, RDOperator
from ...operators.helpers import ModelSelected, ObjectMode
from ...operators.model import SelectModel
from ..osim.osim_export import create_osim, get_muscles

from ...properties.globals import global_properties

from pyxb import ContentNondeterminismExceededError, BIND

# config file generation
from .generic import model_config_dom
from .generic import sdf_dom
from pyxb.namespace import XMLSchema_instance as xsi
import pyxb



def _uri_for_meshes_and_muscles(in_ros_package: bool, abs_file_paths, toplevel_dir: str, file_path: str):
    """
    Generate proper URI's for included geometry files and muscle definitions (.osim).

    :param in_ros_package:  Whether to export into a ros package or plain files
    :param abs_file_paths: If not intstalled into a ros package decides whether to use absolute file paths.
    :param toplevel_dir: The directory in which to export
    :param file_path: The absolute path of the file for which to generate the URI.
    :return:
    """
    if in_ros_package:
        return "package://" + os.path.relpath(file_path, str(Path(toplevel_dir).parent))
    elif not abs_file_paths:
        return "model://" + os.path.relpath(file_path, str(Path(toplevel_dir).parent))
    else:
        return "model://" + file_path


def export_mesh(operator: RDOperator, context, name: str, directory: str, toplevel_dir: str, in_ros_package: bool,
                abs_file_paths=False, export_collision=False):
    """
    Exports a mesh to a separate file.

    :param operator: The calling operator
    :param context: The current context
    :param name: the name of the mesh (not the file name).
    :type name: basestring.
    :param directory: The directory in which to install the meshes
    :param toplevel_dir: The directory in which to export
    :param in_ros_package: Whether to export into a ros package or plain files
    :param abs_file_paths: If not intstalled into a ros package decides whether to use absolute file paths.
    :param export_collision: Exporting a collision mesh or visualization mesh.
    :return: name of the file the mesh is stored in.
    """

    if not export_collision:
        meshes = [obj.name for obj in bpy.data.objects if
                  obj.type == "MESH" and obj.name == name and
                  not obj.RobotEditor.tag == "COLLISION"]
        directory = os.path.join(directory, "meshes", "visual")

    else:
        meshes = [obj.name for obj in bpy.data.objects if
                  obj.type == "MESH" and name == obj.name and
                  obj.RobotEditor.tag == "COLLISION"]
        directory = os.path.join(directory, "meshes", "collisions")


    if not os.path.exists(directory):
        os.makedirs(directory)

    # There is max. 1 object in the list
    assert len(meshes) <= 1
    for mesh in meshes:
        operator.logger.debug("Processing mesh: %s", mesh)

        model_name = bpy.context.active_object.name
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[mesh].select = True
        bpy.context.scene.objects.active = bpy.data.objects[mesh]
        # bpy.context.active_object.select = True

        # get the mesh vertices number
        bm = bpy.context.scene.objects.active.data
        # print("# of vertices=%d" % len(bm.vertices))

        if len(bm.vertices) > 1:
            if '.' in mesh:
                file_path = os.path.join(directory, bpy.data.objects[mesh].RobotEditor.fileName.replace('.', '_') + '.dae')
            else:
                file_path = os.path.join(directory, bpy.data.objects[mesh].RobotEditor.fileName + '.dae')

            bpy.ops.wm.collada_export(filepath=file_path, apply_modifiers=True, selected=True, use_texture_copies=True)

            # quick fix for dispersed meshes
            # todo: find appropriate solution
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    if "matrix" not in line:
                        file.write(line)
        else:
            if '.' in mesh:
                file_path = os.path.join(directory,
                                         bpy.data.objects[mesh].RobotEditor.fileName.replace('.', '_') + '_vertices' + str(len(bm.vertices)) + '.dae')
            else:
                file_path = os.path.join(directory, bpy.data.objects[mesh].RobotEditor.fileName + '_vertices' + str(len(bm.vertices)) + '.dae')

        SelectModel.run(model_name=model_name)

        return _uri_for_meshes_and_muscles(in_ros_package, abs_file_paths, toplevel_dir, file_path)

            # return ("model://" + os.path.join(model_folder_name, "meshes",
            # mesh + ".dae"))


def create_sdf(operator: RDOperator, context, filepath: str, meshpath: str, toplevel_directory: str, in_ros_package: bool, abs_filepaths=False):
    """
    Creates the SDF XML file and exports the meshes

    :param operator: The calling operator
    :param context: The current context
    :param filepath: path to the SDF file
    :param meshpath: Path to the mesh directory
    :param toplevel_directory: The directory in which to export
    :param in_ros_package: Whether to export into a ros package or plain files
    :param abs_filepaths: If not intstalled into a ros package decides whether to use absolute file paths.
    :return:
    """

    def walk_segments(segment, tree, ref_pose):
        """
        Recursively builds a SDF tree object hierarchy for export

        :param segment: Reference to a blender bone object
        :param tree: Reference to a SDF Tree object
        """
        child = tree.add()
        trafo, dummy = segment.RobotEditor.getTransform()
        # child.joint.origin.rpy = list_to_string(trafo.to_euler())
        # child.joint.origin.xyz = list_to_string([i * j for i, j in zip(trafo.translation, blender_scale_factor)])

        pose_xyz = list_to_string([i * j for i, j in zip(trafo.translation, blender_scale_factor)])
        pose_rpy = list_to_string(trafo.to_euler())
        pose_xyz, pose_rpy = localpose2globalpose(ref_pose, pose_rpy, pose_xyz)

        operator.logger.info(" child link pose'%s'" % ' '.join([pose_xyz, pose_rpy]))
        child.link.pose.append(' '.join([pose_xyz, pose_rpy]))
        # child.link.pos[0] = ' '.join([pose_xyz, pose_rpy])
        # if '_joint' in segment.name:
        #     segment.name = segment.name.replace("_joint", "")
        if '.' in segment.name:
            segment.name = segment.name.replace('.', '_')

        # sdf: here the chile does not mean the child of the joint!!!!it is different
        child.joint.name = segment.name
        child.link.name = segment.name.replace("_joint", "_link")


        if segment.parent:
            parent_link = [l for j, l in tree.connectedLinks.items() if segment.parent.name == j.name]
            if parent_link[0] in tree.connectedJoints:
                tree.connectedJoints[parent_link[0]].append(child.joint)
            else:
                tree.connectedJoints[parent_link[0]] = [child.joint]

        if segment.parent:
            operator.logger.info(" segment parent name'%s'" % segment.parent.name)
        operator.logger.info(" segment joint name'%s'" % child.joint.name)
        operator.logger.info(" segment link name'%s'" % child.link.name)

        print("connected links (joint->link): ", {j.name: l.name for j, l in tree.connectedLinks.items()})
        print("connected joints (link->joint): ", {j.name: l for j, l in tree.connectedJoints.items()})

        if segment.RobotEditor.axis_revert:
            revert = -1
        else:
            revert = 1
        #
        # if segment.RobotEditor.axis == 'X':
        #     child.joint.axis.xyz = list_to_string(Vector((1, 0, 0)) * revert)
        # elif segment.RobotEditor.axis == 'Y':
        #     child.joint.axis.xyz = list_to_string(Vector((0, 1, 0)) * revert)
        # elif segment.RobotEditor.axis == 'Z':
        #     child.joint.axis.xyz = list_to_string(Vector((0, 0, 1)) * revert)

        if segment.RobotEditor.axis == 'X':
            joint_axis_xyz = list_to_string(Vector((1, 0, 0)) * revert)
        elif segment.RobotEditor.axis == 'Y':
            joint_axis_xyz = list_to_string(Vector((0, 1, 0)) * revert)
        elif segment.RobotEditor.axis == 'Z':
            joint_axis_xyz = list_to_string(Vector((0, 0, 1)) * revert)

        child.joint.axis[0].xyz.append(joint_axis_xyz)

        child.joint.axis[0].use_parent_model_frame.append(True)
        operator.logger.info(" joint axis xyz'%s'" % joint_axis_xyz)

        print('Parent link:', child.joint.parent)
        print('Child link:', child.joint.child)
        print('Joint type:', child.joint.type)
        print('Axis:', child.joint.axis)
        print('Axis limit:', child.joint.axis[0].limit)
        print('Axis xyz:', child.joint.axis[0].xyz)

        #
        # if segment.parent is None:
        #     print("Debug: parent bone is none", segment,
        #           segment.RobotEditor.jointMode)
        #     child.joint.type = 'fixed'
        # else:
        #     if segment.RobotEditor.jointMode == 'REVOLUTE':
        #         child.joint.limit.lower = radians(
        #             segment.RobotEditor.theta.min)
        #         child.joint.limit.upper = radians(
        #             segment.RobotEditor.theta.max)
        #         child.joint.type = 'revolute'
        #     if segment.RobotEditor.jointMode == 'PRISMATIC':
        #         child.joint.limit.lower = segment.RobotEditor.d.min
        #         child.joint.limit.upper = segment.RobotEditor.d.max
        #         child.joint.type = 'prismatic'
        #     if segment.RobotEditor.jointMode == 'FIXED':
        #         child.joint.type = 'fixed'
        if segment.parent is None:
            #print("Info: Root joint has no parent", segment, segment.RobotEditor.jointMode)
            child.joint.type = 'fixed'
        else:
            if segment.RobotEditor.jointMode == 'REVOLUTE':
                child.joint.axis[0].limit[0].lower.append((radians(
                    segment.RobotEditor.theta.min)))
                child.joint.axis[0].limit[0].upper.append((radians(
                    segment.RobotEditor.theta.max)))
                child.joint.type = 'revolute'
            if segment.RobotEditor.jointMode == 'PRISMATIC':
                child.joint.axis[0].limit[0].lower.append(segment.RobotEditor.d.min)
                child.joint.axis[0].limit[0].upper.append(segment.RobotEditor.d.max)
                child.joint.type = 'prismatic'
            if segment.RobotEditor.jointMode == 'REVOLUTE2':
                child.joint.type = 'revolute2'
            if segment.RobotEditor.jointMode == 'UNIVERSAL':
                child.joint.type = 'universal'
            if segment.RobotEditor.jointMode == 'BALL':
                child.joint.type = 'ball'
            if segment.RobotEditor.jointMode == 'FIXED':
                child.joint.type = 'fixed'

        operator.logger.info(" joint type'%s'" % child.joint.type)

        # Add properties
        armature = context.active_object
        connected_meshes = [mesh.name for mesh in bpy.data.objects if
                            mesh.type == 'MESH' and mesh.parent_bone == segment.name and mesh.parent == armature]
        # if len(connected_meshes) > 0:
        #     child.link.name = connected_meshes[0]
        # else:
        #     child.link.name = child.joint.name + '_link'
        #     # todo: the RobotDesigner does not have the concept of
        #     # links further it is possible to have
        #     # todo: several meshes assigned to the same bone
        #     # todo: solutions add another property to a bone or
        #     # chose the name from the list of connected meshes
        for mesh in connected_meshes:
            operator.logger.info("Connected mesh name: %s", mesh)
            pose_bone = context.active_object.pose.bones[segment.name]
            pose = pose_bone.matrix.inverted() * context.active_object.matrix_world.inverted() * \
                   bpy.data.objects[mesh].matrix_world

           # bpy.context.active_object.matrix_world = segment_world * trafo_sdf * bpy.context.active_object.matrix_world  # * inverse_matrix(bpy.context.active_object.matrix_world)#* \
            #  bpy.context.active_object.matrix_world

            visual_path = export_mesh(operator, context, mesh, meshpath, toplevel_directory,
                                      in_ros_package, abs_filepaths, export_collision=False)
            operator.logger.info("visual mesh path: %s", visual_path)

            if visual_path and "_vertices1.dae" not in visual_path:
                visual = child.add_mesh(visual_path,
                                        [i * j for i, j in zip(bpy.data.objects[mesh].scale, blender_scale_factor)])
                visual_pose_xyz = list_to_string([i * j for i, j in zip(pose.translation, blender_scale_factor)])
                visual_pose_rpy = list_to_string(pose.to_euler())

                visual.pose.append(' '.join([visual_pose_xyz, visual_pose_rpy]))
                visual.name = bpy.data.objects[mesh].name #child.link.name
            else:
                operator.logger.info("No visual model for: %s", mesh)

            collision_path = export_mesh(operator, context, mesh, meshpath, toplevel_directory,
                                         in_ros_package, abs_filepaths, export_collision=True)

            operator.logger.info("collision mesh path: %s", collision_path)

            if collision_path and "_vertices1.dae" not in collision_path:
                collision = child.add_collision(collision_path,
                                                     [i * j for i, j in
                                                      zip(bpy.data.objects[mesh].scale, blender_scale_factor)])

                operator.logger.info(" collision mesh pose translation wo scale'%s'" % pose.translation)
                operator.logger.info(" collision mesh pose scale factor'%s'" % blender_scale_factor)
                operator.logger.info(" collision mesh pose translation wi scale'%s'" % [i * j for i, j in zip(pose.translation, blender_scale_factor)])

                collision_pose_xyz = list_to_string([i * j for i, j in zip(pose.translation, blender_scale_factor)])
                collision_pose_rpy = list_to_string(pose.to_euler())

                collision.pose.append(' '.join([collision_pose_xyz, collision_pose_rpy]))
                collision.name = bpy.data.objects[mesh].name #           child.link.name + '_collision'
                operator.logger.info(" collision mesh pose'%s'" % collision.pose[0])



            else:
                operator.logger.info("No collision model for: %s", mesh)
        #
        # # todo: pick up the real values from Physics Frame?
        #
        frame_names = [
            frame.name for frame in bpy.data.objects if
            frame.RobotEditor.tag == 'PHYSICS_FRAME' and frame.parent_bone == segment.name]

        # If no frame is connected create a default one. This is required for Gazebo!
        operator.logger.info("frame names: %s", frame_names)

        # if not frame_names:
        #     child.add_inertial()

        for frame in frame_names:
            # Add inertial definitions (for Gazebo)
            inertial = child.link.inertial[0]
            print(inertial, inertial.__dict__)
            if bpy.data.objects[frame].parent_bone == segment.name:
                pose_bone = context.active_object.pose.bones[segment.name]


                # set mass
                inertial.mass[0] = bpy.data.objects[frame].RobotEditor.dynamics.mass
                if inertial.mass[0] <= 0.:
                    raise ValueError("Mass of "+frame+" is not positive, but "+str(inertial.mass[0]))
                # Ugly, to throw an exception here. But appending info_list did not print the info in the GUI.

                # set inertia
                inertial.inertia[0].ixx[0] = bpy.data.objects[frame].RobotEditor.dynamics.inertiaXX
                inertial.inertia[0].ixy[0] = bpy.data.objects[frame].RobotEditor.dynamics.inertiaXY
                inertial.inertia[0].ixz[0] = bpy.data.objects[frame].RobotEditor.dynamics.inertiaXZ
                inertial.inertia[0].iyy[0] = bpy.data.objects[frame].RobotEditor.dynamics.inertiaYY
                inertial.inertia[0].iyz[0] = bpy.data.objects[frame].RobotEditor.dynamics.inertiaYZ
                inertial.inertia[0].izz[0] = bpy.data.objects[frame].RobotEditor.dynamics.inertiaZZ

                # set inertial pose
                pose = pose_bone.matrix.inverted() * context.active_object.matrix_world.inverted() * \
                       bpy.data.objects[frame].matrix_world

                frame_pose_xyz = list_to_string([i * j for i, j in zip(pose.translation, blender_scale_factor)])
                frame_pose_rpy = list_to_string(pose.to_euler())

                inertial.pose[0] = ' '.join([frame_pose_xyz, frame_pose_rpy])

        #
        # # add joint controllers
        # if operator.gazebo and segment.RobotEditor.jointController.isActive is True:
        #     controller = child.add_joint_controller(root.control_plugin)
        #     controller.joint_name = child.joint.name
        #     controller.type = segment.RobotEditor.jointController.controllerType
        #     if segment.RobotEditor.jointController.P <= 1.0:
        #         segment.RobotEditor.jointController.P = 100
        #     controller.pid = list_to_string([segment.RobotEditor.jointController.P,
        #                                      segment.RobotEditor.jointController.I,
        #                                      segment.RobotEditor.jointController.D])

        # Add geometry
        for child_segments in segment.children:
            operator.logger.info("Next Segment'%s'" % child_segments.name)
            ref_pose = string_to_list(child.link.pose[0])
            walk_segments(child_segments, child, ref_pose)

    robot_name = context.active_object.name

    blender_scale_factor = context.active_object.scale
    blender_scale_factor = [blender_scale_factor[0],blender_scale_factor[2],blender_scale_factor[1]]

    root = sdf_tree.SDFTree.create_empty(robot_name)
   # root.pose.append(list_to_string([0, 0, 0, 10, 0, 0]))

    # todo SDF Plugin
    # build control plugin element
    # if operator.gazebo:
    #     root.control_plugin = root.add_joint_control_plugin()

    # add root geometries to root.link
    muscles = get_muscles(robot_name)
    if muscles:
        # add muscles path tag
        muscle_uri = _uri_for_meshes_and_muscles(
            in_ros_package,
            abs_filepaths,
            toplevel_directory,
            os.path.join(toplevel_directory, 'muscles.osim'))
        root.sdf.model[0].muscles.append(muscle_uri)

        # add OpenSim muscle plugin
        root.sdf.model[0].plugin.append(sdf_dom.plugin())
        root.sdf.model[0].plugin[0].name = "muscle_interface_plugin"
        root.sdf.model[0].plugin[0].filename = "libgazebo_ros_muscle_interface.so"

    root_segments = [b for b in context.active_object.data.bones if
                     b.parent is None]

    for segments in root_segments:
        operator.logger.info("Root Segment'%s'" % segments.name)
        ref_pose = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # transform to gazebo coordinate frame
        walk_segments(segments, root, ref_pose)

    operator.logger.info("Writing to '%s'" % filepath)
    root.write(filepath)

#     # insert gazebo tags before "</robot>" tag
#     if operator.gazebo:
#         with open(filepath, "r") as f:
#             content = f.read()
#         gazebo_tags = global_properties.gazebo_tags.get(bpy.context.scene)
#         content = content.replace("</robot>", gazebo_tags + "</robot>")
#         with open(filepath, "w") as f:
#             f.write(content)
#
# #
# def create_package(operator: RDOperator, context, toplevel_dir, base_link_name):
#     '''
#     Create a ros package. Copies a template from the resources folder and replaces place holders with the robot name.
#
#     :param operator: The calling operator
#     :param context: The current context
#     :param toplevel_dir: The directory in which to export
#     :return:
#     '''
#     import os
#     import shutil
#
#     operator.logger.debug('Exporting to: %s', toplevel_dir)
#     robot_name = context.active_object.name
#
#     target = os.path.join(toplevel_dir, robot_name + '_description')
#
#     try:
#         shutil.copytree(os.path.join(config.resource_path,
#                                      'robot_name_description'), target)
#     except FileExistsError:
#         operator.logger.error('Attempted to overwrite existing package')
#         operator.report({'ERROR'}, 'File %s exists' % target)
#
#     for dname, dirs, files in os.walk(target, topdown=False):
#         for dir in [i for i in dirs if "robot_name" in i]:
#             os.rename(os.path.join(dname, dir),
#                       os.path.join(dname, dir.replace("robot_name", robot_name)))
#
#         for fname in files:
#             operator.logger.debug('File: %s, %s, %s, %s',
#                                   fname, dname, dirs, robot_name)
#             fpath = os.path.join(dname, fname)
#             try:
#                 with open(fpath) as f:
#                     s = f.read()
#                 s = s.replace("$robot_name$", robot_name)
#                 with open(fpath, "w") as f:
#                     f.write(s)
#                 if "robot_name" in fname:
#                     os.rename(os.path.join(dname, fname),
#                               os.path.join(dname, fname.replace("robot_name", robot_name)))
#             except UnicodeDecodeError:
#                 pass
#
#     create_urdf(operator=operator, context=context, base_link_name=base_link_name,
#                 filepath=os.path.join(target, "sdf", robot_name + ".sdf"),
#                 meshpath=target, toplevel_directory=toplevel_dir, in_ros_package=True, abs_filepaths=False)


# @RDOperator.Preconditions(ModelSelected, ObjectMode)
# @PluginManager.register_class
# class ExportZippedPackage(RDOperator):
#     """
#     :ref:`operator` for exporting  the selected robot to an SDF File into a zipped ROS package.
#     """
#
#     bl_idname = config.OPERATOR_PREFIX + 'export_to_sdf_package_zipped'
#     bl_label = "Export zipped ROS/SDF Package"
#
#     filter_glob = StringProperty(
#         default="*.zip",
#         options={'HIDDEN'},
#     )
#
#     filepath = StringProperty(name="Filename", subtype='FILE_PATH')
#     gazebo = BoolProperty(name="Export Gazebo tags", default=True)
#
#     package_url = BoolProperty(name="Package URL", default=True)
#     abs_file_path = BoolProperty(name="Absolute Filepaths", default=False)
#
#     base_link_name = StringProperty(name="Base link:", default="root_link")
#
#     @RDOperator.OperatorLogger
#     @RDOperator.Postconditions(ModelSelected, ObjectMode)
#     def execute(self, context):
#         """
#         Code snipped from `<http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory>`_
#         """
#         import zipfile
#
#         if os.path.isdir(self.filepath):
#             self.logger.debug(self.filepath)
#             self.report({'ERROR'}, "No File selected!")
#             return {'FINISHED'}
#
#         def zipdir(path, ziph):
#             # ziph is zipfile handle
#             for root, dirs, files in os.walk(path):
#                 self.logger.debug("%s, %s, %s,", root, dirs, files)
#                 for file in files:
#                     file_path = os.path.join(root, file)
#                     ziph.write(file_path, os.path.relpath(file_path, path))
#
#         with tempfile.TemporaryDirectory() as target:
#             create_package(self, context, target, self.base_link_name)
#
#             with zipfile.ZipFile(self.filepath, 'w') as zipf:
#                 zipdir(target, zipf)
#
#         return {'FINISHED'}
#
#     def invoke(self, context, event):
#         context.window_manager.fileselect_add(self)
#         return {'RUNNING_MODAL'}

#
# @RDOperator.Preconditions(ModelSelected, ObjectMode)
# @PluginManager.register_class
# class ExportPackage(RDOperator):
#     """
#     :ref:`operator` for exporting  the selected robot to an URDF File into a ROS package.
#
#     **Preconditions:**
#
#     **Postconditions:**
#     """
#
#     # Obligatory class attributes
#     bl_idname = config.OPERATOR_PREFIX + "export_to_sdf_package"
#     bl_label = "Export ROS/SDF Package"
#
#     directory = StringProperty(
#         name="Mesh directory", subtype='DIR_PATH', default="")
#     gazebo = BoolProperty(name="Export Gazebo tags", default=True)
#
#     package_url = BoolProperty(name="Package URL", default=True)
#     abs_file_path = BoolProperty(name="Absolute Filepaths", default=False)
#     base_link_name = StringProperty(name="Base link:", default="root_link")
#
#     @RDOperator.OperatorLogger
#     @RDOperator.Postconditions(ModelSelected, ObjectMode)
#     def execute(self, context):
#         create_package(self, context, self.directory, self.base_link_name)
#         return {'FINISHED'}
#
#     def invoke(self, context, event):
#         context.window_manager.fileselect_add(self)
#         return {'RUNNING_MODAL'}


def create_config(operator: RDOperator, context,
                filepath: str, meshpath: str, toplevel_directory: str, in_ros_package: bool, abs_filepaths=False):
    """
    Creates the model.config file and exports it

    :param operator: The calling operator
    :param context: The current context
    #   :param filepath: path to the SDF file
    #   :param meshpath: Path to the mesh directory
    :param toplevel_directory: The directory in which to export
    :param in_ros_package: Whether to export into a ros package or plain files
    :param abs_filepaths: If not intstalled into a ros package decides whether to use absolute file paths.
    :return:
    """

    # set namespace
    pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace("http://schemas.humanbrainproject.eu/SP10/2017/model_config")

    # create model config element
    modelI = model_config_dom.model()

    # get model data
    modelI.name = bpy.context.active_object.name
    modelI.version = bpy.context.active_object.RobotEditor.modelMeta.model_version

    # get thumbnail data
    modelI.thumbnail = "thumbnail.png"

    # set sdf fixed name
    sdf = model_config_dom.sdf_versioned()
    sdf._setValue("model.sdf")
    sdf.version = 1.5

    modelI.sdf = sdf

    # get author data
    author = model_config_dom.author_type(bpy.context.active_object.RobotEditor.author.authorName,bpy.context.active_object.RobotEditor.author.authorEmail)
    modelI.author = author

    modelI.description = bpy.context.active_object.RobotEditor.modelMeta.model_description


    # export model.config file
    with open(toplevel_directory + "/model.config", "w") as f:
        output = modelI.toDOM()
        output.documentElement.setAttributeNS(xsi.uri(), 'xsi:schemaLocation','http://schemas.humanbrainproject.eu/SP10/2017/model_config ../model_configuration.xsd')
        output.documentElement.setAttributeNS(xsi.uri(), 'xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
        output = output.toprettyxml()
        f.write(output)


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportPlain(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to a SDF File and mesh directory in the same directory.
    """

    bl_idname = config.OPERATOR_PREFIX + 'export_to_sdf_plain'
    bl_label = "Export SDF - plain"

    filter_glob = StringProperty(
        default="*.sdf",
        options={'HIDDEN'},
    )

    abs_file_paths = BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo = BoolProperty(name="Export Gazebo tags", default=True)
    filepath = StringProperty(name="Filename", subtype='FILE_PATH')

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        toplevel_dir = self.filepath
        self.filepath = os.path.join(self.filepath, 'model.sdf')

        create_sdf(self, context, filepath=self.filepath,
                    meshpath=toplevel_dir, toplevel_directory=toplevel_dir,
                    in_ros_package=False, abs_filepaths=self.abs_file_paths)
        create_config(self, context, filepath=self.filepath,
                      meshpath=toplevel_dir, toplevel_directory=toplevel_dir,
                      in_ros_package=False, abs_filepaths=self.abs_file_paths)
        create_osim(self, context, filepath=self.filepath,
                    meshpath=toplevel_dir, toplevel_directory=toplevel_dir,
                    in_ros_package=False, abs_filepaths=self.abs_file_paths)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportPackage(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to an SDF File into a ROS package including model.config file.
    """

    bl_idname = config.OPERATOR_PREFIX + 'export_to_package'
    bl_label = "Export SDF - ROS package"

    filter_glob = StringProperty(
        default="*.sdf",
        options={'HIDDEN'},
    )

    abs_file_paths = BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo = BoolProperty(name="Export Gazebo tags", default=True)
    filepath = StringProperty(name="Filename", subtype='FILE_PATH')

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        toplevel_dir = self.filepath
        self.filepath = os.path.join(self.filepath, 'model.sdf')

        create_sdf(self, context, filepath=self.filepath,
                    meshpath=toplevel_dir, toplevel_directory=toplevel_dir,
                    in_ros_package=False, abs_filepaths=self.abs_file_paths)
        create_config(self, context, filepath=self.filepath,
                      meshpath=toplevel_dir, toplevel_directory=toplevel_dir,
                      in_ros_package=False, abs_filepaths=self.abs_file_paths)
        create_osim(self, context, filepath=self.filepath,
                    meshpath=toplevel_dir, toplevel_directory=toplevel_dir,
                    in_ros_package=False, abs_filepaths=self.abs_file_paths)
        return {'FINISHED'}

    def invoke(self, context, event):
        self.filepath = context.active_object.name.replace(" ", "_")
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportZippedPackage(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to an SDF File into a zipped ROS package.
    """

    bl_idname = config.OPERATOR_PREFIX + 'export_to_sdf_package_zipped'
    bl_label = "Export SDF - ROS zipped package"

    filter_glob = StringProperty(
        default="*.zip",
        options={'HIDDEN'},
    )

    abs_file_paths = BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo = BoolProperty(name="Export Gazebo tags", default=True)
    filepath = StringProperty(name="Filename", subtype='FILE_PATH')

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        """
        Code snipped from `<http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory>`_
        """
        import zipfile

        if os.path.isdir(self.filepath):
            self.logger.debug(self.filepath)
            self.report({'ERROR'}, "No File selected!")
            return {'FINISHED'}

        def zipdir(path, ziph):
            # ziph is zipfile handle
            for root, dirs, files in os.walk(path):
                self.logger.debug("%s, %s, %s,", root, dirs, files)
                for file in files:
                    file_path = os.path.join(root, file)
                    ziph.write(file_path, os.path.relpath(file_path, path))

        with tempfile.TemporaryDirectory() as target:

            dir_name  = os.path.splitext(os.path.basename(self.filepath))[0]
            temp_dir  = os.path.join(target, dir_name)
            temp_file = os.path.join(temp_dir, 'model.sdf')
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)
            create_sdf(self, context, filepath=temp_file,
                       meshpath=temp_dir, toplevel_directory=temp_dir,
                       in_ros_package=False, abs_filepaths=self.abs_file_paths)
            create_config(self, context, filepath=self.filepath,
                          meshpath=temp_dir, toplevel_directory=temp_dir,
                          in_ros_package=False, abs_filepaths=self.abs_file_paths)
            create_osim(self, context, filepath=self.filepath,
                        meshpath=temp_dir, toplevel_directory=temp_dir,
                        in_ros_package=False, abs_filepaths=self.abs_file_paths)
            self.logger.debug(temp_file)
            with zipfile.ZipFile(self.filepath, 'w') as zipf:
                zipdir(target, zipf)

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    #
    #
    # filepath = StringProperty(name="Filename", subtype='FILE_PATH')
    # gazebo = BoolProperty(name="Export Gazebo tags", default=True)
    #
    # package_url = BoolProperty(name="Package URL", default=True)
    #
    # base_link_name = StringProperty(name="Base link:", default="root_link")
    #
    # @RDOperator.OperatorLogger
    # @RDOperator.Postconditions(ModelSelected, ObjectMode)
    # def execute(self, context):
    #     """
    #     Code snipped from `<http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory>`_
    #     """
    #     import zipfile
    #
    #     if os.path.isdir(self.filepath):
    #         self.logger.debug(self.filepath)
    #         self.report({'ERROR'}, "No File selected!")
    #         return {'FINISHED'}
    #
    #     def zipdir(path, ziph):
    #         # ziph is zipfile handle
    #         for root, dirs, files in os.walk(path):
    #             self.logger.debug("%s, %s, %s,", root, dirs, files)
    #             for file in files:
    #                 file_path = os.path.join(root, file)
    #                 ziph.write(file_path, os.path.relpath(file_path, path))
    #
    #     with tempfile.TemporaryDirectory() as target:
    #         create_package(self, context, target, self.base_link_name)
    #
    #         with zipfile.ZipFile(self.filepath, 'w') as zipf:
    #             zipdir(target, zipf)
    #
    #     return {'FINISHED'}
    #
    # def invoke(self, context, event):
    #     context.window_manager.fileselect_add(self)
    #     return {'RUNNING_MODAL'}
