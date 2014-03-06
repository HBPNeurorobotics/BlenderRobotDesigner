import bpy
from bpy.props import *


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
        
        bpy.ops.roboteditor.selectphysicsframe(frameName = self.frameName)
        bpy.ops.roboteditor.selectarmature(armatureName = armName)
        
        return{'FINISHED'}

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
        
        return{'FINISHED'}
            
# dynamic menu to select physics frame
class RobotEditor_physicsFrameMenu(bpy.types.Menu):
    bl_idname = "roboteditor.physicsframemenu"
    bl_label = "SelectPhysics Frame"
    
    def draw(self, context):
        layout = self.layout
        frames = [f for f in bpy.data.objects if f.RobotEditor.tag == 'PHYSICS_FRAME']
        
        for frame in frames:
            if frame.parent_bone:
                text = frame.name + " --> " + frame.parent_bone
            else:
                text = frame.name
                
            layout.operator("roboteditor.selectphysicsframe", text=text).frameName=frame.name


# operator to assign selected physics frame to active bone
class RobotEditor_assignPhysicsFrame(bpy.types.Operator):
    bl_idname = "roboteditor.assignphysicsframe"
    bl_label = "Assign selected physics frame to active bone"
    
    def execute(self, context):
        bpy.ops.object.parent_set(type = 'BONE')
        return{'FINISHED'}
        
        
# operator to unassign selected physics frame
class RobotEditor_unassignPhysicsFrame(bpy.types.Operator):
    bl_idname = "roboteditor.unassignphysicsframe"
    bl_label = "Unassign selected physics frame"
    
    def execute(self, context):
        currentFrame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]
        currentFrame.parent = None
        
        return{'FINISHED'}
        
            
# draws the layout part of the physics frame submenu
def draw(layout, context):
    layout.operator("roboteditor.createphysicsframe")
    layout.label("Select Physics Frame:")
    topRow = layout.row(align=False)
    frameMenuText = ""
    if(context.active_bone and not context.scene.RobotEditor.physicsFrameName == ""):
        frame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]
        
        if frame.parent_bone:
            frameMenuText = context.scene.RobotEditor.physicsFrameName + " --> " + frame.parent_bone
        else:
            frameMenuText = context.scene.RobotEditor.physicsFrameName
            
    topRow.menu("roboteditor.physicsframemenu", text = frameMenuText)
    topRow.operator("roboteditor.unassignphysicsframe")
    
    if not context.scene.RobotEditor.physicsFrameName is "":
        frame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]
        layout.prop(frame.RobotEditor.dynamics,"mass")
        layout.separator()
        layout.prop(frame.RobotEditor.dynamics,"inertiaTensor")
    
    layout.label("Select Bone:")
    lowerRow = layout.row(align=False)
    lowerRow.menu("roboteditor.bonemenu", text = context.active_bone.name)
    lowerRow.operator("roboteditor.assignphysicsframe")


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