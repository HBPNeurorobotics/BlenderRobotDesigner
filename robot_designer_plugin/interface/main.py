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
#  Copyright (c) 2015, Karlsruhe Institute of Technoy (KIT)
#  Copyright (c) 2016, FZI Forschungszentrum Informatik
#  Copyright (c) 2017-2021, TUM Technical University of Munich
#
# ######

# Blender imports
import bpy

# RobotDesigner imports
from ..core import PluginManager
from ..core.gui import InfoBox
from ..properties.globals import global_properties
from .helpers import DebugBox
from ..core.logfile import LogFunction


@PluginManager.register_class
class ROBOTDESIGNER_PT_UserInterface(bpy.types.Panel):
    """
    Main class for the robot designer GUI Panel
    """

    bl_label = "NRP Robot Designer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "HBP"
    bl_options = {"HIDE_HEADER"}

    @LogFunction
    def draw(self, context):
        """
        Draw the various tabs of the Robot Designer Plugin
        @param context: active Blender context
        @return:
        """
        from . import files, model, segments, geometries, sensors, muscles, world

        layout = self.layout

        layout.label(
            text="HBP Neurorobotics RobotDesigner",
            icon_value=PluginManager.get_icon("hbp"),
        )
        layout.separator()

        global_properties.gui_tab.prop(bpy.context.scene, layout, expand=True)
        control = global_properties.gui_tab.get(bpy.context.scene)
        layout.separator()

        if control == "armatures":
            model.draw(layout, context)
        elif control == "bones":
            segments.draw(layout, context)
        elif control == "meshes":
            geometries.draw(layout, context)
        elif control == "sensors":
            sensors.draw(layout, context)
        if control == "muscles":
            if (
                bpy.data.objects[
                    global_properties.model_name.get(bpy.context.scene)
                ].RobotDesigner.physics_engine
                != "OPENSIM"
            ):
                row = layout.row()
                row.label(text="Muscle Support for OpenSim Physics Engine Only")
            else:
                muscles.draw(layout, context)
        # elif control == 'markers':
        #     markers.draw(layout, context)
        elif control == "files":
            files.draw(layout, context)
        elif control == "world":
            world.draw(layout, context)

        layout.separator()
        row = layout.row(align=True)

        if InfoBox.global_messages:
            box = DebugBox.get(row, context, "Debug")
            if box:
                InfoBox.draw_global_info(box)
