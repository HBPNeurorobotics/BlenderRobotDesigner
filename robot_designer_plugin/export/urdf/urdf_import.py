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
#
# ######
"""
The module that encapsulates all blender calls and offers the importer and exporter for the RobotDesigner
"""

# ######
# System imports
import os
from math import *
from mathutils import Euler, Matrix, Vector

# ######
# Blender imports
import bpy
from bpy.props import StringProperty

# ######
# RobotDesigner imports
from ...core import config, PluginManager, Condition, RDOperator
from ...operators.helpers import ModelSelected, ObjectMode

from ...operators.segments import SelectSegment, CreateNewSegment, UpdateSegments
from ...operators.model import SelectModel, CreateNewModel, SelectCoordinateFrame
from ...operators.rigid_bodies import SelectGeometry, AssignGeometry
from ...operators.dynamics import AssignPhysical, CreatePhysical, SelectPhysical
# ######
# URDF-specific imports

from .generic import urdf_tree
from .generic.helpers import string_to_list, get_value

import logging

__author__ = 'Stefan Ulbrich(FZI), Igor Peric (FZI), Maximillian Stauss (FZI)'


class Importer(object):
    PACKAGE_URL = 'package://'
    FILE_URL_RELATIVE = 'file://'
    FILE_URL_ABSOLUTE = 'file:///'

    def __init__(self, operator: RDOperator, file_path: str, base_dir=""):
        self.file_path = file_path
        if base_dir:
            self.base_dir = base_dir
        else:
            self.base_dir = os.path.dirname(file_path)
        self.logger = operator.logger
        self.operator = operator
        self.controllers = None

    def import_geometry(self, model):
        """
        Adds a geometry to the blender scene. Uses the self.file_name variable of the parenting context
        :param model: A urdf_dom.visual object.
        :return: Returns the transformation in the origin element (a 4x4 blender matrix).
        """

        # determine prefix path for loading meshes in case of paths relative to ROS_PACKAGE_PATH
        prefix_folder = ""
        mesh_url = model.geometry.mesh.filename

        # check for absolute file path
        if mesh_url.startswith(self.FILE_URL_ABSOLUTE):
            mesh_path = mesh_url.replace(self.FILE_URL_ABSOLUTE, '')
        elif mesh_url.startswith(self.FILE_URL_RELATIVE) or mesh_url.startswith(self.PACKAGE_URL):
            mesh_path = mesh_url.replace(self.FILE_URL_RELATIVE, '').replace(self.PACKAGE_URL, '')
            mesh_path = os.path.join(self.base_dir, mesh_path)
        else:
            self.operator.report({'ERROR'}, "Unsupported URL schema")
            self.logger.error("Unsupported URL schema")
            return

        fn, extension = os.path.splitext(mesh_path)
        if extension == ".stl":
            bpy.ops.import_mesh.stl(filepath=mesh_path)
        elif extension == ".dae":
            bpy.ops.wm.collada_import(filepath=mesh_path, import_units=True)

        bpy.context.active_object.RobotEditor.fileName = os.path.basename(os.path.splitext(mesh_path)[0])

        scale_factor = string_to_list(model.geometry.mesh.scale)
        scale_matrix = Matrix([[scale_factor[0], 0, 0, 0], [0, scale_factor[1], 0, 0],
                               [0, 0, scale_factor[2], 0], [0, 0, 0, 1]])

        return Matrix.Translation(Vector(string_to_list(model.origin.xyz))) * \
               Euler(string_to_list(model.origin.rpy), 'XYZ').to_matrix().to_4x4() * scale_matrix

    def parse(self, node: urdf_tree.URDFTree, parent_name=""):
        """
        Recursively parses the URDF tree elements.

        :param node: The actual segment
        :param parent_name: Name of the parent segment (if None the segment is a root element)
        """

        C = bpy.context

        SelectSegment.run(segment_name=parent_name)

        CreateNewSegment.run(segment_name=node.joint.name)
        segment_name = C.active_bone.name
        self.logger.info("%s -> %s", parent_name, segment_name)

        xyz = string_to_list(get_value(node.joint.origin.xyz, "0 0 0"))
        euler = string_to_list(get_value(node.joint.origin.rpy, '0 0 0'))

        if segment_name in self.controllers:
            controller = self.controllers[segment_name]
            PID = controller.pid.split(" ")
            bpy.context.active_bone.RobotEditor.jointController.isActive = True
            bpy.context.active_bone.RobotEditor.jointController.controllerType = controller.type
            bpy.context.active_bone.RobotEditor.jointController.P = float(PID[0])
            bpy.context.active_bone.RobotEditor.jointController.I = float(PID[1])
            bpy.context.active_bone.RobotEditor.jointController.D = float(PID[2])

        axis = string_to_list(node.joint.axis.xyz)
        for i, element in enumerate(axis):
            if element == -1.0:
                bpy.context.active_bone.RobotEditor.axis_revert = True
                axis[i] = 1.0

        if axis == [1.0, 0.0, 0.0]:
            bpy.context.active_bone.RobotEditor.axis = 'X'
        elif axis == [0.0, 1.0, 0.0]:
            bpy.context.active_bone.RobotEditor.axis = 'Y'
        elif axis == [0.0, 0.0, 1.0]:
            bpy.context.active_bone.RobotEditor.axis = 'Z'
        else:
            # todo throw exception -- only main axes are supported. Add a limitations section to documentation
            # (which has to be created as well)!
            pass

        bpy.context.active_bone.RobotEditor.Euler.x.value = xyz[0]
        bpy.context.active_bone.RobotEditor.Euler.y.value = xyz[1]
        bpy.context.active_bone.RobotEditor.Euler.z.value = xyz[2]

        bpy.context.active_bone.RobotEditor.Euler.alpha.value = round(degrees(euler[0]), 0)
        bpy.context.active_bone.RobotEditor.Euler.beta.value = round(degrees(euler[1]), 0)
        bpy.context.active_bone.RobotEditor.Euler.gamma.value = round(degrees(euler[2]), 0)

        if node.joint.dynamics:
            bpy.context.active_bone.RobotEditor.controller.maxVelocity = float(
                    node.joint.limit.velocity)
            # bpy.context.active_bone.RobotEditor.controller.maxVelocity = float(tree.joint.limit.friction)

        if node.joint.type == 'revolute':
            bpy.context.active_bone.RobotEditor.jointMode = 'REVOLUTE'
            bpy.context.active_bone.RobotEditor.theta.max = degrees(float(get_value(node.joint.limit.upper, 0)))
            bpy.context.active_bone.RobotEditor.theta.min = degrees(float(get_value(node.joint.limit.lower, 0)))
        if node.joint.type == 'prismatic':
            bpy.context.active_bone.RobotEditor.jointMode = 'PRISMATIC'
            if node.joint.limit is not None:
                bpy.context.active_bone.RobotEditor.d.max = float(get_value(node.joint.limit.upper, 0))
                bpy.context.active_bone.RobotEditor.d.min = float(get_value(node.joint.limit.lower, 0))

        if node.joint.type == 'fixed':
            bpy.context.active_bone.RobotEditor.jointMode = 'FIXED'

        # todo set the dynamics properties
        if node.link.inertial is not None:
            for inertia in node.link.inertial:
                # dynamics is not associated to a bone!
                origin = inertia.origin
                i = inertia.inertia

                CreatePhysical.run(frameName=node.link.name)
                SelectPhysical.run(frameName=node.link.name)
                SelectSegment.run(segment_name=node.joint.name)
                AssignPhysical.run()

                bpy.data.objects[node.link.name].RobotEditor.dynamics.mass = inertia.mass.value_

                if i.ixy != 0 or i.ixz != 0 or i.iyz != 0:
                    self.operator.report({'ERROR'}, 'Only diogonal inertia matrices currently supported')
                    self.logger.error('Only diogonal inertia matrices currently supported')

                matrix = [i.ixx, i.iyy, i.izz]

                bpy.data.objects[node.link.name].RobotEditor.dynamics.inertiaTensor = matrix

        model = bpy.context.active_object
        model_name = model.name

        pose_bone = bpy.context.active_object.pose.bones[segment_name]
        segment_world = model.matrix_world * pose_bone.matrix

        self.logger.debug("[COLLISION] parsed: " + str(len(list(node.link.collision))) + " collision meshes.")

        # Iterate first over visual models then over collision models
        VISUAL, COLLISON = 0, 1
        for model_type, geometric_models in enumerate((node.link.visual, node.link.collision)):
            # Iterate over the geometric models that are declared for the link
            for nr, model in enumerate(geometric_models):
                # geometry is not optional in the xml
                if model.geometry.mesh is not None:

                    trafo_urdf = self.import_geometry(model)
                    # self.logger.debug("Trafo: \n%s", trafo_urdf)
                    # URDF (the import in ROS) exhibits a strange behavior:
                    # If there is a transformation preceding the mesh in a .dae file, only the scale is
                    # extracted and the rest is omitted. Therefore, we store the scale after import and
                    # multiply it to the scale given in the xml attribute.

                    # if there are multiple objects in the COLLADA file, they will be selected
                    selected_objects = [i for i in bpy.context.selected_objects]
                    for object in selected_objects:
                        bpy.context.scene.objects.active = object  # bpy.data.objects[object]
                        bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")

                    for object in selected_objects:

                        if object.type != 'MESH':
                            continue

                        # Select the object (and deselect others)
                        bpy.ops.object.select_all(False)
                        bpy.context.scene.objects.active = object  # bpy.data.objects[object]
                        bpy.context.active_object.select = True
                        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                        bpy.context.active_object.matrix_world = segment_world * trafo_urdf * \
                                                                 bpy.context.active_object.matrix_world

                        # # Can be removed once collada import has been proven to be stable
                        # scale_object = bpy.context.active_object.scale
                        # scale_matrix = Matrix([[scale_urdf[0] * scale_object[0], 0, 0, 0],
                        #                 [0, scale_urdf[1] * scale_object[1], 0, 0],
                        #                 [0, 0, scale_urdf[2] * scale_object[2], 0], [0, 0, 0, 1]])
                        # bpy.context.active_object.matrix_world = bone_transformation * trafo_urdf * scale_matrix
                        # self.logger.debug("Scale: %s,%s, Matrix world: \n%s", scale_urdf, scale_object,
                        #              bpy.context.active_object.matrix_world)

                        # if the loop continues the name will be suffixed by a number

                        self.logger.info("Model type: " + str(model_type))
                        # Remove multiple "COL_" and "VIS_" strings before renaming
                        if model_type == COLLISON:
                            # %2d changed to %d because it created unwanted space with one digit numbers
                            bpy.context.active_object.name = "COL_%s_%d" % (node.link.name, nr)
                            bpy.context.active_object.RobotEditor.tag = 'COLLISION'
                        else:
                            bpy.context.active_object.name = "VIZ_%s_%d" % (node.link.name, nr)

                        # remove spaces from link name
                        bpy.context.active_object.name = bpy.context.active_object.name.replace(" ", "")

                        # The name might be altered by blender
                        assigned_name = bpy.context.active_object.name

                        bpy.ops.object.transform_apply(location=False,
                                                       rotation=False,
                                                       scale=True)
                        SelectModel.run(model_name=model_name)
                        SelectSegment.run(segment_name=segment_name)
                        SelectGeometry.run(mesh_name=assigned_name)
                        AssignGeometry.run()
                else:
                    self.logger.error("Mesh file not found")
                    pass

        for sub_tree in node.children:
            self.parse(sub_tree, segment_name)
        return segment_name

    def import_file(self):
        robot_name, root_links, kinematic_chains, self.controllers, gazebo_tags = \
            urdf_tree.URDFTree.parse(self.file_path)

        self.logger.debug("%s,%s", self.base_dir, self.file_path)
        # store gazebo tags
        tag_buffer = ''
        self.logger.debug('Processing {0} tags.'.format(len(gazebo_tags)))
        for gazebo_tag in gazebo_tags:
            curr_tag = gazebo_tag.toxml("utf-8").decode("utf-8")
            curr_tag = curr_tag[38:]  # remove <xml version=.../> tag
            tag_buffer = '{0}\n{1}'.format(tag_buffer, curr_tag)
        bpy.context.scene.RobotEditor.gazeboTags = tag_buffer

        self.logger.debug('root links: %s', [i.name for i in root_links])

        CreateNewModel.run(model_name=robot_name, base_segment_name="")
        model_name = bpy.context.active_object.name

        SelectModel.run(model_name=model_name)
        for link in root_links:
            for visual in link.visual:
                if visual.geometry.mesh is not None:
                    trafo = self.import_geometry(visual)
                    s1 = string_to_list(visual.geometry.mesh.scale)
                    s2 = bpy.context.active_object.scale
                    scale = Matrix([[s1[0] * s2[0], 0, 0, 0], [0, s1[1] * s2[1], 0, 0],
                                    [0, 0, s1[2] * s2[2], 0], [0, 0, 0, 1]])
                    bpy.context.active_object.matrix_world = trafo * scale

        for chain in kinematic_chains:
            root_name = self.parse(chain)
            UpdateSegments.run(segment_name=root_name, recurse=True)

        try:
            SelectCoordinateFrame.run(mesh_name='CoordinateFrame')
        except:
            pass

        bpy.ops.view3d.view_lock_to_active()
        bpy.context.active_object.show_x_ray = True

    def import_package(self):
        """
        Searches in the top level directories of the :attr:`file_path` for a ``package.xml``. This path is used
        as base path for finding models.
        """

        import os
        package_dir = os.path.dirname(self.file_path)
        if not package_dir:
            self.logger.error("No path to file given")
            return

        while not os.path.exists(os.path.join(package_dir, "package.xml")):
            self.logger.debug("%s",package_dir)
            package_dir = os.path.dirname(package_dir)

        self.base_dir = os.path.dirname(package_dir)
        return self.import_file()


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportPackage(RDOperator):
    """
    :term:`Operator<operator>` for importing a robot from a ROS package (URDF)
    """

    # Obligatory class attributes
    bl_idname = config.OPERATOR_PREFIX + "import_urdf_package"
    bl_label = "URDF import (ROS package)"

    filepath = StringProperty(name="Filename", subtype='FILE_PATH')

    # directory = StringProperty(
    #        name="Mesh directory", subtype='DIR_PATH', default="")

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        importer = Importer(operator=self, file_path=self.filepath)
        importer.import_package()
        return {'FINISHED'}


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportZippedPackage(RDOperator):
    """
    :term:`Operator<operator>` for importing a robot from a ROS package (URDF)
    """

    # Obligatory class attributes
    bl_idname = config.OPERATOR_PREFIX + "import_urdf_zipped_package"
    bl_label = "URDF import (zipped ROS package)"

    filepath = StringProperty(name="Filename", subtype='FILE_PATH')

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        import zipfile
        import tempfile

        with tempfile.TemporaryDirectory() as target:
            with zipfile.ZipFile(self.filepath, "r") as z:
                z.extractall(target)

            file_path = ""
            for root, subFolders, files in os.walk(target):
                self.logger.debug("%s,%s,%s,%s", root,subFolders,files,[os.path.splitext(i) for i in files])
                for i in files:
                    if '.urdf' == os.path.splitext(i)[1]:
                        if file_path:
                            self.report({"INFO"},"Multiple URDF in zip. Choosing: %s", i)
                        file_path = os.path.join(root,i)

            if file_path:
                self.logger.debug("Importing: %s", file_path)
                importer = Importer(operator=self, file_path=file_path)
                importer.import_package()
            else:
                self.report({'ERROR'}, "No URDF file found in package")
                self.logger.error("No URDF file found in package")

        return {'FINISHED'}


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportPlain(RDOperator):
    """
    :term:`Operator<operator>` for importing a robot from a ROS package (URDF)
    """

    # Obligatory class attributes
    bl_idname = config.OPERATOR_PREFIX + "import_urdf_plain"
    bl_label = "URDF import (plain file)"

    filepath = StringProperty(name="Filename", subtype='FILE_PATH')

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        import os
        importer = Importer(self, self.filepath)
        importer.import_file()
        return {'FINISHED'}

        # Code for looking up ROS packages via environment variables:

        # ros_pkg_paths = os.environ.get("ROS_PACKAGE_PATH")
        # if ros_pkg_paths is not None and \
        #         mesh_filename.startswith(
        #                 "package://") or mesh_filename.startswith("model://"):
        #     mesh_filename = mesh_filename.replace("package://", "").replace(
        #             "model://", "")
        #     ros_pkg_paths = ros_pkg_paths.split(":")
        #     self.logger.debug("Checking ROS_PACKAGE_PATH:")
        #     self.logger.debug(ros_pkg_paths)
        #     for path in ros_pkg_paths:
        #         probe_path = os.path.join(path, mesh_filename)
        #         self.logger.debug("Checking path: " + probe_path)
        #         if os.path.exists(probe_path):
        #             prefix_folder = path
        #             self.logger.debug("Prefix path found: " + prefix_folder)
        #             break
        #     if prefix_folder == "":
        #         self.logger.debug(
        #                 "Warning! Couldn't load file relative to ROS_PACKAGE_PATH environment variable.")
        #         prefix_folder = os.path.dirname(self.file_path)
        #         if prefix_folder.split("/").pop() == mesh_filename.split("/")[
        #             0]:
        #             prefix_folder = '/' + '/'.join(
        #                     prefix_folder.split("/")[1:-1])
