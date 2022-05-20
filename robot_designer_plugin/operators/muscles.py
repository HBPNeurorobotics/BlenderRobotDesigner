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

"""
Sphinx-autodoc tag
"""

# Blender imports
import bpy
import math
from bpy.props import StringProperty, BoolProperty, IntProperty

# RobotDesigner imports
from ..core import config, PluginManager, RDOperator

from .helpers import ModelSelected, SingleSegmentSelected

try:
    from ..properties.globals import global_properties
except:
    pass


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class RenameMuscle(RDOperator):
    """
    :term:`operator` for renaming the selected muscle


    """

    bl_idname = config.OPERATOR_PREFIX + "rename_muscle"
    bl_label = "Rename Active Muscle"

    new_name: StringProperty(name="Enter new name:")

    @RDOperator.OperatorLogger
    def execute(self, context):
        bpy.data.objects[
            global_properties.active_muscle.get(context.scene)
        ].name = self.new_name
        global_properties.active_muscle.set(
            context.scene, self.new_name
        )  # TODO: change material name as well?
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, new_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DeleteMuscle(RDOperator):
    """
    :term:`operator` for deleting the selected muscle.


    """

    bl_idname = config.OPERATOR_PREFIX + "deletemuscle"
    bl_label = "Delete Active Muscle"

    @RDOperator.OperatorLogger
    def execute(self, context):
        active_muscle = global_properties.active_muscle.get(context.scene)

        # remove muscle and all its data
        bpy.data.objects.remove(bpy.data.objects[active_muscle], do_unlink=True)
        bpy.data.materials.remove(
            bpy.data.materials[active_muscle + "_vis"], do_unlink=True
        )
        bpy.data.curves.remove(bpy.data.curves[active_muscle], do_unlink=True)
        global_properties.active_muscle.set(context.scene, "")
        bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateNewMuscle(RDOperator):
    """
    :term:`Operator <operator>` for creating new robot segments and add it to the current model.
    If a segment is already selected, the new segment is added as a child segment. A call :class:`SelectSegment`
    before might be necessary.
    """

    bl_idname = config.OPERATOR_PREFIX + "create_muscle"
    bl_label = "Create New Muscle"

    muscle_name: StringProperty(name="Enter new muscle name:")

    @classmethod
    def run(cls, muscle_name):  # , parent_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected)
    def execute(self, context):
        global_properties.active_muscle.set(bpy.context.scene, self.muscle_name)

        # basic muscle visualization data
        muscleVis = bpy.data.curves.new(name=self.muscle_name, type="CURVE")
        muscleVis.dimensions = "3D"
        muscleVis.fill_mode = "FULL"
        muscleVis.bevel_depth = global_properties.muscle_dim.get(context.scene)
        # create muscle object with visualization data
        muscle = bpy.data.objects.new(self.muscle_name, muscleVis)
        bpy.context.scene.collection.objects.link(muscle)
        muscle.location = (0.0, 0.0, 0.0)
        # setup a material
        lmat = bpy.data.materials.new(self.muscle_name + "_vis")
        lmat.diffuse_color = (0.0, 0.0, 1.0, 1.0)
        # lmat.use_shadeless = True
        muscle.data.materials.append(lmat)
        muscleData = muscle.RobotDesigner.muscles
        muscleData.name = self.muscle_name
        muscleData.muscleType = "THELEN"
        muscleData.robotName = global_properties.model_name.get(context.scene)
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectMuscle(RDOperator):
    """
    :ref:`operator` for selecting a muscle.

    **Preconditions:**

    **RDOperator.Postconditions:**
    """

    bl_idname = config.OPERATOR_PREFIX + "selectm"
    bl_label = "Select Muscle"

    muscle_name: StringProperty()

    @classmethod
    def run(cls, muscle_name=""):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        global_properties.active_muscle.set(bpy.context.scene, self.muscle_name)

        ### todo highlight muscle when selected similar to here:
        #  for bone in [i.name for i in bpy.data.armatures[
        #      context.active_object.data.name].bones]:
        #      if self.muscle_name != 'None':
        #          context.active_object.pose.bones[bone].custom_shape = \
        #              bpy.data.objects[self.muscle_name]
        #      else:
        #          context.active_object.pose.bones[bone].custom_shape = None
        return {"FINISHED"}


#### Muscle Pathpoints
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateNewPathpoint(RDOperator):
    """
    :term:`Operator <operator> for creating a new pathpoint as a spline point on the muscle object
    """

    bl_idname = config.OPERATOR_PREFIX + "create_muscle_pathpoint"
    bl_label = "Add Current Cursor Location as Pathpoint"

    bl_description = (
        "Add the current cursor location as a new pathpoint \n\n"
        + "Select a cursor location with 'Shift' + RightClick"
    )

    @classmethod
    def run(cls):  # , parent_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected)
    def execute(self, context):

        active_muscle = bpy.data.objects[
            global_properties.active_muscle.get(bpy.context.scene)
        ]

        flag = 0
        if len(active_muscle.data.splines) == 0:
            active_muscle.data.splines.new("POLY")
            flag = 1

        if flag == 0:
            active_muscle.data.splines[0].points.add(1)
        cursor = bpy.context.scene.cursor.location

        nr = len(active_muscle.data.splines[0].points)
        active_muscle.data.splines[0].points[nr - 1].co = [
            cursor.x,
            cursor.y,
            cursor.z,
            1,
        ]

        active_muscle.RobotDesigner.muscles.pathPoints.add()

        # add new hok modifier for pathpoint
        active_muscle.modifiers.new(
            name=global_properties.active_muscle.get(bpy.context.scene)
            + "_"
            + str(nr - 1),
            type="HOOK",
        )

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectMusclePathPoint(RDOperator):
    """
    :ref:`operator` for selecting a muscle pathpoint
    """

    bl_idname = config.OPERATOR_PREFIX + "select_muscle_pathpoint"
    bl_label = "Select Muscle Pathpoint"

    muscle_pathpoint_name: StringProperty()

    @classmethod
    def run(cls, muscle_pathpoint=""):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        global_properties.active_muscle_pathpoint.set(
            bpy.context.scene, self.muscle_pathpoint_name
        )

        ### todo highlight pathpoint on selection similar to here:
        #  for bone in [i.name for i in bpy.data.armatures[
        #      context.active_object.data.name].bones]:
        #      if self.muscle_name != 'None':
        #          context.active_object.pose.bones[bone].custom_shape = \
        #              bpy.data.objects[self.muscle_name]
        #      else:
        #          context.active_object.pose.bones[bone].custom_shape = None
        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DeletePathpoint(RDOperator):
    """
    :term:`operator` for deleting a the selected pathpoint from the muscle.


    """

    bl_idname = config.OPERATOR_PREFIX + "delete_muscle_pathpoint"
    bl_label = ""

    pathpoint: bpy.props.IntProperty(name="Delete pathpoint:")  # defining the property

    @RDOperator.OperatorLogger
    def execute(self, context):
        active_muscle = global_properties.active_muscle.get(context.scene)
        bpy.context.view_layer.objects.active = None
        bpy.context.view_layer.objects.active = bpy.data.objects[active_muscle]

        bpy.ops.object.mode_set(mode="EDIT")

        bpy.data.objects[active_muscle].data.splines[0].points[
            self.pathpoint - 1
        ].select = True
        bpy.ops.curve.delete(type="VERT")

        bpy.ops.object.mode_set(mode="OBJECT")

        bpy.context.view_layer.objects.active = bpy.data.objects[
            global_properties.model_name.get(context.scene)
        ]

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class MovePathpointUp(RDOperator):
    """
    :term:`operator` for switching index of pathpoint with previous one.


    """

    bl_idname = config.OPERATOR_PREFIX + "move_pathpoint_up"
    bl_label = ""

    nr: bpy.props.IntProperty(name="Move up pathpoint:")

    @RDOperator.OperatorLogger
    def execute(self, context):
        active_muscle = global_properties.active_muscle.get(context.scene)

        if self.nr != 1:
            active_muscle_points = bpy.data.objects[active_muscle].data.splines[0]
            x = active_muscle_points.points[self.nr - 1].co[0]
            y = active_muscle_points.points[self.nr - 1].co[1]
            z = active_muscle_points.points[self.nr - 1].co[2]
            w = active_muscle_points.points[self.nr - 1].co[3]

            active_muscle_points.points[self.nr - 1].co = active_muscle_points.points[
                self.nr - 2
            ].co
            active_muscle_points.points[self.nr - 2].co = [x, y, z, w]

            # move coordFrame
            frame = (
                bpy.data.objects[active_muscle]
                .RobotDesigner.muscles.pathPoints[self.nr - 2]
                .coordFrame
            )
            bpy.data.objects[active_muscle].RobotDesigner.muscles.pathPoints[
                self.nr - 2
            ].coordFrame = (
                bpy.data.objects[active_muscle]
                .RobotDesigner.muscles.pathPoints[self.nr - 1]
                .coordFrame
            )
            bpy.data.objects[active_muscle].RobotDesigner.muscles.pathPoints[
                self.nr - 1
            ].coordFrame = frame

        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class MovePathpointDown(RDOperator):
    """
    :term:`operator` for switching index of pathpoint with previous one.


    """

    bl_idname = config.OPERATOR_PREFIX + "move_pathpoint_down"
    bl_label = ""

    nr: bpy.props.IntProperty(name="Move down pathpoint:")

    @RDOperator.OperatorLogger
    def execute(self, context):
        active_muscle = global_properties.active_muscle.get(context.scene)

        if self.nr != len(bpy.data.objects[active_muscle].data.splines[0].points):
            active_muscle_points = bpy.data.objects[
                global_properties.active_muscle.get(context.scene)
            ].data.splines[0]
            x = active_muscle_points.points[self.nr - 1].co[0]
            y = active_muscle_points.points[self.nr - 1].co[1]
            z = active_muscle_points.points[self.nr - 1].co[2]
            w = active_muscle_points.points[self.nr - 1].co[3]

            active_muscle_points.points[self.nr - 1].co = active_muscle_points.points[
                self.nr
            ].co
            active_muscle_points.points[self.nr].co = [x, y, z, w]

            # move coordFrame
            frame = (
                bpy.data.objects[active_muscle]
                .RobotDesigner.muscles.pathPoints[self.nr - 1]
                .coordFrame
            )
            bpy.data.objects[active_muscle].RobotDesigner.muscles.pathPoints[
                self.nr - 1
            ].coordFrame = (
                bpy.data.objects[active_muscle]
                .RobotDesigner.muscles.pathPoints[self.nr]
                .coordFrame
            )
            bpy.data.objects[active_muscle].RobotDesigner.muscles.pathPoints[
                self.nr
            ].coordFrame = frame

        return {"FINISHED"}


## select segment to be assigned to muscle
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectSegmentMuscle(RDOperator):
    """
    :term:`Operator<operator>` for selecting a segment to be assigned to a pathpoint.
    """

    bl_idname = config.OPERATOR_PREFIX + "select_segment_muscle"
    bl_label = "Select Segment to Attach Muscle Pathpoint"

    segment_name: StringProperty()
    pathpoint_nr: IntProperty(default=1)

    @RDOperator.OperatorLogger
    def execute(self, context):
        model = bpy.data.objects[global_properties.model_name.get(context.scene)]
        active_muscle = global_properties.active_muscle.get(context.scene)

        for b in model.data.bones:
            b.select = False

        if self.segment_name:
            model.data.bones.active = model.data.bones[self.segment_name]

            model.data.bones.active.select = True
        else:
            model.data.bones.active = None

        # store selected segment
        bpy.data.objects[active_muscle].RobotDesigner.muscles.pathPoints[
            self.pathpoint_nr - 1
        ].coordFrame = self.segment_name

        active_muscle = global_properties.active_muscle.get(context.scene)
        active_model = global_properties.model_name.get(context.scene)

        ### hook pathpoint to segment
        bpy.context.active_object

        muscle_object = bpy.data.objects[active_muscle]

        location = muscle_object.data.splines[0].points[self.pathpoint_nr - 1].co

        # get modifier
        hok = muscle_object.modifiers[active_muscle + "_" + str(self.pathpoint_nr - 1)]
        hok.object = bpy.data.objects[active_model]
        hok.subtarget = self.segment_name
        hok.falloff_type = "NONE"

        context.view_layer.objects.active = bpy.data.objects[active_muscle]
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.curve.select_all(action="DESELECT")
        muscle_object.data.splines[0].points[self.pathpoint_nr - 1].select = True

        bpy.ops.object.hook_reset(modifier=hok.name)

        # bpy.ops.object.hook_select(modifier=hok.name)
        bpy.ops.object.hook_assign(modifier=hok.name)

        bpy.ops.object.mode_set(mode="OBJECT")

        bpy.context.view_layer.objects.active = bpy.data.objects[active_model]

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, segment_name=""):
        return super().run(**cls.pass_keywords())

        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CalculateMuscleLength(RDOperator):
    """
    :term:`operator` for calculating the length of the active muscle


    """

    bl_idname = config.OPERATOR_PREFIX + "calc_muscle_length"
    bl_label = "Calculate Muscle Length"

    muscle: bpy.props.StringProperty()

    @RDOperator.OperatorLogger
    def execute(self, context):
        leng = 0.0

        if len(bpy.data.objects[self.muscle].data.splines) == 0:
            return {"CANCELLED"}

        spline = bpy.data.objects[self.muscle].data.splines[0]

        for i in range(0, len(spline.points) - 1):
            x = spline.points[i].co[0] - spline.points[i + 1].co[0]
            y = spline.points[i].co[1] - spline.points[i + 1].co[1]
            z = spline.points[i].co[2] - spline.points[i + 1].co[2]

            leng += math.sqrt((x ** 2) + (y ** 2) + (z ** 2))

        bpy.data.objects[self.muscle].RobotDesigner.muscles.length = leng

        return {"FINISHED"}
