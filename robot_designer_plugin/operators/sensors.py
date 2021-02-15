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
#  Copyright (c) 2017-2021, TUM Technical University of Munich
#
# ######

# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty

# RobotDesigner imports
from ..core import config, PluginManager, RDOperator
from .helpers import ModelSelected, SingleSegmentSelected, SingleCameraSelected
from ..core.logfile import operator_logger
from ..properties.globals import global_properties


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectSensor(RDOperator):
    """
    :term:`Operator <operator>` for selecting a sensor.
    """

    bl_idname = config.OPERATOR_PREFIX + "select_camera_sensor"
    bl_label = "Select Camera"
    object_name: StringProperty()

    @classmethod
    def run(cls, object_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        Object = bpy.data.objects[self.object_name]

        arm = context.active_object

        for obj in bpy.data.objects:
            obj.select_set(False)

        Object.select_set(True)
        arm.select_set(True)

        global_properties.active_sensor.set(context.scene, self.object_name)

        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class AttachSensor(RDOperator):
    """
    :term:`Operator <operator>` for assigning a camera sensor to a :term:`segment`.
    """

    bl_idname = config.OPERATOR_PREFIX + "assign_sensor"
    bl_label = "Attach Sensor"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected)
    def execute(self, context):
        if (
            bpy.data.objects[
                global_properties.active_sensor.get(context.scene)
            ].RobotDesigner.tag
            == "SENSOR"
        ):
            sensor_type = bpy.data.objects[
                global_properties.active_sensor.get(context.scene)
            ].RobotDesigner.sensor_type
            if sensor_type in [
                "CAMERA_SENSOR",
                "DEPTH_CAMERA_SENSOR",
                "LASER_SENSOR",
                "ALTIMETER_SENSOR",
                "IMU_SENSOR",
            ]:
                bpy.ops.object.parent_set(type="BONE", keep_transform=True)

            elif sensor_type == "FORCE_TORQUE_SENSOR":
                # todo attach force torque sensor to joint
                operator_logger.info("attaching force torque sensor")

            elif sensor_type == "CONTACT_SENSOR":
                # todo attach contact sensor to collision shape
                operator_logger.info("attaching contact sensor")

        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DetachSensor(RDOperator):
    """
    :term:`Operator <operator>` for detaching a single camera sensor from a :term:`segment`.
    """

    bl_idname = config.OPERATOR_PREFIX + "detach_sensor"
    bl_label = "Detach Sensor"

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
        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected, SingleCameraSelected)
@PluginManager.register_class
class ConvertCameraToSensor(RDOperator):
    """
    :term:`Operator <operator>` for detaching a single camera sensor from a :term:`segment`.
    """

    bl_idname = config.OPERATOR_PREFIX + "convert_camera_to_sensor"
    bl_label = "Convert Camera Object to Sensor"

    sensor_type: StringProperty(default="CAMERA_SENSOR")

    @classmethod
    def run(cls, sensor_type):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleCameraSelected)
    def execute(self, context):
        selected = [i for i in context.selected_objects if i.type != "ARMATURE"][0]

        selected.RobotDesigner.tag = "SENSOR"
        selected.RobotDesigner.sensor_type = "CAMERA_SENSOR"
        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateSensor(RDOperator):
    """
    :term:`Operator <operator>` for creating a new :term:`optical sensor`.
    """

    bl_idname = config.OPERATOR_PREFIX + "create_sensor"
    bl_label = "Create Sensor"

    sensor_type: StringProperty(default="CAMERA_SENSOR")
    sensor_name: StringProperty(name="Sensor Name")

    @classmethod
    def run(cls, sensor_type):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        from .model import SelectModel

        model_name = context.active_object.name

        if self.sensor_type in ["CAMERA_SENSOR", "DEPTH_CAMERA_SENSOR", "LASER_SENSOR"]:
            # add camera type sensor
            bpy.ops.object.camera_add()
        else:
            # add other type sensor
            bpy.ops.object.empty_add(type="PLAIN_AXES")

        operator_logger.info("adding", self.sensor_type)

        context.active_object.RobotDesigner.tag = "SENSOR"
        context.active_object.RobotDesigner.sensor_type = self.sensor_type
        context.active_object.name = self.sensor_name
        sensor_name = context.active_object.name

        SelectModel.run(model_name=model_name)
        SelectSensor.run(object_name=sensor_name)

        return {"FINISHED"}

    def invoke(self, context, event):
        self.sensor_type = global_properties.display_sensor_type.get(context.scene)
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class RenameSensor(RDOperator):
    """
    :term:`operator` for renaming the selected sensor


    """

    bl_idname = config.OPERATOR_PREFIX + "rename_sensor"
    bl_label = "Rename Active Sensor"

    new_name: StringProperty(name="Enter new name:")

    # todo
    @RDOperator.OperatorLogger
    def execute(self, context):
        bpy.data.objects[
            global_properties.active_sensor.get(context.scene)
        ].name = self.new_name
        global_properties.active_sensor.set(context.scene, self.new_name)
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, new_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DeleteSensor(RDOperator):
    """
    :term:`operator` for deleting the selected sensor.


    """

    bl_idname = config.OPERATOR_PREFIX + "delete_sensor"
    bl_label = "Delete Active Sensor"

    @RDOperator.OperatorLogger
    def execute(self, context):
        # todo
        active_sensor = global_properties.active_sensor.get(context.scene)

        # remove muscle and all its data
        bpy.data.objects.remove(bpy.data.objects[active_sensor], do_unlink=True)
        bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
