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
# Copyright (c)
#
# Changes:
#
#   2016-01-15: Stefan Ulbrich (FZI) (FZI Forschungszentrum Informatik)
#       Template created
#   Today: Your Name
#       Please add ALWAYS your modifications
#
# ######
"""
Sphinx-autodoc tag
"""

# System imports
# import os
# import sys
# import math

# Blender imports
from bpy.props import StringProperty

# RobotDesigner imports
from ..core import config, PluginManager
from ..core.operators import RDOperator, OperatorLogger, Postconditions, checkConditions

from .helpers import ModelSelected, SingleMeshSelected

# NEVER import oder operators in the toplevel (avoid circular depedencies)
# and, above all, not with the from .. import statement (multiple registration)

@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class OperatorTemplate(RDOperator):
    """
    :ref:`operator` for ...
    """

    # Obligatory class attributes
    bl_idname = config.OPERATOR_PREFIX + "unique_identifier"
    bl_label = "This label will be shown in the gui"

    # Class attributes that will be converted into parameters. Must be properties of bpy.props
    operator_parameter = StringProperty(name="1. Parameter", default="default value")


    @OperatorLogger
    # @Postconditions(ModelSelected)
    def execute(self, context):
        from .segments import SelectSegment
        message = "info"
        self.logger.debug('printing %s', message)

        # You can report messages that are shown in the gui (if invoked from the GUI)
        # {'ERROR'} will also throw an exception which is handled by the OperatorLogger
        self.report({'INFO'}, message)

        # You can throw exceptions. These will be automatically handled by the OperatorLogger
        if not message:
            raise TypeError

        # You can call other operators derived from RDOperator
        # Unfortunately, operators require keyword arguments (as below)
        # and code completion cannot be realized automatically
        SelectSegment.run(segment_name="segment1")

        # Operator must return this
        return {'FINISHED'}

    # Optionally you can provide the user with a overridden run method.
    # There you can specify the keyword arguments required when running
    # the operator (do not change the body of the function).
    # That way, you can use refactoring when changing the
    # parameters. Keep in mind, that you have to take care of the synchronization
    # of the names (parameter must exactly *match* the class's attributes *names*)
    @classmethod
    def run(cls, operator_parameter=""):
        return super().run(**cls.pass_keywords())

    # Optionally add a config dialog
    # def invoke(self, context, event):
    #     '''
    #     Show a gui that let's the user set up the parameters (when invoked from GUI)
    #
    #     :param context: :ref:`context`:
    #     :param event:
    #     :return:
    #     '''
    #     return context.window_manager.invoke_props_dialog(self)
