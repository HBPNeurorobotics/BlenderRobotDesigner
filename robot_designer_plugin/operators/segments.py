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
#
#   2015-01-16: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######
"""
Sphinx-autodoc tag
"""

# System imports
from math import degrees, radians

# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty
# import mathutils

# RobotDesigner imports
from ..core import config, PluginManager, Condition, RDOperator

from .helpers import _mat3_to_vec_roll, ModelSelected, SingleSegmentSelected, PoseMode



@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectSegment(RDOperator):
    """
    :term:`Operator<operator>` for selecting a segment. If :attr:`segment_name` is empty,
    all segments will be deselected
    """
    bl_idname = config.OPERATOR_PREFIX + "select_segment"
    bl_label = "Select Segment"

    segment_name = StringProperty()

    @RDOperator.OperatorLogger
    def execute(self, context):
        if not (context.active_object.type == 'ARMATURE'):  #or context.active_object.type == 'MESH'
            raise Exception("BoneSelectionException")

        model = bpy.context.active_object
        for b in model.data.bones:
            b.select = False

        if self.segment_name:
            model.data.bones.active = model.data.bones[self.segment_name]

            model.data.bones.active.select = True
        else:
            model.data.bones.active = None

        return {'FINISHED'}

    @classmethod
    def run(cls, segment_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class RenameSegment(RDOperator):
    """
    :term:`operator` for renaming an active bone


    """
    bl_idname = config.OPERATOR_PREFIX + "rename_segment"
    bl_label = "Rename active segment"

    new_name = StringProperty(name="Enter new name:")


    @RDOperator.OperatorLogger
    def execute(self, context):
        context.active_bone.name = self.new_name
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, new_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected, PoseMode)
@PluginManager.register_class
class InsertNewParentSegment(RDOperator):
    """
    :term:`operator` for create new parent segment for the currently selected segment.


    """
    bl_idname = config.OPERATOR_PREFIX + "createparentbone"
    bl_label = "Create new parent Bone"

    segment_name = StringProperty(name="Enter new parent bone name:")

    @classmethod
    def run(cls, segment_name):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        current_segment_name = context.active_bone.name
        parent_segment_name = context.active_bone.parent.name if context.active_bone.parent else ""

        self.logger.info("%s %s", current_segment_name, parent_segment_name)

        bpy.ops.pose.select_all(action="DESELECT") #todo make an operator that switches context

        CreateNewSegment.run(segment_name=self.segment_name)
        new_segment_name = context.active_bone.name

        if parent_segment_name:
            AssignParentSegment.run(parent_name=parent_segment_name)

        SelectSegment.run(segment_name=current_segment_name)
        AssignParentSegment.run(parent_name=new_segment_name)



        # rearrange parent pointers accordingly in edit mode
        #current_mode = context.object.mode

        # bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        #
        # new_editbone = context.active_bone
        # if context.active_bone.parent:
        #     parent_name = context.active_bone.parent.name
        #     parent_editbone = context.active_object.data.edit_bones[parent_name]
        # else:
        #     parent_editbone = None
        #
        # new_editbone.parent = parent_editbone
        #
        # current_editbone = context.active_object.data.edit_bones[current_segment_name]
        # current_editbone.parent = new_editbone
        #
        # bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        UpdateSegments.run(segment_name=self.segment_name, recurse=True)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@PluginManager.register_class
class AssignParentSegment(RDOperator):
    """
    :term:`operator` for assigning a parent to a segment.


    """
    bl_idname = config.OPERATOR_PREFIX + "assignparentbone"
    bl_label = "Assign parent bone"

    parent_name = StringProperty()

    @classmethod
    def run(cls, parent_name):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        # arm = context.active_object
        current_segment_name = context.active_bone.name

        current_mode = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        new_parent_editbone = context.active_object.data.edit_bones[
            self.parent_name]
        current_editbone = context.active_object.data.edit_bones[
            current_segment_name]
        current_editbone.parent = new_parent_editbone
        bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        UpdateSegments.run(segment_name=current_segment_name)
        return {'FINISHED'}


@RDOperator.Preconditions()
@PluginManager.register_class
class ImportBlenderArmature(RDOperator):
    """
    :term:`operator` for converting a :term:`armature` into a :term:`model`


    """
    bl_idname = config.OPERATOR_PREFIX + "importnative"
    bl_label = "Import native blender segment"

    recursive = BoolProperty(name="Proceed recursively?")

    @RDOperator.OperatorLogger
    def execute(self, context):

        current_mode = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

        bone = bpy.context.active_bone
        parent = bpy.context.active_bone.parent
        children = bpy.context.active_bone.children
        bone.use_connect = False
        for i in children:
            i.use_connect = False

        bone.length = 1

        if parent is not None:
            m = parent.matrix.inverted() * bone.matrix
        else:
            m = bone.matrix

        bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        euler = m.to_euler()
        xyz = m.translation

        bpy.context.active_bone.RobotEditor.Euler.x.value = xyz[0]
        bpy.context.active_bone.RobotEditor.Euler.y.value = xyz[1]
        bpy.context.active_bone.RobotEditor.Euler.z.value = xyz[2]

        bpy.context.active_bone.RobotEditor.Euler.alpha.value = round(degrees(euler[0]), 0)
        bpy.context.active_bone.RobotEditor.Euler.beta.value = round(degrees(euler[1]), 0)
        bpy.context.active_bone.RobotEditor.Euler.gamma.value = round(degrees(euler[2]), 0)

        bpy.context.active_bone.RobotEditor.RD_Bone = True

        if self.recursive:
            for i in [i.name for i in bpy.context.active_bone.children]:
                SelectSegment.run(segment_name=i)
                ImportBlenderArmature.run(recursive=True)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class DeleteSegment(RDOperator):
    """
    :term:`operator` for deleting a the selected segment *ALL* of its children.


    """
    bl_idname = config.OPERATOR_PREFIX + "deletebone"
    bl_label = "Delete segment and ALL its children"

    confirmation = BoolProperty(name="Are you sure?")

    @RDOperator.OperatorLogger
    def execute(self, context):
        if self.confirmation:

            current_mode = context.object.mode
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            for bone in context.active_object.data.edit_bones:
                bone.select = False

            for bone in context.active_bone.children_recursive:
                bone.select = True

            context.active_bone.select = True

            if context.active_bone.parent is not None:
                parent_name = context.active_bone.parent.name
            else:
                parent_name = None

            bpy.ops.armature.delete()
            bpy.ops.object.mode_set(mode=current_mode, toggle=False)

            if parent_name is not None:
                SelectSegment.run(segment_name=parent_name)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


# class CreateNewSegment(bpy.types.Operator):
#     """
#     :term:`operator` for creating a new segment in the robot model.
#
#
#     """
#     bl_idname = config.OPERATOR_PREFIX + "createbone"
#     bl_label = "Create new Bone"
#
#     boneName = StringProperty(name="Enter new bone name:")
#
#     def execute(self, context):
#         try:
#             parentBoneName = context.active_bone.name
#         except:
#             parentBoneName = None
#
#         if not context.active_object.type == 'ARMATURE':
#             raise Exception("BoneCreationException")
#             # return{'FINISHED'}
#         armatureName = context.active_object.name
#         armatures.createBone(armatureName, self.boneName, parentBoneName)
#
#         designer.ops.select_segment(boneName=self.boneName)
#         armatures.updateKinematics(armatureName, self.boneName)
#
#         # TODO: set parentMode according to own parent
#         return {'FINISHED'}
#
#     def invoke(self, context, event):
#         return context.window_manager.invoke_props_dialog(self)

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateNewSegment(RDOperator):
    """
    :term:`Operator <operator>` for creating new robot segments and add it to the current model.
    If a segment is already selected, the new segment is added as a child segment. A call :class:`SelectSegment`
    before might be necessary.
    """
    bl_idname = config.OPERATOR_PREFIX + "create_segment"
    bl_label = "Create new segment"

    # model_name = StringProperty()
    segment_name = StringProperty(name="Enter new segment name:")
    #parent_name = StringProperty(default="")

    @classmethod
    def run(cls, segment_name):#, parent_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected)
    def execute(self, context):
        current_mode = bpy.context.object.mode
        selected_segments = [i for i in context.active_object.data.bones if i.select]


        # if not self.parent_name:
        #     try:
        #         parentBoneName = context.active_bone.name
        #     except:
        #         parentBoneName = None
        # else:
        #     if self.parent_name in context.active_object:
        #         parentBoneName = self.parent_name
        #     else:
        #         parentBoneName = None

        if len(selected_segments):
            parent_name = selected_segments[0].name
        else:
            parent_name = ""

        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        bone = context.active_object.data.edit_bones.new(self.segment_name)
        segment_name = self.segment_name
        bone.head = (0, 0, 0)  # Dummy
        bone.tail = (0, 0, 1)  # Dummy
        bone.lock = True

        if parent_name:
            self.logger.debug(parent_name)
            bone.parent = context.active_object.data.edit_bones[parent_name]

        bpy.ops.object.mode_set(mode='POSE', toggle=False)

        SelectSegment.run(segment_name=segment_name)

        context.active_bone.RobotEditor.RD_Bone = True

        if not parent_name:
            context.active_bone.RobotEditor.Euler.alpha.value = 90.0
            context.active_bone.RobotEditor.DH.alpha.value = 90.0

        bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
        bpy.context.object.pose.bones[segment_name].constraints[
            0].name = 'RobotEditorConstraint'
        bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        self.logger.info("Current mode after: %s (%s)", bpy.context.object.mode, current_mode)
        self.logger.debug("Segment created. (%s -> %s)", parent_name, self.segment_name)

        UpdateSegments.run(recurse=True, segment_name=self.segment_name)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

# def createBone(model_name, bone_name, parent_name=None):
#     """
#     Creates a new bone
#
#     :param model_name: string identifier of the armature
#     :param bone_name: the name of the new bone
#     :param parent_name: (optional) identifies the name of the parent bone
#     """
#     print("createBone")
#     designer.selectarmature(armatureName=model_name)
#     currentMode = bpy.context.object.mode
#
#     print(bpy.ops.object.mode_set(mode='EDIT', toggle=False))
#     # arm = bpy.data.armatures[armatureName]
#     bone = bpy.data.armatures[model_name].edit_bones.new(bone_name)
#     bone.head = (0, 0, 0)  # Dummy
#     bone.tail = (0, 0, 1)  # Dummy
#     bone.lock = True
#
#     if parent_name is not None:
#         bone.parent = bpy.data.armatures[model_name].edit_bones[parent_name]
#
#     bpy.ops.object.mode_set(mode='POSE', toggle=False)
#
#     designer.select_segment(boneName=bone_name)
#     bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
#     bpy.context.object.pose.bones[bone_name].constraints[
#         0].name = 'RobotEditorConstraint'
#     bpy.ops.object.mode_set(mode=currentMode, toggle=False)
#
#     print("createBone done")



@PluginManager.register_class
class UpdateSegments(RDOperator):
    """
    :term:`operator` for updating the :term:`robot models` after parameters changed.
    If a :term:`segment` name is given it will proceed recursively.
    """
    bl_idname = config.OPERATOR_PREFIX + "udpate_model"
    bl_label = "update model"

    # model_name = StringProperty()
    segment_name = StringProperty(default="")
    recurse = BoolProperty(default=True)

    @classmethod
    def run(cls, recurse=True, segment_name=""):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())

    @RDOperator.Postconditions(ModelSelected)
    @RDOperator.OperatorLogger
    #    @RDOperator.Postconditions(ModelSelected)
    #    @Preconditions(ModelSelected)
    def execute(self, context):
        current_mode = bpy.context.object.mode

        # arm = bpy.data.armatures[armatureName]

        # armature_data_ame = bpy.data.objects[self.model_name].data.name # conversion to operator
        armature_data_ame = context.active_object.data.name

        if self.segment_name:
            segment_name = bpy.data.armatures[armature_data_ame].bones[self.segment_name].name
        else:
            segment_name = bpy.data.armatures[armature_data_ame].bones[0].name

        SelectSegment.run(segment_name=self.segment_name)

        if not bpy.data.armatures[armature_data_ame].bones[segment_name].RobotEditor.RD_Bone:
            self.logger.info("Not updated (not a RD segment): %s", segment_name)
            return {'FINISHED'}

        # local variables for updating the constraints
        joint_axis = bpy.data.armatures[armature_data_ame].bones[segment_name].RobotEditor.axis
        min_rot = bpy.data.armatures[armature_data_ame].bones[segment_name].RobotEditor.theta.min
        max_rot = bpy.data.armatures[armature_data_ame].bones[segment_name].RobotEditor.theta.max
        jointMode = bpy.data.armatures[armature_data_ame].bones[segment_name].RobotEditor.jointMode
        jointValue = bpy.data.armatures[armature_data_ame].bones[segment_name].RobotEditor.theta.value

        matrix, joint_matrix = bpy.data.armatures[armature_data_ame].bones[
            segment_name].RobotEditor.getTransform()

        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

        editbone = bpy.data.armatures[armature_data_ame].edit_bones[
            bpy.data.armatures[armature_data_ame].bones[segment_name].name]
        editbone.use_inherit_rotation = True

        if editbone.parent is not None:
            transform = editbone.parent.matrix.copy()
            matrix = transform * matrix

        pos = matrix.to_translation()
        axis, roll = _mat3_to_vec_roll(matrix.to_3x3())

        editbone.head = pos
        editbone.tail = pos + axis
        editbone.roll = roll

        editbone.length = 1

        bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        # update pose
        bpy.ops.object.mode_set(mode='POSE', toggle=False)
        pose_bone = bpy.context.object.pose.bones[segment_name]
        pose_bone.matrix_basis = joint_matrix

        if jointMode == 'REVOLUTE':
            if 'RobotEditorConstraint' not in pose_bone.constraints:
                bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
                bpy.context.object.pose.bones[segment_name].constraints[
                    0].name = 'RobotEditorConstraint'
            constraint = \
                [i for i in pose_bone.constraints if i.type == 'LIMIT_ROTATION'][0]
            constraint.name = 'RobotEditorConstraint'
            constraint.owner_space = 'LOCAL'
            constraint.use_limit_x = True
            constraint.use_limit_y = True
            constraint.use_limit_z = True
            constraint.min_x = 0.0
            constraint.min_y = 0.0
            constraint.min_z = 0.0
            constraint.max_x = 0.0
            constraint.max_y = 0.0
            constraint.max_z = 0.0
            if joint_axis == 'X':
                constraint.min_x = radians(min_rot)
                constraint.max_x = radians(max_rot)
            elif joint_axis == 'Y':
                constraint.min_y = radians(min_rot)
                constraint.max_y = radians(max_rot)
            elif joint_axis == 'Z':
                constraint.min_z = radians(min_rot)
                constraint.max_z = radians(max_rot)
        # -------------------------------------------------------
        bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        children_names = [i.name for i in
                          bpy.data.armatures[armature_data_ame].bones[
                              segment_name].children]
        for child_name in children_names:
            UpdateSegments.run(segment_name=child_name, recurse=self.recurse)

        SelectSegment.run(segment_name=segment_name)

        return {'FINISHED'}
