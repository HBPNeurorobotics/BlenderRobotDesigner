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
    column.label(text="Show:")
    column = row.column(align=True)
    row = column.row(align=True)
    global_properties.display_sensor_type.prop(context.scene, row, expand=True)

    box = layout.box()
    box.label(text="-- Import/Export of Sensors in Development --")
    row = column.row(align=True)

    sensorbox = layout.box()
    sensorbox.label(text="Select Sensor:")
    row = sensorbox.row()
    columnl = row.column()
    menus.SensorMenu.putMenu(columnl, context)

    columnr = row.column(align=True)

    infoBox = InfoBox(sensorbox)
    mode = global_properties.display_sensor_type.get(context.scene)
    sensors.CreateSensor.place_button(columnr, "Create New Sensor").sensor_type = mode
    sensors.RenameSensor.place_button(columnr, text="Rename Active Sensor", infoBox=infoBox)
    sensors.DeleteSensor.place_button(columnr, text="Delete Active Sensor", infoBox=infoBox)

    tag = bpy.data.objects[global_properties.active_sensor.get(context.scene)].RobotDesigner.tag
    sensor_type = bpy.data.objects[global_properties.active_sensor.get(context.scene)].RobotDesigner.sensor_type

    row = sensorbox.row()
    row.prop(bpy.data.objects[global_properties.active_sensor.get(context.scene)].RobotDesigner, 'sensor_type',
             text="Sensor Type")

    if tag == 'SENSOR':
        box = AttachSensorBox.get(layout, context, "Attach/Detach", icon="LINKED")

        if box:
            infoBox = InfoBox(box)
            row = box.row()

            if sensor_type in ['CAMERA_SENSOR', 'DEPTH_CAMERA_SENSOR', 'LASER_SENSOR', 'ALTIMETER_SENSOR',
                               'IMU_SENSOR']:
                # sensor that can be attached to segment
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
                row = box.column(align=True)
                sensors.AttachSensor.place_button(row, infoBox=infoBox)
                sensors.DetachSensor.place_button(row, infoBox=infoBox)

                box.separator()
                infoBox.draw_info()

            elif sensor_type == 'FORCE_TORQUE_SENSOR':
                # todo sensor that can be attached to joints
                row.label(text='Not Supported Yet')

            elif sensor_type == 'CONTACT_SENSOR':
                # todo sensor that can be attached to collision mesh
                row.label(text='Not Supported Yet')

        box = SensorPropertiesBox.get(layout, context, "Sensor Properties")
        if box:
            infoBox = InfoBox(box)
            row = box.row()

            sensor = getSingleObject(context)

            if sensor_type == "CAMERA_SENSOR":
                column = row.column(align=True)
                column.prop(sensor.data, 'angle_x', text="Horizontal Field of View")
                column = row.column(align=True)
                column.prop(sensor.data, 'angle_y')
                row = box.row()
                column = row.column(align=True)
                column.prop(sensor.RobotDesigner.cameraSensor, 'width', text='Width (px.)')
                column = row.column(align=True)
                column.prop(sensor.RobotDesigner.cameraSensor, 'height', text="Height (px.)")
                row = box.row()
                column = row.column(align=True)
                column.prop(sensor.data, 'clip_start')
                column = row.column(align=True)
                column.prop(sensor.data, 'clip_end')
                row = box.row()
                row.prop(sensor.RobotDesigner.cameraSensor, 'format', text="Format")
                noisebox = box.box()
                noisebox.label(text="Noise")
                row = noisebox.row()
                row.prop(sensor.RobotDesigner.cameraSensor.noise, 'type', text="Type")
                row.prop(sensor.RobotDesigner.cameraSensor.noise, 'mean', text="Mean")
                row.prop(sensor.RobotDesigner.cameraSensor.noise, 'stddev', text="Stddev")

            elif sensor_type == "CONTACT_SENSOR":
                column = row.column(align=True)
                column.prop(bpy.context.active_object.RobotDesigner.contactSensor, 'collision', text='Collision')
                column.prop(bpy.context.active_object.RobotDesigner.contactSensor, 'topic', text='Topic')


            elif sensor_type == "FORCE_TORQUE_SENSOR":
                column = row.column(align=True)
                column.prop(bpy.context.active_object.RobotDesigner.forceTorqueSensor, 'frame', text='Frame')
                column.prop(bpy.context.active_object.RobotDesigner.forceTorqueSensor, 'measure_direction',
                            text='measure direction')

            elif sensor_type == "DEPTH_CAMERA_SENSOR":
                column = row.column(align=True)
                column.prop(bpy.context.active_object.RobotDesigner.depthCameraSensor, 'output', text='Output')

            elif sensor_type == "ALTIMETER_SENSOR":
                row = box.row(align=True)
                col1 = row.column(align=True)
                col2 = row.column(align=True)

                col1.label(text="Vertical Position")
                col1.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vptype')
                col1.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vpmean')
                col1.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vpstddev')
                col1.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vpbias_mean')
                col1.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vpbias_stddev')
                col1.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vpprecision')
                col2.label(text="Vertical Velocity")

                col2.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vvtype')
                col2.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vvmean')
                col2.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vvstddev')
                col2.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vvbias_mean')
                col2.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vvbias_stddev')
                col2.prop(bpy.context.active_object.RobotDesigner.altimeterSensor, 'vvprecision')


            elif sensor_type == "IMU_SENSOR":
                box0 = box.box()
                box0.label(text="Orientation Reference Frame")

                row1 = box0.row(align=True)
                row2 = box0.row(align=True)
                row3 = box0.row(align=True)
                row4 = box0.row(align=True)
                row5 = box0.row(align=True)
                row1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'localization', text='Localization')
                row2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'custom_rpy', text='Custom_rpy')
                row3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'grav_dir_x', text='Grav_dir_x')
                row4.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'parent_frame', text='Parent_frame')
                row5.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'topic', text='Topic')

                box1 = box.box()
                box1.label(text="Angular Velocity")

                row = box1.row(align=True)
                col1 = row.column(align=True)
                col2 = row.column(align=True)
                col3 = row.column(align=True)

                col1.label(text="x")
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avxtype')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avxmean')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avxstddev')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avxbias_mean')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avxbias_stddev')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avxprecision')
                col2.label(text="y")
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avytype')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avymean')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avystddev')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avybias_mean')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avybias_stddev')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avyprecision')
                col3.label(text="z")
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avztype')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avzmean')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avzstddev')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avzbias_mean')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avzbias_stddev')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'avzprecision')

                box2 = box.box()
                box2.label(text="Linear Acceleration")

                row = box2.row(align=True)
                col1 = row.column(align=True)
                col2 = row.column(align=True)
                col3 = row.column(align=True)

                col1.label(text="x")
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laxtype')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laxmean')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laxstddev')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laxbias_mean')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laxbias_stddev')
                col1.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laxprecision')
                col2.label(text="y")
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laytype')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laymean')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laystddev')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laybias_mean')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laybias_stddev')
                col2.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'layprecision')
                col3.label(text="z")
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'laztype')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'lazmean')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'lazstddev')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'lazbias_mean')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'lazbias_stddev')
                col3.prop(bpy.context.active_object.RobotDesigner.imuSensor, 'lazprecision')

            elif sensor_type == "LASER_SENSOR":
                column = row.column(align=True)
                column.prop(bpy.context.active_object.RobotDesigner.laserSensor, 'horizontal_samples',
                            text='Horizontal Samples')
                column.prop(bpy.context.active_object.RobotDesigner.laserSensor, 'vertical_samples',
                            text='Vertical Samples')
                column.prop(bpy.context.active_object.RobotDesigner.laserSensor, 'resolution', text='Resolution')


            else:
                infoBox.add_message('No Sensor (or More Than One) Selected')
                # sensors.ConvertCameraToSensor.place_button(row,"Convert to laser scanner sensor",infoBox).sensor_type = "LASER_SENSOR"

    if tag != 'SENSOR':
        if bpy.data.objects[global_properties.active_sensor.get(context.scene)].type == 'CAMERA':
            row = sensorbox.row()
            sensors.ConvertCameraToSensor.place_button(row, "Convert to Camera Sensor",
                                                       infoBox).sensor_type = "CAMERA_SENSOR"
        row = box.row()
        column = row.column(align=True)
        infoBox.draw_info()
