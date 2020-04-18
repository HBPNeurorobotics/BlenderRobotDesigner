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
# ######


# ######
# System imports
import os
import sys
from math import *
from mathutils import Euler, Matrix, Vector
from pathlib import Path
# ######
# Blender imports
import bpy
from bpy.props import StringProperty

from ..osim.osim_import import OsimImporter
from ...core.config import PLUGIN_PREFIX

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

from .generic import sdf_tree
from .generic.helpers import string_to_list, get_value, get_list_value, rounded, inverse_matrix, pose_float2homogeneous, \
    pose2origin, homo2origin, pose_modelpose

from ...properties.globals import global_properties

import logging

# model.config file reading
from .generic import model_config_dom, robot_model_config_dom

__author__ = 'Benedikt Feldotto(TUM), Guang Chen(TUM), Stefan Ulbrich(FZI)'


class Importer(object):
    PACKAGE_URL = 'package://'
    FILE_URL_RELATIVE = 'model://'
    FILE_URL_ABSOLUTE = 'file:///'
    MUSCLE_PATH = ''

    def __init__(self, operator: RDOperator, file_path: str, base_dir = ""):
        self.file_path = file_path
        if base_dir:
            self.base_dir = base_dir
        else:
            self.base_dir = os.path.dirname(file_path)
        self.logger = operator.logger
        self.operator = operator
        self.controllers = None

    def add_box(self, model):
        """
        This function takes inputs and returns vertex and face arrays.
        no actual mesh data creation is done here.
        """
        width = model.geometry[0].cylinder[0].size[0][0]
        depth = model.geometry[0].cylinder[0].size[0][1]
        height = model.geometry[0].cylinder[0].size[0][2]
        verts = [(+1.0, +1.0, -1.0),
                 (+1.0, -1.0, -1.0),
                 (-1.0, -1.0, -1.0),
                 (-1.0, +1.0, -1.0),
                 (+1.0, +1.0, +1.0),
                 (+1.0, -1.0, +1.0),
                 (-1.0, -1.0, +1.0),
                 (-1.0, +1.0, +1.0),
                 ]

        faces = [(0, 1, 2, 3),
                 (4, 7, 6, 5),
                 (0, 4, 5, 1),
                 (1, 5, 6, 2),
                 (2, 6, 7, 3),
                 (4, 0, 3, 7),
                 ]

        # apply size
        for i, v in enumerate(verts):
            verts[i] = v[0] * width, v[1] * depth, v[2] * height

        return verts, faces


    def import_box(self, model, type):
        """
        Adds a box with radius 0.5 to the blender scene. Uses the self.file_name variable of the parenting context
        The correct lengths are adjusted later together with the scaling
        :param model: A sdf_dom.visual object.
        :param type: COLLISION or VISUAL. COLLISION = 1. VISUAL = 0
        :return: Returns the transformation in the origin element (a 4x4 blender matrix).
        """

        # determine prefix path for loading meshes in case of paths relative to ROS_PACKAGE_PATH
        prefix_folder = ""
        self.logger.debug('model_geometry_bbox: %s', model.geometry[0].box[0].size[0])
        # Previous method for making a box. While it has its uses, for simple box creation, not needed.
        '''
        width = string_to_list(model.geometry[0].box[0].size[0])[0] / 2
        depth = string_to_list(model.geometry[0].box[0].size[0])[1] / 2
        height = string_to_list(model.geometry[0].box[0].size[0])[2] / 2
        verts = [(+1.0, +1.0, -1.0),
                 (+1.0, -1.0, -1.0),
                 (-1.0, -1.0, -1.0),
                 (-1.0, +1.0, -1.0),
                 (+1.0, +1.0, +1.0),
                 (+1.0, -1.0, +1.0),
                 (-1.0, -1.0, +1.0),
                 (-1.0, +1.0, +1.0),
                 ]

        faces = [(0, 1, 2, 3),
                 (4, 7, 6, 5),
                 (0, 4, 5, 1),
                 (1, 5, 6, 2),
                 (2, 6, 7, 3),
                 (4, 0, 3, 7),
                 ]

        # apply size
        for i, v in enumerate(verts):
            verts[i] = v[0] * (width), v[1] * (depth), v[2] * (height)

        mesh_data = bpy.data.meshes.new("bbox_mesh_data")
        mesh_data.from_pydata(verts, [], faces)
        mesh_data.update()

        obj = bpy.data.objects.new(os.path.basename(model.name), mesh_data)
        bpy.context.scene.objects.link(obj)
        # obj.select = True

        bpy.ops.object.select_all(False)
        bpy.context.scene.objects.active = obj  # bpy.data.objects[object]
        bpy.context.active_object.select = True
        '''

        # bpy.context.scene.objects.active = obj
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0))

        bpy.context.active_object.RobotDesigner.fileName = os.path.basename(model.name)

        self.logger.debug('Active robot name: %s', bpy.context.active_object.RobotDesigner.fileName)

        bpy.context.active_object.name = os.path.basename(model.name)
        model_name = bpy.context.active_object.name
        model_type = bpy.context.active_object.type

        if type == 1:
            mat = bpy.data.materials.new('blue')
            mat.diffuse_color = (0, 0, 1, 0.5)
            bpy.context.active_object.data.materials.append(mat)

            bpy.context.active_object.RobotDesigner.tag = "BASIC_COLLISION_BOX"

        self.logger.debug('model_name (geometry): %s', model_name)
        self.logger.debug('model_type (geometry): %s', model_type)

        self.logger.debug('model_geometry_bbox: %s', model.geometry[0].box[0].size[0])

        # todo: if geometry pose is missing
        if not model.pose:
            model_posexyz = [0, 0, 0]
            model_poserpy = [0, 0, 0]
        else:
            self.logger.debug('model_pose (geometry): %s', model.pose[0].value())
            model_posexyz = string_to_list(model.pose[0].value())[0:3]
            model_poserpy = string_to_list(model.pose[0].value())[3:]

        return Matrix.Translation(Vector(model_posexyz)) @ \
               Euler(model_poserpy, 'XYZ').to_matrix().to_4x4()


    def import_sphere(self, model, type):
        """
        Adds a sphere of radius 1.0 to the blender scene. Uses the self.file_name variable of the parenting context
        The correct lengths are adjusted later together with the scaling
        :param model: A sdf_dom.visual object.
        :param type: COLLISION or VISUAL. COLLISION = 1. VISUAL = 0
        :return: Returns the transformation in the origin element (a 4x4 blender matrix).
        """

        # determine prefix path for loading meshes in case of paths relative to ROS_PACKAGE_PATH
        prefix_folder = ""
        c_radius = model.geometry[0].sphere[0].radius[0]

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=(0, 0, 0))
        bpy.context.active_object.RobotDesigner.fileName = os.path.basename(model.name)

        self.logger.debug('Active robot name: %s', bpy.context.active_object.RobotDesigner.fileName)

        bpy.context.active_object.name = os.path.basename(model.name)
        model_name = bpy.context.active_object.name
        # bpy.context.active_object.type = 'ARMATURE'
        model_type = bpy.context.active_object.type

        if type == 1:
            mat = bpy.data.materials.new('blue')
            mat.diffuse_color = (0, 0, 1, 0.5)
            bpy.context.active_object.data.materials.append(mat)

            bpy.context.active_object.RobotDesigner.tag = "BASIC_COLLISION_SPHERE"

        self.logger.debug('model_name (geometry): %s', model_name)
        self.logger.debug('model_type (geometry): %s', model_type)

        self.logger.debug('model_geometry_sphere: radius %s', c_radius)

        # todo: if geometry pose is missing
        if not model.pose:
            model_posexyz = [0, 0, 0]
            model_poserpy = [0, 0, 0]
        else:
            self.logger.debug('model_pose (geometry): %s', model.pose[0].value())
            model_posexyz = string_to_list(model.pose[0].value())[0:3]
            model_poserpy = string_to_list(model.pose[0].value())[3:]

        return Matrix.Translation(Vector(model_posexyz)) @ \
               Euler(model_poserpy, 'XYZ').to_matrix().to_4x4()


    def import_cylinder(self, model, type):
        """
        Adds a cylinder of radius 1.0 and depth 1.0 to the blender scene. Uses the self.file_name variable of the parenting context
        The correct lengths are adjusted later together with the scaling
        :param model: A sdf_dom.visual object.
        :param type: COLLISION or VISUAL. COLLISION = 1. VISUAL = 0
        :return: Returns the transformation in the origin element (a 4x4 blender matrix).
        """

        # determine prefix path for loading meshes in case of paths relative to ROS_PACKAGE_PATH
        prefix_folder = ""
        c_radius = model.geometry[0].cylinder[0].radius[0]
        c_depth = model.geometry[0].cylinder[0].length[0]

        bpy.ops.mesh.primitive_cylinder_add(depth=1.0, radius=1.0, location=(0, 0, 0))
        bpy.context.active_object.RobotDesigner.fileName = os.path.basename(model.name)

        self.logger.debug('Active robot name: %s', bpy.context.active_object.RobotDesigner.fileName)

        bpy.context.active_object.name = os.path.basename(model.name)
        model_name = bpy.context.active_object.name
        # bpy.context.active_object.type = 'ARMATURE'
        model_type = bpy.context.active_object.type

        if type == 1:
            mat = bpy.data.materials.new('blue')
            mat.diffuse_color = (0, 0, 1, 0.5)
            bpy.context.active_object.data.materials.append(mat)

            bpy.context.active_object.RobotDesigner.tag = "BASIC_COLLISION_CYLINDER"

        self.logger.debug('model_name (geometry): %s', model_name)
        self.logger.debug('model_type (geometry): %s', model_type)

        self.logger.debug('model_geometry_cylinder: radius %s, depth %s', c_radius, c_depth)

        # todo: if geometry pose is missing
        if not model.pose:
            model_posexyz = [0, 0, 0]
            model_poserpy = [0, 0, 0]
        else:
            self.logger.debug('model_pose (geometry): %s', model.pose[0].value())
            model_posexyz = string_to_list(model.pose[0].value())[0:3]
            model_poserpy = string_to_list(model.pose[0].value())[3:]

        return Matrix.Translation(Vector(model_posexyz)) @ \
               Euler(model_poserpy, 'XYZ').to_matrix().to_4x4()


    def import_geometry(self, model):
        """
        Adds a geometry to the blender scene. Uses the self.file_name variable of the parenting context
        :param model: A sdf_dom.visual object.
        :return: Returns the transformation in the origin element (a 4x4 blender matrix).
        """

        # determine prefix path for loading meshes in case of paths relative to ROS_PACKAGE_PATH
        prefix_folder = ""
        mesh_x = model.geometry[0].mesh[0]
        mesh_url = model.geometry[0].mesh[0].uri[0]

        # check for absolute file path
        if mesh_url.startswith(self.FILE_URL_ABSOLUTE):
            mesh_path = mesh_url.replace(self.FILE_URL_ABSOLUTE, '')
        elif mesh_url.startswith(self.FILE_URL_RELATIVE) or mesh_url.startswith(self.PACKAGE_URL):
            mesh_path = mesh_url.replace(self.FILE_URL_RELATIVE, '').replace(self.PACKAGE_URL, '')
            mesh_path = os.path.join(str(Path(self.base_dir).parent), mesh_path)
            self.logger.debug("mesh path %s", mesh_path)

        else:
            self.operator.report({'ERROR'}, "Unsupported URL schema")
            self.logger.error("Unsupported URL schema")
            return
        # if len(model.geometry[0].cylinder) > 0:
        #     self.logger.debug('Cylinder Existing')
        #     c_radius = model.geometry[0].cylinder[0].radius[0]
        #     c_depth = model.geometry[0].cylinder[0].length[0]
        #
        #     bpy.ops.mesh.primitive_cylinder_add(depth=c_depth, radius=c_radius)
        #     bpy.context.active_object.RobotDesigner.fileName = os.path.basename(model.name)


        fn, extension = os.path.splitext(mesh_path)
        if extension == ".stl" or extension == ".STL":
            try:
                bpy.ops.import_mesh.stl(filepath=mesh_path)
            except:
                pass
        elif extension == ".dae" or extension == ".DAE":
            try:
                bpy.ops.wm.collada_import(filepath=mesh_path)
            except:
                pass

        bpy.context.active_object.RobotDesigner.fileName = os.path.basename(os.path.splitext(mesh_path)[0])

        self.logger.debug('Active robot name: %s', bpy.context.active_object.RobotDesigner.fileName)
        bpy.context.active_object.name = os.path.basename(model.name)
        model_name = bpy.context.active_object.name
        # bpy.context.active_object.type = 'ARMATURE'
        model_type = bpy.context.active_object.type

        self.logger.debug('model_name (geometry): %s', model_name)
        self.logger.debug('model_type (geometry): %s', model_type)

        self.logger.debug('model_geometry_mesh_scale (geometry): %s', model.geometry[0].mesh[0].scale)

        scale_matrix = Matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                               [0, 0, 1, 0], [0, 0, 0, 1]])
        # scale_matrix = Matrix([[scale_factor[0], 0, 0, 0], [0, scale_factor[1], 0, 0],
        #                       [0, 0, scale_factor[2], 0], [0, 0, 0, 1]])


        # todo: if geometry pose is missing
        if not model.pose:
            model_posexyz = [0, 0, 0]
            model_poserpy = [0, 0, 0]
        else:
            self.logger.debug('model_pose (geometry): %s', model.pose[0].value())
            model_posexyz = string_to_list(model.pose[0].value())[0:3]
            model_poserpy = string_to_list(model.pose[0].value())[3:]

        return Matrix.Translation(Vector(model_posexyz)) @ \
               Euler(model_poserpy, 'XYZ').to_matrix().to_4x4() @ scale_matrix


    def parse(self, node: sdf_tree.SDFTree, ref_pose, parent_name = ""):
        """
        Recursively parses the SDF tree elements.

        :param node: The actual segment
        :param parent_name: Name of the parent segment (if None the segment is a root element)
        :param ref_pose: Reference pose from parent link (SDF, pose referenced to a global coordinate)

        """

        # global_properties.gazebo_tags.set(bpy.context.scene, '')

        # oldscene = bpy.context.scene #get current scene in new file
        C = bpy.context

        self.logger.info("Context mode: %s", C.mode)
        #         if context.mode != 'OBJECT':
        #             bpy.ops.object.mode_set(mode='OBJECT')

        self.logger.info("parent name: %s", parent_name)
        # self.logger.debug('active bone name : %s', C.active_bone.name)
        self.logger.debug('active object name : %s', C.active_object.name)  # the name of the robot

        self.logger.debug('active object type : %s', C.active_object.type)

        if bpy.context.active_object:
            self.logger.debug('active object type == Armature: %s, %s', bpy.context.active_object.type == 'ARMATURE',
                              "Model not selected and active.")
        else:
            self.logger.debug('active object type == Armature: %s, %s', False, "No model selected")

        # DDD=getattr(getattr(bpy.ops, PLUGIN_PREFIX), self.operator.bl_idname.replace(PLUGIN_PREFIX + '.', ''))

        # self.logger.debug('For debug only : %s', DDD)

        SelectSegment.run(segment_name=parent_name)

        CreateNewSegment.run(segment_name=node.link.name)

        segment_name = C.active_bone.name

        self.logger.info("%s -> %s", parent_name, segment_name)
        self.logger.info("link name -> %s", node.link.name)

        # to confirm: SDF a joint's pose is given in child link frame, URDF joint frame = child link frame

        if not node.link.pose:
            child_link_pose = [0, 0, 0, 0, 0, 0]
        else:
            child_link_pose = string_to_list(get_value(node.link.pose[0].value(), "0 0 0 0 0 0"))
        # child_link_pose = pose_modelpose(child_link_pose,  string_to_list("0 0 0.6 0 1.57 0"))

        parent_pose_homo = pose_float2homogeneous(rounded(ref_pose))
        child_pose_homo = pose_float2homogeneous(rounded(child_link_pose))
        xyz, euler = pose2origin(parent_pose_homo, child_pose_homo)

        self.logger.info("child link pose xyzeuler-> %s", child_link_pose)
        self.logger.info("parent link pose xyzeuler-> %s", ref_pose)
        self.logger.info("converted local pose xyz -> %s", xyz)
        self.logger.info("converted local pose euler -> %s", euler)

        # urdf xyz = string_to_list(get_value(node.joint.origin.xyz, "0 0 0"))
        # urdf euler = string_to_list(get_value(node.joint.origin.rpy, '0 0 0'))

        # urdf
        # import joint controllers
        if segment_name in self.controllers:
            controller = self.controllers[segment_name]
            PID = controller.pid.split(" ")
            bpy.context.active_bone.RobotDesigner.jointController.isActive = True
            bpy.context.active_bone.RobotDesigner.jointController.controllerType = controller.type
            bpy.context.active_bone.RobotDesigner.jointController.P = float(PID[0])
            bpy.context.active_bone.RobotDesigner.jointController.I = float(PID[1])
            bpy.context.active_bone.RobotDesigner.jointController.D = float(PID[2])

        if node.joint:
            axis = string_to_list(node.joint.axis[0].xyz[0])
        else:
            axis = string_to_list('1 0 0')
        # axis = [round(axis[0]), round(axis[1]), round(axis[2])]
        self.logger.info("axis -> %s", axis)
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
            self.logger.info("axis is wrong -> %s", axis)
            pass

        self.logger.info("axis -> %s", axis)

        bpy.context.active_bone.RobotDesigner.Euler.x.value = xyz[0]
        bpy.context.active_bone.RobotDesigner.Euler.y.value = xyz[1]
        bpy.context.active_bone.RobotDesigner.Euler.z.value = xyz[2]

        bpy.context.active_bone.RobotDesigner.Euler.alpha.value = round(degrees(euler[0]), 0)
        bpy.context.active_bone.RobotDesigner.Euler.beta.value = round(degrees(euler[1]), 0)
        bpy.context.active_bone.RobotDesigner.Euler.gamma.value = round(degrees(euler[2]), 0)

        # Set joint names
        if node.joint:
            bpy.context.active_bone.RobotDesigner.joint_name = node.joint.name
            # Set attach link to world to true if world joint.
            if node.joint.parent[0] == 'world':
                bpy.context.active_bone.RobotDesigner.world = True

        # Set joint controller
        if node.joint:
            if len(node.joint.axis[0].limit):
                bpy.context.active_bone.RobotDesigner.controller.maxTorque = float(get_list_value(
                    node.joint.axis[0].limit[0].effort, 0))
                bpy.context.active_bone.RobotDesigner.controller.maxVelocity = float(get_list_value(
                    node.joint.axis[0].limit[0].velocity, 0))
                bpy.context.active_bone.RobotDesigner.controller.isActive = True

        # bpy.context.active_bone.RobotDesigner.controller.maxVelocity = float(tree.joint.limit.friction)

        if node.joint:
            if node.joint.type == 'revolute':
                bpy.context.active_bone.RobotDesigner.jointMode = 'REVOLUTE'
                if len(node.joint.axis[0].limit):
                    bpy.context.active_bone.RobotDesigner.theta.max = degrees(
                        float(get_list_value(node.joint.axis[0].limit[0].upper, 0)))
                    bpy.context.active_bone.RobotDesigner.theta.min = degrees(
                        float(get_list_value(node.joint.axis[0].limit[0].lower, 0)))
            if node.joint.type == 'prismatic':
                bpy.context.active_bone.RobotDesigner.jointMode = 'PRISMATIC'
                if len(node.joint.axis[0].limit):
                    bpy.context.active_bone.RobotDesigner.d.max = \
                        float(get_list_value(node.joint.axis[0].limit[0].upper, 0))
                    bpy.context.active_bone.RobotDesigner.d.min = \
                        float(get_list_value(node.joint.axis[0].limit[0].lower, 0))
            if node.joint.type == 'revolute2':
                bpy.context.active_bone.RobotDesigner.jointMode = 'REVOLUTE2'
            if node.joint.type == 'universal':
                bpy.context.active_bone.RobotDesigner.jointMode = 'UNIVERSAL'
            if node.joint.type == 'ball':
                bpy.context.active_bone.RobotDesigner.jointMode = 'BALL'
            if node.joint.type == 'fixed':
                bpy.context.active_bone.RobotDesigner.jointMode = 'FIXED'
        else:
            bpy.context.active_bone.RobotDesigner.jointMode = 'FIXED'

        if node.joint:
            # import joint physics if they exist
            if len(node.joint.physics):
                bpy.context.active_bone.RobotDesigner.ode.cfm_damping = node.joint.physics[0].ode[0].cfm_damping[0]
                bpy.context.active_bone.RobotDesigner.ode.i_s_damper = \
                    node.joint.physics[0].ode[0].implicit_spring_damper[0]
                bpy.context.active_bone.RobotDesigner.ode.cfm = node.joint.physics[0].ode[0].cfm[0]
                bpy.context.active_bone.RobotDesigner.ode.erp = node.joint.physics[0].ode[0].erp[0]

            if len(node.joint.axis[0].dynamics):
                bpy.context.active_bone.RobotDesigner.dynamics.damping = node.joint.axis[0].dynamics[0].damping[0]
                bpy.context.active_bone.RobotDesigner.dynamics.friction = node.joint.axis[0].dynamics[0].friction[0]
                bpy.context.active_bone.RobotDesigner.dynamics.spring_reference = \
                    node.joint.axis[0].dynamics[0].spring_reference[0]
                bpy.context.active_bone.RobotDesigner.dynamics.spring_stiffness = \
                    node.joint.axis[0].dynamics[0].spring_stiffness[0]

        model = bpy.context.active_object
        model_name = model.name

        pose_bone = bpy.context.active_object.pose.bones[segment_name]
        self.logger.debug("bpy.context.active_object name (before iterating over visual): %s", bpy.context.active_object.name)
        self.logger.debug("active object pose bone matrix: %s", homo2origin(pose_bone.matrix))
        self.logger.debug("active object matrix world: %s",
                          homo2origin(model.matrix_world))

        segment_world = model.matrix_world @ pose_bone.matrix
        # segment_world = pose_float2homogeneous(rounded(string_to_list("0 0 0.6 0 0 -1.570796")))*pose_bone.matrix

        # import segment physics properties
        if len(node.link.gravity) > 0:
            bpy.context.active_bone.RobotDesigner.linkInfo.gravity = node.link.gravity[0]
            bpy.context.active_bone.RobotDesigner.linkInfo.link_self_collide = node.link.self_collide[0]

        if len(node.link.inertial) > 0:
            i = node.link.inertial[0].inertia[0]
            SelectSegment.run(segment_name=segment_name)
            CreatePhysical.run(frameName=node.link.name)
            # SelectPhysical.run(frameName=node.link.name)
            # SelectSegment.run(segment_name=segment_name)
            # AssignPhysical.run()

            inertia_name = "PHYS_" + node.link.name

            # set mass
            bpy.data.objects[inertia_name].RobotDesigner.dynamics.mass = node.link.inertial[0].mass[0]

            # set center of mass position
            inertia_location = string_to_list(node.link.inertial[0].pose[0].value())[0:3]
            inertia_location[1] = inertia_location[1] - 1.0
            inertia_rotation = string_to_list(node.link.inertial[0].pose[0].value())[3:]

            # bpy.data.objects[node.link.name].location = [inertia_location[1], inertia_location[2], inertia_location[0]]
            bpy.data.objects[inertia_name].location = inertia_location
            bpy.data.objects[inertia_name].rotation_euler = inertia_rotation

            # set inertia
            bpy.data.objects[inertia_name].RobotDesigner.dynamics.inertiaXX = i.ixx[0]
            bpy.data.objects[inertia_name].RobotDesigner.dynamics.inertiaXY = i.ixy[0]
            bpy.data.objects[inertia_name].RobotDesigner.dynamics.inertiaXZ = i.ixz[0]
            bpy.data.objects[inertia_name].RobotDesigner.dynamics.inertiaYY = i.iyy[0]
            bpy.data.objects[inertia_name].RobotDesigner.dynamics.inertiaYZ = i.iyz[0]
            bpy.data.objects[inertia_name].RobotDesigner.dynamics.inertiaZZ = i.izz[0]

        model = bpy.context.active_object
        model_name = model.name

        pose_bone = bpy.context.active_object.pose.bones[segment_name]
        self.logger.debug("bpy.context.active_object name (before iterating over visual): %s", bpy.context.active_object.name)
        self.logger.debug("active object pose bone matrix: %s", homo2origin(pose_bone.matrix))
        self.logger.debug("active object matrix world: %s",
                          homo2origin(model.matrix_world))

        segment_world = model.matrix_world @ pose_bone.matrix
        # segment_world = pose_float2homogeneous(rounded(string_to_list("0 0 0.6 0 0 -1.570796")))*pose_bone.matrix

        self.logger.debug("[VISUAL] parsed: " + str(len(list(node.link.visual))) + " visual meshes.")

        self.logger.debug("[COLLISION] parsed: " + str(len(list(node.link.collision))) + " collision meshes.")

        # Iterate first over visual models then over collision models
        VISUAL, COLLISON = 0, 1
        for model_type, geometric_models in enumerate((node.link.visual, node.link.collision)):
            # Iterate over the geometric models that are declared for the link
            for nr, model in enumerate(geometric_models):
                self.logger.debug("name = %s", model.name)
                if not len(model.geometry):
                    continue
                # geometry is not optional in the xml
                # geometry element: "box", "cylinder", "heightmap", "image", "mesh", "plane", "polyline", "sphere"
                # if len(model.geometry[0].box) > 0:
                #     self.logger.debug("[VISUAL] box size: " + str(model.geometry[0].box[0].size[0]))
                # if len(model.geometry[0].cylinder) > 0:
                #     trafo_sdf = self.import_cylinder(model)
                #     # if there are multiple objects in the COLLADA file, they will be selected
                #     selected_objects = [i for i in bpy.context.selected_objects]
                #     for object in selected_objects:
                #         bpy.context.scene.objects.active = object  # bpy.data.objects[object]
                #         bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
                #     for object in selected_objects:
                #         #if object.type != 'MESH':
                #         #    self.logger.debug("object type): %s", object.type)
                #         #    continue
                #
                #         # Select the object (and deselect others)
                #         bpy.ops.object.select_all(False)
                #         bpy.context.scene.objects.active = object  # bpy.data.objects[object]
                #         bpy.context.active_object.select = True
                #         self.logger.debug("active object matrix world (from mesh): %s", homo2origin(bpy.context.active_object.matrix_world))
                #         #bpy.context.active_object.matrix_world = pose_float2homogeneous(rounded(string_to_list("0 0 0 0 0 0")))
                #         self.logger.debug("bpy.context.active_object name: %s", bpy.context.active_object.name)
                #         self.logger.debug("active object matrix world (before transfer): %s", homo2origin(bpy.context.active_object.matrix_world))
                #         bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                #         # after applying transform, matrix world becomes zero again
                #         bpy.context.active_object.matrix_world =  segment_world * trafo_sdf * bpy.context.active_object.matrix_world#* inverse_matrix(bpy.context.active_object.matrix_world)#* \
                #                                                #  bpy.context.active_object.matrix_world
                #         self.logger.debug("active object matrix world (after transfer): %s", homo2origin(bpy.context.active_object.matrix_world))
                #         self.logger.info("Model type: " + str(model_type))
                #         # Remove multiple "COL_" and "VIS_" strings before renaming
                #         if model_type == COLLISON:
                #             # %2d changed to %d because it created unwanted space with one digit numbers
                #             bpy.context.active_object.name = "COL_%s_%d" % (node.link.name, nr)
                #             bpy.context.active_object.RobotDesigner.tag = 'COLLISION'
                #         else:
                #             bpy.context.active_object.name = "VIS_%s_%d" % (node.link.name, nr)
                #
                #         # remove spaces from link name
                #         bpy.context.active_object.name = bpy.context.active_object.name.replace(" ", "")
                #
                #         # The name might be altered by blender
                #         assigned_name = bpy.context.active_object.name
                #
                #         bpy.ops.object.transform_apply(location=False,
                #                                        rotation=False,
                #                                        scale=True)
                #         SelectModel.run(model_name=model_name)
                #         SelectSegment.run(segment_name=segment_name)
                #         SelectGeometry.run(geometry_name=assigned_name)
                #         AssignGeometry.run()

                type = "none"
                if len(model.geometry[0].mesh) > 0:
                    type = "mesh"
                elif len(model.geometry[0].cylinder) > 0:
                    type = "cylinder"
                elif len(model.geometry[0].box) > 0:
                    type = "box"
                elif len(model.geometry[0].sphere) > 0:
                    type = "sphere"

                if type == "mesh" or type == "cylinder" or type == "box" or type == "sphere":
                    self.logger.debug("geometry %s", model.geometry[0])

                    if type == "cylinder":
                        trafo_sdf = self.import_cylinder(model, model_type)
                        print("import cyl")
                    elif type == "box":
                        trafo_sdf = self.import_box(model, model_type)
                        print("import box")
                    elif type == "sphere":
                        trafo_sdf = self.import_sphere(model, model_type)
                        print("import sphere")
                    else:
                        trafo_sdf = self.import_geometry(model)
                        print("import mesh")
                    # if there are multiple objects in the COLLADA file, they will be selected
                    selected_objects = [i for i in bpy.context.selected_objects]
                    for object in selected_objects:
                        bpy.context.view_layer.objects.active = object  # bpy.data.objects[object]
                        bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
                    for object in selected_objects:
                        if object.type != 'MESH':
                            self.logger.debug("object type not mesh): %s", object.type)
                            continue

                        # Select the object (and deselect others)
                        bpy.ops.object.select_all(False)
                        bpy.context.view_layer.objects.active = object  # bpy.data.objects[object]
                        bpy.context.active_object.select_set(True)
                        self.logger.debug("active object matrix world (from mesh): %s",
                                          homo2origin(bpy.context.active_object.matrix_world))
                        # bpy.context.active_object.matrix_world = pose_float2homogeneous(rounded(string_to_list("0 0 0 0 0 0")))
                        self.logger.debug("bpy.context.active_object name: %s", bpy.context.active_object.name)
                        self.logger.debug("active object matrix world (before transfer): %s",
                                          homo2origin(bpy.context.active_object.matrix_world))
                        # if len(model.geometry[0].mesh) > 0:
                        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                        # after applying transform, matrix world becomes zero again
                        bpy.context.active_object.matrix_world = segment_world @ trafo_sdf @ bpy.context.active_object.matrix_world  # * inverse_matrix(bpy.context.active_object.matrix_world)#* \
                        #  bpy.context.active_object.matrix_world
                        self.logger.debug("active object matrix world (after transfer): %s",
                                          homo2origin(bpy.context.active_object.matrix_world))
                        self.logger.info("Model type: " + str(model_type))
                        # Remove multiple "COL_" and "VIS_" strings before renaming
                        '''
                        if model_type == COLLISON:
                            # %2d changed to %d because it created unwanted space with one digit numbers
                            if not model.name.startswith("COL_"):
                                bpy.context.active_object.name = "COL_%s" % (model.name)
                            else:
                                bpy.context.active_object.name = "%s" % (model.name)
                            bpy.context.active_object.RobotDesigner.tag = 'COLLISION'

                        else:
                            if not model.name.startswith("VIS_"):
                                bpy.context.active_object.name = "VIS_%s" % (model.name)
                            else:
                                bpy.context.active_object.name = "%s" % (model.name)
                        '''

                        if not model.name.endswith("_" + str(nr)) and nr != 0:
                            bpy.context.active_object.name = "%s_%d" % (model.name, nr)

                        # remove spaces from link name
                        bpy.context.active_object.name = bpy.context.active_object.name.replace(" ", "")

                        if type == "mesh":
                            print(bpy.context.active_object.name)

                        # The name might be altered by blender
                        assigned_name = bpy.context.active_object.name

                        bpy.ops.object.transform_apply(location=False,
                                                       rotation=False,
                                                       scale=True)
                        SelectModel.run(model_name=model_name)
                        SelectSegment.run(segment_name=segment_name)
                        SelectGeometry.run(geometry_name=assigned_name)

                        if model_type == COLLISON:
                            # import surface properties
                            if len(model.surface):
                                surface = bpy.data.objects[assigned_name].RobotDesigner.sdfCollisionProps
                                surface.restitution_coeff = model.surface[0].bounce[0].restitution_coefficient[0]
                                surface.threshold = model.surface[0].bounce[0].threshold[0]
                                surface.coefficient = model.surface[0].friction[0].torsional[0].coefficient[0]
                                surface.use_patch_radius = model.surface[0].friction[0].torsional[0].use_patch_radius[0]
                                surface.surface_radius = model.surface[0].friction[0].torsional[0].surface_radius[0]
                                surface.slip = model.surface[0].friction[0].torsional[0].ode[0].slip[0]
                                surface.mu = model.surface[0].friction[0].ode[0].mu[0]
                                surface.mu2 = model.surface[0].friction[0].ode[0].mu2[0]
                                surface.fdir1 = string_to_list(model.surface[0].friction[0].ode[0].fdir1[0])
                                surface.slip1 = model.surface[0].friction[0].ode[0].slip1[0]
                                surface.slip2 = model.surface[0].friction[0].ode[0].slip2[0]
                                surface.collide_wo_contact = model.surface[0].contact[0].collide_without_contact[0]
                                surface.collide_wo_contact_bitmask = model.surface[0].contact[0].collide_without_contact_bitmask[0]
                                surface.collide_bitmask = model.surface[0].contact[0].collide_bitmask[0]
                                surface.category_bitmask = model.surface[0].contact[0].category_bitmask[0]
                                surface.poissons_ratio = model.surface[0].contact[0].poissons_ratio[0]
                                surface.elastic_modulus = model.surface[0].contact[0].elastic_modulus[0]
                                surface.osim_stiffness = model.surface[0].contact[0].opensim[0].stiffness[0]
                                surface.osim_dissipation = model.surface[0].contact[0].opensim[0].dissipation[0]
                                surface.soft_cfm = model.surface[0].contact[0].ode[0].soft_cfm[0]
                                surface.soft_erp = model.surface[0].contact[0].ode[0].soft_erp[0]
                                surface.kp = model.surface[0].contact[0].ode[0].kp[0]
                                surface.kd = model.surface[0].contact[0].ode[0].kd[0]
                                surface.max_vel = model.surface[0].contact[0].ode[0].max_vel[0]
                                surface.min_depth = model.surface[0].contact[0].ode[0].min_depth[0]
                            AssignGeometry.run(attach_collision_geometry=True)
                        else:
                            AssignGeometry.run()

                        # Write scale values into scale_factor
                        # for objects other than mesh, scaling works correctly iff the model and geometry are selected
                        # else a different object will be scaled and/or will not scale at all
                        if type == "mesh" and model.geometry[0].mesh[0].scale != []:
                            scale_factor = string_to_list(model.geometry[0].mesh[0].scale[0])
                        elif type == 'cylinder':
                            c_radius = model.geometry[0].cylinder[0].radius[0]
                            c_depth = model.geometry[0].cylinder[0].length[0]
                            bpy.data.objects[assigned_name].RobotDesigner.scaling.scale_radius = c_radius
                            bpy.data.objects[assigned_name].RobotDesigner.scaling.scale_depth = c_depth
                            scale_factor = [c_radius, c_radius, c_depth]
                        elif type == 'sphere':
                            s_radius = model.geometry[0].sphere[0].radius[0]
                            bpy.data.objects[assigned_name].RobotDesigner.scaling.scale_all = s_radius
                            scale_factor = [s_radius, s_radius, s_radius]
                        elif type == 'box':
                            b_width = string_to_list(model.geometry[0].box[0].size[0])[0]
                            b_depth = string_to_list(model.geometry[0].box[0].size[0])[1]
                            b_height = string_to_list(model.geometry[0].box[0].size[0])[2]
                            scale_factor = [b_width, b_depth, b_height]
                        else:
                            scale_factor = [1, 1, 1]

                        # Scale the geometry
                        bpy.data.objects[global_properties.mesh_name.get(bpy.context.scene)].scale = scale_factor

                        # bpy.context.active_object.scale = scale_factor
                else:
                    self.logger.error("Mesh file not found")
                    pass
        # update ref_pose
        for sub_tree in node.children:
            ref_pose = child_link_pose
            self.parse(sub_tree, ref_pose, segment_name)
        return segment_name


    def import_file(self):
        muscles, robot_name, robot_location, robot_rotation, root_links, kinematic_chains, self.controllers = \
            sdf_tree.SDFTree.parse(self.file_path)

        self.MUSCLE_PATH = muscles

        self.logger.debug("%s,%s", self.base_dir, self.file_path)
        # store gazebo tags
        tag_buffer = ''
        gazebo_tag = []
        # self.logger.debug('Processing {0} tags.'.format(len(gazebo_tags)))
        # for gazebo_tag in gazebo_tags:
        #    curr_tag = gazebo_tag.toxml("utf-8").decode("utf-8")
        #    curr_tag = curr_tag[38:]  # remove <xml version=.../> tag
        # 3    tag_buffer = '{0}\n{1}'.format(tag_buffer, curr_tag)
        # global_properties.gazebo_tags.set(bpy.context.scene, tag_buffer)

        self.logger.debug('root links: %s', [i.name for i in root_links])

        CreateNewModel.run(model_name=robot_name, base_segment_name="")
        model_name = bpy.context.active_object.name
        model_type = bpy.context.active_object.type
        bpy.context.active_object.RobotDesigner.modelMeta.model_folder = os.path.basename(os.path.dirname(self.file_path))

        self.logger.debug('model_name: %s', model_name)
        self.logger.debug('model_type: %s', model_type)

        SelectModel.run(model_name=model_name)
        # for link in root_links:
        #     for visual in link.visual:
        #         self.logger.debug('mesh name: %s', visual.geometry[0].mesh[0].uri[0])
        #         if visual.geometry[0].mesh is not None:
        #             trafo = self.import_geometry(visual)
        #
        #             if (visual.geometry[0].mesh[0].scale) == []:
        #                 s1 = [1, 1, 1]
        #             else:
        #                 s1 = string_to_list(visual.geometry[0].mesh[0].scale[0])  # string_to_list([0].mesh[0].scale)
        #             s2 = bpy.context.active_object.scale
        #
        #             self.logger.debug('visual_geometry_mesh_scale: %s', s1)
        #             self.logger.debug('context_active_object_scale: %s', s2)
        #
        #
        #             scale = Matrix([[s1[0] * s2[0], 0, 0, 0], [0, s1[1] * s2[1], 0, 0],
        #                             [0, 0, s1[2] * s2[2], 0], [0, 0, 0, 1]])
        #             bpy.context.active_object.matrix_world = trafo * scale
        for chain in kinematic_chains:
            ref_pose = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            self.logger.debug('new chain: %s   %s', chain, ref_pose)
            root_name = self.parse(chain, ref_pose)
            UpdateSegments.run(segment_name=root_name, recurse=True)
            #      try:
            #          SelectCoordinateFrame.run(mesh_name='CoordinateFrame')
            #      except:
            #          pass


        # set robot location and rotation
        bpy.context.active_object.location = robot_location
        bpy.context.active_object.rotation_euler = robot_rotation

        # bpy.ops.view3d.view_lock_to_active()
        bpy.context.active_object.show_in_front = True


    # @RDOperator.Preconditions(ObjectMode)
    # @PluginManager.register_class
    # class ImportPackage(RDOperator):
    #     """
    #     :term:`Operator<operator>` for importing a robot from a ROS package (URDF)
    #     """
    #
    #     # Obligatory class attributes
    #     bl_idname = config.OPERATOR_PREFIX + "import_sdf_package"
    #     bl_label = "SDF import (ROS package)"
    #
    #     filepath = StringProperty(name="Filename", subtype='FILE_PATH')
    #
    #     # directory = StringProperty(
    #     #        name="Mesh directory", subtype='DIR_PATH', default="")
    #
    #     def invoke(self, context, event):
    #         context.window_manager.fileselect_add(self)
    #         return {'RUNNING_MODAL'}
    #
    #     @RDOperator.OperatorLogger
    #     @RDOperator.Postconditions(ModelSelected, ObjectMode)
    #     def execute(self, context):
    #         importer = Importer(operator=self, file_path=self.filepath)
    #         importer.import_package()
    #         return {'FINISHED'}


    def import_config(self):
        """
        imports the model.config file and sets the RDObject variables
        :param self:
        :return:
        """
        model_config_xml = open(self.base_dir + '/model.config').read()
        model = robot_model_config_dom.CreateFromDocument(model_config_xml)

        # read model data
        bpy.context.active_object.RobotDesigner.modelMeta.model_config = model.name
        bpy.context.active_object.RobotDesigner.modelMeta.model_version = str(model.version)

        # read author todo multiple authors
        bpy.context.active_object.RobotDesigner.author.authorName = model.author.name[0]
        bpy.context.active_object.RobotDesigner.author.authorEmail = model.author.email[0]

        bpy.context.active_object.RobotDesigner.modelMeta.model_description = model.description


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportPlain(RDOperator):
        """
        :term:`Operator<operator>` for importing a robot from a SDF plain file
        """

        # Obligatory class attributes
        bl_idname = config.OPERATOR_PREFIX + "import_sdf_plain"
        bl_label = "Import SDF - plain"

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


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportPackage(RDOperator):
        """
        :term:`Operator<operator>` for importing a robot from a ROS/SDF package
        """

        # Obligatory class attributes
        bl_idname = config.OPERATOR_PREFIX + "import_sdf_package"
        bl_label = "Import SDF"

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
            importer.import_config()
            if importer.MUSCLE_PATH != '[]':
                print('muscle path:')
                print(importer.MUSCLE_PATH)
                osim_importer = OsimImporter(self.filepath, importer.MUSCLE_PATH)
                osim_importer.import_osim()
            return {'FINISHED'}


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportZippedPackage(RDOperator):
        """
        :term:`Operator<operator>` for importing a robot from a ROS package (SDF)
        """

        # Obligatory class attributes
        bl_idname = config.OPERATOR_PREFIX + "import_sdf_zipped_package"
        bl_label = "Import SDF from zipped folder"

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
                    self.logger.debug("root: %s, subfolders: %s, files: %s, splitfiles: %s", root, subFolders, files,
                                      [os.path.splitext(i) for i in files])
                    for i in files:
                        if '.sdf' == os.path.splitext(i)[1]:
                            if file_path:
                                self.report({"INFO"}, "Multiple SDF in zip. Choosing: " + str(i))
                            file_path = os.path.join(root, i)

                if file_path:
                    self.logger.debug("Importing: %s", file_path)
                    importer = Importer(operator=self, file_path=file_path)
                    importer.import_file()
                    importer.import_config()
                else:
                    self.report({'ERROR'}, "No SDF file found in package")
                    self.logger.error("No SDF file found in package")

            return {'FINISHED'}
