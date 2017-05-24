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
#   2016-01-15: Stefan Ulbrich (FZI), First version of the plugin framework core
#
# ######
'''
This package is a framework for creating large application-like plugins for Blender. It provides the
Base classes and Python decorators for automatic registration, log files, resource management and
much more.

In the future, it is planned to release this package independently from the HRP/NRP RobotDesigner and
provide mechanisms for the creation of web-based applications for editing.

It consists of submodules for:

1. working with :term:`operators<operator>` (:mod:`robot_designer_plugin.core.operators`),
2. simplify Gui development (:mod:`robot_designer_plugin.core.gui`),
3. logging and debugging (:mod:`robot_designer_plugin.core.logfile`),
4. configuration variables (:mod:`robot_designer_plugin.core.config`),
5. automated plugin setup (registration to blender) (:mod:`robot_designer_plugin.core.pluginmanager`)
'''

from . import constants, config, operators, conditions, logfile, pluginmanager, resources, gui, property
from importlib import reload

reload(constants)
reload(gui)
reload(config)
reload(conditions)
reload(logfile)
reload(operators)
reload(pluginmanager)  # Should be last imported .. depends on gui and operators
reload(property)  # Has to be imported after pluginmanager
reload(resources)

# These have to be listed AFTER reload. Otherwise, they refer to outdated objects

from .pluginmanager import PluginManager
from .conditions import Condition
from .operators import RDOperator
# from .resources import reload_resources

