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

# System imports
import os
from math import *
from mathutils import Euler, Matrix, Vector
from pathlib import Path

# Blender imports
import bpy
from bpy.props import StringProperty

# RobotDesigner imports
from ...core import config, PluginManager, Condition, RDOperator
from ...core.logfile import export_logger
from ...operators.helpers import ModelSelected, ObjectMode
from ...operators.segments import SelectSegment, CreateNewSegment, UpdateSegments
from ...operators.model import SelectModel, CreateNewModel, SelectCoordinateFrame
from ...operators.rigid_bodies import SelectGeometry, AssignGeometry
from ...operators.dynamics import AssignPhysical, CreatePhysical, SelectPhysical

# URDF-specific imports
from .generic import urdf_tree

from .generic.helpers import string_to_list, get_value

from ...properties.globals import global_properties


__author__ = 'Stefan Ulbrich(FZI), Igor Peric (FZI), Maximillian Stauss (FZI)'


class Importer(object):
    PACKAGE_URL = 'package://'
    FILE_URL_RELATIVE = 'model://'
    FILE_URL_ABSOLUTE = 'file:///'

    def __init__(self, operator: RDOperator, file_path: str, base_dir = ""):
        self.file_path = file_path
        if base_dir:
            self.base_dir = base_dir
        else:
            self.base_dir = os.path.dirname(file_path)
        export_logger = operator.logger
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

    export_logger.info("base dir: {}".format(self.base_dir))
    export_logger.info("mesh url: {}".format(mesh_url))

    # check for absolute file path
    if mesh_url.startswith(self.FILE_URL_ABSOLUTE):
        mesh_path = mesh_url.replace(self.FILE_URL_ABSOLUTE, '')
    elif mesh_url.startswith(self.FILE_URL_RELATIVE) or mesh_url.startswith(self.PACKAGE_URL):
        mesh_path = mesh_url.replace(self.FILE_URL_RELATIVE, '').replace(self.PACKAGE_URL, '')
        mesh_path = os.path.join(str(Path(self.base_dir).parent), mesh_path)
    else:
        self.operator.report({'ERROR'}, "Unsupported URL schema")
        export_logger.error("Unsupported URL schema")
        return

    model_name = bpy.context.active_object.name
    # bpy.context.active_object.type = 'ARMATURE'
    model_type = bpy.context.active_object.type

    export_logger.debug('model_name (geometry): {}'.format(model_name))
    export_logger.debug('model_type (geometry): {}'.format(model_type))

    fn, extension = os.path.splitext(mesh_path)
    if extension == ".stl" or extension == ".STL":
        try:
            bpy.ops.import_mesh.stl(filepath=mesh_path)
        except:
            pass
    elif extension == ".dae" or extension == ".DAE":
        try:
            export_logger.info("mesh file: {}".format(mesh_path))
            bpy.ops.wm.collada_import(filepath=mesh_path, import_units=True)
        except:
            pass

    bpy.context.active_object.RobotDesigner.fileName = os.path.basename(os.path.splitext(mesh_path)[0])

    scale_factor = string_to_list(model.geometry.mesh.scale)
    scale_matrix = Matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                           [0, 0, 1, 0], [0, 0, 0, 1]])
    # scale_matrix = Matrix([[scale_factor[0], 0, 0, 0], [0, scale_factor[1], 0, 0],
    #                        [0, 0, scale_factor[2], 0], [0, 0, 0, 1]])

    return Matrix.Translation(Vector(string_to_list(model.origin.xyz))) * \
           Euler(string_to_list(model.origin.rpy), 'XYZ').to_matrix().to_4x4() * scale_matrix


def parse(self, node: urdf_tree.URDFTree, parent_name = ""):
    """
    Recursively parses the URDF tree elements.

    :param node: The actual segment
    :param parent_name: Name of the parent segment (if None the segment is a root element)
    """

    C = bpy.context

    export_logger.info("parent name: {}".format( parent_name))
    # export_logger.debug('active bone name : {}'.format(C.active_bone.name))
    export_logger.debug('active object name (parse): {}'.format(C.active_object.name))

    export_logger.debug('active object type (parse): {}'.format(C.active_object.type))

    if bpy.context.active_object:
        export_logger.debug('active object type == Armature: {}, {}'.format(bpy.context.active_object.type == 'ARMATURE',
                      "Model not selected and active."))
    else:
        export_logger.debug('active object type == Armature: {}, {}'.format(False, "No model selected"))

    SelectSegment.run(segment_name=parent_name)

    CreateNewSegment.run(segment_name=node.joint.name)
    segment_name = C.active_bone.name
    export_logger.info("{} -> {}".format(parent_name, segment_name))

    xyz = string_to_list(get_value(node.joint.origin.xyz, "0 0 0"))
    euler = string_to_list(get_value(node.joint.origin.rpy, '0 0 0'))

    if segment_name in self.controllers:
        controller = self.controllers[segment_name]
        PID = controller.pid.split(" ")
        bpy.context.active_bone.RobotDesigner.jointController.isActive = True
        bpy.context.active_bone.RobotDesigner.jointController.controllerType = controller.type
        bpy.context.active_bone.RobotDesigner.jointController.P = float(PID[0])
        bpy.context.active_bone.RobotDesigner.jointController.I = float(PID[1])
        bpy.context.active_bone.RobotDesigner.jointController.D = float(PID[2])

    axis = string_to_list(node.joint.axis.xyz)
    for i, element in enumerate(axis):
        if element == -1.0:
            bpy.context.active_bone.RobotDesigner.axis_revert = True
            axis[i] = 1.0

    if axis == [1.0, 0.0, 0.0]:
        bpy.context.active_bone.RobotDesigner.axis = 'X'
    elif axis == [0.0, 1.0, 0.0]:
        bpy.context.active_bone.RobotDesigner.axis = 'Y'
    elif axis == [0.0, 0.0, 1.0]:
        bpy.context.active_bone.RobotDesigner.axis = 'Z'
    else:
        # todo throw exception -- only main axes are supported. Add a limitations section to documentation
        # (which has to be created as well)!
        pass

    bpy.context.active_bone.RobotDesigner.Euler.x.value = xyz[0]
    bpy.context.active_bone.RobotDesigner.Euler.y.value = xyz[1]
    bpy.context.active_bone.RobotDesigner.Euler.z.value = xyz[2]

    bpy.context.active_bone.RobotDesigner.Euler.alpha.value = round(degrees(euler[0]), 0)
    bpy.context.active_bone.RobotDesigner.Euler.beta.value = round(degrees(euler[1]), 0)
    bpy.context.active_bone.RobotDesigner.Euler.gamma.value = round(degrees(euler[2]), 0)

    if node.joint.dynamics:
        bpy.context.active_bone.RobotDesigner.controller.maxVelocity = float(
            node.joint.limit.velocity)
        # bpy.context.active_bone.RobotDesigner.controller.maxVelocity = float(tree.joint.limit.friction)

    if node.joint.type == 'revolute':
        bpy.context.active_bone.RobotDesigner.jointMode = 'REVOLUTE'
        bpy.context.active_bone.RobotDesigner.theta.max = degrees(float(get_value(node.joint.limit.upper, 0)))
        bpy.context.active_bone.RobotDesigner.theta.min = degrees(float(get_value(node.joint.limit.lower, 0)))
    if node.joint.type == 'prismatic':
        bpy.context.active_bone.RobotDesigner.jointMode = 'PRISMATIC'
        if node.joint.limit is not None:
            bpy.context.active_bone.RobotDesigner.d.max = float(get_value(node.joint.limit.upper, 0))
            bpy.context.active_bone.RobotDesigner.d.min = float(get_value(node.joint.limit.lower, 0))

    if node.joint.type == 'fixed':
        bpy.context.active_bone.RobotDesigner.jointMode = 'FIXED'

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

            # get mass
            bpy.data.objects[node.link.name].RobotDesigner.dynamics.mass = inertia.mass.value_

            # get inertia
            bpy.data.objects[node.link.name].RobotDesigner.dynamics.inertiaXX = i.ixx
            bpy.data.objects[node.link.name].RobotDesigner.dynamics.inertiaXY = i.ixy
            bpy.data.objects[node.link.name].RobotDesigner.dynamics.inertiaXZ = i.ixz
            bpy.data.objects[node.link.name].RobotDesigner.dynamics.inertiaYY = i.iyy
            bpy.data.objects[node.link.name].RobotDesigner.dynamics.inertiaYZ = i.iyz
            bpy.data.objects[node.link.name].RobotDesigner.dynamics.inertiaZZ = i.izz

            # get inertia pose
            try:
                bpy.data.objects[node.link.name].RobotDesigner.dynamics.inertiaTrans = string_to_list(origin.xyz)
                bpy.data.objects[node.link.name].RobotDesigner.dynamics.inertiaRot = string_to_list(origin.rpy)
            except:
                pass

    model = bpy.context.active_object
    model_name = model.name

    pose_bone = bpy.context.active_object.pose.bones[segment_name]
    segment_world = model.matrix_world * pose_bone.matrix

    export_logger.debug("[COLLISION] parsed: " + str(len(list(node.link.collision))) + " collision meshes.")

    # Iterate first over visual models then over collision models
    VISUAL, COLLISON = 0, 1
    for model_type, geometric_models in enumerate((node.link.visual, node.link.collision)):
        # Iterate over the geometric models that are declared for the link
        for nr, model in enumerate(geometric_models):
            # geometry is not optional in the xml
            if model.geometry.mesh is not None:

                trafo_urdf = self.import_geometry(model)
                # export_logger.debug("Trafo: \n{}".format(trafo_urdf))
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
                    # export_logger.debug("Scale: {}, {}, Matrix world: \n{}".format(scale_urdf, scale_object,
                    #              bpy.context.active_object.matrix_world))

                    # if the loop continues the name will be suffixed by a number

                    export_logger.info("Model type: {}".format(str(model_type)))
                    # Remove multiple "COL_" and "VIS_" strings before renaming
                    if model_type == COLLISON:
                        # %2d changed to %d because it created unwanted space with one digit numbers
                        if not node.link.name.startswith("COL_"):
                            bpy.context.active_object.name = "COL_%{}".format(node.link.name)
                        else:
                            bpy.context.active_object.name = "{}".format(node.link.name)
                        bpy.context.active_object.RobotDesigner.tag = 'COLLISION'
                    else:
                        if not node.link.name.startswith("VIS_"):
                            bpy.context.active_object.name = "VIS_{}".format(node.link.name)
                        else:
                            bpy.context.active_object.name = "{}".format(node.link.name)

                    if not node.link.name.endswith("_" + str(nr)) and nr != 0:
                        bpy.context.active_object.name = "{}_{}".format(bpy.context.active_object.name, nr)

                    # remove spaces from link name
                    bpy.context.active_object.name = bpy.context.active_object.name.replace(" ", "")

                    # The name might be altered by blender
                    assigned_name = bpy.context.active_object.name

                    bpy.ops.object.transform_apply(location=False,
                                               rotation=False,
                                               scale=True)
                    SelectModel.run(model_name=model_name)
                    SelectSegment.run(segment_name=segment_name)
                    SelectGeometry.run(geometry_name=assigned_name)
                    AssignGeometry.run()

                    # scale geometry
                    if model.geometry.mesh.scale == []:
                        scale_factor = [1, 1, 1]
                    else:
                        scale_factor = string_to_list(model.geometry.mesh.scale)

                    bpy.data.objects[global_properties.mesh_name.get(bpy.context.scene)].scale = scale_factor

            else:
                export_logger.error("Mesh file not found")
                pass

    for sub_tree in node.children:
        self.parse(sub_tree, segment_name)
    return segment_name


def import_file(self):
    robot_name, root_links, kinematic_chains, self.controllers, gazebo_tags = \
        urdf_tree.URDFTree.parse(self.file_path)

    export_logger.debug("{} ,{}".format(self.base_dir, self.file_path))
    # store gazebo tags
    tag_buffer = ''
    export_logger.debug('Processing {0} tags.'.format(len(gazebo_tags)))
    for gazebo_tag in gazebo_tags:
        curr_tag = gazebo_tag.toxml("utf-8").decode("utf-8")
        curr_tag = curr_tag[38:]  # remove <xml version=.../> tag
        tag_buffer = '{0}\n{1}'.format(tag_buffer, curr_tag)
    global_properties.gazebo_tags.set(bpy.context.scene, tag_buffer)

    export_logger.debug('root links: {}'.format([i.name for i in root_links]))

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

    # bpy.ops.view3d.view_lock_to_active()
    bpy.context.active_object.show_x_ray = True


def import_package(self):
    """
    Searches in the top level directories of the :attr:`file_path` for a ``package.xml``. This path is used
    as base path for finding models.
    """

    import os
    package_dir = os.path.dirname(self.file_path)
    if not package_dir:
        export_logger.error("No path to file given")
        return

    while not os.path.exists(os.path.join(package_dir, "package.xml")):
        export_logger.debug("{}".format(package_dir))
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
    bl_label = "Import URDF - ROS package"

    filepath: StringProperty(name="Filename", subtype='FILE_PATH')

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
    bl_label = "Import URDF - ROS zipped package"

    filepath: StringProperty(name="Filename", subtype='FILE_PATH')

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
                export_logger.debug("{}, {}, {}, {}".format(root, subFolders, files, [os.path.splitext(i) for i in files]))
                for i in files:
                    if '.urdf' == os.path.splitext(i)[1]:
                        if file_path:
                            self.report({"INFO"}, "Multiple URDF in zip. Choosing: {}".format(i))
                        file_path = os.path.join(root, i)

            if file_path:
                export_logger.debug("Importing: {}".format(file_path))
                importer = Importer(operator=self, file_path=file_path)
                importer.import_package()
            else:
                self.report({'ERROR'}, "No URDF file found in package")
                export_logger.error("No URDF file found in package")

        return {'FINISHED'}


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportPlain(RDOperator):
    """
    :term:`Operator<operator>` for importing a robot from a ROS package (URDF)
    """

    # Obligatory class attributes
    bl_idname = config.OPERATOR_PREFIX + "import_urdf_plain"
    bl_label = "Import URDF - plain"

    filepath: StringProperty(name="Filename", subtype='FILE_PATH')

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
        #     export_logger.debug("Checking ROS_PACKAGE_PATH:")
        #     export_logger.debug(ros_pkg_paths)
        #     for path in ros_pkg_paths:
        #         probe_path = os.path.join(path, mesh_filename)
        #         export_logger.debug("Checking path: {}".format(probe_path))
        #         if os.path.exists(probe_path):
        #             prefix_folder = path
        #             export_logger.debug("Prefix path found: {}".format(prefix_folder))
        #             break
        #     if prefix_folder == "":
        #         export_logger.debug(
        #                 "Warning! Couldn't load file relative to ROS_PACKAGE_PATH environment variable.")
        #         prefix_folder = os.path.dirname(self.file_path)
        #         if prefix_folder.split("/").pop() == mesh_filename.split("/")[
        #             0]:
        #             prefix_folder = '/' + '/'.join(
        #                     prefix_folder.split("/")[1:-1])
