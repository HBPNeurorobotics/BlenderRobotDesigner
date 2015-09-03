from bpy.props import *
from . import armatures

def draw(layout, context):
    if not armatures.checkArmature(layout,context):
        return
    if context.active_bone is not None:

        column = layout.column(align=True)
        column.label("Active Bone:")
        column.menu("roboteditor.bonemenu", text=context.active_bone.name)
        column.separator()
        column.prop(context.active_bone.RobotEditor.controller, "maxVelocity")
        column.prop(context.active_bone.RobotEditor.controller, "maxTorque")
        column.prop(context.active_bone.RobotEditor.controller, "acceleration")
        column.prop(context.active_bone.RobotEditor.controller, "deceleration")
        column.prop(context.active_bone.RobotEditor.controller, "isActive")
        column.label("Joint Limits:")
        if context.active_bone.RobotEditor.jointMode == 'REVOLUTE':
            column.prop(context.active_bone.RobotEditor.theta, "min")
            column.prop(context.active_bone.RobotEditor.theta, "max")
        else:
            column.prop(context.active_bone.RobotEditor.d, "min")
            column.prop(context.active_bone.RobotEditor.d, "max")

        column.separator()
        column.label("Joint controller:")
        column.prop(context.active_bone.RobotEditor.jointController, "isActive")
        column.prop(context.active_bone.RobotEditor.jointController, "controllerType")
        column.separator()
        column.prop(context.active_bone.RobotEditor.jointController, "P")
        column.prop(context.active_bone.RobotEditor.jointController, "I")
        column.prop(context.active_bone.RobotEditor.jointController, "D")