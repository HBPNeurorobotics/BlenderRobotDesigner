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
#   2015-01-16: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######

# System imports
import logging

# Blender imports
import bpy
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, CollectionProperty

# RobotDesigner imports
from ..core import PluginManager
from ..core.logfile import operator_logger, LogFunction
from ..operators.segments import SelectSegment, UpdateSegments
from ..core.property import PropertyGroupHandlerBase, PropertyHandler


class RDGlobals(PropertyGroupHandlerBase):
    """
    Property group that contains all globally defined parameters mostly related to the state of the GUI
    """

    @staticmethod
    def debug_level_callback(self, context):
        operator_logger.info('Switching debug level')
        level = global_properties.operator_debug_level.get(context.scene)
        if level == 'debug':
            operator_logger.setLevel(logging.DEBUG)
        elif level == 'info':
            operator_logger.setLevel(logging.INFO)
        elif level == 'warning':
            operator_logger.setLevel(logging.WARNING)
        else:
            operator_logger.setLevel(logging.ERROR)

    @staticmethod
    def updateGlobals(self, context):
        model_name = context.active_object.name
        segment_name = context.active_bone.name

        UpdateSegments.run(model_name=model_name, segment_name=segment_name)


    @staticmethod
    def updateBoneName(self, context):

        SelectSegment.run(segment_name=global_properties.segment_name.get(context.scene))

    @staticmethod
    def update_geometry_name(self, context):
        print("Udpate Mesh name")
        for i in [i for i in bpy.context.selected_objects if i.name != context.active_object.name]:
            i.select = False
        try:
            bpy.data.objects[global_properties.mesh_name.get(context.scene)].select = True
        except KeyError:
            pass  # This happens when the search title is selected

    @staticmethod
    def displayMeshes(self, context):
        """
        Hides/Shows mesh objects in dependence of the respective Global property
        """

        hide_mesh = global_properties.display_mesh_selection.get(context.scene)
        meshNames = [obj.name for obj in bpy.data.objects if
                     not obj.parent_bone is None and
                     obj.type == 'MESH']
        for mesh in meshNames:
            obj = bpy.data.objects[mesh]
            if hide_mesh == 'all':
                obj.hide = False
            elif hide_mesh == 'collision' and obj.RobotEditor.tag == 'COLLISION':
                obj.hide = False
            elif hide_mesh == 'visual' and obj.RobotEditor.tag == 'DEFAULT':
                obj.hide = False
            else:
                obj.hide = True

    def __init__(self):

        # Holds the current selected kinematics model (armature) name
        self.model_name = PropertyHandler(StringProperty())

        # Holds the name of the currently selected segment (Bone)
        self.segment_name = PropertyHandler(StringProperty(update=self.updateBoneName))

        # Holds the name of the currently selected geometry (Mesh object)
        self.mesh_name = PropertyHandler(StringProperty(update=self.update_geometry_name))

        # Holds the name of the currently selected physics frame (Empty object)
        self.physics_frame_name = PropertyHandler(StringProperty())

        # Used to realize the main tab in the GUI
        self.gui_tab = PropertyHandler(EnumProperty(
            items=[('armatures', 'Robot', 'Modify the Robot'),
                   ('bones', 'Segments', 'Modify segements'),
                   ('meshes', 'Geometries', 'Assign meshes to segments'),
                   ('sensors', 'Sensors', 'Assign sensors to segments'),
                   # ('markers', 'Markers', 'Assign markers to bones'),
                   # ('controller', 'Controller', 'Modify controller parameter'),
                   ('tools', 'Tools', 'Tools'),
                   ('files', 'Files', 'Export Armature')],
        ))

        # Holds the selection to operate on colission geometries OR visual geometries
        self.mesh_type = PropertyHandler(EnumProperty(
            items=[('DEFAULT', 'Visual', 'Set visual meshes'),
                   ('COLLISION', 'Collision', 'Set collision meshes')]
        ))

        # Holds the selection to list connected or unassigned meshes in dropdown menus
        self.list_meshes = PropertyHandler(EnumProperty(
            items=[("all", 'List all', 'Show all meshes in menu', 'RESTRICT_VIEW_OFF', 1),
                   ("connected", 'List connected', 'Show only connected meshes in menu', 'OUTLINER_OB_ARMATURE', 2),
                   ('disconnected', 'List disconnected', 'Show only disconnected meshes in menu',
                    'ARMATURE_DATA', 3)]))

        # Holds the selection of wheter do hide/display connected/unassigned meshes in the 3D viewport
        self.display_mesh_selection = PropertyHandler(EnumProperty(
            items=[('all', 'Show All connected',
                    'Show all mesh objects in viewport'),
                   ('collision', 'Show collision models',
                    'Show only connected collision models'),
                   ('visual', 'Show visual models',
                    'Show only connected visual models')],
            update=self.displayMeshes))

        # Holds the selection to list connected or unassigned segments in dropdown menus
        self.list_segments = PropertyHandler(EnumProperty(
            items=[("all", 'List all', 'Show all bones in menu', 'RESTRICT_VIEW_OFF', 1),
                   ("connected", 'List connected', 'Show only bones with connected meshes in menu',
                    'OUTLINER_OB_ARMATURE', 2,),
                   ('disconnected', 'List disconnected',
                    'List only bones without connected meshes in menu', 'ARMATURE_DATA', 3)]))

        self.storage_mode = PropertyHandler(EnumProperty(items=[('temporary', 'Non-persistant GIT',
                                                           'Stores/retrieves files from GIT temporary' +
                                                           ' repository'),
                                                                ('git', 'Persitant GIT',
                                                           'Stores/retrieves files from persistent GIT repository'),
                                                                ('local', 'Local',
                                                           'Stores/retrieves from local hard disk')]))
        self.git_url = PropertyHandler(StringProperty(name='GIT URL'))
        self.git_repository = PropertyHandler(StringProperty(name='GIT Repository'))

        self.segment_tab = PropertyHandler(EnumProperty(
            items=[('kinematics', 'Kinematics', 'Edit kinematic properties'),
                   ('dynamics', 'Dynamics', 'Edit Dynamic properties'),
                   ('controller', 'Controller', 'Edit Controller properties')],
            name="asdf"))

        self.bone_length = PropertyHandler(FloatProperty(name="Global bone length", default=1, min=0.001,
                                                         update=self.updateGlobals))
        self.do_kinematic_update = PropertyHandler(BoolProperty(name="Import Update", default=True))

        self.gazebo_tags = PropertyHandler(StringProperty(name="Gazebo tags", default=""))

        self.operator_debug_level = PropertyHandler(EnumProperty(
            items=[('debug', 'Debug', 'Log everything including debug messages (verbose)'),
                   ('info', 'Info', 'Log information'),
                   ('warning', 'Warning', 'Log only warnings'),
                   ('error', 'Error', 'Log only errors')], update=self.debug_level_callback))


global_properties = RDGlobals()
global_properties.register(bpy.types.Scene)
