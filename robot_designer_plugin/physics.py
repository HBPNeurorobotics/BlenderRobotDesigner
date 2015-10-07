# Blender-specific imports (catch exception for sphinx documentation)
import bpy
from mathutils import Euler, Matrix, Quaternion, Vector
from bpy.props import *
from . import armatures


# operator to create physics frame
class RobotEditor_createPhysicsFrame(bpy.types.Operator):
    bl_idname = "roboteditor.createphysicsframe"
    bl_label = "Create Physics Frame"

    frameName = StringProperty()

    def execute(self, context):
        armName = context.active_object.name
        bpy.ops.object.empty_add(type='PLAIN_AXES')
        context.active_object.name = self.frameName
        context.active_object.RobotEditor.tag = 'PHYSICS_FRAME'

        bpy.ops.roboteditor.selectphysicsframe(frameName=self.frameName)
        bpy.ops.roboteditor.selectarmature(armatureName=armName)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


# operator to select a physics frame
class RobotEditor_selectPhysicsFrame(bpy.types.Operator):
    bl_idname = "roboteditor.selectphysicsframe"
    bl_label = "Select Physics Frame"

    frameName = StringProperty()

    def execute(self, context):
        arm = context.active_object
        context.scene.RobotEditor.physicsFrameName = self.frameName

        frame = bpy.data.objects[self.frameName]

        for obj in bpy.data.objects:
            obj.select = False

        frame.select = True
        arm.select = True

        context.scene.objects.active = arm

        return {'FINISHED'}


# dynamic menu to select physics frame
class RobotEditor_physicsFrameMenu(bpy.types.Menu):
    bl_idname = "roboteditor.physicsframemenu"
    bl_label = "SelectPhysics Frame"

    def draw(self, context):
        layout = self.layout
        frameNames = [f.name for f in bpy.data.objects if f.RobotEditor.tag == 'PHYSICS_FRAME']

        for frame in sorted(frameNames, key=str.lower):
            if bpy.data.objects[frame].parent_bone:
                text = frame + " --> " + bpy.data.objects[frame].parent_bone
            else:
                text = frame

            layout.operator("roboteditor.selectphysicsframe", text=text).frameName = frame


# operator to assign selected physics frame to active bone
class RobotEditor_assignPhysicsFrame(bpy.types.Operator):
    bl_idname = "roboteditor.assignphysicsframe"
    bl_label = "Assign selected physics frame to active bone"

    def execute(self, context):
        bpy.ops.object.parent_set(type='BONE')

        if bpy.context.active_bone.parent:
            to_parent_matrix = bpy.context.active_bone.parent.matrix_local
        else:
            to_parent_matrix = Matrix()
        from_parent_matrix, bone_matrix = bpy.context.active_bone.RobotEditor.getTransform()
        armature_matrix = bpy.context.active_object.matrix_basis

        # find selected physics frame
        for ob in bpy.data.objects:
            if ob.select and ob.RobotEditor.tag == 'PHYSICS_FRAME':
                frame = ob
                print(frame.name)

        # frame.matrix_basis = armature_matrix*to_parent_matrix*from_parent_matrix*bone_matrix
        # frame.matrix_basis = parent_matrix*armature_matrix*bone_matrix
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


# operator to generate collision meshes for all assigned physics frames


# operator to unassign selected physics frame
class RobotEditor_unassignPhysicsFrame(bpy.types.Operator):
    bl_idname = "roboteditor.unassignphysicsframe"
    bl_label = "Unassign selected physics frame"

    def execute(self, context):
        currentFrame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]
        physNode_global = currentFrame.matrix_world
        currentFrame.parent = None
        currentFrame.matrix_world = physNode_global
        return {'FINISHED'}


# draws the layout part of the physics frame submenu
def draw(layout, context):
    if not armatures.checkArmature(layout, context):
        return
    layout.operator("roboteditor.createphysicsframe")
    layout.label("Select Physics Frame:")
    topRow = layout.column(align=False)
    frameMenuText = ""
    if context.active_bone and not context.scene.RobotEditor.physicsFrameName == "":
        if context.scene.RobotEditor.physicsFrameName in bpy.data.objects:
            frame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]

            if frame.parent_bone:
                frameMenuText = context.scene.RobotEditor.physicsFrameName + " --> " + frame.parent_bone
            else:
                frameMenuText = context.scene.RobotEditor.physicsFrameName

    topRow.menu("roboteditor.physicsframemenu", text=frameMenuText)
    topRow.operator("roboteditor.unassignphysicsframe")

    if context.scene.RobotEditor.physicsFrameName is not "":
        frame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]
        layout.prop(frame.RobotEditor.dynamics, "mass")
        layout.separator()
        layout.prop(frame.RobotEditor.dynamics, "inertiaTensor")

    layout.label("Select Bone:")
    lowerRow = layout.column(align=False)
    lowerRow.menu("roboteditor.bonemenu", text=context.active_bone.name)
    lowerRow.operator("roboteditor.assignphysicsframe")
    # TODO: Fix faulty collision mesh generation
    lowerRow = layout.row(align=False)
    layout.label("Collision Meshes:")
    lowerRow = layout.row(align=False)


def register():
    bpy.utils.register_class(RobotEditor_createPhysicsFrame)
    bpy.utils.register_class(RobotEditor_selectPhysicsFrame)
    bpy.utils.register_class(RobotEditor_physicsFrameMenu)
    bpy.utils.register_class(RobotEditor_assignPhysicsFrame)
    bpy.utils.register_class(RobotEditor_unassignPhysicsFrame)


def unregister():
    bpy.utils.unregister_class(RobotEditor_createPhysicsFrame)
    bpy.utils.unregister_class(RobotEditor_selectPhysicsFrame)
    bpy.utils.unregister_class(RobotEditor_physicsFrameMenu)
    bpy.utils.unregister_class(RobotEditor_assignPhysicsFrame)
    bpy.utils.unregister_class(RobotEditor_unassignPhysicsFrame)
