# Blender-specific imports (catch exception for sphinx documentation)
import bpy
from bpy.props import *


# operator to create new marker
class RobotEditor_createMarker(bpy.types.Operator):
    bl_idname = "roboteditor.createmarker"
    bl_label = "Create Marker"

    markerName = StringProperty(name="Marker Name")
    radius = FloatProperty(name="Radius", default=0.0025, min=0.001)

    def execute(self, context):
        armName = context.active_object.name
        bpy.ops.surface.primitive_nurbs_surface_sphere_add(radius=self.radius)
        context.active_object.name = self.markerName
        bpy.ops.object.empty_add(type='PLAIN_AXES')
        context.active_object.name = "MARKER_" + self.markerName
        context.active_object.RobotEditor.tag = 'MARKER'

        for obj in bpy.data.objects:
            obj.select = False

        bpy.data.objects[self.markerName].select = True
        bpy.data.objects["MARKER_" + self.markerName].select = True
        context.scene.objects.active = bpy.data.objects["MARKER_" + self.markerName]
        bpy.ops.object.parent_set()

        bpy.ops.roboteditor.selectarmature(armatureName=armName)
        bpy.ops.roboteditor.selectmarker(markerName="MARKER_" + self.markerName)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


# operator to select marker
class RobotEditor_selectMarker(bpy.types.Operator):
    bl_idname = "roboteditor.selectmarker"
    bl_label = "Select Marker"

    markerName = StringProperty()

    def execute(self, context):
        context.scene.RobotEditor.markerName = self.markerName
        marker = bpy.data.objects[self.markerName]
        arm = context.active_object

        for obj in bpy.data.objects:
            obj.select = False

        marker.select = True
        arm.select = True

        return {'FINISHED'}


# dynamic menu to select from markers
class RobotEditor_markerMenu(bpy.types.Menu):
    bl_idname = "roboteditor.markermenu"
    bl_label = "Select Marker"

    def draw(self, context):
        layout = self.layout
        markerNames = [obj.name for obj in bpy.data.objects if
                       obj.RobotEditor.tag == 'MARKER' and context.scene.RobotEditor.liveSearchMarkers in obj.name]

        for marker in sorted(markerNames, key=str.lower):
            if bpy.data.objects[marker].parent_bone:
                text = marker + " --> " + bpy.data.objects[marker].parent_bone
            else:
                text = marker
            layout.operator("roboteditor.selectmarker", text=text).markerName = marker


# operator to assign marker to bone
class RobotEditor_assignMarker(bpy.types.Operator):
    bl_idname = "roboteditor.assignmarker"
    bl_label = "Assign Marker to Bone"

    def execute(self, context):
        bpy.ops.object.parent_set(type='BONE')
        return {'FINISHED'}


# operator to unassign marker from bone
class RobotEditor_unassignMarker(bpy.types.Operator):
    bl_idname = "roboteditor.unassignmarker"
    bl_label = "Unassign marker"

    def execute(self, context):
        currentMarker = bpy.data.objects[context.scene.RobotEditor.markerName]
        marker_global = currentMarker.matrix_world
        currentMarker.parent = None
        currentMarker.matrix_world = marker_global

        return {'FINISHED'}


# defines the UI part of the markers submenu
def draw(layout, context):
    layout.operator("roboteditor.createmarker")
    layout.label("Select marker")
    topRow = layout.column(align=True)
    markerMenuText = ""
    if context.active_bone and not context.scene.RobotEditor.markerName == "":
        marker = bpy.data.objects[context.scene.RobotEditor.markerName]

        if marker.parent_bone:
            markerMenuText = context.scene.RobotEditor.markerName + " --> " + marker.parent_bone
        else:
            markerMenuText = context.scene.RobotEditor.markerName
    topRow.menu("roboteditor.markermenu", text=markerMenuText)
    topRow.prop(context.scene.RobotEditor, "liveSearchMarkers", icon='VIEWZOOM', text="")
    topRow.separator()
    topRow.operator("roboteditor.unassignmarker")

    layout.label("Select Bone:")
    lowerRow = layout.column(align=True)
    lowerRow.menu("roboteditor.bonemenu", text=context.active_bone.name)
    lowerRow.prop(context.scene.RobotEditor, "liveSearchBones", icon='VIEWZOOM', text="")
    lowerRow.separator()
    lowerRow.operator("roboteditor.assignmarker")


def register():
    bpy.utils.register_class(RobotEditor_createMarker)
    bpy.utils.register_class(RobotEditor_selectMarker)
    bpy.utils.register_class(RobotEditor_markerMenu)
    bpy.utils.register_class(RobotEditor_assignMarker)
    bpy.utils.register_class(RobotEditor_unassignMarker)


def unregister():
    bpy.utils.unregister_class(RobotEditor_createMarker)
    bpy.utils.unregister_class(RobotEditor_selectMarker)
    bpy.utils.unregister_class(RobotEditor_markerMenu)
    bpy.utils.unregister_class(RobotEditor_assignMarker)
    bpy.utils.unregister_class(RobotEditor_unassignMarker)
