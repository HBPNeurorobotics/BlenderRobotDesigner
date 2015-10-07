# Blender-specific imports (catch exception for sphinx documentation)
import bpy
from bpy.props import *
from . import armatures, collision
from .tools import collapsible, boneSelector, meshSelector


def displayMeshes(self, context):
    hide_mesh = context.scene.RobotEditor.hideMeshType
    meshNames = [obj.name for obj in bpy.data.objects if
                 not obj.parent_bone is None and
                 obj.type == 'MESH']
    for mesh in meshNames:
        obj = bpy.data.objects[mesh]
        if hide_mesh == 'all':
            obj.hide = False
        elif hide_mesh == 'collision' and obj.RobotEditor.tag == 'COLLISION':
            obj.hide = False
        elif hide_mesh == 'visual' and obj.RobotEditor.tag == 'DEFAULT':
            obj.hide = False
        else:
            obj.hide = True


# operator to select mesh
class RobotEditor_selectMesh(bpy.types.Operator):
    bl_idname = "roboteditor.selectmesh"
    bl_label = "Select Mesh"

    meshName = StringProperty()

    def execute(self, context):
        context.scene.RobotEditor.meshName = self.meshName
        mesh = bpy.data.objects[self.meshName]
        arm = context.active_object

        for obj in bpy.data.objects:
            obj.select = False

        mesh.select = True
        arm.select = True

        return {'FINISHED'}


# dynamic menu to select mesh
class RobotEditor_boneMeshMenu(bpy.types.Menu):
    bl_idname = "roboteditor.bonemeshmenu"
    bl_label = "Select Bone"

    def draw(self, context):
        mesh_type = context.scene.RobotEditor.meshType
        hide_bone = context.scene.RobotEditor.listBones
        layout = self.layout

        currentArm = context.active_object
        boneNames = [bone.name for bone in currentArm.data.bones if
                     context.scene.RobotEditor.liveSearchBones in bone.name]
        meshes = {obj.parent_bone: obj.name for obj in bpy.data.objects if
                  not obj.parent_bone is None and
                  obj.type == 'MESH' and
                  obj.RobotEditor.tag == mesh_type}

        for bone in sorted(boneNames, key=str.lower):
            if bone in meshes:
                text = bone + " <-- " + meshes[bone]
                if hide_bone == 'disconnected':
                    continue
            # elif bpy.data.objects[mesh].parent:
            #    text = context.scene.RobotEditor.meshName + " --> " + bpy.data.objects[mesh].parent.name
            #    text = mesh + " --> " + bpy.data.objects[mesh].parent.name
            else:
                text = bone
                if hide_bone == 'connected':
                    continue
            layout.operator("roboteditor.selectbone", text=text).boneName = bone


# dynamic menu to select mesh
class RobotEditor_meshMenu(bpy.types.Menu):
    bl_idname = "roboteditor.meshmenu"
    bl_label = "Select Mesh"

    def draw(self, context):
        mesh_type = context.scene.RobotEditor.meshType
        hide_mesh = context.scene.RobotEditor.listMeshes
        layout = self.layout
        meshNames = [obj.name for obj in bpy.data.objects if
                     obj.type == 'MESH' and
                     obj.RobotEditor.tag == mesh_type and
                     context.scene.RobotEditor.liveSearchMeshes in obj.name]

        for mesh in meshNames:
            if bpy.data.objects[mesh].parent_bone:
                text = mesh + " --> " + bpy.data.objects[mesh].parent_bone
                if hide_mesh == 'disconnected':
                    continue
            # elif bpy.data.objects[mesh].parent:
            #    text = context.scene.RobotEditor.meshName + " --> " + bpy.data.objects[mesh].parent.name
            #    text = mesh + " --> " + bpy.data.objects[mesh].parent.name
            else:
                text = mesh
                if hide_mesh == 'connected':
                    continue
            layout.operator("roboteditor.selectmesh", text=text).meshName = mesh


# operator to assign mesh to bone
class RobotEditor_assignMesh(bpy.types.Operator):
    bl_idname = "roboteditor.assignmesh"
    bl_label = "Assign selected mesh to active bone"

    def execute(self, context):
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        return {'FINISHED'}


# operator to rename meshes using their parent bone's name
class RobotEditor_renameAllMeshes(bpy.types.Operator):
    bl_idname = "roboteditor.renamemeshes"
    bl_label = "Renames meshes after bones"

    def execute(self, context):
        currentMesh = bpy.data.objects[context.scene.RobotEditor.meshName]
        for i in bpy.data.objects:
            if i.parent_bone != '' and i.type == 'MESH':
                if i.name == currentMesh:
                    context.scene.RobotEditor.meshName = i.parent_bone
                i.name = 'Visualization_' + i.parent_bone

        return {'FINISHED'}


# operator to unassign mesh from bone
class RobotEditor_unassignMesh(bpy.types.Operator):
    bl_idname = "roboteditor.unassignmesh"
    bl_label = "Unassign selected mesh"

    def execute(self, context):
        currentMesh = bpy.data.objects[context.scene.RobotEditor.meshName]
        mesh_global = currentMesh.matrix_world
        currentMesh.parent = None
        currentMesh.matrix_world = mesh_global

        return {'FINISHED'}


# operator to unassign all meshes in the scene
class RobotEditor_unassignAllMeshes(bpy.types.Operator):
    bl_idname = "roboteditor.unassignallmeshes"
    bl_label = "Unassign ALL meshes"

    confirmation = BoolProperty(
        name="This disconnects all collision OR visual geometries from the model. Are you sure?")

    def execute(self, context):
        mesh_type = context.scene.RobotEditor.meshType
        if mesh_type == 'DEFAULT':
            meshes = [obj for obj in bpy.data.objects if
                      obj.type == 'MESH' and obj.parent_bone is not '' and obj.RobotEditor.tag != 'COLLISION']
        else:
            meshes = [obj for obj in bpy.data.objects if
                      obj.type == 'MESH' and obj.parent_bone is not '' and obj.RobotEditor.tag == 'COLLISION']

        if self.confirmation:
            for mesh in meshes:
                bpy.ops.roboteditor.selectmesh(meshName=mesh.name)
                bpy.ops.roboteditor.unassignmesh()

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class RobotEditor_setAllMeshesObject(bpy.types.Operator):
    bl_idname = "roboteditor.setallmeshesactiveobject"
    bl_label = "Select all geometry"

    def execute(self, context):
        mesh_type = context.scene.RobotEditor.meshType
        meshes = {obj.name for obj in bpy.data.objects if
                  not obj.parent_bone is None and
                  obj.type == 'MESH' and
                  obj.RobotEditor.tag == mesh_type}

        bpy.ops.object.select_all(action='DESELECT')

        for mesh in meshes:
            bpy.data.objects[mesh].select = True
            context.scene.objects.active = bpy.data.objects[mesh]

        return {'FINISHED'}


class RobotEditor_setSelectedMeshActiveObject(bpy.types.Operator):
    bl_idname = "roboteditor.setseletedmeshactiveobject"
    bl_label = "Select geometry"

    def execute(self, context):
        mesh = context.scene.RobotEditor.meshName
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[mesh].select = True
        context.scene.objects.active = bpy.data.objects[mesh]
        return {'FINISHED'}


# defines the layout part of the mesh submenu
def draw(layout, context):
    if not armatures.checkArmature(layout, context):
        return

    box = layout.box()
    row = box.row(align=True)
    row.label("Mesh type:")
    row.prop(bpy.context.scene.RobotEditor, "meshType", expand=True)
    row = box.row(align=True)
    row.label("Show:")
    row.prop(bpy.context.scene.RobotEditor, "hideMeshType", expand=True)
    box.separator()

    box = layout.box()
    if collapsible(box, context, 'collapseDisconnectMesh', "Disconnect meshes"):
        row = box.row()
        column = row.column(align=True)
        meshSelector(column, context)

        column = row.column(align=True)
        column.operator("roboteditor.unassignmesh")
        column.operator("roboteditor.unassignallmeshes")
        column.operator("roboteditor.renamemeshes")
        column.operator("roboteditor.setseletedmeshactiveobject")
        column.operator("roboteditor.setallmeshesactiveobject")
        selected_objects = [i for i in context.selected_objects if i.name != context.active_object.name]
        if len(selected_objects) == 1:
            box.prop(selected_objects[0].RobotEditor, 'fileName')
        box.separator()

    box = layout.box()
    if collapsible(box, context, 'collapseConnectMesh', "Connect meshes"):
        row = box.row()
        column = row.column(align=True)
        column.menu("roboteditor.bonemeshmenu")

        column.prop(context.scene.RobotEditor, "liveSearchBones", icon='VIEWZOOM', text="")
        column.prop(context.scene.RobotEditor, "listBones", expand=True)
        column = row.column(align=True)
        column.operator("roboteditor.assignmesh")
        box.separator()

    if bpy.context.scene.RobotEditor.meshType == "DEFAULT":
        box = layout.box()
        if collapsible(box, context, 'collapseCollision', 'Generate collision meshes'):
            collision.draw(box, context)

            # lowerRow = layout.row(align=False)
            # layout.label("Select Physics Frame:")
            # frameMenuText = ""
            # if context.active_bone and not context.scene.RobotEditor.physicsFrameName == "":
            #     frame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]
            #
            #     if frame.parent_bone:
            #         frameMenuText = context.scene.RobotEditor.physicsFrameName + " --> " + frame.parent_bone
            #     else:
            #         frameMenuText = context.scene.RobotEditor.physicsFrameName
            #
            # lowerRow.menu("roboteditor.physicsframemenu", text=frameMenuText)
            # lowerRow.operator("roboteditor.assigncollisionmodel")


def register():
    bpy.utils.register_class(RobotEditor_selectMesh)
    bpy.utils.register_class(RobotEditor_meshMenu)
    bpy.utils.register_class(RobotEditor_boneMeshMenu)
    bpy.utils.register_class(RobotEditor_assignMesh)
    bpy.utils.register_class(RobotEditor_unassignMesh)
    bpy.utils.register_class(RobotEditor_unassignAllMeshes)
    bpy.utils.register_class(RobotEditor_renameAllMeshes)
    bpy.utils.register_class(RobotEditor_setSelectedMeshActiveObject)
    bpy.utils.register_class(RobotEditor_setAllMeshesObject)


def unregister():
    bpy.utils.unregister_class(RobotEditor_selectMesh)
    bpy.utils.unregister_class(RobotEditor_meshMenu)
    bpy.utils.unregister_class(RobotEditor_boneMeshMenu)
    bpy.utils.unregister_class(RobotEditor_assignMesh)
    bpy.utils.unregister_class(RobotEditor_unassignMesh)
    bpy.utils.unregister_class(RobotEditor_unassignAllMeshes)
    bpy.utils.unregister_class(RobotEditor_renameAllMeshes)
    bpy.utils.unregister_class(RobotEditor_setSelectedMeshActiveObject)
    bpy.utils.unregister_class(RobotEditor_setAllMeshesObject)
