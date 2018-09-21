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

import bpy
from ..properties.globals import global_properties


def draw(layout, context):
    """
    Draw method that builds the part of the GUI responsible for the bone submenu.

    :param layout:
    :param context:
    :return:
    """

    layout.label("Parent Mode:")
    layout.prop(context.active_bone.RobotDesigner, "parentMode", expand=True)
    parent_column = layout.column(align=True)

    if context.active_bone.RobotDesigner.parentMode == 'EULER':
        parent_column.label("Euler position:")
        parent_column.prop(context.active_bone.RobotDesigner.Euler.x, "value", slider=False, text="x")
        parent_column.prop(context.active_bone.RobotDesigner.Euler.y, "value", slider=False, text="y")
        parent_column.prop(context.active_bone.RobotDesigner.Euler.z, "value", slider=False, text="z")
        parent_column.separator()
        parent_column.label("Euler rotation in xy'z''")
        parent_column.prop(context.active_bone.RobotDesigner.Euler.alpha, "value", slider=False, text="alpha")
        parent_column.prop(context.active_bone.RobotDesigner.Euler.beta, "value", slider=False, text="beta")
        parent_column.prop(context.active_bone.RobotDesigner.Euler.gamma, "value", slider=False, text="gamma")
    else:  # parentMode == 'DH'
        parent_column.label("DH parameter:")
        parent_column.prop(context.active_bone.RobotDesigner.DH.theta, "value", slider=False, text="theta")
        parent_column.prop(context.active_bone.RobotDesigner.DH.d, "value", slider=False, text="d")
        parent_column.prop(context.active_bone.RobotDesigner.DH.alpha, "value", slider=False, text="alpha")
        parent_column.prop(context.active_bone.RobotDesigner.DH.a, "value", slider=False, text="a")

    layout.label("Active Axis:")
    axis_row = layout.row()
    axis_row.prop(context.active_bone.RobotDesigner, "axis", expand=True)
    axis_row.prop(context.active_bone.RobotDesigner, "axis_revert")

    # Only show joint if not root bone
    if not context.active_bone.parent == None:
        layout.label("Joint Type:")
        layout.prop(context.active_bone.RobotDesigner, "jointMode", expand=True)
        joint_column = layout.column(align=True)

        if context.active_bone.RobotDesigner.jointMode == 'REVOLUTE':
            joint_column.label("theta:")
            joint_column.prop(context.active_bone.RobotDesigner.theta, "value", slider=False)
            joint_column.prop(context.active_bone.RobotDesigner.theta, "offset", slider=False)
            joint_column.prop(context.active_bone.RobotDesigner.theta, "min", slider=False)
            joint_column.prop(context.active_bone.RobotDesigner.theta, "max", slider=False)
        elif context.active_bone.RobotDesigner.jointMode == 'PRISMATIC':
            joint_column.label("d:")
            joint_column.prop(context.active_bone.RobotDesigner.d, "value", slider=False)
            joint_column.prop(context.active_bone.RobotDesigner.d, "offset", slider=False)
            joint_column.prop(context.active_bone.RobotDesigner.d, "min", slider=False)
            joint_column.prop(context.active_bone.RobotDesigner.d, "max", slider=False)
