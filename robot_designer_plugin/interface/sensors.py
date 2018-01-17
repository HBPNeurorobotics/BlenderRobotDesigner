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
    column.label("Sensor type:")
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

    box = AttachSensorBox.get(sensorbox, context, "Attach/Detach", icon="LINKED")
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


    box = SensorPropertiesBox.get(sensorbox, context, "Sensor Properties", icon="SCRIPTWIN")
    if box:
        infoBox = InfoBox(box)
        row = box.row()

        sensor = getSingleObject(context)

        if sensor:

            if sensor_type == "CAMERA_SENSOR":
                if sensor.RobotEditor.tag == 'CAMERA_SENSOR':
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
                else:
                    infoBox.add_message('Selected object is no camera sensor')
                    if sensor.type == 'CAMERA':
                        sensors.ConvertCameraToSensor.place_button(row, "Convert to camera sensor",
                                                                   infoBox).sensor_type = "CAMERA_SENSOR"

            # add more sensors here:
            # elif sensor_type == " xxxx"
                    # show properties

            elif sensor_type == "LASER_SENSOR":
                if sensor.RobotEditor.tag == 'LASER_SENSOR':
                    pass
                else:
                    infoBox.add_message('Selected object is no camera sensor')
                    if sensor.type == 'CAMERA':
                        # sensors.ConvertCameraToSensor.place_button(row,"Convert to laser scanner sensor",infoBox).sensor_type = "LASER_SENSOR"
                        pass
        else:
            infoBox.add_message('No sensor (or more than one) selected')

        row = box.row()
        column = row.column(align=True)
        infoBox.draw_info()
