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

# RobotDesigner imports
from .model import check_armature
from .helpers import ControllerBox
from ..core.logfile import LogFunction


@LogFunction
def draw(layout, context):
    """
    Draws the user interface for modifying the joint controller of a segment.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """

    if not check_armature(layout, context):
        return
    if context.active_bone is not None:
        # Joint controller properties
        # Only shown for child segments. Unless root segment is connected to world
        control_box = ControllerBox.get(layout, context, "Joint Controller Plugin")
        if control_box:
            if not (context.active_bone.parent is not None) or (
                context.active_bone.RobotDesigner.world is True
            ):
                control_box.label(text="No Joint defined for this Link.")
            else:
                control_box.prop(
                    context.active_bone.RobotDesigner.jointController,
                    "isActive",
                    text="Active Controller",
                )
                control_box.prop(
                    context.active_bone.RobotDesigner.jointController, "controllerType"
                )
                control_box.separator()
                control_box.prop(context.active_bone.RobotDesigner.jointController, "P")
                control_box.prop(context.active_bone.RobotDesigner.jointController, "I")
                control_box.prop(context.active_bone.RobotDesigner.jointController, "D")
