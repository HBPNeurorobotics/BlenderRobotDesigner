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
from mathutils import Matrix, Euler, Vector
########
# RD imports
from ..osim import osim_dom  # xsd bindings
from ...core import config, PluginManager, RDOperator
from ...properties.globals import global_properties

from ...operators.muscles import CreateNewMuscle, CreateNewPathpoint
from ...operators.segments import SelectSegment
from ...operators.model import SelectModel
from ...operators.rigid_bodies import SelectGeometry
from ...operators.mesh_generation import AttachWrappingObject

from ..sdf.generic.helpers import string_to_list

# logger = logging.getLogger('SDF')
# logger.setLevel(logging.DEBUG)


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

        RDmuscle.RobotDesigner.muscles.muscleType = type

        if type in ['THELEN', 'MILLARD_EQUIL', 'MILLARD_ACCEL', 'RIGID_TENDON']:
            RDmuscle.RobotDesigner.muscles.length = muscle.optimal_fiber_length / 0.9
            RDmuscle.RobotDesigner.muscles.max_isometric_force = muscle.max_isometric_force

        global_properties.active_muscle.set(bpy.context.scene, muscle.name)
        self.import_pathpoints(muscle, RDmuscle)

        self.connect_wrapping_objects(muscle, RDmuscle)


    def connect_wrapping_objects(self, muscle, RDmuscle):
        """
        Create dependencies between muscle and corresponding wrapping objects
        :param muscle: .osim pyxb muscle instance
        :param RDmuscle: muscle object
        :return:
        """

        # iterate through all connected wrapping objects to the pyxb muscle instance
        w = 0
        while True:
            try:
                # add muscle to muscle list of all connected wrapping objects
                path = muscle.GeometryPath.PathWrapSet.objects.PathWrap[w]
                wrapping_object = bpy.context.scene.objects[path.wrap_object]
                wrapping_object.RobotDesigner.wrap.muscleNames.add()
                nr = len(wrapping_object.RobotDesigner.wrap.muscleNames)
                wrapping_object.RobotDesigner.wrap.muscleNames[nr - 1].name = RDmuscle.name

                # add wrapping object to wrapping objects list of muscle
                wrapList = RDmuscle.RobotDesigner.muscles.connectedWraps
                wrapList.add()
                nrw = len(wrapList)
                wrapList[nrw - 1].wrappingName = wrapping_object.name
                w += 1
            except:
                break

    def import_pathpoints(self, muscle, RDmuscle):
        """
            import muscle pathpoints from the osim file
        :param muscle: .osim pyxb muscle instance
        :return: RDmuscle: Robot Designer muscle instance
        """
        p = 0

        while (True):
            try:
                # current pathpoint
                pathpoint = muscle.GeometryPath.PathPointSet.objects.PathPoint[p]

                # get pathpoint parent world pose
                model = bpy.data.objects[global_properties.model_name.get(bpy.context.scene)]
                pose_bone = model.pose.bones[pathpoint.body]
                segment_world = model.matrix_world @ pose_bone.matrix

                # calculate pathpoint world pose
                location_local = [float(x) for x in pathpoint.location.split()]
                location_global = segment_world @ Matrix.Translation(
                    (location_local[0], location_local[1], location_local[2], 1))

                # create new pathpoint and set parameters of RD pathpoint object
                CreateNewPathpoint.run()
                location_global = location_global.to_translation()
                RDmuscle.data.splines[0].points[p].co = (location_global[0], location_global[1], location_global[2], 1)

                #  hook pathpoints to segments
                RDmuscle.RobotDesigner.muscles.pathPoints[p].coordFrame = pathpoint.body
                bpy.ops.RobotDesigner.select_segment_muscle(segment_name=pathpoint.body, pathpoint_nr=p + 1)

                p += 1

            except:
                break

    def import_wrapping_sphere(self, body, wrapping):
        """
        Create wrapping sphere from osim file
        :param body: parent segment
        :param wrapping: .osim pyxb wrapping object instance
        :return:
        """
        radius = wrapping.radius
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, calc_uvs=True,
                                             enter_editmode=False, location=(0, 0, 0))
        sphere = bpy.context.active_object
        sphere.name = wrapping.name

        lmat = bpy.data.materials.new(sphere.name)
        lmat.diffuse_color = (0.0, 0.135, 0.0, 1.0)
        # lmat.use_shadeless = True
        sphere.data.materials.append(lmat)

        sphere.RobotDesigner.tag = 'WRAPPING'
        sphere.RobotDesigner.wrap.WrappingType = 'WRAPPING_SPHERE'

        model = bpy.data.objects[global_properties.model_name.get(bpy.context.scene)]
        pose_bone = model.pose.bones[body.name]
        segment_world = model.matrix_world @ pose_bone.matrix

        model_posexyz = string_to_list(wrapping.translation[:])[0:3]
        model_poserpy = [0, 0, 0]
        trafo = Matrix.Translation(Vector(model_posexyz)) @ \
            Euler(model_poserpy, 'XYZ').to_matrix().to_4x4()

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.context.active_object.matrix_world = segment_world @ trafo @ bpy.context.active_object.matrix_world

        assigned_name = bpy.context.active_object.name

        bpy.ops.object.transform_apply(location=False,
                                       rotation=False,
                                       scale=True)
        SelectModel.run(model_name=model.name)
        SelectSegment.run(segment_name=body.name)
        SelectGeometry.run(geometry_name=assigned_name)

        bpy.data.objects[sphere.name].RobotDesigner.scaling.scale_all = radius
        # Model has to be selected and active in order to update scale
        # Geometry has to be selected, else the update function itself will take a different object
        bpy.data.objects[sphere.name].RobotDesigner.scaling.scale_all_update(bpy.context)

        AttachWrappingObject.run()

    def import_wrapping_cylinder(self, body, wrapping):
        """
        Create wrapping cylinder from osim file
        :param body: parent segment
        :param wrapping: .osim pyxb wrapping object instance
        :return:
        """
        radius = wrapping.radius
        depth = wrapping.length
        bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=1.0,
                                            enter_editmode=False, location=(0, 0, 0))
        cylinder = bpy.context.active_object
        cylinder.name = wrapping.name

        lmat = bpy.data.materials.new(cylinder.name)
        lmat.diffuse_color = (0.0, 0.135, 0.0, 1.0)
        # lmat.use_shadeless = True
        cylinder.data.materials.append(lmat)

        cylinder.RobotDesigner.tag = 'WRAPPING'
        cylinder.RobotDesigner.wrap.WrappingType = 'WRAPPING_CYLINDER'

        model = bpy.data.objects[global_properties.model_name.get(bpy.context.scene)]
        pose_bone = model.pose.bones[body.name]
        segment_world = model.matrix_world @ pose_bone.matrix

        model_posexyz = string_to_list(wrapping.translation[:])
        model_poserpy = string_to_list(wrapping.xyz_body_rotation[:])
        trafo = Matrix.Translation(Vector(model_posexyz)) @ \
                Euler(model_poserpy, 'XYZ').to_matrix().to_4x4()

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.context.active_object.matrix_world = segment_world @ trafo @ bpy.context.active_object.matrix_world

        assigned_name = bpy.context.active_object.name

        bpy.ops.object.transform_apply(location=False,
                                       rotation=False,
                                       scale=True)
        SelectModel.run(model_name=model.name)
        SelectSegment.run(segment_name=body.name)
        SelectGeometry.run(geometry_name=assigned_name)

        bpy.data.objects[cylinder.name].RobotDesigner.scaling.scale_radius = radius
        bpy.data.objects[cylinder.name].RobotDesigner.scaling.scale_depth = depth
        # Model has to be selected and active in order to update scale
        # Geometry has to be selected, else the update function itself will take a different object
        bpy.data.objects[cylinder.name].RobotDesigner.scaling.scale_radius_update(bpy.context)
        bpy.data.objects[cylinder.name].RobotDesigner.scaling.scale_depth_update(bpy.context)

        AttachWrappingObject.run()

    def import_osim(self):
        """
        Imports all listed muscles and wrapping objects in .osim file
        """
        # import wrapping objects
        # If multiple BodySets or WrapObjectSets exist, the loop can be easily enhanced.
        # However since osim_export does not have support for multiple BodySets, this has been left out for now.
        b = 0
        while True:
            try:
                body = self.muscles.Model.BodySet[0].objects.Body[b]
                print("\nimporting for ", body.name)
                s = 0
                while True:
                    try:
                        wrapping_sphere = body.WrapObjectSet[0].objects.WrapSphere[s]
                        print("importing wrapping sphere: ", wrapping_sphere.name)
                        self.import_wrapping_sphere(body, wrapping_sphere)
                        s += 1
                    except:
                        break
                c = 0
                while True:
                    try:
                        wrapping_cylinder = body.WrapObjectSet[0].objects.WrapCylinder[c]
                        print("importing wrapping cylinder: ", wrapping_cylinder.name)
                        self.import_wrapping_cylinder(body, wrapping_cylinder)
                        c += 1
                    except:
                        break
                b += 1
            except:
                break

        # import Thelen2003 Muscles
        m = 0
        while (True):
            try:
                muscle = self.muscles.Model.ForceSet.objects.Thelen2003Muscle[m]
                type = 'THELEN'
                self.import_muscles(muscle, type)
                m += 1
                print("import thelen")
            except:
                break

        # import Millard2012 Equilibrium Muscles
        m = 0
        while (True):
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

        # import Myorobotics Muscles
        m = 0
        while (True):
            try:
                muscle = self.muscles.Model.ForceSet.objects.MyoroboticsMuscle[m]
                type = 'MYOROBOTICS'
                self.import_muscles(muscle, type)
                m += 1
            except:
                break
