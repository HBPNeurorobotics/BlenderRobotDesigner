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
#
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######

# ######
# System imports
# import os
# import sys
# import math

# ######
# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty
# import mathutils

# ######
# RobotDesigner imports
from ..core import config, PluginManager, Condition, RDOperator
from .helpers import ModelSelected, SingleMeshSelected, ObjectMode, SingleCameraSelected

from ..properties.globals import global_properties

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectSensor(RDOperator):
    """
    :term:`Operator <operator>` for selecting a sensor.
    """
    bl_idname = config.OPERATOR_PREFIX + "select_camera_sensor"
    bl_label = "Select Camera"
    object_name = StringProperty()

    @classmethod
    def run(cls, object_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        Object = bpy.data.objects[self.object_name]

        arm = context.active_object

        for obj in bpy.data.objects:
            obj.select = False

        Object.select = True
        arm.select = True

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, SingleCameraSelected)
@PluginManager.register_class
class AssignCameraSensor(RDOperator):
    """
    :term:`Operator <operator>` for assigning a camera sensor to a :term:`segment`.
    """
    bl_idname = config.OPERATOR_PREFIX + "assign_camera_sensor"
    bl_label = "Assign Camera"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, SingleCameraSelected)
@PluginManager.register_class
class DetachCameraSensor(RDOperator):
    """
    :term:`Operator <operator>` for detaching a single camera sensor from a :term:`segment`.
    """
    bl_idname = config.OPERATOR_PREFIX + "unassignmesh"
    bl_label = "Unassign selected mesh"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleCameraSelected)
    def execute(self, context):
        sensor_name = global_properties.camera_sensor_name.get(context.scene)
        current_sensor = bpy.data.objects[sensor_name]
        mesh_global = current_sensor.matrix_world
        current_sensor.parent = None
        current_sensor.matrix_world = mesh_global
        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, SingleCameraSelected)
@PluginManager.register_class
class ConvertCameraToSensor(RDOperator):
    """
    :term:`Operator <operator>` for detaching a single camera sensor from a :term:`segment`.
    """
    bl_idname = config.OPERATOR_PREFIX + "unassignmesh"
    bl_label = "Unassign selected mesh"

    sensor_type = StringProperty(default="CAMERA_SENSOR")

    @classmethod
    def run(cls, sensor_type):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleCameraSelected)
    def execute(self, context):

        selected = [i for i in context.selected_objects if i.type != "ARMATURE"][0]

        selected.RobotEditor.tag = "CAMERA_SENSOR"
        return {'FINISHED'}
