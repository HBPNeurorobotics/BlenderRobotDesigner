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
#   2017        Benedikt Feldotto (TUM), Muscle Support
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

from ..operators import segments, model, rigid_bodies, dynamics, sensors, muscles

from ..core import PluginManager
from ..core.config import OPERATOR_PREFIX
from ..core.operators import RDOperator
from ..core.logfile import gui_logger
from ..properties.globals import global_properties
from ..core.constants import StringConstants

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
        mesh_type = global_properties.mesh_type.get(context.scene)
        hide_bone = global_properties.display_mesh_selection.get(context.scene)
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


# dynamic menu to select bone for muscle coordinate frame
@PluginManager.register_class
class SegmentsMusclesMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting robot segments to be assigned to muscle pathpoint.
    """
    bl_idname = OPERATOR_PREFIX + "bonemuscleenu"
    bl_label = "Select Muscle"
    filter = None

    @RDOperator.OperatorLogger
    def draw(self, context):
        mesh_type = global_properties.mesh_type.get(context.scene)
        hide_bone = global_properties.display_mesh_selection.get(context.scene)
        layout = self.layout

        current_model = context.active_object
        segment_names = [bone.name for bone in current_model.data.bones]

    #    for bone in sorted(segment_names, key=str.lower):
    #        x = muscles.SelectSegmentMuscle
    #        x.segment_name = bone
    #        layout.operator(x.bl_idname, text=bone).segment_name = bone

        for root in [bone.name for bone in current_model.data.bones if bone.parent is None]:
            layout.operator(muscles.SelectSegmentMuscle.bl_idname, text=root).segment_name = root

            def recursion(children, level=0):

                for bone in sorted([bone.name for bone in children], key=str.lower):
                    text = '    ' * level + '\__ ' + bone
                    layout.operator(muscles.SelectSegmentMuscle.bl_idname, text=text).segment_name = bone
                    recursion(current_model.data.bones[bone].children, level + 1)

            recursion(current_model.data.bones[root].children)


class ConnectedObjectsMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting sensors while displaying connections to robot segments in the scene.
    """
    bl_idname = "Override"

    obj_tag = None # can be set to scene property
    show_connected = None # set to scene property
    blender_type = "CAMERA"
    quick_search = None
    operator_property = "geometry_name"
    operator = rigid_bodies.SelectGeometry
    text = "Select Mesh"

    @RDOperator.OperatorLogger
    def draw(self, context):
        obj_tag = self.obj_tag.get(context.scene)
        obj_hidden = self.show_connected.get(context.scene)
        layout = self.layout
        type = global_properties.display_mesh_selection.get(context.scene)
        if type == 'all':
            obj_names = [obj.name for obj in bpy.data.objects if
                         obj.type == self.blender_type and
                         not obj.hide]
        elif type == 'collision':
            obj_names = [obj.name for obj in bpy.data.objects if
                         obj.type == self.blender_type and
                         obj.RobotEditor.tag == 'COLLISION' and
                         not obj.hide]
        elif type == 'visual':
            obj_names = [obj.name for obj in bpy.data.objects if
                         obj.type == self.blender_type and
                         obj.RobotEditor.tag == 'DEFAULT' and
                         not obj.hide]
        elif type == 'none':
            obj_names = []

        self.logger.debug(obj_names)

        for obj in obj_names:
            if bpy.data.objects[obj].parent_bone:
                text = obj + " --> " + bpy.data.objects[obj].parent_bone
                if obj_hidden == 'disconnected':
                    continue
            else:
                text = obj
                if obj_hidden == 'connected':
                    continue
            setattr(layout.operator(self.operator.bl_idname, text=text),self.operator_property, obj)

    @classmethod
    def putMenu(cls,layout, context, text=None, **kwargs):

        hide_obj = cls.show_connected.get(context.scene)

        # Get selected meshes
        selected = [i for i in bpy.context.selected_objects if i.type == cls.blender_type]

        text = cls.text

        if len(selected) == 1:
            object = selected[0]
            if object.parent_bone and not hide_obj == 'disconnected':
                text = object.name + " --> " + object.parent_bone
            elif not object.parent_bone and not hide_obj == 'connected':
                text = object.name

        layout.menu(cls.bl_idname, text=text)
        row = layout.row(align=True)
        cls.show_connected.prop(context.scene, row,  expand=True, icon_only=True)
        row.separator()

        cls.quick_search.prop_search(bpy.context.scene, row,
                                     bpy.data,'objects', icon='VIEWZOOM', text='')
        #row.prop_search(bpy.context.scene.RobotEditor, cls.quick_search, bpy.data, 'objects',
        #                icon='VIEWZOOM', text='')

@PluginManager.register_class
class GeometriesMenu(ConnectedObjectsMenu):
    """
    :ref:`menu` for selecting geometries while displaying connections to robot segments in the scene.
    """
    bl_idname = OPERATOR_PREFIX + "meshmenu"
    bl_label = "Select Geometry"

    obj_tag = global_properties.mesh_type
    show_connected = global_properties.list_meshes # set to scene property
    blender_type = StringConstants.mesh
    quick_search = global_properties.mesh_name
    operator_property = "geometry_name"
    operator = rigid_bodies.SelectGeometry

@PluginManager.register_class
class CameraSensorMenu(ConnectedObjectsMenu):
    """
    :ref:`menu` for selecting geometries while displaying connections to robot segments in the scene.
    """
    bl_idname = OPERATOR_PREFIX + "camera_sensor_menu"
    bl_label = "Select Camera Sensor"

    obj_tag = global_properties.sensor_type # can be set to scene property
    show_connected = global_properties.list_meshes # set to scene property
    blender_type = StringConstants.camera
    quick_search = global_properties.mesh_name
    operator_property = "object_name"
    operator = sensors.SelectSensor
    text = "Select sensor"

@PluginManager.register_class
class MassObjectMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting :term:`mass entities` while displaying connections to robot segments in the scene.
    """
    bl_idname = OPERATOR_PREFIX + "mass_object_menu"
    bl_label = "Select mass object"

    obj_tag = global_properties.physics_type
    show_connected = global_properties.list_meshes
    blender_type = StringConstants.empty
    #quick_search = None #global_properties.physics_frame_name
    operator_property = "frameName"
    operator = dynamics.SelectPhysical
    text = "Select mass object"


    @staticmethod
    def fmt_obj(obj):
        if obj.parent_bone:
            text = obj.name + " --> " + obj.parent_bone
        else:
            text = obj.name
        return text


    @staticmethod
    def may_show( obj, obj_hidden):
        connected = (obj.parent_bone or obj_hidden != 'disconnected') and \
                    (not obj.parent_bone or obj_hidden != 'connected')
        return connected and obj.type == MassObjectMenu.blender_type and not obj.hide and obj.RobotEditor.tag == 'PHYSICS_FRAME'


    @RDOperator.OperatorLogger
    def draw(self, context):
        hide_obj = self.show_connected.get(context.scene)

        layout = self.layout
        current_model = context.active_object

        objs = [obj for obj in context.scene.objects if self.may_show(obj, hide_obj)]

        for obj in objs:
            text = self.fmt_obj(obj)
            setattr(layout.operator(self.operator.bl_idname, text=text),self.operator_property, obj.name)


    @classmethod
    def putMenu(cls,layout, context, text=None, **kwargs):
        hide_obj = cls.show_connected.get(context.scene)

        # Get selected meshes
        current_model = context.active_object
        selected = [obj for obj in context.scene.objects if cls.may_show(obj, hide_obj) and obj.select]

        text = cls.text
        if len(selected) == 1:
            object = selected[0]
            text = cls.fmt_obj(object)

        layout.menu(cls.bl_idname, text=text)
        row = layout.row(align=True)
        cls.show_connected.prop(context.scene, row,  expand=True, icon_only=True)
        row.separator()

        #cls.quick_search.prop_search(bpy.context.scene, row,
        #                             bpy.data,'objects', icon='VIEWZOOM', text='')



@PluginManager.register_class
class ModelMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` for selecting robot models or optionally create new ones.
    """

    bl_idname = OPERATOR_PREFIX + "armaturemenu"
    bl_label = "Selecht Model"

    @RDOperator.OperatorLogger
    def draw(self, context):
        layout = self.layout
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']

        layout.operator(model.CreateNewModel.bl_idname, text="New...")

        for arm in armatures:
            text = arm.name
            model.SelectModel.place_button(layout, text=text).model_name = text



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
            model.SelectCoordinateFrame.place_button(layout, text=mesh).mesh_name = mesh


@PluginManager.register_class
class MuscleMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` to select alternative display for the coordinate frames.
    """
    bl_idname = OPERATOR_PREFIX + "musclemenu"
    bl_label = "Select Muscle"
    axis = IntProperty(default=0)

    @RDOperator.OperatorLogger
    def draw(self, context):
        layout = self.layout

        active_model = global_properties.model_name.get(context.scene)
        hide_muscle = global_properties.display_muscle_selection.get(context.scene)

        for muscle in [obj.name for obj in bpy.data.objects
                       if bpy.data.objects[obj.name].RobotEditor.muscles.robotName == active_model
                        and hide_muscle == 'all'
                        or hide_muscle.lower() == bpy.data.objects[obj.name].RobotEditor.muscles.robotName.lower()]:
             muscles.SelectMuscle.place_button(layout, text=muscle).muscle_name = muscle


@PluginManager.register_class
class MusclePointsMenu(bpy.types.Menu, BaseMenu):
    """
    :ref:`menu` to select alternative display for the coordinate frames.
    """
    bl_idname = OPERATOR_PREFIX + "musclepointsmenu"
    bl_label = "Select Muscle Pathpoint"
    axis = IntProperty(default=0)

    @RDOperator.OperatorLogger
    def draw(self, context):
        layout = self.layout
        muscle_pathpoints = [obj.name for obj in bpy.data.objects[global_properties.model_name.get(bpy.context.scene)].RobotEditor.muscles[global_properties.active_muscle.get(bpy.context.scene)].pathPoints]
                ## if muscle type to show!

        for muscle_pathpoint in muscle_pathpoints:
            muscles.SelectMusclePathPoint.place_button(layout, text=muscle_pathpoint).muscle_pathpoint_name = muscle_pathpoint


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


# # dynamic menu to select physics frame
# @PluginManager.register_class
# class MassObjectMenu(bpy.types.Menu, BaseMenu):
#     """
#     :ref:`menu` for selecting physical instances.
#     """
#     bl_idname = OPERATOR_PREFIX + "physicsframemenu"
#     bl_label = "SelectPhysics Frame"
#
#     @RDOperator.OperatorLogger
#     def draw(self, context):
#         layout = self.layout
#         mass_object_names = [f.name for f in bpy.data.objects if f.RobotEditor.tag == 'PHYSICS_FRAME']
#
#         for frame in sorted(mass_object_names, key=str.lower):
#             if bpy.data.objects[frame].parent_bone:
#                 text = frame + " --> " + bpy.data.objects[frame].parent_bone
#             else:
#                 text = frame
#
#             layout.operator(dynamics.SelectPhysical.bl_idname, text=text).frameName = frame
