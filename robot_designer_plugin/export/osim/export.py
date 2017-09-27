import pyxb
import os.path
from pathlib import Path

# ######
# Blender imports
import bpy

########
# RD imports
from ..osim import osim_dom  # xsd bindings
from ...core import config, PluginManager, RDOperator
from ...properties.globals import global_properties


class OsimExporter(object):
  def __init__(self):
    self.doc = osim_dom.OpenSimDocument()
    self.doc.Version = "20303"
    self.doc.Model = pyxb.BIND(
      ForceSet=pyxb.BIND(
        objects=pyxb.BIND(
          Millard2012EquilibriumMuscle=[],
          Millard2012AccelerationMuscle=[]
        )
      )
    )
    self.muscle_type_to_pyxb_list = {
      'Millard2012EquilibriumMuscle' : self.doc.Model.ForceSet.objects.Millard2012EquilibriumMuscle,
      'Millard2012AccelerationMuscle': self.doc.Model.ForceSet.objects.Millard2012AccelerationMuscle
    }


  def write_osim_file(self, filename):
    assert filename.endswith('.osim')
    with open(filename, "w") as f:
      output = self.doc.toDOM()
      output = output.toprettyxml()
      f.write(output)


  def add_all_muscles(self, data, context):
    active_model = global_properties.model_name.get(context.scene)
    muscles = list(filter(lambda obj: obj.RobotEditor.muscles.robotName == active_model, data.objects))
    print ("Exporting Muscles:", muscles)
    for m in muscles:
      self._add_blender_muscle(m)


  def _add_blender_muscle(self, m):
    m = osim_dom.Millard2012EquilibriumMuscle(
      name = m.name,
      GeometryPath=osim_dom.GeometryPath(
        PathPointSet = pyxb.BIND(
          objects = pyxb.BIND(
            PathPoint = self._build_pyxb_path_nodes_list(m)
          )
        )
      ),
      # TODO: Fix hardcoded values
      max_isometric_force = 1000.,
      optimal_fiber_length = 0.01,
      tendon_slack_length = 0.01
    )
    self._add_pyxb_muscle(m)


  def _build_pyxb_path_nodes_list(self, m):
    def transform_to_pyxb(nd):
      name, parent, (x, y ,z) = nd
      return osim_dom.PathPoint(
        location = osim_dom.vector3("%f %f %f" % (x, y, z)),
        body = parent,
        name = name
      )
    return list(map(transform_to_pyxb, self._get_intermediate_repr_path_nodes(m)))


  def _get_intermediate_repr_path_nodes(self, m):
    def transform_vertex(arg):
      i, pt = arg
      name = '%s_node%i' % (m.name, i)
      parent = 'world' # TODO: fix
      x, y, z, _ = pt.co
      return (name, parent, (x, y, z))
    return map(transform_vertex, enumerate(m.data.splines[0].points))


  def _add_pyxb_muscle(self, m):
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
  pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(None)

  exporter = OsimExporter()

  exporter.add_all_muscles(bpy.data, context)

  exporter.write_osim_file(
    os.path.join(toplevel_directory, "muscles.osim"))