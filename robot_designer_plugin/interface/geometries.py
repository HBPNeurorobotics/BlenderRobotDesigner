
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
#   2015:       Stefan Ulbrich (FZI), Gui redesigned
#   2015-01-16: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#   2017-07:    Benedikt Feldotto (TUM), Polygon reduction, Geometry properties and scaling
# ######

# Blender imports
import bpy

# RobotDesigner imports
from .model import check_armature

from . import menus
from ..operators import rigid_bodies, soft_bodies, collision, mesh_generation, segments
from .helpers import (
    drawInfoBox,
    info_list,
    getSingleSegment,
    ConnectGeometryBox,
    DisconnectGeometryBox,
    CollisionBox,
    GeometrySettingsBox,
    PolygonReductionBox,
    MeshGenerationBox,
    DeformableBox,
)
from ..core.gui import InfoBox
from ..properties.globals import global_properties
from .helpers import SDFCollisionPropertiesBox
from .helpers import BounceBox, FrictionBox, ContactBox, SoftContactBox
from ..core.logfile import LogFunction


@LogFunction
def draw(layout, context):
    """
    Draws the user interface for geometric modelling.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return

    if len([i for i in context.selected_objects if i.type == "MESH"]) == 0:
        info_list.append("No mesh selected")
    elif len(context.selected_objects) > 2:
        info_list.append("Too many objects selected")

    box = layout.box()
    row = box.row(align=True)
    row.label(text="Mesh Type:")
    global_properties.mesh_type.prop(context.scene, row, expand=True)
    row = box.row(align=True)
    row.label(text="Show:")
    global_properties.display_mesh_selection.prop(context.scene, row, expand=True)

    if 1:
        row = box.row()
        column = row.column(align=True)
        column.label(text="Segment Selector")
        # Start of segment menu code.
        single_segment = getSingleSegment(context)
        column.menu(
            menus.SegmentsGeometriesMenu.bl_idname,
            text=single_segment.name if single_segment else "",
        )
        row2 = column.row(align=True)
        global_properties.list_segments.prop(
            context.scene, row2, expand=True, icon_only=True
        )

        global_properties.segment_name.prop_search(
            context.scene,
            row2,
            context.active_object.data,
            "bones",
            icon="VIEWZOOM",
            text="",
        )
        # End of segment menu code.
        column = row.column(align=True)
        column.label(text="Mesh Selector")
        menus.GeometriesMenu.putMenu(column, context)

    mesh_obj = bpy.data.objects[global_properties.mesh_name.get(context.scene)]

    box = GeometrySettingsBox.get(
        layout, context, "Geometry Properties", icon="PREFERENCES"
    )
    if box:
        infoBox = InfoBox(box)
        row = box.row()
        column = row.column(align=True)
        rigid_bodies.SetGeometryActive.place_button(column, infoBox=infoBox)
        rigid_bodies.SelectAllGeometries.place_button(column, infoBox=infoBox)
        rigid_bodies.RenameAllGeometries.place_button(column, infoBox=infoBox)

        selected_objects = [
            i for i in context.selected_objects if i.name != context.active_object.name
        ]
        if len(selected_objects):
            obj = bpy.data.objects[global_properties.mesh_name.get(context.scene)]
            rigid_bodies.RenameGeometry.place_button(
                column, text="Rename Selected Geometry", infoBox=infoBox
            )
            box.prop(mesh_obj, "rotation_euler", slider=False, text="Rotation")
            box.prop(mesh_obj, "location", slider=False, text="Location")
            row2 = box.row()
            column = row2.column(align=True)
            if obj.RobotDesigner.tag == "BASIC_COLLISION_CYLINDER":
                column.label(text="Scale (%s)" % obj.name)
                column.prop(
                    mesh_obj.RobotDesigner.scaling,
                    "scale_radius",
                    slider=False,
                    text="Radius",
                )
                column.prop(
                    mesh_obj.RobotDesigner.scaling,
                    "scale_depth",
                    slider=False,
                    text="Depth",
                )
            elif obj.RobotDesigner.tag == "BASIC_COLLISION_SPHERE":
                column.label(text="Scale (%s)" % obj.name)
                column.prop(
                    mesh_obj.RobotDesigner.scaling,
                    "scale_all",
                    slider=False,
                    text="Radius",
                )
            else:
                box.prop(mesh_obj, "scale", slider=False, text="Scale (%s)" % obj.name)
            box.prop(selected_objects[0].RobotDesigner, "fileName")

        box.separator()
        infoBox.draw_info()

    box = ConnectGeometryBox.get(layout, context, "Attach Geometry", icon="LINKED")
    if box:
        infoBox = InfoBox(box)
        row = box.row()

        row = box.column(align=True)
        rigid_bodies.AssignGeometry.place_button(row, infoBox=infoBox)
        segments.ConvertVertexMapSkinning.place_button(row, infoBox=infoBox)

        box.separator()
        infoBox.draw_info()

    box = DisconnectGeometryBox.get(layout, context, "Detach Geometry", icon="UNLINKED")
    if box:
        infoBox = InfoBox(box)
        row = box.row()

        column = row.column(align=True)
        rigid_bodies.DetachGeometry.place_button(column, infoBox=infoBox)
        rigid_bodies.DetachAllGeometries.place_button(column, infoBox=infoBox)

        box.separator()
        infoBox.draw_info()

    if global_properties.mesh_type.get(context.scene) == "DEFAULT":
        box = CollisionBox.get(
            layout, context, "Generate collision meshes", icon="SURFACE_NCURVE"
        )
        if box:
            infoBox = InfoBox(box)
            row = box.row()

            column = row.column(align=True)
            collision.GenerateAllCollisionMeshes.place_button(column, infoBox=infoBox)
            collision.GenerateCollisionMesh.place_button(column, infoBox=infoBox)
            collision.GenerateAllCollisionConvexHull.place_button(
                column, infoBox=infoBox
            )
            collision.GenerateCollisionConvexHull.place_button(column, infoBox=infoBox)

            row2 = box.row()
            row2.label(text="Add Basic Collision Geometry:")
            row3 = box.row()
            column = row3.column(align=True)
            collision.CreateBasicCollisionBox.place_button(
                column, text="Create Box", infoBox=infoBox
            )

            column = row3.column(align=True)
            collision.CreateBasicCollisionCylinder.place_button(
                column, text="Create Cylinder", infoBox=infoBox
            )

            column = row3.column(align=True)
            collision.CreateBasicCollisionSphere.place_button(
                column, text="Create Sphere", infoBox=infoBox
            )

            box.row()
            infoBox.draw_info()

    box = MeshGenerationBox.get(
        layout, context, "Generate geometry", icon="MOD_TRIANGULATE"
    )
    if box:
        infoBox = InfoBox(box)
        row = box.row()

        column = row.column(align=True)
        mesh_generation.GenerateMeshFromSegment.place_button(column, infoBox=infoBox)
        mesh_generation.GenerateMeshFromAllSegment.place_button(column, infoBox=infoBox)
        box.separator()
        infoBox.draw_info()

    box = DeformableBox.get(
        layout, context, "Deformable Geometries", icon="STYLUS_PRESSURE"
    )
    if box:
        infoBox = InfoBox(box)
        row = box.row()

        column = row.column(align=True)
        soft_bodies.ConvertSoftBodies.place_button(column, infoBox=infoBox)
        box.separator()
        infoBox.draw_info()

    box = PolygonReductionBox.get(
        layout, context, "Polygon Reduction", icon="MOD_DECIM"
    )
    if box:
        infoBox = InfoBox(box)
        row = box.row()
        row.alignment = "EXPAND"
        column = row.column(align=True)

        try:
            column.prop(
                mesh_obj.modifiers["Decimate"], "ratio", slider=False, text="Ratio"
            )
        except KeyError:
            mesh_obj.modifiers.new("Decimate", "DECIMATE")
            column.prop(
                mesh_obj.modifiers["Decimate"], "ratio", slider=False, text="Ratio"
            )

        row2 = column.row()
        rigid_bodies.ReduceAllGeometry.place_button(row2, infoBox=infoBox)

        box.separator()
        infoBox.draw_info()

    if mesh_obj.RobotDesigner.tag == "COLLISION":
        SDFbox = SDFCollisionPropertiesBox.get(
            layout, context, "SDF Collision Surface Properties", icon="SHADING_WIRE"
        )
        if SDFbox:
            box1 = BounceBox.get(SDFbox, context, "Bounce")
            if box1:
                box1.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "restitution_coeff",
                    text="Restitution Coefficient",
                )
                box1.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "threshold",
                    text="Threshold",
                )
            box2 = FrictionBox.get(SDFbox, context, "Friction")
            if box2:
                box3 = box2.box()
                box3.label(text="Torsional Friction")
                box3.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "coefficient",
                    text="Coefficient",
                )
                box3.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "use_patch_radius",
                    text="Use Patch Radius",
                )
                box3.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "patch_radius",
                    text="Patch Radius",
                )
                box3.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "surface_radius",
                    text="Surface Radius",
                )
                box4 = box3.box()
                box4.label(text="ODE")
                box4.prop(mesh_obj.RobotDesigner.sdfCollisionProps, "slip", text="Slip")

                box5 = box2.box()
                box5.label(text="ODE")
                box5.prop(mesh_obj.RobotDesigner.sdfCollisionProps, "mu", text="Mu")
                box5.prop(mesh_obj.RobotDesigner.sdfCollisionProps, "mu2", text="Mu2")
                box5.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps, "fdir1", text="FDir1"
                )
                box5.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps, "slip1", text="Slip1"
                )
                box5.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps, "slip2", text="Slip2"
                )

            box6 = ContactBox.get(SDFbox, context, "Contact")
            if box6:
                box6.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "collide_wo_contact",
                    text="Collide Without Contact",
                )
                box6.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "collide_wo_contact_bitmask",
                    text="Collide without contact bitmask",
                )
                box6.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "collide_bitmask",
                    text="Collide Bitmask",
                )
                box6.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "category_bitmask",
                    text="Category Bitmask",
                )
                box6.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "poissons_ratio",
                    text="Poissons Ratio",
                )
                box6.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "elastic_modulus",
                    text="Elastic Modulus",
                )

                if (
                    bpy.data.objects[
                        global_properties.model_name.get(bpy.context.scene)
                    ].RobotDesigner.physics_engine
                    == "OPENSIM"
                ):
                    box7 = box6.box()
                    box7.label(text="Opensim")
                    box7.prop(
                        mesh_obj.RobotDesigner.sdfCollisionProps,
                        "osim_stiffness",
                        text="Stiffness",
                    )
                    box7.prop(
                        mesh_obj.RobotDesigner.sdfCollisionProps,
                        "osim_dissipation",
                        text="Dissipation",
                    )

                box8 = box6.box()
                box8.label(text="ODE")
                box8.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "soft_cfm",
                    text="Soft CMF",
                )
                box8.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "soft_erp",
                    text="Soft ERP",
                )
                box8.prop(mesh_obj.RobotDesigner.sdfCollisionProps, "kp", text="Kp")
                box8.prop(mesh_obj.RobotDesigner.sdfCollisionProps, "kd", text="Kd")
                box8.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps, "max_vel", text="Max. Vel"
                )
                box8.prop(
                    mesh_obj.RobotDesigner.sdfCollisionProps,
                    "min_depth",
                    text="Min. Depth",
                )

            if (
                bpy.data.objects[
                    global_properties.model_name.get(bpy.context.scene)
                ].RobotDesigner.physics_engine
                == "DART"
            ):
                box9 = SoftContactBox.get(SDFbox, context, "Soft Contact")
                if box9:
                    box9.row().label(text="Dart:")
                    box9.prop(
                        mesh_obj.RobotDesigner.sdfCollisionProps,
                        "bone_attachment",
                        text="Bone Attachment",
                    )
                    box9.prop(
                        mesh_obj.RobotDesigner.sdfCollisionProps,
                        "dart_stiffness",
                        text="Stifness",
                    )
                    box9.prop(
                        mesh_obj.RobotDesigner.sdfCollisionProps,
                        "damping",
                        text="Damping",
                    )
                    box9.prop(
                        mesh_obj.RobotDesigner.sdfCollisionProps,
                        "flesh_mass_fraction",
                        text="Flesh Mass Fraction",
                    )

    drawInfoBox(layout, context)
