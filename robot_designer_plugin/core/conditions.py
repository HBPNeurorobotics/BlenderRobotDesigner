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
This submodule provides the :class:`Condition`.
"""

from .logfile import operator_logger as logger, log_callstack
from .config import EXCEPTION_MESSAGE


class Condition(object):
    """
    Base Class for conditions.

    Classes should implement a ``check()`` method which returns a tuple of (bool,str) stating whether
    the condition's are met and an (potentially) empty error message.

    Using the :meth:`.operators.RDOperator.Preconditions` decorator, the conditions that should be met
    when executing an operator (i.e., a subclass of :class:`.operators.RDOperator`) are added to the classes'
    list of preconditions and :meth:`check_conditions` is called when Blender executes the
    :meth:`.operators.RDOperator.poll` method.

    .. note::

        Instances of this type should never be created.

    For examples see :class:`robot_designer_plugin.operators.helpers.ModelSelected`.
    """

    @staticmethod
    def check_conditions(*conditions):
        """
        Checks whether the arguments are met.

        :param conditions: A an arbitrary number of conditions
        :type conditions: :class:`Condition` sub classes.
        :return: Tuple(bool, str), True and empty string if all conditions are met. False and sting with message of
        unmet conditions.
        """
        try:
            check = [i.check() for i in conditions]
            return all([i[0] for i in check]), "\n".join([i[1] for i in check if not i[0]])

        except Exception as e:
            logger.error("Exception in check precondition!\n" + EXCEPTION_MESSAGE + "\nConditions: %s",
                         type(e).__name__, e, log_callstack(), log_callstack(True), conditions)
            return False, "Exception raised"

    @staticmethod
    def call():
        '''
        Needs to be overridden in sub classes

        :raises: NotImplementedError
        '''
        raise NotImplementedError("Must be overridden in subclasses")
