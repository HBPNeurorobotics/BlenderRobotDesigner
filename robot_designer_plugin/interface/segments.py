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
from .model import check_armature
from . import kinematics, controllers, dynamics
from .helpers import create_segment_selector
from ..operators import segments
from ..core.pluginmanager import PluginManager
from ..properties.globals import RDGlobals

def draw(layout, context):
    """
    Draws the user interface for modifying segments.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return
    # layout.label("Active Bone:")
    if context.active_bone is not None:

        box = layout.box()
        row = box.row(align=True)
        column = row.column(align=True)
        column.label('Active segment:')
        column = row.column(align=True)
        create_segment_selector(column, context)

        box = layout.box()
        row = box.row()

        if not context.active_bone.RobotEditor.RD_Bone:
            row.label("Not a bone created by the Robot designer")
            row = box.row()
            row.operator(segments.ImportBlenderArmature.bl_idname, text="Import native Blender segmet")
            row.prop(context.active_bone.RobotEditor, "RD_Bone")

        else:
            row.label("Edit:")

            print(PluginManager.get_property(bpy.context.scene, RDGlobals.boneMode))

            row.prop(bpy.context.scene.RobotEditor, "boneMode", expand=True)

            if bpy.context.scene.RobotEditor.boneMode == "kinematics":
                kinematics.draw(box, context)
            elif bpy.context.scene.RobotEditor.boneMode == "dynamics":
                dynamics.draw(box, context)
            elif bpy.context.scene.RobotEditor.boneMode == "controller":
                controllers.draw(box, context)

    else:
        layout.operator(segments.CreateNewSegment.bl_idname, text="Create new base bone")
