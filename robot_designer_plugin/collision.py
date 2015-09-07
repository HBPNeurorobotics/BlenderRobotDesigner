__author__ = 'ulbrich'

import bpy
from bpy.props import *
from .tools import meshSelector

import logging

logger = logging.getLogger('Meshes')
logger.setLevel(logging.DEBUG)

def create_collision_mesh(context, target):
    """

    :param context: The bpy.context object
    :param target: The name of the mesh
    :return: string
    """



class RobotEditor_generateAllCollisionMeshes(bpy.types.Operator):
    bl_idname = "roboteditor.generatallecollisionmeshes"
    bl_label = "Generate All Collision Meshes"

    def execute(self, context):

        visuals = [o.name for o in bpy.data.objects if o.type == 'MESH'
                   and o.parent == context.active_object and o.RobotEditor.tag != "COLLISION"]

        logger.debug("Visuals: %s", visuals)

        for i in visuals:
            bpy.ops.roboteditor.generatecollisionmesh(target=i)

        return {'FINISHED'}

class RobotEditor_SettingsDialog(bpy.types.Operator):
    bl_idname ="roboteditor.collisiondialog"
    bl_label = "Settings for creating collision meshes"

    levels = bpy.props.FloatProperty(name='Levels')
    offset = bpy.props.FloatProperty(name='Offset')

    def execute(self, context):
        # context.scene.RobotEditor.subdivisionLevels = self.levels
        # context.scene.RobotEditor.shrinkWrapOffset = self.offset

        return {'FINISHED'}

    def invoke(self,context,event):
        # self.levels = context.scene.RobotEditor.subdivisionLevels
        # self.offset = context.scene.RobotEditor.shrinkWrapOffset
        return context.window_manager.invoke_props_dialog(self)

class RobotEditor_generateCollisionMesh(bpy.types.Operator):
    """
    Operator that creates a collision mesh using the builtin subdivide and shrinkwrap operators.
    """
    bl_idname = "roboteditor.generatecollisionmesh"
    bl_label = "Generate Collision Mesh for selected"

    target = StringProperty()

    def execute(self, context):
        """
        Executes the operator.

        :param context: Blender context object
        :return:
        """
        #bpy.ops.roboteditor.collisiondialog('INVOKE_DEFAULT')

        logger.debug("Creating Collision mesh for: %s", self.target)
        armature = context.active_object.name

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active= bpy.data.objects[self.target]

        d = bpy.data.objects[self.target].dimensions
        bpy.ops.mesh.primitive_cube_add(location=bpy.data.objects[self.target].location,
                                        rotation=bpy.data.objects[self.target].rotation_euler)
        offset = bpy.context.scene.RobotEditor.shrinkWrapOffset
        bpy.context.object.dimensions = d*100
        bpy.ops.object.transform_apply(scale=True)
        mod = bpy.context.object.modifiers.new(name='subsurf', type='SUBSURF')
        mod.subdivision_type = 'SIMPLE'
        mod.levels = bpy.context.scene.RobotEditor.subdivisionLevels
        bpy.ops.object.modifier_apply(modifier='subsurf')
        mod = bpy.context.object.modifiers.new(name='shrink_wrap', type='SHRINKWRAP')
        mod.wrap_method = "NEAREST_SURFACEPOINT"
        mod.offset = bpy.context.scene.RobotEditor.shrinkWrapOffset
        logger.debug("%f, %f", mod.offset, bpy.context.scene.RobotEditor.shrinkWrapOffset)
        mod.target = bpy.data.objects[self.target]
        bpy.ops.object.modifier_apply(modifier='shrink_wrap')

        bpy.context.object.name = 'COL_' + self.target
        name = bpy.context.object.name

        context.active_object.RobotEditor.tag = 'COLLISION'
        logger.debug("Created mesh: %s", bpy.context.active_object.name)

        if 'RD_COLLISON_OBJECT_MATERIAL' in bpy.data.materials:
            bpy.ops.object.material_slot_add()
            context.active_object.data.materials[0] = bpy.data.materials['RD_COLLISON_OBJECT_MATERIAL']
            logger.debug("Assigned material to : %s", bpy.context.active_object.name)
        else:
            logger.debug("Could not find material for collision mesh")

        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.roboteditor.selectarmature(armatureName=armature)
        bpy.ops.roboteditor.selectbone(boneName=bpy.data.objects[self.target].parent_bone)
        bpy.data.objects[name].select = True
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.roboteditor.selectarmature(armatureName=armature)

        return {'FINISHED'}


# class RobotEditor_assignCollisionModel(bpy.types.Operator):
#     bl_idname = "roboteditor.assigncollisionmodel"
#     bl_label = "Assign selected mesh as collision model to physics frame."
#
#     def execute(self, context):
#         bpy.ops.object.select_all(action="DESELECT")
#         if context.scene.RobotEditor.meshName in bpy.data.objects:
#             bpy.data.objects[context.scene.RobotEditor.meshName].select = True
#             if context.scene.RobotEditor.physicsFrameName in bpy.data.objects:
#                 context.scene.objects.active = bpy.data.objects[
#                     context.scene.RobotEditor.physicsFrameName]
#                 bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
#
#         if context.scene.RobotEditor.armatureName in bpy.data.objects:
#             context.scene.objects.active = bpy.data.objects[context.scene.RobotEditor.armatureName]
#         return {'FINISHED'}


def draw(layout,context):
    row = layout.row()
    column = row.column()
    meshSelector(column, context)
    column = row.column()
    column.operator("roboteditor.generatallecollisionmeshes")
    if context.scene.RobotEditor.meshName != "":
        column.operator("roboteditor.generatecollisionmesh").target = context.scene.RobotEditor.meshName
    column.prop(context.scene.RobotEditor, "subdivisionLevels")
    column.prop(context.scene.RobotEditor, "shrinkWrapOffset")
    row = layout.row()


def register():
    #bpy.utils.register_class(RobotEditor_assignCollisionModel)
    bpy.utils.register_class(RobotEditor_generateCollisionMesh)
    bpy.utils.register_class(RobotEditor_generateAllCollisionMeshes)
    #bpy.utils.register_class(RobotEditor_SettingsDialog)

def unregister():
    #bpy.utils.unregister_class(RobotEditor_assignCollisionModel)
    bpy.utils.unregister_class(RobotEditor_generateCollisionMesh)
    bpy.utils.unregister_class(RobotEditor_generateAllCollisionMeshes)
    #bpy.utils.unregister_class(RobotEditor_SettingsDialog)
