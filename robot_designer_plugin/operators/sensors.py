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
from .helpers import ModelSelected, SingleSegmentSelected, ObjectMode, SingleCameraSelected

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

        global_properties.active_sensor.set(context.scene, self.object_name)

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, SingleCameraSelected, SingleSegmentSelected)
@PluginManager.register_class
class AttachSensor(RDOperator):
    """
    :term:`Operator <operator>` for assigning a camera sensor to a :term:`segment`.
    """
    bl_idname = config.OPERATOR_PREFIX + "assign_sensor"
    bl_label = "Assign Sensor"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleCameraSelected, SingleSegmentSelected)
    def execute(self, context):

        if bpy.data.objects[global_properties.active_sensor.get(context.scene)].RobotEditor.tag == "CAMERA_SENSOR":
            bpy.ops.object.parent_set(type='BONE', keep_transform=True)

        # todo: for other sensors add link name tag

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, SingleCameraSelected)
@PluginManager.register_class
class DetachSensor(RDOperator):
    """
    :term:`Operator <operator>` for detaching a single camera sensor from a :term:`segment`.
    """
    bl_idname = config.OPERATOR_PREFIX + "detach_sensor"
    bl_label = "Detach sensor"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleCameraSelected)
    def execute(self, context):
        sensor_name = global_properties.active_sensor.get(context.scene)
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
    bl_idname = config.OPERATOR_PREFIX + "convert_camera_to_sensor"
    bl_label = "Convert camera object to sensor"

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


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateSensor(RDOperator):
    """
    :term:`Operator <operator>` for creating a new :term:`optical sensor`.
    """

    bl_idname = config.OPERATOR_PREFIX + "create_sensor"
    bl_label = "Create sensor"

    sensor_type = StringProperty(default="CAMERA_SENSOR")
    sensor_name = StringProperty(name="Sensor Name")

    @classmethod
    def run(cls, sensor_type):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        from .model import SelectModel

        model_name = context.active_object.name

        if self.sensor_type == "CAMERA_SENSOR":
            print("add camaera")
            bpy.ops.object.camera_add()
        else:
            bpy.ops.object.empty_add(type='PLAIN_AXES')

        context.active_object.RobotEditor.tag = self.sensor_type
        context.active_object.name = self.sensor_name
        sensor_name = context.active_object.name

        SelectModel.run(model_name=model_name)
        SelectSensor.run(object_name=sensor_name)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class RenameSensor(RDOperator):
    """
    :term:`operator` for renaming the selected muscle


    """
    bl_idname = config.OPERATOR_PREFIX + "rename_sensor"
    bl_label = "Rename active sensor"

    new_name = StringProperty(name="Enter new name:")

        # todo
    @RDOperator.OperatorLogger
    def execute(self, context):
        bpy.data.objects[global_properties.active_sensor.get(context.scene)].name = self.new_name
        global_properties.active_sensor.set(context.scene, self.new_name)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, new_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DeleteSensor(RDOperator):
    """
    :term:`operator` for deleting the selected muscle.


    """
    bl_idname = config.OPERATOR_PREFIX + "delete_sensor"
    bl_label = "Delete active sensor"

    @RDOperator.OperatorLogger
    def execute(self, context):

        #todo
        active_sensor = global_properties.active_sensor.get(context.scene)

        # remove muscle and all its data
        bpy.data.objects.remove(bpy.data.objects[active_sensor], True)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)


        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

