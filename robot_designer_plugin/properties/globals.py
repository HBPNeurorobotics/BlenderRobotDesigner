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
from ..operators.muscles import SelectMuscle
from ..core.property import PropertyGroupHandlerBase, PropertyHandler

class RDSelectedObjects(PropertyGroupHandlerBase):

    def __init__(self):

        self.visible = PropertyHandler()

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
    def display_physics(self, context):
        for physics in [physics for physics in bpy.data.objects if physics.RobotEditor.tag == 'PHYSICS_FRAME']:
            if self.display_physics_selection == True:
                physics.hide = False
            else:
                physics.hide = True

    @staticmethod
    def updateMuscleName(self, context):

        SelectMuscle.run(muscle_name=global_properties.active_muscle.get(context.scene))

    @staticmethod
    def update_geometry_name(self, context):
        print("Update Mesh name")
        for i in [i for i in bpy.context.selected_objects if i.name != context.active_object.name]:
            i.select = False
        try:
            bpy.data.objects[global_properties.mesh_name.get(context.scene)].select = True
        except KeyError:
            print ("Selecting ", global_properties.mesh_name.get(context.scene), " failed due to key error!")
            pass  # This happens when the search title is selected

    @staticmethod
    def display_geometries(self, context):
        """
        Hides/Shows mesh objects in dependence of the respective Global property
        """

        hide_geometry = global_properties.display_mesh_selection.get(context.scene)
        geometry_name = [obj.name for obj in bpy.data.objects if
                     not obj.parent_bone is None and
                     obj.type == 'MESH']

        for mesh in geometry_name:
            obj = bpy.data.objects[mesh]
            if hide_geometry == 'all':
                obj.hide = False
            elif hide_geometry== 'collision' and obj.RobotEditor.tag == 'COLLISION':
                obj.hide = False
            elif hide_geometry == 'visual' and obj.RobotEditor.tag == 'DEFAULT':
                obj.hide = False
            elif hide_geometry == 'none':
                obj.hide = True
            else:
                obj.hide = True


    @staticmethod
    def display_muscles(self, context):
        """
        Hides/Shows muscles in dependence of the respective Global property
        """

        hide_muscles = global_properties.display_muscle_selection.get(context.scene)


        muscle_names = [obj.name for obj in bpy.data.objects if
         bpy.data.objects[obj.name].RobotEditor.muscles.robotName != '']

        for muscle in muscle_names:
            obj = bpy.data.objects[muscle]
            if hide_muscles == 'all':
                obj.hide = False
           # elif hide_muscles == 'MYOROBOTICS' and obj.RobotEditor.muscles.muscleType == 'MYOROBOTICS':
           #     obj.hide = False
            elif hide_muscles == 'MILLARD_EQUIL' and obj.RobotEditor.muscles.muscleType == 'MILLARD_EQUIL':
                obj.hide = False
            elif hide_muscles == 'MILLARD_ACCEL' and obj.RobotEditor.muscles.muscleType == 'MILLARD_ACCEL':
                obj.hide = False
            elif hide_muscles == 'THELEN' and obj.RobotEditor.muscles.muscleType == 'THELEN':
                obj.hide = False
            elif hide_muscles == 'RIGID_TENDON' and obj.RobotEditor.muscles.muscleType == 'RIGID_TENDON':
                obj.hide = False
            elif hide_muscles == 'none':
                obj.hide = True
            else:
                obj.hide = True

    @staticmethod
    def name_update(self, context):
        """
        updates the robot name for every assigned muscle
        """
        if self.old_name != '':
            muscles = [obj for obj in bpy.data.objects if obj.RobotEditor.muscles.robotName == self.old_name]

            for muscle in muscles:
                muscle.RobotEditor.muscles.robotName = self.model_name

            self.old_name = self.model_name

        bpy.context.active_object.name = self.model_name

    @staticmethod
    def muscle_dim_update(self, context):
        """
        updates the visualization dimension of all muscles in scene
        """
        print("in the function")
        active_model = self.model_name
        for muscle in [obj.name for obj in bpy.data.objects
            if bpy.data.objects[obj.name].RobotEditor.muscles.robotName == active_model]:
                bpy.data.objects[muscle].data.bevel_depth = self.muscle_dim
                print("changeing ----")






    def __init__(self):

        # Holds the current selected kinematics model (armature) name
        self.model_name = PropertyHandler(StringProperty(name='Name', update=self.name_update))
        self.old_name = PropertyHandler(StringProperty(name='Name'))

        # Holds the name of the currently selected segment (Bone)
        self.segment_name = PropertyHandler(StringProperty(update=self.updateBoneName))

        # Holds the name of the currently selected geometry (Mesh object)
        self.mesh_name = PropertyHandler(StringProperty(update=self.update_geometry_name))

        # Holds the name of the currently selected physics frame (Empty object)
        self.camera_sensor_name = PropertyHandler(StringProperty())

        # Used to realize the main tab in the GUI
        self.gui_tab = PropertyHandler(EnumProperty(
            items=[('armatures', 'Robot', 'Modify the Robot'),
                   ('bones', 'Segments', 'Modify segements'),
                   ('meshes', 'Geometries', 'Assign meshes to segments'),
                   ('sensors', 'Sensors', 'Assign sensors to the robot'),
                   ('muscles', 'Muscles', 'Assign muscles to the robot'),
                   # ('markers', 'Markers', 'Assign markers to bones'),
                   # ('controller', 'Controller', 'Modify controller parameter'),
                   ('tools', 'Tools', 'Tools'),
                   ('files', 'Files', 'Export Armature')],
        ))

        # Holds the selection to operate on colission geometries OR visual geometries
        self.mesh_type = PropertyHandler(EnumProperty(
            items=[('DEFAULT', 'Visual geometries', 'Edit visual geometries'),
                   ('COLLISION', 'Collision geometries', 'Edit collision geometries')]
        ))

        self.sensor_type = PropertyHandler(EnumProperty(
            items=[('CAMERA_SENSOR','Camera', 'Edit camera sensors'),
                   ('LASER_SENSOR', 'Laser', 'Edit laser scanners'),
                   ('CONTACT_SENSOR', 'Contact', 'Edit contact sensors'),
                   ('FORCE_TORQUE_SENSOR', 'Force Torque', 'Edit force torque sensors'),
                   ('DEPTH_CAMERA_SENSOR', 'Depth Camera', 'Edit depth camera sensors'),
                   ('ALTIMETER_SENSOR', 'Altimeter', 'Edit altimeter sensors'),
                   ('IMU_SENSOR', 'IMU', 'Edit IMU sensors')]
                    # ('POSITION', 'Position sensors', 'Edit position sensors')]
        ))

        self.active_sensor = PropertyHandler(StringProperty(name="Active sensor", default=""))

        self.physics_type = PropertyHandler(EnumProperty(items=[('PHYSICS_FRAME', 'Mass object', 'Mass object')]))

        self.display_physics_selection = PropertyHandler(BoolProperty(name="Show Physics Frames", description="Show or hide physics frames", default=True, update=self.display_physics))


        # Holds the selection to list connected or unassigned meshes in dropdown menus
        self.list_meshes = PropertyHandler(EnumProperty(
            items=[("all", 'List all', 'Show all meshes in menu', 'RESTRICT_VIEW_OFF', 1),
                   ("connected", 'List connected', 'Show only connected meshes in menu', 'OUTLINER_OB_ARMATURE', 2),
                   ('disconnected', 'List disconnected', 'Show only disconnected meshes in menu',
                    'ARMATURE_DATA', 3)]))

        self.assign_collision = PropertyHandler(BoolProperty(name="Assign as Collision Mesh", description="Adds a collision tag to the mesh", default=False))

        # Holds the selection of wheter do hide/display connected/unassigned meshes in the 3D viewport
        self.display_mesh_selection = PropertyHandler(EnumProperty(
            items=[('all', 'All',
                    'Show all objects in viewport'),
                   ('collision', 'Collision',
                    'Show only connected collision models'),
                   ('visual', 'Visual',
                    'Show only connected visual models'),
                   ('none', "None", "Show no connected model")],
            update=self.display_geometries))

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

        self.active_muscle = PropertyHandler(StringProperty(name="Active Muscle", default=""))

        self.display_muscle_selection = PropertyHandler(EnumProperty(
            items=[('all', 'All', 'Show all muscles'),
            #       ('MYOROBOTICS', 'Myorobotics', 'Show only Myorobotics Muscles'),
                   ('MILLARD_EQUIL', 'Millard Equilibrium 2012', 'Show only Millard Equilibrium 2012 Muscles'),
                   ('MILLARD_ACCEL', 'Millard Acceleration 2012', 'Show only Millard Acceleration 2012 Muscles'),
                   ('THELEN', 'Thelen 2003', 'Show only Thelen 2003 Muscles'),
                   ('RIGID_TENDON', 'Rigid Tendon', 'Show only Rigid Tendon Muscles'),
                   ('none', "None", "Show no muscles")],
            update=self.display_muscles))

        self.muscle_dim = PropertyHandler(FloatProperty(name="Muscle Dimension:", default=0.05, update=self.muscle_dim_update))



global_properties = RDGlobals()
global_properties.register(bpy.types.Scene)
