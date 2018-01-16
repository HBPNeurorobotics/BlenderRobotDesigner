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
from bpy.props import EnumProperty

# ######
# RobotDesigner imports

from ..core import config, PluginManager
from ..core.gui import InfoBox
from ..properties.globals import global_properties
from .helpers import DebugBox

@PluginManager.register_class
class UserInterface(bpy.types.Panel):
    bl_label = "NRP Robot Designer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "HBP"
    bl_options = {"HIDE_HEADER"}


    from ..core.logfile import LogFunction
    @LogFunction

    def draw(self, context):
        from ..operators import gui
        from . import files, model, segments, geometries, sensors, muscles, world
        layout = self.layout

        layout.label("HBP Neurorobotics RobotDesigner", icon_value=PluginManager.get_icon('hbp'))
        layout.separator()

        global_properties.gui_tab.prop(bpy.context.scene, layout, expand=True)
        control = global_properties.gui_tab.get(bpy.context.scene)
        layout.separator()

        if control == 'armatures':
            model.draw(layout, context)
        elif control == 'bones':
            segments.draw(layout, context)
        elif control == 'meshes':
            geometries.draw(layout, context)
        elif control == 'sensors':
            sensors.draw(layout,context)
        if control == 'muscles':
            muscles.draw(layout, context)
        # elif control == 'markers':
        #     markers.draw(layout, context)
        elif control == 'files':
            files.draw(layout, context)
        elif control == 'world':
            world.draw(layout, context)
        elif control == 'tools':
            row = layout.row(align=True)
            row.operator(gui.PrintTransformations.bl_idname)
            row = layout.row(align=True)
            global_properties.operator_debug_level.prop(bpy.context.scene,row, expand=True)

        row = layout.row(align=True)
        row.label("Set Mode")
        if context.active_object:
            row.operator("object.mode_set", text="Object Mode").mode = 'OBJECT'
            if context.active_object.type == "ARMATURE":
                row.operator("object.mode_set", text="Pose Mode").mode = 'POSE'


        layout.separator()
        row = layout.row(align=True)

        if InfoBox.global_messages:
            box = DebugBox.get(row, context, "Debug")
            if box:
                box.label("press <F8> to clear", icon="INFO")
                InfoBox.draw_global_info(box)


    def draw_header(self, context):
        layout = self.layout
        obj = context.object
        layout.label("Hello World")
        layout.prop(obj, "select", text="testst")