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
# Copyright (c) 2015, Karlsruhe Institute of Technology (KIT)
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######

# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty

# RobotDesigner imports
from ..core import config, PluginManager, RDOperator
from .helpers import (
    ModelSelected,
    SingleMeshSelected,
    ObjectMode,
    SingleSegmentSelected,
)
from ..core.logfile import operator_logger
from ..properties.globals import global_properties


# operator to select mesh
@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectGeometry(RDOperator):
    """
    :ref:`Operator <operator>` for selecting a geometry (:class:`bpy.types.Object` with `bpy.types.Mesh` data)
    second to the selected model (Blender object with :class:`bpy.types.Armature` data)
    """

    bl_idname = config.OPERATOR_PREFIX + "select_geometry"
    bl_label = "Select Geometry"

    geometry_name: StringProperty()

    @classmethod
    def run(cls, geometry_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):
        mesh = bpy.data.objects[self.geometry_name]

        if mesh.type != "MESH":
            self.report({"ERROR"}, "Object is no geometry (Mesh). Is {}".format(mesh.type))
            global_properties.mesh_name.set(context.scene, "Search")
            return {"FINISHED"}

        # Has the side effect of de-selecting all other objects except for the armature and our mesh.
        global_properties.mesh_name.set(context.scene, self.geometry_name)

        #    context.region.tag_redraw()
        #    context.area.tag_redraw()
        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectWrappingObject(RDOperator):
    """
    :ref:`Operator <operator>` for selecting a wrapping object (:class:`bpy.types.Object` with `bpy.types.Mesh` data)
    second to the selected model (Blender object with :class:`bpy.types.Armature` data)
    """

    bl_idname = config.OPERATOR_PREFIX + "select_wrappingobject"
    bl_label = "Select Wrapping Object"

    wrapping_name: StringProperty()

    @classmethod
    def run(cls, wrapping_name=""):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):
        mesh = bpy.data.objects[self.wrapping_name]

        if mesh.type != "MESH" or mesh.RobotDesigner.tag != "WRAPPING":
            self.report({"ERROR"}, "Object is no wrapping geometry (Mesh). Is {}".format(mesh.type))
            global_properties.wrapping_name.set(context.scene, "Search")
            return {"FINISHED"}

        # Has the side effect of de-selecting all other objects except for the armature and our mesh.
        global_properties.wrapping_name.set(context.scene, self.wrapping_name)

        #    context.region.tag_redraw()
        #    context.area.tag_redraw()
        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected, SingleSegmentSelected)
@PluginManager.register_class
class RenameGeometry(RDOperator):
    """
    :term:`operator` for renaming the selected mesh
    """

    bl_idname = config.OPERATOR_PREFIX + "rename_mesh"
    bl_label = "Rename Selected Mesh"
    new_name: StringProperty(name="Enter new name:")

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        mesh_name = global_properties.mesh_name.get(context.scene)
        current_mesh = bpy.data.objects[mesh_name]
        current_mesh.name = self.new_name
        bpy.data.scenes["Scene"].RobotDesigner.mesh_name = current_mesh.name
        bpy.data.objects[current_mesh.name].RobotDesigner.fileName = current_mesh.name
        global_properties.mesh_name.set(context.scene, current_mesh.name)
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    @classmethod
    def run(cls, new_name=""):
        return super().run(**cls.pass_keywords())


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected, SingleSegmentSelected)
@PluginManager.register_class
class AssignGeometry(RDOperator):
    """
    :ref:`operator` for assigning a geometry to a segment.
    """

    bl_idname = config.OPERATOR_PREFIX + "assign_geometry"
    bl_label = "Assign Selected Geometry to Active Segment"

    attach_collision_geometry: BoolProperty(
        name="Assign as Collision Mesh",
        description="Adds a collision tag to the mesh",
        default=False,
    )

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected, SingleSegmentSelected)
    def execute(self, context):
        # Set parenting relation. There are two ways to attach geometry to a bone:
        # This way, which sets the parent_bone variable of the object. Or by using vertex weights,
        # in which case parent_bone should be left empty.
        # See also https://blender.stackexchange.com/questions/9200/make-object-a-a-parent-of-object-b-via-python
        # At this point bpy.context.scene.objects.active should point to the armature which will be the parent.
        bpy.ops.object.parent_set(type="BONE", keep_transform=True)
        # In order to get the child we have to jump through some hoops.
        obj = bpy.data.objects[global_properties.mesh_name.get(context.scene)]

        # Change the name depending on whether we want collision geometry or visual geometry.

        def maybe_remove_prefix(s, prefix):
            return s[len(prefix) :] if s.startswith(prefix) else s

        def maybe_remove_postfix(s, postfix):
            return s[: -len(postfix)] if s.endswith(postfix) else s

        new_name = obj.name
        new_name = maybe_remove_postfix(
            new_name, ".001"
        )  # Heuristic to remove the suffix created by cloning.
        # Heuristics to remove previously assigned prefixes.
        # Since the prefix is regenerated it seems in order to try to remove the old prefix.
        if len(new_name) > len("VIS_"):
            new_name = maybe_remove_prefix(new_name, "VIS_")
        if len(new_name) > len("COL_"):
            new_name = maybe_remove_prefix(new_name, "COL_")

        operator_logger.info(
            "Attaching {} to {}".format("COL" if self.attach_collision_geometry else "VIS",
             obj.name)
        )

        if (
            self.attach_collision_geometry
            and obj.RobotDesigner.tag != "COLLISION"
            and "BASIC_COLLISION_" not in obj.RobotDesigner.tag
        ):
            obj.RobotDesigner.tag = "COLLISION"
            new_name = "COL_" + new_name
        elif (
            obj.RobotDesigner.tag == "COLLISION"
            or "BASIC_COLLISION_" in obj.RobotDesigner.tag
        ):
            pass
        else:
            obj.RobotDesigner.tag = "DEFAULT"
            new_name = "VIS_" + new_name
        obj.name = new_name
        obj.RobotDesigner.fileName = new_name
        # Update the global reference to the selected mesh.
        global_properties.mesh_name.set(context.scene, obj.name)
        # This is just a boolean variable which is reset here to False. It helps
        # determine whether we want a collision mesh or a visual one.

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class RenameAllGeometries(RDOperator):
    """
    :ref:`operator` for renaming geometries using their parented segment's name.
    """

    bl_idname = config.OPERATOR_PREFIX + "rename_geometries"
    bl_label = "Rename Geometries After Segments"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        import collections

        mesh_name = global_properties.mesh_name.get(context.scene)
        current_mesh = bpy.data.objects[mesh_name]
        armature = context.active_object
        # Blender automatically renames duplicate mesh names. However this apparently comes at a later stage.
        # Too late to make the filename member unique. Therefore let's keep track of duplicate names by ourselves.
        duplication_count = collections.defaultdict(int)
        for i in armature.children:
            if i.parent_bone != "" and i.type == "MESH":
                new_name = i.name.split("_")[0] + "_" + i.parent_bone
                num = duplication_count[new_name]
                duplication_count[new_name] = num + 1
                if num > 0:
                    new_name += "_%i" % num
                i.name = new_name
                i.RobotDesigner.fileName = new_name

        global_properties.mesh_name.set(
            context.scene, current_mesh.name[:4] + current_mesh.parent_bone
        )

        return {"FINISHED"}


# operator to unassign mesh from bone
@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class DetachGeometry(RDOperator):
    """
    :term:`operator` for detaching a single :term:`geometry` form a :term:`segment`.
    """

    bl_idname = config.OPERATOR_PREFIX + "unassignmesh"
    bl_label = "Detach Selected Geometry"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):
        from . import segments, model

        mesh_name = global_properties.mesh_name.get(context.scene)
        current_mesh = bpy.data.objects[mesh_name]
        mesh_global = current_mesh.matrix_world
        current_mesh.parent = None
        current_mesh.RobotDesigner.tag = "DEFAULT"
        if current_mesh.name.startswith("VIS_") or current_mesh.name.startswith("COL_"):
            current_mesh.name = current_mesh.name[4:]
        elif current_mesh.name.startswith("BASCOL_"):
            current_mesh.name = current_mesh.name[7:]

        current_mesh.matrix_world = mesh_global

        global_properties.mesh_name.set(context.scene, current_mesh.name)

        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class DetachAllGeometries(RDOperator):
    """
    :ref:`operator` for detaching *all* :term:`geometries` from the selected :term:`model`.
    """

    bl_idname = config.OPERATOR_PREFIX + "unassignallmeshes"
    bl_label = "Detach All Geometries"

    confirmation: BoolProperty(
        name="This disconnects all collision OR visual geometries from the model. Are you sure?"
    )

    @classmethod
    def run(cls, confirmation=True):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):
        mesh_type = global_properties.display_mesh_selection.get(context.scene)
        if mesh_type == "all":
            meshes = [
                obj
                for obj in bpy.data.objects
                if obj.type == "MESH"
                and obj.parent_bone != ""
                and obj.RobotDesigner.tag != "WRAPPING"
                and obj.RobotDesigner.tag != "PHYSICS_FRAME"
            ]
        elif mesh_type == "visual":
            meshes = [
                obj
                for obj in bpy.data.objects
                if obj.type == "MESH"
                and obj.parent_bone != ""
                and obj.RobotDesigner.tag == "DEFAULT"
            ]
        elif mesh_type == "collision":
            meshes = [
                obj
                for obj in bpy.data.objects
                if obj.type == "MESH"
                and obj.parent_bone != ""
                and obj.RobotDesigner.tag == "COLLISION"
            ]
        elif mesh_type == "bascol":
            meshes = [
                obj
                for obj in bpy.data.objects
                if obj.type == "MESH"
                and obj.parent_bone != ""
                and "BASIC_COLLISION_" in obj.RobotDesigner.tag
            ]
        else:
            self.confirmation = False

        if self.confirmation:
            for mesh in meshes:
                SelectGeometry.run(geometry_name=mesh.name)
                DetachGeometry.run()
                if mesh.name.startswith("VIS_") or mesh.name.startswith("COL_"):
                    mesh.name = mesh.name[4:]
                    mesh.RobotDesigner.tag = "DEFAULT"
                elif mesh.name.startswith("BASCOL_"):
                    mesh.name = mesh.name[7:]
                    mesh.RobotDesigner.tag = "DEFAULT"

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class SelectAllGeometries(RDOperator):
    """
    :ref:`operator` for selecting all geometries.


    """

    bl_idname = config.OPERATOR_PREFIX + "setallmeshesactiveobject"
    bl_label = "Make All Geometries Active"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ObjectMode)
    def execute(self, context):
        meshes = {
            obj.name
            for obj in context.scene.objects
            if not obj.parent_bone is None and obj.type == "MESH"
        }
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_all(action="DESELECT")

        for mesh in meshes:
            bpy.data.objects[mesh].select_set(True)
            context.view_layer.objects.active = bpy.data.objects[mesh]

        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected, ObjectMode, SingleMeshSelected)
@PluginManager.register_class
class SetGeometryActive(RDOperator):
    """
    :ref:`operator` for ...
    """

    bl_idname = config.OPERATOR_PREFIX + "setseletedmeshactiveobject"
    bl_label = "Make Geometry Active"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        selected = [i.name for i in bpy.context.selected_objects if i.type == "MESH"][0]
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[selected].select_set(True)
        context.view_layer.objects.active = bpy.data.objects[selected]
        return {"FINISHED"}


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class ReduceAllGeometry(RDOperator):
    """
    :term:`operator` for reducing the polygon number of all meshes in the scene.


    """

    bl_idname = config.OPERATOR_PREFIX + "polygonallreduction"
    bl_label = "Apply to All Meshes"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, SingleMeshSelected)
    def execute(self, context):
        armature = context.active_object

        hide_geometry = global_properties.display_mesh_selection.get(context.scene)
        meshes = [
            obj
            for obj in armature.children
            if obj.parent_bone is not None and obj.type == "MESH"
        ]

        if hide_geometry != "all":
            meshes = [
                item
                for item in meshes
                if (
                    hide_geometry == "collision"
                    and item.RobotDesigner.tag == "COLLISION"
                )
                or (hide_geometry == "visual" and item.RobotDesigner.tag == "DEFAULT")
            ]

        mesh_names = [m.name for m in meshes]
        del meshes  # Don't want to get into trouble with danling pointers again.

        ratio_act = (
            bpy.data.objects[global_properties.mesh_name.get(context.scene)]
            .modifiers["Decimate"]
            .ratio
        )
        for selected_mesh in mesh_names:
            obj = bpy.data.objects[selected_mesh]
            try:
                obj.modifiers["Decimate"].ratio = ratio_act
            except KeyError:
                obj.modifiers.new("Decimate", "DECIMATE").ratio = ratio_act

        return {"FINISHED"}
