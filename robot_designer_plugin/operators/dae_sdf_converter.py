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

# #!/usr/bin/python


# System imports
import os
import shutil
import numpy as np
import glob
from mathutils import Vector
import math

# Blender imports
import bpy

# Robot Designer imports
from ..core.logfile import operator_logger

output_folder = "output_sdf_models"
mesh_folder = "/home/hbp/Downloads/models/COLLADA"  # todo adapt paths


def create_sdf_folder(output_dir, sdf_name):
    """
    Create the folder structure which satisfied SDF specification.

    @param sdf_name : the name of the sdf package
    @param output_dir : the model output directory
    """
    operator_logger.info("Creating sdf folder in output dir: {}, sdf_name: {}".format(output_dir, sdf_name))

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
        operator_logger.info("Output folder does not exist. Create it now.")

    # create the sdf_name folder
    sdf_folder = os.path.join(output_dir, sdf_name)
    if not os.path.isdir(sdf_folder):
        os.mkdir(sdf_folder)

    # create the sdf_name/mesh folder
    f = "{}/{}/mesh".format(output_dir, sdf_name)
    if not os.path.isdir(f):
        os.mkdir(f)


def delete_sdf_folder(sdf_name):
    """
    Delete the specific folder in [output_folder] with name [sdf_name].

    @param sdf_name : the name of the sdf package
    """
    f = "{}%{}".format(output_folder, sdf_name)
    if os.path.isdir(f):
        shutil.rmtree(f)


def check_output_exist(sdf_name):
    """
    Check if an SDF package in [output_folder] with name [sdf_name] has already been created.

    @param sdf_name : the name of the sdf package

    @return:
        Bool: True  - the same package has been created
              False - no package with the same name has been created
    """

    output_folder_path = "{}/{}".format(output_dir, sdf_name)
    sdf_path = "{}/model.sdf".format(output_folder_path)
    config_path = "{}/model.config".format(output_folder_path)
    mesh_path = "{}/mesh".format(output_folder_path)
    dae_path = "{}/{}.dae".format(mesh_path, sdf_name)
    if os.path.exists(output_folder_path):
        if os.path.exists(sdf_path) and os.path.exists(config_path):
            if os.path.exists(mesh_path):
                if os.path.exists(dae_path):
                    return True
    return False


def create_config_file(
    sdf_name, sdf_author_name="", sdf_author_email="", sdf_description=""
):
    """
    Create a config file with specific information.

    @param sdf_name      : the name of the sdf package
    @param sdf_author_name   : the name of the author
    @param sdf_author_email  : the email of the author
    @param sdf_description   : the description of the package

    @return
        String: content of the config file
    """
    description = sdf_description + " Model converted from mesh file {}.".format(sdf_name)
    config_content = """<?xml version="1.0"?>
<model>
    <name>{}</name>
    <sdf version="1.6">model.sdf</sdf>
    <author>
        <name>{}</name>
        <email>{}</email>
    </author>
    <description>{}</description>
</model>
""".format(
        sdf_name,
        sdf_author_name,
        sdf_author_email,
        description,
    )
    return config_content


def create_sdf_file(sdf_name, sdf_mass=1, sdf_inertia=[1, 0, 0, 1, 0, 1], sdf_mesh_scale=1):
    """
    Create an sdf file based on the imported .dae file.

    @param sdf_name    : the name of the sdf package
    @param sdf_mass    : the mass of the imported object
    @param sdf_inertia : the inertia of the imported object

    @return String: content of the sdf file
    """
    sdf_content = """<?xml version="1.0"?>
<sdf version="1.6">
    <model name='{name}'>
        <pose>0 0 0 0 0 0</pose>
        <static>0</static>
        <link name='body'>
            <inertial>
                <mass>{mass}</mass>
                <pose>0 0 0 0 0 0</pose>
                <inertia>
                    <ixx>{inertia[0]}</ixx>
                    <ixy>{inertia[1]}</ixy>
                    <ixz>{inertia[2]}</ixz>
                    <iyy>{inertia[3]}</iyy>
                    <iyz>{inertia[4]}</iyz>
                    <izz>{inertia[5]}</izz>
                </inertia>
            </inertial>
            <collision name="{name}-coll">
                <pose>0 0 0 0 0 0</pose>
                <geometry>
                    <mesh>
                        <uri>model://{name}/mesh/{name}-coll.dae</uri>
                        <scale>{sdf_mesh_scale} {sdf_mesh_scale} {sdf_mesh_scale}</scale>
                    </mesh>
                </geometry>
            </collision>
            <visual name='{name}'>
                <pose>0 0 0 0 0 0</pose>
                <geometry>
                    <mesh>
                        <uri>model://{name}/mesh/{name}.dae</uri>
                        <scale>{sdf_mesh_scale} {sdf_mesh_scale} {sdf_mesh_scale}</scale>
                    </mesh>
                </geometry>
            </visual>
            <velocity_decay>
                <linear>0.01</linear>
                <angular>0.01</angular>
            </velocity_decay>
            <self_collide>0</self_collide>
            <kinematic>0</kinematic>
            <gravity>1</gravity>
        </link>
    </model>
</sdf>
""".format(
        name=sdf_name, mass=sdf_mass, inertia=sdf_inertia, sdf_mesh_scale=sdf_mesh_scale
    )
    return sdf_content


def clear_scene(keep_obj=False):
    """
    Delete all the objects in the scene

    @param keep_obj : if True, then the Mesh in the scene will be kept;
                     if False, nothing will remain in the scene
    """
    # delete all the objects in the scene
    # https://blenderscripting.blogspot.com/2012/03/deleting-objects-from-scene.html
    # bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_by_type(type="LIGHT")
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.select_by_type(type="CAMERA")
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.select_by_type(type="EMPTY")
    bpy.ops.object.delete(use_global=False)

    if not keep_obj:
        bpy.ops.object.select_by_type(type="MESH")
        bpy.ops.object.delete(use_global=False)
        for item in bpy.data.meshes:
            bpy.data.meshes.remove(item)


def obj_get_dimensions(obj):
    """
    Get the dimensions of the object

    @param obj : the Mesh to be measured

    @return Tuple (x, y, z): the 3d size (x, y, z) of the object
    """
    x, y, z = obj.dimensions.x, obj.dimensions.y, obj.dimensions.z
    operator_logger.debug("The orginal size of the obj: {:.4f}, {:.4f}, {:.4f}".format((x, y, z)))
    if bpy.context.scene.unit_settings.system == "IMPERIAL":
        # convert to the SI
        # 1 feet = 0.3048 meter
        x, y, z = x * 0.3048, y * 0.3048, z * 0.3048
    operator_logger.debug("The converted size of the obj: {:.4f}, {:.4f}, {:.4f}".format((x, y, z)))
    return x, y, z


def obj_check(obj):
    """
    Check if the object is too thin (maybe the object is a planar)

    @param obj : the Mesh to be checked
    """
    # check if the object is a planar
    x, y, z = obj_get_dimensions(obj)

    min_d = np.min([x, y, z])
    if min_d < 0.001:  # the object is too thin
        operator_logger.error("Invalid size: {:.4f}, {:.4f}, {:.4f}".format((x, y, z)))
        raise Exception("Invalid size!")


def obj_scale(obj, dae_mesh_dim_min, dae_mesh_dim_max):
    """
    Scale the object to be fitted for the gripper

    @param obj : the Mesh to be re-scaled
    @param dae_mesh_dim_min : Min dimension of the .dae mesh files
    @param dae_mesh_dim_max : Max dimension of the .dae mesh files
    """
    x, y, z = obj_get_dimensions(obj)

    # scale the object (to min ~ max in meters)
    MAX_D = dae_mesh_dim_min
    MIN_D = dae_mesh_dim_max

    l = np.sort([x, y, z])
    if l[1] < MIN_D:
        factor = MIN_D / l[1]
    elif l[1] <= MAX_D:
        factor = 1.0
    else:  # l[1] > MAX_D
        factor = MAX_D / l[1]
    operator_logger.debug("The scale factor of the obj: {:.4f}".format(factor))
    # Set the obj as current active object
    obj.select_set(True)
    bpy.ops.transform.resize(value=(factor, factor, factor))
    # Change the origin of the object
    obj.select_set(True)
    # https://docs.blender.org/api/blender_python_api_current/bpy.ops.object.html#bpy.ops.object.origin_set
    bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN", center="BOUNDS")



def obj_remesh(obj):
    """
    Do remesh operation to the Mesh so as to simplify the Mesh. This operation
        could greatly slow down the conversion speed.

    @param obj : the Mesh to be remeshed
    """
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_add(type="REMESH")
    obj.modifiers["Remesh"].mode = "BLOCKS"
    obj.modifiers["Remesh"].octree_depth = 6
    obj.modifiers["Remesh"].scale = 0.99
    obj.modifiers["Remesh"].use_remove_disconnected = True
    obj.modifiers["Remesh"].threshold = 1.0
    bpy.ops.object.modifier_apply(apply_as="DATA")


def obj_merge():
    """
    Merge all the Mesh in the current scene as one Mesh.
    """
    scene = bpy.context.scene
    obs = []
    for ob in scene.objects:
        # whatever objects you want to join...
        if ob.type == "MESH":
            obs.append(ob)
    ctx = bpy.context.copy()

    # one of the objects to join
    ctx["active_object"] = obs[0]
    ctx["selected_objects"] = obs
    # we need the scene bases as well for joining
    ctx["selected_editable_objects"] = obs
    bpy.ops.object.join(ctx)


def obj_calc_inertia(obj, density=1000):
    """
    Calculate the inertia for the object, based on the
        approximate volume and the given density.

    @param obj     : the object to calculate
    @param density : the density of the object, unit: kg/m^3

    @return Tuple (mass, inertia):
    @return Float mass   - the mass of the object
    @return List inertia - the inertia of the object
    """
    # first we calcuate the volume of the object
    def calc_volume(obj):
        """
        Treat the object as cuboid and calculate the volumne
        """
        x, y, z = obj.dimensions.x, obj.dimensions.y, obj.dimensions.z
        volume = x * y * z
        operator_logger.debug(volume)
        return volume

    def calc_volume1(obj):
        """
        Calculate the volume based on the triangle meshes of the object
        """
        volume = 0
        ob = obj
        ob_mat = ob.matrix_world
        me = ob.data
        me.calc_tessface()
        for tf in me.tessfaces:
            tfv = tf.vertices
            if len(tf.vertices) == 3:
                tf_tris = (
                    (me.vertices[tfv[0]], me.vertices[tfv[1]], me.vertices[tfv[2]]),
                )
            else:
                tf_tris = (
                    me.vertices[tfv[0]],
                    me.vertices[tfv[1]],
                    me.vertices[tfv[2]],
                ), (me.vertices[tfv[2]], me.vertices[tfv[3]], me.vertices[tfv[0]])
            for tf_iter in tf_tris:
                v1 = ob_mat * tf_iter[0].co
                v2 = ob_mat * tf_iter[1].co
                v3 = ob_mat * tf_iter[2].co
                volume += v1.dot(v2.cross(v3)) / 6.0
        if volume < 0:
            volume = -volume
        return volume

    def calc_inertia(x, y, z, mass):
        """
        Treat the object as cuboid and calculate the inertia.
        Source: https://en.wikipedia.org/wiki/List_of_moments_of_inertia
        """
        ixx = 1.0 / 12 * mass * (y * y + z * z)
        iyy = 1.0 / 12 * mass * (x * x + z * z)
        izz = 1.0 / 12 * mass * (x * x + y * y)
        return [ixx, 0, 0, iyy, 0, izz]

    volume = calc_volume(obj)
    # we treat the material of the objects as plastic and get
    # the mass of the object:
    mass = volume * density
    # then we treat the object as cuboid to calculate the inertia
    x, y, z = obj.dimensions.x, obj.dimensions.y, obj.dimensions.z

    return mass, calc_inertia(x, y, z, mass)


def calc_inertial(file,
                  dae_mesh_dim_min, dae_mesh_dim_max,
                  rotate_x, rotate_y, rotate_z,
                  translate_x, translate_y, translate_z,
                  lift_up
                  ):
    """
    Calculate the inertial information for the imported .dae file.

    @param file : the .dae file to be imported
    @param dae_mesh_dim_min : Min dimension of the .dae mesh files
    @param dae_mesh_dim_max : Max dimension of the .dae mesh files

    @param rotate_x : Rotate all meshes in x by degrees
    @param rotate_y : Rotate all meshes in Y by degrees
    @param rotate_z : Rotate all meshes in z by degrees
    @param translate_x : Translate all meshes in x
    @param translate_y : Translate all meshes in Y
    @param translate_z : Translate all meshes in z
    @param lift_up : Lift the model to ground

    @return Tuple (mass, inertia):
            Float mass   - the mass of the object
            List inertia - the inertia of the object
    """
    # remove all the unnecessary objects in the scene of blender
    clear_scene()
    # set to the SI
    bpy.context.scene.unit_settings.system = "METRIC"
    # import the dae file
    try:
        bpy.ops.wm.collada_import(filepath=file, import_units=False)
    except:
        operator_logger.error(
        "An error occurred during importing the collada file: {}".format(file)
    )

    # keep only the object in the scene
    clear_scene(keep_obj=True)
    # combine all parts of the object - is done
    operator_logger.info("Combining the meshes...")
    obj_merge()
    # scale the object so that it can be graspable -- Is done in SDF now
    operator_logger.info("Scaling the meshes...")
    obj = bpy.data.objects[0]
    obj_scale(obj, dae_mesh_dim_min, dae_mesh_dim_max)

    # Rotate the mesh
    obj.rotation_euler[0] = obj.rotation_euler[0] + rotate_x * math.pi/180
    obj.rotation_euler[1] = obj.rotation_euler[1] + rotate_y * math.pi/180
    obj.rotation_euler[2] = obj.rotation_euler[2] + rotate_z * math.pi/180

    # Translate the mesh
    obj.location = obj.location + Vector((translate_x, translate_y, translate_z))

    # lift model above ground
    if lift_up:
        move_object_to_ground(obj)

    # calculate the mass and inertia of the object
    operator_logger.info("The name of the imported object is: {}".format(obj.name))
    mass, inertia = obj_calc_inertia(obj)
    if mass == 0:
        operator_logger.error("Invalid mass: {:4f}".format( mass))
        # if the object has invalid mass, then the object cannot be used in the simulation
        raise Exception("Invalid mass!")
    return {"mass": mass, "inertia": inertia}


def move_object_to_ground(obj):
    """
    Moves the given object to the ground, that means the lowest vertex point hits the ground
    @param obj: Object to translate
    @return:
    """
    matrix_w = obj.matrix_world
    vectors = [matrix_w @ vertex.co for vertex in obj.data.vertices]
    min_vec = min(vectors, key=lambda item: item.z)
    obj.location[2] = obj.location[2] - min_vec[2]

def gen_collision_mesh(sdf_name, is_remesh=False):
    """
    Generate the mesh file for collision detection. Sometimes a simplified mesh
        file could possibility better for simulation, since computing contact
        is very time-consuming.

    @param sdf_name  : the name of the sdf package
    @param is_remesh : enable remesh functionality to simplify the Mesh
    """
    # ! This function modifies the shape of the mesh.
    # It must be used after gen_visual_mesh
    obj = bpy.data.objects[0]
    if is_remesh:
        obj_remesh(obj)
    # After remesh, the original Mesh will be overwritten!
    coll_name = sdf_name + "-coll"
    dst_path = os.path.abspath("{}/{}/mesh".format(output_dir, sdf_name))
    dst_name = "{}/{}.dae".format(dst_path, coll_name)
    convert_collada_file(dst_name)


def gen_visual_mesh(sdf_name):
    """
    Generate the mesh file for visualization.

    @param sdf_name  : the name of the sdf package
    """
    dst_path = os.path.abspath("{}/{}/mesh".format(output_dir, sdf_name))
    dst_name = "{}/{}.dae".format(dst_path, sdf_name)
    convert_collada_file(dst_name)


def convert_collada_file(dst_path):
    """
    Export the Mesh in the curent scene to [dst_path] as a .dae file

    @param dst_path : the .dae file to be exported
    """
    bpy.ops.wm.collada_export(filepath=dst_path,  apply_modifiers=True)


def usage():
    msg = """\33[33mUsage of this script:\033[0m
    \33[34mblender -b -P obj_sdf_converter_shapenet.py -- [path_to_mesh]

\33[34m[path_to_mesh]\033[0m refers to the absolute path of the folder which contains .obj files.
For example:
  python obj_sdf_converter.py '/home/user_name/Documents/meshes'
The output will be placed at: {out_path}
    """.format(
        out_path=os.path.abspath(output_folder)
    )
    operator_logger.info(msg)


def dae_sdf_converter(input_folder, sdf_mesh_scale,
                      dae_mesh_dim_min, dae_mesh_dim_max,
                      rotate_x, rotate_y, rotate_z,
                      translate_x, translate_y, translate_z,
                      lift_up,
                      sdf_author_name, sdf_author_mail, sdf_description
):
    """
    Convert all the .dae files in [input_folder] to sdf packages,
        and save them in [output_folder].

    @param input_folder: .dae files input folder
    @param sdf_mesh_scale: user defined scale of the sdf model meshes
    @param dae_mesh_dim_min : Min dimension of the .dae mesh files
    @param dae_mesh_dim_max : Max dimension of the .dae mesh files
    @param rotate_x : Rotate all meshes in x by degrees
    @param rotate_y : Rotate all meshes in Y by degrees
    @param rotate_z : Rotate all meshes in z by degrees
    @param translate_x : Translate all meshes in x
    @param translate_y : Translate all meshes in Y
    @param translate_z : Translate all meshes in z
    @param lift_up : If true the model is lifted above ground
    @param sdf_author_name : Name of the model author
    @param sdf_author_mail : Email of the model author
    @param sdf_description : Description of the model
    """
    global output_dir
    input_dir = "{}".format(input_folder)
    output_dir = os.path.join(input_dir, output_folder)
    operator_logger.info("input dir is {}".format(input_folder))
    operator_logger.info("output dir is {}".format(output_dir))

    operator_logger.info("\n")
    operator_logger.info(
        "\33[33mThe DAE files in this folder will be converted: {}\033[0m".format(
            os.path.abspath(input_dir))
    )
    operator_logger.info(
        "\33[33mThe converted SDF packages will be stored at: {}\033[0m".format(
            os.path.abspath(output_dir))
    )

    # extract all the mesh file in the current folder
    success_cnt = 0
    file_cnt = 0

    # list of all .dae files in all subdirectories
    files = glob.glob(input_dir + "/**/*.dae", recursive=True)
    #files = [os.path.basename(file_path) for file_path in files_path]
    operator_logger.info("Found these {} .dae files: {}".format(len(files), files))

    for idx, file in enumerate(files):
        file_cnt += 1

        # load each of the mesh file
        operator_logger.info(
            "\n\nProcessing the {} of {} files: {}".format(
                (idx + 1, len(files), file))
        )
        sdf_name = os.path.basename(file.replace(".dae", ""))
        # before processing, first check if it has already been created
        while check_output_exist(sdf_name) == True:
            operator_logger.info(
                "The package for {} has already been created. Adding index...".format(
                    sdf_name)
            )
            sdf_name = sdf_name + '_0'

        # create folder structure
        operator_logger.info("Creating package for {}...".format(sdf_name))
        create_sdf_folder(output_dir, sdf_name)

        # get inertial properties
        inertial_properties = calc_inertial(file,
                                            dae_mesh_dim_min, dae_mesh_dim_max,
                                            rotate_x, rotate_y, rotate_z,
                                            translate_x, translate_y, translate_z,
                                            lift_up)
        # generate visual mesh
        gen_visual_mesh(sdf_name)
        # generate collision mesh
        gen_collision_mesh(sdf_name)

        # create config file
        f = "{}/{}/model.config".format((output_dir, sdf_name))
        operator_logger.info("Creating model.config at {}".format(f))
        h = open(f, "w+")
        h.write(create_config_file(sdf_name, sdf_author_name, sdf_author_mail, sdf_description))
        h.close()

        # create sdf file
        f = "{}/{}/model.sdf".format(output_dir, sdf_name)
        operator_logger.info("Creating model.sdf at {}".format(f))
        h = open(f, "w+")
        h.write(
            create_sdf_file(
                sdf_name,
                sdf_mass=inertial_properties["mass"],
                sdf_inertia=inertial_properties["inertia"],
                sdf_mesh_scale=sdf_mesh_scale,
            )
        )
        h.close()

        success_cnt += 1

        delete_sdf_folder(sdf_name)

    operator_logger.info(
        "\33[33m\nConversion finished. Total: {}. Succeeded: {}.\033[0m".format(
            (file_cnt, success_cnt))
    )
    operator_logger.info(
        "\33[33mThe converted SDF packages have been stored at: {}\033[0m".format(
            os.path.abspath(output_folder))
    )
