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
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#   2014      : Stefan Ulbrich (FZI), Igor Peric (FZI Forschungszentrum Informatik)
#       URDF import/export implemented
#   2016-01-15: Stefan Ulbrich (FZI)
#       Major refactoring. Integrated into complex plugin framework.
#
# ######

"""
Sphinx-autodoc tag
"""

# Blender imports
import bpy

# RobotDesigner imports
from ..core.operators import RDOperator
from .helpers import ModelSelected, ObjectMode
from .segments import SelectSegment


class Traverse(RDOperator):
    """
    :term:`operator` for updating the :term:`robot models` after parameters changed.
    If a :term:`segment` name is given it will proceed recursively.

    **Requirements:**

    **Effects:**
    """

    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    @RDOperator.OperatorLogger
    def execute(self, context):
        current_mode = bpy.context.object.mode

        armature_data_name = context.active_object.data.name

        if self.segment_name:
            segment_name = (
                bpy.data.armatures[armature_data_name].bones[self.segment_name].name
            )
        else:
            segment_name = bpy.data.armatures[armature_data_name].bones[0].name

        SelectSegment.run(segment_name=self.segment_name)

        if (
            not bpy.data.armatures[armature_data_name]
            .bones[segment_name]
            .RobotDesigner.RD_Bone
        ):
            self.logger.info("Not updated (not a RD segment): %s", segment_name)
            return

        # local variables for updating the constraints
        joint_axis = (
            bpy.data.armatures[armature_data_name]
            .bones[segment_name]
            .RobotDesigner.axis
        )
        min_rot = (
            bpy.data.armatures[armature_data_name]
            .bones[segment_name]
            .RobotDesigner.theta.min
        )
        max_rot = (
            bpy.data.armatures[armature_data_name]
            .bones[segment_name]
            .RobotDesigner.theta.max
        )
        jointMode = (
            bpy.data.armatures[armature_data_name]
            .bones[segment_name]
            .RobotDesigner.jointMode
        )
        jointValue = (
            bpy.data.armatures[armature_data_name]
            .bones[segment_name]
            .RobotDesigner.theta.value
        )

        matrix, joint_matrix = (
            bpy.data.armatures[armature_data_name]
            .bones[segment_name]
            .RobotDesigner.getTransform()
        )

        bpy.ops.object.mode_set(mode="EDIT", toggle=False)

        editbone = bpy.data.armatures[armature_data_name].edit_bones[
            bpy.data.armatures[armature_data_name].bones[segment_name].name
        ]
        editbone.use_inherit_rotation = True

        if editbone.parent is not None:
            transform = editbone.parent.matrix.copy()
            matrix = transform @ matrix

        pos = matrix.to_translation()
        axis, roll = _mat3_to_vec_roll(matrix.to_3x3())

        editbone.head = pos
        editbone.tail = pos + axis
        editbone.roll = roll

        editbone.length = 0.1

        bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        # update pose
        bpy.ops.object.mode_set(mode="POSE", toggle=False)
        pose_bone = bpy.context.object.pose.bones[segment_name]
        pose_bone.matrix_basis = joint_matrix

        if jointMode == "REVOLUTE":
            if "RobotDesignerConstraint" not in pose_bone.constraints:
                bpy.ops.pose.constraint_add(type="LIMIT_ROTATION")
                bpy.context.object.pose.bones[segment_name].constraints[
                    0
                ].name = "RobotDesignerConstraint"
            constraint = [
                i for i in pose_bone.constraints if i.type == "LIMIT_ROTATION"
            ][0]
            constraint.name = "RobotDesignerConstraint"
            constraint.owner_space = "LOCAL"
            constraint.use_limit_x = True
            constraint.use_limit_y = True
            constraint.use_limit_z = True
            constraint.min_x = 0.0
            constraint.min_y = 0.0
            constraint.min_z = 0.0
            constraint.max_x = 0.0
            constraint.max_y = 0.0
            constraint.max_z = 0.0
            if joint_axis == "X":
                constraint.min_x = radians(min_rot)
                constraint.max_x = radians(max_rot)
            elif joint_axis == "Y":
                constraint.min_y = radians(min_rot)
                constraint.max_y = radians(max_rot)
            elif joint_axis == "Z":
                constraint.min_z = radians(min_rot)
                constraint.max_z = radians(max_rot)
        # -------------------------------------------------------
        bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        children_names = [
            i.name
            for i in bpy.data.armatures[armature_data_name].bones[segment_name].children
        ]
        for child_name in children_names:
            UpdateSegments.run(segment_name=child_name, recurse=self.recurse)

        SelectSegment.run(segment_name=segment_name)

        return {"FINISHED"}
