import bpy
from . import armatures, bones, meshes, markers, physics, files, controllers


class RobotEditor_UserInterface(bpy.types.Panel):
    bl_label = "RobotEditor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        layout = self.layout
        if armatures.draw(layout, context):
            # armature selected!
            layout.separator()
            layout.prop(bpy.context.scene.RobotEditor,"controlEnum", expand=True)
            control = context.scene.RobotEditor.controlEnum
            
            if control == 'bones':
                bones.draw(layout, context)
            elif control == 'meshes':
                meshes.draw(layout, context)
            elif control == 'markers':
                markers.draw(layout, context)
            elif control == 'physics':
                physics.draw(layout, context)
            elif control == 'controller':
                controllers.draw(layout, context)
            elif control == 'files':
                files.draw(layout, context)
                
        #layout.prop(bpy.context.scene.RobotEditor,"controlEnum", expand=True)

# initialize all RobotEditor properties
def init():
    bpy.types.Bone.RobotEditor = bpy.props.PointerProperty(type=bpy.types.RobotEditor_BoneProperty)
    bpy.types.Object.RobotEditor = bpy.props.PointerProperty(type=bpy.types.RobotEditor_Properties)
    bpy.types.Scene.RobotEditor = bpy.props.PointerProperty(type=bpy.types.RobotEditor_Globals)

def register():
    bpy.utils.register_class(RobotEditor_UserInterface)
    
def unregister():
    bpy.utils.unregister_class(RobotEditor_UserInterface)
