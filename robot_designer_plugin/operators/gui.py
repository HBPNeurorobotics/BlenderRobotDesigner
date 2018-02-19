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
# Blender imports
import bpy

# RobotDesigner imports
from ..core import config, PluginManager, RDOperator


@PluginManager.register_class
class PrintTransformations(RDOperator):
    """
    :ref:`operator` for print transformation matrix from active object to all selected objects.

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "printtransformations"
    bl_label = "Print transformation matrix from active object to all selected objects"

    @classmethod
    def poll(cls, context):
        return True

    @RDOperator.OperatorLogger
    def execute(self, context):
        active_object = bpy.context.active_object

        for ob in [obj for obj in context.scene.objects if obj.select]:
            print('Transformation from %(from)s to %(to)s:' % {'from': active_object.name, 'to': ob.name})
            transform = active_object.matrix_world.inverted() * ob.matrix_world
            print(transform)

        return {'FINISHED'}


