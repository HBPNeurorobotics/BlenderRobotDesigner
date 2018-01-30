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
from .helpers import ModelSelected, SingleMeshSelected, ObjectMode, SingleSegmentSelected

from ..properties.globals import global_properties

# operator to select mesh
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectGeometry(RDOperator):
    """
    :ref:`Operator <operator>` for selecting a geometry (:class:`bpy.types.Object` with `bpy.types.Mesh` data)
    second to the selected model (Blender object with :class:`bpy.types.Armature` data)
    """
    bl_idname = config.OPERATOR_PREFIX + "select_geometry"
    bl_label = "Select geometry"

    geometry_name = StringProperty()

    @classmethod
    def run(cls, geometry_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):
        mesh = bpy.data.objects[self.geometry_name]

        if mesh.type != 'MESH':
            self.report({'ERROR'}, 'Object is no geometry (Mesh). Is %s' % mesh.type)
            global_properties.mesh_name.set(context.scene, 'Search')
            return {'FINISHED'}

        # Has the side effect of de-selecting all other objects except for the armature and our mesh.
        global_properties.mesh_name.set(context.scene, self.geometry_name)

        context.region.tag_redraw()
        context.area.tag_redraw()
        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected, SingleSegmentSelected)
@PluginManager.register_class
class AssignGeometry(RDOperator):
    """
    :ref:`operator` for assigning a geometry to a segment.
    """
    bl_idname = config.OPERATOR_PREFIX + "assign_geometry"
    bl_label = "Assign selected geometry to active segment"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected, SingleSegmentSelected)
    def execute(self, context):
        # Set parenting relation. There are two ways to attach geometry to a bone:
        # This way, which sets the parent_bone variable of the object. Or by using vertex weights,
        # in which case parent_bone should be left empty.
        # See also https://blender.stackexchange.com/questions/9200/make-object-a-a-parent-of-object-b-via-python
        # At this point bpy.context.scene.objects.active should point to the armature which will be the parent.
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        # In order to get the child we have to jump through some hoops.
        obj = bpy.data.objects[global_properties.mesh_name.get(context.scene)]
        # Change the name depending on whether we want collision geometry or visual geometry.

        def maybe_remove_prefix(s, prefix):
            return s[len(prefix):] if s.startswith(prefix) else s

        def maybe_remove_postfix(s, postfix):
            return s[:-len(postfix)] if s.endswith(postfix) else s

        new_name = obj.name
        new_name = maybe_remove_postfix(new_name, '.001') # Heuristic to remove the suffix created by cloning.
        # Heuristics to remove previously assigned prefixes.
        # Since the prefix is regenerated it seems in order to try to remove the old prefix.
        if len(new_name)>len('VIS_'):
            new_name = maybe_remove_prefix(new_name, 'VIS_')
        if len(new_name)>len('COL_'):
            new_name = maybe_remove_prefix(new_name, 'COL_')
        if global_properties.assign_collision.get(context.scene) == True or obj.RobotEditor.tag == 'COLLISION':
            obj.RobotEditor.tag = 'COLLISION'
            new_name = "COL_" + new_name
        else:
            obj.RobotEditor.tag == 'DEFAULT'
            new_name = "VIS_" + new_name
        obj.name = new_name
        obj.RobotEditor.fileName = new_name
        # Update the global reference to the selected mesh.
        global_properties.mesh_name.set(context.scene, obj.name)
        # This is just a boolean variable which is reset here to False. It helps
        # determine whether we want a collision mesh or a visual one.
        global_properties.assign_collision.set(context.scene, False)

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class RenameAllGeometries(RDOperator):
    """
    :ref:`operator` for renaming geometries using their parented segment's name.




    """
    bl_idname = config.OPERATOR_PREFIX + "rename_geometries"
    bl_label = "Rename geometries after segments"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        mesh_name = global_properties.mesh_name.get(context.scene)
        current_mesh = bpy.data.objects[mesh_name]
        for i in bpy.data.objects:
            if i.parent_bone != '' and i.type == 'MESH':
                i.name = i.name[:4] + i.parent_bone
                i.RobotEditor.fileName = i.name

        global_properties.mesh_name.set(context.scene, current_mesh.name[:4] + current_mesh.parent_bone )

        return {'FINISHED'}


# operator to unassign mesh from bone
@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class DetachGeometry(RDOperator):
    """
    :term:`operator` for detaching a single :term:`geometry` form a :term:`segment`.
    """
    bl_idname = config.OPERATOR_PREFIX + "unassignmesh"
    bl_label = "Detach selected geometry"

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
        current_mesh.RobotEditor.tag = 'DEFAULT'
        if current_mesh.name.startswith("VIS_") or current_mesh.name.startswith("COL_") :
            current_mesh.name = current_mesh.name[4:]

        current_mesh.matrix_world = mesh_global

        global_properties.mesh_name.set(context.scene, current_mesh.name)

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DetachAllGeometries(RDOperator):
    """
    :ref:`operator` for detaching *all* :term:`geometries` from the selected :term:`model`.
    """
    bl_idname = config.OPERATOR_PREFIX + "unassignallmeshes"
    bl_label = "Detach all geometries"

    confirmation = BoolProperty(
        name="This disconnects all collision OR visual geometries from the model. Are you sure?")

    @classmethod
    def run(cls, confirmation=True):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        mesh_type =  global_properties.display_mesh_selection.get(context.scene)
        if mesh_type == 'all':
            meshes = [obj for obj in bpy.data.objects if
                      obj.type == 'MESH' and obj.parent_bone is not '']
        elif mesh_type == 'visual':
            meshes = [obj for obj in bpy.data.objects if
                      obj.type == 'MESH' and obj.parent_bone is not '' and obj.RobotEditor.tag != 'COLLISION']
        elif mesh_type == 'collision':
            meshes = [obj for obj in bpy.data.objects if
                      obj.type == 'MESH' and obj.parent_bone is not '' and obj.RobotEditor.tag == 'COLLISION']
        else:
            self.confirmation = False



        if self.confirmation:
            for mesh in meshes:
                SelectGeometry.run(geometry_name=mesh.name)
                DetachGeometry.run()
                if mesh.name.startswith("VIS_") or mesh.name.startswith("COL_"):
                    mesh.name = mesh.name[4:]
                    mesh.RobotEditor.tag = 'DEFAULT'

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
        mesh_type =  global_properties.mesh_type.get(context.scene)
        meshes = {obj.name for obj in bpy.data.objects if
                  not obj.parent_bone is None and
                  obj.type == 'MESH' }
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')

        for mesh in meshes:
            bpy.data.objects[mesh].select = True
            context.scene.objects.active = bpy.data.objects[mesh]

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected, ObjectMode, SingleMeshSelected)
@PluginManager.register_class
class SetGeometryActive(RDOperator):
    """
    :ref:`operator` for ...
    """
    bl_idname = config.OPERATOR_PREFIX + "setseletedmeshactiveobject"
    bl_label = "Make geometry active"

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


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class ReduceAllGeometry(RDOperator):
    """
    :term:`operator` for reducing the polygon number of all meshes in the scene.


    """
    bl_idname = config.OPERATOR_PREFIX + "polygonallreduction"
    bl_label = "Apply to all meshes"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):

        hide_geometry = global_properties.display_mesh_selection.get(context.scene)
        geometry_names = [obj.name for obj in bpy.data.objects if
                         not obj.parent_bone is None and
                         obj.type == 'MESH']

        meshes = [item.name for item in geometry_names if hide_geometry == 'collision' and item.RobotEditor.tag == 'COLLISION' if hide_geometry == 'visual' and item.RobotEditor.tag == 'DEFAULT']

        if hide_geometry == 'all':
            meshes = geometry_names

        ratio_act = bpy.data.objects[global_properties.mesh_name.get(context.scene)].modifiers["Decimate"].ratio
        for selected_mesh in meshes:
                obj = bpy.data.objects[selected_mesh]
                try:
                    obj.modifiers["Decimate"].ratio = ratio_act
                except KeyError:
                    obj.modifiers.new("Decimate", 'DECIMATE').ratio = ratio_act

        return {'FINISHED'}