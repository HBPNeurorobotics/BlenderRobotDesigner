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
from ..core.gui import InfoBox
from .helpers import getSingleSegment, getSingleObject


def draw(layout, context):
    """
    Draws the user interface for modifying the dynamic properties of a segment.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return

    settings = layout.row()
    global_properties.display_physics_selection.prop(context.scene, settings)

    box = layout.box()
    box.label("Select mass object")
    infoBox = InfoBox(box)
    row = box.row()
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

    column = row.column(align=True)
    menus.MassObjectMenu.putMenu(column, context)
    # create_geometry_selection(column, context)
    row = box.column(align=True)
    dynamics.CreatePhysical.place_button(row,infoBox=infoBox)
    dynamics.ComputePhysical.place_button(row,infoBox=infoBox)

    #dynamics.AssignPhysical.place_button(row,infoBox=infoBox)
    #dynamics.DetachPhysical.place_button(row,infoBox=infoBox)


    obj = getSingleObject(context)
    if obj and obj.RobotEditor.tag=="PHYSICS_FRAME":
        frame_name = global_properties.physics_frame_name.get(context.scene)
        box = layout.box()
        box.label("Properties", icon="MODIFIER")
        frame = bpy.data.objects[frame_name]
        box.prop(frame.RobotEditor.dynamics, "mass")
        box.separator()

        row_t = box.row(align=True)
        row_r = box.row(align=True)

        active_physics_frame = global_properties.physics_frame_name.get(context.scene)

        row_t.prop(bpy.data.objects[active_physics_frame], 'location', text="Translation")
        row_r.prop(bpy.data.objects[active_physics_frame], 'rotation_euler', text="Rotation")

        ## old

        ## delete this from the roboteditor
       # row_t.prop(frame.RobotEditor.dynamics, "inertiaTrans")
       # row_r.prop(frame.RobotEditor.dynamics, "inertiaRot")

        row0 = box.row(align=True)
        row1 = box.row(align=True)
        row2 = box.row(align=True)
        row3 = box.row(align=True)
        row0.label("Inertia Matrix")
        row1.prop(frame.RobotEditor.dynamics, "inertiaXX")
        row2.prop(frame.RobotEditor.dynamics, "inertiaXY")
        row3.prop(frame.RobotEditor.dynamics, "inertiaXZ")
        row1.prop(frame.RobotEditor.dynamics, "inertiaXY")
        row2.prop(frame.RobotEditor.dynamics, "inertiaYY")
        row3.prop(frame.RobotEditor.dynamics, "inertiaYZ")
        row1.prop(frame.RobotEditor.dynamics, "inertiaXZ")
        row2.prop(frame.RobotEditor.dynamics, "inertiaYZ")
        row3.prop(frame.RobotEditor.dynamics, "inertiaZZ")

    infoBox.draw_info()
