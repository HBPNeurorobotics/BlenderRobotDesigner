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
import math
import mathutils

# Blender imports
import bpy
from bpy.props import StringProperty

from ..core import Condition, PluginManager
from ..core.constants import StringConstants
from ..core import RDOperator

def _vec_roll_to_mat3(vec, roll):
    """
    Function to convert a given rotation vector and a roll angle along this axis into a 3x3 rotation matrix
    Python port of the C function defined in armature.c
    Credits: blenderartists.org user vida_vida

    :param vec:
    :param roll:
    :return:
    """
    target = mathutils.Vector((0, 1, 0))
    nor = vec.normalized()
    axis = target.cross(nor)
    if axis.dot(axis) > 0.0000000001:  # this seems to be the problem for some bones, no idea how to fix
        axis.normalize()
        theta = target.angle(nor)
        bMatrix = mathutils.Matrix.Rotation(theta, 3, axis)
    else:
        updown = 1 if target.dot(nor) > 0 else -1
        bMatrix = mathutils.Matrix.Scale(updown, 3)

        # C code:
        # bMatrix[0][0]=updown; bMatrix[1][0]=0.0;    bMatrix[2][0]=0.0;
        # bMatrix[0][1]=0.0;    bMatrix[1][1]=updown; bMatrix[2][1]=0.0;
        # bMatrix[0][2]=0.0;    bMatrix[1][2]=0.0;    bMatrix[2][2]=1.0;
        bMatrix[2][2] = 1.0

    rMatrix = mathutils.Matrix.Rotation(roll, 3, nor)
    mat = rMatrix * bMatrix
    return mat


def _mat3_to_vec_roll(mat):
    """
    Function to convert a 3x3 rotation matrix to a rotation axis and a roll angle along this axis
    Python port of the C function defined in armature.c

    Thanks to blenderartists.org user vida_vida

    :param mat:
    :return:
    """
    from ..properties.globals import global_properties
    vec = mat.col[1] * global_properties.bone_length.get(bpy.context.scene)
    vecmat = _vec_roll_to_mat3(mat.col[1], 0)
    vecmatinv = vecmat.inverted()
    rollmat = vecmatinv * mat
    roll = math.atan2(rollmat[0][2], rollmat[2][2])
    return vec, roll


class ModelSelected(Condition):
    @staticmethod
    def check():
        """
        :ref:`condition` that assures the armature is selected.

        :return: True if the condition is met, else false. String with error message.
        """
        if bpy.context.active_object:
            return bpy.context.active_object.type == 'ARMATURE', "Model not selected and active." #or bpy.context.active_object.type == 'MESH'
        else:
            return False, "No model selected"


class SingleSegmentSelected(Condition):
    @staticmethod
    def check():
        """
        :ref:`condition` that assures that a single mesh object (i.e., two selected objects where exactly one is a mesh).

        :return: True if the condition is met, else false. String with error message.
        """
        if bpy.context.active_bone:
            selected_segments = [i for i in bpy.context.active_object.data.bones if i.select]
            return len(selected_segments) == 1, "Single Segment must be selected"
        else:
            return False, "No Object select"


class AtLeastOneSegmentSelected(Condition):
    @staticmethod
    def check():
        """
        :ref:`condition` that assures that at least one bone of the active object is selected

        :return: True if the condition is met, else false. String with error message.
        """
        if bpy.context.active_bone:
            selected_segments = [i for i in bpy.context.active_object.data.bones if i.select]
            return len(selected_segments) >= 1, "At least one segment must be selected"
        else:
            return False, "No Object select"


class SingleMeshSelected(Condition):
    @staticmethod
    def check():
        """
        :ref:`condition` that assures that a single mesh object (i.e., two selected objects where exactly one is a mesh).

        :return: True if the condition is met, else false. String with error message.
        """
        selected = [i for i in bpy.context.selected_objects if i.type == 'MESH']
        return len(selected) == 1, "Single mesh object must be selected."


class ObjectMode(Condition):
    @staticmethod
    def check():
        """
        :term:`condition` that assures that the :term:`object mode` is selected.
        """
        if bpy.context.object:
            return bpy.context.object.mode == 'OBJECT', "Must be in object mode"
        else:
            return True, ""


class PoseMode(Condition):
    @staticmethod
    def check():
        """
        :term:`condition` that assures that the :term:`pose mode` is selected.
        """
        if bpy.context.object:
            return bpy.context.object.mode == 'POSE', "Must be in pose mode"
        else:
            return True, ""


class NotEditMode(Condition):
    @staticmethod
    def check():
        """
        :term:`condition` that assures that the :term:`edit mode` is *not* selected.
        """
        if bpy.context.object:
            return bpy.context.object.mode != 'EDIT', "Must not be in edit mode"
        else:
            return True, ""


class SingleCameraSelected(Condition):
    @staticmethod
    def check():
        """
        :term:`condition` that assures that a :class:`bpy.types.Camera` associated object is selected.
        """
        selected = [i for i in bpy.context.selected_objects if i.type == StringConstants.camera]
        return len(selected) == 1, "Single camera object must be selected."


class SingleMassObjectSelected(Condition):
    @staticmethod
    def check():
        """
        :term:`condition` that assures that a :class:`bpy.types.Camera` associated object is selected.
        """
        selected = [i for i in bpy.context.selected_objects if
                    i.type == StringConstants.empty and i.RobotDesigner.tag == "PHYSICS_FRAME"]
        return len(selected) == 1, "Single mass object must be selected."


class SelectObjectBase(RDOperator):
    """
    Base class for :ref:`operators <operator>` for selecting an object (:class:`bpy.types.Object`)
    second to the selected model (Blender object with :class:`bpy.types.Armature` data)
    """

    object_name = StringProperty()
    object_data_type = 'MESH'

    @classmethod
    def run(cls, object_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        mesh = bpy.data.objects[self.object_name]

        arm = context.active_object

        for obj in context.scene.objects:
            obj.select = False

        mesh.select = True
        arm.select = True

        return {'FINISHED'}


class AssignObjectBase(RDOperator):
    """
    Base class for :ref:`operators <operator>` for assigning an object to the currently selected
    segment segment.
    """

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        return {'FINISHED'}

		
class ObjectScaled(Condition):
    @staticmethod
    def check():
        """
        :term:`condition` that assures that model has been scaled before the operation.
        """
        if bpy.context.active_object:
            return (bpy.context.active_object.scale.x == bpy.context.active_object.scale.y == bpy.context.active_object.scale.z == 1.0), "Object has to be scaled!"
        else:
            return True, ""