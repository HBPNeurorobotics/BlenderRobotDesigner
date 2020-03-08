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

# Blender imports
import bpy

# RobotDesigner imports
from .model import check_armature

import math

from . import menus
from ..operators import sensors
from .helpers import EditMusclesBox, WrappingBox, getSingleSegment, AttachWrapBox, WrapPropertiesBox, MusclePropertiesBox
from ..core.gui import InfoBox
from ..properties.globals import global_properties
from ..properties.objects import RDScaler
from ..operators import model, muscles, segments, mesh_generation

from .helpers import create_segment_selector


def draw(layout, context):
    """
    Draws the user interface for geometric modelling.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    if not check_armature(layout, context):
        return

    box = layout.box()
    row = box.row()
    # selective display muscle type
    row.label("Show Muscle Type:")
    col = row.column()
    global_properties.display_muscle_selection.prop(context.scene, col, expand=True)
    row = box.row()
    row.label("Show Wrapping Objects: ")
    col = row.column()
    global_properties.display_wrapping_selection.prop(context.scene, col, expand=True)

    box = EditMusclesBox.get(layout, context, "Edit Muscles", icon="LINKED")
    if box:
        infoBox = InfoBox(box)

        active_model = global_properties.model_name.get(context.scene)
        active_muscle = global_properties.active_muscle.get(bpy.context.scene)

        row1 = box.row()

        # Muscle instances
        column = row1.column(align=True)
        column.menu(menus.MuscleMenu.bl_idname,
                    text=active_muscle if not active_muscle == '' else "Select Muscle")

        column = row1.column(align=True)
        muscles.CreateNewMuscle.place_button(column, text="Create new muscle", infoBox=infoBox)
        muscles.RenameMuscle.place_button(column, text="Rename active muscle", infoBox=infoBox)
        muscles.DeleteMuscle.place_button(column, text="Delete active muscle", infoBox=infoBox)

        row2 = box.row()

        # Muscle Pathpoints
        if active_muscle != '':
            pointbox = box.box()
            row3 = pointbox.row()
            row3.label(text="Muscle attachment points")

            row4 = pointbox.row()
            column = row4.column(align=True)
            muscles.CreateNewPathpoint.place_button(column, text="Add new pathpoint", infoBox=infoBox)

            i = 0
            # pathpoint characteristics
            try:
                for obj in context.scene.objects[active_muscle].data.splines[0].points:

                    row5 = pointbox.row(align=True)
                    i = i + 1

                    # pathpoint coordinates
                    row5.prop(obj, 'co', text=str(i))

                    # assigned segment
                    if bpy.data.objects[active_muscle].RobotDesigner.muscles.pathPoints[i - 1].coordFrame not in \
                            [bone.name for bone in bpy.data.objects[active_model].data.bones]: row5.alert = True
                    row5.prop(bpy.data.objects[active_muscle].RobotDesigner.muscles.pathPoints[i - 1], 'coordFrame',
                              text='')
                    row5.alert = False

                    # swap pathpoints
                    muscles.MovePathpointUp.place_button(row5, text='', icon='TRIA_UP', infoBox=infoBox).nr = i
                    muscles.MovePathpointDown.place_button(row5, text='', icon='TRIA_DOWN', infoBox=infoBox).nr = i

                    # delete pathpoint
                    muscles.DeletePathpoint.place_button(row5, text='', infoBox=infoBox, icon="CANCEL").pathpoint = i

                row7 = pointbox.row()

                # assign segments to pathpoints
                row7.label(text="Attach pathpoints to segments:")
                row7.menu(menus.SegmentsMusclesMenu.bl_idname, text="Select Segment")

                musclepropertiesbox = MusclePropertiesBox.get(box, context, "Muscle Properties", icon="SCRIPTWIN")
                if musclepropertiesbox:

                    musclebox = musclepropertiesbox.box()
                    musclebox.label("Muscle Characteristics")
                    # show length of muscle
                    row = musclebox.row()
                    row.prop(bpy.data.objects[active_muscle].RobotDesigner.muscles, 'length', text="Muscle length")
                    muscles.CalculateMuscleLength.place_button(row, infoBox=infoBox,
                                                               text="Calculate").muscle = active_muscle

                    # Muscle Characteristics
                    # max force
                    row = musclebox.row()
                    row.prop(bpy.data.objects[active_muscle].RobotDesigner.muscles, 'max_isometric_force',
                             text="Max isometric Force")

                    # muscle type
                    row = musclebox.row()
                    if active_muscle != '':
                       row.prop(bpy.data.objects[active_muscle].RobotDesigner.muscles, 'muscleType', text='Muscle Type')
                    box.row()

                    settingsbox = musclepropertiesbox.box()
                    row1 = settingsbox.row()
                    row1.label("Settings: ")
                    row2 = settingsbox.row()
                    global_properties.muscle_dim.prop(context.scene, row2, expand=True)

                wrapbox = box.box()
                row0 = wrapbox.row()
                row0.label(text="Muscle wrapping objects")
                row1 = wrapbox.row()
                column = row1.column(align=True)

                j=0
                try:
                    for connected_wraps in bpy.data.objects[active_muscle].RobotDesigner.muscles.connectedWraps:
                        for wrapping_objects in context.scene.objects:
                            if wrapping_objects.name == connected_wraps.wrappingName:
                                j = j+1
                                row2 = wrapbox.row(align=True)
                                row2.prop(wrapping_objects, 'name', text=str(j))
                                mesh_generation.DisconnectWrappingObject.place_button\
                                    (row2, text='Disconnect from Muscle', infoBox=infoBox).wrappingOrder = j

                    row3 = wrapbox.row()
                    row3.label(text='Add existing wrapping object to muscle: ')
                    row3.menu(menus.ConnectWrapMenu.bl_idname, text='Select Wrapping Object')



                except:
                    musclepropertiesbox.row()
                    box.row()
                    pass


            except:
                pointbox.row()
                box.row()
                pass

    box = WrappingBox.get(layout, context, "Wrapping Objects", icon="LINKED")
    if box:
        infoBox = InfoBox(box)

        row0 = box.row()
        column = row0.column(align=True)
        mesh_generation.CreateWrappingSphere.place_button(column, text="Add Wrapping Sphere", infoBox=infoBox)
        mesh_generation.CreateWrappingCylinder.place_button(column, text="Add Wrapping Cylinder", infoBox=infoBox)

        row1 = box.row()
        row1.label("Select: ")
        row2 = box.row()
        column = row2.column(align=True)
        menus.WrappingObjectsMenu.putMenu(column, context)
        column = row2.column(align=True)
        mesh_generation.RenameWrappingObject.place_button(column, text="Rename Wrapping Object", infoBox=infoBox)
        mesh_generation.DeleteWrappingObject.place_button(column, text="Delete Wrapping Object", infoBox=infoBox)

        boxy = WrapPropertiesBox.get(box, context, "Wrapping Object Properties", icon="SCRIPTWIN")
        if boxy:
            infoBox = InfoBox(boxy)
            row4 = boxy.row()
            selected_objects = [i for i in context.selected_objects if i.name != context.active_object.name]
            if len(selected_objects):
                meshes = global_properties.mesh_name.get(context.scene)
                # obj = bpy.data.objects[meshes].RobotDesigner.wrap.scaling
                obj = bpy.data.objects[meshes].RobotDesigner.scaling
            if bpy.data.objects[meshes].RobotDesigner.wrap.WrappingType == "WRAPPING_SPHERE":
                boxy.prop(obj, "scale_all", slider=False, text="Scale Sphere: ")
            elif bpy.data.objects[meshes].RobotDesigner.wrap.WrappingType == "WRAPPING_CYLINDER":
                column = row4.column()
                column.prop(obj, "scale_radius", slider=False, text="Scale Radius")
                column.prop(obj, "scale_depth", slider=False, text="Scale Depth")
                row5 = boxy.row()
                row5.prop(bpy.data.objects[meshes], "rotation_euler", slider=False, text="Rotate: ")

            row6 = boxy.row()
            row6.prop(bpy.data.objects[global_properties.mesh_name.get(context.scene)], "location", slider=False,
                      text="Location")

        box = AttachWrapBox.get(box, context, "Wrapping Object Attach/Detach", icon="LINKED")
        if box:
            infoBox = InfoBox(box)

            row3 = box.row()
            column = row3.column(align=True)

            single_segment = getSingleSegment(context)

            column.menu(menus.SegmentsGeometriesMenu.bl_idname,
                        text=single_segment.name if single_segment else "Select Segment")
            row_bone = column.row(align=True)

            global_properties.list_segments.prop(context.scene, row_bone, expand=True, icon_only=True)
            row_bone.separator()

            global_properties.segment_name.prop_search(context.scene, row_bone, context.active_object.data, 'bones',
                                                    icon='VIEWZOOM',
                                                    text='')
            column = row3.column(align=True)
            mesh_generation.AttachWrappingObject.place_button(column, text="Attach Wrapping Object", infoBox=infoBox)
            mesh_generation.DetachWrappingObject.place_button(column, text="Detach Wrapping Object", infoBox=infoBox)
            mesh_generation.DetachAllWrappingObjects.place_button(column, text="Detach all Wrapping Objects",
                                                                infoBox=infoBox)



    # infoBox.draw_info()
