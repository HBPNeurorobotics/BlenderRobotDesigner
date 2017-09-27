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


  doc = osim_dom.OpenSimDocument()
  doc.Model = pyxb.BIND(
    ForceSet=pyxb.BIND(
      objects=pyxb.BIND(
        Millard2012EquilibriumMuscle=[],
        Millard2012AccelerationMuscle=[]
      )
    )
  )

  with open(os.path.join(toplevel_directory, "muscles.osim"), "w") as f:
    output = doc.toDOM()
    output = output.toprettyxml()
    f.write(output)