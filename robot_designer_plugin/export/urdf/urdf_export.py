# #####
#  This file is part of the RobotDesigner developed in the Neurorobotics
#  subproject of the Human Brain Project (https://www.humanbrainproject.eu).
#
#  The Human Brain Project is a European Commission funded project
#  in the frame of the Horizon2020 FET Flagship plan.
#  (http://ec.europa.eu/programmes/horizon2020/en/h2020-section/fet-flagships)
#
#  The Robot Designer has initially been forked from the RobotEditor
#  (https://gitlab.com/h2t/roboteditor) developed at the Karlsruhe Institute
#  of Technology in the High Performance Humanoid Technologies Laboratory (H2T).
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
#  Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# ######

"""
:term:`Operators <operator>` (and functions) exporting to URDF. It supports the creation of ROS packages, zipped
ROS packages and 'plain' URDF files with absolute or relative file paths.

Note: modify :meth:`pyxb.binding.basis._TypeBinding_mixin.toxml` to call :meth:`xml.dom.minidom.Node.toprettyxml`

"""

# System imports
import os
from math import radians
import tempfile

# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty
from mathutils import Vector

# RobotDesigner imports
from .generic import urdf_tree
from .generic.helpers import list_to_string
from ...core import config, PluginManager, RDOperator
from ...core.logfile import export_logger
from ...operators.helpers import ModelSelected, ObjectMode
from ...operators.model import SelectModel

from ...properties.segments import getTransformFromBlender
from ...properties.globals import global_properties


def export_mesh(operator: RDOperator, context, name: str, directory: str, toplevel_dir: str, in_ros_package: bool,
                                                          abs_file_paths = False, export_collision = False):
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
        meshes = [obj.name for obj in context.scene.objects if
              obj.type == "MESH" and obj.name == name and
              not obj.RobotDesigner.tag == "COLLISION"]
        directory = os.path.join(directory, "meshes")

    else:
        meshes = [obj.name for obj in context.scene.objects if
              obj.type == "MESH" and name == obj.name and
              obj.RobotDesigner.tag == "COLLISION"]
        directory = os.path.join(directory, "collisions")

    if not os.path.exists(directory):
        os.makedirs(directory)

    # There is max. 1 object in the list
    assert len(meshes) <= 1
    for mesh in meshes:
        export_logger.debug("Processing mesh: %s", mesh)

        model_name = bpy.context.active_object.name
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[mesh].select = True
        bpy.context.scene.objects.active = bpy.data.objects[mesh]
        # bpy.context.active_object.select = True

        # get the mesh vertices number
        bm = bpy.context.scene.objects.active.data
        # export_logger.debug("# of vertices=%d" % len(bm.vertices))

        if len(bm.vertices) > 1:
            if '.' in mesh:
                file_path = os.path.join(directory, mesh.replace('.', '_') + '.dae')
            else:
               file_path = os.path.join(directory, mesh + '.dae')

            bpy.ops.wm.collada_export(
                filepath=file_path, apply_modifiers=True, selected=True, use_texture_copies=True)

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
               file_path = os.path.join(directory, mesh.replace('.', '_') + '_vertices' + str(len(bm.vertices)) + '.dae')
           else:
              file_path = os.path.join(directory, mesh + '_vertices' + str(len(bm.vertices)) + '.dae')

        SelectModel.run(model_name=model_name)
        if in_ros_package:
            return "package://" + os.path.relpath(file_path, toplevel_dir)
        elif not abs_file_paths:
            return "file://" + os.path.relpath(file_path, toplevel_dir)
        else:
            return "file://" + file_path

            # return ("model://" + os.path.join(model_folder_name, "meshes",
            # mesh + ".dae"))


def create_urdf(operator: RDOperator, context, base_link_name,
                          filepath: str, meshpath: str, toplevel_directory: str, in_ros_package: bool, abs_filepaths = False):
    """
    Creates the URDF XML file and exports the meshes

    :param operator: The calling operator
    :param context: The current context
    :param filepath: path to the URDF file
    :param meshpath: Path to the mesh directory
    :param toplevel_directory: The directory in which to export
    :param in_ros_package: Whether to export into a ros package or plain files
    :param abs_filepaths: If not intstalled into a ros package decides whether to use absolute file paths.
    :return:
    """


def walk_segments(segment, tree):
    """
    Recursively builds a URDF tree object hierarchy for export

    :param segment: Reference to a blender bone object
    :param tree: Reference to a URDF Tree object
    """
    child = tree.add()
    trafo, _ = getTransformFromBlender(segment)
    child.joint.origin.rpy = list_to_string(trafo.to_euler())
    child.joint.origin.xyz = list_to_string([i * j for i, j in zip(trafo.translation, blender_scale_factor)])

    if '_joint' in segment.name:
        segment.name = segment.name.replace("_joint", "")
    if '.' in segment.name:
        segment.name = segment.name.replace('.', '_')

    child.joint.name = segment.name + '_joint'
    child.link.name = segment.name + '_link'
    if segment.RobotDesigner.axis_revert:
        revert = -1
    else:
        revert = 1

    if segment.RobotDesigner.axis == 'X':
        child.joint.axis.xyz = list_to_string(Vector((1, 0, 0)) * revert)
    elif segment.RobotDesigner.axis == 'Y':
        child.joint.axis.xyz = list_to_string(Vector((0, 1, 0)) * revert)
    elif segment.RobotDesigner.axis == 'Z':
        child.joint.axis.xyz = list_to_string(Vector((0, 0, 1)) * revert)

    if segment.parent is None:
        export_logger.debug("Debug: parent bone is none", segment,
              segment.RobotDesigner.jointMode)
        child.joint.type = 'fixed'
    else:
        if segment.RobotDesigner.jointMode == 'REVOLUTE':
            child.joint.limit.lower = radians(
                segment.RobotDesigner.theta.min)
            child.joint.limit.upper = radians(
                segment.RobotDesigner.theta.max)
            child.joint.type = 'revolute'
        if segment.RobotDesigner.jointMode == 'PRISMATIC':
            child.joint.limit.lower = segment.RobotDesigner.d.min
            child.joint.limit.upper = segment.RobotDesigner.d.max
            child.joint.type = 'prismatic'
        if segment.RobotDesigner.jointMode == 'FIXED':
            child.joint.type = 'fixed'

    # Add properties
    connected_meshes = [mesh.name for mesh in context.scene.objects if
                        mesh.type == 'MESH' and mesh.parent_bone == segment.name]
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
        pose_bone = context.active_object.pose.bones[segment.name]
        pose = pose_bone.matrix.inverted() * context.active_object.matrix_world.inverted() * \
               bpy.data.objects[mesh].matrix_world

        visual_path = export_mesh(operator, context, mesh, meshpath, toplevel_directory,
                                  in_ros_package, abs_filepaths, export_collision=False)
        if visual_path and "_vertices1.dae" not in visual_path:
            visual = child.add_mesh(visual_path,
                                    [i * j for i, j in zip(bpy.data.objects[mesh].scale, blender_scale_factor)])
            visual.origin.xyz = list_to_string([i * j for i, j in zip(pose.translation, blender_scale_factor)])
            visual.origin.rpy = list_to_string(pose.to_euler())
        else:
            export_logger.info("No visual model for: %s", mesh)

        collision_path = export_mesh(operator, context, mesh, meshpath, toplevel_directory,
                                     in_ros_package, abs_filepaths, export_collision=True)
        if collision_path and "_vertices1.dae" not in collision_path:
            collision = child.add_collisionmodel(collision_path,
                                                 [i * j for i, j in
                                                  zip(bpy.data.objects[mesh].scale, blender_scale_factor)])

            collision.origin.xyz = list_to_string([i * j for i, j in zip(pose.translation, blender_scale_factor)])
            collision.origin.rpy = list_to_string(pose.to_euler())
        else:
            export_logger.info("No collision model for: %s", mesh)

    # todo: pick up the real values from Physics Frame?

    frame_names = [
        frame.name for frame in context.scene.objects if
        frame.RobotDesigner.tag == 'PHYSICS_FRAME' and frame.parent_bone == segment.name]

    # If no frame is connected create a default one. This is required for Gazebo!
    if not frame_names:
        child.add_inertial()

    for frame in frame_names:
        # Add inertial definitions (for Gazebo)
        inertial = child.add_inertial()
        export_logger.debug(inertial, inertial.__dict__)
        if bpy.data.objects[frame].parent_bone == segment.name:
            # set mass
            inertial.mass.value_ = bpy.data.objects[frame].RobotDesigner.dynamics.mass

            # set inertia
            inertial.inertia.ixx = round(bpy.data.objects[frame].RobotDesigner.dynamics.inertiaXX, 4)
            inertial.inertia.ixy = round(bpy.data.objects[frame].RobotDesigner.dynamics.inertiaXY, 4)
            inertial.inertia.ixz = round(bpy.data.objects[frame].RobotDesigner.dynamics.inertiaXZ, 4)
            inertial.inertia.iyy = round(bpy.data.objects[frame].RobotDesigner.dynamics.inertiaYY, 4)
            inertial.inertia.iyz = round(bpy.data.objects[frame].RobotDesigner.dynamics.inertiaYZ, 4)
            inertial.inertia.izz = round(bpy.data.objects[frame].RobotDesigner.dynamics.inertiaZZ, 4)

            # set inertial pose
            assert False, "FIXME: Use the matrix of the physics frame rather than intertiaTrans and inertiaRot!"
            inertial.origin.xyz = list_to_string(bpy.data.objects[frame].RobotDesigner.dynamics.inertiaTrans)
            inertial.origin.rpy = list_to_string(bpy.data.objects[frame].RobotDesigner.dynamics.inertiaRot)

    # add joint controllers
    if operator.gazebo and segment.RobotDesigner.jointController.isActive is True:
        controller = child.add_joint_controller(root.control_plugin)
        controller.joint_name = child.joint.name
        controller.type = segment.RobotDesigner.jointController.controllerType
        if segment.RobotDesigner.jointController.P <= 1.0:
            segment.RobotDesigner.jointController.P = 100
        controller.pid = list_to_string([segment.RobotDesigner.jointController.P,
                                         segment.RobotDesigner.jointController.I,
                                         segment.RobotDesigner.jointController.D])

    # Add geometry
    for child_segments in segment.children:
        walk_segments(child_segments, child)

    robot_name = context.active_object.name

    blender_scale_factor = context.active_object.scale

    root = urdf_tree.URDFTree.create_empty(robot_name, base_link_name)

    # build control plugin element
    if operator.gazebo:
        root.control_plugin = root.add_joint_control_plugin()

    # add root geometries to root.link

    root_segments = [b for b in context.active_object.data.bones if
                 b.parent is None]

    for segments in root_segments:
        walk_segments(segments, root)

    export_logger.info("Writing to '%s'" % filepath)
    root.write(filepath)

    # insert gazebo tags before "</robot>" tag
    if operator.gazebo:
        with open(filepath, "r") as f:
            content = f.read()
        gazebo_tags = global_properties.gazebo_tags.get(bpy.context.scene)
        content = content.replace("</robot>", gazebo_tags + "</robot>")
        content = content.replace('xmlns="http://schemas.humanbrainproject.eu/SP10/2017/model_config"', "")
        with open(filepath, "w") as f:
           f.write(content)


def create_package(operator: RDOperator, context, toplevel_dir, base_link_name):
    '''
    Create a ros package. Copies a template from the resources folder and replaces place holders with the robot name.

    :param operator: The calling operator
    :param context: The current context
    :param toplevel_dir: The directory in which to export
    :return:
    '''
    import os
    import shutil

    export_logger.debug('Exporting to: %s', toplevel_dir)
    robot_name = context.active_object.name

    target = os.path.join(toplevel_dir, robot_name + '_description')

    try:
       shutil.copytree(os.path.join(config.resource_path,
                                 'robot_name_description'), target)
    except FileExistsError:
        export_logger.error('Attempted to overwrite existing package')
        operator.report({'ERROR'}, 'File %s exists' % target)

    for dname, dirs, files in os.walk(target, topdown=False):
        for dir in [i for i in dirs if "robot_name" in i]:
           os.rename(os.path.join(dname, dir),
                       os.path.join(dname, dir.replace("robot_name", robot_name)))

        for fname in files:
            export_logger.debug('File: %s, %s, %s, %s',
                              fname, dname, dirs, robot_name)
            fpath = os.path.join(dname, fname)
            try:
                with open(fpath) as f:
                    s = f.read()
                s = s.replace("$robot_name$", robot_name)
                with open(fpath, "w") as f:
                    f.write(s)
                if "robot_name" in fname:
                    os.rename(os.path.join(dname, fname),
                          os.path.join(dname, fname.replace("robot_name", robot_name)))
            except UnicodeDecodeError:
                pass

    create_urdf(operator=operator, context=context, base_link_name=base_link_name,
            filepath=os.path.join(target, "urdf", robot_name + ".urdf"),
            meshpath=target, toplevel_directory=toplevel_dir, in_ros_package=True, abs_filepaths=False)


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportZippedPackage(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to an URDF File into a zipped ROS package.
    """

    bl_idname = config.OPERATOR_PREFIX + 'export_to_urdf_package_zipped'
    bl_label = "Export URDF - ROS zipped Package"

    filter_glob: StringProperty(
        default="*.zip",
        options={'HIDDEN'},
    )

    filepath: StringProperty(name="Filename", subtype='FILE_PATH')
    gazebo: BoolProperty(name="Export Gazebo tags", default=True)

    package_url: BoolProperty(name="Package URL", default=True)
    abs_file_path: BoolProperty(name="Absolute Filepaths", default=False)

    base_link_name: StringProperty(name="Base link:", default="root_link")

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
            create_package(self, context, target, self.base_link_name)

            with zipfile.ZipFile(self.filepath, 'w') as zipf:
                zipdir(target, zipf)

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportPackage(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to an URDF File into a ROS package.

    **Preconditions:**

    **Postconditions:**
    """

    # Obligatory class attributes
    bl_idname = config.OPERATOR_PREFIX + "export_to_urdf_package"
    bl_label = "Export URDF - ROS package"

    directory: StringProperty(
        name="Mesh directory", subtype='DIR_PATH', default="")
    gazebo: BoolProperty(name="Export Gazebo tags", default=True)

    package_url: BoolProperty(name="Package URL", default=True)
    abs_file_path: BoolProperty(name="Absolute Filepaths", default=False)
    base_link_name: StringProperty(name="Base link:", default="root_link")

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        create_package(self, context, self.directory, self.base_link_name)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportPlain(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to a URDF File and mesh directory in the same directory.
    """

    bl_idname = config.OPERATOR_PREFIX + 'export_to_urdf_plain'
    bl_label = "Export URDF - plain"

    filter_glob: StringProperty(
        default="*.urdf",
        options={'HIDDEN'},
    )

    abs_file_paths: BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo: BoolProperty(name="Export Gazebo tags", default=True)
    filepath: StringProperty(name="Filename", subtype='FILE_PATH')
    base_link_name: StringProperty(name="Base link:", default="root_link")

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        toplevel_dir = os.path.dirname(self.filepath)
        create_urdf(self, context, filepath=self.filepath, base_link_name=self.base_link_name,
                    meshpath=toplevel_dir, toplevel_directory=toplevel_dir,
                    in_ros_package=False, abs_filepaths=self.abs_file_paths)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
