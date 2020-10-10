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
from mathutils import Euler, Matrix
from math import radians

# Blender imports
import bpy
from bpy.props import FloatProperty, BoolProperty, EnumProperty, PointerProperty, StringProperty

# RobotDesigner imports
from ..operators.segments import UpdateSegments
from ..core import PluginManager
from ..core.logfile import prop_logger as logger

from .globals import global_properties


@PluginManager.register_property_group()
class RDActuator(bpy.types.PropertyGroup):
    """
    Property group that contains all controller-related parameters
    """
    isActive: BoolProperty(name="Active Dynamic Limits", default=False)

    maxVelocity: FloatProperty(name="Max. Velocity", precision=4, step=100, default=-1)
    maxTorque: FloatProperty(name="Max. Torque", precision=4, step=100, default=-1)
    acceleration: FloatProperty(name="Acceleration", precision=4, step=100)
    deceleration: FloatProperty(name="Deceleration", precision=4, step=100)

@PluginManager.register_property_group()
class RDLinkInfo(bpy.types.PropertyGroup):
    '''
    Property group that contains information about link's gravity and self collision
    '''
    link_self_collide: BoolProperty(name='Self Collide', default=True)
    gravity: BoolProperty(name='Gravity', default=True)


@PluginManager.register_property_group()
class RDOde(bpy.types.PropertyGroup):
    '''
    Property group that contains ODE data
    '''
    cfm_damping: BoolProperty(name='CFM Damping', default=False)
    i_s_damper: BoolProperty(name='Implicit-Spring-Damper', default=False)
    cfm: FloatProperty(name='CFM', default=0, min=0)
    erp: FloatProperty(name='ERP', default=0.2, min=0, max=1)


@PluginManager.register_property_group()
class RDJointDynamics(bpy.types.PropertyGroup):
    '''
    Property group that contains joint dynamics data
    '''
    damping: FloatProperty(name='Damping', default=0)
    friction: FloatProperty(name='Friction', default=0)
    spring_reference: FloatProperty(name='Spring Reference', default=0)
    spring_stiffness: FloatProperty(name='Spring Stiffness', default=0)


@PluginManager.register_property_group()
class RDDegreeOfFreedom(bpy.types.PropertyGroup):
    """
    Property group that defines a degree of freedom
    """

    def updateDoF(self: memoryview, context):
        if global_properties.do_kinematic_update.get(context.scene):
            segment_name = context.active_bone.name
            UpdateSegments.run(segment_name=segment_name, recurse=False)

    value: FloatProperty(name="Value", update=updateDoF, precision=4,
                         step=100)
    offset: FloatProperty(name="Offset", update=updateDoF, precision=4,
                          step=100)
    min: FloatProperty(name="Min", default=-90.0, precision=4, step=100)
    max: FloatProperty(name="Max", default=90.0, precision=4, step=100)
    isActive: BoolProperty(name="LimitActive", default=True)


@PluginManager.register_property_group()
class RDJointController(bpy.types.PropertyGroup):
    """
    Property group for joint controllers
    """
    isActive: BoolProperty(name="Active", default=False)

    controllerType: EnumProperty(
        items=[('position', 'Position', 'Position'),
               ('velocity', 'Velocity', 'Velocity')],
        name="Controller mode:")

    # controllerType = EnumProperty(
    #     items=[('PID', 'PID controller', 'PID controller'),
    #            ('P', 'P controller', 'P controller')],
    #     name="Controller type:"
    # )

    P: FloatProperty(name="P", precision=4, step=100, default=1.0)
    I: FloatProperty(name="I", precision=4, step=100, default=0.0)
    D: FloatProperty(name="D", precision=4, step=100, default=0.0)


@PluginManager.register_property_group()
class RDEulerAnglesSegment(bpy.types.PropertyGroup):
    """
    Property group that defines a joint in Euler mode
    """

    def getTransformFromParent(self):
        rot = Euler((radians(self.alpha.value), radians(self.beta.value),
                     radians(self.gamma.value)), 'XYZ').to_matrix()
        rot.resize_4x4()

        transl = Matrix.Translation((self.x.value, self.y.value, self.z.value))
        # print("here",transl * rot)
        return transl @ rot

    x: PointerProperty(type=RDDegreeOfFreedom)
    y: PointerProperty(type=RDDegreeOfFreedom)
    z: PointerProperty(type=RDDegreeOfFreedom)
    alpha: PointerProperty(type=RDDegreeOfFreedom)
    beta: PointerProperty(type=RDDegreeOfFreedom)
    gamma: PointerProperty(type=RDDegreeOfFreedom)


@PluginManager.register_property_group()
class RDDenavitHartenbergSegment(bpy.types.PropertyGroup):
    """
    Property group that defines a joint in DH mode
    """

    def getTransformFromParent(self):
        alphaMatrix = Euler((radians(self.alpha.value), 0, 0),
                            'XYZ').to_matrix()
        alphaMatrix.resize_4x4()

        thetaMatrix = Euler((0, 0, radians(self.theta.value)),
                            'XYZ').to_matrix()
        thetaMatrix.resize_4x4()

        translation = Matrix.Translation((self.a.value, 0, self.d.value, 1))

        return translation @ alphaMatrix @ thetaMatrix

    theta: PointerProperty(type=RDDegreeOfFreedom)
    d: PointerProperty(type=RDDegreeOfFreedom)
    alpha: PointerProperty(type=RDDegreeOfFreedom)
    a: PointerProperty(type=RDDegreeOfFreedom)


@PluginManager.register_property_group(bpy.types.Bone)
class RDSegment(bpy.types.PropertyGroup):
    """
    Bone property, contains all relevant bone information for RobotDesigner
    """

    def callbackSegments(self, context):
        armName = context.active_object.name
        segment_name = context.active_bone.name
        # We should not have to recurse when updating a local property.
        UpdateSegments.run(segment_name=segment_name, recurse=False)

    def getTransform(self):
        """
        returned transform matrix is of the form translation*parentMatrix*rotation
        parent is dependent of parent mode, that is either Euler or DH
        either translation or rotation is I_4 dependent of the joint type,
        whereas a revolute joints contributes a rotation only and a
        prismatic joint contributes a translation only
        """

        translation = Matrix()  # initialize as I_4 matrix
        rotation = Matrix()  # initialize as I_4 matrix
        axis_matrix = Matrix()  # contains axis information which should be applied to parentMatrix

        if self.axis_revert:
            inverted = -1
        else:
            inverted = 1

        if self.parentMode == 'EULER':
            parentMatrix = self.Euler.getTransformFromParent()
        else:  # self.parentMode == 'DH'
            parentMatrix = self.DH.getTransformFromParent()

        if self.jointMode == 'REVOLUTE':
            if self.axis == 'X':
                rotation = Euler(
                    (radians(self.theta.value + self.theta.offset), 0, 0),
                    'XYZ').to_matrix()
                rotation.resize_4x4()
                axis_matrix = Euler((radians(180 * (1 - inverted) / 2), 0, 0),
                                    'XYZ').to_matrix()
                axis_matrix.resize_4x4()
            elif self.axis == 'Y':
                rotation = Euler(
                    (0, radians(self.theta.value + self.theta.offset), 0),
                    'XYZ').to_matrix()
                rotation.resize_4x4()
                axis_matrix = Euler((0, radians(180 * (1 - inverted) / 2), 0),
                                    'XYZ').to_matrix()
                axis_matrix.resize_4x4()
            elif self.axis == 'Z':
                rotation = Euler(
                    (0, 0, radians(self.theta.value + self.theta.offset)),
                    'XYZ').to_matrix()
                rotation.resize_4x4()
                axis_matrix = Euler((0, 0, radians(180 * (1 - inverted) / 2)),
                                    'XYZ').to_matrix()
                axis_matrix.resize_4x4()

        if self.jointMode == 'PRISMATIC':
            if self.axis == 'X':
                translation = Matrix.Translation(
                    (inverted * (self.d.value + self.d.offset), 0, 0, 1))
            elif self.axis == 'Y':
                translation = Matrix.Translation(
                    (0, inverted * (self.d.value + self.d.offset), 0, 1))
            elif self.axis == 'Z':
                translation = Matrix.Translation(
                    (0, 0, inverted * (self.d.value + self.d.offset), 1))

        if self.jointMode == 'FIXED' or self.jointMode == 'REVOLUTE2' or self.jointMode == 'UNIVERSAL' or self.jointMode == 'BALL':  # todo: check if this is right for fixed joint type
            translation = Matrix.Translation((0, 0, 0, 1))

        return parentMatrix @ axis_matrix, translation @ rotation
        # return parentMatrix, translation*rotation

    jointMode: EnumProperty(
        items=[('REVOLUTE', 'Revolute', 'revolute joint'),
               ('PRISMATIC', 'Prismatic', 'prismatic joint'),
               ('REVOLUTE2', 'Revolute2', 'revolute2 joint'),
               ('UNIVERSAL', 'Universal', 'universal joint'),
               ('BALL', 'Ball', 'ball joint'),
               ('FIXED', 'Fixed', 'fixed joint')],
        name="Joint Mode", update=callbackSegments
    )

    parentMode: EnumProperty(
        items=[('EULER', 'Euler', 'Euler mode'),
               ('DH', 'DH', 'DH mode')],
        name="Parent Mode", update=callbackSegments
    )

    axis: EnumProperty(
        items=[('X', 'X', 'X Axis'),
               ('Y', 'Y', 'Y Axis'),
               ('Z', 'Z', 'Z Axis')],
        name="Active Axis", default='Z', update=callbackSegments
    )

    RD_Bone: BoolProperty(name="Created by RD", default=False)

    axis_revert: BoolProperty(name="Axis Reverted?", default=False,
                              update=callbackSegments)

    dynamic_limits: PointerProperty(type=RDActuator)
    theta: PointerProperty(type=RDDegreeOfFreedom)  # Joint transform + limits, relative to local frame.
    d: PointerProperty(type=RDDegreeOfFreedom)
    jointController: PointerProperty(type=RDJointController)
    linkInfo: PointerProperty(type=RDLinkInfo)
    ode: PointerProperty(type=RDOde)
    joint_dynamics: PointerProperty(type=RDJointDynamics)
    Euler: PointerProperty(type=RDEulerAnglesSegment)  # Frame relative to parent
    DH: PointerProperty(
        type=RDDenavitHartenbergSegment)  # Dito but in a different way. Only one, either DH or Euler is used.
    world: BoolProperty(name="Attach Link to World", default=False)
    joint_name: StringProperty(name="Joint Name: ")  # Name of parent joint of segment


def getTransformFromBlender(bone):
    # In whatever mode we currently are, get me a normal bpy.types.Bone.
    # bone = bpy.context.active_object.data.bones[bone.name]
    # On the other hand ...
    assert isinstance(bone, bpy.types.Bone)
    parent = bone.parent
    if parent is not None:
        pose_wrt_parent = parent.matrix_local.inverted() @ bone.matrix_local
    else:
        pose_wrt_parent = bone.matrix_local
    # Now, compute the joint Trafo. RD Applies the joint trafo to the pose bone.
    # What is computed here as pose_wrt_parent refers to the edit bones.
    _, joint_trafo = bone.RobotDesigner.getTransform()
    return pose_wrt_parent, joint_trafo
