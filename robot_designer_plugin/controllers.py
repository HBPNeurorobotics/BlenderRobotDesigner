from bpy.props import *
from . import armatures
from .tools import collapsible


def draw(layout, context):
    if not armatures.checkArmature(layout, context):
        return
    if context.active_bone is not None:

        box = layout.box()
        if collapsible(box, context, 'collapseControllerLimits', 'Limits'):
            # column.label("Active Bone:")
            # column.menu("roboteditor.bonemenu", text=context.active_bone.name)
            # column.separator()
            box.prop(context.active_bone.RobotEditor.controller, "maxVelocity")
            box.prop(context.active_bone.RobotEditor.controller, "maxTorque")
            box.prop(context.active_bone.RobotEditor.controller, "acceleration")
            box.prop(context.active_bone.RobotEditor.controller, "deceleration")
            box.prop(context.active_bone.RobotEditor.controller, "isActive")
            box.label("Joint Limits:")
            if context.active_bone.RobotEditor.jointMode == 'REVOLUTE':
                box.prop(context.active_bone.RobotEditor.theta, "min")
                box.prop(context.active_bone.RobotEditor.theta, "max")
            else:
                box.prop(context.active_bone.RobotEditor.d, "min")
                box.prop(context.active_bone.RobotEditor.d, "max")

        layout.separator()
        box = layout.box()

        if collapsible(box, context, 'collapseController', 'Controller'):
            box.label("Joint controller:")
            box.prop(context.active_bone.RobotEditor.jointController, "isActive")
            box.prop(context.active_bone.RobotEditor.jointController, "controllerType")
            box.separator()
            box.prop(context.active_bone.RobotEditor.jointController, "P")
            box.prop(context.active_bone.RobotEditor.jointController, "I")
            box.prop(context.active_bone.RobotEditor.jointController, "D")
