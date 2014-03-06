import bpy
from bpy.props import *
from . import armatures

# operator to create new bone
class RobotEditor_createBone(bpy.types.Operator):
    bl_idname = "roboteditor.createbone"
    bl_label = "Create new Bone"
    
    boneName = StringProperty(name="Enter new bone name:")
    
    def execute(self, context):
        try:
            parentBoneName = context.active_bone.name
        except:
            parentBoneName = None
        
        if not context.active_object.type == 'ARMATURE':
            raise Exception("BoneCreationException")
            #return{'FINISHED'}
        arm = context.active_object    
        armatures.createBone(arm.name, self.boneName, parentBoneName)
        
        bpy.ops.roboteditor.selectbone(boneName = self.boneName)
        armatures.updateKinematics(arm.name,self.boneName)
        
        #TODO: set parentMode according to own parent
        return{'FINISHED'}   

    def invoke(self, context, event) :
        return context.window_manager.invoke_props_dialog(self)
        
        
# operator to select a bone       
class RobotEditor_selectBone(bpy.types.Operator):
    bl_idname = "roboteditor.selectbone"
    bl_label = "Select Bone"
    
    boneName = StringProperty()
    
    def execute(self, context):
        if not context.active_object.type == 'ARMATURE':
            raise Exception("BoneSelectionException")
        
        arm = bpy.context.active_object
        arm.data.bones.active = arm.data.bones[self.boneName]
        
        for b in arm.data.bones:
            b.select = False
        
        
        arm.data.bones.active.select = True
        return{'FINISHED'}

# Dynamic menu to select bone       
class RobotEditor_BoneMenu(bpy.types.Menu):
    bl_idname = "roboteditor.bonemenu"
    bl_label = "Select Bone"
    
    def draw(self, context) :
        currentArm = context.active_object
        
        layout = self.layout
        bones = currentArm.data.bones
        
        for bone in bones:
            text = bone.name
            layout.operator("roboteditor.selectbone", text=text).boneName = text


# operator to rename active bone
class RobotEditor_renameBone(bpy.types.Operator):
    bl_idname = "roboteditor.renamebone"
    bl_label = "Rename active Bone"
    
    newName = StringProperty(name = "Enter new name:")
    
    def execute(self, context):
        context.active_bone.name = self.newName
        return{'FINISHED'}
        
    def invoke(self, context, event) :
        return context.window_manager.invoke_props_dialog(self) 

        
        
# operator to create new parent bone for the current active bone       
class RobotEditor_createParentBone(bpy.types.Operator):
    bl_idname = "roboteditor.createparentbone"
    bl_label = "Create new parent Bone"
    
    boneName = StringProperty(name = "Enter new parent bone name:")
    
    def execute(self, context):
        currentBone = context.active_bone
        currentBoneName = currentBone.name
        
        bpy.ops.roboteditor.createbone(boneName = self.boneName)
        
        # rearrange parent pointers accordingly in edit mode
        currentMode = context.object.mode
        
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        
        newEditBone = context.active_bone
        if not currentBone.parent is None:
            oldParentName = currentBone.parent.name
            oldParentEditBone = context.active_object.data.edit_bones[oldParentName]
        else:
            oldParentEditBone = None
            
        newEditBone.parent = oldParentEditBone
        
        currentEditBone = context.active_object.data.edit_bones[currentBoneName]
        currentEditBone.parent = newEditBone
        
        bpy.ops.object.mode_set(mode=currentMode, toggle=False)
        
        armatures.updateKinematics(context.active_object.name, self.boneName)
        
        return{'FINISHED'}
        
    def invoke(self, context, even):
        return context.window_manager.invoke_props_dialog(self)
        
# operator to assign parent to bone
class RobotEditor_assignParentBone(bpy.types.Operator):
    bl_idname = "roboteditor.assignparentbone"
    bl_label = "Assign parent bone"
    
    parentName = StringProperty()
    
    def execute(self, context):
        arm = context.active_object
        currentBoneName = context.active_bone.name
        
        currentMode = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='EDIT',toggle=False)
        newParentEditBone = arm.data.edit_bones[self.parentName]
        currentEditBone = arm.data.edit_bones[currentBoneName]
        currentEditBone.parent = newParentEditBone
        bpy.ops.object.mode_set(mode=currentMode, toggle=False)
        
        armatures.updateKinematics(context.active_object.name, currentBoneName)
        return{'FINISHED'}
 
 
# dynmic menu for assigning parent bones
class RobotEditor_AssignParentMenu(bpy.types.Menu):
    bl_idname = "roboteditor.assignparentbonemenu"
    bl_label = "Assign parent to bone"
    
    def draw(self, context):
        arm = context.active_object
        currentBone = context.active_bone
        
        # can't parent to self or own children
        disallowedBones = currentBone.children_recursive
        disallowedBones.append(currentBone)
        bones = [bone for bone in arm.data.bones if not bone in disallowedBones]
        
        layout = self.layout
        
        layout.operator("roboteditor.createparentbone", text="New...")
        
        for bone in bones:
            text = bone.name
            if bone.name == currentBone.parent.name :
                text = text + " <-- Parent"
            layout.operator("roboteditor.assignparentbone", text=text).parentName = bone.name


# operator to delete bone and ALL of its children
class RobotEditor_deleteBone(bpy.types.Operator):
    bl_idname = "roboteditor.deletebone"
    bl_label = "Delete Bone and ALL its children"
    
    confirmation = BoolProperty(name="Are you sure?")
    
    def execute(self, context):
        if self.confirmation:
            arm = context.active_object.data
        
            currentMode = context.object.mode
            bpy.ops.object.mode_set(mode='EDIT', toggle = False)
            for bone in context.active_object.data.edit_bones:
                bone.select = False
            
            for bone in context.active_bone.children_recursive:
                bone.select = True
        
            context.active_bone.select = True
            
            if not context.active_bone.parent is None:
                parentName = context.active_bone.parent.name
            else:
                parentName = None
        
            bpy.ops.armature.delete()
            bpy.ops.object.mode_set(mode=currentMode, toggle = False)
            
            if not parentName is None:
                bpy.ops.roboteditor.selectbone(boneName = parentName)
        return{'FINISHED'}
        
    def invoke(self,context,event) :
        return context.window_manager.invoke_props_dialog(self)
        
# draw method that builds the part of the GUI responsible for the bone submenu        
def draw(layout, context):
    #layout.label("Active Bone:")
    if not context.active_bone is None:
        
        if not context.active_bone.parent is None:
            activeBoneParentName = context.active_bone.parent.name
        else:
            activeBoneParentName = ""
            
        row = layout.row(align=True)
        leftColumn = row.column(align=True)
        leftColumn.label("Active Bone:")
        leftColumn.menu("roboteditor.bonemenu", text = context.active_bone.name)
        leftColumn.separator()
        leftColumn.prop(context.scene.RobotEditor,"boneLength", slider = False)
        leftColumn.separator()
        leftColumn.label("Select parent:")
        leftColumn.menu("roboteditor.assignparentbonemenu",text = activeBoneParentName)
        
        row.separator()
        
        rightColumn = row.column(align=False)
        rightColumn.label("")
        rightColumn.operator("roboteditor.renamebone")
        rightColumn.operator("roboteditor.createbone", text="Create new child Bone")
        rightColumn.operator("roboteditor.createparentbone", text="Create new Parent Bone")
        rightColumn.separator()
        rightColumn.operator("roboteditor.deletebone", text="Delect active Bone")
        
        layout.label("Parent Mode:")
        layout.prop(context.active_bone.RobotEditor,"parentMode", expand=True)
        parentModeColumn = layout.column(align=True)
        
        if(context.active_bone.RobotEditor.parentMode == 'EULER'):
            parentModeColumn.label("Euler position:")
            parentModeColumn.prop(context.active_bone.RobotEditor.Euler.x,"value", slider=False, text="x")
            parentModeColumn.prop(context.active_bone.RobotEditor.Euler.y,"value", slider=False, text="y")
            parentModeColumn.prop(context.active_bone.RobotEditor.Euler.z,"value", slider=False, text="z")
            parentModeColumn.separator()
            parentModeColumn.label("Euler rotation in xy'z''")
            parentModeColumn.prop(context.active_bone.RobotEditor.Euler.alpha,"value", slider=False, text="alpha")
            parentModeColumn.prop(context.active_bone.RobotEditor.Euler.beta,"value", slider=False, text="beta")
            parentModeColumn.prop(context.active_bone.RobotEditor.Euler.gamma,"value", slider=False, text="gamma")
        else: #parentMode == 'DH'
            parentModeColumn.label("DH parameter:")
            parentModeColumn.prop(context.active_bone.RobotEditor.DH.theta,"value",slider=False,text="theta")
            parentModeColumn.prop(context.active_bone.RobotEditor.DH.d,"value",slider=False,text="d")
            parentModeColumn.prop(context.active_bone.RobotEditor.DH.alpha,"value",slider=False,text="alpha")
            parentModeColumn.prop(context.active_bone.RobotEditor.DH.a,"value",slider=False,text="a")
        
        layout.label("Actice Axis:")
        axisRow = layout.row()
        axisRow.prop(context.active_bone.RobotEditor,"axis", expand=True)
        axisRow.prop(context.active_bone.RobotEditor,"axis_revert")
        
        layout.label("Joint Type:")
        layout.prop(context.active_bone.RobotEditor,"jointMode", expand=True)
        jointTypeColumn = layout.column(align=True)
        
        if(context.active_bone.RobotEditor.jointMode == 'REVOLUTE'):
            jointTypeColumn.label("theta:")
            jointTypeColumn.prop(context.active_bone.RobotEditor.theta,"value",slider=False)
            jointTypeColumn.prop(context.active_bone.RobotEditor.theta,"offset",slider=False)
            jointTypeColumn.prop(context.active_bone.RobotEditor.theta,"min",slider=False)
            jointTypeColumn.prop(context.active_bone.RobotEditor.theta,"max",slider=False)
        else: #jointMode == 'PRISMATIC'
            jointTypeColumn.label("d:")
            jointTypeColumn.prop(context.active_bone.RobotEditor.d,"value",slider=False)
            jointTypeColumn.prop(context.active_bone.RobotEditor.d,"offset",slider=False)
            jointTypeColumn.prop(context.active_bone.RobotEditor.d,"min",slider=False)
            jointTypeColumn.prop(context.active_bone.RobotEditor.d,"max",slider=False)            
    else:
        layout.operator("roboteditor.createbone",text="Create new base bone")
        
def register():
    bpy.utils.register_class(RobotEditor_createBone)
    bpy.utils.register_class(RobotEditor_selectBone)
    bpy.utils.register_class(RobotEditor_BoneMenu)
    bpy.utils.register_class(RobotEditor_renameBone)
    bpy.utils.register_class(RobotEditor_createParentBone)
    bpy.utils.register_class(RobotEditor_assignParentBone)
    bpy.utils.register_class(RobotEditor_AssignParentMenu)
    bpy.utils.register_class(RobotEditor_deleteBone)
    
def unregister():
    bpy.utils.unregister_class(RobotEditor_createBone)
    bpy.utils.unregister_class(RobotEditor_selectBone)
    bpy.utils.unregister_class(RobotEditor_BoneMenu)
    bpy.utils.unregister_class(RobotEditor_renameBone)
    bpy.utils.unregister_class(RobotEditor_createParentBone)
    bpy.utils.unregister_class(RobotEditor_assignParentBone)
    bpy.utils.unregister_class(RobotEditor_AssignParentMenu)
    bpy.utils.unregister_class(RobotEditor_deleteBone)