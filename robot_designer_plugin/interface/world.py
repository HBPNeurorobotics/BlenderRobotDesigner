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
from .helpers import EditMusclesBox
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

    # General Properties
    box = layout.box()
    box.label(text="Active Specification")
    global_properties.world_s_name.prop(bpy.context.scene, box)
    global_properties.gravity.prop(bpy.context.scene, box)

    # Light Probperties
    box1 = box.box()
    box1.label(text="Light")
    #todo change to dropdown just like adding a sensor
    global_properties.light_s_name.prop(bpy.context.scene, box1)
    global_properties.cast_shadows.prop(bpy.context.scene, box1)
    global_properties.diffuse.prop(bpy.context.scene, box1)
    global_properties.specular.prop(bpy.context.scene, box1)

    # Included Models
    box2 = box.box()
    box2.label(text="Insert robot models here via dropdown menu ")
    #todo list all added robots