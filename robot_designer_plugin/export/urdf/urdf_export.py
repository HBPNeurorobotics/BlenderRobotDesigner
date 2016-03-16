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
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#   2015        Stefan Ulbrich, Igor Peric, Maximilian Stauss
#                   Initial version of URDF support
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#   2016-02-05: Stefan Ulbrich (FZI), Export as ROS package and ZIP file option.
#
# ######

"""
:term:`Operators <operator>` (and functions) exporting to URDF. It supports the creation of ROS packages, zipped
ROS packages and 'plain' URDF files with absolute or relative file paths.

Note: modify :meth:`pyxb.binding.basis._TypeBinding_mixin.toxml` to call :meth:`xml.dom.minidom.Node.toprettyxml`

"""

# ######
# System imports
import os
from math import radians
import tempfile

# ######
# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty
from mathutils import Vector

# ######
# RobotDesigner imports
from .generic import urdf_tree
from .generic.helpers import list_to_string
from ...core import config, PluginManager, RDOperator
from ...operators.helpers import ModelSelected, ObjectMode
from ...operators.model import SelectModel


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
        directory = os.path.join(directory, "meshes")

    else:
        meshes = [obj.name for obj in bpy.data.objects if
                  obj.type == "MESH" and name == obj.name and
                  obj.RobotEditor.tag == "COLLISION"]
        directory = os.path.join(directory, "collisions")

    if not os.path.exists(directory):
        os.makedirs(directory)

    # There is max. 1 object in the list
    assert len(meshes) <= 1
    for mesh in meshes:
        operator.logger.debug("Processing mesh: %s", mesh)

        file_path = os.path.join(directory, mesh + '.dae')
        model_name = bpy.context.active_object.name
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects[mesh]
        bpy.context.active_object.select = True
        bpy.ops.wm.collada_export(
            filepath=file_path, selected=True, use_texture_copies=True)

        # quick fix for dispersed meshes
        # todo: find appropriate solution
        with open(file_path, "r") as file:
            lines = file.readlines()
        with open(file_path, "w") as file:
            for line in lines:
                if "matrix" not in line:
                    file.write(line)

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
                filepath: str, meshpath: str, toplevel_directory: str, in_ros_package: bool, abs_filepaths=False):
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
        trafo, dummy = segment.RobotEditor.getTransform()
        child.joint.origin.rpy = list_to_string(trafo.to_euler())
        child.joint.origin.xyz = list_to_string([i * j for i, j in zip(trafo.translation, blender_scale_factor)])
        child.joint.name = segment.name + '_joint'
        child.link.name = segment.name + '_link'
        if segment.RobotEditor.axis_revert:
            revert = -1
        else:
            revert = 1

        if segment.RobotEditor.axis == 'X':
            child.joint.axis.xyz = list_to_string(Vector((1, 0, 0)) * revert)
        elif segment.RobotEditor.axis == 'Y':
            child.joint.axis.xyz = list_to_string(Vector((0, 1, 0)) * revert)
        elif segment.RobotEditor.axis == 'Z':
            child.joint.axis.xyz = list_to_string(Vector((0, 0, 1)) * revert)

        if segment.parent is None:
            print("Debug: parent bone is none", segment,
                  segment.RobotEditor.jointMode)
            child.joint.type = 'fixed'
        else:
            if segment.RobotEditor.jointMode == 'REVOLUTE':
                child.joint.limit.lower = radians(
                    segment.RobotEditor.theta.min)
                child.joint.limit.upper = radians(
                    segment.RobotEditor.theta.max)
                child.joint.type = 'revolute'
            if segment.RobotEditor.jointMode == 'PRISMATIC':
                child.joint.limit.lower = segment.RobotEditor.d.min
                child.joint.limit.upper = segment.RobotEditor.d.max
                child.joint.type = 'prismatic'
            if segment.RobotEditor.jointMode == 'FIXED':
                child.joint.type = 'fixed'

        # Add properties
        connected_meshes = [mesh.name for mesh in bpy.data.objects if
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
            if visual_path:
                visual = child.add_mesh(visual_path,
                                        [i * j for i, j in zip(bpy.data.objects[mesh].scale, blender_scale_factor)])
                visual.origin.xyz = list_to_string(pose.translation)
                visual.origin.rpy = list_to_string(pose.to_euler())
            else:
                operator.logger.info("No visual model for: %s", mesh)

            collision_path = export_mesh(operator, context, mesh, meshpath, toplevel_directory,
                                         in_ros_package, abs_filepaths, export_collision=True)
            if collision_path:
                collision = child.add_collisionmodel(collision_path)
                collision.origin.xyz = list_to_string(pose.translation)
                collision.origin.rpy = list_to_string(pose.to_euler())
            else:
                operator.logger.info("No collision model for: %s", mesh)

        # todo: pick up the real values from Physics Frame?

        frame_names = [
            frame.name for frame in bpy.data.objects if frame.RobotEditor.tag == 'PHYSICS_FRAME']

        for frame in frame_names:
            # Add inertial definitions (for Gazebo)
            inertial = child.add_inertial()
            if bpy.data.objects[frame].parent_bone == segment.name:
                inertial.mass.value_ = bpy.data.objects[
                    frame].RobotEditor.dynamics.mass
                inertial.inertia.ixx = bpy.data.objects[
                    frame].RobotEditor.dynamics.inertiaTensor[0]
                inertial.inertia.iyy = bpy.data.objects[
                    frame].RobotEditor.dynamics.inertiaTensor[1]
                inertial.inertia.izz = bpy.data.objects[
                    frame].RobotEditor.dynamics.inertiaTensor[2]

        # add joint controllers
        if operator.gazebo and segment.RobotEditor.jointController.isActive is True:
            controller = child.add_joint_controller(root.control_plugin)
            controller.joint_name = segment.name
            controller.type = segment.RobotEditor.jointController.controllerType
            if segment.RobotEditor.jointController.P <= 1.0:
                segment.RobotEditor.jointController.P = 100
            controller.pid = list_to_string([segment.RobotEditor.jointController.P,
                                             segment.RobotEditor.jointController.I,
                                             segment.RobotEditor.jointController.D])

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
    root.write(filepath)

    # insert gazebo tags before "</robot>" tag
    if operator.gazebo:
        with open(filepath, "r") as f:
            content = f.read()
        gazebo_tags = bpy.context.scene.RobotEditor.gazeboTags
        content = content.replace("</robot>", gazebo_tags + "</robot>")
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

    operator.logger.debug('Exporting to: %s', toplevel_dir)
    robot_name = context.active_object.name

    target = os.path.join(toplevel_dir, robot_name + '_description')

    try:
        shutil.copytree(os.path.join(config.resource_path,
                                     'robot_name_description'), target)
    except FileExistsError:
        operator.logger.error('Attempted to overwrite existing package')
        operator.report({'ERROR'}, 'File %s exists' % target)

    for dname, dirs, files in os.walk(target, topdown=False):
        for dir in [i for i in dirs if "robot_name" in i]:
            os.rename(os.path.join(dname, dir),
                      os.path.join(dname, dir.replace("robot_name", robot_name)))

        for fname in files:
            operator.logger.debug('File: %s, %s, %s, %s',
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
    bl_label = "Export zipped ROS/URDF Package"

    filter_glob = StringProperty(
        default="*.zip",
        options={'HIDDEN'},
    )

    filepath = StringProperty(name="Filename", subtype='FILE_PATH')
    gazebo = BoolProperty(name="Export Gazebo tags", default=True)

    package_url = BoolProperty(name="Package URL", default=True)
    abs_file_path = BoolProperty(name="Absolute Filepaths", default=False)

    base_link_name = StringProperty(name="Base link:", default="root_link")

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

        target = tempfile.TemporaryDirectory()
        create_package(self, context, target.name, self.base_link_name)

        with zipfile.ZipFile(self.filepath, 'w') as zipf:
            zipdir(target.name, zipf)

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
    bl_label = "Export ROS/URDF Package"

    directory = StringProperty(
        name="Mesh directory", subtype='DIR_PATH', default="")
    gazebo = BoolProperty(name="Export Gazebo tags", default=True)

    package_url = BoolProperty(name="Package URL", default=True)
    abs_file_path = BoolProperty(name="Absolute Filepaths", default=False)
    base_link_name = StringProperty(name="Base link:", default="root_link")

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
    bl_label = "Export plain URDF"

    filter_glob = StringProperty(
        default="*.urdf",
        options={'HIDDEN'},
    )

    abs_file_paths = BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo = BoolProperty(name="Export Gazebo tags", default=True)
    filepath = StringProperty(name="Filename", subtype='FILE_PATH')
    base_link_name = StringProperty(name="Base link:", default="root_link")

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
