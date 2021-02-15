# #####
#  This file is part of the RobotDesigner developed in the Neurorobotics
#  subproject of the Human Brain Project (https://www.humanbrainproject.eu).
#
#  The Human Brain Project is a European Commission funded project
#  in the frame of the Horizon2020 FET Flagship plan.
#  (http://ec.europa.eu/programmes/horizon2020/en/h2020-section/fet-flagships)
#
#  The Robot Designer has initially been forked from the RobotEditor
#  (https://gitlab.com/h2t/roboteditor) developed at the Karlsruhe Institute
#  of Technology in the High Performance Humanoid Technologies Laboratory (H2T).
# #####

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# #####
#
#  Copyright (c) 2017-2021, TUM Technical University of Munich
#
# #####

# Blender imports
import bpy
from bpy.props import StringProperty

# RobotDesigner imports
from ..core import config, PluginManager, RDOperator
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

        bpy.ops.object.empty_add(type="PLAIN_AXES")

        context.active_object.RobotDesigner.tag = "WORLD"

        worlds = [
            obj.name for obj in bpy.data.objects if obj.RobotDesigner.tag == "WORLD"
        ]
        index = 1
        name = self.world_name
        while name in worlds:
            name = self.world_name + str(index)
            index += 1

        context.active_object.name = name
        context.active_object.RobotDesigner.worlds.name = name
        world_name = context.active_object.name

        SelectWorld.run(object_name=world_name)

        return {"FINISHED"}

    def invoke(self, context, event):
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

        return {"FINISHED"}


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
            index = context.active_object.RobotDesigner.worlds.robot_list.find(
                self.robot_name
            )
            context.active_object.RobotDesigner.worlds.robot_list.remove(index)

        return {"FINISHED"}


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

        return {"FINISHED"}
