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
This sub package provides logging mechanism for the plugin development.

Blender is not easy to debug (adding an external debugger is planned) such that providing informative
output to a log file is mandatory.
The log file is stored in the path stored in the plugin directory (:data:`.config.script_path`) in
``resources/log.txt``.

An example of a log file:


.. literalinclude:: ../../../doc/source/developer_manual/log_example.txt

Logging of operators can be automated with the decorators and base classes in the :mod:`.operators` module.
"""

import logging
import sys
import traceback
import os

from .gui import InfoBox

from ..core.config import BACKTRACE_MESSAGE_CALLSTACK, BACKTRACE_MESSAGE, BACKTRACE_FILTER_FUNC, \
    BACKTRACE_FILTER_HIDE_CODE, BACKTRACE_MESSAGE_STACK, BACKTRACE_MESSAGE_STACK_CODE, EXCEPTION_MESSAGE, script_path

from importlib import reload

reload(logging)
logging.basicConfig(format='[%(levelname)5s|%(name)10s|%(filename)12s:%(lineno)03d|%(funcName)s()] %(message)s',
                    filename=os.path.join(script_path, 'resources/log.txt'), filemode='w')

# Also log to stdout
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

operator_logger = logging.getLogger('Operators')
'''
Logging object associated with :term:`operators`. All loggers store to ``resources/log.txt``
'''
export_logger = logging.getLogger('Export')
'''
Logging object associated with :term:`operators`. All loggers store to ``resources/log.txt``
'''
core_logger = logging.getLogger('Core')
'''
Logging object associated with the :term:`plugin core`. All loggers store to ``resources/log.txt``
'''
gui_logger = logging.getLogger('GUI')
'''
Logging object associated with the user interface. All loggers store to ``resources/log.txt``
'''
prop_logger = logging.getLogger('Properties')
'''
Logging object associated with :term:`properties`. All loggers store to ``resources/log.txt``
'''

operator_logger.setLevel(logging.INFO)
export_logger.setLevel(logging.INFO)
core_logger.setLevel(logging.INFO)
gui_logger.setLevel(logging.INFO)
prop_logger.setLevel(logging.INFO)


def LogFunction(func):
    """
    Logging / exception handling decorator for functions (use for draw function for instance).

    :param func: The function to decorate
    :return: A :term:`decorator`
    """

    def func_logger(self, context):

        # Execute the Operator
        try:
            return func(self, context)

        except Exception as e:
            gui_logger.error("Draw function in {} module threw an exception:\n {} {} {} {} {}".format(
                             func.__module__, EXCEPTION_MESSAGE, type(e).__name__, e, log_callstack(), log_callstack(back_trace=True)))
            InfoBox.global_messages.append(e)

    return func_logger


def log_callstack(back_trace=False):
    """
    Helper function that formats either a (filtered) backtrace or call stack in a string. Blender internals
    are filtered such that errors in the own code can be detected more easily.

    :param back_trace: If true, the backtrace is returned. Otherwise, the call stack is returned.
    :return: the formatted call stack/backtrace in a string.
    """

    if not back_trace:
        message = BACKTRACE_MESSAGE_CALLSTACK % len([i for i in traceback.extract_stack() if i[2] == 'run'])
        stack = traceback.extract_stack()[:-1]
    else:
        message = BACKTRACE_MESSAGE
        stack = traceback.extract_tb(sys.exc_info()[2])

    last_call = ""
    for path, line, func, code in stack:
        if 'addons' in path:
            file = '...' + path[path.find('addons') + 6:]
        elif 'scripts' in path:
            file = '...' + path[path.find('scripts') + 7:]
        else:
            file = path
        if func not in BACKTRACE_FILTER_FUNC:
            if func in BACKTRACE_FILTER_HIDE_CODE:
                message += BACKTRACE_MESSAGE_STACK.format(func, file, line)
            else:
                message += BACKTRACE_MESSAGE_STACK_CODE.format(func, file, line, code, last_call)
        last_call = code

    return message


def log_callstack_last(back_trace=False):
    if not back_trace:
        stack = traceback.extract_stack()[:-1]
    else:
        stack = traceback.extract_tb(sys.exc_info()[2])

    message = "empty"

    print("Parsing stack")

    for path, line, func, code in stack:
        print(path, func)
        if func not in BACKTRACE_FILTER_FUNC:
            if func not in BACKTRACE_FILTER_HIDE_CODE:
                file = os.path.split(path)[-1]
                message = "{}:{}".format(file, line)

    return message
