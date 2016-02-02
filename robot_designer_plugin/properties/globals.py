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


@PluginManager.register_class
class StringCollection(bpy.types.PropertyGroup):
    name = StringProperty()


@PluginManager.register_class
class RDGlobals(bpy.types.PropertyGroup):
    '''
    Property group that contains all globally defined parameters mostly related to the state of the GUI
    '''

    def updateGlobals(self, context):
        model_name = context.active_object.name
        segment_name = context.active_bone.name

        UpdateSegments.run(model_name=model_name, segment_name= segment_name)


    def displayMeshes(self, context):
        """
        Hides/Shows mesh objects in dependence of the respective Global property
        """

        hide_mesh = context.scene.RobotEditor.hideMeshType
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

    armatureName = StringProperty(name="armatureName")


    @LogFunction
    def updateBoneName(self, context):
        SelectSegment.run(segment_name=context.scene.RobotEditor.segment_name)


    segment_name = StringProperty(name="boneName", update=updateBoneName)


    @LogFunction
    def updateMeshName(self, context):
        #SelectGeometry.run(meshName=context.scene.RobotEditor.meshName)
        for i in [i for i in bpy.context.selected_objects if i.name != context.active_object.name]:
            i.select=False
        try:
            bpy.data.objects[context.scene.RobotEditor.meshName].select = True
        except KeyError:
            pass # This happens when the search title is selected


    meshName = StringProperty(name="meshName", update=updateMeshName)

    markerName = StringProperty(name="markerName")
    physicsFrameName = StringProperty(name="physicsFrameName")
    controlEnum = EnumProperty(
            items=[('armatures', 'Robot', 'Modify the Robot'),
                   ('bones', 'Segments', 'Modify segements'),
                   ('meshes', 'Geometries', 'Assign meshes to segments'),
                   # ('markers', 'Markers', 'Assign markers to bones'),
                   # ('controller', 'Controller', 'Modify controller parameter'),
                   ('tools', 'Tools', 'Tools'),
                   ('files', 'Files', 'Export Armature')],
            name="RobotEditor Control Panel"
    )
    meshType = EnumProperty(
            items=[('DEFAULT', 'Visual', 'Set visual meshes'),
                   ('COLLISION', 'Collision', 'Set collision meshes')]
    )
    listMeshes = EnumProperty(
            items=[("all", 'List all', 'Show all meshes in menu','RESTRICT_VIEW_OFF',1),
                   ("connected", 'List connected', 'Show only connected meshes in menu','OUTLINER_OB_ARMATURE',2),
                   ('disconnected', 'List disconnected', 'Show only disconnected meshes in menu',
                    'ARMATURE_DATA',3)])

    hideMeshType = EnumProperty(
            items=[('all', 'Show All connected',
                    'Show all mesh objects in viewport'),
                   ('collision', 'Show collision models',
                    'Show only connected collision models'),
                   ('visual', 'Show visual models',
                    'Show only connected visual models')],
            update=displayMeshes)

    listBones = EnumProperty(
            items=[("all", 'List all', 'Show all bones in menu','RESTRICT_VIEW_OFF',1),
                   ("connected", 'List connected','Show only bones with connected meshes in menu',
                    'OUTLINER_OB_ARMATURE',2,),
                   ('disconnected', 'List disconnected',
                    'List only bones without connected meshes in menu','ARMATURE_DATA',3)])
    storageMode = EnumProperty(items=[('temporary', 'Non-persistant GIT',
                                       'Stores/retrieves files from GIT temporary' +
                                       ' repository'),
                                      ('git', 'Persitant GIT',
                                       'Stores/retrieves files from persistent GIT repository'),
                                      ('local', 'Local',
                                       'Stores/retrieves from local hard disk')])
    gitURL = StringProperty(name='GIT URL')
    gitRepository = StringProperty(name='GIT Repository')
    modelFolderName = StringProperty(name='Model folder')

    boneMode = EnumProperty(
            items=[('kinematics', 'Kinematics', 'Edit kinematic properties'),
                   ('dynamics', 'Dynamics', 'Edit Dynamic properties'),
                   ('controller', 'Controller', 'Edit Controller properties')])
    boneLength = FloatProperty(name="Global bone length", default=1, min=0.001,
                               update=updateGlobals)
    doKinematicUpdate = BoolProperty(name="Import Update", default=True)

    meshes = CollectionProperty(type=StringCollection)

    # liveSearchBones = StringProperty(name="Live Search for Bones", default="")
    # liveSearchMeshes = StringProperty(name="Live Search for Meshes",
    #                                   default="")
    # liveSearchMarkers = StringProperty(name="Live Search for Markers",
    #                                    default="")

    # collapsable bone elements
    # collapseBoneEdit = BoolProperty(name="Edit Bones")
    # collapseGlobalSettings = BoolProperty(
    #         name="Robot Designer global settings")
    # collapseController = BoolProperty(name="Collapse controller box")
    # collapseControllerLimits = BoolProperty(
    #         name="Collapse controller limits box")
    # collapseCollision = BoolProperty(name="Collapse collision mesh limits box",
    #                                  default=False)
    # collapseDisconnectMesh = BoolProperty(
    #         name="Collapse collision mesh limits box", default=True)
    # collapseConnectMesh = BoolProperty(
    #         name="Collapse collision mesh limits box", default=True)
    # collapseCFSelection = BoolProperty(
    #         name="Collapse coordinate frame selection box", default=False)
    # collapseSoftBodies = BoolProperty(name="Collapse soft body box", default=False)
    # # gazebo tags
    gazeboTags = StringProperty(name="Gazebo tags", default="")

    def debug_level_callback(self, context):
        operator_logger.info('Switching debug level')
        if context.scene.RobotEditor.OperatorDebugLevel == 'debug':
            operator_logger.setLevel(logging.DEBUG)
        elif context.scene.RobotEditor.OperatorDebugLevel == 'info':
            operator_logger.setLevel(logging.INFO)
        elif context.scene.RobotEditor.OperatorDebugLevel == 'warning':
            operator_logger.setLevel(logging.WARNING)
        else:
            operator_logger.setLevel(logging.ERROR)

    OperatorDebugLevel = EnumProperty(
            items=[('debug', 'Debug', 'Log everything including debug messages (verbose)'),
                   ('info', 'Info', 'Log information'),
                   ('warning', 'Warning', 'Log only warnings'),
                   ('error', 'Error', 'Log only errors')], update=debug_level_callback)