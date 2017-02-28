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
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######

# system imports
import re
import numbers
from .transformations import compose_matrix, concatenate_matrices, inverse_matrix, translation_from_matrix, euler_from_matrix

# Blender-specific imports
from mathutils import *

__author__ = 'ulbrich'

def string2float_list(s):
    return [float(i) for i in s.split()]

def rounded(val):
    if isinstance(val, str):
        return rounded(float(val))
    elif isinstance(val, numbers.Number):
        return int(round(val,6) * 1e5) / 1.0e5
    else:
        return [rounded(v) for v in val]


def pose_modelpose(pose, model_pose):
    pose_link = pose_float2homogeneous(rounded(pose))
    pose_model = pose_float2homogeneous(rounded(model_pose))
    con_matrix = concatenate_matrices(pose_model, pose_link)
    pose_xyz = translation_from_matrix(con_matrix)
    pose_rpy = euler_from_matrix(con_matrix)
    return [pose_xyz[0], pose_xyz[1], pose_xyz[2], pose_rpy[0], pose_rpy[1], pose_rpy[2]]


def pose_string2homogeneous(pose):
    pose_float = string2float_list(pose)
    translate = pose_float[:3]
    angles = pose_float[3:]
    homogeneous = compose_matrix(None, None, angles, translate)
    return homogeneous


def pose_float2homogeneous(pose_float):
    translate = pose_float[:3]
    angles = pose_float[3:]
    homogeneous = compose_matrix(None, None, angles, translate)
    return homogeneous

def localpose2globalpose(ref_pose_global, angles, translate):
    localhomo = compose_matrix(None, None, string2float_list(angles), string2float_list(translate))
    translate = ref_pose_global[:3]
    angles = ref_pose_global[3:]
    refghomo = compose_matrix(None, None, angles, translate)
    relative_matrix = concatenate_matrices(refghomo, localhomo)
    glb_xyz = translation_from_matrix(relative_matrix)
    glb_rpy = euler_from_matrix(relative_matrix)
    return list_to_string(glb_xyz), list_to_string(glb_rpy)


def pose2origin(parent_pose_homo, self_pose_homo):
    relative_matrix = concatenate_matrices(inverse_matrix(parent_pose_homo), self_pose_homo)
    org_xyz = translation_from_matrix(relative_matrix)
    org_rpy = euler_from_matrix(relative_matrix)
    return org_xyz, org_rpy

def homo2origin(self_pose_homo):
    org_xyz = translation_from_matrix(self_pose_homo)
    org_rpy = euler_from_matrix(self_pose_homo)
    return org_xyz, org_rpy


def rpy_to_xyz(rpy):
    """Converts
    Converts a tuple representing roll-pitch-yaw (XYZ=ZY'X'')values to euler XY'Z''

    :param rpy: list/tuple with the RPY angles
    :return: list with the euler angles
    """
    euler = Euler(rpy, 'ZYX').to_quaternion().to_euler('XYZ')
    return [euler.x, euler.y, euler.z]


def convert_euler(euler, old_convention, new_convention):
    """Converts between Euler conventions.

    **WARNING: does not do what it is expected to do (x will always be the angle around the local x axis)**.
    Converts between different euler conventions. Conventions are specified as strings.
    Possible options are 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX' and 'RPY'

    :param euler: The euler angles
    :type euler: Python list/tuple with three elements
    :param old_convention: String describing the old convention
    :param new_convention: String describing the new convention
    :return: python list of the orientation in the new convention
    """
    # todo move to helper module one level above (and create it)
    if old_convention == 'RPY':
        old_convention = 'ZYX'  # todo check
    if new_convention == 'RPY':
        new_convention = 'ZYX'  # todo check
    new_euler = Euler(euler, old_convention).to_matrix().to_euler(new_convention)
    return [new_euler.x, new_euler.y, new_euler.z]


def list_to_string(l):
    """
    Converts a python list of floats to a string. If there are no decimals behind the comma separator they will be
    cut off (e.g., :math:`1.0 \rightarrow 1`)

    :param l:
    :return:
    """
    print("HERER", l)
    #return " ".join([str(i).rstrip('0').rstrip('.') for i in l])  BUG e10 ->  e1
    return " ".join([str(i) for i in l])


def string_to_list(s):
    """
    Converts a XML string representing a float vector to python list of float.

    :param s: the XML string
    :return: the python list
    """
    # todo move to helper module one level above (and create it)
    v = [float(i) for i in re.findall("[-+]?\d*\.?\d+[eE]?[-+]?\d*", s)]
    return v


def get_value(element, default=0.0):
    """
    Reads a value of an urdf_dom element. If the element is not readable (i.e., is None),
    the default value is returned. This is useful when working with etree or generateDS.py.

    :param element: the urdf_dom element
    :param default: The default value
    :return: The value (a string!)
    """
    # todo can we get the default value from the xsd file?
    try:
        return element
    except AttributeError:
        return default


def get_list_value(element, default=0.0):
    """
    Reads a value of an urdf_dom element. If the element is not readable (i.e., is None),
    the default value is returned. This is useful when working with etree or generateDS.py.

    :param element: the urdf_dom element
    :param default: The default value
    :return: The value (a string!)
    """
    # todo can we get the default value from the xsd file?
    try:
        if len(element):
            return element[0]
        else:
            return 0.0
    except AttributeError:
        return default