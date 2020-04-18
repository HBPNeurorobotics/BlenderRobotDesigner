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
"""
This module includes import and export functions for different file formats for robot descriptions.
"""

from importlib import reload
from ..core import PluginManager

from . import urdf
from . import sdf
from . import osim
from . import generic_tools

reload(urdf)
reload(sdf)
reload(osim)
reload(generic_tools)

PluginManager.register_plugin("SDF", [sdf.ImportPackage, sdf.ImportZippedPackage,
                                      sdf.ExportPackage, sdf.ExportZippedPackage])
# PluginManager.register_plugin("URDF", [urdf.ImportPlain, urdf.ImportPackage, urdf.ImportZippedPackage, urdf.ExportPlain,
#                                       urdf.ExportPackage, urdf.ExportZippedPackage])

# todo add all import export plugins into this directory.
# The file dialog should have a selection box for the format
# todo that includes all plugins and draw the operators and arguments
# required (a draw function has to be included)
__author__ = 'ulbrich-gchen'

# draft for creating a plugin mechanism
plugins = [ ('sdf', 'SDF', '.sdf', True, True)]
           #('urdf', 'URDF', '.urdf', True, True),
           # ('simox', 'SIMOX XML', '.xml', True, False), ('collada', 'COLLADA v1.5', '.dae', False, True)]
