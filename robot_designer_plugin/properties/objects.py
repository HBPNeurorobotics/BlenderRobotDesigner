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
#   2017:       Benedikt Feldotto (TUM), ModelMeta, Muscle Support
#
# ######

# Blender imports
import bpy
from bpy.props import FloatProperty, StringProperty, \
    EnumProperty, FloatVectorProperty, PointerProperty, IntProperty, CollectionProperty

# RobotDesigner imports
from ..core import PluginManager
from ..properties.globals import global_properties


# from .globals import global_properties

@PluginManager.register_property_group()
class RDDynamics(bpy.types.PropertyGroup):
    '''
    Property group that contains dynamics values
    '''
    # from mathutils import Vector
    # def updateCoM(self, context):
    #    frame = bpy.data.objects[bpy.context.scene.RobotEditor.physicsFrameName]
    #    position = Vector((frame.RobotEditor.dynamics.CoM[0],frame.RobotEditor.dynamics.CoM[1],
    # frame.RobotEditor.dynamics.CoM[2]))
    #    frame.location = position

    # CoM = FloatVectorProperty(name = "Center of Mass", update=updateCoM, subtype = 'XYZ')
    mass = FloatProperty(name="Mass (kg)", precision=4, step=0.1, default=1.0)

    # add inertia pose here
    inertiaTrans = FloatVectorProperty(name="Translation", precision=4, step=0.1, default=[0.0, 0.0, 0.0])
    inertiaRot = FloatVectorProperty(name="Rotation", precision=4, step=0.1, default=[0.0, 0.0, 0.0])

    # new inertia tensor
    inertiaXX = FloatProperty(name="", precision=4, step=0.1, default=1.0)
    inertiaXY = FloatProperty(name="", precision=4, step=0.1, default=1.0)
    inertiaXZ = FloatProperty(name="", precision=4, step=0.1, default=1.0)
    inertiaYY = FloatProperty(name="", precision=4, step=0.1, default=1.0)
    inertiaYZ = FloatProperty(name="", precision=4, step=0.1, default=1.0)
    inertiaZZ = FloatProperty(name="", precision=4, step=0.1, default=1.0)



@PluginManager.register_property_group()
class RDCamera(bpy.types.PropertyGroup):
    width = IntProperty(default=320, min=1)
    height = IntProperty(default=240, min=1)
    format = EnumProperty(items=[('L8', 'L8', 'L8'),
                                 ('R8G8B8', 'R8G8B8', 'R8G8B8'),
                                 ('B8G8R8', 'B8G8R8', 'B8G8R8'),
                                 ('BAYER_RGGB8', 'BAYER_RGGB8', 'BAYER_RGGB8'),
                                 ('BAYER_BGGR8', 'BAYER_BGGR8', 'BAYER_BGGR8'),
                                 ('BAYER_GBRG8', 'BAYER_GBRG8', 'BAYER_GBRG8'),
                                 ('BAYER_GRBG8', 'BAYER_GRBG8', 'BAYER_GRBG8')
                                 ])


@PluginManager.register_property_group()
class RDLaser(bpy.types.PropertyGroup):
    horizontal_samples = IntProperty(name="horizontal samples", default=320, min=1)
    vertical_samples = IntProperty(name="vertical samples", default=240, min=1)
    resolution = EnumProperty(items=[('8-Bit', '8-Bit', '8-Bit'),
                                     ('16-Bit', '16-Bit', '16-Bit')
                                     ])

#----------------------


class SceneSettingItem(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(name="Test Prop", default="Unknown")
    value = bpy.props.IntProperty(name="Test Prop", default=22)



def muscle_type_update(self, context):
    active_muscle = global_properties.active_muscle.get(bpy.context.scene)

    if bpy.data.objects[active_muscle].RobotEditor.muscles.muscleType == 'MYOROBOTICS':
        color = (1.0,0.0,0.0)
    elif bpy.data.objects[active_muscle].RobotEditor.muscles.muscleType == 'MILLARD':
        color = (0.0, 1.0, 0.0)
    elif bpy.data.objects[active_muscle].RobotEditor.muscles.muscleType == 'THELEN':
        color = (0.0, 0.0, 1.0)

    bpy.data.objects[active_muscle].data.materials[active_muscle + "_vis"].diffuse_color = color


def muscle_pathpoint_update(self, context):
    #if bpy.data.objects[global_properties.active_muscle.get(self,context)]
    print('pathpoint update')
   # bpy.data.objects['Line'].data.materials['linematerial'].diffuse_color = (1.0, 0.0, 0.0)


#@PluginManager.register_property_group()
class RDMusclePoints(bpy.types.PropertyGroup):
    '''
    Property group that contains muscle attachement points
    '''

    x = FloatProperty(name="X", precision=4, step=0.1, default=1.0, update=muscle_pathpoint_update)
    y = FloatProperty(name="Y", precision=4, step=0.1, default=1.0, update=muscle_pathpoint_update)
    z = FloatProperty(name="Z", precision=4, step=0.1, default=1.0, update=muscle_pathpoint_update)

    coordFrame = StringProperty(name="Coordinate Frame", default="global")


@PluginManager.register_property_group()
class RDMuscle(bpy.types.PropertyGroup):
    '''
    Property group that contains muscle values
    '''

    muscleType = EnumProperty(
        items=[('MYOROBOTICS', 'Myorobotics', 'Myorobotics Muscle'),
               ('MILLARD', 'Millard 2012', 'Millard 2012 Muscle'),
               ('THELEN', 'Thelen 2003', 'Thelen 2003 Muscle')],
        name="Muscle Type:", update=muscle_type_update
    )

    robotName = StringProperty(name="RobotName")

    bpy.utils.register_class(RDMusclePoints)
    pathPoints = CollectionProperty(type=RDMusclePoints)




#-----------------

@PluginManager.register_property_group()
class RDModelMeta(bpy.types.PropertyGroup):
   '''
   Property group that contains model meta data suc as name, version and description
   '''
   model_version = StringProperty(name='Version', default="1.0")
   model_description = StringProperty(name='Description')


@PluginManager.register_property_group()
class RDAuthor(bpy.types.PropertyGroup):
   '''
   Property group that contains author details such as name and email
   '''
   authorName = StringProperty(name="author name")
   authorEmail = StringProperty(name ="author email")


@PluginManager.register_property_group(bpy.types.Object)
class RDObjects(bpy.types.PropertyGroup):
    '''
    Property group that stores general information for individual Blender
    objects with respect to the RobotEditor
    '''
    fileName = StringProperty(name="Mesh File Name")
    tag = EnumProperty(
        items=[('DEFAULT', 'Default', 'Default'),
               ('MARKER', 'Marker', 'Marker'),
               ('PHYSICS_FRAME', 'Physics Frame', 'Physics Frame'),
               ('ARMATURE', 'Armature', 'Armature'),
               ('COLLISION', 'Collision', 'Collision'),
               ('CAMERA_SENSOR', 'Camera sensor', 'Camera sensor'),
               ('LASER_SENSOR', 'Laser sensor', 'Laser sensor')]
    )

    dynamics = PointerProperty(type=RDDynamics)
    camera = PointerProperty(type=RDCamera)
    modelMeta = PointerProperty(type=RDModelMeta)
    author = PointerProperty(type=RDAuthor)

    muscles = PointerProperty(type=RDMuscle)


