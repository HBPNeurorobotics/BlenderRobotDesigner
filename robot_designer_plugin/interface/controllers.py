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
from .helpers import ControllerBox, ControllerLimitsBox


def draw(layout, context):
    """
    Draws the user interface for modifying the joint controller of a segment.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """

    if not check_armature(layout, context):
        return
    if context.active_bone is not None:

        box = ControllerLimitsBox.get(layout, context, 'Limits')
        if box:
            box.prop(context.active_bone.RobotDesigner.controller, "maxVelocity")
            box.prop(context.active_bone.RobotDesigner.controller, "maxTorque")
            box.prop(context.active_bone.RobotDesigner.controller, "acceleration")
            box.prop(context.active_bone.RobotDesigner.controller, "deceleration")
            box.prop(context.active_bone.RobotDesigner.controller, "isActive")
            box.label("Joint Limits:")
            if context.active_bone.RobotDesigner.jointMode == 'REVOLUTE':
                box.prop(context.active_bone.RobotDesigner.theta, "min")
                box.prop(context.active_bone.RobotDesigner.theta, "max")
            else:
                box.prop(context.active_bone.RobotDesigner.d, "min")
                box.prop(context.active_bone.RobotDesigner.d, "max")

        layout.separator()

        box = ControllerBox.get(layout, context, 'Controller')
        if box:
            box.label("Joint controller:")
            box.prop(context.active_bone.RobotDesigner.jointController, "isActive")
            box.prop(context.active_bone.RobotDesigner.jointController, "controllerType")
            box.separator()
            box.prop(context.active_bone.RobotDesigner.jointController, "P")
            box.prop(context.active_bone.RobotDesigner.jointController, "I")
            box.prop(context.active_bone.RobotDesigner.jointController, "D")
