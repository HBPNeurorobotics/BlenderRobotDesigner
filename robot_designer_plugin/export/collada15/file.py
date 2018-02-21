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
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######
"""
Sphinx-autodoc tag
"""

# ######
# System imports
# import os
# import sys
# import math

# ######
# Blender imports
import bpy
from bpy.props import StringProperty
# import mathutils

# ######
# RobotDesigner imports
from ...core import config, PluginManager
from ...core.operators import RDOperator
from ...operators.helpers import ModelSelected, ObjectMode

# ######
# Plugin imports
from . import  fix
from . import collada

def extractData(segment_name):
    tree = collada.Tree()
    arm = bpy.context.active_object

    bpy.ops.roboteditor.select_segment(segment_name=segment_name)
    currentBone = bpy.context.active_bone

    tree.name = segment_name

    if currentBone.parent:
        parentName = currentBone.parent.name
    else:
        parentName = None

    if currentBone.RobotEditor.axis_revert:
        inverted = -1
    else:
        inverted = 1

    axis = ["0", "0", "0"]
    if currentBone.RobotEditor.axis == 'X':
        axis[0] = str(inverted)
    elif currentBone.RobotEditor.axis == 'Y':
        axis[1] = str(inverted)
    elif currentBone.RobotEditor.axis == 'Z':
        axis[2] = str(inverted)

    tree.axis = axis

    trafo, dummy = currentBone.RobotEditor.getTransform()
    # translation
    tree.addTrafo([str(element) for element in trafo.translation])
    # rotation
    rotation = trafo.to_euler()
    tree.addTrafo([str(element) for element in [0, 0, 1, rotation.z]])
    tree.addTrafo([str(element) for element in [0, 1, 0, rotation.y]])
    tree.addTrafo([str(element) for element in [1, 0, 0, rotation.x]])

    if currentBone.RobotEditor.jointMode == 'REVOLUTE':
        tree.initialValue = str(currentBone.RobotEditor.theta.offset)
        tree.min = str(currentBone.RobotEditor.theta.min)
        tree.max = str(currentBone.RobotEditor.theta.max)
        tree.axis_type = 'revolute'
    else:
        tree.initialValue = str(currentBone.RobotEditor.d.offset)
        tree.min = str(currentBone.RobotEditor.d.min)
        tree.max = str(currentBone.RobotEditor.d.max)
        tree.axis_type = 'prismatic'
    children = [child.name for child in currentBone.children]

    tree.meshes = [mesh.name for mesh in bpy.data.objects if
                   mesh.type == 'MESH' and mesh.parent_bone == segment_name]

    markers = [m for m in bpy.data.objects if
               m.RobotEditor.tag == 'MARKER' and m.parent_bone == segment_name]
    # tree.markers = [(m.name,(currentBone.matrix_local.inverted()*m.matrix_world.translation).to_tuple())
    #  for m in markers]
    # tree.markers = [(m.name,(m.matrix_parent_inverse*m.matrix_world.translation).to_tuple()) for m in markers]

    poseBone = arm.pose.bones[segment_name]
    tree.markers = [
        (m.name, (
            poseBone.matrix.inverted() * arm.matrix_world.inverted() * m.matrix_world.translation).to_tuple())
        for
        m in markers]

    for child in children:
        tree.addChild(extractData(child))

    return tree
# @PluginManager.register_class
# class ImportCollada15(RDOperator):
#     """
#     Not implemented
#     **Preconditions:**
#
#     **Postconditions:**
#     """
#     bl_idname = config.OPERATOR_PREFIX + "selectarmature"
#     bl_label = "Select model"
#
#     model_name = StringProperty()
#
#     @classmethod
#     def run(cls, model_name=""):
#         return super().run(**cls.pass_keywords())
#
#     @classmethod
#     def poll(cls, context):
#         """
#         Checks whether preconditions are met for this :ref:`operator`
#
#         :param context: :ref:`context`
#         :return: True when conditions are met, False otherwise
#         """
#         return check_conditions(ObjectMode)
#
#     @OperatorLogger
#     @Postconditions(ModelSelected)
#     def execute(self, context):
#         self.report({'ERROR'},"Not implemented")

@RDOperator.Preconditions(ObjectMode, ModelSelected)
@PluginManager.register_class
class RobotEditor_exportCollada(RDOperator):
    """
    :term:`operator` for exporting a :term:`robot model` to COLLADA 1.5
    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = "roboteditor.colladaexport"
    bl_label = "Export to COLLADA 1.5"

    filepath = StringProperty(subtype='FILE_PATH')

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        bpy.ops.wm.collada_export(filepath=self.filepath,
                                  check_existing=False, filter_blender=False,
                                  filter_image=False, filter_movie=False,
                                  filter_python=False, filter_font=False,
                                  filter_sound=False, filter_text=False,
                                  filter_btx=False, filter_collada=True,
                                  apply_modifiers=True,
                                  filter_folder=True)

        fix.fixCollada(self.filepath, self.filepath, context)
        handler = collada.COLLADA()
        handler.import14(self.filepath)

        arm = context.active_object
        baseBoneName = arm.data.bones[0].name

        tree = collada.Tree()
        tree.name = arm.name
        tree.addChild(extractData(baseBoneName))

        handler.attach(tree)

        massFrames = [obj for obj in context.scene.objects if
                      obj.RobotEditor.tag == 'PHYSICS_FRAME' and obj.parent_bone is not '']
        for frame in massFrames:
            # transform = frame.parent.data.bones[frame.parent_bone].matrix_local.inverted() * frame.matrix_local
            segment_name = frame.parent.data.bones[frame.parent_bone].name
            poseBone = arm.pose.bones[segment_name]
            transform = poseBone.matrix.inverted() * arm.matrix_world.inverted() * frame.matrix_world
            frameTrafos = [tuple(v for v in transform.translation)]
            frameRotation = transform.to_euler()
            frameTrafos.append(tuple([0, 0, 1, frameRotation.z]))
            frameTrafos.append(tuple([0, 1, 0, frameRotation.y]))
            frameTrafos.append(tuple([1, 0, 0, frameRotation.x]))

            collisionModels = []
            collisionModelTransformations = {}
            for model in [i for i in context.scene.objects if i.parent == frame]:
                modelName = model.data.name.replace('.', '_') + '-mesh'
                collisionModels.append(modelName)
                # matrix = model.parent.data.bones[model.parent_bone].matrix_local.inverted() * model.matrix_local
                matrix = model.matrix_local
                collisionModelTransformations[modelName] = [tuple(v for v in matrix.translation)]
                rotation = matrix.to_euler()
                collisionModelTransformations[modelName].append(tuple([0, 0, 1, rotation.z]))
                collisionModelTransformations[modelName].append(tuple([0, 1, 0, rotation.y]))
                collisionModelTransformations[modelName].append(tuple([1, 0, 0, rotation.x]))

            # TODO also bring the matrix_local to all collisionmodels
            print("mass frames", frame.name, collisionModels)
            handler.addMassObject(frame.name, frameTrafos,
                                  tuple(v for v in frame.RobotEditor.dynamics.inertiaTensor),
                                  frame.RobotEditor.dynamics.mass, collisionModels,
                                  collisionModelTransformations)

        handler.write(self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
        return {'FINISHED'}
