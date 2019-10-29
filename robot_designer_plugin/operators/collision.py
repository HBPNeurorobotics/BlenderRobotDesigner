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
"""
Sphinx-autodoc tag
"""

# ######
# System imports
import os
import sys
# import math

# ######
# Blender imports
import bpy
from bpy.props import FloatProperty, IntProperty, StringProperty
# import mathutils
import bmesh

# ######
# RobotDesigner imports
from ..core import config, PluginManager, RDOperator
from .helpers import ModelSelected, SingleMeshSelected
from .rigid_bodies import SelectGeometry, AssignGeometry
from .segments import SelectSegment
from .model import SelectModel
from ..properties.globals import global_properties

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class GenerateAllCollisionMeshes(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "generatallecollisionmeshes"
    bl_label = "Generate All Collision Meshes"

    shrinkWrapOffset = FloatProperty(name="Shrinkwrap Offset", default=0.001,
                                     unit='LENGTH', min=0, max=0.5)
    subdivisionLevels = IntProperty(name="Subdivision Levels", default=2)

    @RDOperator.OperatorLogger
    # @Postconditions(ModelSelected)
    def execute(self, context):
        visuals = [o.name for o in context.scene.objects if o.type == 'MESH'
                   and o.parent == context.active_object and o.RobotDesigner.tag != "COLLISION"]

        self.logger.debug("Visuals: %s", visuals)

        for i in visuals:
            SelectGeometry.run(geometry_name=i)
            GenerateCollisionMesh.run(shrinkWrapOffset=self.shrinkWrapOffset, subdivisionLevels=self.subdivisionLevels)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class GenerateAllCollisionConvexHull(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "generatallecollisionconvexhull"
    bl_label = "Generate convex hulls for all collision meshes"

    @RDOperator.OperatorLogger
    # @Postconditions(ModelSelected)
    def execute(self, context):
        visuals = [o.name for o in context.scene.objects if o.type == 'MESH'
                   and o.parent == context.active_object and o.RobotDesigner.tag != "COLLISION"]

        self.logger.debug("Visuals: %s", visuals)

        for i in visuals:
            self.logger.debug("Compute convex hull for: " + i)
            SelectGeometry.run(geometry_name=i)
            GenerateCollisionConvexHull.run()

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class GenerateCollisionMesh(RDOperator):
    """
    :ref:`operator` for creating a collision mesh using the builtin
    subdivide and shrinkwrap operators.

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "generatecollisionmesh"
    bl_label = "Generate Collision Mesh for selected"

    shrinkWrapOffset = FloatProperty(name="Shrinkwrap Offset", default=0.001,
                                     unit='LENGTH', min=0, max=0.5)
    subdivisionLevels = IntProperty(name="Subdivision Levels", default=2)

    @classmethod
    def run(cls, shrinkWrapOffset, subdivisionLevels):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        from . import segments, model

        target_name = [i.name for i in bpy.context.selected_objects if i.type == 'MESH'][0]
        self.logger.debug("Creating Collision mesh for: %s", target_name)
        armature = context.active_object.name

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects[target_name]

        d = bpy.data.objects[target_name].dimensions
        bpy.ops.mesh.primitive_cube_add(
            location=bpy.data.objects[target_name].location,
            rotation=bpy.data.objects[target_name].rotation_euler)
        bpy.context.object.dimensions = d * 1000000
        bpy.ops.object.transform_apply(scale=True)
        mod = bpy.context.object.modifiers.new(name='subsurf', type='SUBSURF')
        mod.subdivision_type = 'SIMPLE'
        mod.levels = self.subdivisionLevels
        bpy.ops.object.modifier_apply(modifier='subsurf')
        mod = bpy.context.object.modifiers.new(name='shrink_wrap',
                                               type='SHRINKWRAP')
        mod.wrap_method = "NEAREST_SURFACEPOINT"
        mod.offset = self.shrinkWrapOffset * 1000
        self.logger.debug("%f, %f", mod.offset, self.shrinkWrapOffset)
        mod.target = bpy.data.objects[target_name]
        bpy.ops.object.modifier_apply(modifier='shrink_wrap')

        if not bpy.context.object.name.startswith("COL_"):
            bpy.context.object.name = 'COL_' + target_name[4:]
        name = bpy.context.object.name

        context.active_object.RobotDesigner.tag = 'COLLISION'
        self.logger.debug("Created mesh: %s", bpy.context.active_object.name)

        if 'RD_COLLISON_OBJECT_MATERIAL' in bpy.data.materials:
            bpy.ops.object.material_slot_add()
            context.active_object.data.materials[0] = bpy.data.materials[
                'RD_COLLISON_OBJECT_MATERIAL']
            self.logger.debug("Assigned material to : %s",
                              bpy.context.active_object.name)
        else:
            self.logger.debug("Could not find material for collision mesh")

        bpy.ops.object.select_all(action='DESELECT')

        model.SelectModel.run(model_name=armature)
        segments.SelectSegment.run(segment_name=bpy.data.objects[target_name].parent_bone)
        bpy.data.objects[name].select = True
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)
        bpy.ops.object.select_all(action='DESELECT')
        model.SelectModel.run(model_name=armature)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected, SingleMeshSelected)
@PluginManager.register_class
class GenerateCollisionConvexHull(RDOperator):
    """
    :ref:`operator` for creating a collision mesh using the builtin
    convex hull computation.

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "generateconvexhull"
    bl_label = "Generate convex hull for selected"

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    def execute(self, context):
        from . import segments, model

        target_name = [i.name for i in bpy.context.selected_objects if i.type == 'MESH'][0]

        self.logger.debug("Creating Collision mesh for: %s", target_name)
        armature = context.active_object.name

        cv_hull_obj_name = 'COL_' + target_name[4:] + "_convex_hull"

        bpy.ops.object.select_all(action='DESELECT')

        exp_object = bpy.data.objects[target_name]
        orig_object = bpy.data.objects[target_name]

        orig_object.select = True
        orig_object.name = target_name + "_CONVEX_HULL_TMP_OBJECT"
        bpy.ops.object.duplicate()

        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH' and obj.name == target_name + "_CONVEX_HULL_TMP_OBJECT" + ".001":
                obj.name = cv_hull_obj_name
                obj.select = True
                exp_object.select = False
                exp_object = obj

        try:
            collisionMesh = exp_object.data
            self.logger.debug("Got collision mesh input")
            bm = bmesh.new()  # create an empty BMesh
            self.logger.debug("Created new bmesh object")

            bm.from_mesh(collisionMesh)  # fill it in from a Mesh
            self.logger.debug("Filled bmesh object with data")

            verts = [v for v in bm.verts if (not v.hide)]
            edges = [e for e in bm.edges if (not e.hide)]
            faces = [f for f in bm.faces if (not f.hide)]

            cv_input = bm.verts  # (verts, edges, faces)
            # Set use_existing_faces=False so that all new geometry is added to the mesh 'bm'.
            # Then we can go and delete everything that is not in the output of the operator.
            # This will leave only the convex hull.
            # Why? I noticed that under some conditions, where are leftover faces/vertices
            # from the original mesh. I believe this happens when the input mesh is not a closed
            # manifold, i.e. not topologically a sphere-like.
            new = bmesh.ops.convex_hull(bm, input=cv_input, use_existing_faces=False)

            self.logger.debug("Convex hull computation done.")

            # To delete leftover vertices and faces.
            # https://blender.stackexchange.com/questions/1541/how-can-i-delete-mesh-parts-with-python
            # enum {
            # DEL_VERTS = 1,
            # DEL_EDGES,
            # DEL_ONLYFACES,
            # DEL_EDGESFACES,
            # DEL_FACES,
            # DEL_ALL,
            # DEL_ONLYTAGGED
            # };
            new = set(new["geom"])
            to_delete = [v for v in bm.verts if not v in new]
            bmesh.ops.delete(bm, geom=to_delete, context=1)
            to_delete = [f for f in bm.faces if not f in new]
            bmesh.ops.delete(bm, geom=to_delete, context=5)

            bmesh.ops.recalc_face_normals(bm, faces=bm.faces)

            bm.to_mesh(collisionMesh)
            bm.free()

            exp_object.select = True

            exp_object.RobotDesigner.tag = 'COLLISION'
            self.logger.debug("Created mesh: %s", exp_object.name)

            orig_object.name = target_name

            bpy.ops.object.select_all(action='DESELECT')

            if 'RD_COLLISON_OBJECT_MATERIAL' in bpy.data.materials:
                bpy.ops.object.material_slot_add()
                context.active_object.data.materials[0] = bpy.data.materials[
                    'RD_COLLISON_OBJECT_MATERIAL']
                self.logger.debug("Assigned material to : %s",
                                  bpy.context.active_object.name)
            else:
                self.logger.debug("Could not find material for collision mesh")

            bpy.ops.object.select_all(action='DESELECT')
            model.SelectModel.run(model_name=armature)
            segments.SelectSegment.run(segment_name=bpy.data.objects[target_name].parent_bone)
            bpy.data.objects[cv_hull_obj_name].select = True
            bpy.ops.object.parent_set(type='BONE', keep_transform=True)
            model.SelectModel.run(model_name=armature)

        except Exception as e:
            orig_object.name = target_name
            self.logger.info("Exception when computing convex hull")
            self.logger.info(type(e))
            self.logger.info(e)
            return {'CANCELLED'}

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateBasicCollisionBox(RDOperator):
    """
    :ref:`operator` for creating a basic collision box

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "create_basic_collision_box"
    bl_label = "Create Basic Collision Box"

    cube_name = StringProperty(name="Enter name: ")

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

        model = context.active_object
        segment = model.data.bones.active
        bpy.ops.mesh.primitive_cube_add(radius=0.5)
        cube = context.active_object
        cube.name = "BASCOL_" + self.cube_name
        bpy.data.objects[cube.name].RobotDesigner.tag = 'BASIC_COLLISION_BOX'

        mat = bpy.data.materials.new('blue')
        mat.diffuse_color = (0, 0, 1)
        mat.use_transparency = True
        mat.alpha = 0.3
        bpy.data.objects[cube.name].show_transparent = True
        cube.data.materials.append(mat)

        bpy.ops.object.select_all(action='DESELECT')
        SelectModel.run(model_name=model.name)
        SelectGeometry.run(geometry_name=cube.name)
        SelectSegment.run(segment_name=segment.name)
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateBasicCollisionCylinder(RDOperator):
    """
    :ref:`operator` for creating a basic collision cylinder

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "create_basic_collision_cylinder"
    bl_label = "Create Basic Collision Cylinder"

    cylinder_name = StringProperty(name="Enter name: ")

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

        model = context.active_object
        segment = model.data.bones.active
        bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=1.0)
        cylinder = context.active_object
        cylinder.name = "BASCOL_" + self.cylinder_name
        bpy.data.objects[cylinder.name].RobotDesigner.tag = 'BASIC_COLLISION_CYLINDER'

        mat = bpy.data.materials.new('blue')
        mat.diffuse_color = (0, 0, 1)
        mat.use_transparency = True
        mat.alpha = 0.3
        bpy.data.objects[cylinder.name].show_transparent = True
        cylinder.data.materials.append(mat)

        bpy.ops.object.select_all(action='DESELECT')
        SelectModel.run(model_name=model.name)
        SelectGeometry.run(geometry_name=cylinder.name)
        SelectSegment.run(segment_name=segment.name)
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class CreateBasicCollisionSphere(RDOperator):
    """
    :ref:`operator` for creating a basic collision sphere

    **Preconditions:**

    **Postconditions:**
    """
    bl_idname = config.OPERATOR_PREFIX + "create_basic_collision_sphere"
    bl_label = "Create Basic Collision Sphere"

    sphere_name = StringProperty(name="Enter name: ")

    @classmethod
    def run(cls):
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

        model = context.active_object
        segment = model.data.bones.active
        bpy.ops.mesh.primitive_uv_sphere_add(size=1.0)
        sphere = context.active_object
        sphere.name = "BASCOL_" + self.sphere_name
        bpy.data.objects[sphere.name].RobotDesigner.tag = 'BASIC_COLLISION_SPHERE'

        mat = bpy.data.materials.new('blue')
        mat.diffuse_color = (0, 0, 1)
        mat.use_transparency = True
        mat.alpha = 0.3
        bpy.data.objects[sphere.name].show_transparent = True
        sphere.data.materials.append(mat)

        bpy.ops.object.select_all(action='DESELECT')
        SelectModel.run(model_name=model.name)
        SelectGeometry.run(geometry_name=sphere.name)
        SelectSegment.run(segment_name=segment.name)
        bpy.ops.object.parent_set(type='BONE', keep_transform=True)

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
