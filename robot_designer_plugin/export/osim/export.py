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
  """
  Return objects that represent muscles. And only those associated with the given model.

  :param active_model_name: The name of the robot for which to find associated muscles.
  :return: A list of associated objects that represent muscles.
  """
  return list(filter(lambda obj: obj.RobotEditor.muscles.robotName == active_model_name, bpy.data.objects))


class OsimExporter(object):
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


  def write_osim_file(self, filename):
    assert filename.endswith('.osim')
    with open(filename, "w") as f:
      output = self.doc.toDOM()
      output = output.toprettyxml()
      f.write(output)


  def add_muscles(self, context, muscles):
    print ("Exporting Muscles:", muscles)
    for m in muscles:
      self._add_blender_muscle(m, context)


  def _select_pyxb_muscle_class(self, obj):
    muscle_type_to_pyxb_type = {
      'MILLARD' : osim_dom.Millard2012EquilibriumMuscle,
      'THELEN'  : osim_dom.Thelen2003Muscle,
    }
    return muscle_type_to_pyxb_type[
           str(obj.RobotEditor.muscles.muscleType)]


  def _add_blender_muscle(self, m, context):
    try:
      pyxb_class = self._select_pyxb_muscle_class(m)
    except KeyError as e:
      print ("Warning: Not exporting object as muscle because: \n%s: %s" % (type(e).__name__, str(e)))
      return
    # calc muscle length
    bpy.ops.roboteditor.calc_muscle_length(muscle=m.name)

    m = pyxb_class(
      name = m.name,
      GeometryPath=osim_dom.GeometryPath(
        PathPointSet = pyxb.BIND(
          objects = pyxb.BIND(
            PathPoint = self._build_pyxb_path_nodes_list(m, context)
          )
        )
      ),
      # TODO: Fix hardcoded values
      max_isometric_force = m.RobotEditor.muscles.max_isometric_force,
      optimal_fiber_length = m.RobotEditor.muscles.length * 0.9,
      tendon_slack_length = m.RobotEditor.muscles.length * 0.1
    )
    self._add_pyxb_muscle(m, context)


  def _build_pyxb_path_nodes_list(self, m, context):
    def transform_to_pyxb(nd):
      name, parent, (x, y ,z) = nd
      return osim_dom.PathPoint(
        location = osim_dom.vector3("%f %f %f" % (x, y, z)),
        body = parent,
        name = name
      )
    return list(map(transform_to_pyxb, self._get_intermediate_repr_path_nodes(m, context)))


  def _get_intermediate_repr_path_nodes(self, m, context):
    def transform_vertex(arg):
      i, pt = arg
      name = '%s_node%i' % (m.name, i)
      parent = m.RobotEditor.muscles.pathPoints[i].coordFrame
      x, y, z, _ = pt.co
      active_model = global_properties.model_name.get(context.scene)
      pose_bone = bpy.data.objects[active_model].pose.bones[parent]
      pose = pose_bone.matrix.inverted() * bpy.data.objects[active_model].matrix_world.inverted() * \
             bpy.data.objects[m.name].matrix_world
      vec = mathutils.Vector((x,y,z,1))
      trans = mathutils.Matrix.Translation(vec)
      pose_rel = pose * trans
      return (name, parent, (pose_rel[0][3], pose_rel[1][3], pose_rel[2][3]))
    return map(transform_vertex, enumerate(m.data.splines[0].points))


  def _add_pyxb_muscle(self, m, context):
    self.muscle_type_to_pyxb_list[type(m).__name__].append(m)



def create_osim(operator: RDOperator, context,
                filepath: str, meshpath: str, toplevel_directory: str, in_ros_package: bool, abs_filepaths=False):
  """
  Creates the .osim muscle definition file

  :param operator: The calling operator
  :param context: The current context
  #   :param filepath: path to the SDF file
  #   :param meshpath: Path to the mesh directory
  :param toplevel_directory: The directory in which to export
  :param in_ros_package: Whether to export into a ros package or plain files
  :param abs_filepaths: If not intstalled into a ros package decides whether to use absolute file paths.
  :return:
  """
  # Might be set at another place. Therefore need to clear it.

  muscles = get_muscles(context.active_object.name)
  if muscles:
    pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(None)
    exporter = OsimExporter()
    exporter.add_muscles(context, muscles)
    exporter.write_osim_file(
      os.path.join(toplevel_directory, "muscles.osim"))