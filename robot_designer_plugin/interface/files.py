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
#   2017:       Benedikt Feldotto (TUM), SDF and URDF re-integration, GUI unification, Model MetaData
# ######

# Blender imports
import bpy

# RobotDesigner imports
from .model import check_armature
from ..core import PluginManager
from ..core.gui import InfoBox
from ..properties.globals import global_properties
from ..operators import file_tools
from .helpers import DebugBox


def draw(layout, context):
    """
    Draws the user interface for file operations (i.e., import/export)

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """

    if context.active_object and context.active_object.type == 'ARMATURE':
        box = layout.box()
        box.label(text="Model Meta Data")

        model_box = box.box()
        model_box.label(text="Description")

        global_properties.model_name.prop(context.scene, model_box)

        model_box.prop(bpy.context.active_object.RobotDesigner.modelMeta, 'model_config', text='Config Name')
        model_box.prop(bpy.context.active_object.RobotDesigner.modelMeta, 'model_version', text='Version')
        model_box.prop(bpy.context.active_object.RobotDesigner.modelMeta, 'model_description', text='Description')
        model_box.prop(bpy.context.active_object.RobotDesigner.modelMeta, 'model_folder', text='Folder Name')

        author_box = box.box()
        author_box.label(text="Author")

        ## todo support multiple authors
        # file.CreateAuthor.place_button(author_box, "Create new")
        # author_box.menu(menus.AuthorMenu.bl_idname, text="Author 1")

        author_box.prop(bpy.context.active_object.RobotDesigner.author, 'authorName', text='Name')
        author_box.prop(bpy.context.active_object.RobotDesigner.author, 'authorEmail', text='Email')

    file_box = layout.box()
    file_box.label(text='Import/Export')

    # # GIT upload/download support functions
    # global_properties.storage_mode.prop(context.scene,layout, expand=True)
    # storage_mode = global_properties.storage_mode.get(context.scene)
    # #
    # if storage_mode == 'local':
    #     pass
    # elif storage_mode == 'git':
    #      global_properties.git_repository.prop(context.scene, layout)
    #      global_properties.git_url.prop(context.scene, layout)
    # elif storage_mode == 'temporary':
    #      global_properties.git_url.prop(context.scene, layout)

    row = file_box.row()
    global_properties.export_thumbnail.prop(context.scene, row)
    row = file_box.row()
    column = row.column()

    plugins = []
    for plugin in PluginManager.getFilePlugins(PluginManager.PluginTypes.FILE):
        label, operators, draw_function, _ = plugin

        if not label in plugins:
            box = column.box()
            row2 = box.row(align=True)

            column2 = row2.column(align=True)
            column2.label(text=label)
            button_columns = row2.column()
            row_import = button_columns.row()
            column_import = row_import.column(align=True)
            row_export = button_columns.row()
            column_export = row_export.column(align=True)

            info_row = button_columns.row()
            infoBox = InfoBox(info_row)


            if not draw_function:
                for operator in operators[:len(operators)//2]:
                    # Import operators
                    operator.place_button(layout=column_import, infoBox=infoBox)

                for operator in operators[len(operators)//2:]:
                    # Export operators
                    operator.place_button(layout=column_export, infoBox=infoBox)

            infoBox.draw_info()
        plugins.append(label)


    tools_box = layout.box()
    tools_box.label(text='File Tools')

    row = tools_box.row(align=True)
    row.operator(file_tools.ConvertDAEPackages.bl_idname)
    row = tools_box.row(align=True)
    row.operator(file_tools.StlToDaeConverter.bl_idname)

    layout.separator()
    row = layout.row()
    debug_box = DebugBox.get(row, context, "Debug Tools")
    if debug_box:

        row = debug_box.row()
        row.label(text='Level')
        global_properties.operator_debug_level.prop(bpy.context.scene, row, expand=True)

        row = debug_box.column(align=False)
        row.operator(file_tools.PrintTransformations.bl_idname)
        row.operator('script.reload', text="Reload Addon Scripts")



