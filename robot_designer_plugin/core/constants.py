# #####
#  This file is part of the RobotDesigner developed in the Neurorobotics
#  subproject of the Human Brain Project (https://www.humanbrainproject.eu).
#
#  The Human Brain Project is a European Commission funded project
#  in the frame of the Horizon2020 FET Flagship plan.
#  (http://ec.europa.eu/programmes/horizon2020/en/h2020-section/fet-flagships)
#
#  The Robot Designer has initially been forked from the RobotEditor
#  (https://gitlab.com/h2t/roboteditor) developed at the Karlsruhe Institute
#  of Technology in the High Performance Humanoid Technologies Laboratory (H2T).
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
#  Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# ######
"""
This submodule provides resolvable names for Blender constants.
"""


class StringConstants(object):
    """
    Blender String constants. Using this class's static arguments circumvents typos causing runtime errors.

    .. todo::

        Increase this list with all important constants.

    """
    mesh = "MESH"
    camera = "CAMERA"
    armature = "ARMATURE"
    bone = "BONE"
    empty = "EMPTY"
    info = "INFO"
    error = "ERROR"
    none = "NONE"
    tria_right = "TRIA_RIGHT"
    tria_down = "TRIA_DOWN"
