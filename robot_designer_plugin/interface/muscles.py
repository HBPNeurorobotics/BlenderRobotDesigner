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
# Copyright (c) 2017, Technical University Munich
#
#
# ######

# Blender imports
import bpy

# RobotDesigner imports
from .model import check_armature

import math

from . import menus
from ..operators import sensors
from .helpers import getSingleObject, getSingleSegment, info_list, AttachSensorBox, DetachSensorBox, SensorPropertiesBox
from ..core.gui import InfoBox
from ..properties.globals import global_properties
from ..operators import model, muscles, segments

from .helpers import create_segment_selector

def draw(layout, context):
    """
    Draws the user interface for geometric modelling.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return

    box = layout.box()
    row = box.row()
    row.label("Show:")
    global_properties.display_muscle_selection.prop(context.scene, row, expand=True)

    box = AttachSensorBox.get(layout, context, "Muscles", icon="LINKED")
    if box:
        infoBox = InfoBox(box)

        active_model = global_properties.model_name.get(context.scene)
        active_muscle = global_properties.active_muscle.get(bpy.context.scene)

        row1 = box.row()

        column = row1.column(align=True)
        column.menu(menus.MuscleMenu.bl_idname,
                    text=global_properties.active_muscle.get(bpy.context.scene))# if global_properties.active_muscle.get(bpy.context.scene) else "Select Segment")

        column = row1.column(align=True)
        muscles.CreateNewMuscle.place_button(column, text="Create new muscle", infoBox=infoBox)
        muscles.DeleteMuscle.place_button(column, text="Delete active muscle", infoBox=infoBox)

        row2 = box.row()

        if active_muscle != '':
            pointbox = box.box()
            row3 = pointbox.row()
            row3.label(text="Muscle attachment points")

            row4 = pointbox.row()
            column = row4.column(align=True)
            muscles.CreateNewPathpoint.place_button(column, text="Add new pathpoint", infoBox=infoBox)

            i = 0
            # put pathpoints
            for obj in bpy.data.objects[active_muscle].data.splines[0].points:
                row5 = pointbox.row(align=True)
                i = i + 1
       #        x.label(text=obj.name)
      #         row5.prop(obj, 'x', text='X')
      #         row5.prop(obj, 'y', text='Y')
      #         row5.prop(obj, 'z', text='Z')
                row5.prop(obj, 'co', text=str(i))

                #row5.prop(bpy.data.objects[active_muscle].RobotEditor.muscles.pathpoints[0], 'coordFrame')

                row5.prop(bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[i-1], 'coordFrame', text='')

                muscles.MovePathpointUp.place_button(row5, text='', icon='TRIA_UP', infoBox=infoBox).nr = i
                muscles.MovePathpointDown.place_button(row5, text='', icon='TRIA_DOWN', infoBox=infoBox).nr = i

                bone = bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[i-1].coordFrame
                muscles.DeletePathpoint.place_button(row5, infoBox=infoBox, icon="X_VEC").pathpoint = i

        row6 = pointbox.row()
        row7 = pointbox.row()

        row7.label(text="Attach segments to pathpoints")
      #  bone = bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[0].coordFrame


        x = menus.SegmentsMusclesMenu
        x.nr = 0
        row7.menu(x.bl_idname, text="Select Segment")
        print(bpy.ops.roboteditor.calc_muscle_length)

       # bpy.ops.roboteditor.calc_muscle_length(muscle="m") #.execute(context) #(.place_button(row5, infoBox=infoBox, icon="X_VEC"))

        row = box.row()



      #  row.prop(bpy.data.objects[active_muscle].RobotEditor.muscles, 'length', text="Muscle length:")

    #    bpy.data.objects['wer'].RobotEditor.muscles.pathPoints[0].coordFrame = "hoolla"

        row = box.row()
        if active_muscle != '':
            row.prop(bpy.data.objects[active_muscle].RobotEditor.muscles,
                 'muscleType', text='Muscle Type')
        box.row()

        infoBox.draw_info()
