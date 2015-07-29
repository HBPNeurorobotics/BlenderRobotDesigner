# Blender-specific imports (catch exception for sphinx documentation)
import bpy
from bpy.props import *

from . import armatures, bones, meshes, markers, physics, files, controllers


# operator to print transformation matrix from active object to all selected objects
class RobotEditor_printTransformations(bpy.types.Operator):
    bl_idname = "roboteditor.printtransformations"
    bl_label = "Print transformation matrix from active object to all selected objects"

    def execute(self, context):
        active_object = bpy.context.active_object

        for ob in [obj for obj in bpy.data.objects if obj.select]:
            print('Transformation from %(from)s to %(to)s:' % {'from': active_object.name, 'to': ob.name})
            transform = active_object.matrix_world.inverted() * ob.matrix_world
            print(transform)

        return {'FINISHED'}


class RobotEditor_UserInterface(bpy.types.Panel):
    bl_label = "NRP Robot Designer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        layout = self.layout
        layout.operator("roboteditor.printtransformations")
        if armatures.draw(layout, context):
            # armature selected!
            layout.separator()
            layout.prop(bpy.context.scene.RobotEditor, "controlEnum", expand=True)
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

                # layout.prop(bpy.context.scene.RobotEditor,"controlEnum", expand=True)


# initialize all RobotEditor properties
def init():
    bpy.types.Bone.RobotEditor = bpy.props.PointerProperty(type=bpy.types.RobotEditor_BoneProperty)
    bpy.types.Object.RobotEditor = bpy.props.PointerProperty(type=bpy.types.RobotEditor_Properties)
    bpy.types.Scene.RobotEditor = bpy.props.PointerProperty(type=bpy.types.RobotEditor_Globals)


def register():
    bpy.utils.register_class(RobotEditor_printTransformations)
    bpy.utils.register_class(RobotEditor_UserInterface)


def unregister():
    bpy.utils.unregister_class(RobotEditor_printTransformations)
    bpy.utils.unregister_class(RobotEditor_UserInterface)
