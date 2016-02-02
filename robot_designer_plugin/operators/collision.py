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
from bpy.props import FloatProperty, IntProperty
# import mathutils

# ######
# RobotDesigner imports
from ..core import config, PluginManager, RDOperator
from .helpers import ModelSelected, SingleMeshSelected
from .rigid_bodies import SelectGeometry

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class GenerateAllCollisionMeshes(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "generatallecollisionmeshes"
    bl_label = "Generate All Collision Meshes"

    shrinkWrapOffset = FloatProperty(name="Shrinkwrap Offset", default=0.001,
                                     unit='LENGTH', min=0, max=0.5)
    subdivisionLevels = IntProperty(name="Subdivision Levels", default=2)


    @RDOperator.OperatorLogger
    # @Postconditions(ModelSelected)
    def execute(self, context):
        visuals = [o.name for o in bpy.data.objects if o.type == 'MESH'
                   and o.parent == context.active_object and o.RobotEditor.tag != "COLLISION"]

        self.logger.debug("Visuals: %s", visuals)

        for i in visuals:
            SelectGeometry.run(mesh_name=i)
            GenerateCollisionMesh.run(shrinkWrapOffset=self.shrinkWrapOffset, subdivisionLevels=self.subdivisionLevels)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class GenerateCollisionMesh(RDOperator):
    """
    :ref:`operator` for creating a collision mesh using the builtin
    subdivide and shrinkwrap operators.

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "generatecollisionmesh"
    bl_label = "Generate Collision Mesh for selected"

    shrinkWrapOffset = FloatProperty(name="Shrinkwrap Offset", default=0.001,
                                     unit='LENGTH', min=0, max=0.5)
    subdivisionLevels = IntProperty(name="Subdivision Levels", default=2)

    @classmethod
    def run(cls, shrinkWrapOffset, subdivisionLevels):
        return super().run(**cls.pass_keywords())
    @RDOperator.OperatorLogger
    def execute(self, context):
        from . import segments, model

        target_name = [i.name for i in bpy.context.selected_objects if i.type == 'MESH'][0]

        self.logger.debug("Creating Collision mesh for: %s", target_name)
        armature = context.active_object.name

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects[target_name]

        d = bpy.data.objects[target_name].dimensions
        bpy.ops.mesh.primitive_cube_add(
                location=bpy.data.objects[target_name].location,
                rotation=bpy.data.objects[target_name].rotation_euler)
        bpy.context.object.dimensions = d * 1000000
        bpy.ops.object.transform_apply(scale=True)
        mod = bpy.context.object.modifiers.new(name='subsurf', type='SUBSURF')
        mod.subdivision_type = 'SIMPLE'
        mod.levels = self.subdivisionLevels
        bpy.ops.object.modifier_apply(modifier='subsurf')
        mod = bpy.context.object.modifiers.new(name='shrink_wrap',
                                               type='SHRINKWRAP')
        mod.wrap_method = "NEAREST_SURFACEPOINT"
        mod.offset = self.shrinkWrapOffset * 1000
        self.logger.debug("%f, %f", mod.offset, self.shrinkWrapOffset)
        mod.target = bpy.data.objects[target_name]
        bpy.ops.object.modifier_apply(modifier='shrink_wrap')

        bpy.context.object.name = 'COL_' + target_name
        name = bpy.context.object.name

        context.active_object.RobotEditor.tag = 'COLLISION'
        self.logger.debug("Created mesh: %s", bpy.context.active_object.name)

        if 'RD_COLLISON_OBJECT_MATERIAL' in bpy.data.materials:
            bpy.ops.object.material_slot_add()
            context.active_object.data.materials[0] = bpy.data.materials[
                'RD_COLLISON_OBJECT_MATERIAL']
            self.logger.debug("Assigned material to : %s",
                              bpy.context.active_object.name)
        else:
            self.logger.debug("Could not find material for collision mesh")

        bpy.ops.object.select_all(action='DESELECT')

        model.SelectModel.run(model_name=armature)
        segments.SelectSegment.run(segment_name=bpy.data.objects[target_name].parent_bone)
        bpy.data.objects[name].select = True
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        bpy.ops.object.select_all(action='DESELECT')
        model.SelectModel.run(model_name=armature)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
