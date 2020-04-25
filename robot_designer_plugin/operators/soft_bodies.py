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
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#   2015-01-7 : Initial implementation of functionality
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######
"""
Sphinx-autodoc tag
"""

# System imports
# import os
# import sys
# import math

# Blender imports
import bpy
from bpy.props import FloatProperty, BoolProperty
# import mathutils

# RobotDesigner imports
from ..core import config, PluginManager, RDOperator, Condition

from .helpers import SingleMeshSelected, ModelSelected, ObjectScaled


@RDOperator.Preconditions(SingleMeshSelected, ModelSelected, ObjectScaled)
@PluginManager.register_class
class ConvertSoftBodies(RDOperator):
    """
    Operator for making a deformable mesh (with an 'ARMATURE' modifier linked
    to the kinematics model.
    """

    bl_idname = config.OPERATOR_PREFIX + "disjoint_vertex_groups"
    bl_label = "Make Disjoint Vertex Groups"
    remove_overlaps: BoolProperty(name="Remove overlaps?")
    separate: BoolProperty(name="Separate by vertex groups?")
    assign_to_model: BoolProperty(name="Assign separated meshes to bones")

    smooth: BoolProperty(name="Smooth seams", default=False)
    solidify: BoolProperty(name="Make solid", default=False)

    t1: FloatProperty(name="Minimum weight", default=0.5, min=0.0, max=1.0)
    t2: FloatProperty(name="Maximum common weight", default=0.5, min=0.0,
                      max=1.0)

    thickness: FloatProperty(name="Thickness", unit='LENGTH', min=0.0, max=1.0, default=0.2)

    @RDOperator.OperatorLogger
    def execute(self, context):
        self.logger.debug("Running ConvertSoftBodies with parameters: %s %s", self.smooth, self.solidify)

        from .segments import SelectSegment
        from .rigid_bodies import SelectGeometry, AssignGeometry, SetGeometryActive
        from .model import SelectModel

        model_name = context.active_object.name

        # Find selected mesh
        selected = bpy.context.selected_objects
        selected.remove(context.active_object)
        mesh_object = selected[0]

        # Make object active
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        bpy.ops.object.select_all(action="DESELECT")
        mesh_object.select_set(True)
        context.view_layer.objects.active = mesh_object

        maxima = [0] * len(mesh_object.data.vertices)
        indices = [-1] * len(mesh_object.data.vertices)

        if self.remove_overlaps:
            self.logger.debug("Removing overlaps. Threshold: %s", self.t2)

        for v in mesh_object.data.vertices:
            for g in v.groups:

                # Already a vertex above the threshold is an overlap
                if self.remove_overlaps and g.weight > self.t2 and maxima[v.index] > self.t2:
                    indices[v.index] = -1
                # If not, check if it passes the minimal threshold
                elif g.weight > maxima[v.index]:
                    maxima[v.index] = g.weight
                    if g.weight > self.t1:
                        indices[v.index] = g.group






                        # if g.weight > maxima[v.index]:
                        #
                        #     if self.remove_overlaps:
                        #         if maxima[v.index] > self.t2:
                        #             indices[v.index] = -1
                        #         else:
                        #             indices[v.index] = g.group
                        #     else:
                        #         if g.weight > self.t1:
                        #             indices[v.index] = g.group
                        #
                        #     maxima[v.index] = g.weight

            # Remove vertex from all or all but one group. When removing the v.groups attribute changes so it has to
            # be copied first.
            vertex_groups_indices = [i.group for i in v.groups]
            for index in vertex_groups_indices:
                if indices[v.index] != index:
                    mesh_object.vertex_groups[index].remove([v.index])
            if v.index == -1 and 'RDNone' in mesh_object.vertex_groups:  # 'REPLACE', 'ADD', 'SUBTRACT')
                mesh_object.vertex_groups['RDNone'].add([v.index], 0.9, "ADD")

        if self.separate:
            for m in mesh_object.modifiers:
                if m.type == "ARMATURE":
                    mesh_object.modifiers.remove(m)

            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bone2object = {}
            for v in mesh_object.vertex_groups:
                bpy.ops.mesh.select_all(action="DESELECT")
                mesh_object.vertex_groups.active_index = v.index
                bpy.ops.object.vertex_group_select()
                try:
                    bpy.ops.mesh.separate(type='SELECTED')
                except RuntimeError:
                    pass
                selected = bpy.context.selected_objects
                selected.remove(context.active_object)
                if len(selected) == 1:
                    bone2object[v.name] = selected[0].name
                    selected[0].select = False

            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            for bone, object in bone2object.items():
                if self.smooth:
                    SelectModel.run(model_name=model_name)
                    SelectGeometry.run(geometry_name=object)
                    SetGeometryActive.run()
                    bpy.ops.object.mode_set(mode="EDIT", toggle=False)
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.region_to_loop()
                    bpy.ops.mesh.vertices_smooth(repeat=15)
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.delete_loose()
                    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                if self.solidify:
                    SelectModel.run(model_name=model_name)
                    SelectGeometry.run(geometry_name=object)
                    SetGeometryActive.run()
                    mod = bpy.context.object.modifiers.new(name='solidify', type='SOLIDIFY')
                    mod.thickness = self.thickness
                    bpy.ops.object.modifier_apply(modifier='solidify')

            if self.assign_to_model:

                for bone, object in bone2object.items():
                    try:

                        SelectModel.run(model_name=model_name)
                        if bone in bpy.context.active_object.data.bones:
                            SelectSegment.run(segment_name=bone)
                            SelectGeometry.run(geometry_name=object)
                            AssignGeometry.run()
                        else:
                            self.logger.error("Vertex group %s has no matching bone" % bone)
                    except KeyError:
                        self.logger.info("Vertex group %s has no matching bone" % bone)

        SelectModel.run(model_name=model_name)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.prop(self, "t1")
        row = layout.row(align=True)
        row.prop(self, "remove_overlaps")
        row.prop(self, "t2")
        row = layout.row()
        row.prop(self, "separate")
        row = layout.row()
        row.prop(self, "assign_to_model")
        row = layout.row()
        row.prop(self, "smooth")
        row = layout.row()
        row.prop(self, "solidify")
        row.prop(self, "thickness")
