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
from bpy.props import StringProperty, BoolProperty
from mathutils import Vector, Matrix, Euler
from math import pi

# ######
# RobotDesigner imports
from ..core import config, PluginManager, Condition, RDOperator
from .helpers import ModelSelected, SingleMeshSelected, SingleSegmentSelected
from ..properties.globals import global_properties


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


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateWrappingSphere(RDOperator):
    bl_idname = config.OPERATOR_PREFIX + "create_sphere"
    bl_label = "Create new sphere"

    sphere_name = StringProperty(name="Enter new sphere name:")

    @classmethod
    def run(cls, sphere_name):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

        from .model import SelectModel
        from .rigid_bodies import SelectGeometry

        model = bpy.context.active_object
        active_muscle = bpy.data.objects[global_properties.active_muscle.get(bpy.context.scene)]

        bpy.ops.mesh.primitive_uv_sphere_add(size=1, calc_uvs=True, view_align=False, enter_editmode=False)

        sphere = bpy.context.active_object
        sphere.name = self.sphere_name

        sphere.RobotDesigner.wrap.muscleNames.add()
        nrm = len(sphere.RobotDesigner.wrap.muscleNames)
        sphere.RobotDesigner.wrap.muscleNames[nrm-1].name = active_muscle.name

        active_muscle.RobotDesigner.muscles.connectedWraps.add()
        nrw = len(active_muscle.RobotDesigner.muscles.connectedWraps)
        active_muscle.RobotDesigner.muscles.connectedWraps[nrw-1].wrappingName = sphere.name

        lmat = bpy.data.materials.new(self.sphere_name)
        lmat.diffuse_color = (0.0, 0.135, 0.0)
        lmat.use_shadeless = True
        sphere.data.materials.append(lmat)

        sphere.RobotDesigner.tag = 'WRAPPING'
        sphere.RobotDesigner.wrap.WrappingType = 'WRAPPING_SPHERE'

        SelectModel.run(model_name=model.name)
        SelectGeometry.run(geometry_name=sphere.name)

        return{'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateWrappingCylinder(RDOperator):
    bl_idname = config.OPERATOR_PREFIX + "create_cylinder"
    bl_label = "Create new cylinder"

    cylinder_name = StringProperty(name="Enter new cylinder name:")

    @classmethod
    def run(cls, cylinder_name):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

        from .model import SelectModel
        from .rigid_bodies import SelectGeometry

        model = bpy.context.active_object
        active_muscle = bpy.data.objects[global_properties.active_muscle.get(bpy.context.scene)]

        bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=1, view_align=False, enter_editmode=False)

        cylinder = bpy.context.active_object
        cylinder.name = self.cylinder_name

        cylinder.RobotDesigner.wrap.muscleNames.add()
        nrm = len(cylinder.RobotDesigner.wrap.muscleNames)
        cylinder.RobotEditor.wrap.muscleNames[nrm - 1].name = active_muscle.name

        active_muscle.RobotDesigner.muscles.connectedWraps.add()
        nrw = len(active_muscle.RobotDesigner.muscles.connectedWraps)
        active_muscle.RobotDesigner.muscles.connectedWraps[nrw - 1].wrappingName = cylinder.name

        lmat = bpy.data.materials.new(self.cylinder_name)
        lmat.diffuse_color = (0., 0.135, 0.0)
        lmat.use_shadeless = True
        cylinder.data.materials.append(lmat)

        cylinder.RobotDesigner.tag = 'WRAPPING'
        cylinder.RobotDesigner.wrap.WrappingType = 'WRAPPING_CYLINDER'

        SelectModel.run(model_name=model.name)
        SelectGeometry.run(geometry_name=cylinder.name)

        return{'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected, SingleSegmentSelected)
@PluginManager.register_class
class RenameWrappingObject(RDOperator):
    """
    :term:`operator` for renaming the selected wrapping object


    """
    bl_idname = config.OPERATOR_PREFIX + "rename_wrapping_object"
    bl_label = ""

    new_name = StringProperty(name="Enter new name:")


    @RDOperator.OperatorLogger
    def execute(self, context):
        selected_object = global_properties.mesh_name.get(context.scene)

        for muscles in context.scene.objects[selected_object].RobotDesigner.wrap.muscleNames:
            i = 0
            for connected_wraps in context.scene.objects[muscles.name].RobotDesigner.muscles.connectedWraps:
                if connected_wraps.wrappingName == selected_object:
                    context.scene.objects[muscles.name].RobotDesigner.muscles.connectedWraps[i].wrappingName = \
                        self.new_name
                    break
                i = i + 1

        bpy.data.objects[global_properties.mesh_name.get(bpy.context.scene)].name = self.new_name
        global_properties.mesh_name.set(context.scene, self.new_name)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, new_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DeleteWrappingObject(RDOperator):
    """
    :term:`operator` for deleting the selected wrapping object.


    """
    bl_idname = config.OPERATOR_PREFIX + "delete_wrapping_object"
    bl_label = ""

    @RDOperator.OperatorLogger
    def execute(self, context):

        selected_object = global_properties.mesh_name.get(context.scene)

        for muscles in context.scene.objects[selected_object].RobotDesigner.wrap.muscleNames:
            i=0
            for connected_wraps in context.scene.objects[muscles.name].RobotDesigner.muscles.connectedWraps:
                if connected_wraps.wrappingName == selected_object:
                    context.scene.objects[muscles.name].RobotDesigner.muscles.connectedWraps.remove(i)
                    break
                i = i+1


        bpy.data.objects.remove(bpy.data.objects[selected_object], True)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DisconnectWrappingObject(RDOperator):

    bl_idname = config.OPERATOR_PREFIX + "disconnect_wrapping_object"
    bl_label = ""

    wrappingOrder = bpy.props.IntProperty(name="Disconnect wrapping object:")

    @RDOperator.OperatorLogger
    def execute(self, context):

        active_muscle = global_properties.active_muscle.get(context.scene)

        connected_wraps = context.scene.objects[active_muscle].RobotDesigner.muscles.connectedWraps

        active_wrap = connected_wraps[self.wrappingOrder-1].wrappingName

        i = 0
        for muscles in context.scene.objects[active_wrap].RobotDesigner.wrap.muscleNames:
            if muscles.name == active_muscle:
                context.scene.objects[active_wrap].RobotDesigner.wrap.muscleNames.remove(i)
            i = i+1

        connected_wraps.remove(self.wrappingOrder-1)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

@RDOperator.Preconditions(ModelSelected, SingleMeshSelected, SingleSegmentSelected)
@PluginManager.register_class
class AttachWrappingObject(RDOperator):
    """
    :ref:`operator` for assigning a geometry to a segment.
    """
    bl_idname = config.OPERATOR_PREFIX + "attach_wrapping_object"
    bl_label = "Assign object to active segment?"


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected, SingleSegmentSelected)
    def execute(self, context):
        # Set parenting relation. There are two ways to attach geometry to a bone:
        # This way, which sets the parent_bone variable of the object. Or by using vertex weights,
        # in which case parent_bone should be left empty.
        # See also https://blender.stackexchange.com/questions/9200/make-object-a-a-parent-of-object-b-via-python
        # At this point bpy.context.scene.objects.active should point to the armature which will be the parent.
        bpy.ops.object.parent_set(type='BONE', keep_transform=False)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class DetachWrappingObject(RDOperator):
    """
    :term:`operator` for detaching a single :term:`geometry` from a :term:`segment`.
    """
    bl_idname = config.OPERATOR_PREFIX + "detach_wrapping_object"
    bl_label = "Detach selected object?"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):
        from . import segments, model
        mesh_name = global_properties.mesh_name.get(context.scene)
        current_mesh = bpy.data.objects[mesh_name]
        mesh_global = current_mesh.matrix_world
        current_mesh.parent = None

        current_mesh.matrix_world = mesh_global

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DetachAllWrappingObjects(RDOperator):
    """
    :ref:`operator` for detaching *all* :term:`geometries` from the selected :term:`model`.
    """
    bl_idname = config.OPERATOR_PREFIX + "detach_all_meshes"
    bl_label = "Detach all wrapping geometries?"

    @classmethod
    def run(cls, confirmation=True):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        from .rigid_bodies import SelectGeometry
        meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH' and
                  obj.parent_bone is not '' and obj.RobotDesigner.tag == 'WRAPPING']

        for mesh in meshes:
            SelectGeometry.run(geometry_name=mesh.name)
            DetachWrappingObject.run()

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectWrappingObject(RDOperator):
    bl_idname = config.OPERATOR_PREFIX + "select_wrapping_object"
    bl_label = "Select wrapping object: "

    wrapping_name = StringProperty()

    @RDOperator.OperatorLogger
    def execute(self, context):
        model = bpy.data.objects[global_properties.model_name.get(context.scene)]
        active_muscle = bpy.data.objects[global_properties.active_muscle.get(bpy.context.scene)]

        wrapping_object = context.scene.objects[self.wrapping_name]
        wrapping_object.RobotDesigner.wrap.muscleNames.add()
        nr = len(wrapping_object.RobotDesigner.wrap.muscleNames)
        wrapping_object.RobotDesigner.wrap.muscleNames[nr - 1].name = active_muscle.name

        wrapList = active_muscle.RobotDesigner.muscles.connectedWraps
        wrapList.add()
        nrw = len(wrapList)
        wrapList[nrw-1].wrappingName = self.wrapping_name


        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, wrapping_name=""):
        return super().run(**cls.pass_keywords())




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
            # e= C.active_bone.RobotDesigner.Euler

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
            SelectGeometry.run(geometry_name=bezier.name)  #
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
        axis = C.active_bone.RobotDesigner.axis
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

            max_length = max(distance_to_children + [segment_length])
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
                bpy.ops.mesh.primitive_cone_add(radius1=segment_length / 10, radius2=segment_length / 10)

            C.active_object.name = bone_name + '_axis'
            new_name = C.active_object.name
            SelectModel.run(model_name=model.name)
            SelectSegment.run(bone_name)
            SelectGeometry.run(new_name)
            AssignGeometry.run()

        return {'FINISHED'}
