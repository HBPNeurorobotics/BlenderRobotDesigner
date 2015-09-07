import bpy

__author__ = 'ulbrich'


def collapsible(box, context, bool_property,label):
    """
    Create a collapsible box element

    :param box: the box which content has to be collapsed
    :param context: Blender context object
    :param bool_property: Name of the global scene property
    :type bool_property: string
    :param label: Label close to the folding symbol
    :return: Boolean True if expanded, False if collapsed.
    """

    row = box.row()
    row.prop(context.scene.RobotEditor, bool_property,
             icon="TRIA_DOWN" if getattr(context.scene.RobotEditor,bool_property) else "TRIA_RIGHT",
             icon_only=True, emboss=False
             )
    row.label(text=label)
    return getattr(context.scene.RobotEditor, bool_property)


def boneSelector(layout,context):
    layout.menu("roboteditor.bonemenu", text=context.active_bone.name)
    layout.prop(context.scene.RobotEditor, "liveSearchBones", icon='VIEWZOOM', text="")


def meshSelector(layout,context):
    meshMenuText = ""
    hide_mesh = context.scene.RobotEditor.listMeshes
    if context.scene.RobotEditor.meshName in bpy.data.objects:
        if context.active_bone and not context.scene.RobotEditor.meshName == "":
            mesh = bpy.data.objects[context.scene.RobotEditor.meshName]

            if mesh.parent_bone and not hide_mesh == 'disconnected':
                meshMenuText = context.scene.RobotEditor.meshName + " --> " + mesh.parent_bone
            # elif mesh.parent:
            #     meshMenuText = context.scene.RobotEditor.meshName + " --> " + mesh.parent.name
            elif not mesh.parent_bone and not hide_mesh == 'connected':
                meshMenuText = context.scene.RobotEditor.meshName
            else:
                meshMenuText = ''

    layout.menu("roboteditor.meshmenu", text=meshMenuText)
    layout.prop(context.scene.RobotEditor, "liveSearchMeshes", icon='VIEWZOOM', text="")
    layout.prop(context.scene.RobotEditor, "listMeshes", expand=True)

