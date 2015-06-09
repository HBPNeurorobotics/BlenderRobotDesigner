import bpy
from bpy.props import *

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

        return{'FINISHED'}

# dynamic menu to select mesh
class RobotEditor_meshMenu(bpy.types.Menu):
    bl_idname = "roboteditor.meshmenu"
    bl_label = "Select Mesh"

    def draw(self, context):
        layout = self.layout
        meshNames = [obj.name for obj in bpy.data.objects if obj.type == 'MESH' and context.scene.RobotEditor.liveSearchMeshes in obj.name]

        for mesh in meshNames:
            if bpy.data.objects[mesh].parent_bone:
                text = mesh + " --> " + bpy.data.objects[mesh].parent_bone
            elif bpy.data.objects[mesh].parent:
                #text = context.scene.RobotEditor.meshName + " --> " + bpy.data.objects[mesh].parent.name
                text = mesh + " --> " + bpy.data.objects[mesh].parent.name
            else:
                text = mesh
            layout.operator("roboteditor.selectmesh", text=text).meshName=mesh


# operator to assign mesh to bone
class RobotEditor_assignMesh(bpy.types.Operator):
    bl_idname = "roboteditor.assignmesh"
    bl_label = "Assign selected mesh to active bone"

    def execute(self, context):
        bpy.ops.object.parent_set(type = 'BONE', keep_transform=True)
        return{'FINISHED'}


# operator to rename meshes using their parent bone's name
class RobotEditor_renameAllMeshes(bpy.types.Operator):
    bl_idname = "roboteditor.renamemeshes"
    bl_label = "Renames meshes after bones"

    def execute(self, context):
        currentMesh = bpy.data.objects[context.scene.RobotEditor.meshName]
        for i in bpy.data.objects:
            if i.parent_bone != '' and i.type=='MESH':
                if i.name == currentMesh:
                    context.scene.RobotEditor.meshName=i.parent_bone
                i.name = 'Visualization_'+i.parent_bone

        return{'FINISHED'}

# operator to unassign mesh from bone
class RobotEditor_unassignMesh(bpy.types.Operator):
    bl_idname = "roboteditor.unassignmesh"
    bl_label = "Unassign selected mesh"

    def execute(self, context):
        currentMesh = bpy.data.objects[context.scene.RobotEditor.meshName]
        mesh_global = currentMesh.matrix_world
        currentMesh.parent = None
        currentMesh.matrix_world = mesh_global

        return{'FINISHED'}



# operator to unassign all meshes in the scene
class RobotEditor_unassignAllMeshes(bpy.types.Operator):
    bl_idname = "roboteditor.unassignallmeshes"
    bl_label = "Unassign ALL meshes"

    confirmation = BoolProperty(name="Are you sure?")

    def execute(self, context):
            if self.confirmation:
                meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH' and not obj.parent_bone is '']

                for mesh in meshes:
                    bpy.ops.roboteditor.selectmesh(meshName = mesh.name)
                    bpy.ops.roboteditor.unassignmesh()

            return{'FINISHED'}

    def invoke(self,context,event):
        return context.window_manager.invoke_props_dialog(self)

class RobotEditor_assignCollisionModel(bpy.types.Operator):
    bl_idname = "roboteditor.assigncollisionmodel"
    bl_label = "Assign selected mesh as collision model to physics frame."

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")
        if context.scene.RobotEditor.meshName in bpy.data.objects:
            bpy.data.objects[context.scene.RobotEditor.meshName].select = True
            if context.scene.RobotEditor.physicsFrameName in bpy.data.objects:
                context.scene.objects.active = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]
                bpy.ops.object.parent_set(type = 'OBJECT', keep_transform=True)

        if context.scene.RobotEditor.armatureName in bpy.data.objects:
            context.scene.objects.active = bpy.data.objects[context.scene.RobotEditor.armatureName]
        return{'FINISHED'}


# defines the layout part of the mesh submenu
def draw(layout, context):
    layout.label("Select mesh:")
    topRow = layout.column(align=True)
    meshMenuText = ""
    if context.scene.RobotEditor.meshName in bpy.data.objects:
        if(context.active_bone and not context.scene.RobotEditor.meshName == ""):
            mesh = bpy.data.objects[context.scene.RobotEditor.meshName]

            if mesh.parent_bone:
                meshMenuText = context.scene.RobotEditor.meshName + " --> " + mesh.parent_bone
            elif mesh.parent:
                meshMenuText = context.scene.RobotEditor.meshName + " --> " + mesh.parent.name
            else:
                meshMenuText = context.scene.RobotEditor.meshName
    topRow.menu("roboteditor.meshmenu", text=meshMenuText)
    topRow.prop(context.scene.RobotEditor, "liveSearchMeshes", icon='VIEWZOOM', text="")
    topRow.separator()
    rightColumn = topRow.column(align=False)
    rightColumn.operator("roboteditor.unassignmesh")
    rightColumn.operator("roboteditor.unassignallmeshes")
    rightColumn.operator("roboteditor.renamemeshes")

    layout.label("Select bone")
    midRow = layout.row(align = False)
    col = midRow.column(align = True)

    col.menu("roboteditor.bonemenu", text = context.active_bone.name)
    col.prop(context.scene.RobotEditor, "liveSearchBones", icon='VIEWZOOM', text="")
    midRow.operator("roboteditor.assignmesh")

    lowerRow = layout.row(align=False)
    layout.label("Select Physics Frame:")
    frameMenuText = ""
    if(context.active_bone and not context.scene.RobotEditor.physicsFrameName == ""):
        frame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]

        if frame.parent_bone:
            frameMenuText = context.scene.RobotEditor.physicsFrameName + " --> " + frame.parent_bone
        else:
            frameMenuText = context.scene.RobotEditor.physicsFrameName

    lowerRow.menu("roboteditor.physicsframemenu", text = frameMenuText)
    lowerRow.operator("roboteditor.assigncollisionmodel")





def register():
    bpy.utils.register_class(RobotEditor_selectMesh)
    bpy.utils.register_class(RobotEditor_meshMenu)
    bpy.utils.register_class(RobotEditor_assignMesh)
    bpy.utils.register_class(RobotEditor_unassignMesh)
    bpy.utils.register_class(RobotEditor_unassignAllMeshes)
    bpy.utils.register_class(RobotEditor_renameAllMeshes)
    bpy.utils.register_class(RobotEditor_assignCollisionModel)


def unregister():
    bpy.utils.unregister_class(RobotEditor_selectMesh)
    bpy.utils.unregister_class(RobotEditor_meshMenu)
    bpy.utils.unregister_class(RobotEditor_assignMesh)
    bpy.utils.unregister_class(RobotEditor_unassignMesh)
    bpy.utils.unregister_class(RobotEditor_unassignAllMeshes)
    bpy.utils.unregister_class(RobotEditor_renameAllMeshes)
    bpy.utils.unregister_class(RobotEditor_assignCollisionModel)
