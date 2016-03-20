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
#
#   2016-02-08: Stefan Ulbrich (FZI), initial version of mesh generation.
#
# ######

# ######
# System imports
# import os
# import sys
# import math

# ######
# Blender imports
import bpy
# from bpy.props import StringProperty, BoolProperty
from mathutils import Vector, Matrix, Euler
from math import pi

# ######
# RobotDesigner imports
from ..core import config, PluginManager, Condition, RDOperator
from .helpers import ModelSelected, SingleMeshSelected, SingleSegmentSelected


# operator to select mesh
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class GenerateMeshFromAllSegment(RDOperator):
    """
    :ref:`operator` for ...

    """
    bl_idname = config.OPERATOR_PREFIX + "generate_all_meshes"
    bl_label = "Generate geometry for all segments"

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        from .model import SelectModel
        from .rigid_bodies import SelectGeometry, AssignGeometry
        from .segments import SelectSegment

        C = bpy.context
        D = bpy.data
        model_name = C.active_object.name

        segment_names = [i.name for i in C.active_object.data.bones if i.parent]

        for segment in segment_names:
            SelectModel.run(model_name=model_name)
            SelectSegment.run(segment_name=segment)
            GenerateMeshFromSegment.run()

        return {'FINISHED'}


# operator to select mesh
@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class GenerateMeshFromSegment(RDOperator):
    """
    :ref:`operator` for ...

    """
    bl_idname = config.OPERATOR_PREFIX + "generate_mesh"
    bl_label = "Generate geometry for segment"

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected)  # Not SingleMeshSelected, in case of abortion
    def execute(self, context):

        from .model import SelectModel
        from .rigid_bodies import SelectGeometry, AssignGeometry
        from .segments import SelectSegment

        C = bpy.context
        D = bpy.data

        model = C.active_object

        bone_name = C.active_bone.name
        pose_bone = C.active_object.pose.bones[bone_name]

        if not C.active_bone.parent:
            self.report({"ERROR"}, "Does not work for root segments")
            return {'CANCELLED'}

        parent_bone = C.active_object.pose.bones[C.active_bone.parent.name]
        parent_name = parent_bone.name

        parent_frame = model.matrix_world * parent_bone.matrix

        bone_world = model.matrix_world * pose_bone.matrix
        bone_to_parent = bone_world.inverted() * parent_frame
        parent_to_bone = parent_frame.inverted() * bone_world
        l = bone_to_parent.translation.length

        v1 = bone_to_parent.translation
        max_v1 = max(abs(i) for i in v1)
        v2 = parent_to_bone.translation
        max_v2 = max(abs(i) for i in v2)

        if max_v1 != 0:
            bpy.ops.curve.primitive_bezier_circle_add(radius=l / 20)
            print(l)

            bevel = C.active_object

            bezier = bpy.ops.curve.primitive_bezier_curve_add()

            bezier = C.active_object
            bezier.data.bevel_object = bevel

            bezier.matrix_world = bone_world

            print(bezier.matrix_world)
            # e= C.active_bone.RobotEditor.Euler

            bpy.ops.object.mode_set(mode="EDIT", toggle=False)

            a = bezier.data.splines[0].bezier_points[0]
            b = bezier.data.splines[0].bezier_points[1]

            a.co = (0, 0, 0)
            b.co = bone_to_parent.translation

            print(v1, max_v1)
            v1 = Vector([0.1 * i / max_v1 if abs(i) == max_v1 else 0.0 for i in v1])

            v2 = Vector([0.1 * i / max_v2 if abs(i) == max_v2 else 0.0 for i in v2])
            # v2 = Vector(v2)#.to_4d()
            # v2[3]=0.0

            a.handle_right = v1
            a.handle_left = -1 * v1
            print(v1, a.handle_right, a.handle_left)

            m = Matrix()
            m.translation = v2

            # m[3][3] = 0
            # b.co = (bone_to_parent *m).translation
            print(m, bone_to_parent.inverted() * parent_frame * m)
            b.handle_left = (bone_to_parent * m).translation
            m.translation = -1 * v2

            b.handle_right = (bone_to_parent * m).translation
            print(v2, b.handle_right, b.handle_left)

            # print(a.co,b.co)

            bpy.ops.object.mode_set(mode="OBJECT", toggle=False)
            bpy.ops.object.convert(target='MESH')
            bpy.ops.object.select_all(action='DESELECT')
            bevel.select = True
            bpy.ops.object.delete()

            SelectModel.run(model_name=model.name)
            SelectGeometry.run(geometry_name=bezier.name) #
            SelectSegment.run(segment_name=parent_name)
            AssignGeometry.run()
            SelectSegment.run(segment_name=bone_name)


        GenerateMeshFromJoint.run()

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class GenerateMeshFromJoint(RDOperator):
    bl_idname = config.OPERATOR_PREFIX + "generate_joint"
    bl_label = "Generate geometry for joint"

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected)  # Not SingleMeshSelected, in case of abortion
    def execute(self, context):

        from .model import SelectModel
        from .rigid_bodies import SelectGeometry, AssignGeometry
        from .segments import SelectSegment

        C = bpy.context
        D = bpy.data

        model = C.active_object

        bone_name = C.active_bone.name
        axis = C.active_bone.RobotEditor.axis
        pose_bone = C.active_object.pose.bones[bone_name]
        parent_bone = pose_bone.parent
        bone_to_parent = pose_bone.matrix.inverted() * parent_bone.matrix
        bone_world = model.matrix_world * pose_bone.matrix

        segment_length = bone_to_parent.translation.length
        distance_to_children = [(child.matrix.inverted() * pose_bone.matrix).translation.length for child in
                                pose_bone.children]

        self.logger.debug("%s, %s", segment_length, distance_to_children)

        # if there is no translation to parent, the parent (or its parent) draws the joint
        if bone_to_parent.translation.length > 0.001:

            max_length = max(distance_to_children+[segment_length])
            # If there is only one children, and its a distance 0, we have a ball joint
            if len(pose_bone.children) == 1 and distance_to_children[0] < 0.001:

                bpy.ops.mesh.primitive_uv_sphere_add(size=segment_length / 15.0)
                C.active_object.matrix_world = bone_world
            # if there IS a child, at distance >0 (or more than one child), draw a hinge joint
            elif len(pose_bone.children):
                bpy.ops.mesh.primitive_cylinder_add(radius=max_length / 15, depth=max_length / 5)
                if axis == 'X':
                    m = Euler((0, 0, pi / 4)).to_matrix().to_4x4()
                elif axis == 'Y':
                    m = Euler((0, 0, pi / 4)).to_matrix().to_4x4()
                else:
                    m = Matrix()

                C.active_object.matrix_world = bone_world * m
            else:
                bpy.ops.mesh.primitive_cone_add(radius1=segment_length/10,radius2=segment_length/10)


            C.active_object.name = bone_name + '_axis'
            new_name = C.active_object.name
            SelectModel.run(model_name=model.name)
            SelectSegment.run(bone_name)
            SelectGeometry.run(new_name)
            AssignGeometry.run()

        return {'FINISHED'}
