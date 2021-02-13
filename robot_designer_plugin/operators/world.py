# ######
# Blender imports
import bpy
from bpy.props import StringProperty
# import mathutils

# ######
# RobotDesigner imports
from ..core import config, PluginManager, RDOperator, Condition
from .helpers import ModelSelected, NotEditMode, ObjectMode
from ..properties.globals import global_properties


@RDOperator.Preconditions()
@PluginManager.register_class
class CreateNewWorld(RDOperator):
    """
    :term:`Operator <operator>` for creating a new :term:`world`.
    """

    bl_idname = config.OPERATOR_PREFIX + "create_world"
    bl_label = "Create World"

    world_name: StringProperty(name="World Name")

    @classmethod
    def run(cls, world_name):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions()
    def execute(self, context):

        bpy.ops.object.empty_add(type='PLAIN_AXES')

        context.active_object.RobotDesigner.tag = 'WORLD'

        worlds = [obj.name for obj in bpy.data.objects if obj.RobotDesigner.tag == 'WORLD']
        index = 1
        name = self.world_name
        while name in worlds:
            name = self.world_name + str(index)
            index += 1

        context.active_object.name = name
        context.active_object.RobotDesigner.worlds.name = name
        world_name = context.active_object.name

        SelectWorld.run(object_name=world_name)

        return {'FINISHED'}

    def invoke(self, context, event):
        # self.sensor_type = global_properties.display_sensor_type.get(context.scene)
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions()
@PluginManager.register_class
class SelectWorld(RDOperator):
    """
    :term:`Operator <operator>` for selecting a world.
    """
    bl_idname = config.OPERATOR_PREFIX + "select_world"
    bl_label = "Select World"
    object_name: StringProperty()

    @classmethod
    def run(cls, object_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions()
    def execute(self, context):
        Object = bpy.data.objects[self.object_name]

        for obj in bpy.data.objects:
            obj.select_set(False)

        Object.select_set(True)
        bpy.context.view_layer.objects.active = Object

        global_properties.world_name.set(context.scene, self.object_name)

        return {'FINISHED'}


@RDOperator.Preconditions()
@PluginManager.register_class
class RemoveRobot(RDOperator):
    """
    :term:'Operator <operator>' to remove a robot from the list.
    """
    bl_idname = config.OPERATOR_PREFIX + "remove_robot"
    bl_label = "Remove Robot"
    robot_name: StringProperty()

    @classmethod
    def run(cls, robot_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions()
    def execute(self, context):

        if self.robot_name in context.active_object.RobotDesigner.worlds.robot_list:
            index = context.active_object.RobotDesigner.worlds.robot_list.find(self.robot_name)
            context.active_object.RobotDesigner.worlds.robot_list.remove(index)

        return {'FINISHED'}


@RDOperator.Preconditions()
@PluginManager.register_class
class AddRobot(RDOperator):
    """
    :term: 'Operator <operator>' to add a robot to the list.
    """
    bl_idname = config.OPERATOR_PREFIX + "add_robot"
    bl_label = "Add Robot"
    robot_name: StringProperty()

    @classmethod
    def run(cls, robot_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions()
    def execute(self, context):

        if self.robot_name not in context.active_object.RobotDesigner.worlds.robot_list:
            new_bot = context.active_object.RobotDesigner.worlds.robot_list.add()
            new_bot.name = self.robot_name

        return {'FINISHED'}

