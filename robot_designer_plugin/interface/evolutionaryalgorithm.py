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

from .helpers import SCMparametersOpBox, GeneralparametersOpBox
from ..core.gui import InfoBox
from ..core import PluginManager
from ..core.logfile import LogFunction
from ..properties.globals import global_properties
from ..operators import model, evolutionaryalgorithm, segments

def draw(layout, context):
    if not check_armature(layout, context):
        return

    box = layout.box()
    row = box.row(align=True)
    row.label("Optimization type:")
    global_properties.typeoptimization.prop(context.scene, row, expand=True)

    # box: select the robot population
    box = layout.box()
    infoBox = InfoBox(box)
    row = box.row()
    row.label("Select model to evolve:")
    row = box.row()
    active_model = global_properties.model_name.get(context.scene)
    column = row.column(align=True)
    column.menu(menus.SelectionRobotsMenu.bl_idname,
                text=active_model if not active_model == " " else "Select Model")

    column = row.column(align=True)
    evolutionaryalgorithm.AddRobot.place_button(column, text="Select robot model", infoBox=infoBox)
    row = box.row()

    # box: select result plot type
    box = layout.box()
    row = box.row(align=True)
    row.label("Generate instances:")
    global_properties.visualresult.prop(context.scene, row, expand=True)
    row = box.row(align=True)

    if global_properties.typeoptimization.get(context.scene)=='joints':

        row.label("Generate simulation plots:")
        global_properties.toolbox.prop(context.scene, row, expand=True)
        row = box.row(align=True)
        row.label("Ev. Algorithm:")
        global_properties.encoding.prop(context.scene, row, expand=True)

    # box: selection of general GA parameters
    """GA Parameters
    Define the operator parameters"""
    box = GeneralparametersOpBox.get(layout, context, "General Parameters", icon="MOD_ARMATURE")  # here parameters
    if box:
        infoBox = InfoBox(box)
        row = box.row()
        global_properties.max_generation.prop(context.scene, row)
        row = box.row()
        if global_properties.typeoptimization.get(context.scene) == 'meshes':
            global_properties.num_adaptions.prop(context.scene, row)
            row = box.row()
            if global_properties.num_adaptions.get(context.scene) is not 0:
                global_properties.adaption_rate.prop(context.scene, row)
                row = box.row()

        if global_properties.visualresult.get(context.scene)=='all':
            global_properties.offsetlateral.prop(context.scene, row)
            row = box.row()
            global_properties.offsetfront.prop(context.scene, row)

    #box: selection of operator GA parameters
    """Selection, crossover and mutation Parameters
    Define the operator parameters"""
    box = SCMparametersOpBox.get(layout, context, "Operator Parameters", icon="RNA") #  here parameters
    if box and global_properties.encoding.get(context.scene)=='binary':
        infoBox = InfoBox(box)
        row = box.row()
        row.label ("Selection parameters:")
        row = box.row()
        global_properties.selection_rate.prop(context.scene, row)
        row = box.row()
        row.label ("Crossover parameters:")
        row = box.row()
        global_properties.offspring_size.prop(context.scene, row)
        row = box.row()
        row.label ("Mutation parameters:")
        row = box.row()
        global_properties.mutation_rate_bin.prop(context.scene, row)

    if box and global_properties.encoding.get(context.scene) == 'real':
        infoBox = InfoBox(box)
        row = box.row()
        row.label("Selection parameters:")
        row = box.row()
        global_properties.selection_rate.prop(context.scene, row)
        row = box.row()
        row.label("Crossover parameters:")
        row = box.row()
        global_properties.offspring_size.prop(context.scene, row)
        row = box.row()
        row.label("Mutation parameters:")
        row = box.row()
        global_properties.mutation_rate_real.prop(context.scene, row)
        row = box.row()
        global_properties.mutation_deviation.prop(context.scene, row)

    # box: Run Genetic Algorithm
    box = layout.box()
    infoBox = InfoBox(box)
    row = box.row()
    row = box.row()
    if global_properties.typeoptimization.get(context.scene) == 'joints':
        evolutionaryalgorithm.StartSimulationJoints.place_button(row, text="Start Simulation", infoBox=infoBox)
    if global_properties.typeoptimization.get(context.scene) == 'meshes':
        evolutionaryalgorithm.StartSimulationMeshes.place_button(row, text="Start Simulation", infoBox=infoBox)

    row = box.row()


