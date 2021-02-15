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

# #####
#
#  Copyright (c) 2016-2021, TUM Technical University of Munich
#
# ######

"""
:term:`Operators <operator>` (and functions) exporting to SDF. It supports the creation of ROS packages, zipped
ROS packages and 'plain' SDF files with absolute or relative file paths.

Note: modify :meth:`pyxb.binding.basis._TypeBinding_mixin.toxml` to call :meth:`xml.dom.minidom.Node.toprettyxml`

"""

# System imports
import os
from math import radians
import tempfile
from pathlib import Path

# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty
from mathutils import Vector

# RobotDesigner imports
from .generic import sdf_tree
from .generic.helpers import list_to_string, string_to_list, localpose2globalpose
from ...core import config, PluginManager, RDOperator
from ...core.logfile import export_logger
from ...operators.helpers import ModelSelected, ObjectMode
from ...operators.model import SelectModel
from ..osim.osim_export import create_osim, get_muscles
from ..generic_tools import (
    create_thumbnail,
    export_rqtez_publisher_muscle,
    export_rqtez_publisher_controller,
    export_rqt_multiplot_muscles,
    export_rqt_multiplot_jointcontroller,
)
from ...properties.globals import global_properties

from .generic import config_model_dom
from .generic import sdf_model_dom
from pyxb.namespace import XMLSchema_instance as xsi
import pyxb


def _uri_for_meshes_and_muscles(
    in_ros_package: bool, abs_file_paths, toplevel_dir: str, file_path: str
):
    """
    Generate proper URI's for included geometry files and muscle definitions (.osim).

    :param in_ros_package:  Whether to export into a ros package or plain files
    :param abs_file_paths: If not installed into a ros package decides whether to use absolute file paths.
    :param toplevel_dir: The directory in which to export
    :param file_path: The absolute path of the file for which to generate the URI.
    :return:
    """
    if in_ros_package:
        uri = os.path.relpath(file_path, str(Path(toplevel_dir).parent))
        return "package://" + uri.replace(os.path.sep, "/")
    elif not abs_file_paths:
        uri = os.path.relpath(file_path, str(Path(toplevel_dir).parent))
        return "model://" + uri.replace(os.path.sep, "/")
    else:
        return "model://" + file_path.replace(os.path.sep, "/")


def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def export_mesh(
    operator: RDOperator,
    context,
    name: str,
    directory: str,
    toplevel_dir: str,
    in_ros_package: bool,
    abs_file_paths=False,
    export_collision=False,
):
    """
    Exports a mesh to a separate file.

    :param operator: The calling operator
    :param context: The current context
    :param name: the name of the mesh (not the file name).
    :type name: basestring.
    :param directory: The directory in which to install the meshes
    :param toplevel_dir: The directory in which to export
    :param in_ros_package: Whether to export into a ros package or plain files
    :param abs_file_paths: If not intstalled into a ros package decides whether to use absolute file paths.
    :param export_collision: Exporting a collision mesh or visualization mesh.
    :return: name of the file the mesh is stored in.
    """

    if not export_collision:
        meshes = [
            obj.name
            for obj in context.scene.objects
            if obj.type == "MESH"
            and obj.name == name
            and obj.RobotDesigner.tag == "DEFAULT"
        ]
        directory = os.path.join(directory, "meshes", "visual")

    else:
        meshes = [
            obj.name
            for obj in context.scene.objects
            if obj.type == "MESH"
            and name == obj.name
            and obj.RobotDesigner.tag == "COLLISION"
        ]
        directory = os.path.join(directory, "meshes", "collisions")
    if not os.path.exists(directory):
        os.makedirs(directory)
    # There is max. 1 object in the list
    assert len(meshes) <= 1
    for mesh in meshes:
        export_logger.debug("Processing mesh: %s", mesh)
        model_name = bpy.context.active_object.name
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[mesh].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects[mesh]
        # bpy.context.active_object.select = True
        # get the mesh vertices number
        bm = bpy.context.view_layer.objects.active.data
        # export_logger.debug("# of vertices=%d" % len(bm.vertices))
        if len(bm.vertices) > 1:
            if "." in mesh:
                file_path = os.path.join(
                    directory,
                    bpy.data.objects[mesh].RobotDesigner.fileName.replace(".", "_")
                    + ".dae",
                )
            else:
                file_path = os.path.join(
                    directory, bpy.data.objects[mesh].RobotDesigner.fileName + ".dae"
                )

            hide_flag_backup = bpy.context.view_layer.objects.active.hide_get()
            bpy.context.view_layer.objects.active.hide_set(
                False
            )  # Blender does not want to export hidden objects.

            # disconnect mesh from armature
            parent_bone = bpy.data.objects[mesh].parent_bone
            bpy.data.objects[mesh].parent = None

            bpy.ops.wm.collada_export(
                filepath=file_path,
                apply_modifiers=True,
                selected=True,
                use_texture_copies=True,
            )

            # reconnect mesh to armature
            bpy.data.objects[mesh].parent = bpy.data.objects[model_name]
            bpy.data.objects[mesh].parent_bone = parent_bone

            ## collada importer does not import library_visual_scene in blender 2.8
            # tree = ET.parse(source=file_path)
            # collada = tree.getroot()
            # if collada.tag[0] == '{':
            #     uri, ignore, tag = collada.tag[1:].partition("}")
            #     xmlns = '{' + uri + '}'
            #     ET.register_namespace('', uri)
            #     # ET.register_namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
            # else:
            #     xmlns = ''
            #
            # lib_geometries = collada.find(xmlns + 'library_geometries')
            # geometry_id = lib_geometries[0].get('id')
            # mesh_url = '#' + geometry_id
            #
            # node_attr = {'id': mesh, 'name': mesh, 'type': 'NODE'}
            # inst_geo_attr = {'url': mesh_url, 'name': mesh}
            #
            # lib_visual = collada.find(xmlns + 'library_visual_scenes')
            # visual_scene = lib_visual.find(xmlns + 'visual_scene')
            # if len(visual_scene) == 0:
            #     node = visual_scene.makeelement('node', node_attr)
            #     visual_scene.append(node)
            #     instance = node.makeelement('instance_geometry', inst_geo_attr)
            #     node.append(instance)
            #
            #     collada.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
            #
            #     indent(collada)
            #     ET.ElementTree(collada).write(file_path, encoding="utf-8", xml_declaration=True)
            ## collada importer does not import library_visual_scene in blender 2.8

            # for elem in collada:
            #     scene = elem.find(xmlns + 'visual_scene')
            #     try:
            #         node = scene.makeelement('node', node_attr)
            #         scene.append(node)
            #         instance = node.makeelement('instance_geometry', inst_geo_attr)
            #         instance.text = None
            #         node.append(instance)
            #     except:
            #         pass

            # collada.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')

            # ET.ElementTree(collada).write(file_path, encoding="utf-8", xml_declaration=True)

            bpy.context.view_layer.objects.active.hide_set(hide_flag_backup)

            # quick fix for dispersed meshes
            # todo: find appropriate solution
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    if "matrix" not in line:
                        file.write(line)
        else:
            if "." in mesh:
                file_path = os.path.join(
                    directory,
                    bpy.data.objects[mesh].RobotDesigner.fileName.replace(".", "_")
                    + "_vertices"
                    + str(len(bm.vertices))
                    + ".dae",
                )
            else:
                file_path = os.path.join(
                    directory,
                    bpy.data.objects[mesh].RobotDesigner.fileName
                    + "_vertices"
                    + str(len(bm.vertices))
                    + ".dae",
                )
        SelectModel.run(model_name=model_name)
        return _uri_for_meshes_and_muscles(
            in_ros_package, abs_file_paths, toplevel_dir, file_path
        )

        # return ("model://" + os.path.join(model_folder_name, "meshes",
        # mesh + ".dae"))


def create_sdf(
    operator: RDOperator,
    context,
    filepath: str,
    meshpath: str,
    toplevel_directory: str,
    in_ros_package: bool,
    abs_filepaths=False,
):
    """
    Creates the SDF XML file and exports the meshes

    :param operator: The calling operator
    :param context: The current context
    :param filepath: path to the SDF file
    :param meshpath: Path to the mesh directory
    :param toplevel_directory: The directory in which to export
    :param in_ros_package: Whether to export into a ros package or plain files
    :param abs_filepaths: If not installed into a ros package decides whether to use absolute file paths.
    :return:
    """

    def walk_segments(segment, tree, ref_pose):
        """
        Recursively builds a SDF tree object hierarchy for export

        :param segment: Reference to a blender bone object
        :param tree: Reference to a SDF Tree object. (Defined in sdf_tree.py)
        """

        export_logger.info("walk_segments: %s" % str(segment))

        child = tree.add()
        trafo, dummy = segment.RobotDesigner.getTransform()
        # trafo, _ = getTransformFromBlender(segment)

        # child.joint.origin.rpy = list_to_string(trafo.to_euler())
        # child.joint.origin.xyz = list_to_string([i * j for i, j in zip(trafo.translation, blender_scale_factor)])

        # Link Sdf properties export
        child.link.gravity.append(segment.RobotDesigner.linkInfo.gravity)
        child.link.self_collide.append(segment.RobotDesigner.linkInfo.link_self_collide)
        # joint ode properties
        child.joint.physics = [pyxb.BIND()]
        child.joint.physics[0].ode = [pyxb.BIND()]
        child.joint.physics[0].ode[0].cfm_damping.append(
            segment.RobotDesigner.ode.cfm_damping
        )
        child.joint.physics[0].ode[0].implicit_spring_damper.append(
            segment.RobotDesigner.ode.i_s_damper
        )
        child.joint.physics[0].ode[0].cfm.append(segment.RobotDesigner.ode.cfm)
        child.joint.physics[0].ode[0].erp.append(segment.RobotDesigner.ode.erp)
        child.joint.axis[0].dynamics = [pyxb.BIND()]
        child.joint.axis[0].dynamics[0].damping.append(
            segment.RobotDesigner.joint_dynamics.damping
        )
        child.joint.axis[0].dynamics[0].friction.append(
            segment.RobotDesigner.joint_dynamics.friction
        )
        child.joint.axis[0].dynamics[0].spring_reference.append(
            segment.RobotDesigner.joint_dynamics.spring_reference
        )
        child.joint.axis[0].dynamics[0].spring_stiffness.append(
            segment.RobotDesigner.joint_dynamics.spring_stiffness
        )

        pose_xyz = list_to_string(
            [i * j for i, j in zip(trafo.translation, blender_scale_factor)]
        )
        pose_rpy = list_to_string(trafo.to_euler())
        pose_xyz, pose_rpy = localpose2globalpose(ref_pose, pose_rpy, pose_xyz)

        export_logger.info(" child link pose'%s'" % " ".join([pose_xyz, pose_rpy]))
        child.link.pose.append(" ".join([pose_xyz, pose_rpy]))
        # child.link.pos[0] = ' '.join([pose_xyz, pose_rpy])
        # if '_joint' in segment.name:
        #     segment.name = segment.name.replace("_joint", "")
        if "." in segment.name:
            segment.name = segment.name.replace(".", "_")

        # sdf: here the child does not mean the child of the joint!!!!it is different
        child.joint.name = segment.RobotDesigner.joint_name
        child.link.name = segment.name.replace("_joint", "_link")

        if segment.parent:
            parent_link = [
                l
                for j, l in tree.connectedLinks.items()
                if segment.parent.name == l.name
            ]
            if parent_link[0] in tree.connectedJoints:
                tree.connectedJoints[parent_link[0]].append(child.joint)
            else:
                tree.connectedJoints[parent_link[0]] = [child.joint]

        # If root segment is connected to world
        if segment.RobotDesigner.world is True and segment.parent is None:
            tree.connectedJoints[tree.link] = [child.joint]

        if segment.parent:
            export_logger.info(" segment parent name'%s'" % segment.parent.name)
        export_logger.info(" segment joint name'%s'" % child.joint.name)
        export_logger.info(" segment link name'%s'" % child.link.name)

        export_logger.info(
            "connected links (joint->link): ",
            {j.name: l.name for j, l in tree.connectedLinks.items()},
        )
        export_logger.info(
            "connected joints (link->joint): ",
            {l.name: j[0].name for l, j in tree.connectedJoints.items()},
        )

        if segment.RobotDesigner.axis_revert:
            revert = -1
        else:
            revert = 1

        if segment.RobotDesigner.axis == "X":
            joint_axis_xyz = list_to_string(Vector((1, 0, 0)) * revert)
        elif segment.RobotDesigner.axis == "Y":
            joint_axis_xyz = list_to_string(Vector((0, 1, 0)) * revert)
        elif segment.RobotDesigner.axis == "Z":
            joint_axis_xyz = list_to_string(Vector((0, 0, 1)) * revert)

        child.joint.axis[0].xyz.append(joint_axis_xyz)

        # Settings the following flag is probably wrong. Why? Because RD derives the pose of the
        # child bone from the joint angle and axis w.r.t. the child edit pose. Hence Blenders/RD's
        # behaviour is consistent with Gazebo when this option is turned off.

        # child.joint.axis[0].use_parent_model_frame.append(True)

        export_logger.info(" joint axis xyz'%s'" % joint_axis_xyz)

        export_logger.info("Parent link:", child.joint.parent)
        export_logger.info("Child link:", child.joint.child)
        export_logger.info("Joint type:", child.joint.type)
        export_logger.info("Axis:", child.joint.axis)
        export_logger.info("Axis limit:", child.joint.axis[0].limit)
        export_logger.info("Axis xyz:", child.joint.axis[0].xyz)

        # Export individual limits only if set as active in GUI
        seg = segment.RobotDesigner
        if seg.jointMode == "REVOLUTE":
            if seg.theta.isActive or seg.dynamic_limits.isActive:
                # child.joint.axis[0].limit.append(sdf_model_dom.CTD_ANON_59())
                child.joint.axis[0].limit = [pyxb.BIND()]
            if seg.theta.isActive:
                child.joint.axis[0].limit[0].lower.append((radians(seg.theta.min)))
                child.joint.axis[0].limit[0].upper.append((radians(seg.theta.max)))
            if seg.dynamic_limits.isActive is True:
                child.joint.axis[0].limit[0].effort.append(seg.dynamic_limits.maxTorque)
                child.joint.axis[0].limit[0].velocity.append(
                    seg.dynamic_limits.maxVelocity
                )
            child.joint.type = "revolute"

        if seg.jointMode == "PRISMATIC":
            if seg.d.isActive or seg.dynamic_limits.isActive:
                # child.joint.axis[0].limit.append(sdf_model_dom.CTD_ANON_59())
                child.joint.axis[0].limit = [pyxb.BIND()]
            if seg.d.isActive:
                child.joint.axis[0].limit[0].lower.append(seg.d.min)
                child.joint.axis[0].limit[0].upper.append(seg.d.max)
            if seg.dynamic_limits.isActive:
                child.joint.axis[0].limit[0].effort.append(seg.dynamic_limits.maxTorque)
                child.joint.axis[0].limit[0].velocity.append(
                    seg.dynamic_limits.maxVelocity
                )
            child.joint.type = "prismatic"

        if seg.jointMode == "REVOLUTE2":
            child.joint.type = "revolute2"
        if seg.jointMode == "UNIVERSAL":
            child.joint.type = "universal"
        if seg.jointMode == "BALL":
            child.joint.type = "ball"
        if seg.jointMode == "FIXED":
            child.joint.type = "fixed"

        export_logger.info(" joint type'%s'" % child.joint.type)

        ### Add Meshes
        armature = context.active_object
        connected_meshes = [
            mesh.name
            for mesh in context.scene.objects
            if mesh.type == "MESH"
            and mesh.parent_bone == segment.name
            and mesh.parent == armature
        ]
        # if len(connected_meshes) > 0:
        #     child.link.name = connected_meshes[0]
        # else:
        #     child.link.name = child.joint.name + '_link'
        #     # todo: the RobotDesigner does not have the concept of
        #     # links further it is possible to have
        #     # todo: several meshes assigned to the same bone
        #     # todo: solutions add another property to a bone or
        #     # chose the name from the list of connected meshes
        for mesh in connected_meshes:
            export_logger.info("Connected mesh name: %s", mesh)
            pose_bone = context.active_object.pose.bones[segment.name]
            pose = (
                pose_bone.matrix.inverted()
                @ context.active_object.matrix_world.inverted()
                @ bpy.data.objects[mesh].matrix_world
            )

            # bpy.context.active_object.matrix_world = segment_world * trafo_sdf * bpy.context.active_object.matrix_world  # * inverse_matrix(bpy.context.active_object.matrix_world)#* \
            #  bpy.context.active_object.matrix_world
            visual_path = export_mesh(
                operator,
                context,
                mesh,
                meshpath,
                toplevel_directory,
                in_ros_package,
                abs_filepaths,
                export_collision=False,
            )
            export_logger.info("visual mesh path: %s", visual_path)
            if visual_path and "_vertices1.dae" not in visual_path:
                visual = child.add_mesh(
                    visual_path,
                    [
                        i * j
                        for i, j in zip(
                            bpy.data.objects[mesh].scale, blender_scale_factor
                        )
                    ],
                )
                visual_pose_xyz = list_to_string(
                    [i * j for i, j in zip(pose.translation, blender_scale_factor)]
                )
                visual_pose_rpy = list_to_string(pose.to_euler())
                visual.pose.append(" ".join([visual_pose_xyz, visual_pose_rpy]))
                visual.name = bpy.data.objects[mesh].name  # child.link.name
            else:
                export_logger.info("No visual model for: %s", mesh)
            collision_path = export_mesh(
                operator,
                context,
                mesh,
                meshpath,
                toplevel_directory,
                in_ros_package,
                abs_filepaths,
                export_collision=True,
            )
            export_logger.info("collision mesh path: %s", collision_path)
            # this does not include basic collision objects
            if collision_path and "_vertices1.dae" not in collision_path:
                collision = child.add_collision(
                    collision_path,
                    [
                        i * j
                        for i, j in zip(
                            bpy.data.objects[mesh].scale, blender_scale_factor
                        )
                    ],
                )
                export_logger.info(
                    " collision mesh pose translation wo scale'%s'" % pose.translation
                )
                export_logger.info(
                    " collision mesh pose scale factor'%s'" % blender_scale_factor
                )
                export_logger.info(
                    " collision mesh pose translation wi scale'%s'"
                    % [i * j for i, j in zip(pose.translation, blender_scale_factor)]
                )

                collision_pose_xyz = list_to_string(
                    [i * j for i, j in zip(pose.translation, blender_scale_factor)]
                )
                collision_pose_rpy = list_to_string(pose.to_euler())
                collision.pose.append(
                    " ".join([collision_pose_xyz, collision_pose_rpy])
                )
                collision.name = bpy.data.objects[
                    mesh
                ].name  # child.link.name + '_collision'
                export_logger.info(
                    " collision mesh pose'%s'" % collision.pose[0].value()
                )
            else:
                export_logger.info("No collision model for: %s", mesh)
            # add basic collision objects
            if "BASIC_COLLISION_" in bpy.data.objects[mesh].RobotDesigner.tag:
                collision = child.add_basic(
                    bpy.data.objects[mesh].RobotDesigner.tag,
                    [
                        i * j
                        for i, j in zip(
                            bpy.data.objects[mesh].scale, blender_scale_factor
                        )
                    ],
                )
                export_logger.info(
                    " basic collision mesh pose translation wo scale'%s'"
                    % pose.translation
                )
                export_logger.info(
                    " basic collision mesh pose scale factor'%s'" % blender_scale_factor
                )
                export_logger.info(
                    " basic collision mesh pose translation wi scale'%s'"
                    % [i * j for i, j in zip(pose.translation, blender_scale_factor)]
                )

                collision_pose_xyz = list_to_string(
                    [i * j for i, j in zip(pose.translation, blender_scale_factor)]
                )
                collision_pose_rpy = list_to_string(pose.to_euler())
                collision.pose.append(
                    " ".join([collision_pose_xyz, collision_pose_rpy])
                )
                collision.name = bpy.data.objects[
                    mesh
                ].name  # child.link.name + '_collision'
                export_logger.info(
                    " basic collision mesh pose'%s'" % collision.pose[0].value()
                )
            else:
                export_logger.info("No basic collision model for: %s", mesh)
            # export surface properties for both collision and basic collision objects
            if "COLLISION" in bpy.data.objects[mesh].RobotDesigner.tag:
                # add surface properties
                collision.surface.append(sdf_model_dom.surface())
                surface_property = bpy.data.objects[
                    mesh
                ].RobotDesigner.sdfCollisionProps
                # add bounce properties
                collision.surface[0].bounce = [pyxb.BIND()]
                bounce = collision.surface[0].bounce[0]
                bounce.restitution_coefficient.append(
                    surface_property.restitution_coeff
                )
                bounce.threshold.append(surface_property.threshold)
                # add friction properties
                collision.surface[0].friction = [pyxb.BIND()]
                friction = collision.surface[0].friction[0]
                friction.torsional = [pyxb.BIND()]
                torsional = friction.torsional[0]
                torsional.coefficient.append(surface_property.coefficient)
                torsional.use_patch_radius.append(surface_property.use_patch_radius)
                torsional.patch_radius.append(surface_property.patch_radius)
                torsional.surface_radius.append(surface_property.surface_radius)
                torsional.ode = [pyxb.BIND()]
                torsional.ode[0].slip.append(surface_property.slip)
                friction.ode = [pyxb.BIND()]
                friction_ode = collision.surface[0].friction[0].ode[0]
                friction_ode.mu.append(surface_property.mu)
                friction_ode.mu2.append(surface_property.mu2)
                fdir1 = "%f %f %f" % (
                    surface_property.fdir1[0],
                    surface_property.fdir1[1],
                    surface_property.fdir1[2],
                )
                friction_ode.fdir1.append(fdir1)
                friction_ode.slip1.append(surface_property.slip1)
                friction_ode.slip2.append(surface_property.slip2)

                # add contact properties
                collision.surface[0].contact = [pyxb.BIND()]
                contact = collision.surface[0].contact[0]
                contact.collide_without_contact.append(
                    surface_property.collide_wo_contact
                )
                contact.collide_without_contact_bitmask.append(
                    surface_property.collide_wo_contact_bitmask
                )
                contact.collide_bitmask.append(surface_property.collide_bitmask)
                contact.category_bitmask.append(surface_property.category_bitmask)
                contact.poissons_ratio.append(surface_property.poissons_ratio)
                contact.elastic_modulus.append(surface_property.elastic_modulus)
                if (
                    bpy.data.objects[
                        global_properties.model_name.get(bpy.context.scene)
                    ].RobotDesigner.physics_engine
                    == "OPENSIM"
                ):
                    contact.opensim = [pyxb.BIND()]
                    contact_opensim = contact.opensim[0]
                    contact_opensim.stiffness.append(surface_property.osim_stiffness)
                    contact_opensim.dissipation.append(
                        surface_property.osim_dissipation
                    )

                contact.ode = [pyxb.BIND()]
                contact_ode = contact.ode[0]
                contact_ode.soft_cfm.append(surface_property.soft_cfm)
                contact_ode.soft_erp.append(surface_property.soft_erp)
                contact_ode.kp.append(surface_property.kp)
                contact_ode.kd.append(surface_property.kd)
                contact_ode.max_vel.append(surface_property.max_vel)
                contact_ode.min_depth.append(surface_property.min_depth)
                # add soft contact properties
                # todo: not yet implemented dart properties.
                # if bpy.data.objects[
                #   global_properties.model_name.get(bpy.context.scene)].RobotDesigner.physics_engine == 'DART':

        ### Add Physics
        frame_names = [
            frame.name
            for frame in context.scene.objects
            if frame.RobotDesigner.tag == "PHYSICS_FRAME"
            and frame.parent_bone == segment.name
        ]

        # If no frame is connected create a default one. This is required for Gazebo!
        export_logger.info("frame names: %s", frame_names)

        # if not frame_names:
        #     child.add_inertial()

        for frame in frame_names:
            # Add inertial definitions (for Gazebo)
            inertial = child.link.inertial[0]
            export_logger.debug(inertial, inertial.__dict__)
            if bpy.data.objects[frame].parent_bone == segment.name:
                pose_bone = context.active_object.pose.bones[segment.name]

            # set mass
            inertial.mass[0] = bpy.data.objects[frame].RobotDesigner.dynamics.mass
            if inertial.mass[0] <= 0.0:
                raise ValueError(
                    "Mass of "
                    + frame
                    + " is not positive, but "
                    + str(inertial.mass[0])
                )
            # Ugly, to throw an exception here. But appending info_list did not print the info in the GUI.

            # set inertia
            inertial.inertia[0].ixx[0] = bpy.data.objects[
                frame
            ].RobotDesigner.dynamics.inertiaXX
            inertial.inertia[0].ixy[0] = bpy.data.objects[
                frame
            ].RobotDesigner.dynamics.inertiaXY
            inertial.inertia[0].ixz[0] = bpy.data.objects[
                frame
            ].RobotDesigner.dynamics.inertiaXZ
            inertial.inertia[0].iyy[0] = bpy.data.objects[
                frame
            ].RobotDesigner.dynamics.inertiaYY
            inertial.inertia[0].iyz[0] = bpy.data.objects[
                frame
            ].RobotDesigner.dynamics.inertiaYZ
            inertial.inertia[0].izz[0] = bpy.data.objects[
                frame
            ].RobotDesigner.dynamics.inertiaZZ

            # set inertial pose
            pose = (
                pose_bone.matrix.inverted()
                @ context.active_object.matrix_world.inverted()
                @ bpy.data.objects[frame].matrix_world
            )

            frame_pose_xyz = list_to_string(
                [i * j for i, j in zip(pose.translation, blender_scale_factor)]
            )
            frame_pose_rpy = list_to_string(pose.to_euler())

            inertial.pose[0] = " ".join([frame_pose_xyz, frame_pose_rpy])

        # add joint controllers
        if operator.gazebo and segment.RobotDesigner.jointController.isActive is True:
            if segment.parent is None and segment.RobotDesigner.world is False:
                pass
            else:
                if segment.RobotDesigner.jointController.P <= 1.0:
                    segment.RobotDesigner.jointController.P = 100

                controller_pid = list_to_string(
                    [
                        segment.RobotDesigner.jointController.P,
                        segment.RobotDesigner.jointController.I,
                        segment.RobotDesigner.jointController.D,
                    ]
                )

                controller = pyxb.BIND(
                    joint_name=child.joint.name,
                    type=segment.RobotDesigner.jointController.controllerType,
                    pid=controller_pid,
                )
                root.control_plugin.controller.append(controller)

        ### add link sensors
        sensor_names = [
            sensor.name
            for sensor in context.scene.objects
            if sensor.RobotDesigner.tag == "SENSOR"
            and sensor.parent_bone == segment.name
        ]

        export_logger.info(" sensor name'%s'" % sensor_names)

        for sensor in sensor_names:
            active_sensor = bpy.data.objects[sensor]
            type = active_sensor.RobotDesigner.sensor_type
            if type == "CAMERA_SENSOR":
                sensor_sdf = child.add_camera_sensor()
                sensor_sdf.name = sensor
                # camera
                sensor_sdf.type = "camera"
                sensor_sdf.camera.name = "left eze"
                # todo sensor_sdf.horizontal_fov = bpy.data.cameras[sensor].angle_x
            # todo   sensor_sdf.camera.image.append('imagename')
            # todo    sensor_sdf.camera.image.width.append(active_sensor.RobotDesigner.cameraSensor.width)
            # todo   sensor_sdf.camera.image.height = active_sensor.RobotDesigner.cameraSensor.height
            # todo    sensor_sdf.camera.image.format = active_sensor.RobotDesigner.cameraSensor.format

            else:
                "type not found"
        # elif type == 'CAMERA':   todo other sensor types
        #   sensor_sdf.type = 'camera'

        #      export_logger.info(" sensor name'%s'" % child.link.sensor.name)

        """
        A quick word on poses in sdf 1.6
        The way it works hasn't changed from 1.5
        You first have to append before you can freely set a value in it.
        Difference is when calling the value. 
        In 1.6, you have to use: ...pose[0].value() in order to call the value of the pose. 
        """

        # Add geometry
        for child_segments in segment.children:
            export_logger.info("Next Segment'%s'" % child_segments.name)
            ref_pose = string_to_list(child.link.pose[0].value())
            walk_segments(child_segments, child, ref_pose)

    robot_name = context.active_object.name

    blender_scale_factor = context.active_object.scale
    blender_scale_factor = [
        blender_scale_factor[0],
        blender_scale_factor[2],
        blender_scale_factor[1],
    ]

    root = sdf_tree.SDFTree.create_empty(robot_name)

    # add model pose
    root.sdf.model[0].pose.append(
        " ".join(
            [
                list_to_string(context.active_object.location),
                list_to_string(context.active_object.rotation_euler),
            ]
        )
    )

    # A link for world. Used for export of root links connected to world
    root.link.name = "world"

    if (
        bpy.data.objects[
            global_properties.model_name.get(bpy.context.scene)
        ].RobotDesigner.physics_engine
        == "OPENSIM"
    ):
        # add root geometries to root.link
        muscles = get_muscles(robot_name, context)
        if muscles:
            # add muscles path tag
            muscle_uri = _uri_for_meshes_and_muscles(
                in_ros_package,
                abs_filepaths,
                toplevel_directory,
                os.path.join(toplevel_directory, "muscles.osim"),
            )
            root.sdf.model[0].muscles.append(muscle_uri)

            # add OpenSim muscle plugin
            root.sdf.model[0].plugin.append(sdf_model_dom.plugin())
            length = len(root.sdf.model[0].plugin)
            root.sdf.model[0].plugin[length - 1].name = "muscle_interface_plugin"
            root.sdf.model[0].plugin[
                length - 1
            ].filename = "libgazebo_ros_muscle_interface.so"

    # build control plugin element
    # if there is a segment which has a controller attached to it: then create controller plugin
    for segment in bpy.context.active_object.data.bones:
        # The joint controller might still be active even if the root segment is not connected to world.
        # An if clause to ignore the controller in such a scenario
        if segment.parent is None and segment.RobotDesigner.world is False:
            pass
        elif segment.RobotDesigner.jointController.isActive is True:
            if operator.gazebo:
                root.sdf.model[0].plugin.append(sdf_model_dom.plugin())
                root.control_plugin = root.sdf.model[0].plugin[
                    len(root.sdf.model[0].plugin) - 1
                ]
                root.control_plugin.name = robot_name + "_controller"
                root.control_plugin.filename = "libgeneric_controller_plugin.so"
                root.control_plugin.controller = []
                break

    root_segments = [b for b in context.active_object.data.bones if b.parent is None]

    for segments in root_segments:
        export_logger.info("Root Segment'%s'" % segments.name)
        ref_pose = [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]  # transform to gazebo coordinate frame
        walk_segments(segments, root, ref_pose)

    export_logger.info("Writing to '%s'" % filepath)
    root.write(filepath)


def create_config(
    operator: RDOperator,
    context,
    filepath: str,
    meshpath: str,
    toplevel_directory: str,
    in_ros_package: bool,
    abs_filepaths=False,
):
    """
    Creates the model.config file and exports it

    :param operator: The calling operator
    :param context: The current context
    #   :param filepath: path to the SDF file
    #   :param meshpath: Path to the mesh directory
    :param toplevel_directory: The directory in which to export
    :param in_ros_package: Whether to export into a ros package or plain files
    :param abs_filepaths: If not installed into a ros package decides whether to use absolute file paths.
    :return:
    """

    # create model config element
    modelI = config_model_dom.model()

    # get model data
    modelI.name = bpy.context.active_object.RobotDesigner.modelMeta.model_config
    modelI.version = bpy.context.active_object.RobotDesigner.modelMeta.model_version

    # get thumbnail data
    modelI.thumbnail = "thumbnail.png"

    # set sdf fixed name
    sdf = config_model_dom.sdf_versioned()
    sdf._setValue("model.sdf")
    sdf.version = 1.6

    modelI.sdf = sdf

    # get author data
    author = config_model_dom.author_type(
        bpy.context.active_object.RobotDesigner.author.authorName,
        bpy.context.active_object.RobotDesigner.author.authorEmail,
    )
    # modelI.author = author
    modelI.author = author

    modelI.description = (
        bpy.context.active_object.RobotDesigner.modelMeta.model_description
    )

    # export model.config file
    with open(toplevel_directory + "/model.config", "w") as f:
        output = modelI.toDOM()
        output.documentElement.setAttributeNS(
            xsi.uri(),
            "xsi:schemaLocation",
            "http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config ../robot_model_configuration.xsd",
        )
        output.documentElement.setAttributeNS(
            xsi.uri(), "xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance"
        )
        output = output.toprettyxml()
        f.write(output)


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportPlain(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to a SDF File and mesh directory in the same directory.
    """

    bl_idname = config.OPERATOR_PREFIX + "export_to_sdf_plain"
    bl_label = "Export SDF - plain"

    filter_glob: StringProperty(
        default="*.sdf",
        options={"HIDDEN"},
    )

    abs_file_paths: BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo: BoolProperty(name="Export Gazebo tags", default=True)
    filepath: StringProperty(name="Filename", subtype="FILE_PATH")

    @classmethod
    def run(cls, abs_file_paths, gazebo, filepath):
        """
        Run this operator
        """

        return super().run(**cls.pass_keywords())

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        toplevel_dir = self.filepath
        self.filepath = os.path.join(self.filepath, "model.sdf")

        create_sdf(
            self,
            context,
            filepath=self.filepath,
            meshpath=toplevel_dir,
            toplevel_directory=toplevel_dir,
            in_ros_package=False,
            abs_filepaths=self.abs_file_paths,
        )
        create_config(
            self,
            context,
            filepath=self.filepath,
            meshpath=toplevel_dir,
            toplevel_directory=toplevel_dir,
            in_ros_package=False,
            abs_filepaths=self.abs_file_paths,
        )
        create_osim(
            self,
            context,
            filepath=self.filepath,
            meshpath=toplevel_dir,
            toplevel_directory=toplevel_dir,
            in_ros_package=False,
            abs_filepaths=self.abs_file_paths,
        )

        # thumbnail export
        create_thumbnail(toplevel_directory=toplevel_dir)

        # rqt_ez_publisher exports
        if (
            global_properties.export_rqt_ez_publisher_muscles.get(bpy.context.scene)
            == True
        ):
            export_rqtez_publisher_muscle(toplevel_directory=toplevel_dir)
        if (
            global_properties.export_rqt_ez_publisher_jointcontroller.get(
                bpy.context.scene
            )
            == True
        ):
            export_rqtez_publisher_controller(toplevel_directory=toplevel_dir)

        # rqt_multiplot exports
        if (
            global_properties.export_rqt_multiplot_muscles.get(bpy.context.scene)
            == True
        ):
            export_rqt_multiplot_muscles(toplevel_directory=toplevel_dir)
        if (
            global_properties.export_rqt_multiplot_jointcontroller.get(
                bpy.context.scene
            )
            == True
        ):
            export_rqt_multiplot_jointcontroller(toplevel_directory=toplevel_dir)

        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportPackage(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to an SDF File into a ROS package including model.config file.
    """

    bl_idname = config.OPERATOR_PREFIX + "export_to_sdf_package"
    bl_label = "Export SDF"

    filter_glob: StringProperty(
        default="*.sdf",
        options={"HIDDEN"},
    )

    abs_file_paths: BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo: BoolProperty(name="Export Gazebo tags", default=True)
    filepath: StringProperty(name="Filename", subtype="FILE_PATH")

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        toplevel_dir = self.filepath
        self.filepath = os.path.join(self.filepath, "model.sdf")

        create_sdf(
            self,
            context,
            filepath=self.filepath,
            meshpath=toplevel_dir,
            toplevel_directory=toplevel_dir,
            in_ros_package=False,
            abs_filepaths=self.abs_file_paths,
        )
        create_config(
            self,
            context,
            filepath=self.filepath,
            meshpath=toplevel_dir,
            toplevel_directory=toplevel_dir,
            in_ros_package=False,
            abs_filepaths=self.abs_file_paths,
        )
        create_osim(
            self,
            context,
            filepath=self.filepath,
            meshpath=toplevel_dir,
            toplevel_directory=toplevel_dir,
            in_ros_package=False,
            abs_filepaths=self.abs_file_paths,
        )

        # thumbnail export
        create_thumbnail(toplevel_directory=toplevel_dir)

        # rqt_ez_publisher exports
        if (
            global_properties.export_rqt_ez_publisher_muscles.get(bpy.context.scene)
            == True
        ):
            export_rqtez_publisher_muscle(toplevel_directory=toplevel_dir)
        if (
            global_properties.export_rqt_ez_publisher_jointcontroller.get(
                bpy.context.scene
            )
            == True
        ):
            export_rqtez_publisher_controller(toplevel_directory=toplevel_dir)

        # rqt_multiplot exports
        if (
            global_properties.export_rqt_multiplot_muscles.get(bpy.context.scene)
            == True
        ):
            export_rqt_multiplot_muscles(toplevel_directory=toplevel_dir)
        if (
            global_properties.export_rqt_multiplot_jointcontroller.get(
                bpy.context.scene
            )
            == True
        ):
            export_rqt_multiplot_jointcontroller(toplevel_directory=toplevel_dir)

        return {"FINISHED"}

    def invoke(self, context, event):
        self.filepath = (
            context.active_object.RobotDesigner.modelMeta.model_folder.replace(" ", "_")
        )
        if self.filepath == "":
            self.filepath = global_properties.model_name.get(bpy.context.scene).replace(
                " ", "_"
            )
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


@RDOperator.Preconditions(ModelSelected, ObjectMode)
@PluginManager.register_class
class ExportZippedPackage(RDOperator):
    """
    :ref:`operator` for exporting  the selected robot to an SDF File into a zipped ROS package.
    """

    bl_idname = config.OPERATOR_PREFIX + "export_to_sdf_package_zipped"
    bl_label = "Export SDF as zipped folder"

    filter_glob: StringProperty(
        default="*.zip",
        options={"HIDDEN"},
    )

    abs_file_paths: BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo: BoolProperty(name="Export Gazebo tags", default=True)
    filepath: StringProperty(name="Filename", subtype="FILE_PATH")

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions(ModelSelected, ObjectMode)
    def execute(self, context):
        """
        Code snipped from `<http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory>`_
        """
        import zipfile

        if os.path.isdir(self.filepath):
            self.logger.debug(self.filepath)
            self.report({"ERROR"}, "No File selected!")
            return {"FINISHED"}

        def zipdir(path, ziph):
            # ziph is zipfile handle
            for root, dirs, files in os.walk(path):
                self.logger.debug("%s, %s, %s,", root, dirs, files)
                for file in files:
                    file_path = os.path.join(root, file)
                    ziph.write(file_path, os.path.relpath(file_path, path))

        with tempfile.TemporaryDirectory() as target:

            dir_name = os.path.splitext(os.path.basename(self.filepath))[0]
            temp_dir = os.path.join(target, dir_name)
            temp_file = os.path.join(temp_dir, "model.sdf")
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)
            create_sdf(
                self,
                context,
                filepath=temp_file,
                meshpath=temp_dir,
                toplevel_directory=temp_dir,
                in_ros_package=False,
                abs_filepaths=self.abs_file_paths,
            )
            create_config(
                self,
                context,
                filepath=self.filepath,
                meshpath=temp_dir,
                toplevel_directory=temp_dir,
                in_ros_package=False,
                abs_filepaths=self.abs_file_paths,
            )
            create_osim(
                self,
                context,
                filepath=self.filepath,
                meshpath=temp_dir,
                toplevel_directory=temp_dir,
                in_ros_package=False,
                abs_filepaths=self.abs_file_paths,
            )

            # thumbnail export
            create_thumbnail(toplevel_directory=toplevel_dir)

            # rqt_ez_publisher exports
            if (
                global_properties.export_rqt_ez_publisher_muscles.get(bpy.context.scene)
                == True
            ):
                export_rqtez_publisher_muscle(toplevel_directory=toplevel_dir)
            if (
                global_properties.export_rqt_ez_publisher_jointcontroller.get(
                    bpy.context.scene
                )
                == True
            ):
                export_rqtez_publisher_controller(toplevel_directory=toplevel_dir)

            # rqt_multiplot exports
            if (
                global_properties.export_rqt_multiplot_muscles.get(bpy.context.scene)
                == True
            ):
                export_rqt_multiplot_muscles(toplevel_directory=toplevel_dir)
            if (
                global_properties.export_rqt_multiplot_jointcontroller.get(
                    bpy.context.scene
                )
                == True
            ):
                export_rqt_multiplot_jointcontroller(toplevel_directory=toplevel_dir)

            self.logger.debug(temp_file)
            with zipfile.ZipFile(self.filepath, "w") as zipf:
                zipdir(target, zipf)

        return {"FINISHED"}

    def invoke(self, context, event):
        self.filepath = (
            context.active_object.RobotDesigner.modelMeta.model_folder.replace(" ", "_")
        )
        if self.filepath == "":
            self.filepath = global_properties.model_name.get(bpy.context.scene).replace(
                " ", "_"
            )
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}
