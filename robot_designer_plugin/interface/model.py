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
#   2015:       Stefan Ulbrich (FZI), Gui redesigned
#   2015-01-16: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
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

# ######
# RobotDesigner imports
from .helpers import create_segment_selector
from ..core.logfile import LogFunction
from ..core.gui import InfoBox
from ..operators import model, segments
from . import menus
from .helpers import drawInfoBox, push_info, ModelPropertiesBox

from ..operators.helpers import PoseMode, NotEditMode

@LogFunction
def check_armature(layout, context):
    """
    Helper function that checks whether a :ref:`armature` is selected. If not it draws a selection box.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    :return: Whether a robot model is selected (Bool).
    """
    if context.active_object is not None and context.active_object.type == 'ARMATURE':
        return True
    else:
        layout.menu(menus.ModelMenu.bl_idname, text="Select Robot")
        return False

@LogFunction
def draw(layout, context):
    """
    Draws the user interface for modifying the model.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    is_model_selected = False
    if context.active_object and context.active_object.type == 'ARMATURE':

        is_model_selected = True

        box = layout.box()
        infoBox=InfoBox(box)

        row = box.row(align=True)
        row.label(text="Select Robot:")
        menus.ModelMenu.putMenu(row, context, text=context.active_object.name)

        row.operator('view3d.view_lock_to_active')
        row = box.row(align=True)
        model.RenameModel.place_button(row, infoBox=infoBox)
        row.separator()
        model.RebuildModel.place_button(row, infoBox=infoBox)

        row = box.row(align=True)
        row.label(text="Merge with another robot model")
        menus.JoinModelMenu.putMenu(row, context, text="")
        layout.separator()
        infoBox.draw_info()

        box = layout.box()
        infoBox = InfoBox(box)
        box.label("Segment structure:")

        if context.active_bone and context.active_bone.parent:
            parent_name = context.active_bone.parent.name
        else:
            parent_name = ""

        row = box.row(align=True)
        left_column = row.column(align=True)
        create_segment_selector(left_column, context)
        left_column.operator("pose.select_all", text="Deselect all").action="DESELECT"
        row.separator()
        right_column = row.column(align=False)
        segments.RenameSegment.place_button(right_column, infoBox=infoBox)
        segments.CreateNewSegment.place_button(right_column, text="Create new child Bone", infoBox=infoBox)
        segments.InsertNewParentSegment.place_button(right_column, text="Create new Parent Bone", infoBox=infoBox)
        right_column.separator()
        segments.DeleteSegment.place_button(right_column, text="Delete active Bone", infoBox=infoBox)
        left_column.separator()
        row = box.row()
        row.label("Re-assign parent:")
        menus.AssignParentMenu.putMenu(row, context,text=parent_name)
        infoBox.draw_info()


        box = ModelPropertiesBox.get(layout, context, 'Model properties')
        if box:
            row = box.row(align=True)
            column = row.column(align=True)
            column.label("Custom coordinate frames:")
            column = row.column(align=True)
            column.menu(menus.CoordinateFrameMenu.bl_idname, text='None')

        box = layout.box()
        box.label(text="Custom Gazebo tags")
        box.prop(bpy.context.scene.RobotEditor, "gazeboTags", slider=True)
    else:
        layout.menu(menus.ModelMenu.bl_idname, text="Select Robot")
        layout.label(text="Select robot first")

    push_info(PoseMode)
    drawInfoBox(layout, context)#["Some operations require to be in pose mode"] if context.mode == "OBJECT" else [])
    return is_model_selected
