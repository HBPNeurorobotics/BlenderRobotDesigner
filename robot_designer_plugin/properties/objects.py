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

# Blender imports
import bpy
from bpy.props import FloatProperty, StringProperty, \
    EnumProperty, FloatVectorProperty, PointerProperty

# RobotDesigner imports
from ..core import PluginManager
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
    mass = FloatProperty(name="Mass", precision=4, step=0.1)
    inertiaTensor = FloatVectorProperty(name="Inertia Tensor", precision=10,
                                        step=0.1)

@PluginManager.register_property_group(bpy.types.Object)
class RDObjects(bpy.types.PropertyGroup):
    '''
    Property group that stores general information for individual Blender
    objects with respect to the RobotEditor
    '''
    fileName = StringProperty(name="fileName")
    tag = EnumProperty(
            items=[('DEFAULT', 'Default', 'Default'),
                   ('MARKER', 'Marker', 'Marker'),
                   ('PHYSICS_FRAME', 'Physics Frame', 'Physics Frame'),
                   ('ARMATURE', 'Armature', 'Armature'),
                   ('COLLISION', 'Collision', 'Collision'),
                   ('CAMERA_SENSOR', 'Camera sensor', 'Camera sensor'),
                   ('LASER_SENSOR','Laser sensor', 'Laser sensor')]
    )

    dynamics = PointerProperty(type=RDDynamics)
