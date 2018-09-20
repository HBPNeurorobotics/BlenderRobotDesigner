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

#from .rigid_bodies import AssignGeometry, SelectGeometry
from .rigid_bodies import *
from .helpers import _mat3_to_vec_roll, ModelSelected, SingleSegmentSelected, PoseMode, AtLeastOneSegmentSelected, NotEditMode


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

        # Alternative to do this:
        # mode = context.mode
        # bpy.ops.object.mode_set(mode='EDIT')
        # bpy.ops.armature.select_all(action='DESELECT')
        # bpy.ops.object.mode_set(mode=mode)

        # Second alternative:
        # mode = context.mode
        # bpy.ops.object.mode_set(mode='EDIT')
        # for b in context.selected_bones:
        #     b.select = False
        # bpy.ops.object.mode_set(mode=mode)

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


@RDOperator.Preconditions(ModelSelected, AtLeastOneSegmentSelected, NotEditMode)
@PluginManager.register_class
class ImportBlenderArmature(RDOperator):
    """
    Set :term:`pose` properties and mark all selected bones as known to the robot designer.
    """
    bl_idname = config.OPERATOR_PREFIX + "importnative"
    bl_label = "(Re)import Bones"

    def execute_on_bone(self, bone):
        self.logger.info("Importing bone %s", bone.name)
        # Make the UpdateSegments operator consider this bone as if it has not been taken control of yet.
        # Otherwise UpdateSegments would mess up the bones transform as soon as the first RD related property is changed.
        # Example:
        # - have this bone down a bone hierarchy. It happens to be managed by RD already.
        # - Further down we do bpy.context.active_bone.RobotEditor.Euler.x.value = xyz[0]
        # - Triggers UpdateSegments
        # - y, z, etc still filled with garbage.
        # - UpdateSegments uses garbage to compute and assign new bone transform.
        bone.RobotEditor.RD_Bone = False
        parent = bone.parent
        if parent is not None:
            m = parent.matrix_local.inverted() * bone.matrix_local
        else:
            m = bone.matrix_local
        euler = m.to_euler()
        xyz = m.translation
        bone.RobotEditor.Euler.x.value = xyz[0]
        bone.RobotEditor.Euler.y.value = xyz[1]
        bone.RobotEditor.Euler.z.value = xyz[2]
        bone.RobotEditor.Euler.alpha.value = round(degrees(euler[0]), 0)
        bone.RobotEditor.Euler.beta.value = round(degrees(euler[1]), 0)
        bone.RobotEditor.Euler.gamma.value = round(degrees(euler[2]), 0)
        bone.RobotEditor.RD_Bone = True


    @RDOperator.OperatorLogger
    def execute(self, context):
        armature = bpy.context.active_object
        # Done via names because I get crashes if I keep references. Perhaps due to angling pointers inside kept references?
        selected_bone_names = [ str(b.name) for b in armature.data.bones ]
        for bname in selected_bone_names:
            SelectSegment.run(bname) # required by property update callback.
            self.execute_on_bone(armature.data.bones[bname])
        return {'FINISHED'}



@RDOperator.Preconditions(ModelSelected, AtLeastOneSegmentSelected, NotEditMode)
@PluginManager.register_class
class ConvertVertexMapSkinning(RDOperator):
    """
    :term:`operator` Operator for converting vertex weight based skinning to
    use of the bone parent property. Bone parent will be assigned to the
    bone with the largest total weight. Vertex weighting will be disabled
    on the mesh.
    """
    bl_idname = config.OPERATOR_PREFIX + "convert_vertexmap_skinning"
    bl_label = "Assign selected bones via vertex maps"

    def allow_connect_to_that_bone_because_vertex_weight(self, bone, obj):
        """ There can only be one parent_bone. So in case of multiple VG's we have to decide which one to take."""
        total_weights = []
        for vg in obj.vertex_groups:
            total_weight = 0.
            for i in range(len(obj.data.vertices)):
                try:
                    total_weight += vg.weight(i)
                except RuntimeError:
                    pass
            total_weights.append((vg.name, total_weight))
        bone_with_largest_weight, _ = max(total_weights, key=lambda x: x[1])
        return bone_with_largest_weight == bone.name

    def allow_connect_to_that_bone(self, bone, obj):
        return obj.parent_bone == bone.name or (
        bone.name in obj.vertex_groups and self.allow_connect_to_that_bone_because_vertex_weight(bone, obj))

    def stop_vertex_group_from_interfering(self, armature, obj, context):
        try:
            obj.modifiers[armature.name].use_vertex_groups = False
        except KeyError:
            # This is the normal case actually, i.e. the object has no vertex weighting w.r.t. that bone.
            pass

    def execute_on_bone(self, bone, armature, context):
        meshes_to_connect = [ ch for ch in armature.children if self.allow_connect_to_that_bone(bone, ch) ]
        for obj in meshes_to_connect:
            self.logger.debug("Attempt to attach geometry %s to %s", obj.name, bone.name)
            self.stop_vertex_group_from_interfering(armature, obj, context)
            # We just use the operators that we already have.
            # Assign geometry operates on selected items - one bone and one mesh.
            SelectGeometry.run(geometry_name=obj.name)
            AssignGeometry.run(attach_collision_geometry=(global_properties.mesh_type=='COLLISION'))

    @RDOperator.OperatorLogger
    def execute(self, context):
        armature = bpy.context.active_object
        bone_names = [ str(b.name) for b in armature.data.bones if b.select ]
        for bname in bone_names:
            SelectSegment.run(bname)  # required by property update callback.
            self.execute_on_bone(armature.data.bones[bname], armature, context)
        return {'FINISHED'}



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


    @RDOperator.Postconditions(ModelSelected)
    @RDOperator.OperatorLogger
    #    @RDOperator.Postconditions(ModelSelected)
    #    @Preconditions(ModelSelected)
    def execute(self, context):
        current_mode = bpy.context.object.mode
        self.logger.debug("UpdateSegments: recurse=%s, bone=%s", str(self.recurse), str(self.segment_name))

        armature_data_name = context.active_object.data.name

        if self.segment_name:
            segment_name = bpy.data.armatures[armature_data_name].bones[self.segment_name].name # Isn't this the identity operation??
        else:
            segment_name = bpy.data.armatures[armature_data_name].bones[0].name

        SelectSegment.run(segment_name=self.segment_name)

        if not bpy.data.armatures[armature_data_name].bones[segment_name].RobotEditor.RD_Bone:
            self.logger.info("Not updated (not a RD segment): %s", segment_name)
            return {'FINISHED'}

        bone = bpy.data.armatures[armature_data_name].bones[segment_name]

        # Transforms as per RD spec.
        matrix, joint_matrix = bone.RobotEditor.getTransform()

        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

        editbone = bpy.data.armatures[armature_data_name].edit_bones[
            bpy.data.armatures[armature_data_name].bones[segment_name].name]
        editbone.use_inherit_rotation = True

        # Express desired matrix in frame of the Armature
        if editbone.parent is not None:
            transform = editbone.parent.matrix.copy()
            matrix = transform * matrix

        # Adjust bone properties to match RD transform specs.
        # Try to move it around rigidly. Keep length.
        pos = matrix.to_translation()
        axis, roll = _mat3_to_vec_roll(matrix.to_3x3())
        length = editbone.length
        editbone.head = pos # Changes length.
        editbone.tail = pos + length * axis
        editbone.roll = roll

        bpy.ops.object.mode_set(mode=current_mode, toggle=False)

        # update pose
        bpy.ops.object.mode_set(mode='POSE', toggle=False)
        pose_bone = bpy.context.object.pose.bones[segment_name]
        pose_bone.matrix_basis = joint_matrix

        # Local variables for updating the constraints
        # These refer to the settings pertaining to the RD.
        joint_axis = bpy.data.armatures[armature_data_name].bones[segment_name].RobotEditor.axis
        min_rot = bpy.data.armatures[armature_data_name].bones[segment_name].RobotEditor.theta.min
        max_rot = bpy.data.armatures[armature_data_name].bones[segment_name].RobotEditor.theta.max
        jointMode = bpy.data.armatures[armature_data_name].bones[segment_name].RobotEditor.jointMode
        jointValue = bpy.data.armatures[armature_data_name].bones[segment_name].RobotEditor.theta.value
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
        elif 'RobotEditorConstraint' in pose_bone.constraints:
          pose_bone.constraints.remove(pose_bone.constraints['RobotEditorConstraint'])

        # -------------------------------------------------------
        bpy.ops.object.mode_set(mode=current_mode, toggle=False)


        children_names = [i.name for i in
                              bpy.data.armatures[armature_data_name].bones[
                                  segment_name].children]
        for child_name in children_names:
                UpdateSegments.run(segment_name=child_name, recurse=self.recurse)

        SelectSegment.run(segment_name=segment_name)

        return {'FINISHED'}
