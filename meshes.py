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
        meshNames = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']

        for mesh in meshNames:
            if bpy.data.objects[mesh].parent_bone:
                text = mesh + " --> " + bpy.data.objects[mesh].parent_bone
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
            if i.parent_bone != '':
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
        currentMesh.parent = None

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


# defines the layout part of the mesh submenu
def draw(layout, context):
    layout.label("Select mesh:")
    topRow = layout.row(align=False)
    meshMenuText = ""
    if context.scene.RobotEditor.meshName in bpy.data.objects:
        if(context.active_bone and not context.scene.RobotEditor.meshName == ""):
            mesh = bpy.data.objects[context.scene.RobotEditor.meshName]

            if mesh.parent_bone:
                meshMenuText = context.scene.RobotEditor.meshName + " --> " + mesh.parent_bone
            else:
                meshMenuText = context.scene.RobotEditor.meshName
    topRow.menu("roboteditor.meshmenu", text=meshMenuText)
    rightColumn = topRow.column(align=True)
    rightColumn.operator("roboteditor.unassignmesh")
    rightColumn.operator("roboteditor.unassignallmeshes")
    rightColumn.operator("roboteditor.renamemeshes")

    layout.label("Select bone")
    lowerRow = layout.row(align = False)

    lowerRow.menu("roboteditor.bonemenu", text = context.active_bone.name)
    lowerRow.operator("roboteditor.assignmesh")




def register():
    bpy.utils.register_class(RobotEditor_selectMesh)
    bpy.utils.register_class(RobotEditor_meshMenu)
    bpy.utils.register_class(RobotEditor_assignMesh)
    bpy.utils.register_class(RobotEditor_unassignMesh)
    bpy.utils.register_class(RobotEditor_unassignAllMeshes)
    bpy.utils.register_class(RobotEditor_renameAllMeshes)


def unregister():
    bpy.utils.unregister_class(RobotEditor_selectMesh)
    bpy.utils.unregister_class(RobotEditor_meshMenu)
    bpy.utils.unregister_class(RobotEditor_assignMesh)
    bpy.utils.unregister_class(RobotEditor_unassignMesh)
    bpy.utils.unregister_class(RobotEditor_unassignAllMeshes)
    bpy.utils.unregister_class(RobotEditor_renameAllMeshes)
