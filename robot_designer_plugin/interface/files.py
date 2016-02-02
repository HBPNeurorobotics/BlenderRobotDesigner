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
from ..core import PluginManager
from ..core.gui import InfoBox

def draw(layout, context):
    """
    Draws the user interface for file operations (i.e., import/export)

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    layout = layout.box()
    layout.label('Import/Export')
    layout.prop(bpy.context.scene.RobotEditor, "storageMode", expand=True)
    if bpy.context.scene.RobotEditor.storageMode == 'local':
        pass
    elif bpy.context.scene.RobotEditor.storageMode == 'git':
        layout.prop(bpy.context.scene.RobotEditor, "gitRepository")
        layout.prop(bpy.context.scene.RobotEditor, "gitURL")
    elif bpy.context.scene.RobotEditor.storageMode == 'temporary':
        layout.prop(bpy.context.scene.RobotEditor, "gitURL")

    row = layout.row()
    column = row.column()

    for plugin in PluginManager.getFilePlugins(PluginManager.PluginTypes.FILE):
        label, operators, draw_function, _ = plugin

        box = column.box()
        row2 =box.row(align=True)
        infoBox = InfoBox(row2)
        column2 = row2.column(align=True)
        column2.label(text=label)
        column2 = row2.column(align=True)
        if not draw_function:
            for operator in operators:
                operator.place_button(layout=column2, infoBox=infoBox)
        row2=box.row(align=True)
        infoBox.draw_info()

    row = layout.row()
    column = row.column()
    #column.label('Import:')
    # if use_simox:
    #     column.operator("roboteditor.simoximport")
    # if use_mmm:
    #     column.operator("roboteditor.mmmimport")
    #column.operator("roboteditor.urdfimport")

    #column = row.column()

    #column.label('export:')
    #if context.mode == 'OBJECT':
    #    if check_armature(column, context):
    #        column.prop(bpy.context.scene.RobotEditor, "modelFolderName")
    #        column.operator("roboteditor.urdfexport")
    #        # column.operator("roboteditor.colladaexport")
    #else:
    #    column.label('Please activate object mode for export')
