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
from .model import check_armature
from ..core.gui import InfoBox
from .helpers import getSingleSegment
from .helpers import (
    PhysicsBox,
    LinkBox,
    JointLimitsBox,
    JointAxisBox,
    JointDynamicsBox,
    JointPhysicsBox,
)
from ..core.logfile import LogFunction


@LogFunction
def draw(layout, context):
    """
    Draws the user interface for modifying the dynamic properties of a segment.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return

    single_segment = getSingleSegment(context)

    # link properties
    linkBox = LinkBox.get(layout, context, "Link")
    if linkBox:
        infoBox = InfoBox(linkBox)
        row = linkBox.column(align=True)

        dynamics.CreatePhysical.place_button(row, infoBox=infoBox)
        dynamics.ComputePhysical.place_button(row, infoBox=infoBox)
        dynamics.ComputeMass.place_button(row, infoBox=infoBox)

        objs = [
            o
            for o in context.active_object.children
            if o.RobotDesigner.tag == "PHYSICS_FRAME"
            and o.parent_bone == single_segment.name
        ]
        try:
            (obj,) = objs
            if obj and obj.RobotDesigner.tag == "PHYSICS_FRAME":
                frame_name = obj.name
                box = linkBox.box()
                box.label(
                    text="Mass Properties (" + single_segment.name + ")",
                    icon="MODIFIER",
                )
                frame = bpy.data.objects[frame_name]
                box.prop(frame.RobotDesigner.dynamics, "mass")
                box.separator()

                row_t = box.row(align=True)
                row_r = box.row(align=True)

                row_t.prop(bpy.data.objects[frame_name], "location", text="Translation")
                row_r.prop(
                    bpy.data.objects[frame_name], "rotation_euler", text="Rotation"
                )

                row0 = box.row(align=True)
                row1 = box.row(align=True)
                row2 = box.row(align=True)
                row3 = box.row(align=True)
                row0.label(text="Inertia Matrix")
                row1.prop(frame.RobotDesigner.dynamics, "inertiaXX")
                row2.prop(frame.RobotDesigner.dynamics, "inertiaXY")
                row3.prop(frame.RobotDesigner.dynamics, "inertiaXZ")
                row1.prop(frame.RobotDesigner.dynamics, "inertiaXY")
                row2.prop(frame.RobotDesigner.dynamics, "inertiaYY")
                row3.prop(frame.RobotDesigner.dynamics, "inertiaYZ")
                row1.prop(frame.RobotDesigner.dynamics, "inertiaXZ")
                row2.prop(frame.RobotDesigner.dynamics, "inertiaYZ")
                row3.prop(frame.RobotDesigner.dynamics, "inertiaZZ")
        except:
            pass

        linkBox.prop(
            bpy.context.active_bone.RobotDesigner.linkInfo,
            "link_self_collide",
            text="Self Collide",
        )
        linkBox.prop(
            bpy.context.active_bone.RobotDesigner.linkInfo, "gravity", text="Gravity"
        )

        infoBox.draw_info()

    # joint physics properties
    # Only shown for child segments. Unless root segment is connected to world.
    joint_box = PhysicsBox.get(layout, context, "Joint")
    if joint_box:

        if (context.active_bone.parent is None) and (
            context.active_bone.RobotDesigner.world is not True
        ):
            joint_box.label(text="No Joint defined for this Link.")
        else:
            axis_box = JointAxisBox.get(joint_box, context, "Axis")
            if axis_box:
                limit_box = JointLimitsBox.get(axis_box, context, "Limits")
                if limit_box:
                    limit_box.prop(
                        context.active_bone.RobotDesigner.dynamic_limits,
                        "isActive",
                        text="Active Joint Dynamic Limits",
                    )

                    if context.active_bone.RobotDesigner.dynamic_limits.isActive:
                        limit_box.prop(
                            context.active_bone.RobotDesigner.dynamic_limits, "maxVelocity"
                        )
                        limit_box.prop(
                            context.active_bone.RobotDesigner.dynamic_limits, "maxTorque"
                        )

                    ## URDF only
                    # limit_box.prop(context.active_bone.RobotDesigner.controller, "acceleration")
                    # limit_box.prop(context.active_bone.RobotDesigner.controller, "deceleration")

                dynamics_box = JointDynamicsBox.get(axis_box, context, "Dynamics")
                if dynamics_box:
                    dynamics_box.prop(
                        bpy.context.active_bone.RobotDesigner.joint_dynamics,
                        "damping",
                        text="Damping",
                    )
                    dynamics_box.prop(
                        bpy.context.active_bone.RobotDesigner.joint_dynamics,
                        "friction",
                        text="Friction",
                    )
                    dynamics_box.prop(
                        bpy.context.active_bone.RobotDesigner.joint_dynamics,
                        "spring_reference",
                        text="Spring Reference",
                    )
                    dynamics_box.prop(
                        bpy.context.active_bone.RobotDesigner.joint_dynamics,
                        "spring_stiffness",
                        text="Spring Stiffness",
                    )

            physics_box = JointPhysicsBox.get(joint_box, context, "Physics")
            if physics_box:
                physics_ode_box = physics_box.box()
                physics_ode_box.label(text="ODE")
                physics_ode_box.prop(
                    bpy.context.active_bone.RobotDesigner.ode,
                    "cfm_damping",
                    text="CFM-Damping",
                )
                physics_ode_box.prop(
                    bpy.context.active_bone.RobotDesigner.ode,
                    "i_s_damper",
                    text="I. S. Damper",
                )  # implicit spring
                physics_ode_box.prop(
                    bpy.context.active_bone.RobotDesigner.ode, "cfm", text="CFM"
                )  # constraint force mixing
                physics_ode_box.prop(
                    bpy.context.active_bone.RobotDesigner.ode, "erp", text="ERP"
                )  # error reduction parameter
