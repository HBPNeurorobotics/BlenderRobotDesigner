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
from ..operators import rigid_bodies, soft_bodies, collision, mesh_generation
from .helpers import drawInfoBox, info_list, CameraSensorBox
from ..core.gui import InfoBox
from ..properties.globals import global_properties

def draw(layout, context):
    """
    Draws the user interface for geometric modelling.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return

    if len([i for i in context.selected_objects if i.type=="MESH"])==0:
        info_list.append("No mesh selected")
    elif len(context.selected_objects)>2:
        info_list.append("Too many objects selected")

    box = layout.box()
    row = box.row(align=True)
    row.label("Mesh type:")
    row.prop(bpy.context.scene, "meshType", expand=True)
    row = box.row(align=True)
    row.label("Show:")
    global_properties.display_mesh_selection.prop(context.scene, row, expand=True)
    box.separator()

    box = CameraSensorBox.get(layout, context, "Cameras", icon="CAMERA_DATA")
    if box:
        infoBox = InfoBox(box)
        row = box.row()
        column = row.column(align=True)
        menus.CameraSensorMenu.putMenu(column, context)

        column = row.column(align=True)
        rigid_bodies.DetachGeometry.place_button(column, infoBox=infoBox)
        rigid_bodies.DetachAllGeometries.place_button(column, infoBox=infoBox)
        rigid_bodies.RenameAllGeometries.place_button(column, infoBox=infoBox)
        rigid_bodies.SetGeometryActive.place_button(column, infoBox=infoBox)
        rigid_bodies.SelectAllGeometries.place_button(column, infoBox=infoBox)
        selected_objects = [i for i in context.selected_objects if i.name != context.active_object.name]
        if len(selected_objects):
            box.prop(selected_objects[0].RobotEditor, 'fileName')
        box.separator()
        infoBox.draw_info()

    drawInfoBox(layout,context)
