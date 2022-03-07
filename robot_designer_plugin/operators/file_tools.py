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

# System imports
import os
import glob
import copy

# Blender imports
import bpy

# RobotDesigner imports
from ..core import config, PluginManager, RDOperator
from .dae_sdf_converter import dae_sdf_converter
from ..core.logfile import operator_logger
from bpy.props import StringProperty, BoolProperty, IntProperty, FloatProperty


@PluginManager.register_class
class ConvertDAEPackages(RDOperator):
    """
    :ref:`operator` for converting the .dae files in a folder to SDF packages.
    **Preconditions:**
    **Postconditions:**
    """

    bl_idname = config.OPERATOR_PREFIX + "convertdaepackages"
    bl_label = "Convert All '.dae' Files in a Folder to SDF Packages"

    # need to set a path so so we can get the file name and path
    filepath: StringProperty(subtype="FILE_PATH")
    filename: StringProperty(subtype="FILE_NAME")
    directory: StringProperty(subtype="DIR_PATH")

    sdf_mesh_scale: IntProperty(
        name="SDF Mesh Scale",
        description="Scale of the meshes defined in the SDF",
        default=1,
    )

    dae_mesh_dim_max: FloatProperty(
        name="DAE dim min",
        description="Min scale of the meshes modifying the .dae in meters",
        default=1.0,
    )
    dae_mesh_dim_min: FloatProperty(
        name="DAE dim max",
        description="Max cale of the meshes modifying the .dae in meters",
        default=1.0,
    )

    rotate_x: FloatProperty(
        name="Rotate X",
        description="Rotate all meshes by the given degrees",
        default=0.0,
    )

    rotate_y: FloatProperty(
        name="Rotate Y",
        description="Rotate all meshes by the given degrees",
        default=0.0,
    )

    rotate_z: FloatProperty(
        name="Rotate Z",
        description="Rotate all meshes by the given degrees",
        default=0.0,
    )

    translate_x: FloatProperty(
        name="Translate X",
        description="Move all meshes by given x translation",
        default=0.0,
    )

    translate_y: FloatProperty(
        name="Translate Y",
        description="Move all meshes by given y translation",
        default=0.0,
    )

    translate_z: FloatProperty(
        name="Translate Z",
        description="Move all meshes by given z translation",
        default=0.0,
    )

    lift_up: BoolProperty(
        name="Lift Model above ground",
        description="Moves the mesh above the ground for simulation",
        default=True,
    )

    sdf_author_name: StringProperty(
        name="Author Name",
        description="The name of the model author",
        default="Benedikt Feldotto",
    )

    sdf_author_mail: StringProperty(
        name="Author EMail",
        description="Email adress of the model author",
        default="feldotto@in.tum.de",
    )

    sdf_description: StringProperty(
        name="Model Description",
        description="A short description of the model",
        default="Export3D Model from https://de.3dexport.com/.",
    )




    @classmethod
    def poll(cls, context):
        return True

    @RDOperator.OperatorLogger
    def execute(self, context):
        # print(self.filepath)
        dae_sdf_converter(self.directory, self.sdf_mesh_scale,
                          self.dae_mesh_dim_min, self.dae_mesh_dim_max,
                          self.rotate_x, self.rotate_y, self.rotate_z,
                          self.translate_x, self.translate_y, self.translate_z,
                          self.lift_up,
                          self.sdf_author_name, self.sdf_author_mail, self.sdf_description
                          )
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


@PluginManager.register_class
class FileToDaeConverter(RDOperator):
    """
    :ref:`operator` for converting all .obj files in a folder to .dae files.
    **Preconditions:**
    **Postconditions:**
    """

    bl_idname = config.OPERATOR_PREFIX + "convert_files_to_dae"
    bl_label = "Convert All Files of selected type in a Folder to '.dae' Files"

    directory: StringProperty(subtype="DIR_PATH")

    obj_files: BoolProperty(
        name="Convert .obj files",
        description="Searches for all .obj file in directory and subdirectories and converts them to .dae files",
        default=True,
    )

    stl_files: BoolProperty(
        name="Convert .stl files",
        description="Searches for all .stl file in directory and subdirectories and converts them to .dae files",
        default=True,
    )

    fdx_files: BoolProperty(
        name="Convert .fdx files",
        description="Searches for all .fdx file in directory and subdirectories and converts them to .dae files",
        default=True,
    )

    xthreed: BoolProperty(
        name="Convert .x3d files",
        description="Searches for all .x3d file in directory and subdirectories and converts them to .dae files",
        default=True,
    )

    separate_folders: BoolProperty(
        name="Export in separate folders",
        description="Creates a separate folder for the different file types",
        default=True,
    )

    join_meshes: BoolProperty(
        name="Joint mutliple meshes",
        description="Joins multiple meshes to a single mesh file",
        default=True,
    )

    decimate_models: BoolProperty(
        name="Decimate models if vertices above threshold",
        description="Decimates all models that have a vertex count above the given threshold",
        default=True,
    )

    decimate_vertex_threshold: IntProperty(
        name="Decimate threshold",
        description="Decimates all models that have a vertex count above the given threshold",
        default=50000,
    )

    @classmethod
    def poll(cls, context):
        return True

    @RDOperator.OperatorLogger
    def execute(self, context):
        operator_logger.info("Files input folder is: {}".format(self.directory))

        # Analyze file types to process
        file_type_dict = {'obj': self.obj_files,
                          'stl': self.stl_files,
                          'fdx': self.fdx_files,
                          'x3d': self.xthreed}
        file_types = [file_type for file_type, value in file_type_dict.items() if file_type_dict[file_type]]

        output_dir = copy.deepcopy(os.path.join(self.directory, "output_dae_files"))
        if self.separate_folders:
            # output sorted by file type
            for file_type in file_types:
                os.mkdir(output_dir + "_from_" + file_type)
        else:
            # all output files in the same folder
            os.mkdir(output_dir)

        for file_type in file_types:
            # process file type
            files = glob.glob(self.directory + "/**/*." + file_type, recursive=True)
            operator_logger.info("Found these {} .{} files: {}".format(len(files), file_type, files))

            for file in files:
                # import file, export .dae file, delete mesh in blender
                operator_logger.info("Converting file: {}".format(file))

                # import file
                if file_type == 'obj':
                    bpy.ops.import_scene.obj(filepath=os.path.join(self.directory, file))
                elif file_type == 'stl':
                    bpy.ops.import_mesh.stl(filepath=os.path.join(self.directory, file))
                elif file_type == 'fdx':
                    bpy.ops.import_scene.fbx(filepath=os.path.join(self.directory, file))
                elif file_type == '3ds':
                    bpy.ops.import_scene.autodesk_3ds(filepath=os.path.join(self.directory, file))

                # Deselect all
                bpy.ops.object.select_all(action='DESELECT')

                if self.join_meshes:
                    # join all objects to one mesh
                    # Mesh objects
                    MSH_OBJS = [m for m in bpy.context.scene.objects if m.type == 'MESH']

                    for OBJS in MSH_OBJS:
                        # Select all mesh objects
                        OBJS.select_set(state=True)

                        # Makes one active
                        bpy.context.view_layer.objects.active = OBJS
                    bpy.ops.object.join()
                else:
                    bpy.context.selected_objects[0].select_set(state=True)

                ob = bpy.context.selected_objects[0]
                ob_data = ob.data
                vertices = len(ob_data.vertices)
                edges = len(ob_data.edges)
                polygons = len(ob_data.polygons)  # faces
                operator_logger.info("File has {} vertices {} edges {} polygons".format(vertices, edges, polygons))

                if self.decimate_models:
                    # decimate large meshes
                    if(vertices > self.decimate_vertex_threshold):
                        ratio = self.decimate_vertex_threshold / vertices
                        operator_logger.info("Decimating mesh with ratio {}".format(ratio))
                        ob.modifiers.new("Decimate", "DECIMATE")
                        ob.modifiers["Decimate"].ratio = ratio


                # export models
                if self.separate_folders:
                    export_dir = output_dir + '_from_' + file_type
                else:
                    export_dir = output_dir

                bpy.ops.wm.collada_export(
                    filepath=os.path.join(export_dir, os.path.basename(file.replace(".obj", ".dae")
                                                                       .replace(".fdx", ".dae")
                                                                       .replace(".stl", ".dae"))),
                    apply_modifiers=True,
                    selected=True,
                    use_texture_copies=True)

                # delete objects after export
                bpy.ops.object.delete()

        operator_logger.info("\33[33m === Done converting files ===\033[0m")

        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}

@PluginManager.register_class
class PrintTransformations(RDOperator):
    """
    :ref:`operator` for print transformation matrix from active object to all selected objects.

    **Preconditions:**

    **Postconditions:**
    """

    bl_idname = config.OPERATOR_PREFIX + "printtransformations"
    bl_label = "Print Transformation Matrix from Active Object to All Selected Objects"

    @classmethod
    def poll(cls, context):
        return True

    @RDOperator.OperatorLogger
    def execute(self, context):
        active_object = bpy.context.active_object

        for ob in [obj for obj in context.scene.objects if obj.select_get()]:
            operator_logger.info(
                "Transformation from {} to {}".format(
                    {"from": active_object.name, "to": ob.name})
            )
            transform = active_object.matrix_world.inverted() @ ob.matrix_world
            operator_logger.info(transform)

        return {"FINISHED"}
