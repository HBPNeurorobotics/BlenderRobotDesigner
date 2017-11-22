# #####
# This file is part of the RobotDesigner of the Neurorobotics subproject (SP10)
# in the Human Brain Project (HBP).
# It has been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
# developed at the Technical University of Munich at the chair of embedded and robotic system.
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


import pyxb
import os.path
from pathlib import Path
import logging

# ######
# Blender imports
import bpy
from mathutils import Matrix
########
# RD imports
from ..osim import osim_dom  # xsd bindings
from ...core import config, PluginManager, RDOperator
from ...properties.globals import global_properties

from ...operators.muscles import CreateNewMuscle, CreateNewPathpoint

#logger = logging.getLogger('SDF')
#logger.setLevel(logging.DEBUG)


__author__ = 'Benedikt Feldotto(TUM)'


class OsimImporter(object):

  def __init__(self, file_path, musclepath):
        # initialize logger and operator
        operator = RDOperator
        self.logger = operator.logger
        self.operator = operator
        self.controllers = None

        # create dom object from .osim file
        base_dir = os.path.dirname(file_path)
        self.logger.debug(base_dir)
        self.logger.debug(musclepath)
        print("mpath")
        print(musclepath)
        muscles_osim = open(base_dir + '/' + '/'.join(musclepath.split('/', 3)[3:])[:-2]).read()
        self.muscles = osim_dom.CreateFromDocument(muscles_osim)


  def import_muscles(self, muscle, type):
      """
        import a single muscle from the osim file
        :param muscle: .osim pyxb muscle instance
        :return: type: string for muscle type
      """
      CreateNewMuscle.run(muscle.name)
      RDmuscle = bpy.data.objects[muscle.name]

      RDmuscle.RobotEditor.muscles.muscleType = type
      RDmuscle.RobotEditor.muscles.length = muscle.optimal_fiber_length / 0.9
      RDmuscle.RobotEditor.muscles.max_isometric_force = muscle.max_isometric_force

      global_properties.active_muscle.set(bpy.context.scene, muscle.name)

      self.import_pathpoints(muscle, RDmuscle)


  def import_pathpoints(self, muscle, RDmuscle):
      """
          import muscle pathpoints from the osim file
      :param muscle: .osim pyxb muscle instance
      :return: RDmuscle: Robot Designer muscle instance
      """
      p = 0
      while(True):
        try:
            # current pathpoint
            pathpoint = muscle.GeometryPath.PathPointSet.objects.PathPoint[p]

            # get pathpoint parent world pose
            model = bpy.data.objects[global_properties.model_name.get(bpy.context.scene)]
            pose_bone = model.pose.bones[pathpoint.body]
            segment_world = model.matrix_world * pose_bone.matrix

            # calculate pathpoint world pose
            location_local = [float(x) for x in pathpoint.location.split()]
            location_global = segment_world * Matrix.Translation((location_local[0],location_local[1],location_local[2],1))

            # create new pathpoint and set parameters of RD pathpoint object
            CreateNewPathpoint.run()
            location_global = location_global.to_translation()
            RDmuscle.data.splines[0].points[p].co = (location_global[0],location_global[1],location_global[2], 1)

            #
            #  hook pathpoints to segments
            RDmuscle.RobotEditor.muscles.pathPoints[p].coordFrame = pathpoint.body
            #global_properties.model_name.set(bpy.context.scene, 'robot-hookmesh')
            #global_properties.active_muscle.set(bpy.context.scene, 'm1')
            bpy.ops.roboteditor.select_segment_muscle(segment_name=pathpoint.body, pathpoint_nr=p+1)



            p += 1

        except:
            break


  def import_osim(self):
    """
    Imports all listed muscles in .osim file
    """
    # import Thelen2003 Muscles
    m = 0
    while(True):
        try:
            muscle = self.muscles.Model.ForceSet.objects.Thelen2003Muscle[m]
            type = 'THELEN'
            self.import_muscles(muscle, type)
            m += 1
        except:
            break

    # import Millard2012 Equilibrium Muscles
    m = 0
    while(True):
        try:
            muscle = self.muscles.Model.ForceSet.objects.Millard2012EquilibriumMuscle[m]
            type = 'MILLARD_EQUIL'
            self.import_muscles(muscle, type)
            m += 1
        except:
            break

    # import Millard2012 Acceleration Muscles
    m = 0
    while (True):
        try:
            muscle = self.muscles.Model.ForceSet.objects.Millard2012AccelerationMuscle[m]
            type = 'MILLARD_ACCEL'
            self.import_muscles(muscle, type)
            m += 1
        except:
            break

    # import Rigid Tendon Muscles
    m = 0
    while (True):
        try:
            muscle = self.muscles.Model.ForceSet.objects.RigidTendonMuscle[m]
            type = 'RIGID_TENDON'
            self.import_muscles(muscle, type)
            m += 1
        except:
            break










