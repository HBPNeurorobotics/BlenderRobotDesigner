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
#  Copyright (c) 2021, TUM Technical University of Munich
#
# ######

# System imports
import pyxb
import os.path

# Blender imports
import bpy
import mathutils

# RD imports
from ..osim import osim_dom  # xsd bindings
from ...core import RDOperator
from ...core.logfile import export_logger
from ...properties.globals import global_properties


def get_muscles(active_model_name, context):
    """
    Return objects that represent muscles. And only those associated with the given model.

    :param active_model_name: The name of the robot for which to find associated muscles.
    :return: A list of associated objects that represent muscles.
    """
    return list(
        filter(
            lambda obj: obj.RobotDesigner.muscles.robotName == active_model_name,
            context.scene.objects,
        )
    )


def get_wrapping_objects(active_model_name, context):
    """
    helper function to get all wrapping objects of current model
    @param active_model_name: the active robot model name
    @param context: blender active context
    @return:
    """
    meshes = [
        obj
        for obj in context.scene.objects
        if obj.RobotDesigner.tag == "WRAPPING" and obj.parent.name == active_model_name
    ]
    return meshes


class OsimExporter(object):
    """
    OpenSim Exporter class
    """

    def __init__(self):
        self.doc = osim_dom.OpenSimDocument()
        self.doc.Version = "30000"
        self.doc.Model = pyxb.BIND(
            ForceSet=pyxb.BIND(
                objects=pyxb.BIND(
                    Millard2012EquilibriumMuscle=[],
                    Millard2012AccelerationMuscle=[],
                    Thelen2003Muscle=[],
                    RigidTendonMuscle=[],
                    MyoroboticsMuscle=[],
                )
            ),
            BodySet=[],
        )
        self.muscle_type_to_pyxb_list = {
            "Millard2012EquilibriumMuscle": self.doc.Model.ForceSet.objects.Millard2012EquilibriumMuscle,
            "Millard2012AccelerationMuscle": self.doc.Model.ForceSet.objects.Millard2012AccelerationMuscle,
            "Thelen2003Muscle": self.doc.Model.ForceSet.objects.Thelen2003Muscle,
            "RigidTendonMuscle": self.doc.Model.ForceSet.objects.RigidTendonMuscle,
            "MyoroboticsMuscle": self.doc.Model.ForceSet.objects.MyoroboticsMuscle,
        }

    def write_osim_file(self, filename):
        """
        write .osim file to directory
        @param filename: export filename
        @return:
        """
        assert filename.endswith(".osim")
        with open(filename, "w") as f:
            output = self.doc.toDOM()
            output = output.toprettyxml()
            f.write(output)

    def add_muscles(self, context, muscles, wrapping_objects):
        """
        collect respective wrapping objects to export
        @param context: Blender active context
        @param muscles: list of muscles to export
        @param wrapping_objects: list of wrapping objects
        @return:
        """
        for m in muscles:
            wrapping_list = [
                w for w in wrapping_objects if w.RobotDesigner.muscles.name == m.name
            ]
            self._add_blender_muscle(m, wrapping_list, context)

    def _select_pyxb_muscle_class(self, obj):
        """
        selects the pyxb generated muscle class for the given muscles
        @param obj:
        @return:
        """
        muscle_type_to_pyxb_type = {
            "MILLARD_EQUIL": osim_dom.Millard2012EquilibriumMuscle,
            "MILLARD_ACCEL": osim_dom.Millard2012AccelerationMuscle,
            "THELEN": osim_dom.Thelen2003Muscle,
            "RIGID_TENDON": osim_dom.RigidTendonMuscle,
            "MYOROBOTICS": osim_dom.MyoroboticsMuscle,
        }
        return muscle_type_to_pyxb_type[str(obj.RobotDesigner.muscles.muscleType)]

    def _add_blender_muscle(self, m, w, context):
        """
        add a blender muscle to export
        @param m: muscle
        @param w: wrapping object
        @param context:
        @return:
        """
        try:
            pyxb_class = self._select_pyxb_muscle_class(m)
        except KeyError as e:
            export_logger.error(
                "Warning: Not exporting object as muscle because: \n%s: %s"
                % (type(e).__name__, str(e))
            )
            return
        # calc muscle length
        bpy.ops.robotdesigner.calc_muscle_length(muscle=m.name)

        if m.RobotDesigner.muscles.muscleType in [
            "THELEN",
            "MILLARD_EQUIL",
            "MILLARD_ACCEL",
            "RIGID_TENDON",
            "MYOROBOTICS_MUSCLE",
        ]:
            m = pyxb_class(
                name=m.name,
                GeometryPath=osim_dom.GeometryPath(
                    PathPointSet=pyxb.BIND(
                        objects=pyxb.BIND(
                            PathPoint=self._build_pyxb_path_nodes_list(m, context)
                        )
                    ),
                    PathWrapSet=pyxb.BIND(
                        objects=pyxb.BIND(
                            PathWrap=self._build_pyxb_path_wraps_list(m, w, context)
                        )
                    ),
                ),
                # TODO: Fix hardcoded values
                max_isometric_force=[
                    0.6
                ],  # round(m.RobotDesigner.muscles.max_isometric_force, 4),
                optimal_fiber_length=[
                    0.6
                ],  # round(m.RobotDesigner.muscles.length * 0.9, 4),
                tendon_slack_length=[0.6],
            )  # round(m.RobotDesigner.muscles.length * 0.1, 4))
        else:
            m = pyxb_class(
                name=m.name,
                GeometryPath=osim_dom.GeometryPath(
                    PathPointSet=pyxb.BIND(
                        objects=pyxb.BIND(
                            PathPoint=self._build_pyxb_path_nodes_list(m, context)
                        )
                    ),
                    PathWrapSet=pyxb.BIND(
                        objects=pyxb.BIND(
                            PathWrap=self._build_pyxb_path_wraps_list(m, w, context)
                        )
                    ),
                ),
            )
        self._add_pyxb_muscle(m, context)

    def add_body_set(self, context, wrapping):
        """
        Add a body set the the .osim
        @param context: Blender active context
        @param wrapping: wrapping object
        @return:
        """
        bodyset = osim_dom.BodySet(
            name="", objects=pyxb.BIND(Body=self._add_body(context, wrapping))
        )
        self.doc.Model.BodySet.append(bodyset)

    def _add_body(self, context, wrapping):
        """
        Add wrapping object
        @param context: Blender active context
        @param wrapping: wrapping object
        @return:
        """

        def body(body, objects):
            return osim_dom.Body(
                name=body.name, WrapObjectSet=self._add_wrap_set(objects)
            )

        bodies = []

        for bone in context.active_object.data.bones:
            object_list = []
            for object in wrapping:
                if object.parent_bone == bone.name:
                    object_list.append(object)

            if len(object_list) != 0:
                bodies.append(body(bone, object_list))

        return bodies

    def _add_wrap_set(self, wrapping):
        """
        Add wrap set to .osim
        @param wrapping: wrapping objects
        @return:
        """
        cylinders = [
            cylinder
            for cylinder in wrapping
            if cylinder.RobotDesigner.wrap.WrappingType == "WRAPPING_CYLINDER"
        ]
        spheres = [
            sphere
            for sphere in wrapping
            if sphere.RobotDesigner.wrap.WrappingType == "WRAPPING_SPHERE"
        ]

        def wrap_set():
            return osim_dom.WrapObjectSet(
                name="",
                objects=pyxb.BIND(
                    WrapCylinder=self._add_w_cylinder(cylinders),
                    WrapSphere=self._add_w_sphere(spheres),
                ),
            )

        wrapset = []
        wrapset.append(wrap_set())
        return wrapset

    def _add_w_cylinder(self, cylinders):
        """
        Adds all wrapping cylinder to .osim
        @param cylinders: wrapping cylinders
        @return:
        """
        clist = []

        def cylinder_to_pyxb(nd):
            n, r, l, location, rotation = nd
            return osim_dom.WrapCylinder(
                xyz_body_rotation=osim_dom.vector3(
                    "%f %f %f" % (rotation[0], rotation[1], rotation[2])
                ),
                translation=osim_dom.vector3(
                    "%f %f %f" % (location[0], location[1], location[2])
                ),
                active="true",
                radius=r,
                length=l,
                name=n,
            )

        for c in cylinders:
            clist.append(cylinder_to_pyxb(self._get_wrapping_information(c)))
        return clist

    def _add_w_sphere(self, spheres):
        slist = []

        def sphere_to_pyxb(nd):
            n, r, l, location, rotation = nd
            return osim_dom.WrapSphere(
                translation=osim_dom.vector3(
                    "%f %f %f" % (location[0], location[1], location[2])
                ),
                active="true",
                radius=r,
                name=n,
            )

        for s in spheres:
            slist.append(sphere_to_pyxb(self._get_wrapping_information(s)))
        return slist

    def _get_wrapping_information(self, wrapping):
        """
        Returns wrapping object information
        @param wrapping: wrapping object
        @return:
        """
        blender_scale_factor = bpy.context.active_object.scale
        blender_scale_factor = [
            blender_scale_factor[0],
            blender_scale_factor[2],
            blender_scale_factor[1],
        ]
        segment = wrapping.parent_bone
        pose_bone = bpy.context.active_object.pose.bones[segment]
        pose = (
            pose_bone.matrix.inverted()
            @ bpy.context.active_object.matrix_world.inverted()
            @ bpy.data.objects[wrapping.name].matrix_world
        )

        pose_xyz = [i * j for i, j in zip(pose.translation, blender_scale_factor)]
        pose_rpy = pose.to_euler()

        name = wrapping.name

        scale = [
            i * j
            for i, j in zip(bpy.data.objects[wrapping.name].scale, blender_scale_factor)
        ]
        radius = scale[0]
        depth = scale[2]

        return (name, radius, depth, pose_xyz, pose_rpy)

    def _build_pyxb_path_wraps_list(self, m, w, context):
        """
        Builds pysb path wrap list
        @param m: muscle
        @param w: wrapping object
        @param context: Blender active context
        @return:
        """

        wrapping_objects = [
            objects for objects in m.RobotDesigner.muscles.connectedWraps
        ]
        length = len(wrapping_objects) + 1

        def path_wrap_to_pyxb(obj):
            i, object = obj
            return osim_dom.PathWrap(
                wrap_object=object.wrappingName,
                method="midpoint",
                name="PathWrap%i" % (length - i),
            )

        return list(map(path_wrap_to_pyxb, enumerate(wrapping_objects)))

    def _build_pyxb_path_nodes_list(self, m, context):
        """
        build pyxb path nodes list
        @param m: muscle
        @param context: Blender active context
        @return:
        """

        def transform_to_pyxb(nd):
            name, parent, (x, y, z) = nd
            x = x * bpy.data.objects[context.active_object.name].scale[0]
            y = y * bpy.data.objects[context.active_object.name].scale[1]
            z = z * bpy.data.objects[context.active_object.name].scale[2]
            return osim_dom.PathPoint(
                location=osim_dom.vector3("%f %f %f" % (x, y, z)),
                body=parent,
                name=name,
            )

        return list(
            map(transform_to_pyxb, self._get_intermediate_repr_path_nodes(m, context))
        )

    def _get_intermediate_repr_path_nodes(self, m, context):
        """
        Returns intermediate representation of path nodes
        @param m: muscle
        @param context: Blender active context
        @return:
        """

        def transform_vertex(arg):
            i, pt = arg
            name = "%s_node%i" % (m.name, i)
            parent = m.RobotDesigner.muscles.pathPoints[i].coordFrame
            x, y, z = pt.co
            active_model = global_properties.model_name.get(context.scene)
            pose_bone = bpy.data.objects[active_model].pose.bones[parent]
            pose = (
                pose_bone.matrix.inverted()
                @ bpy.data.objects[active_model].matrix_world.inverted()
                @ bpy.data.objects[m.name].matrix_world
            )
            vec = mathutils.Vector((x, y, z, 1))
            trans = mathutils.Matrix.Translation(vec)
            pose_rel = pose @ trans

            # bpy.data.meshes.remove(muscle_mesh, True)
            m.data.bevel_depth = global_properties.muscle_dim.get(context.scene)
            return (name, parent, (pose_rel[0][3], pose_rel[1][3], pose_rel[2][3]))

        m.data.bevel_depth = 0
        muscle_mesh = m.to_mesh()

        return map(transform_vertex, enumerate(muscle_mesh.vertices))

    def _add_pyxb_muscle(self, m, context):
        self.muscle_type_to_pyxb_list[type(m).__name__].append(m)


def create_osim(
    operator: RDOperator,
    context,
    filepath: str,
    meshpath: str,
    toplevel_directory: str,
    in_ros_package: bool,
    abs_filepaths=False,
):
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

    muscles = get_muscles(context.active_object.name, context)
    wrapping_objects = get_wrapping_objects(context.active_object.name, context)
    if muscles:
        pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(None)
        exporter = OsimExporter()
        exporter.add_muscles(context, muscles, wrapping_objects)
        if wrapping_objects:
            exporter.add_body_set(context, wrapping_objects)
        exporter.write_osim_file(os.path.join(toplevel_directory, "muscles.osim"))
