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
This submodule holds the configuration of the plugin (path variables, error message format, etc.)
"""

import os

script_path = os.path.dirname(os.path.dirname(__file__))

resource_path = os.path.join(script_path, 'resources')

'''This variable stores the file name where the plugin is defined (assuming it is the top level of the :mod:`core`.)'''

PLUGIN_PREFIX = "robotdesigner"
OPERATOR_PREFIX = PLUGIN_PREFIX + '.'
MENU_PREFIX = "ROBOTDESIGNER_MT_"

BACKTRACE_FILTER_FUNC = ('func_wrapper', 'op_logger', '__call__')
BACKTRACE_FILTER_HIDE_CODE = ('run', 'runNestedOperator')
BACKTRACE_MESSAGE_STACK_CODE = "\t\t{0:25}\t\t({1}:{2})\n\t\t\t{3}\n"
BACKTRACE_MESSAGE_STACK = "\t\t{0:25}\t\t({1}:{2})\n"

BACKTRACE_MESSAGE_CALLSTACK = "\n\tNesting Level %d:\n\n\tCallstack:\n"
BACKTRACE_MESSAGE = "\n\tBacktrace:\n"

EXCEPTION_MESSAGE = "\tException:\t{}\n\tMessages:\n\t\t{}\n{}\n{}"
