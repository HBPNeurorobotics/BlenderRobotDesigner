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
import math
import random
import numpy as np
import time
import csv


# ######
# Blender imports
import bpy
import bmesh

# ######
# RobotDesigner imports
from ..core import config, PluginManager, RDOperator
from .helpers import ModelSelected
from ..properties.globals import global_properties


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class AddRobot(RDOperator):
    """
    :ref:`operator` for selecting robots to simulate.
    """

    bl_idname = config.OPERATOR_PREFIX + "add_robot"
    bl_label = "Add Robot"

    @classmethod
    def run(cls):
        """
        Run this operator
        """
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

        active_model = global_properties.model_name.get(context.scene)
        bpy.context.scene.RobotDesigner.model_to_simulate.clear()
        list_robots = bpy.context.scene.RobotDesigner.model_to_simulate.add()
        list_robots.name = active_model

        return {'FINISHED'}



@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class StartSimulationJoints(RDOperator):
    """
    :ref:`operator` for starting simulation EA applied to Segments position.
    """

    bl_idname = config.OPERATOR_PREFIX + "start_sim"
    bl_label = "Start Simulation"

    @classmethod
    def run(cls):
        """
        Run this operator
        """
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

<<<<<<< HEAD
        def selectrobot(blenderrobots):
            """
            select robot to simulate
            """
=======
        def selectrobot(blenderrobots):  #select robot to simulate
>>>>>>> c729e77
            robot_tosimulate = blenderrobots[0].name

            return robot_tosimulate

<<<<<<< HEAD
        def listbones(numberindividuals, robot_tosimulate):
            """
            get bones of the armature robot_tosimulate
            """
=======
        def listbones(numberindividuals, robot_tosimulate):  #get bones of the armature robot_tosimulate
>>>>>>> c729e77
            for r in range(numberindividuals):
                M_bones_list = [obj.name for obj in bpy.data.armatures[robot_tosimulate].bones]

            return M_bones_list

<<<<<<< HEAD
        def numbits (upper_limit, lower_limit, decimal_precision):
            """
            number of bits needed to represent the variable value in a binary string.
            normaliz is for normalizing values when converting from real to bin, and viceversa
            """
=======
        def numbits (upper_limit, lower_limit, decimal_precision):  #number of bits needed to represent the variable value in a binary string. normaliz is for normalizing values when converting from real to bin, and viceversa
>>>>>>> c729e77
            bits_string = int(np.ceil(math.log10((upper_limit - lower_limit) * (10 ** decimal_precision)) / math.log10(2)))
            max_bin = bin(2**bits_string-1)[2:]
            normaliz = (int(str(max_bin),2)/2)/(10 ** decimal_precision)

            return bits_string, normaliz

<<<<<<< HEAD
        def getparameters (M_bones_list, robot_tosimulate):
            """
            get the x, y, z position of the bones in M_bones_list
            """
=======
        def getparameters (M_bones_list, robot_tosimulate):  #get the x, y, z position of the bones in M_bones_list
>>>>>>> c729e77
            M_ch_real = [[0 for i in range(3)] for j in range(len(M_bones_list))]

            bpy.context.scene.objects.active = bpy.data.objects[robot_tosimulate]

            for b in range(len(M_bones_list)):
                    bpy.context.active_object.data.bones.active.select = False
                    bone = bpy.context.active_object.data.bones[M_bones_list[b]]
                    bone.select = True
<<<<<<< HEAD
                    x_pos_real, y_pos_real, z_pos_real = bone.RobotDesigner.Euler.x.value, bone.RobotDesigner.Euler.y.value, bone.RobotDesigner.Euler.z.value
=======
                    x_pos_real, y_pos_real, z_pos_real = bone.RobotEditor.Euler.x.value, bone.RobotEditor.Euler.y.value, bone.RobotEditor.Euler.z.value
>>>>>>> c729e77

                    M_ch_real[b] = [x_pos_real, y_pos_real, z_pos_real]

            return M_ch_real

<<<<<<< HEAD
        def individualsgen (gen, M_M_M_historial, M_bones_list, M_ch_real):
            """
            get segments' position from individuals of previous generation
            """
=======
        def individualsgen (gen, M_M_M_historial, M_bones_list, M_ch_real):  #get segments' position from individuals of previous generation
>>>>>>> c729e77
            if gen == 0:
                M_ch_realextra = [[(random.randint(-int(max(max(M_ch_real))), int(max(max(M_ch_real))))) for i in range(3)] for j in range(len(M_bones_list))]
                M_M_ch_real = [M_ch_real, M_ch_realextra]  #M_ch_realextra is an individual with random segments' position values to pair with the initial robot

            else:
                M_M_ch_real = M_M_M_historial[gen-1]

            return M_M_ch_real

<<<<<<< HEAD
        def code (M_M_ch_real, M_bones_list, normaliz, decimal_precision, bits_string):
            """
            code from real system number to binary system
            """
=======
        def code (M_M_ch_real, M_bones_list, normaliz, decimal_precision, bits_string):  #code from real system number to binary system
>>>>>>> c729e77
            M_M_ch_bin = []
            for m in range(len(M_M_ch_real)):
                M_ch_bin = [[bin(0)[2:].zfill(bits_string) for i in range(3)] for j in range(len(M_bones_list))]
                for r in range(len(M_M_ch_real[m])):
                    for c in range(len(M_M_ch_real[m][0])):
                        norm = int(round((M_M_ch_real[m][r][c] + normaliz),decimal_precision)*(10**decimal_precision))
                        M_ch_bin[r][c] = bin(norm)[2:].zfill(bits_string)

                M_M_ch_bin.append(M_ch_bin)
            return M_M_ch_bin

<<<<<<< HEAD
        def robotstructure(M_bones_list, robot_tosimulate):
            """
            get the tree structure of the robot
            """
=======
        def robotstructure(M_bones_list, robot_tosimulate):  #get the tree structure of the robot
>>>>>>> c729e77
            tree_structure=[]

            for b in range(len(M_bones_list)):
                if bpy.data.armatures[robot_tosimulate].bones[M_bones_list[b]].parent==None:
                    parent=None
                else:
                    parent = bpy.data.armatures[robot_tosimulate].bones[M_bones_list[b]].parent.name
                if bpy.data.armatures[robot_tosimulate].bones[M_bones_list[b]].children.keys()==[]:
                    children=None
                else:
                    children = bpy.data.armatures[robot_tosimulate].bones[M_bones_list[b]].children.keys()

                tree_structure.append([M_bones_list[b], parent, children])

            return tree_structure

<<<<<<< HEAD
        def iniboneposition(M_bones_list, robot_tosimulate):
            """
            get initial position of the armature's segments
            """
=======
        def iniboneposition(M_bones_list, robot_tosimulate):  #get initial position of the armature's segments
>>>>>>> c729e77
            bone_position=[]

            for b in range(len(M_bones_list)):
                pos_bone = np.asarray(bpy.data.armatures[robot_tosimulate].bones[M_bones_list[b]].head_local)
                bone_position.append((M_bones_list[b], pos_bone))

            return bone_position

<<<<<<< HEAD
        def inimeshposition():
            """
            get initial position of armature's meshes
            """
            mesh_position = []

            meshes = [obj.name for obj in bpy.data.objects \
                if obj.type == 'MESH' if obj.RobotDesigner.tag == "DEFAULT"]
=======
        def inimeshposition():  #get initial position of armature's meshes
            mesh_position = []

            meshes = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']
>>>>>>> c729e77

            for m in range(len(meshes)):
                pos_glob_mesh = bpy.data.objects[meshes[m]].matrix_world.to_translation()
                mesh_position.append((meshes[m], pos_glob_mesh))

            return mesh_position

<<<<<<< HEAD
        def fitnessf (gen, M_bones_list, M_M_ch_real, tree_structure, M_ev_direction, M_fitness):
            """
            fitness function
            """

            def growthmatrix(children,matrix_children_pos):
                """
                generate general knowledge to evaluate the segments' movement direction in the fitness function
                """
=======
        def fitnessf (gen, M_bones_list, M_M_ch_real, tree_structure, M_ev_direction, M_fitness):  #fitness function

            def growthmatrix(children,matrix_children_pos):  # generate general knowledge to evaluate the segments' movement direction in the fitness function
>>>>>>> c729e77
                direction = [['' for i in range(3)] for j in range(len(children))]

                for c in range(len(children)):
                    for euler in range(3):
                        if round(matrix_children_pos[c][euler], 1) > 0:
                            direction[c][euler] = '+'
                        if round(matrix_children_pos[c][euler], 1) < 0:
                            direction[c][euler] = '-'
                        if round(matrix_children_pos[c][euler], 1) == 0:
                            direction[c][euler] = 'N'

                return direction

            V_fitness = [0 for i in range((len(M_M_ch_real)))]

            for m in range(len(M_M_ch_real)):

                if gen==0: # in generation 0, only the original robot is evaluated
                    m=0
                meta_parent = [tree_structure[b][0] for b in range(len(M_bones_list)) if tree_structure[b][1] == None][0] # get the first parent of the armature
                meta_parent_pos = M_M_ch_real[m][M_bones_list.index(meta_parent)]
                fitness = - sum([abs(col) for col in meta_parent_pos]) * 2  # if this meta parent has moved its bone, it will be penalized

                parents_armature_all = [tree_structure[b][1] for b in range(len(M_bones_list)) if tree_structure[b][1] is not None]  #get all the bones that are parents
                parents_armature = list(set(parents_armature_all)) #deleted repeated names

                for p in range(len(parents_armature)): #evaluate fitness of each bone's children
                    f=0
                    parent_p = parents_armature[p]
                    children = [tree_structure[b][2] for b in range(len(M_bones_list)) if tree_structure[b][0] == parent_p] #get children of the bone parent_p
                    children=children[0]

                    if children != None:
                        matrix_children_pos = [M_M_ch_real[m][M_bones_list.index(c)] for c in children]

                        if gen == 0:
                            M_ev_direction.append(growthmatrix(children, matrix_children_pos))

                        for row in range(len(matrix_children_pos)):  # calculate of the bone's fitness.
                            for euler in range(3):
                                if M_ev_direction[p][row][euler] == '+':
                                    f = f + matrix_children_pos[row][euler]*10 #10, 10, and 30 are the weights of the fitness function
                                if M_ev_direction[p][row][euler] == '-':
                                    f = f - matrix_children_pos[row][euler]*10
                                if M_ev_direction[p][row][euler] == 'N':
                                    f = f - abs(matrix_children_pos[row][euler])*30

                    fitness=fitness+f

                if gen != 0:
                    V_fitness[m] = int(fitness)
                    fitness = V_fitness
            M_fitness.append (fitness)

            return fitness, meta_parent, M_ev_direction, M_fitness

<<<<<<< HEAD
        def selectionbin (gen, M_M_ch_bin, num_offspring, s_rate, fitness):
            """
            selection for GA: mate 2 x num_offspring times the individuals for kepping offspring population size after crossover
            """
=======
        def selectionbin (gen, M_M_ch_bin, num_offspring, s_rate, fitness):  #selection for GA: mate 2 x num_offspring times the individuals for kepping offspring population size after crossover
>>>>>>> c729e77
            selected_matrices = []

            if gen==0: #in generation 0 there is no selection
                for o in range(num_offspring):
                    selected_matrices.append(M_M_ch_bin)

            else:  #rank selection
                V_fitness_gen_sorted = sorted(fitness,reverse=True) #sort fitness oof the individuals
                best_fitnesses = V_fitness_gen_sorted[0:int(s_rate*len(fitness))+1]
                indexes_best = [fitness.index(ind) for ind in best_fitnesses]

                b=0 #counter
                for i in range(num_offspring):
                    pair = [M_M_ch_bin[indexes_best[b]], M_M_ch_bin[indexes_best[b+1]]]
                    selected_matrices.append((pair))
                    b+=2
                    if len(indexes_best) % 2 == 0:
                        if b>=int(s_rate*len(fitness)):
                            b=0
                    else:
                        if b>=(int(s_rate*len(fitness))-1):
                            b=0

            return selected_matrices

<<<<<<< HEAD
        def crossoverbin (bits_string, selected_matrices, M_M_ch_bin):
            """
            crossover for GA
            """
=======
        def crossoverbin (bits_string, selected_matrices, M_M_ch_bin): #crossover for GA
>>>>>>> c729e77
            M_M_cross = []

            for m in range(len(selected_matrices)):
                M_cross = [[bin(0)[2:].zfill(bits_string) for i in range(len(M_M_ch_bin[0][0]))] for j in range(len(M_M_ch_bin[0]))]
                for row in range (len(selected_matrices[m][0])):
                    for column in range (len(selected_matrices[m][0][0])):
                        s = random.randint(0, bits_string)
                        M_cross[row][column] = selected_matrices[m][0][row][column][:s] + selected_matrices[m][1][row][column][s:]
                M_M_cross.append(M_cross)

            return M_M_cross

<<<<<<< HEAD
        def mutationbin (gen,M_M_cross, M_M_ch_bin, bits_string, mutation_rate):
            """
            mutation for GA
            """
=======
        def mutationbin (gen,M_M_cross, M_M_ch_bin, bits_string, mutation_rate):  #mutation for GA
>>>>>>> c729e77
            M_M_mut = [0 for i in range(len(M_M_cross))]

            for o in range(len(M_M_cross)):
                M_mut = [['' for i in range(len(M_M_ch_bin[0][0]))] for j in range(len(M_M_ch_bin[0]))]
                for row in range(len(M_M_cross[o])):
                    for column in range(len(M_M_cross[o][0])):
                        for b in range(bits_string):

                            if random.random() < mutation_rate:
                                if M_M_cross[o][row][column][b]==1:
                                    M_mut[row][column] = M_mut[row][column]+'0'
                                else:
                                    M_mut[row][column] = M_mut[row][column]+'1'
                            else:
                                M_mut[row][column] = M_mut[row][column]+str(M_M_cross[o][row][column][b])

                M_M_mut[o] = M_mut

            return M_M_mut

<<<<<<< HEAD
        def selectionreal (gen, M_M_ch_real, num_offspring, s_rate, fitness):
            """
            selection for ES: mate 2 x num_offspring times the individuals for kepping offspring population size after crossover
            """
=======
        def selectionreal (gen, M_M_ch_real, num_offspring, s_rate, fitness):  #selection for ES: mate 2 x num_offspring times the individuals for kepping offspring population size after crossover
>>>>>>> c729e77
            selected_matrices = []

            if gen==0: #only two parent reproduce all offspring
                for o in range(num_offspring):
                    selected_matrices.append(M_M_ch_real)

            else:  #rank selection
                V_fitness_gen_sorted = sorted(fitness,reverse=True) #sort individual fitness
                best_fitnesses = V_fitness_gen_sorted[0:int(s_rate*len(fitness))+1]
                indexes_best = [fitness.index(ind) for ind in best_fitnesses]

                b=0 #counter
                for i in range(num_offspring):
                    pair = [M_M_ch_real[indexes_best[b]], M_M_ch_real[indexes_best[b+1]]]
                    selected_matrices.append((pair))
                    b+=2
                    if len(indexes_best) % 2 == 0:
                        if b>=int(s_rate*len(fitness)):
                            b=0
                    else:
                        if b>=(int(s_rate*len(fitness))-1):
                            b=0

            return selected_matrices

<<<<<<< HEAD
        def crossoverreal (selected_matrices, M_M_ch_real):
            """
            crossover for ES
            """
=======
        def crossoverreal (selected_matrices, M_M_ch_real): #crossover for ES
>>>>>>> c729e77
            M_M_cross = []

            for m in range(len(selected_matrices)):
                M_cross = [[0 for i in range(len(M_M_ch_real[0][0]))] for j in range(len(M_M_ch_real[0]))]
                for row in range (len(selected_matrices[m][0])):
                    for column in range (len(selected_matrices[m][0][0])):
                        if random.random() < 0.5: #offspring gets the parameter's value of one parent, or the another, with 50% probability
                            M_cross[row][column] = selected_matrices[m][0][row][column]
                        else:
                            M_cross[row][column] = selected_matrices[m][1][row][column]
                M_M_cross.append(M_cross)

            return M_M_cross

<<<<<<< HEAD
        def mutationreal (M_M_cross, M_M_ch_real, mutation_rate, mutation_deviation):
            """
            mutation for ES
            """
=======
        def mutationreal (M_M_cross, M_M_ch_real, mutation_rate, mutation_deviation): #mutation for ES
>>>>>>> c729e77
            M_M_mut = [0 for i in range(len(M_M_cross))]

            for o in range(len(M_M_cross)):
                M_mut = [[0 for i in range(len(M_M_ch_real[0][0]))] for j in range(len(M_M_ch_real[0]))]
                for row in range(len(M_M_cross[o])):
                    for column in range(len(M_M_cross[o][0])):

                            if random.random() < mutation_rate:
                                M_mut[row][column] = M_M_cross[o][row][column] + np.random.normal(0,mutation_deviation)
                            else:
                                M_mut[row][column] = M_M_cross[o][row][column]

                M_M_mut[o] = M_mut

            return M_M_mut

<<<<<<< HEAD
        def decode(M_M_mut, M_bones_list, normaliz, decimal_precision):
            """
            decode bones' positions from binary to real
            """
=======
        def decode(M_M_mut, M_bones_list, normaliz, decimal_precision): #decode bones' positions from binary to real
>>>>>>> c729e77
            M_M_newch_real = []

            for o in range(len(M_M_mut)):
                M_newch_real = np.zeros((len(M_bones_list), 3))
                for row in range(len(M_M_mut[o])):
                    for column in range(len(M_M_mut[o][0])):
                        M_newch_real[row][column] = int(M_M_mut[o][row][column],2)/(10**decimal_precision) - normaliz

                M_M_newch_real.append(M_newch_real)

            return M_M_newch_real

<<<<<<< HEAD
        def historialgen (M_M_newch_real, M_M_M_historial):
            """
            record individuals bone's position for all generations
            """
=======
        def historialgen (M_M_newch_real, M_M_M_historial):  #record individuals bone's position for all generations
>>>>>>> c729e77
            M_M_M_historial.append(M_M_newch_real)

            return M_M_M_historial

<<<<<<< HEAD
        def createrobotinstances(gen, num_offspring, robot_tosimulate, M_bones_list, list_instances, offset_o, offset_g):
            """
            create robot instances to plot all individuals
            """
=======
        def createrobotinstances(gen, num_offspring, robot_tosimulate, M_bones_list, list_instances, offset_o, offset_g): #create robot instances to plot all individuals
>>>>>>> c729e77

            for i in range(num_offspring):

                context.scene.objects.active = bpy.data.objects[robot_tosimulate]
                context.active_object.select = True
<<<<<<< HEAD
                meshes = [obj.name for obj in bpy.data.objects \
                            if not obj.parent_bone is None \
                            and obj.type == 'MESH' and obj.RobotDesigner.tag == 'DEFAULT'
                            and obj.parent == bpy.data.objects[robot_tosimulate]]
=======
                meshes = [obj.name for obj in bpy.data.objects if not obj.parent_bone is None and obj.type == 'MESH' and obj.parent == bpy.data.objects[robot_tosimulate]]
>>>>>>> c729e77

                for m in range(len(meshes)):
                    bpy.data.objects[meshes[m]].select = True
                for b in range(len(M_bones_list)):
                    bone = bpy.context.active_object.data.bones[M_bones_list[b]]
                    bone.select = True
                bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value": ((i * offset_o + offset_o / 2 - num_offspring * offset_o / 2), -offset_g * (gen), 0)})  #for Monkeyrobot robot and visuals and bones
                bpy.data.scenes[0].update()
                list_instances[gen-1][i]=bpy.context.scene.objects.active.name
                bpy.ops.object.select_all(action='DESELECT')

                bpy.context.active_object.data.name = bpy.context.active_object.name  # rename armature as the object name

            return list_instances #names of the armatures of all generations

        def visualprop (gen, robot_tosimulate, M_bones_list, M_M_newch_real, M_ch_real, list_instances, indiv, tree_structure, initial_bone_position, initial_mesh_position): #COMPLEX FUNCTION! change visual properties of the meshes

<<<<<<< HEAD
            def bonematrixrotation_L_G(robot_tosimulate, bone_to_rot, dx, dy, dz):
                """
                matrix rotation of the bones to achieve correct bone position when translating them in local coordinates
                """
=======
            def bonematrixrotation_L_G(robot_tosimulate, bone_to_rot, dx, dy, dz):  #matrix rotation of the bones to achieve correct bone position when translating them in local coordinates
>>>>>>> c729e77

                bone = bpy.data.armatures[robot_tosimulate].bones[bone_to_rot].parent
                gAl = np.identity(3)

                while bone != None:
                    A = bone.matrix
                    gAl = np.dot(A, gAl)
                    bone = bone.parent

                d_g = np.dot(gAl, [dx, dy, dz])

                return d_g

<<<<<<< HEAD
            def editmode_mesh(mesh_to_edit):
                """
                from object to edit mode of a mesh
                """
=======
            def editmode_mesh(mesh_to_edit):  #from object to edit mode of a mesh
>>>>>>> c729e77
                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                bpy.ops.object.select_all(action='DESELECT')
                mesh = bpy.data.objects[mesh_to_edit]
                mesh.select = True
                bpy.context.scene.objects.active = mesh
                bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                obj = bpy.context.object.data
                bm = bmesh.from_edit_mesh(obj)
                return bm, obj, mesh

            parent_armature_all = [tree_structure[b][1] for b in range(len(M_bones_list)) if tree_structure[b][1] is not None] #get all the bones that are parents
            parents_armature = list(set(parent_armature_all)) #deleted repeated names
            result = global_properties.visualresult.get(context.scene)
            current_scene = bpy.context.scene
            current_scene.RobotDesigner.display_mesh_selection = 'all'

            for par in range(len(parents_armature)): #change visual properties of bone that are parents
                parent_p = parents_armature[par]
                chi_indexes = [b for b in range(len(M_bones_list)) if tree_structure[b][1] == parent_p] #indexes in M_bones_list of the children

                ##################################################################check if the bone has a mesh attached. if not, got to its children
                meshes = []
                for c in range(len(chi_indexes)):
<<<<<<< HEAD
                    mesh = [obj.name for obj in bpy.data.objects \
                            if not obj.parent_bone is None \
                            and obj.type == 'MESH' and obj.RobotDesigner.tag == 'DEFAULT'\
                            and bpy.data.armatures[robot_tosimulate].bones[obj.parent_bone].name == M_bones_list[chi_indexes[c]]]
=======
                    mesh = [obj.name for obj in bpy.data.objects if
                            not obj.parent_bone is None and obj.type == 'MESH' and
                            bpy.data.armatures[robot_tosimulate].bones[obj.parent_bone].name == M_bones_list[chi_indexes[c]]]
>>>>>>> c729e77
                    meshes.append(mesh)

                for m in range(len(meshes)):
                    if not meshes[m]:
                        pre_chi_index_m = chi_indexes[m]
                        chi_ind = [b for b in range(len(M_bones_list)) if tree_structure[b][0] == tree_structure[pre_chi_index_m][2][0]][0]
                        chi_indexes[m] = chi_ind
                ###########################################################################################
                meshbone_index = [b for b in range(len(M_bones_list)) if tree_structure[b][0] == parent_p][0] #index of the mesh attached to the bone

                if result == 'all': #meshes when all individuals are plotted
                    meshes = [obj.name for obj in bpy.data.objects if
<<<<<<< HEAD
                              not obj.parent_bone is None and obj.type == 'MESH' \
                              and obj.RobotDesigner.tag == 'DEFAULT' \
                              and obj.parent.name == list_instances[gen - 1][indiv] and
=======
                              not obj.parent_bone is None and obj.type == 'MESH' and obj.parent.name == list_instances[gen - 1][indiv] and
>>>>>>> c729e77
                              bpy.data.armatures[robot_tosimulate].bones[obj.parent_bone].name == parent_p]

                if result == 'best': #meshes when only the best individual is plotted
                    meshes = [obj.name for obj in bpy.data.objects if  # meshes of the parent
<<<<<<< HEAD
                              not obj.parent_bone is None and obj.type == 'MESH' \
                              and obj.RobotDesigner.tag == 'DEFAULT' and \
=======
                              not obj.parent_bone is None and obj.type == 'MESH' and
>>>>>>> c729e77
                              bpy.data.armatures[robot_tosimulate].bones[obj.parent_bone].name == parent_p]

                for m in range(len(meshes)):
                    pos_bone_chi = [initial_bone_position[j][1] for j in chi_indexes] #get position of parent's children bone

                    pos_bone_meshbone=bpy.data.objects[M_bones_list[meshbone_index]].matrix_world.to_translation()

                    pos_glob_mesh=bpy.data.objects[meshes[m]].matrix_world.to_translation()
                    scale_factor = bpy.data.objects[meshes[m]].scale  # factor to correct vert local position

                    bm, obj, mesh = editmode_mesh(meshes[m]) #go to edit mode

                    pos_loc_vertex = [[] for cii in range(len(chi_indexes))]
                    vertexes = [[] for cii in range(len(chi_indexes))]
                    for v in range(len(bm.verts)): #get verts of the mesh that are closer to one particular child when there the parent bone has many children
                        bm.verts.ensure_lookup_table()
                        dist_vertex_children = [math.sqrt((pos_bone_chi[cii][0] - (bm.verts[v].co[0]* scale_factor[0] + pos_glob_mesh[0])) ** 2 +
                                                          (pos_bone_chi[cii][1] - (bm.verts[v].co[1]* scale_factor[1] + pos_glob_mesh[1])) ** 2 +
                                                          (pos_bone_chi[cii][2] - (bm.verts[v].co[2]* scale_factor[2] + pos_glob_mesh[2])) ** 2) for cii
                                                in range(len(chi_indexes))]
                        ichildren_min_dist = np.argmin(dist_vertex_children)
                        ichildren_min_dist = int(ichildren_min_dist)
                        vertexes[int(ichildren_min_dist)].append(v)
                        pos_loc_vertex[ichildren_min_dist].append([bm.verts[v].co.x* scale_factor[0], bm.verts[v].co.y* scale_factor[1], bm.verts[v].co.z* scale_factor[2]])


                    for ci in range(len(chi_indexes)): # give values to vertex's position
                        j = chi_indexes[ci]
                        pos_loc_vertex_chi = np.asarray(pos_loc_vertex[ci])
                        print(meshes[m], pos_loc_vertex_chi)

                        if pos_loc_vertex_chi is not None:
                            max_loc_pos = [np.max(np.amax(pos_loc_vertex_chi, 0)[e]) for e in range(3)]
                            max_glob_pos = max_loc_pos + np.asarray(pos_glob_mesh) #from local to global
                            min_loc_pos = [np.min(np.amin(pos_loc_vertex_chi, 0)[e]) for e in range(3)]
                            min_glob_pos = min_loc_pos + np.asarray(pos_glob_mesh)

                            dx, dy, dz = M_M_newch_real[indiv][j][0] - M_ch_real[j][0], M_M_newch_real[indiv][j][1] - M_ch_real[j][1], \
                                         M_M_newch_real[indiv][j][2] - M_ch_real[j][2] #variation of the segment position

                            d_g = bonematrixrotation_L_G(robot_tosimulate, M_bones_list[j], dx, dy, dz)

                            bm, obj, mesh = editmode_mesh(meshes[m])

                            for v in vertexes[ci]:
                                bm.verts.ensure_lookup_table()
                                bm.verts[v].select = True
                                pos_glob_vertex = np.asarray(bm.verts[v].co) * np.asarray(scale_factor) + np.asarray(pos_glob_mesh)

                                for co in range(3):  # cases to relate vertex-bone. p goes from 0 to 1 and establishes how close the vertex is to the bone being 0 the closest and 1 the furthest  vertex to the bone
                                    if min_glob_pos[co] <= pos_bone_chi[ci][co] <= max_glob_pos[co]:  # case 1- bone inside mesh
                                        if pos_bone_chi[ci][co] < pos_glob_vertex[co] < pos_bone_meshbone[co] or pos_bone_meshbone[co] < \
                                                pos_glob_vertex[co] < pos_bone_chi[ci][co]:
                                            p = (abs(pos_glob_vertex[co] - pos_bone_meshbone[co]) / abs(
                                                pos_bone_chi[ci][co] - pos_bone_meshbone[co]))
                                        elif abs(pos_bone_chi[ci][co] - pos_glob_vertex[co]) <= abs(
                                                pos_bone_meshbone[co] - pos_glob_vertex[co]) and np.sign(bm.verts[v].co[co]) == np.sign(
                                                d_g[co]):
                                            p = 1
                                        else:
                                            p = 0
                                    else:
                                        if max_glob_pos[co] <= pos_bone_chi[ci][co]:  # case 2- bone pos > mesh
                                            if pos_bone_meshbone[co] <= pos_glob_vertex[co] <= max_glob_pos[co]:
                                                p = (abs(pos_glob_vertex[co] - pos_bone_meshbone[co]) / abs(
                                                    max_glob_pos[co] - pos_bone_meshbone[co]))
                                            else:
                                                p = 0
                                        if pos_bone_chi[ci][co] <= min_glob_pos[co]:  # case 3- bone pos < mesh
                                            if min_glob_pos[co] <= pos_glob_vertex[co] <= pos_bone_meshbone[co]:
                                                p = (abs(pos_glob_vertex[co] - pos_bone_meshbone[co]) / abs(
                                                    min_glob_pos[co] - pos_bone_meshbone[co]))
                                            else:
                                                p = 0

                                    bm.verts[v].co[co] = bm.verts[v].co[co] + (d_g[co] * p) / scale_factor[co]
                                    bmesh.update_edit_mesh(obj, True)

                                bm.verts[v].select = False
                                bmesh.update_edit_mesh(obj, True)

                        mesh.select = False
                        bpy.ops.object.mode_set(mode='OBJECT')

            return None

<<<<<<< HEAD
        def sendparametersall(gen, robot_tosimulate, M_M_newch_real, M_bones_list, num_offspring, list_instances, M_ch_real, tree_structure, initial_bone_position, initial_mesh_position):
            """
            send segment's position value to Blender when all individuals are plotted
            """
=======
        def sendparametersall(gen, robot_tosimulate, M_M_newch_real, M_bones_list, num_offspring, list_instances, M_ch_real, tree_structure, initial_bone_position, initial_mesh_position):  #send segment's position value to Blender when all individuals are plotted
>>>>>>> c729e77

            for indiv in range(num_offspring):
                context.scene.objects.active = bpy.data.objects[list_instances[gen-1][indiv]]
                context.active_object.select = True

                for b in range(len(M_bones_list)):

                    bone = bpy.context.active_object.data.bones[M_bones_list[b]]
                    bpy.context.active_object.data.bones.active.select = False
                    bone.select = True
<<<<<<< HEAD
                    bone.RobotDesigner.Euler.x.value = M_M_newch_real[indiv][b][0]  #x position
=======
                    bone.RobotEditor.Euler.x.value = M_M_newch_real[indiv][b][0]  #x position
>>>>>>> c729e77

                    bone = bpy.context.active_object.data.bones[M_bones_list[b]]
                    bpy.context.active_object.data.bones.active.select = False
                    bone.select = True
<<<<<<< HEAD
                    bone.RobotDesigner.Euler.y.value = M_M_newch_real[indiv][b][1]  #y position
=======
                    bone.RobotEditor.Euler.y.value = M_M_newch_real[indiv][b][1]  #y position
>>>>>>> c729e77

                    bone = bpy.context.active_object.data.bones[M_bones_list[b]]
                    bpy.context.active_object.data.bones.active.select = False
                    bone.select = True
<<<<<<< HEAD
                    bone.RobotDesigner.Euler.z.value = M_M_newch_real[indiv][b][2]  #z position
=======
                    bone.RobotEditor.Euler.z.value = M_M_newch_real[indiv][b][2]  #z position
>>>>>>> c729e77

                visualprop(gen, robot_tosimulate, M_bones_list, M_M_newch_real, M_ch_real, list_instances, indiv, tree_structure, initial_bone_position, initial_mesh_position) #change meshes' visual properties

            bpy.ops.object.select_all(action='DESELECT')
<<<<<<< HEAD
            bpy.ops.robotdesigner.selectarmature(model_name=robot_tosimulate)

            return None

        def sendparametersbest(gen, robot_tosimulate, M_M_newch_real, M_bones_list, M_ch_real, tree_structure, fitness, initial_bone_position, initial_mesh_position):
            """
            send segment's position value to Blender when only the best individual is plotted
            """
=======
            bpy.ops.roboteditor.selectarmature(model_name=robot_tosimulate)

            return None

        def sendparametersbest(gen, robot_tosimulate, M_M_newch_real, M_bones_list, M_ch_real, tree_structure, fitness, initial_bone_position, initial_mesh_position): #send segment's position value to Blender when only the best individual is plotted

>>>>>>> c729e77
            best_fitness = max(fitness) #get best individual
            index_best = fitness.index(best_fitness)

            for b in range(len(M_bones_list)):
                mesh = [obj.name for obj in bpy.data.objects if
                        obj.parent_bone == bpy.data.armatures[robot_tosimulate].bones[M_bones_list[b]].name
<<<<<<< HEAD
                        and obj.type == 'MESH' and obj.RobotDesigner.tag == "DEFAULT"]
=======
                        and obj.type == 'MESH']
>>>>>>> c729e77

                if not bpy.data.armatures[robot_tosimulate].bones[M_bones_list[b]].parent_recursive or not mesh: #not moving metaparent or bones without mesh
                    None
                else:
                    bone = bpy.context.active_object.data.bones[M_bones_list[b]]
                    bpy.context.active_object.data.bones.active.select = False
                    bone.select = True
<<<<<<< HEAD
                    bone.RobotDesigner.Euler.x.value = M_M_newch_real[index_best][b][0]  # x position
=======
                    bone.RobotEditor.Euler.x.value = M_M_newch_real[index_best][b][0]  # x position
>>>>>>> c729e77

                    bone = bpy.context.active_object.data.bones[M_bones_list[b]]
                    bpy.context.active_object.data.bones.active.select = False
                    bone.select = True
<<<<<<< HEAD
                    bone.RobotDesigner.Euler.y.value = M_M_newch_real[index_best][b][1]  # y position
=======
                    bone.RobotEditor.Euler.y.value = M_M_newch_real[index_best][b][1]  # y position
>>>>>>> c729e77

                    bone = bpy.context.active_object.data.bones[M_bones_list[b]]
                    bpy.context.active_object.data.bones.active.select = False
                    bone.select = True
<<<<<<< HEAD
                    bone.RobotDesigner.Euler.z.value = M_M_newch_real[index_best][b][2]  # z position
=======
                    bone.RobotEditor.Euler.z.value = M_M_newch_real[index_best][b][2]  # z position
>>>>>>> c729e77

            visualprop(gen, robot_tosimulate, M_bones_list, M_M_newch_real, M_ch_real, M_bones_list, index_best, tree_structure, initial_bone_position, initial_mesh_position)

            bpy.ops.object.select_all(action='DESELECT')
<<<<<<< HEAD
            bpy.ops.robotdesigner.selectarmature(model_name=robot_tosimulate)

            return None

        def toolbox(max_gen, M_fitness, M_bones_list, M_M_M_historial, M_ch_real):
            """
            function to write in a csv the evaluation data to get the plots. it should be used in combination with the file "plots_ea", since matplotlib does not work in blender
            """
=======
            bpy.ops.roboteditor.selectarmature(model_name=robot_tosimulate)

            return None

        def toolbox(max_gen, M_fitness, M_bones_list, M_M_M_historial, M_ch_real): #function to write in a csv the evaluation data to get the plots. it should be used in combination with the file "plots_ea", since matplotlib does not work in blender

>>>>>>> c729e77
            def removecsvfile (fname):
                os.remove(fname)

                return None

            def csvwrite(fname, xval, yval):
                with open(fname, 'a', newline='') as csvfile:
                    fplot = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    fplot.writerow([xval, yval])

                return None

<<<<<<< HEAD
            def fitnessplot (max_gen, M_fitness):
                """
                specify path for the cvs
                """
=======
            def fitnessplot (max_gen, M_fitness): #specify path for the cvs
>>>>>>> c729e77
                fname = 'C:/tmp/fitness.csv'
                if os.path.isfile(fname)==True:
                    removecsvfile(fname)

                for g in range (max_gen+1):
                    av_f = np.mean(M_fitness[g])
                    csvwrite(fname, g, av_f)

                return None

<<<<<<< HEAD
            def growthplot (max_gen, M_bones_list, M_M_M_historial, M_ch_real):
                """
                specify path for the cvs
                """
=======
            def growthplot (max_gen, M_bones_list, M_M_M_historial, M_ch_real): #specify path for the cvs
>>>>>>> c729e77
                fname1 = 'C:/tmp/maxgrowth.csv'
                if os.path.isfile(fname1)==True:
                    removecsvfile(fname1)

                for g in range(max_gen):
                    dmax_individualgen=[]

                    for ig in range(len(M_M_M_historial[g])): #comupute maximum growth of the generation
                        dxmax, dymax, dzmax=0,0,0

                        for b in range(len(M_bones_list)):
                            dx, dy, dz = abs(M_M_M_historial[g][ig][b][0] - M_ch_real[b][0]), abs(
                                M_M_M_historial[g][ig][b][1] - M_ch_real[b][1]), abs(
                                M_M_M_historial[g][ig][b][2] - M_ch_real[b][2])
                            if dx > dxmax:
                                dxmax = dx
                            if dy > dymax:
                                dymax = dy
                            if dz > dzmax:
                                dzmax = dz

                        dmax_individualgen.append(max(dxmax, dymax, dzmax))

                    dmax_gen = max(dmax_individualgen)

                    csvwrite(fname1, g+1, dmax_gen)

                return None

            fitnessplot(max_gen, M_fitness)
            growthplot(max_gen, M_bones_list, M_M_M_historial, M_ch_real)

            return None


<<<<<<< HEAD
        def main():
            """
            Main function for the simulator
            """
=======
        """Main function for the simulator"""
        def main():
>>>>>>> c729e77
            gen=0
            RD=context.scene.RobotDesigner
            numberindividuals = RD.population_size  # number of individuals for simulation in generation 0
            historial_ch = []
            blenderrobots = RD.model_to_simulate  # individuals existing in Blender
            max_gen = RD.max_generation
            num_offspring = RD.offspring_size
            mutation_rate_bin = RD.mutation_rate_bin
            mutation_rate_real = RD.mutation_rate_real
            mutation_deviation = RD.mutation_deviation
            s_rate = RD.selection_rate
            offset_o=RD.offsetlateral
            offset_g=RD.offsetfront
            result = global_properties.visualresult.get(context.scene)
            plot = global_properties.toolbox.get(context.scene)
            encoding = global_properties.encoding.get(context.scene)

            robot_to_simulate = selectrobot(blenderrobots)
            bones = listbones(numberindividuals, robot_to_simulate)
            ch_real_robot0 = getparameters(bones, robot_to_simulate)
            list_instances = [['' for i in range(num_offspring)] for j in range(max_gen)]
            tree_structure=robotstructure(bones, robot_to_simulate)
            ini_bone_position = iniboneposition(bones, robot_to_simulate)
            ini_mesh_position = inimeshposition()
            matrix_direction = []
            M_fitness=[]


            while gen!=max_gen:  #loop for evolving the individuals. Each gen, one iteration.

                ch_real = individualsgen(gen, historial_ch, bones, ch_real_robot0)
                fitness, parent, matrix_direction, M_fitness = fitnessf(gen, bones, ch_real, tree_structure, matrix_direction, M_fitness)

                if encoding == 'binary': #bear in mind this type of EA has not been developed completely in an optimized way
                    upper_limit, lower_limit, decimal_precision = int(10), -int(10), 1  # limits for the x,y and z position of the segments and number of decimals for the position parameter. Manually tune depending model
                    bits_string, normaliz = numbits(upper_limit, lower_limit, decimal_precision)
                    ch_bin = code(ch_real, bones, normaliz, decimal_precision, bits_string)
                    matched_ch = selectionbin(gen, ch_bin, num_offspring, s_rate, fitness)
                    ch_cro = crossoverbin(bits_string, matched_ch, ch_bin)
                    ch_mut = mutationbin(gen,ch_cro, ch_bin, bits_string, mutation_rate_bin)
                    ch_new_real = decode(ch_mut, bones, normaliz, decimal_precision)
                if encoding == 'real':
                    matched_ch = selectionreal(gen, ch_real, num_offspring, s_rate, fitness)
                    ch_cro = crossoverreal(matched_ch, ch_real)
                    ch_mut = mutationreal(ch_cro, ch_real, mutation_rate_real, mutation_deviation)
                    ch_new_real = ch_mut
                historial_ch = historialgen(ch_new_real, historial_ch)

                gen += 1

                if result=='all':
                    list_instances = createrobotinstances(gen, num_offspring, robot_to_simulate, bones, list_instances,offset_o,offset_g)
                    sendparametersall(gen, robot_to_simulate, ch_new_real, bones, num_offspring, list_instances, ch_real_robot0,  tree_structure, ini_bone_position, ini_mesh_position)

            fitness, parent, matrix_direction, M_fitness = fitnessf(gen, bones, ch_new_real, tree_structure, matrix_direction, M_fitness)

            if result=='best':
                sendparametersbest(gen, robot_to_simulate, ch_new_real, bones,  ch_real_robot0,  tree_structure, fitness, ini_bone_position, ini_mesh_position)

            if plot=='on':
                toolbox(max_gen, M_fitness, bones, historial_ch, ch_real_robot0)

            return None

        main()

        return {'FINISHED'}


@RDOperator.Preconditions(ModelSelected)
@PluginManager.register_class
class StartSimulationMeshes(RDOperator):
    """
    :ref:`operator` for start simulation EA applied to meshes' nodes position.
    """
    bl_idname = config.OPERATOR_PREFIX + "start_sim_mesh"
    bl_label = "Start Simulation"

    @classmethod
    def run(cls):
        """
        Run this operator
        """
        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected)
    def execute(self, context):

<<<<<<< HEAD
        def selectrobot(robot_to_sim):
            """
            select robot to simulate
            """
            print("Select Robot")
=======
        def selectrobot(robot_to_sim):  #select robot to simulate
>>>>>>> c729e77
            armature_name = robot_to_sim[0].name

            return armature_name

<<<<<<< HEAD
        def editmode_mesh(mesh_to_edit):
            """
            go to edit mode
            """
            print("Edit Mode Mesh")
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.select_all(action='DESELECT')
            mesh = bpy.data.objects[mesh_to_edit]
            mesh.select = True
            bpy.context.scene.objects.active = mesh
=======
        def editmode_mesh(mesh_to_edit): #go to edit mode
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.object.select_all(action='DESELECT')
            mesh = bpy.data.objects[mesh_to_edit]
            mesh.select_set(True)
            bpy.context.view_layer.objects.active = mesh
>>>>>>> c729e77
            bpy.ops.object.mode_set(mode='EDIT', toggle=False)

            obj = bpy.context.object.data
            bm = bmesh.from_edit_mesh(obj)
            return bm, obj, mesh

<<<<<<< HEAD
        def meshes_initial_armature (armature_name):
            """
            get meshes of robot to simulate
            """
            meshes_name = [obj.name for obj in bpy.data.objects \
                        if obj.parent_bone is not None and obj.type == 'MESH' \
                         and obj.RobotDesigner.tag == "DEFAULT"]
            print("Meshes initial armature are ", meshes_name)

            return meshes_name

        def armatures_scene ():
            """
            get all armatures of the Blender scene
            """
            print("Armatures scene")
=======
        def meshes_initial_armature (armature_name):  #get meshes of robot to simulate
            meshes_name = [obj.name for obj in bpy.data.objects if obj.parent_bone is not None and obj.type == 'MESH']

            return meshes_name

        def armatures_scene ():  #get all armatures of the Blender scene
>>>>>>> c729e77
            armatures = [obj.name for obj in bpy.data.objects if obj.type == 'ARMATURE']

            return armatures

<<<<<<< HEAD
        def verts_co (armature_name, meshes):
            """
            get verts xyz position for the armature armature_name
            """
            print("Verts co")
=======
        def verts_co (armature_name, meshes): #get verts xyz position for the armature armature_name
>>>>>>> c729e77
            pos_verts = [[] for m in range(len(meshes))]

            for m in range(len(meshes)):
                bm, obj, mesh = editmode_mesh(meshes[m])

                for v in range(len(bm.verts)):
                    bm.verts.ensure_lookup_table()
                    pos_verts[m].append(bm.verts[v].co)

                pos_verts[m] = np.asarray(pos_verts[m])

            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
<<<<<<< HEAD
            bpy.ops.robotdesigner.selectarmature(model_name=armature_name)
=======
            bpy.ops.roboteditor.selectarmature(model_name=armature_name)
>>>>>>> c729e77


            return pos_verts

<<<<<<< HEAD
        def individualsgen (gen, pos_verts, historial_individuals):
            """
            get verts' position of individuals
            """
            print("inidividualsgen")
=======
        def individualsgen (gen, pos_verts, historial_individuals):  #get verts' position of individuals
>>>>>>> c729e77
            if gen == 0:
                individuals_ch = [pos_verts, pos_verts]

            else:
                individuals_ch = historial_individuals[gen-1]

            return individuals_ch

<<<<<<< HEAD
        def historialgen (individuals_ch, historial_individuals):
            """
            store verts position of the population individuals
            """
            print("historialgen")
=======
        def historialgen (individuals_ch, historial_individuals):  #store verts position of the population individuals
>>>>>>> c729e77
            historial_individuals.append(individuals_ch)

            return historial_individuals

<<<<<<< HEAD
        def fitnessfunction (individuals_ch, ini_verts_co, meshes):
            """
            compute fitness of each vert of the meshes to get mesh fitness and, by summing all meshes fitness, claculate individual fitness
            """
            print("Fitnessfunction")
=======
        def fitnessfunction (individuals_ch, ini_verts_co, meshes): #compute fitness of each vert of the meshes to get mesh fitness and, by summing all meshes fitness, claculate individual fitness

>>>>>>> c729e77
            fitness = []
            for ind in range(len(individuals_ch)):
                f_ind = []
                for m in range(len(meshes)):
                    for v in range(len(individuals_ch[0][m])):
                        for coo in range(3):
                            function = (individuals_ch[ind][m][v][coo] - ini_verts_co[m][v][coo])
                            if ini_verts_co[m][v][coo] > 0:
                                f = function*1e3 #1e3 is the weight value to calculate fitness
                            else:
                                f = -function*1e3
                            f_ind.append(f)

                fitness.append(np.sum(f_ind))
<<<<<<< HEAD
            print("Fitness is:", fitness)
            return fitness

        def selection (gen, individuals_ch, num_offspring, s_rate, fitnesses):
            """
            selection: mate 2 x num_offspring times the individuals for kepping offspring population size after crossover
            """
            print("Selection")
=======

            return fitness

        def selection (gen, individuals_ch, num_offspring, s_rate, fitnesses):  #selection: mate 2 x num_offspring times the individuals for kepping offspring population size after crossover
>>>>>>> c729e77
            selected = []

            if gen==0:
                for o in range(num_offspring):
                    selected.append(individuals_ch)

            else:  #rank selection
                fitnesses_sorted = sorted(fitnesses,reverse=True) #get fitter individuals
                best_fitnesses = fitnesses_sorted[0:int(s_rate*len(fitnesses))+1]
                indexes_best = [fitnesses.index(f) for f in best_fitnesses]

                b=0 #counter
                for i in range(num_offspring):
                    pair = [individuals_ch[indexes_best[b]], individuals_ch[indexes_best[b+1]]]
                    selected.append(pair)
                    b+=2
                    if len(indexes_best) % 2 == 0:
                        if b>=int(s_rate*len(fitnesses)):
                            b=0
                    else:
                        if b>=(int(s_rate*len(fitnesses))-1):
                            b=0

            return selected

<<<<<<< HEAD
        def crossover (selected, meshes):
            """
            crossover
            """
            print("Crossover")
=======
        def crossover (selected, meshes): #crossover
>>>>>>> c729e77
            crossed = []

            for s in range(len(selected)):
                crossed_ind = []
                for m in range(len(meshes)):
                    cross_off = [[0 for i in range(len(selected[s][0][m][0]))] for j in range(len(selected[s][0][m]))]
                    for row in range (len(selected[s][0][m])):
                            if random.random() < 0.5:#offspring gets the parameter's value of one parent, or the another, with 50% probability
                                cross_off[row] = selected[s][0][m][row]
                            else:
                                cross_off[row] = selected[s][1][m][row]
                    crossed_ind.append(cross_off)

                crossed.append(crossed_ind)

            return crossed

        def mutation (crossed, mutation_rate, mutation_deviation, meshes):
<<<<<<< HEAD
            """
            mutation
            """
            print("Mutation")
=======

>>>>>>> c729e77
            mutated = []
            for o in range(len(crossed)):
                mutated_ind = []
                for m in range(len(meshes)):
                    mutate_off = [[0 for i in range(len(crossed[o][m][0]))] for j in range(len(crossed[o][m]))]

                    for row in range(len(crossed[o][m])):
                                if random.random() < mutation_rate:
                                    abs_vert = np.sum(abs(np.asarray(crossed[o][m][row])))
                                    p_vert = np.array([crossed[o][m][row][j]/abs_vert for j in range (3)]) #compute scaling factor for each xyz position of the vert (to get smoother results)
                                    mutate_off[row] = crossed[o][m][row] + np.random.normal(0, mutation_deviation) * p_vert

                                else:
                                    mutate_off[row] = crossed[o][m][row]
                    mutated_ind.append(mutate_off)

                mutated.append(mutated_ind)

            return mutated

<<<<<<< HEAD
        def best_ind (mutated, ini_verts_co, meshes):
            """
            get best infividual of a generation
            """
            print("Best Individual")
            fitness_last = fitnessfunction(mutated, ini_verts_co, meshes)
            best_fitness = max(fitness_last)
            index_best = fitness_last.index(best_fitness)
            print("Best individual number: ", index_best)
            return index_best

        def neighbours_adapt (mutated, armature_name, meshes, adapt_rate, ind):
            """
            adaptability function to get smoother geometries
            """
            print("Neighbours Adapt")
=======
        def best_ind (mutated, ini_verts_co, meshes): #get best infividual of a generation

            fitness_last = fitnessfunction(mutated, ini_verts_co, meshes)
            best_fitness = max(fitness_last)
            index_best = fitness_last.index(best_fitness)

            return index_best

        def neighbours_adapt (mutated, armature_name, meshes, adapt_rate, ind): # adaptability function to get smoother geometries

>>>>>>> c729e77
            for m in range(len(meshes)):
                bm, obj, mesh = editmode_mesh(meshes[m])

                for v in range(len(bm.verts)):
                    bm.verts.ensure_lookup_table()
                    neighbour1 = [0 for ed1 in range(len(bm.verts[v].link_edges))]
                    n_v_1 = [[0,0,0] for ed1 in range(len(bm.verts[v].link_edges))]

                    for ed1 in range(len(bm.verts[v].link_edges)):
                        bm.edges.ensure_lookup_table()
                        neighbour1[ed1] =  bm.verts[v].link_edges[ed1].verts[1].index #first level vertexes neighbours of the vertex v
                        if neighbour1[ed1] == v: #check if it is the correct vertex and not v
                            neighbour1[ed1] = bm.verts[v].link_edges[ed1].verts[0].index
                        n_v_1[ed1] = mutated[ind][m][neighbour1[ed1]]

                    n_v_2 = []
                    for n1 in range(len(bm.verts[v].link_edges)):
                        for ed2 in range(len(bm.verts[neighbour1[n1]].link_edges)):
                            bm.edges.ensure_lookup_table()
                            neighbour2 = bm.verts[neighbour1[n1]].link_edges[ed2].verts[1].index #second level vertexes neighbours of the vertex v
                            if neighbour2==neighbour1[n1]: #check
                                neighbour2 = bm.verts[neighbour1[n1]].link_edges[ed2].verts[0].index
                            if neighbour2 not in neighbour1: # take out from the list of it is repeated
                                n_v_2.append(mutated[ind][m][neighbour2])

                    if n_v_1:
                        average_neighbours_1 = np.mean(n_v_1, 0)
                    else: #avoid errors
                        average_neighbours_1 = [0,0,0]
                    if n_v_2:
                        average_neighbours_2 = np.mean(n_v_2, 0)
                    else: #avoid errors
                        average_neighbours_2 = [0,0,0]

                    mutated[ind][m][v] = np.asarray(mutated[ind][m][v])*(1-adapt_rate) + (average_neighbours_1+average_neighbours_2)/2 *adapt_rate #give value

                offspring_adapted = mutated
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.select_all(action='DESELECT')
<<<<<<< HEAD
                bpy.ops.robotdesigner.selectarmature(model_name=armature_name)

            return offspring_adapted

        def minvertexbonedistance(armature_name, meshes):
            """
            get closer vertex of the bones to meshes
            """
            print("Min vertex bone distance")
            local_pos_verts = np.asarray(verts_co(armature_name, meshes))

            def level_up_parent(armature_name, segment):
                """
                go to the parent of a particular segment
                """
=======
                bpy.ops.roboteditor.selectarmature(model_name=armature_name)

            return offspring_adapted

        def minvertexbonedistance(armature_name, meshes): #get closer vertex of the bones to meshes
            local_pos_verts = np.asarray(verts_co(armature_name, meshes))

            def level_up_parent(armature_name, segment): #go to the parent of a particular segment

>>>>>>> c729e77
                if bpy.data.armatures[armature_name].bones[segment].parent:
                    segment_up = bpy.data.armatures[armature_name].bones[segment].parent.name
                else:
                    segment_up=segment

                return segment_up

<<<<<<< HEAD
            def checkmesh(armature_name, parent_ofsegment_name):
                """
                check if the bone has a mesh attached. If not, go to its parent
                """
                mesh = [obj.name for obj in bpy.data.objects if obj.parent_bone == bpy.data.armatures[armature_name].bones[parent_ofsegment_name].name
                        and obj.type == 'MESH' and obj.RobotDesigner.tag == "DEFAULT"]
=======
            def checkmesh(armature_name, parent_ofsegment_name): #check if the bone has a mesh attached. If not, go to its parent
                mesh = [obj.name for obj in bpy.data.objects if obj.parent_bone == bpy.data.armatures[armature_name].bones[parent_ofsegment_name].name
                        and obj.type == 'MESH']
>>>>>>> c729e77

                if not mesh:
                    parent_ofsegment_name = level_up_parent(armature_name, parent_ofsegment_name)

                return parent_ofsegment_name

            min_index_parent_vert = []
            meshes_up = []
            initial_segment_position = []
            global_pos_mesh_initial =[]
            for m in range(len(meshes)):
                segment_ofmesh_name = bpy.data.objects[meshes[m]].parent_bone
                parent_ofsegment_name = level_up_parent(armature_name, segment_ofmesh_name)
                parent_ofsegment_name = checkmesh(armature_name, parent_ofsegment_name)
                mesh_up = [obj.name for obj in bpy.data.objects if bpy.data.objects[obj.name].parent_bone == parent_ofsegment_name and obj.type == 'MESH'
<<<<<<< HEAD
                           and obj.RobotDesigner.tag==bpy.data.objects[meshes[m]].RobotDesigner.tag][0] #get meshes of the parent segment
=======
                           and obj.RobotEditor.tag==bpy.data.objects[meshes[m]].RobotEditor.tag][0] #get meshes of the parent segment
>>>>>>> c729e77
                m_up = meshes.index(mesh_up)

                global_pos_mesh = np.asarray(bpy.data.objects[meshes[m]].matrix_world.to_translation())
                global_pos_mesh_up = np.asarray(bpy.data.objects[meshes[m_up]].matrix_world.to_translation()) #up means of the parent segment
                scale_factor = np.asarray(bpy.data.objects[meshes[m]].scale)
                scale_factor_up = np.asarray(bpy.data.objects[meshes[m_up]].scale)
                global_pos_verts = [(local_pos_verts[m][v] * scale_factor + global_pos_mesh) for v in range(len(local_pos_verts[m]))]
                global_pos_verts_up = [(local_pos_verts[m_up][v] * scale_factor_up + global_pos_mesh_up) for v in range(len(local_pos_verts[m_up]))]

                global_pos_parent_bone = np.asarray(bpy.data.armatures[armature_name].bones[segment_ofmesh_name].head_local)

                dist_parent_vert = [(math.sqrt((global_pos_verts[v][0]-global_pos_parent_bone[0])**2 #distance between vertexes and parent segment
                                               +(global_pos_verts[v][1]-global_pos_parent_bone[1])**2
                                               +(global_pos_verts[v][2]-global_pos_parent_bone[2])**2)) for v in range(len(global_pos_verts))]
                dist_parent_vert_up = [(math.sqrt((global_pos_verts_up[v][0]-global_pos_parent_bone[0])**2
                                               +(global_pos_verts_up[v][1]-global_pos_parent_bone[1])**2
                                               +(global_pos_verts_up[v][2]-global_pos_parent_bone[2])**2)) for v in range(len(global_pos_verts_up))]

                min_index_parent_vert.append([dist_parent_vert.index(min(dist_parent_vert)), dist_parent_vert_up.index(min(dist_parent_vert_up))]) # get the vertex that is closer
                meshes_up.append(m_up)
                initial_segment_position.append(global_pos_parent_bone) #get initial segment position
                global_pos_mesh_initial.append(global_pos_mesh_up) #get initial mesh position

            return min_index_parent_vert, meshes_up, initial_segment_position, global_pos_mesh_initial

<<<<<<< HEAD
        def sendparametersbest (offspring_generation, ini_verts_co, armature_name, meshes):
            """
            send verts xyz position to Blender for the best individual
            """
            print("Send parameter best")
=======
        def sendparametersbest (offspring_generation, ini_verts_co, armature_name, meshes): #send verts xyz position to Blender for the best individual
>>>>>>> c729e77
            fitness_last = fitnessfunction(offspring_generation, ini_verts_co, meshes)
            best_fitness = max(fitness_last)
            index_best = fitness_last.index(best_fitness)

            for m in range(len(meshes)):
                bm, obj, mesh = editmode_mesh(meshes[m])

                for v in range(len(bm.verts)):
                    bm.verts.ensure_lookup_table()
                    bm.verts[v].select = True

                    bm.verts[v].co = offspring_generation[index_best][m][v]
                    bmesh.update_edit_mesh(obj, True)
                    bm.verts[v].select = False
                    bmesh.update_edit_mesh(obj, True)

<<<<<<< HEAD
                mesh.select = False

            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.robotdesigner.selectarmature(model_name=armature_name)

            return None

        def sendparametersgen (indiv_generation, armature_name, list_instances, gen, ind):
            """
            send verts xyz position to Blender for the best individual
            """
            print("Send parameters gen")
            bpy.ops.object.select_all(action='DESELECT')
            context.scene.objects.active = bpy.data.objects[list_instances[gen][ind]]
            context.active_object.select = True
            meshes = [obj.name for obj in bpy.data.objects \
                        if obj.parent_bone is not None and obj.type == 'MESH' \
                        and obj.RobotDesigner.tag == "DEFAULT" \
                        and obj.parent.name == list_instances[gen][ind]]
=======
                mesh.select_set(False)

            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.roboteditor.selectarmature(model_name=armature_name)

            return None

        def sendparametersgen (indiv_generation, armature_name, list_instances, gen, ind): #send verts xyz position to Blender for the best individual

            bpy.ops.object.select_all(action='DESELECT')
            context.scene.objects.active = bpy.data.objects[list_instances[gen][ind]]
            context.active_object.select_set(True)
            meshes = [obj.name for obj in bpy.data.objects if obj.parent_bone is not None and obj.type == 'MESH'
                           and obj.parent.name == list_instances[gen][ind]]
>>>>>>> c729e77

            for m in range(len(meshes)):
                bm, obj, mesh = editmode_mesh(meshes[m])

                for v in range(len(bm.verts)):
                    bm.verts.ensure_lookup_table()
                    bm.verts[v].select = True

                    bm.verts[v].co = indiv_generation[ind][m][v]
                    bmesh.update_edit_mesh(obj, True)
                    bm.verts[v].select = False
                    bmesh.update_edit_mesh(obj, True)

<<<<<<< HEAD
                mesh.select = False

            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.robotdesigner.selectarmature(model_name=armature_name)

            return None

        def bonematrixrotation(armature_name, segment, coo):
            """
            matrix rotation of the bones to achieve correct vertex position when translating them in local
            """
            print("Bone matrix Rotation")
=======
                mesh.select_set(False)

            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.roboteditor.selectarmature(model_name=armature_name)

            return None

        def bonematrixrotation(armature_name, segment, coo): #matrix rotation of the bones to achieve correct vertex position when translating them in local

>>>>>>> c729e77
            bone = bpy.data.armatures[armature_name].bones[segment].parent
            gAl = np.identity(3)

            while bone != None:
                A = bone.matrix
                gAl = np.dot(A, gAl)
                bone = bone.parent

            lAg = np.linalg.inv(gAl)
            d_l = np.dot(lAg, coo)

            return d_l

<<<<<<< HEAD
        def placejoints_mesh (armature_name, min_index_parent_vert, ini_position_verts):
            """
            place mesh bone on the correct mesh spot
            """
            print("Place joints mesh1")
            def reassign_mesh(meshes, m, segment_ofmesh_name, armature_name, new_mesh_name):
                segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects[new_mesh_name[4:]].select = True
=======
        def placejoints_mesh (armature_name, min_index_parent_vert, ini_position_verts): #place mesh bone on the correct mesh spot

            def reassign_mesh(meshes, m, segment_ofmesh_name, armature_name, new_mesh_name):
                segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects[new_mesh_name].select_set(True)
>>>>>>> c729e77
                bpy.context.active_object.data.bones.active = segment_ofmesh
                bpy.context.active_object.data.bones.active.select = True
                bpy.context.scene.objects.active = bpy.data.objects[armature_name]
                bpy.ops.object.parent_set(type='BONE', keep_transform=True)
<<<<<<< HEAD
                obj = bpy.data.objects[new_mesh_name[4:]]
                obj.name = meshes[m]
                obj.RobotDesigner.fileName = obj.name
                if meshes[m][:3]=='COL':
                    obj.RobotDesigner.tag = 'COLLISION'
                else:
                    obj.RobotDesigner.tag == 'DEFAULT'
=======
                obj = bpy.data.objects[new_mesh_name]
                obj.name = meshes[m]
                obj.RobotEditor.fileName = obj.name
                if meshes[m][:3]=='COL':
                    obj.RobotEditor.tag = 'COLLISION'
                else:
                    obj.RobotEditor.tag == 'DEFAULT'
>>>>>>> c729e77

                return None

            bpy.ops.object.select_all(action='DESELECT')
            context.scene.objects.active = bpy.data.objects[armature_name]
<<<<<<< HEAD
            context.active_object.select = True

            meshes = [obj.name for obj in bpy.data.objects \
                    if obj.parent_bone is not None and obj.type == 'MESH' \
                    and obj.RobotDesigner.tag == "DEFAULT" \
                    and obj.parent.name == armature_name]

            for m in range(len(meshes)):
                print("range1", m)
                print("range1", meshes[m])
                print("range1",bpy.data.objects[meshes[m]].parent_bone)
=======
            context.active_object.select_set(True)

            meshes = [obj.name for obj in bpy.data.objects if obj.parent_bone is not None and obj.type == 'MESH'
                   and obj.parent.name == armature_name]

            for m in range(len(meshes)):

>>>>>>> c729e77
                segment_ofmesh_name = bpy.data.objects[meshes[m]].parent_bone

                bm, obj, _ = editmode_mesh(meshes[m])
                bm.verts.ensure_lookup_table()
                co_parent_joint_G = np.asarray(bm.verts[min_index_parent_vert[m][0]].co) - np.asarray(ini_position_verts[m][min_index_parent_vert[m][0]])
                co_parent_joint = bonematrixrotation(armature_name, segment_ofmesh_name, co_parent_joint_G)

                bpy.ops.object.mode_set(mode='OBJECT')
<<<<<<< HEAD
                bpy.ops.robotdesigner.selectarmature(model_name=armature_name)
                segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]

                bpy.ops.robotdesigner.select_geometry(geometry_name=meshes[m])
                bpy.ops.robotdesigner.unassignmesh()
                new_mesh_name = meshes[m] # BF bpy.context.selected_objects[0].name
                bpy.ops.object.select_all(action='DESELECT')

                segment_ofmesh.select = True
                segment_ofmesh.RobotDesigner.Euler.x.value += co_parent_joint[0]
=======
                bpy.ops.roboteditor.selectarmature(model_name=armature_name)
                segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]

                bpy.ops.roboteditor.select_geometry(geometry_name=meshes[m])
                bpy.ops.roboteditor.unassignmesh()
                new_mesh_name = bpy.context.selected_objects[0].name
                bpy.ops.object.select_all(action='DESELECT')

                segment_ofmesh.select = True
                segment_ofmesh.RobotEditor.Euler.x.value += co_parent_joint[0]
>>>>>>> c729e77
                segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                segment_ofmesh.select = False

                segment_ofmesh.select = True
<<<<<<< HEAD
                segment_ofmesh.RobotDesigner.Euler.y.value += co_parent_joint[1]
=======
                segment_ofmesh.RobotEditor.Euler.y.value += co_parent_joint[1]
>>>>>>> c729e77
                segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                segment_ofmesh.select = False

                segment_ofmesh.select = True
<<<<<<< HEAD
                segment_ofmesh.RobotDesigner.Euler.z.value += co_parent_joint[2]

=======
                segment_ofmesh.RobotEditor.Euler.z.value += co_parent_joint[2]
>>>>>>> c729e77
                segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                segment_ofmesh.select = False

                reassign_mesh(meshes, m, segment_ofmesh_name, armature_name, new_mesh_name)
                bpy.ops.object.select_all(action='DESELECT')

<<<<<<< HEAD
                bpy.ops.robotdesigner.selectarmature(model_name=armature_name)
            print("Place joints mesh done")

            return None

        def placejoints_model (armature_name, min_index_parent_vert, meshes_up, segment_ini_pos, ini_position_verts, mesh_pos_ini):
            """
            place bone on the correct bone spot
            """
            print("Place joints model")
            meshes = [obj.name for obj in bpy.data.objects \
                    if obj.parent_bone is not None and obj.type == 'MESH'\
                     and obj.RobotDesigner.tag == "DEFAULT" \
                     and obj.parent.name == armature_name]
=======
                bpy.ops.roboteditor.selectarmature(model_name=armature_name)

            return None

        def placejoints_model (armature_name, min_index_parent_vert, meshes_up, segment_ini_pos, ini_position_verts, mesh_pos_ini): #place bone on the correct bone spot

            meshes = [obj.name for obj in bpy.data.objects if obj.parent_bone is not None and obj.type == 'MESH'
                      and obj.parent.name == armature_name]
>>>>>>> c729e77

            for m in range(len(meshes)):
                segment_ofmesh_name = bpy.data.objects[meshes[m]].parent_bone

                bm, obj, _ = editmode_mesh(meshes[meshes_up[m]])
                bm.verts.ensure_lookup_table()
                global_pos_mesh = np.asarray(bpy.data.objects[meshes[meshes_up[m]]].matrix_world.to_translation())
                armature_location = np.asarray(bpy.data.objects[armature_name].location)
                segment_pos = np.asarray(bpy.data.armatures[armature_name].bones[segment_ofmesh_name].head_local)

                co_parent_joint_G = (np.asarray(bm.verts[min_index_parent_vert[m][1]].co) +global_pos_mesh - segment_pos) - \
                                    (np.asarray(ini_position_verts[meshes_up[m]][min_index_parent_vert[m][1]])+mesh_pos_ini[m]
                                     - segment_ini_pos[m]) - armature_location #global position of the bone

                co_parent_joint = bonematrixrotation(armature_name, segment_ofmesh_name, co_parent_joint_G) #from global coordinates to local

                bpy.ops.object.mode_set(mode='OBJECT')
<<<<<<< HEAD
                bpy.ops.robotdesigner.selectarmature(model_name=armature_name)
=======
                bpy.ops.roboteditor.selectarmature(model_name=armature_name)
>>>>>>> c729e77
                segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]

                if not bpy.data.armatures[armature_name].bones[segment_ofmesh_name].parent_recursive: #keep metaparent bone at the same spot as the original model
                    fix_parent = bonematrixrotation(armature_name, segment_ofmesh_name, segment_ini_pos[m])
                    segment_ofmesh.select = True
<<<<<<< HEAD
                    segment_ofmesh.RobotDesigner.Euler.x.value = fix_parent[0]
=======
                    segment_ofmesh.RobotEditor.Euler.x.value = fix_parent[0]
>>>>>>> c729e77
                    segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                    segment_ofmesh.select = False

                    segment_ofmesh.select = True
<<<<<<< HEAD
                    segment_ofmesh.RobotDesigner.Euler.y.value = fix_parent[1]
=======
                    segment_ofmesh.RobotEditor.Euler.y.value = fix_parent[1]
>>>>>>> c729e77
                    segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                    segment_ofmesh.select = False

                    segment_ofmesh.select = True
<<<<<<< HEAD
                    segment_ofmesh.RobotDesigner.Euler.z.value = fix_parent[2]
=======
                    segment_ofmesh.RobotEditor.Euler.z.value = fix_parent[2]
>>>>>>> c729e77
                    segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                    segment_ofmesh.select = False

                else:
                    segment_ofmesh.select = True
<<<<<<< HEAD
                    segment_ofmesh.RobotDesigner.Euler.x.value += co_parent_joint[0]
=======
                    segment_ofmesh.RobotEditor.Euler.x.value += co_parent_joint[0]
>>>>>>> c729e77
                    segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                    segment_ofmesh.select = False

                    segment_ofmesh.select = True
<<<<<<< HEAD
                    segment_ofmesh.RobotDesigner.Euler.y.value += co_parent_joint[1]
=======
                    segment_ofmesh.RobotEditor.Euler.y.value += co_parent_joint[1]
>>>>>>> c729e77
                    segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                    segment_ofmesh.select = False

                    segment_ofmesh.select = True
<<<<<<< HEAD
                    segment_ofmesh.RobotDesigner.Euler.z.value += co_parent_joint[2]
=======
                    segment_ofmesh.RobotEditor.Euler.z.value += co_parent_joint[2]
>>>>>>> c729e77
                    segment_ofmesh = bpy.context.active_object.data.bones[segment_ofmesh_name]
                    segment_ofmesh.select = False

            return None

<<<<<<< HEAD
        def createrobotinstances(generations, num_offspring, armature_name, meshes, offset_o, offset_g):
            """
            create robot instances to plot all individuals
            """
            print("Create robot instances")
=======
        def createrobotinstances(generations, num_offspring, armature_name, meshes, offset_o, offset_g): #create robot instances to plot all individuals

>>>>>>> c729e77
            list_instances = [['' for i in range(num_offspring)] for g in range(generations)]

            for g in range(generations):
                for i in range(num_offspring):
                    context.scene.objects.active = bpy.data.objects[armature_name]
                    context.active_object.select = True
                    segments = bpy.context.active_object.data.bones.keys()
<<<<<<< HEAD
                  # todo copy physics:  physics_frames = [obj.name for obj in bpy.data.objects if obj.parent_bone in segments and obj.type == 'EMPTY']

                    for m in range(len(meshes)):    # select meshes
                        bpy.data.objects[meshes[m]].select = True
                    for s in range(len(segments)):  # select segments
                        bone = bpy.context.active_object.data.bones[segments[s]]
                        bone.select = True
                  #  for p in range(len(physics_frames)):   # select physics frames
                   #     bpy.data.objects[physics_frames[p]].select = True
                    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value": ((i * offset_o + offset_o / 2 - num_offspring * offset_o / 2), -offset_g * (g + 1), 0)})
                    bpy.data.scenes[0].update()
                    list_instances[g][i]=bpy.context.scene.objects.active.name
                    # bpy.ops.robotdesigner.createphysicsframes()  # todo: calculate new physics automatically after adaption


                    # bf rename segments not necessary
                    #   for b in range(len(bpy.context.active_object.data.bones)):
                  #      bpy.context.active_object.data.bones[b].name = bpy.context.active_object.data.bones[b].name+str(g)+str(i) #rename bones
                    #
                    #   bpy.context.active_object.data.name = bpy.context.active_object.name #rename armature as the object name
=======

                    for m in range(len(meshes)):
                        bpy.data.objects[meshes[m]].select = True
                    for s in range(len(segments)):
                        bone = bpy.context.active_object.data.bones[segments[s]]
                        bone.select = True
                    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value": ((i * offset_o + offset_o / 2 - num_offspring * offset_o / 2), -offset_g * (g + 1), 0)})
                    bpy.data.scenes[0].update()
                    list_instances[g][i]=bpy.context.scene.objects.active.name

                    for b in range(len(bpy.context.active_object.data.bones)):
                        bpy.context.active_object.data.bones[b].name = bpy.context.active_object.data.bones[b].name+str(g)+str(i) #rename bones

                        bpy.context.active_object.data.name = bpy.context.active_object.name #rename armature as the object name
>>>>>>> c729e77

                    bpy.ops.object.select_all(action='DESELECT')

            return list_instances


<<<<<<< HEAD

        def main():
            print("Starting Evolutionary Algorithm")
=======
        def main():
>>>>>>> c729e77
            RD=context.scene.RobotDesigner
            bone_sim = RD.model_to_simulate
            max_gen = RD.max_generation
            size_offspring = RD.offspring_size
            mutation_rate = RD.mutation_rate_real
            mutation_deviation = RD.mutation_deviation
            selection_rate = RD.selection_rate
            n_adapt = global_properties.num_adaptions.get(context.scene)
            adapt_rate = global_properties.adaption_rate.get(context.scene)
            current_scene = bpy.context.scene
            result = global_properties.visualresult.get(context.scene)
<<<<<<< HEAD
            offset_o = RD.offsetlateral
            offset_g = RD.offsetfront
=======
            offset_o=RD.offsetlateral
            offset_g=RD.offsetfront
>>>>>>> c729e77
            current_scene.RobotDesigner.display_mesh_selection = 'all'

            historial_individuals = []

<<<<<<< HEAD
            print('1')
            armature = selectrobot(bone_sim)
            meshes = meshes_initial_armature(armature)
            ini_position_verts = verts_co(armature, meshes)
            print('2')
            vert_parent_mesh, meshes_level_up, segment_ini_pos, mesh_pos_ini = minvertexbonedistance(armature, meshes)

            print(max_gen)
            for gen in range(max_gen):
                print('Run Generation ', gen)
=======
            armature = selectrobot(bone_sim)
            meshes = meshes_initial_armature(armature)
            ini_position_verts = verts_co(armature, meshes)
            vert_parent_mesh, meshes_level_up, segment_ini_pos, mesh_pos_ini = minvertexbonedistance(armature, meshes)

            for gen in range(max_gen):

>>>>>>> c729e77
                individuals_generation = individualsgen(gen, ini_position_verts, historial_individuals)
                fitness_generation = fitnessfunction(individuals_generation, ini_position_verts, meshes)
                selected_parents = selection(gen, individuals_generation, size_offspring, selection_rate, fitness_generation)
                crossed = crossover(selected_parents, meshes)
                offspring_generation = mutation(crossed, mutation_rate, mutation_deviation, meshes)
                historial_individuals = historialgen(offspring_generation, historial_individuals)

            if result == 'best':
                offspring_adapted = historial_individuals[max_gen-1]
                best_individual = best_ind(offspring_adapted, ini_position_verts, meshes)
                for i in range(n_adapt): #loop for adaptability steps
                    offspring_adapted = neighbours_adapt(offspring_adapted, armature, meshes, adapt_rate, best_individual)
                sendparametersbest(offspring_adapted, ini_position_verts, armature, meshes)

<<<<<<< HEAD
            elif result == 'all':
=======
            if result == 'all':
>>>>>>> c729e77
                list_instances = createrobotinstances(max_gen, size_offspring, armature, meshes, offset_o, offset_g)
                for g in range (len(historial_individuals)): #generations
                    offspring_adapted = historial_individuals[g]
                    for g_ind in range(len(historial_individuals[0])): #individuals of a generation
                        for i in range(n_adapt): #loop for adaptbility steps
                            offspring_adapted = neighbours_adapt(offspring_adapted, armature, meshes, adapt_rate, g_ind)
                        sendparametersgen(offspring_adapted, armature, list_instances, g, g_ind)

<<<<<<< HEAD

            armatures_population = armatures_scene()
            for ar in range(len(armatures_population)):
                # TODO place joint mesh and model
                #placejoints_mesh(armatures_population[ar], vert_parent_mesh, ini_position_verts)
                #placejoints_model(armatures_population[ar], vert_parent_mesh, meshes_level_up, segment_ini_pos, ini_position_verts, mesh_pos_ini)
                print('Generating new collision meshes')
                bpy.context.scene.objects.active = bpy.data.objects[armatures_population[ar]]
                bpy.ops.robotdesigner.copyallvistocol()

                print("Genearting new physics frames")
                for bone in bpy.data.objects[armatures_population[ar]].data.bones:  # bpy.context.active_object.data.bones:

                    bpy.ops.robotdesigner.createphysicsframe()

                    bpy.context.scene.RobotDesigner.segment_name = bone.name
                    bpy.data.objects[bone.name].RobotDesigner.dynamics.mass = 1.0

                    bpy.ops.robotdesigner.computephysicsframe(from_visual_geometry=False)
                    bpy.ops.robotdesigner.computemass(density=1.0, from_visual_geometry=False)

            #current_scene.RobotDesigner.display_mesh_selection = 'visual'

            print('--finished')

            return None

        try:
            main()
        except:
            pass

        return {'FINISHED'}
=======
            armatures_population = armatures_scene()
            for ar in range(len(armatures_population)):
                placejoints_mesh(armatures_population[ar], vert_parent_mesh, ini_position_verts)
                placejoints_model(armatures_population[ar], vert_parent_mesh, meshes_level_up, segment_ini_pos, ini_position_verts, mesh_pos_ini)

            current_scene.RobotDesigner.display_mesh_selection = 'visual'

            return None

        main()

        return {'FINISHED'}



>>>>>>> c729e77
