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

# ######
# Blender imports
import bpy
import mathutils
########
# RD imports
from ..osim import osim_dom  # xsd bindings
from ...core import config, PluginManager, RDOperator
from ...properties.globals import global_properties


def get_muscles(active_model_name):
  return list(filter(lambda obj: obj.RobotEditor.muscles.robotName == active_model_name, bpy.data.objects))


class OsimImporter(object):
  def __init__(self):
    self.doc = osim_dom.OpenSimDocument()
    self.doc.Version = "30000"
    self.doc.Model = pyxb.BIND(
      ForceSet=pyxb.BIND(
        objects=pyxb.BIND(
          Millard2012EquilibriumMuscle=[],
          Millard2012AccelerationMuscle=[],
          Thelen2003Muscle=[],
          RigidTendonMuscle=[]
        )
      )
    )
    self.muscle_type_to_pyxb_list = {
      'Millard2012EquilibriumMuscle' : self.doc.Model.ForceSet.objects.Millard2012EquilibriumMuscle,
      'Millard2012AccelerationMuscle': self.doc.Model.ForceSet.objects.Millard2012AccelerationMuscle,
      'Thelen2003Muscle' : self.doc.Model.ForceSet.objects.Thelen2003Muscle,
      'RigidTendonMuscle' : self.doc.Model.ForceSet.objects.RigidTendonMuscle,
    }


  def read_osim_file(self, filename):
    assert filename.endswith('.osim')
    with open(filename, "w") as f:
      output = self.doc.toDOM()
      output = output.toprettyxml()
      f.write(output)


  def create_new_muscle(name, ):