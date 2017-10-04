# #####
# This file is part of the RobotDesigner of the Neurorobotics subproject (SP10)
# in the Human Brain Project (HBP).
# It has been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
# developed at the Karlsruhe Institute of Technology in the
# High Performance Humanoid Technologies Laboratory (H2T).
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
# Copyright (c) 2017, Technical University Munich
#
#
# ######
"""
Sphinx-autodoc tag
"""

# System imports
from math import degrees, radians

# Blender imports
import bpy
import math
from bpy.props import StringProperty, BoolProperty, IntProperty
# import mathutils

# RobotDesigner imports
from ..core import config, PluginManager, Condition, RDOperator

from .helpers import _mat3_to_vec_roll, ModelSelected, SingleSegmentSelected, PoseMode

from ..properties.globals import global_properties

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectMuscle(RDOperator):
    """
    :term:`Operator<operator>` for selecting a segment. If :attr:`segment_name` is empty,
    all segments will be deselected
    """
    bl_idname = config.OPERATOR_PREFIX + "select_segment"
    bl_label = "Select Segment"

    segment_name = StringProperty()

    @RDOperator.OperatorLogger
    def execute(self, context):
        if not (context.active_object.type == 'ARMATURE'):  #or context.active_object.type == 'MESH'
            raise Exception("BoneSelectionException")

        model = bpy.context.active_object
        for b in model.data.bones:
            b.select = False

        if self.segment_name:
            model.data.bones.active = model.data.bones[self.segment_name]

            model.data.bones.active.select = True
        else:
            model.data.bones.active = None

        return {'FINISHED'}

    @classmethod
    def run(cls, segment_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected, SingleSegmentSelected)
@PluginManager.register_class
class RenameMuscle(RDOperator):
    """
    :term:`operator` for renaming an active bone


    """
    bl_idname = config.OPERATOR_PREFIX + "rename_segment"
    bl_label = "Rename active segment"

    new_name = StringProperty(name="Enter new name:")


    @RDOperator.OperatorLogger
    def execute(self, context):
        context.active_bone.name = self.new_name
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, new_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DeleteMuscle(RDOperator):
    """
    :term:`operator` for deleting a the selected segment *ALL* of its children.


    """
    bl_idname = config.OPERATOR_PREFIX + "deletemuscle"
    bl_label = "Delete active muscle"

    @RDOperator.OperatorLogger
    def execute(self, context):

        active_muscle = global_properties.active_muscle.get(context.scene)

        # remove muscle and all data its data
        bpy.data.objects.remove(bpy.data.objects[active_muscle], True)
        bpy.data.materials.remove(bpy.data.materials[active_muscle + "_vis"], True)
        bpy.data.curves.remove(bpy.data.curves[active_muscle], True)
        global_properties.active_muscle.set(context.scene, '')
        context.scene.update()


        return {'FINISHED'}

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
    bl_label = "Create new muscle"

    muscle_name = StringProperty(name="Enter new muscle name:")

    @classmethod
    def run(cls, muscle_name):#, parent_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected)
    def execute(self, context):
        global_properties.active_muscle.set(bpy.context.scene, self.muscle_name)

        # basic muscle visualization data
        muscleVis = bpy.data.curves.new(name=self.muscle_name, type='CURVE')
        muscleVis.dimensions = '3D'
        muscleVis.fill_mode = 'FULL'
        muscleVis.bevel_depth = 0.05

        # create muscle object with visualization data
        muscle = bpy.data.objects.new(self.muscle_name, muscleVis)
        bpy.context.scene.objects.link(muscle)
        muscle.location = (0.0, 0.0, 0.0)   ## todo change this up to according reference frame!

        muscleData = muscle.RobotEditor.muscles
        muscleData.name = self.muscle_name
        muscleData.muscleType = "THELEN"
        muscleData.robotName = global_properties.model_name.get(context.scene)

        # setup a material
        lmat = bpy.data.materials.new(self.muscle_name + "_vis")
        lmat.diffuse_color = (0.0, 0.0, 1.0)
        lmat.use_shadeless = True
        muscle.data.materials.append(lmat)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

# def createBone(model_name, bone_name, parent_name=None):
#     """
#     Creates a new bone
#
#     :param model_name: string identifier of the armature
#     :param bone_name: the name of the new bone
#     :param parent_name: (optional) identifies the name of the parent bone
#     """
#     print("createBone")
#     designer.selectarmature(armatureName=model_name)
#     currentMode = bpy.context.object.mode
#
#     print(bpy.ops.object.mode_set(mode='EDIT', toggle=False))
#     # arm = bpy.data.armatures[armatureName]
#     bone = bpy.data.armatures[model_name].edit_bones.new(bone_name)
#     bone.head = (0, 0, 0)  # Dummy
#     bone.tail = (0, 0, 1)  # Dummy
#     bone.lock = True
#
#     if parent_name is not None:
#         bone.parent = bpy.data.armatures[model_name].edit_bones[parent_name]
#
#     bpy.ops.object.mode_set(mode='POSE', toggle=False)
#
#     designer.select_segment(boneName=bone_name)
#     bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
#     bpy.context.object.pose.bones[bone_name].constraints[
#         0].name = 'RobotEditorConstraint'
#     bpy.ops.object.mode_set(mode=currentMode, toggle=False)
#
#     print("createBone done")





@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectMuscle(RDOperator):
    """
    :ref:`operator` for selecting mesh for visualization of coordinate frames.

    **Preconditions:**

    **RDOperator.Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "selectcf"
    bl_label = "Select Muscle"

    muscle_name = StringProperty()

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

        ### highlight muscle similar to here
      #  for bone in [i.name for i in bpy.data.armatures[
      #      context.active_object.data.name].bones]:
      #      if self.muscle_name != 'None':
      #          context.active_object.pose.bones[bone].custom_shape = \
      #              bpy.data.objects[self.muscle_name]
      #      else:
      #          context.active_object.pose.bones[bone].custom_shape = None
        return {'FINISHED'}



#### Muscle Pathpoints
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateNewPathpoint(RDOperator):
    """
    :term:`Operator <operator>` for creating new robot segments and add it to the current model.
    If a segment is already selected, the new segment is added as a child segment. A call :class:`SelectSegment`
    before might be necessary.
    """
    bl_idname = config.OPERATOR_PREFIX + "create_muscle_pathpoint"
    bl_label = "Add current cursor location as pathpoint?"

    # model_name = StringProperty()
    #parent_name = StringProperty(default="")

    @classmethod
    def run(cls, pathpoint_name):#, parent_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleSegmentSelected)
    def execute(self, context):

        active_muscle = bpy.data.objects[global_properties.active_muscle.get(bpy.context.scene)]

        flag = 0
        if len(active_muscle.data.splines) == 0:
            active_muscle.data.splines.new('POLY')
            flag = 1

        if flag == 0:
            active_muscle.data.splines[0].points.add(1)
        cursor = bpy.context.scene.cursor_location


        nr = len(active_muscle.data.splines[0].points)
        active_muscle.data.splines[0].points[nr-1].co = [cursor.x, cursor.y, cursor.z,1]

        active_muscle.RobotEditor.muscles.pathPoints.add()

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectMusclePathPoint(RDOperator):
    """
    :ref:`operator` for selecting mesh for visualization of coordinate frames.

    **Preconditions:**

    **RDOperator.Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "select_muscle_pathpoint"
    bl_label = "Select Muscle Pathpoint"

    muscle_pathpoint_name = StringProperty()

    @classmethod
    def run(cls, muscle_pathpoint=""):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())


    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

        global_properties.active_muscle_pathpoint.set(bpy.context.scene, self.muscle_pathpoint_name)

        ### highlight muscle similar to here
      #  for bone in [i.name for i in bpy.data.armatures[
      #      context.active_object.data.name].bones]:
      #      if self.muscle_name != 'None':
      #          context.active_object.pose.bones[bone].custom_shape = \
      #              bpy.data.objects[self.muscle_name]
      #      else:
      #          context.active_object.pose.bones[bone].custom_shape = None
        return {'FINISHED'}




@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DeletePathpoint(RDOperator):
    """
    :term:`operator` for deleting a the selected segment *ALL* of its children.


    """
    bl_idname = config.OPERATOR_PREFIX + "delete_muscle_pathpoint"
    bl_label = ""

    pathpoint = bpy.props.IntProperty(name="Delete pathpoint:")  # defining the property

    @RDOperator.OperatorLogger
    def execute(self, context):
        print("context")
        print(context)
        active_muscle = global_properties.active_muscle.get(context.scene)
       # bpy.context.scene.objects.active = None
        bpy.context.scene.objects.active = bpy.data.objects[active_muscle]

        bpy.ops.object.mode_set(mode='EDIT')

        bpy.data.objects[active_muscle].data.splines[0].points[self.pathpoint-1].select = True
        bpy.ops.curve.delete(type='VERT')

        bpy.ops.object.mode_set(mode='OBJECT')

        bpy.context.scene.objects.active = bpy.data.objects[global_properties.model_name.get(context.scene)]

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class MovePathpointUp(RDOperator):
    """
    :term:`operator` for deleting a the selected segment *ALL* of its children.


    """
    bl_idname = config.OPERATOR_PREFIX + "move_pathpoint_up"
    bl_label = ""

    nr = bpy.props.IntProperty(name="Move up pathpoint:")

    @RDOperator.OperatorLogger
    def execute(self, context):

        active_muscle = global_properties.active_muscle.get(context.scene)

        if self.nr != 1:
            active_muscle_points = bpy.data.objects[active_muscle].data.splines[0]
            x = active_muscle_points.points[self.nr-1].co[0]
            y = active_muscle_points.points[self.nr-1].co[1]
            z = active_muscle_points.points[self.nr-1].co[2]
            w = active_muscle_points.points[self.nr-1].co[3]

            active_muscle_points.points[self.nr-1].co = active_muscle_points.points[self.nr-2].co
            active_muscle_points.points[self.nr-2].co = [x,y,z,w]

            # move coordFrame
            frame = bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.nr-2].coordFrame
            bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.nr-2].coordFrame = \
                bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.nr-1].coordFrame
            bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.nr - 1].coordFrame = frame

        return {'FINISHED'}

   # def invoke(self, context, event):
   #     return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class MovePathpointDown(RDOperator):
    """
    :term:`operator` for deleting a the selected segment *ALL* of its children.


    """
    bl_idname = config.OPERATOR_PREFIX + "move_pathpoint_down"
    bl_label = ""

    nr = bpy.props.IntProperty(name="Move down pathpoint:")

    @RDOperator.OperatorLogger
    def execute(self, context):

        active_muscle = global_properties.active_muscle.get(context.scene)

        if self.nr != len(bpy.data.objects[active_muscle].data.splines[0].points):
            active_muscle_points = bpy.data.objects[global_properties.active_muscle.get(context.scene)].data.splines[0]
            x = active_muscle_points.points[self.nr-1].co[0]
            y = active_muscle_points.points[self.nr-1].co[1]
            z = active_muscle_points.points[self.nr-1].co[2]
            w = active_muscle_points.points[self.nr-1].co[3]

            active_muscle_points.points[self.nr-1].co = active_muscle_points.points[self.nr].co
            active_muscle_points.points[self.nr].co = [x,y,z,w]

            # move coordFrame
            frame = bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.nr-1].coordFrame
            bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.nr-1].coordFrame = \
                bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.nr].coordFrame
            bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.nr].coordFrame = frame

        return {'FINISHED'}

   # def invoke(self, context, event):
   #     return context.window_manager.invoke_props_dialog(self)



## select segment to be assigned to muscle
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectSegmentMuscle(RDOperator):
    """
    :term:`Operator<operator>` for selecting a segment. If :attr:`segment_name` is empty,
    all segments will be deselected
    """
    bl_idname = config.OPERATOR_PREFIX + "select_segment_muscle"
    bl_label = "Select Segment to attach muscle pathpoint"

    segment_name = StringProperty()
    pathpoint_nr = IntProperty(default=1)

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

        bpy.data.objects[active_muscle].RobotEditor.muscles.pathPoints[self.pathpoint_nr-1].coordFrame = self.segment_name

        ### hook pathpoint to segment
        active_muscle = global_properties.active_muscle.get(context.scene)
        active_model = global_properties.model_name.get(context.scene)

        muscle_object = bpy.data.objects[active_muscle]
        # set curve active object

 #       hok = muscle_object.modifiers.new(name=active_muscle + '_' + str(self.pathpoint_nr-1), type='HOOK')
 #       hok.object = bpy.data.objects[active_model]
 #       hok.subtarget = self.segment_name
 #       hok.falloff_type = 'NONE'

 #       context.scene.objects.active = bpy.data.objects[active_muscle]
 #       bpy.ops.object.mode_set(mode='EDIT')
 #       muscle_object.data.splines[0].points[self.pathpoint_nr-1].select = True

 #       bpy.ops.object.hook_assign(modifier=hok.name)

        bpy.ops.object.mode_set(mode='OBJECT')

        bpy.context.scene.objects.active = bpy.data.objects[active_model]


        ## todo recalculate coord system


        return {'FINISHED'}

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
    :term:`operator` for deleting a the selected segment *ALL* of its children.


    """
    bl_idname = config.OPERATOR_PREFIX + "calc_muscle_length"
    bl_label = ""

    muscle = bpy.props.StringProperty()

    @RDOperator.OperatorLogger
    def execute(self, context):

        active_muscle = global_properties.active_muscle.get(context.scene)

        leng = 0.0

        spline = bpy.data.objects[active_muscle].data.splines[0]

        print("hallo")

        for i in range(0, len(spline.points) - 1):
            x = spline.points[i].co[0] - spline.points[i + 1].co[0]
            y = spline.points[i].co[1] - spline.points[i + 1].co[1]
            z = spline.points[i].co[2] - spline.points[i + 1].co[2]

            leng += math.sqrt((x ** 2) + (y ** 2) + (z ** 2))

        bpy.data.objects[self.muscle].RobotEditor.muscles.length = leng


        return {'FINISHED'}

