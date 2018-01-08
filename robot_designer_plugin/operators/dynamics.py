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
from mathutils import Matrix

import bpy
from bpy.props import StringProperty

# ######
# RobotDesigner imports
from ..core import config, PluginManager, RDOperator
from .helpers import ModelSelected, SingleSegmentSelected, SingleMassObjectSelected

from ..properties.globals import global_properties

# operator to create physics frame
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreatePhysical(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "createphysicsframe"
    bl_label = "Create Physics Frame"

    frameName = StringProperty()

    @classmethod
    def run(cls, frameName=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)  # todo condition for physicframe
    def execute(self, context):
        from . import model
        model_name = context.active_object.name
        bpy.ops.object.empty_add(type='PLAIN_AXES')
        context.active_object.name = self.frameName
        context.active_object.RobotEditor.tag = 'PHYSICS_FRAME'

        # set new mass object to cursor location
        cursor = bpy.context.scene.cursor_location
        context.active_object.location = [cursor.x, cursor.y, cursor.z]


        model.SelectModel.run(model_name=model_name)
        SelectPhysical.run(frameName=self.frameName)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


# operator to select a physics frame
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectPhysical(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "selectphysicsframe"
    bl_label = "Select Physics Frame"

    frameName = StringProperty()

    @classmethod
    def run(cls, frameName=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)  # todo condition for physicframe
    def execute(self, context):
        arm = context.active_object
        global_properties.physics_frame_name.set(context.scene, self.frameName)

        frame = bpy.data.objects[self.frameName]

        for obj in bpy.data.objects:
            obj.select = False

        frame.select = True
        arm.select = True

        context.scene.objects.active = arm

        return {'FINISHED'}


# operator to assign selected physics frame to active bone
@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected, SingleMassObjectSelected)
@PluginManager.register_class
class AssignPhysical(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "assignphysicsframe"
    bl_label = "Assign selected physics frame to active bone"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected, SingleMassObjectSelected)
    def execute(self, context):
        bpy.ops.object.parent_set(type='BONE')

        if bpy.context.active_bone.parent:
            to_parent_matrix = bpy.context.active_bone.parent.matrix_local
        else:
            to_parent_matrix = Matrix()
        from_parent_matrix, bone_matrix = bpy.context.active_bone.RobotEditor.getTransform()
        armature_matrix = bpy.context.active_object.matrix_basis

        # find selected physics frame
        for ob in bpy.data.objects:
            if ob.select and ob.RobotEditor.tag == 'PHYSICS_FRAME':
                frame = ob
                print(frame.name)

        # frame.matrix_basis = armature_matrix*to_parent_matrix*from_parent_matrix*bone_matrix
        # frame.matrix_basis = parent_matrix*armature_matrix*bone_matrix
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


# operator to generate collision meshes for all assigned physics frames


# operator to unassign selected physics frame
@RDOperator.Preconditions(ModelSelected, SingleMassObjectSelected)
@PluginManager.register_class
class DetachPhysical(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "unassignphysicsframe"
    bl_label = "Unassign selected physics frame"

    frameName = StringProperty()

    @classmethod
    def run(cls, frameName=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMassObjectSelected)
    def execute(self, context):
        if self.frameName:
            current_frame = context.scene.objects[self.frameName]
        else:
            current_frame = context.scene.objects[global_properties.physics_frame_name.get(context.scene)]
        physNode_global = current_frame.matrix_world
        current_frame.parent = None
        current_frame.matrix_world = physNode_global
        return {'FINISHED'}
