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

from . import export


def parseTree(tree, parentName):
    # print("parsetree")
    armName = bpy.context.active_object.name
    armatures.createBone(armName, tree.name, parentName)
    bpy.ops.roboteditor.select_segment(segment_name=tree.name)
    # print(tree.name)
    boneProp = bpy.context.active_bone.RobotEditor

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

    bpy.context.active_bone.RobotEditor.Euler.x.value = m.translation[0] / 1000
    bpy.context.active_bone.RobotEditor.Euler.y.value = m.translation[1] / 1000
    bpy.context.active_bone.RobotEditor.Euler.z.value = m.translation[2] / 1000

    bpy.context.active_bone.RobotEditor.Euler.gamma.value = degrees(m.to_euler().z)
    bpy.context.active_bone.RobotEditor.Euler.beta.value = degrees(m.to_euler().y)
    bpy.context.active_bone.RobotEditor.Euler.alpha.value = degrees(m.to_euler().x)

    if tree.axis_type == 'revolute':
        bpy.context.active_bone.RobotEditor.jointMode = 'REVOLUTE'
        # boneProp.theta.value = float(tree.initalValue)
        bpy.context.active_bone.RobotEditor.theta.max = float(tree.max)
        bpy.context.active_bone.RobotEditor.theta.min = float(tree.min)
    else:
        bpy.context.active_bone.RobotEditor.jointMode = 'PRISMATIC'
        # boneProp.d.value = float(tree.initialValue)
        bpy.context.active_bone.RobotEditor.d.max = float(tree.max)
        bpy.context.active_bone.RobotEditor.d.min = float(tree.min)

    if tree.axis is not None:
        for i, axis in enumerate(tree.axis):
            if axis == -1.0:
                bpy.context.active_bone.RobotEditor.axis_revert = True
                tree.axis[i] = 1.0

        if tree.axis == [1.0, 0.0, 0.0]:
            bpy.context.active_bone.RobotEditor.axis = 'X'
        elif tree.axis == [0.0, 1.0, 0.0]:
            bpy.context.active_bone.RobotEditor.axis = 'Y'
        elif tree.axis == [0.0, 0.0, 1.0]:
            bpy.context.active_bone.RobotEditor.axis = 'Z'
    # print("parsetree done")

    for child in tree.children:
        parseTree(child, tree.name)






# operator to import an MMM-Motion
class RobotEditor_importMMM(bpy.types.Operator):
    bl_idname = "roboteditor.mmmimport"
    bl_label = "Import MMM"
    filepath = StringProperty(subtype='FILE_PATH')

    def execute(self, context):
        mmm.read(self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def draw(layout, context):
    layout.operator("roboteditor.colladaexport")
    layout.operator("roboteditor.mmmimport")


# operator to import the kinematics in a SIMOX-XML file
class RobotEditor_importSIMOX(bpy.types.Operator):
    bl_idname = "roboteditor.simoximport"
    bl_label = "Import SIMOX XML"
    filepath = StringProperty(subtype='FILE_PATH')

    def execute(self, context):
        tree = simox.read(self.filepath)
        parseTree(tree, None)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}






