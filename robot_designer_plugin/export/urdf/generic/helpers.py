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

# Blender-specific imports
from mathutils import *

__author__ = 'ulbrich'


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
    return " ".join([str(i).rstrip('0').rstrip('.') for i in l])


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
