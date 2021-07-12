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

import bpy
from mathutils import Euler, Matrix, Quaternion, Vector
from bpy.props import StringProperty

from math import *
from . import collada as c, fix, armatures

import xml.etree.cElementTree as etree

try:
    from . import simox

    use_simox = False
except ImportError:
    use_simox = False

try:
    from . import mmm

    use_mmm = False
except ImportError:
    use_mmm = False


def parseTree(tree, parentName):
    # print("parsetree")
    armName = bpy.context.active_object.name
    armatures.createBone(armName, tree.name, parentName)
    bpy.ops.RobotDesigner.select_segment(segment_name=tree.name)
    # print(tree.name)
    boneProp = bpy.context.active_bone.RobotDesigner

    m = Matrix()
    # print(tree.transformations)
    for i in tree.transformations:
        # We expect a matrix here!
        # Todo accept rotation and translations too!
        if type(i[0]) is list:
            m = m * Matrix(i)
        elif len(i) == 3:
            # TODO
            pass
        elif len(i) == 4:
            # TODO
            pass
        else:
            raise Exception("ParsingError")
            # print(m)

    bpy.context.active_bone.RobotDesigner.Euler.x.value = m.translation[0] / 1000
    bpy.context.active_bone.RobotDesigner.Euler.y.value = m.translation[1] / 1000
    bpy.context.active_bone.RobotDesigner.Euler.z.value = m.translation[2] / 1000

    bpy.context.active_bone.RobotDesigner.Euler.gamma.value = degrees(m.to_euler().z)
    bpy.context.active_bone.RobotDesigner.Euler.beta.value = degrees(m.to_euler().y)
    bpy.context.active_bone.RobotDesigner.Euler.alpha.value = degrees(m.to_euler().x)

    if tree.axis_type == 'revolute':
        bpy.context.active_bone.RobotDesigner.jointMode = 'REVOLUTE'
        # boneProp.theta.value = float(tree.initalValue)
        bpy.context.active_bone.RobotDesigner.theta.max = float(tree.max)
        bpy.context.active_bone.RobotDesigner.theta.min = float(tree.min)
    else:
        bpy.context.active_bone.RobotDesigner.jointMode = 'PRISMATIC'
        # boneProp.d.value = float(tree.initialValue)
        bpy.context.active_bone.RobotDesigner.d.max = float(tree.max)
        bpy.context.active_bone.RobotDesigner.d.min = float(tree.min)

    if tree.axis is not None:
        for i, axis in enumerate(tree.axis):
            if axis == -1.0:
                bpy.context.active_bone.RobotDesigner.axis_revert = True
                tree.axis[i] = 1.0

        if tree.axis == [1.0, 0.0, 0.0]:
            bpy.context.active_bone.RobotDesigner.axis = 'X'
        elif tree.axis == [0.0, 1.0, 0.0]:
            bpy.context.active_bone.RobotDesigner.axis = 'Y'
        elif tree.axis == [0.0, 0.0, 1.0]:
            bpy.context.active_bone.RobotDesigner.axis = 'Z'
    # print("parsetree done")

    for child in tree.children:
        parseTree(child, tree.name)


# operator to import an MMM-Motion
class RobotDesigner_importMMM(bpy.types.Operator):
    bl_idname = "RobotDesigner.mmmimport"
    bl_label = "Import MMM"
    filepath = StringProperty(subtype='FILE_PATH')

    def execute(self, context):
        mmm.read(self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def draw(layout, context):
    layout.operator("RobotDesigner.colladaexport")
    layout.operator("RobotDesigner.mmmimport")


# operator to import the kinematics in a SIMOX-XML file
class RobotDesigner_importSIMOX(bpy.types.Operator):
    bl_idname = "RobotDesigner.simoximport"
    bl_label = "Import SIMOX XML"
    filepath = StringProperty(subtype='FILE_PATH')

    def execute(self, context):
        tree = simox.read(self.filepath)
        parseTree(tree, None)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
