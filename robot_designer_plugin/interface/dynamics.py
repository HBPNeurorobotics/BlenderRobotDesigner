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

# Blender imports
import bpy

# RobotDesigner imports
from ..operators import dynamics
from . import menus
from .model import check_armature
from ..properties.globals import global_properties

def draw(layout, context):
    """
    Draws the user interface for modifying the dynamic properties of a segment.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return
    layout.operator(dynamics.CreatePhysical.bl_idname)
    layout.label("Select Physics Frame:")
    topRow = layout.column(align=False)
    frameMenuText = ""
    frame_name = global_properties.physics_frame_name.get(context.scene)
    if context.active_bone and frame_name:
        if frame_name in bpy.data.objects:
            frame = bpy.data.objects[frame_name]

            if frame.parent_bone:
                frameMenuText = frame_name + " --> " + frame.parent_bone
            else:
                frameMenuText = frame_name

    topRow.menu(menus.MassObjectMenu.bl_idname, text=frameMenuText)
    topRow.operator(dynamics.DetachPhysical.bl_idname)

    if frame_name:
        frame = bpy.data.objects[frame_name]
        layout.prop(frame.RobotEditor.dynamics, "mass")
        layout.separator()
        layout.prop(frame.RobotEditor.dynamics, "inertiaTensor")

    layout.label("Select Bone:")
    lower_row = layout.column(align=False)
    lower_row.menu(menus.SegmentsMenu.bl_idname, text=context.active_bone.name)
    lower_row.operator(dynamics.AssignPhysical.bl_idname)
