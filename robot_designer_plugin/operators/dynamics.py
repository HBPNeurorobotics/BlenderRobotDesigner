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
from collections import defaultdict

import bpy
from bpy.props import StringProperty, FloatProperty, BoolProperty

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
    bl_label = "Create And Attach Physics Frame"

    frameName: StringProperty()

    @classmethod
    def run(cls, frameName=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)  # todo condition for physicframe
    def execute(self, context):
        from . import model

        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        armature = context.active_object

        bones = set([b for b in armature.data.bones if b.select])

        bones_that_have_physics_frames = set()
        for obj in armature.children:
            if obj.parent_bone and obj.RobotDesigner.tag == 'PHYSICS_FRAME':
                bone = armature.data.bones[obj.parent_bone]
                bones_that_have_physics_frames.add(bone)

        bones = bones.difference(bones_that_have_physics_frames)

        frame = None
        for bone in bones:
            frame = just_create_the_physics_frame(context, bone.name)
            assign_the_physics_frame_to_the_bone(context, frame, bone)
            # https://blender.stackexchange.com/questions/15353/get-the-location-in-world-coordinates-of-a-bones-head-and-tail-while-in-pose-mo
            # https: // blender.stackexchange.com / questions / 80306 / location - still - the - same - although - its - moved
            special_bone = armature.pose.bones[bone.name]
            # frame.worldPosition = armature.matrix_world.to_translation() + 0.5 * (bone.active_pose_bone.tail + bone.active_pose_bone.head)
            frame.matrix_world = armature.matrix_world @ special_bone.matrix

        if frame:
            SelectPhysical.run(frameName=frame.name)
            frame.RobotDesigner.dynamics.scale_update(context)

        return {'FINISHED'}


def assign_the_physics_frame_to_the_bone(context, frame, bone):
    armature = context.active_object
    frame.parent = armature
    frame.parent_type = 'BONE'
    frame.parent_bone = bone.name


def just_create_the_physics_frame(context, name):
    armature = context.active_object
    #bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.ops.mesh.primitive_cube_add(size=1.0)
    context.active_object.name = 'PHYS_' + name
    frame = context.active_object.name
    context.active_object.RobotDesigner.tag = 'PHYSICS_FRAME'
    # set new mass object to cursor location
    cursor = bpy.context.scene.cursor.location
    context.active_object.location = [cursor.x, cursor.y, cursor.z]
    obj = context.active_object
    bpy.context.view_layer.objects.active = armature  # Restore the active object.

    # change physics frame color
    # obj.data.materials.clear()
    mat = bpy.data.materials.new(frame)
    mat.diffuse_color = (1.0, 0.0, 1.0, 0.5)
    # mat.diffuse_shader = 'LAMBERT'
    # mat.diffuse_intensity = 1.0
    # mat.use_transparency = True
    # mat.alpha = 0.3
    bpy.data.objects[frame].show_transparent = True


    # mat = bpy.data.materials['MaterialName']
    obj.data.materials.append(mat)

    return obj


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

    frameName: StringProperty()

    @classmethod
    def run(cls, frameName=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)  # todo condition for physicframe
    def execute(self, context):
        arm = context.active_object

        frame = bpy.data.objects[self.frameName]

        for obj in bpy.data.objects:
            obj.select_set(False)

        frame.select_set(True)
        arm.select_set(True)

        context.view_layer.objects.active = arm

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
    bl_label = "Assign Selected Physics Frame To Active Bone"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected, SingleMassObjectSelected)
    def execute(self, context):
        bpy.ops.object.parent_set(type='BONE')

        # if bpy.context.active_bone.parent:
        #     to_parent_matrix = bpy.context.active_bone.parent.matrix_local
        # else:
        #     to_parent_matrix = Matrix()
        # from_parent_matrix, bone_matrix = bpy.context.active_bone.RobotDesigner.getTransform()
        # armature_matrix = bpy.context.active_object.matrix_basis

        # # find selected physics frame
        # for ob in bpy.data.objects:
        #     if ob.select and ob.RobotDesigner.tag == 'PHYSICS_FRAME':
        #         frame = ob
        #         print(frame.name)

        # frame.matrix_basis = armature_matrix*to_parent_matrix*from_parent_matrix*bone_matrix
        # frame.matrix_basis = parent_matrix*armature_matrix*bone_matrix
        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class ComputePhysical(RDOperator):
    bl_idname = config.OPERATOR_PREFIX + "computephysicsframe"
    bl_label = "Compute Inertia From Mesh"

    from_visual_geometry: BoolProperty(name="From visual geometry")

    class SegmentAssociations(object):
        def __init__(self):
            self.visual = None
            self.collision = None
            self.physics_frame = None

        def __str__(self):
            return '<' + ', '.join([str(self.visual), str(self.collision), str(self.physics_frame)]) + '>'

    def maybe_compute_inertia(self, bone, associations):
        assert associations.physics_frame is not None
        if associations.collision and not self.from_visual_geometry:
            the_mesh = associations.collision
        elif associations.visual and self.from_visual_geometry:
            the_mesh = associations.visual
        else:
            return
        bounds = the_mesh.bound_box
        dimension = the_mesh.dimensions
        len = (bounds[-1][0] - bounds[0][0],
               bounds[-1][1] - bounds[0][1],
               bounds[1][2] - bounds[0][2])  # The 1 is no error!
        len = (dimension[0], dimension[1], dimension[2])
        com = list(map(lambda x: x * 0.5,
                       (bounds[-1][0] + bounds[0][0],
                        bounds[-1][1] + bounds[0][1],
                        bounds[1][2] + bounds[0][2])))
        mass = 1.0
        # Of a Brick.
        Iunit = (1. / 12. * (len[1] ** 2 + len[2] ** 2),
                 1. / 12. * (len[0] ** 2 + len[2] ** 2),
                 1. / 12. * (len[0] ** 2 + len[1] ** 2))
        print("bone:", bone, len, mass, Iunit, com)
        d = associations.physics_frame.RobotDesigner.dynamics
        d.inertiaXX = mass * Iunit[0]
        d.inertiaYY = mass * Iunit[1]
        d.inertiaZZ = mass * Iunit[2]
        d.inertiaXY = 0.
        d.inertiaXZ = 0.
        d.inertiaYZ = 0.
        d.mass = mass
        # d.inertiaTrans = com
        # d.inertiaRot   = [0., 0., 0.]
        # print ("Setting matrix "+str(the_mesh.matrix_world))
        m_com = Matrix.Translation(com)
        associations.physics_frame.matrix_world = the_mesh.matrix_world @ m_com
        d.scale_update(bpy.context)

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        armature = context.active_object
        # print (self.__class__.__name__)

        # Mapping from bone to things
        segment_associations = defaultdict(self.SegmentAssociations)
        for obj in armature.children:
            if obj.parent_bone:
                bone = armature.data.bones[obj.parent_bone]
                print("visit ", obj, obj.parent_bone, bone, bone.select)
                if bone.select:
                    if obj.RobotDesigner.tag == 'PHYSICS_FRAME':
                        segment_associations[bone].physics_frame = obj
                    elif obj.RobotDesigner.tag == 'COLLISION' or 'BASIC_COLLISION_' in obj.RobotDesigner.tag:
                        segment_associations[bone].collision = obj
                    elif obj.RobotDesigner.tag == 'DEFAULT':
                        segment_associations[bone].visual = obj

        bones = [b for b in armature.data.bones if b.select]

        for bone in bones:
            self.maybe_compute_inertia(bone, segment_associations[bone])

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class ComputeMass(RDOperator):
    bl_idname = config.OPERATOR_PREFIX + "computemass"
    bl_label = "Compute Mass Properties From Mesh"

    density: FloatProperty(name="Density (kg/m^3)", precision=4, step=0.01, default=1.0)
    from_visual_geometry: BoolProperty(name="From visual geometry")

    class SegmentAssociations(object):
        def __init__(self):
            self.visual = None
            self.collision = None
            self.physics_frame = None

        def __str__(self):
            return '<' + ', '.join([str(self.visual), str(self.collision), str(self.physics_frame)]) + '>'

    def maybe_compute_and_assign_mass_props(self, bone, associations):
        assert associations.physics_frame is not None
        if associations.collision and not self.from_visual_geometry:
            the_mesh = associations.collision
        elif associations.visual and self.from_visual_geometry:
            the_mesh = associations.visual
        else:
            return
        bounds = the_mesh.bound_box
        dimension = the_mesh.dimensions
        len = (bounds[-1][0] - bounds[0][0],
               bounds[-1][1] - bounds[0][1],
               bounds[1][2] - bounds[0][2])  # The 1 is no error!
        len = (dimension[0], dimension[1], dimension[2])
        mass = len[0] * len[1] * len[2] * self.density
        # Of a Brick.
        d = associations.physics_frame.RobotDesigner.dynamics
        d.mass = mass
        # d.inertiaTrans = com
        # d.inertiaRot   = [0., 0., 0.]
        # print ("Setting matrix "+str(the_mesh.matrix_world))
        d.scale_update(bpy.context)

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        armature = context.active_object
        # print (self.__class__.__name__)

        # Mapping from bone to things
        segment_associations = defaultdict(self.SegmentAssociations)
        for obj in armature.children:
            if obj.parent_bone:
                bone = armature.data.bones[obj.parent_bone]
                print("visit ", obj, obj.parent_bone, bone, bone.select)
                if bone.select:
                    if obj.RobotDesigner.tag == 'PHYSICS_FRAME':
                        segment_associations[bone].physics_frame = obj
                    elif obj.RobotDesigner.tag == 'COLLISION' or 'BASIC_COLLISION_' in obj.RobotDesigner.tag:
                        segment_associations[bone].collision = obj
                    elif obj.RobotDesigner.tag == 'DEFAULT':
                        segment_associations[bone].visual = obj

        bones = [b for b in armature.data.bones if b.select]

        for bone in bones:
            self.maybe_compute_and_assign_mass_props(bone, segment_associations[bone])

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


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
    bl_label = "Detach Selected Physics Frame"

    frameName: StringProperty()

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


