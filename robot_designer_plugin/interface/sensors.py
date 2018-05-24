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
# Copyright (c) 2015, Karlsruhe Institute of Technology (KIT)
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#   2016-03-17: Stefan Ulbrich (FZI), Initial version of sensors.
#
# ######

# Blender imports
import bpy

# RobotDesigner imports
from .model import check_armature

from . import menus
from ..operators import sensors, muscles
from .helpers import getSingleObject, getSingleSegment, info_list, AttachSensorBox, DetachSensorBox, SensorPropertiesBox
from ..core.gui import InfoBox
from ..properties.globals import global_properties


def draw(layout, context):
    """
    Draws the user interface for sensor configuration.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return

    if len([i for i in context.selected_objects if i.type == "MESH"]) == 0:
        info_list.append("No mesh selected")
    elif len(context.selected_objects) > 2:
        info_list.append("Too many objects selected")

    box = layout.box()
    row = box.row(align=True)
    column = row.column(align=True)
    column.label("Show:")
    column = row.column(align=True)
    row = column.row(align=True)
    global_properties.sensor_type.prop(context.scene, row, expand=True)
    row = column.row(align=True)

    sensorbox = layout.box()
    sensorbox.label("Select Sensor:")
    row = sensorbox.row()
    columnl = row.column()
    menus.SensorMenu.putMenu(columnl, context)

    columnr = row.column(align=True)

    infoBox = InfoBox(sensorbox)
    mode = global_properties.sensor_type.get(context.scene)
    sensors.CreateSensor.place_button(columnr, "Create new sensor").sensor_type = mode
    sensors.RenameSensor.place_button(columnr, text="Rename active sensor", infoBox=infoBox)
    sensors.DeleteSensor.place_button(columnr, text="Delete active sensor", infoBox=infoBox)

    sensor_type = bpy.data.objects[global_properties.active_sensor.get(context.scene)].RobotEditor.tag

    box = AttachSensorBox.get(layout, context, "Attach/Detach", icon="LINKED")
    if box:
        infoBox = InfoBox(box)
        row = box.row()

        if sensor_type == 'CAMERA_SENSOR' or sensor_type =='LASER_SENSOR':
            column = row.column(align=True)

            single_segment = getSingleSegment(context)

            column.menu(menus.SegmentsGeometriesMenu.bl_idname,
                    text=single_segment.name if single_segment else "Select Segment")
            row2 = column.row(align=True)

            global_properties.list_segments.prop(context.scene, row2, expand=True, icon_only=True)
            row2.separator()
            global_properties.segment_name.prop_search(context.scene, row2, context.active_object.data, 'bones',
                                                   icon='VIEWZOOM',
                                                   text='')

            #create_geometry_selection(column, context)

            row = box.column(align=True)
            sensors.AttachSensor.place_button(row, infoBox=infoBox)
            sensors.DetachSensor.place_button(row, infoBox=infoBox)

            box.separator()
            infoBox.draw_info()

        # elif sensor_type == 'CONTACT_SENSOR':
        #       assign to collision mesh instead of bone


    box = SensorPropertiesBox.get(layout, context, "Sensor Properties")
    if box:
        infoBox = InfoBox(box)
        row = box.row()

        sensor = getSingleObject(context)

        if sensor:

            if sensor_type == "CAMERA_SENSOR":
                    column = row.column(align=True)
                    column.prop(sensor.data, 'angle_x', text="Horizontal field of view")
                    column = row.column(align=True)
                    column.prop(sensor.data, 'angle_y')
                    row = box.row()
                    column = row.column(align=True)
                    column.prop(sensor.RobotEditor.camera, 'width', text='width (px.)')
                    column = row.column(align=True)
                    column.prop(sensor.RobotEditor.camera, 'height', text="height (px.)")
                    row = box.row()
                    column = row.column(align=True)
                    column.prop(sensor.data, 'clip_start')
                    column = row.column(align=True)
                    column.prop(sensor.data, 'clip_end')
                    row = box.row()
                    row.prop(sensor.RobotEditor.camera, 'format', text="Format")

            elif sensor_type == "CONTACT_SENSOR":
                    column = row.column(align=True)
                    column.prop(bpy.context.active_object.RobotEditor.contactSensor, 'collision', text='collision')
                    column.prop(bpy.context.active_object.RobotEditor.contactSensor, 'topic', text='topic')


            elif sensor_type == "FORCE_TORQUE_SENSOR":
                if sensor.RobotEditor.tag == 'FORCE_TORQUE_SENSOR':
                    column = row.column(align=True)
                    column.prop(bpy.context.active_object.RobotEditor.forceTorqueSensor, 'frame', text='frame')
                    column.prop(bpy.context.active_object.RobotEditor.forceTorqueSensor, 'measure_direction', text='measure direction')

            elif sensor_type == "DEPTH_CAMERA_SENSOR":
                if sensor.RobotEditor.tag == 'DEPTH_CAMERA_SENSOR':
                    column = row.column(align=True)
                    column.prop(bpy.context.active_object.RobotEditor.depthCameraSensor, 'output', text='output')

            elif sensor_type == "ALTIMETER_SENSOR":
                    box.label(text="Vertical Position")
                    box1 = box.box()
                    box1.label(text="Noise")
                    box1.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vptype', text='type')
                    box1.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vpmean', text='mean')
                    box1.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vpstddev', text='stddev')
                    box1.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vpbias_mean', text='bias_mean')
                    box1.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vpbias_stddev', text='bias_stddev')
                    box1.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vpprecision', text='precision')
                    box.label(text="Vertical Velocity")
                    box2 = box.box()
                    box2.label(text="Noise")
                    box2.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vvtype', text='type')
                    box2.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vvmean', text='mean')
                    box2.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vvstddev', text='stddev')
                    box2.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vvbias_mean', text='bias_mean')
                    box2.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vvbias_stddev', text='bias_stddev')
                    box2.prop(bpy.context.active_object.RobotEditor.altimeterSensor, 'vvprecision', text='precision')


            elif sensor_type == "IMU_SENSOR":
                    box.label(text="orientation_reference_frame")
                    box.prop(bpy.context.active_object.RobotEditor.imuSensor, 'localization', text='localization')
                    box.prop(bpy.context.active_object.RobotEditor.imuSensor, 'custom_rpy', text='custom_rpy')
                    box.prop(bpy.context.active_object.RobotEditor.imuSensor, 'grav_dir_x', text='grav_dir_x')
                    box.prop(bpy.context.active_object.RobotEditor.imuSensor, 'parent_frame', text='parent_frame')
                    box.prop(bpy.context.active_object.RobotEditor.imuSensor, 'topic', text='topic')
                    box1 = box.box()
                    box1.label(text="angular_velocity")
                    box1.label(text="x")
                    box1.label(text="noise")
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avxtype', text='type')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avxmean', text='mean')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avxstddev', text='stddev')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avxbias_mean', text='bias_mean')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avxbias_stddev', text='bias_stddev')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avxprecision', text='precision')
                    box1.label(text="y")
                    box1.label(text="noise")
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avytype', text='type')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avymean', text='mean')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avystddev', text='stddev')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avybias_mean', text='bias_mean')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avybias_stddev', text='bias_stddev')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avyprecision', text='precision')
                    box1.label(text="z")
                    box1.label(text="noise")
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avztype', text='type')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avzmean', text='mean')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avzstddev', text='stddev')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avzbias_mean', text='bias_mean')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avzbias_stddev', text='bias_stddev')
                    box1.prop(bpy.context.active_object.RobotEditor.imuSensor, 'avzprecision', text='precision')
                    box2 = box.box()
                    box2.label(text="linear_acceleration")
                    box2.label(text="x")
                    box2.label(text="noise")
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laxtype', text='type')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laxmean', text='mean')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laxstddev', text='stddev')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laxbias_mean', text='bias_mean')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laxbias_stddev', text='bias_stddev')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laxprecision', text='precision')
                    box2.label(text="y")
                    box2.label(text="noise")
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laytype', text='type')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laymean', text='mean')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laystddev', text='stddev')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laybias_mean', text='bias_mean')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laybias_stddev', text='bias_stddev')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'layprecision', text='precision')
                    box2.label(text="z")
                    box2.label(text="noise")
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'laztype', text='type')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'lazmean', text='mean')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'lazstddev', text='stddev')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'lazbias_mean', text='bias_mean')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'lazbias_stddev', text='bias_stddev')
                    box2.prop(bpy.context.active_object.RobotEditor.imuSensor, 'lazprecision', text='precision')

            elif sensor_type == "LASER_SENSOR":
                    column = row.column(align=True)
                    column.prop(bpy.context.active_object.RobotEditor.contactSensor, 'collision', text='Collision')

            else:
                infoBox.add_message('No sensor (or more than one) selected')
                # sensors.ConvertCameraToSensor.place_button(row,"Convert to laser scanner sensor",infoBox).sensor_type = "LASER_SENSOR"

                if sensor.type == 'CAMERA':
                    sensors.ConvertCameraToSensor.place_button(row, "Convert to camera sensor",
                                               infoBox).sensor_type = "CAMERA_SENSOR"
        row = box.row()
        column = row.column(align=True)
        infoBox.draw_info()
