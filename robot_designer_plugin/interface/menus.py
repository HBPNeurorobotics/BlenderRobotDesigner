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
#   2015:       Stefan Ulbrich (FZI), Gui redesigned
#   2015-01-16: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
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
from bpy.props import IntProperty, StringProperty, CollectionProperty

# ######
# RobotDesigner imports

from ..operators import segments, model, rigid_bodies, dynamics

from ..core import PluginManager
from ..core.config import OPERATOR_PREFIX
from ..core.operators import RDOperator
from ..core.logfile import gui_logger

class BaseMenu(object):

    logger = gui_logger

    @classmethod
    def putMenu(cls,layout,context, text="", **kwargs): # todo which kwargs are possible
        layout.menu(cls.bl_idname, text=text)

# dynamic menu to select mesh
@PluginManager.register_class
class SegmentsGeometriesMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting robot segments while displaying connections to geometries in the scene.
    """
    bl_idname = OPERATOR_PREFIX + "bonemeshmenu"
    bl_label = "Select Bone"
    filter = None

    @RDOperator.OperatorLogger
    def draw(self, context):
        mesh_type = context.scene.RobotEditor.meshType
        hide_bone = context.scene.RobotEditor.listBones
        layout = self.layout

        current_model = context.active_object
        segment_names = [bone.name for bone in current_model.data.bones]
        meshes = {obj.parent_bone: obj.name for obj in bpy.data.objects if
                  obj.parent_bone is not None and
                  obj.type == 'MESH' and
                  obj.RobotEditor.tag == mesh_type}

        for bone in sorted(segment_names, key=str.lower):
            if bone in meshes:
                text = bone + " <-- " + meshes[bone]
                if hide_bone == 'disconnected':
                    continue
            # elif bpy.data.objects[mesh].parent:
            #    text = context.scene.RobotEditor.meshName + " --> " + bpy.data.objects[mesh].parent.name
            #    text = mesh + " --> " + bpy.data.objects[mesh].parent.name
            else:
                text = bone
                if hide_bone == 'connected':
                    continue
            layout.operator(segments.SelectSegment.bl_idname, text=text).segment_name = bone


# dynamic menu to select mesh
@PluginManager.register_class
class GeometriesMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting geometries while displaying connections to robot segments in the scene.
    """
    bl_idname = OPERATOR_PREFIX + "meshmenu"
    bl_label = "Select Geometry"

    @RDOperator.OperatorLogger
    def draw(self, context):
        mesh_type = context.scene.RobotEditor.meshType
        hide_mesh = context.scene.RobotEditor.listMeshes
        layout = self.layout
        geometry_names = [obj.name for obj in bpy.data.objects if
                          obj.type == 'MESH' and
                          obj.RobotEditor.tag == mesh_type and not obj.hide]
        self.logger.debug(geometry_names)

        for mesh in geometry_names:
            if bpy.data.objects[mesh].parent_bone:
                text = mesh + " --> " + bpy.data.objects[mesh].parent_bone
                if hide_mesh == 'disconnected':
                    continue
            # elif bpy.data.objects[mesh].parent:
            #    text = context.scene.RobotEditor.meshName + " --> " + bpy.data.objects[mesh].parent.name
            #    text = mesh + " --> " + bpy.data.objects[mesh].parent.name
            else:
                text = mesh
                if hide_mesh == 'connected':
                    continue
            layout.operator(rigid_bodies.SelectGeometry.bl_idname, text=text).mesh_name = mesh

    @classmethod
    def putMenu(cls,layout, context, text=None, **kwargs):

        text = "Select Mesh"
        hide_mesh = bpy.context.scene.RobotEditor.listMeshes

        # Get selected meshes
        selected = [i for i in bpy.context.selected_objects if i.type == 'MESH']

        if len(selected) == 1:
            # if context.scene.RobotEditor.meshName in bpy.data.objects:
            #    if context.active_bone and not context.scene.RobotEditor.meshName == "":
            mesh = selected[0]
            if mesh.parent_bone and not hide_mesh == 'disconnected':
                text = mesh.name + " --> " + mesh.parent_bone
            elif not mesh.parent_bone and not hide_mesh == 'connected':
                text = mesh.name
            else:
                text = 'Select Mesh'

        layout.menu(cls.bl_idname, text=text)
        row = layout.row(align=True)
        row.prop(bpy.context.scene.RobotEditor, "listMeshes", expand=True, icon_only=True)
        row.separator()

        # bpy.context.scene.RobotEditor.meshes.add().name = "test"
        # for obj in bpy.data.objects:
        #     if obj.type=="MESH":
        #         if obj.name not in bpy.context.scene.RobotEditor.meshes:
        #             bpy.context.scene.RobotEditor.meshes.add().name = obj.name
        # for name in bpy.context.scene.RobotEditor.meshes:
        #     if name not in [i.name for i in bpy.data.objects if i.type=='MESH']:
        #         bpy.context.scene.RobotEditor.meshes.remove(bpy.context.scene.RobotEditor.meshes.find(name))

        # row.prop_search(bpy.context.scene.RobotEditor, "meshName", bpy.context.scene.RobotEditor, 'meshes',
        #                 icon='VIEWZOOM', text='')
        row.prop_search(bpy.context.scene.RobotEditor, "meshName", bpy.data, 'objects',
                         icon='VIEWZOOM', text='')

# menu to select exisiting armature or create new one
@PluginManager.register_class
class ModelMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting robot models or optionally create new ones.
    """

    bl_idname = OPERATOR_PREFIX + "armaturemenu"
    bl_label = "Selecht Armature"

    @RDOperator.OperatorLogger
    def draw(self, context):
        layout = self.layout
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']

        layout.operator(model.CreateNewModel.bl_idname, text="New...")

        for arm in armatures:
            text = arm.name
            #layout.operator(model.SelectModel.bl_idname, text=text).armatureName = text
            model.SelectModel.place_button(layout, text=text).model_name = text



# dynamic menu for joining two armatures
@PluginManager.register_class
class JoinModelMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for joining two robot models.
    """
    bl_idname = OPERATOR_PREFIX + "joinarmaturemenu"
    bl_label = "Join selected armature with different armature"

    @RDOperator.OperatorLogger
    def draw(self, context):
        layout = self.layout

        current_model_name = context.active_object.data.name
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE' and not obj.name == current_model_name]

        for arm in armatures:
            text = arm.name
            layout.operator(model.JoinModels.bl_idname, text=text).targetArmatureName = text


@PluginManager.register_class
class CoordinateFrameMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` to select alternative display for the coordinate frames.
    """
    bl_idname = OPERATOR_PREFIX + "cfmenu"
    bl_label = "Select Mesh"

    axis = IntProperty(default=0)

    @RDOperator.OperatorLogger
    def draw(self, context):
        layout = self.layout
        geometry_names = [obj.name for obj in bpy.data.objects if
                          obj.type in ('MESH', 'EMPTY') and
                          obj.parent is None and
                          obj.parent_bone == '']

        for mesh in geometry_names:
            model.SelectCoordinateFrame.place_button(layout,text=mesh).mesh_name = mesh


# Dynamic menu to select bone
@PluginManager.register_class
class SegmentsMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting robot segments.
    """
    bl_idname = OPERATOR_PREFIX + "bonemenu"
    bl_label = "Select Segment"

    @RDOperator.OperatorLogger
    def draw(self, context):
        current_model = context.active_object

        layout = self.layout

        for root in [bone.name for bone in current_model.data.bones if bone.parent is None]:
            layout.operator(segments.SelectSegment.bl_idname, text=root).segment_name = root

            def recursion(children, level=0):

                for bone in sorted([bone.name for bone in children], key=str.lower):

                    text = '    ' * level + '\__ ' + bone
                    layout.operator(segments.SelectSegment.bl_idname, text=text).segment_name = bone
                    recursion(current_model.data.bones[bone].children, level + 1)

            recursion(current_model.data.bones[root].children)

            # for bone in sorted(boneNames, key=str.lower):
            #     text = bone
            #     layout.operator(SelectSegment.bl_idname, text=text).segment_name = text


# dynmic menu for assigning parent bones
@PluginManager.register_class
class AssignParentMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for re-assigning the parent of a robot segments.
    """
    bl_idname = OPERATOR_PREFIX + "assignparentbonemenu"
    bl_label = "Assign parent to bone"

    @RDOperator.OperatorLogger
    def draw(self, context):
        arm = context.active_object
        current_segment = context.active_bone

        # can't parent to self or own children
        disallowed_segments = current_segment.children_recursive
        disallowed_segments.append(current_segment)
        segment_names = [bone.name for bone in arm.data.bones if bone not in disallowed_segments]

        layout = self.layout

        layout.operator(segments.InsertNewParentSegment.bl_idname, text="New...")

        for bone in sorted(segment_names, key=str.lower):
            text = bone
            if current_segment.parent and bone == current_segment.parent.name:
                text += " <-- Parent"
            layout.operator(segments.AssignParentSegment.bl_idname, text=text).parent_name = bone


# dynamic menu to select physics frame
@PluginManager.register_class
class MassObjectMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting physical instances.
    """
    bl_idname = OPERATOR_PREFIX + "physicsframemenu"
    bl_label = "SelectPhysics Frame"

    @RDOperator.OperatorLogger
    def draw(self, context):
        layout = self.layout
        mass_object_names = [f.name for f in bpy.data.objects if f.RobotEditor.tag == 'PHYSICS_FRAME']

        for frame in sorted(mass_object_names, key=str.lower):
            if bpy.data.objects[frame].parent_bone:
                text = frame + " --> " + bpy.data.objects[frame].parent_bone
            else:
                text = frame

            layout.operator(dynamics.SelectPhysical.bl_idname, text=text).frameName = frame
