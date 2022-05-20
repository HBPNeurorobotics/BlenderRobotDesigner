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
# Copyright (c)
#
# Changes:
#
#   2016-01-15: Stefan Ulbrich (FZI) (FZI Forschungszentrum Informatik)
#       Template created
#   Today: Your Name
#       Please add ALWAYS your modifications
#
# ######

"""
Sphinx-autodoc tag
"""

# System imports
import os
from inspect import getmembers, isclass

# Blender imports
import bpy

# RobotDesigner imports
from ..core import config, PluginManager, RDOperator, logfile


@PluginManager.register_class
class GenerateAPI(RDOperator):
    """
    :ref:`operator` for ...

    **Preconditions:**

    **Postconditions:**
    """

    bl_idname = config.OPERATOR_PREFIX + "generate_api"
    bl_label = "Generate Python API"

    @RDOperator.OperatorLogger
    def execute(self, context):

        try:
            base_path = os.path.join(config.script_path, "resources/blender_api/bpy/")
            self.logger.info("Writing API stubs to: {}".format(base_path))

            for op_module_name in dir(bpy.ops):
                ops_dir = os.path.join(base_path, "ops")
                if not os.path.exists(ops_dir):
                    os.makedirs(ops_dir)
                self.logger.debug("Creating module: {}".format(ops_dir))

                with open(os.path.join(ops_dir, op_module_name + ".py"), "w") as f:
                    op_module = getattr(bpy.ops, op_module_name)
                    for op_submodule_name in dir(op_module):
                        op = getattr(op_module, op_submodule_name)
                        text = repr(op).split("\n")
                        if text[-1].startswith("bpy.ops."):
                            f.write(
                                'def {}:\n    """\n    {}\n    """\n    pass\n'.format(
                                    text[-1].replace(
                                        "bpy.ops.{}".format(op_module_name), ""
                                    ),
                                    text[0].replace("#", ""))
                                )

            types = [i for i in getmembers(bpy.types, isclass) if "." not in i[0]]

            with open(os.path.join(base_path, "types.py"), "w") as f:
                for bpy_type in types:
                    if bpy_type[0] != "Operator":
                        f.write("class {}(object):\n\tpass\n\n".format(bpy_type[0]))
                    else:
                        # Adding overridable methods removes inspection check warnings about unused variables
                        f.write(
                            "class {}(object):"
                            "\n\t@classmethod"
                            "\n\tdef poll(cls,context): pass"
                            "\n\tdef invoke(self, context, event): pass"
                            "\n\tdef execute(self,context): pass \n\n".format(bpy_type[0])
                        )

            # Data is just a class with classes

            # Context

            with open(os.path.join(base_path, "__init__.py"), "w") as f:
                f.write("from . import ops, types, props\n\n")
                f.write("class context(object):")

                for member in [
                    i[0] for i in getmembers(bpy.context) if "__" not in i[0]
                ]:
                    f.write("\n    {} = None".format( member))
                f.write("\n\n")

                f.write("class data(object):")
                for member in [i[0] for i in getmembers(bpy.data) if "__" not in i[0]]:
                    f.write("\n    {} = None".format(member))
                f.write("\n\n")

            # utils are several modules

            # Properties are in one module
            with open(base_path + "props.py", "w") as f:
                f.write("import sys\n\n")

                for prop in [
                    getattr(bpy.props, i[0])
                    for i in getmembers(bpy.props)
                    if "Property" in i[0]
                ]:
                    text = prop.__doc__.split("\n")
                    signature = text[0].replace(".. function:: ", "")
                    docstring = "\n".join(text[1:])
                    f.write(
                        'def {}:\n   """{}\n   """\n   pass\n\n'.format(
                        signature, docstring)
                    )

            return {"FINISHED"}

        except:
            print(logfile.log_callstack())
