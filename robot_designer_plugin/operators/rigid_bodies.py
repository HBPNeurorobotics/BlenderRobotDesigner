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

# ######
# System imports
# import os
# import sys
# import math

# ######
# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty
# import mathutils

# ######
# RobotDesigner imports
from ..core import config, PluginManager, Condition, RDOperator
from .helpers import ModelSelected, SingleMeshSelected, ObjectMode


# operator to select mesh
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectGeometry(RDOperator):
    """
    :ref:`operator` for ...




    """
    bl_idname = config.OPERATOR_PREFIX + "selectmesh"
    bl_label = "Select Mesh"

    mesh_name = StringProperty()

    @classmethod
    def run(cls, mesh_name=""):
        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):
        mesh = bpy.data.objects[self.mesh_name]

        if mesh.type != 'MESH':
            self.report({'ERROR'}, 'Object is no geometry (Mesh). Is %s' % mesh.type)
            context.scene.RobotEditor.meshName = 'Search'
            return {'FINISHED'}

        context.scene.RobotEditor.meshName = 'Search'

        arm = context.active_object

        for obj in bpy.data.objects:
            obj.select = False

        mesh.select = True
        arm.select = True

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class AssignGeometry(RDOperator):
    """
    :ref:`operator` for assigning a geometry to a segment.




    """
    bl_idname = config.OPERATOR_PREFIX + "assignmesh"
    bl_label = "Assign selected mesh to active bone"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class RenameAllGeometries(RDOperator):
    """
    :ref:`operator` for renaming geometries using their parented segment's name.




    """
    bl_idname = config.OPERATOR_PREFIX + "renamemeshes"
    bl_label = "Renames meshes after bones"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        current_mesh = bpy.data.objects[context.scene.RobotEditor.meshName]
        for i in bpy.data.objects:
            if i.parent_bone != '' and i.type == 'MESH':
                if i.name == current_mesh:
                    context.scene.RobotEditor.meshName = i.parent_bone
                i.name = 'Visualization_' + i.parent_bone

        return {'FINISHED'}


# operator to unassign mesh from bone
@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class DetachGeometry(RDOperator):
    """
    :term:`operator` for detaching a single :term:`geometry` form a :term:`segment`.




    """
    bl_idname = config.OPERATOR_PREFIX + "unassignmesh"
    bl_label = "Unassign selected mesh"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):
        current_mesh = bpy.data.objects[context.scene.RobotEditor.meshName]
        mesh_global = current_mesh.matrix_world
        current_mesh.parent = None
        current_mesh.matrix_world = mesh_global

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DetachAllGeometries(RDOperator):
    """
    :ref:`operator` for detaching *all* :term:`geometries` from the selected :term:`model`.




    """
    bl_idname = config.OPERATOR_PREFIX + "unassignallmeshes"
    bl_label = "Unassign ALL meshes"

    confirmation = BoolProperty(
            name="This disconnects all collision OR visual geometries from the model. Are you sure?")

    @classmethod
    def run(cls, confirmation=True):
        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        mesh_type = context.scene.RobotEditor.meshType
        if mesh_type == 'DEFAULT':
            meshes = [obj for obj in bpy.data.objects if
                      obj.type == 'MESH' and obj.parent_bone is not '' and obj.RobotEditor.tag != 'COLLISION']
        else:
            meshes = [obj for obj in bpy.data.objects if
                      obj.type == 'MESH' and obj.parent_bone is not '' and obj.RobotEditor.tag == 'COLLISION']

        if self.confirmation:
            for mesh in meshes:
                SelectGeometry.run(mesh_name=mesh.name)
                DetachGeometry.run()

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectAllGeometries(RDOperator):
    """
    :ref:`operator` for selecting all geometries.




    """
    bl_idname = config.OPERATOR_PREFIX + "setallmeshesactiveobject"
    bl_label = "Select all geometries"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ObjectMode)
    def execute(self, context):
        mesh_type = context.scene.RobotEditor.meshType
        meshes = {obj.name for obj in bpy.data.objects if
                  not obj.parent_bone is None and
                  obj.type == 'MESH' and
                  obj.RobotEditor.tag == mesh_type}
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')

        for mesh in meshes:
            bpy.data.objects[mesh].select = True
            context.scene.objects.active = bpy.data.objects[mesh]

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected,ObjectMode, SingleMeshSelected)
@PluginManager.register_class
class SetGeometryActive(RDOperator):
    """
    :ref:`operator` for ...
    """
    bl_idname = config.OPERATOR_PREFIX + "setseletedmeshactiveobject"
    bl_label = "Select geometry"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        selected = [i.name for i in bpy.context.selected_objects if i.type == 'MESH'][0]
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[selected].select = True
        context.scene.objects.active = bpy.data.objects[selected]
        return {'FINISHED'}
