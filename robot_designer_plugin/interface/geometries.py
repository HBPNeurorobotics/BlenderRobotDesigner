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
#
# ######

# Blender imports
import bpy

# RobotDesigner imports
from .model import check_armature

from . import menus
from ..operators import rigid_bodies, soft_bodies, collision, mesh_generation
from .helpers import drawInfoBox, info_list, getSingleSegment, ConnectGeometryBos, DisconnectGeometryBox, \
    CollisionBox, DeformableBox, MeshGenerationBox, create_segment_selector
from ..core.logfile import LogFunction
from ..core.gui import InfoBox
from ..core import PluginManager
from ..properties.globals import RDGlobals

@LogFunction
def create_geometry_selection(layout, context):
    """
    Creates a GUI element for selecting meshes

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    text = "Select Mesh"
    hide_mesh = context.scene.RobotEditor.listMeshes

    # Get selected meshes
    selected = [i for i in bpy.context.selected_objects if i.type == 'MESH']

    if len(selected) == 1:
        # if context.scene.RobotEditor.meshName in bpy.data.objects:
        #    if context.active_bone and not context.scene.RobotEditor.meshName == "":
        mesh = selected[0]
        if mesh.parent_bone and not hide_mesh == 'disconnected':
            text = mesh.name + " --> " + mesh.parent_bone
        # elif mesh.parent:
        #     meshMenuText = context.scene.RobotEditor.meshName + " --> " + mesh.parent.name
        elif not mesh.parent_bone and not hide_mesh == 'connected':
            text = mesh.name
        else:
            text = 'Select Mesh'

    layout.menu(menus.GeometriesMenu.bl_idname, text=text)
    row = layout.row(align=True)
    row.prop(context.scene.RobotEditor, "listMeshes", expand=True, icon_only=True)
    row.separator()
    row.prop_search(context.scene.RobotEditor, "meshName", context.scene.RobotEditor, 'connected_meshes',
                    icon='VIEWZOOM', text='')

    # layout.prop(context.scene.RobotEditor, "liveSearchMeshes", icon='VIEWZOOM', text="")


def draw(layout, context):
    """
    Draws the user interface for geometric modelling.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return

    if len([i for i in context.selected_objects if i.type=="MESH"])==0:
        info_list.append("No mesh selected")
    elif len(context.selected_objects)>2:
        info_list.append("Too many objects selected")

    box = layout.box()
    row = box.row(align=True)
    row.label("Mesh type:")
    row.prop(bpy.context.scene.RobotEditor, "meshType", expand=True)
    row = box.row(align=True)
    row.label("Show:")
    row.prop(bpy.context.scene.RobotEditor, "hideMeshType", expand=True)
    box.separator()

    box = DisconnectGeometryBox.get(layout, context, "Disconnect meshes", icon="UNLINKED")
    if box:
        infoBox = InfoBox(box)
        row = box.row()
        column = row.column(align=True)
        menus.GeometriesMenu.putMenu(column, context)
        print("test: ", menus.GeometriesMenu.bl_idname, menus.ConnectedObjectsMenu.bl_idname,
              menus.GeometriesMenu.blender_type, menus.ConnectedObjectsMenu.blender_type)
        #create_geometry_selection(column, context)

        column = row.column(align=True)
        rigid_bodies.DetachGeometry.place_button(column, infoBox=infoBox)
        rigid_bodies.DetachAllGeometries.place_button(column, infoBox=infoBox)
        rigid_bodies.RenameAllGeometries.place_button(column, infoBox=infoBox)
        rigid_bodies.SetGeometryActive.place_button(column, infoBox=infoBox)
        rigid_bodies.SelectAllGeometries.place_button(column, infoBox=infoBox)
        selected_objects = [i for i in context.selected_objects if i.name != context.active_object.name]
        if len(selected_objects):
            box.prop(selected_objects[0].RobotEditor, 'fileName')
        box.separator()
        infoBox.draw_info()


    box = ConnectGeometryBos.get(layout, context, "Connect geometry", icon="LINKED")
    if box:
        infoBox = InfoBox(box)
        row = box.row()
        column = row.column(align=True)


        single_segment = getSingleSegment(context)

        column.menu(menus.SegmentsGeometriesMenu.bl_idname,
                    text=single_segment.name if single_segment else "Select Segment")
        row2 = column.row(align=True)


        row2.prop(context.scene.RobotEditor, "listBones", expand=True, icon_only=True)
        row2.separator()
        row2.prop_search(context.scene.RobotEditor, "segment_name", context.active_object.data, 'bones',
                         icon='VIEWZOOM',
                         text='')

        column = row.column(align=True)
        menus.GeometriesMenu.putMenu(column, context)
        #create_geometry_selection(column, context)
        row = box.column(align=True)
        rigid_bodies.AssignGeometry.place_button(row, infoBox=infoBox)
        box.separator()
        infoBox.draw_info()



    if bpy.context.scene.RobotEditor.meshType == "DEFAULT":
        box = CollisionBox.get(layout, context, "Generate collision meshes", icon='SURFACE_NCURVE')
        if box:
            infoBox = InfoBox(box)
            row = box.row()
            column = row.column(align=True)

            menus.GeometriesMenu.putMenu(column, context)
            #create_geometry_selection(column, context)
            column = row.column(align=True)
            collision.GenerateAllCollisionMeshes.place_button(column, infoBox=infoBox)
            collision.GenerateCollisionMesh.place_button(column, infoBox=infoBox)

            box.row()
            infoBox.draw_info()
            # lowerRow = layout.row(align=False)
            # layout.label("Select Physics Frame:")
            # frameMenuText = ""
            # if context.active_bone and not context.scene.RobotEditor.physicsFrameName == "":
            #     frame = bpy.data.objects[context.scene.RobotEditor.physicsFrameName]
            #
            #     if frame.parent_bone:
            #         frameMenuText = context.scene.RobotEditor.physicsFrameName + " --> " + frame.parent_bone
            #     else:
            #         frameMenuText = context.scene.RobotEditor.physicsFrameName
            #
            # lowerRow.menu("roboteditor.physicsframemenu", text=frameMenuText)
            # lowerRow.operator("roboteditor.assigncollisionmodel")

    box = MeshGenerationBox.get(layout, context, "Generate geometry", icon="MOD_TRIANGULATE")
    if box:
        infoBox = InfoBox(box)
        row = box.row()
        column = row.column(align=True)
        create_segment_selector(column, context)
        column = row.column(align=True)
        mesh_generation.GenerateMeshFromSegment.place_button(column, infoBox=infoBox)
        mesh_generation.GenerateMeshFromAllSegment.place_button(column,infoBox=infoBox)
        box.separator()
        infoBox.draw_info()


    box = DeformableBox.get(layout, context, "Deformable Geometries", icon="STYLUS_PRESSURE")
    if box:
        infoBox = InfoBox(box)
        row = box.row()
        column = row.column(align=True)
        menus.GeometriesMenu.putMenu(column, context)
        column = row.column(align=True)
        soft_bodies.ConvertSoftBodies.place_button(column, infoBox=infoBox)
        box.separator()
        infoBox.draw_info()

    drawInfoBox(layout,context)