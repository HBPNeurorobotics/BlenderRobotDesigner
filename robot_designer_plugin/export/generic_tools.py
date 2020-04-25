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
# Copyright (c) 2020, TU Munich
#
# ######

import bpy
from robot_designer_plugin.core import config, PluginManager, RDOperator


def create_thumbnail(toplevel_directory):
    """
    Create a rendered thumbnail file and export it.
    """

    # set storing parameters
    bpy.data.scenes['Scene'].render.filepath = toplevel_directory + "/thumbnail.png"
    bpy.context.scene.render.resolution_x = 600
    bpy.context.scene.render.resolution_y = 600

    # render and save file
    bpy.ops.render.render(write_still=True, use_viewport=True)