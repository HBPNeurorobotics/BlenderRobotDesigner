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
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######
"""
Sphinx-autodoc tag
"""

# ######
# System imports
# import os
# import sys
# import math

# ######
# Blender imports
import bpy
from bpy.props import StringProperty
# import mathutils

# ######
# RobotDesigner imports
from ..core import config, PluginManager, RDOperator, Condition
from .helpers import ModelSelected
from ..properties.globals import global_properties

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectCoordinateFrame(RDOperator):
    """
    :ref:`operator` for selecting mesh for visualization of coordinate frames.

    **Preconditions:**

    **RDOperator.Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "selectcf"
    bl_label = "Select Mesh"

    mesh_name = StringProperty()

    @classmethod
    def run(cls, mesh_name=""):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        for bone in [i.name for i in bpy.data.armatures[
            context.active_object.data.name].bones]:
            if self.mesh_name != 'None':
                context.active_object.pose.bones[bone].custom_shape = \
                    bpy.data.objects[self.mesh_name]
            else:
                context.active_object.pose.bones[bone].custom_shape = None
        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class RebuildModel(RDOperator):
    """
    :ref:`operator` for rebuilding a model, i.e. to reassign all meshes to
    bones in case of a broken export.

    **Preconditions:**

    **RDOperator.Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "rebuildmodel"
    bl_label = "Rebuild model"

    @classmethod
    def run(cls):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        from . import rigid_bodies, segments, dynamics
        mesh_names = [obj.name for obj in bpy.data.objects if
                      obj.type == 'MESH' and obj.parent_bone]
        # first, meshes
        # build dictionary which stores the mapping of meshes to bones
        meshes_bones_dictionary = dict()

        for m in mesh_names:
            meshes_bones_dictionary[m] = bpy.data.objects[m].parent_bone

        # remove assignment of meshes->bones
        rigid_bodies.DetachAllGeometries.run(confirmation=True)

        # reassign all meshes to bones according to dictionary
        for k, v in meshes_bones_dictionary.items():
            segments.SelectSegment.run(segment_name=v)
            rigid_bodies.SelectGeometry.run(geometry_name=k)
            rigid_bodies.AssignGeometry.run()

        # then markers
        marker_names = [obj.name for obj in bpy.data.objects if
                        obj.RobotEditor.tag == 'MARKER' and obj.parent_bone]

        marker_bones_dictionary = dict()

        # for m in marker_names:
        #     marker_bones_dictionary[m] = bpy.data.objects[m].parent_bone
        #     designer.selectmarker(markerName=m)
        #     designer.unassignmarker()
        #
        # for k, v in marker_bones_dictionary.items():
        #     designer.select_segment(segment_name=v)
        #     designer.selectmarker(markerName=k)
        #     designer.assignmarker()

        # finally, physic frames
        ph_names = [obj.name for obj in bpy.data.objects if
                    obj.RobotEditor.tag == 'PHYSICS_FRAME' and obj.parent_bone]

        ph_bones_dictionary = dict()

        for frame in ph_names:
            ph_bones_dictionary[frame] = bpy.data.objects[frame].parent_bone
            dynamics.SelectPhysical.run(frameName=frame)
            dynamics.DetachPhysical()

        for k, v in ph_bones_dictionary.items():
            segments.SelectSegment.run(segment_name=v)
            dynamics.SelectPhysical.run(frameName=k)
            dynamics.AssignPhysical.run()

        return {'FINISHED'}

@PluginManager.register_class
class SelectModel(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **RDOperator.Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "selectarmature"
    bl_label = "Select model"

    model_name = StringProperty()

    @classmethod
    def run(cls, model_name=""):
        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        from . import segments
        for obj in bpy.data.objects:
            obj.select = False

        context.scene.objects.active = bpy.data.objects[self.model_name]
        context.active_object.select = True
        global_properties.model_name.set(context.scene, self.model_name)
        global_properties.old_name.set(context.scene, self.model_name)
        # not so sure if this is needed at all

        if len(context.active_object.data.bones) > 0:
            baseBoneName = context.active_object.data.bones[0].name
            segments.SelectSegment.run(segment_name=baseBoneName)
        return {'FINISHED'}

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class RenameModel(RDOperator):
    """
    :ref:`operator` for renaming models

    **Preconditions:**

    **RDOperator.Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "renamearmature"
    bl_label = "Rename selected armature"

    newName = StringProperty(name="Enter new name:")

    @classmethod
    def run(cls, newName=""):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        # oldName = context.active_object.name
        # context.active_object.name = self.newName
        # bpy.data.armatures[oldName].name = self.newName

        global_properties.model_name.set(context.scene, self.newName)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class JoinModels(RDOperator):
    """
    :ref:`operator` for joining two models

    **Preconditions:**

    **RDOperator.Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "joinarmature"

    bl_label = "Join two models"

    targetArmatureName = StringProperty()

    @classmethod
    def run(cls, targetArmatureName=""):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        from . import segments
        sourceArmName = context.active_object.name
        sourceParentBoneName = context.active_object.data.bones[0].name
        SelectModel.run(model_name=self.targetArmatureName)
        bpy.data.objects[sourceArmName].select = True

        bpy.ops.object.join()
        segments.SelectSegment.run(segment_name=sourceParentBoneName)
        segments.AssignParentSegment.run(parentName=context.active_object.data.bones[0].name)

        # Might be swapped! todo check double
        segments.UpdateSegments.run(segment_name=sourceParentBoneName, recurse=True)
        return {'FINISHED'}


@PluginManager.register_class
class CreateNewModel(RDOperator):
    """
    :ref:`operator` for creating new robot models.

    **Preconditions:**

    **RDOperator.Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "create_model"
    bl_label = "Create new robot model"

    model_name = StringProperty(name="Enter model name:")
    base_segment_name = StringProperty(name="Enter root segment name:", default="")

    @classmethod
    def run(cls, model_name, base_segment_name):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        from . import segments
        model_data = bpy.data.armatures.new(self.model_name)
        model_object = bpy.data.objects.new(self.model_name, model_data)
        model_object.data = model_data
        model_data.show_names = True
        model_data.show_axes = True
        model_data.draw_type = 'STICK'
        scene = bpy.context.scene
        scene.objects.link(model_object)
        SelectModel.run(model_name=self.model_name)
        if self.base_segment_name:
            segments.CreateNewSegment.run(segment_name=self.base_segment_name)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

# def createArmature(new_name):
#     """
#     Creates a new armature
#     :param new_name: the name of the new armature
#     :return: reference to the new armature object
#     """
#
#     armature_data = bpy.data.armatures.new(new_name)
#     armature_Object = bpy.data.objects.new(new_name, armature_data)
#     armature_Object.data = armature_data
#     armature_data.show_names = True
#     armature_data.show_axes = True
#     armature_data.draw_type = 'STICK'
#     # armature_data.use_deform_envelopes = False
#     scene = bpy.context.scene
#     scene.objects.link(armature_Object)
#     return armature_Object




# # update kinematics chain of armatureName starting with segment_name
# def updateKinematics(model_name, segment_name=None):
#     currentMode = bpy.context.object.mode
#
#     designer.select_segment(boneName=segment_name)
#
#     # arm = bpy.data.armatures[armatureName]
#
#     armatureDataName = bpy.data.objects[model_name].data.name
#
#     if segment_name is not None:
#         segment_name = bpy.data.armatures[armatureDataName].bones[segment_name].name
#     else:
#         segment_name = bpy.data.armatures[armatureDataName].bones[0].name
#
#     if bpy.data.armatures[armatureDataName].bones[
#         segment_name].RobotEditor.RD_Bone == False:
#         print("Not updated (not a RD segment):", segment_name)
#         return
#
#     # local variables for updating the constraints
#     jointAxis = bpy.data.armatures[armatureDataName].bones[
#         segment_name].RobotEditor.axis
#     min_rot = bpy.data.armatures[armatureDataName].bones[
#         segment_name].RobotEditor.theta.min
#     max_rot = bpy.data.armatures[armatureDataName].bones[
#         segment_name].RobotEditor.theta.max
#     jointMode = bpy.data.armatures[armatureDataName].bones[
#         segment_name].RobotEditor.jointMode
#     jointValue = bpy.data.armatures[armatureDataName].bones[
#         segment_name].RobotEditor.theta.value
#
#     matrix, jointMatrix = bpy.data.armatures[armatureDataName].bones[
#         segment_name].RobotEditor.getTransform()
#
#     bpy.ops.object.mode_set(mode='EDIT', toggle=False)
#
#     edit_bone = bpy.data.armatures[armatureDataName].edit_bones[
#         bpy.data.armatures[armatureDataName].bones[segment_name].name]
#     edit_bone.use_inherit_rotation = True
#
#     if edit_bone.parent is not None:
#         transform = edit_bone.parent.matrix.copy()
#         matrix = transform * matrix
#
#     pos = matrix.to_translation()
#     axis, roll = _mat3_to_vec_roll(matrix.to_3x3())
#
#     edit_bone.head = pos
#     edit_bone.tail = pos + axis
#     edit_bone.roll = roll
#
#     edit_bone.length = 0.1
#
#     bpy.ops.object.mode_set(mode=currentMode, toggle=False)
#
#     # update pose
#     bpy.ops.object.mode_set(mode='POSE', toggle=False)
#     # pose_bone = bpy.context.active_pose_bone
#     pose_bone = bpy.context.object.pose.bones[segment_name]
#     #    print (pose_bone.name, jointMatrix)
#     pose_bone.matrix_basis = jointMatrix
#
#     # Adding constraints for revolute joints
#     # ---------- REMOVED DUE TO BUG IN BLENDER ------------
#     if jointMode == 'REVOLUTE':
#         if 'RobotEditorConstraint' not in pose_bone.constraints:
#             bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
#             bpy.context.object.pose.bones[segment_name].constraints[
#                 0].name = 'RobotEditorConstraint'
#         constraint = \
#         [i for i in pose_bone.constraints if i.type == 'LIMIT_ROTATION'][0]
#         constraint.name = 'RobotEditorConstraint'
#         constraint.owner_space = 'LOCAL'
#         constraint.use_limit_x = True
#         constraint.use_limit_y = True
#         constraint.use_limit_z = True
#         constraint.min_x = 0.0
#         constraint.min_y = 0.0
#         constraint.min_z = 0.0
#         constraint.max_x = 0.0
#         constraint.max_y = 0.0
#         constraint.max_z = 0.0
#         if jointAxis == 'X':
#             constraint.min_x = math.radians(min_rot)
#             constraint.max_x = math.radians(max_rot)
#         elif jointAxis == 'Y':
#             constraint.min_y = math.radians(min_rot)
#             constraint.max_y = math.radians(max_rot)
#         elif jointAxis == 'Z':
#             constraint.min_z = math.radians(min_rot)
#             constraint.max_z = math.radians(max_rot)
#     # -------------------------------------------------------
#     bpy.ops.object.mode_set(mode=currentMode, toggle=False)
#
#     #   print("Number of children")
#     #   print(len(arm.bones[boneName].children))
#     #   print("updateKinematics Done")
#     # recursive call on all children
#
#     childBoneNames = [i.name for i in
#                       bpy.data.armatures[armatureDataName].bones[
#                           boneName].children]
#     #   print(boneName,childBoneNames)
#     for childBoneName in childBoneNames:
#         #        if childBoneName == "":
#         #            print('Empty name',childBoneName,childBoneNames,boneName)
#         updateKinematics(model_name, childBoneName)
#
#     designer.select_segment(boneName=segment_name)
