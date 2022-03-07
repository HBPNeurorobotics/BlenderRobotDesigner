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
# Copyright (c) 2015, Karlsruhe Institute of Technology (KIT)
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#
#   2015-01-16: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#   2017-06:    Benedikt Feldotto (TUM): Model Meta Data
#   2017-07:    Benedikt Feldotto (TUM): Full Inertia Support
#   2017-09:    Benedikt Feldotto (TUM), Muscle Support
#
# ######

# System imports
import numpy as np

# Blender imports
import bpy
from bpy.props import (
    FloatProperty,
    StringProperty,
    EnumProperty,
    IntVectorProperty,
    FloatVectorProperty,
    PointerProperty,
    IntProperty,
    CollectionProperty,
    BoolProperty,
    CollectionProperty,
)

# RobotDesigner imports
from ..core import PluginManager
from ..properties.globals import global_properties


def raise_error(self, context):
    self.layout.label(text="Invalid Input! Please Check the Input Mass and Inertia!")


@PluginManager.register_property_group()
class RDDynamics(bpy.types.PropertyGroup):
    """
    Property group that contains dynamics parameters
    """

    def scale_update(self, context):
        obj = [
            o
            for o in bpy.context.active_object.children
            if o.RobotDesigner.tag == "PHYSICS_FRAME"
            and o.parent_bone == bpy.context.active_bone.name
        ]
        (frame,) = obj

        if (
            self.mass < 0
            or self.inertiaXX < 0
            or self.inertiaYY < 0
            or self.inertiaZZ < 0
            or self.inertiaXX + self.inertiaYY < self.inertiaZZ
            or self.inertiaYY + self.inertiaZZ < self.inertiaXX
            or self.inertiaZZ + self.inertiaXX < self.inertiaYY
        ):
            bpy.context.window_manager.popup_menu(
                raise_error, title="Error", icon="ERROR"
            )
        else:
            boxScaleX = np.sqrt(
                6 * (self.inertiaZZ + self.inertiaYY - self.inertiaXX) / self.mass
            )
            boxScaleY = np.sqrt(
                6 * (self.inertiaZZ + self.inertiaXX - self.inertiaYY) / self.mass
            )
            boxScaleZ = np.sqrt(
                6 * (self.inertiaXX + self.inertiaYY - self.inertiaZZ) / self.mass
            )
            frame.scale[0] = boxScaleX
            frame.scale[1] = boxScaleY
            frame.scale[2] = boxScaleZ

    mass: FloatProperty(
        name="Mass (kg)",
        soft_min=0,
        precision=4,
        step=0.1,
        default=1.0,
        update=scale_update,
    )
    # new inertia tensor
    inertiaXX: FloatProperty(
        name="", soft_min=0, precision=4, step=0.1, default=1.0, update=scale_update
    )
    inertiaYY: FloatProperty(
        name="", soft_min=0, precision=4, step=0.1, default=1.0, update=scale_update
    )
    inertiaZZ: FloatProperty(
        name="", soft_min=0, precision=4, step=0.1, default=1.0, update=scale_update
    )
    inertiaXY: FloatProperty(name="", precision=4, step=0.1, default=0.0)
    inertiaXZ: FloatProperty(name="", precision=4, step=0.1, default=0.0)
    inertiaYZ: FloatProperty(name="", precision=4, step=0.1, default=0.0)


@PluginManager.register_property_group()
class RDSensorNoise(bpy.types.PropertyGroup):
    """
    Prpperty group that contains sensor noise parameters
    """

    type: EnumProperty(items=[("gaussian", "Gaussian", "Gaussian")])
    mean: FloatProperty(name="Mean", default=0)
    stddev: FloatProperty(name="Stddev", default=0)


@PluginManager.register_property_group()
class RDCamera(bpy.types.PropertyGroup):
    """
    Property group that contains camera sensor parameters
    """

    width: IntProperty(default=320, min=1)
    height: IntProperty(default=240, min=1)
    format: EnumProperty(
        items=[
            ("L8", "L8", "L8"),
            ("R8G8B8", "R8G8B8", "R8G8B8"),
            ("B8G8R8", "B8G8R8", "B8G8R8"),
            ("BAYER_RGGB8", "BAYER_RGGB8", "BAYER_RGGB8"),
            ("BAYER_BGGR8", "BAYER_BGGR8", "BAYER_BGGR8"),
            ("BAYER_GBRG8", "BAYER_GBRG8", "BAYER_GBRG8"),
            ("BAYER_GRBG8", "BAYER_GRBG8", "BAYER_GRBG8"),
        ]
    )

    noise: PointerProperty(type=RDSensorNoise)


@PluginManager.register_property_group()
class RDContactSensor(bpy.types.PropertyGroup):
    """
    Property group that contains contact sensor parameters
    """

    collision: StringProperty(name="Collision", default="__default__")
    topic: StringProperty(name="Topic", default="__default_topic__")


@PluginManager.register_property_group()
class RDForceTorqueSensor(bpy.types.PropertyGroup):
    """
    Property group that contains force-torque sensor parameters
    """

    frame: StringProperty(name="Frame", default="child")
    measure_direction: StringProperty(
        name="Measure_direction", default="child_to_parent"
    )


@PluginManager.register_property_group()
class RDDepthCameraSensor(bpy.types.PropertyGroup):
    """
    Property group that contains depth camera sensor parameters
    """

    output: StringProperty(name="Output", default="depths")


@PluginManager.register_property_group()
class RDAltimeterSensor(bpy.types.PropertyGroup):
    """
    Property group that contains altimeter sensor parameters
    """

    vptype: StringProperty(name="VP_Type", default="none")
    vpmean: FloatProperty(name="VP_Mean", default=0)
    vpstddev: FloatProperty(name="VP_Stddev", default=0)
    vpbias_mean: FloatProperty(name="VPBias_Mean", default=0)
    vpbias_stddev: FloatProperty(name="VPBias_Stddev", default=0)
    vpprecision: FloatProperty(name="VP_Precision", default=0)
    vvtype: StringProperty(name="VP_Type", default="none")
    vvmean: FloatProperty(name="VP_Mean", default=0)
    vvstddev: FloatProperty(name="VV_Stddev", default=0)
    vvbias_mean: FloatProperty(name="VVBias_Mean", default=0)
    vvbias_stddev: FloatProperty(name="VVBias_Stddev", default=0)
    vvprecision: FloatProperty(name="VV_Precision", default=0)


@PluginManager.register_property_group()
class RDIMUSensor(bpy.types.PropertyGroup):
    """
    Property group that contains IMU sensor parameters
    """

    localization: StringProperty(name="Localization", default="CUSTOM")
    custom_rpy: FloatVectorProperty(
        name="Custom_rpy", precision=4, default=[0.0, 0.0, 0.0]
    )
    grav_dir_x: FloatVectorProperty(
        name="Grav_dir_x", precision=4, default=[1.0, 0.0, 0.0]
    )
    parent_frame: StringProperty(name="Parent_frame", default="Name of parent frame")
    topic: StringProperty(name="Topic", default="__default_topic__")
    vvtype: StringProperty(name="VV_Type", default="none")
    avxmean: FloatProperty(name="AVX_Mean", default=0)
    avxstddev: FloatProperty(name="AVX_Stddev", default=0)
    avxbias_mean: FloatProperty(name="AVXBias_Mean", default=0)
    avxbias_stddev: FloatProperty(name="AVXBias_Stddev", default=0)
    avxprecision: FloatProperty(name="AVX_precision", default=0)
    avymean: FloatProperty(name="AVY_Mean", default=0)
    avystddev: FloatProperty(name="AVY_Stddev", default=0)
    avybias_mean: FloatProperty(name="AVYBias_Mean", default=0)
    avybias_stddev: FloatProperty(name="AVYBias_Stddev", default=0)
    avyprecision: FloatProperty(name="AVY_Precision", default=0)
    avzmean: FloatProperty(name="AVZ_Mean", default=0)
    avzstddev: FloatProperty(name="AVZ_Stddev", default=0)
    avzbias_mean: FloatProperty(name="AVZBias_Stddev", default=0)
    avzbias_stddev: FloatProperty(name="AVZ_bias_stddev", default=0)
    avzprecision: FloatProperty(name="AVZ_Precision", default=0)
    laxmean: FloatProperty(name="LAX_mean", default=0)
    laxstddev: FloatProperty(name="LAX_stddev", default=0)
    laxbias_mean: FloatProperty(name="LAX_stddev", default=0)
    laxbias_stddev: FloatProperty(name="LAX_bias_stddev", default=0)
    laxprecision: FloatProperty(name="LAX_precision", default=0)
    laymean: FloatProperty(name="LAY_mean", default=0)
    laystddev: FloatProperty(name="LAY_stddev", default=0)
    laybias_mean: FloatProperty(name="LAY_Mean", default=0)
    laybias_stddev: FloatProperty(name="LAYBias_Stddev", default=0)
    layprecision: FloatProperty(name="LAY_Precision", default=0)
    lazmean: FloatProperty(name="LAZ_Mean", default=0)
    lazstddev: FloatProperty(name="LAZ_Stddev", default=0)
    lazbias_mean: FloatProperty(name="LAZ_Stddev", default=0)
    lazbias_stddev: FloatProperty(name="LAZBias_Stddev", default=0)
    lazprecision: FloatProperty(name="LAZ_Precision", default=0)


@PluginManager.register_property_group()
class RDLaserSensor(bpy.types.PropertyGroup):
    """
    Property group that contains laser sensor parameters
    """

    horizontal_samples: IntProperty(name="Horizontal Samples", default=320, min=1)
    vertical_samples: IntProperty(name="Vertical Samples", default=240, min=1)
    resolution: EnumProperty(
        items=[("8-Bit", "8-Bit", "8-Bit"), ("16-Bit", "16-Bit", "16-Bit")]
    )


class SceneSettingItem(bpy.types.PropertyGroup):
    """
    Property group that contains scene setting parameters
    """

    name = bpy.props.StringProperty(name="Test Prop", default="Unknown")
    value = bpy.props.IntProperty(name="Test Prop", default=22)


class RDMusclePoints(bpy.types.PropertyGroup):
    """
    Property group that contains muscle attachment point specifications
    """

    coordFrame: StringProperty(default="Select Segment")


class RDMuscleNames(bpy.types.PropertyGroup):
    """
    Property group that contains muscle names
    """

    name: StringProperty(default="Select Muscle")


class RDWrappingObjects(bpy.types.PropertyGroup):
    """
    Property group that contains wrapping object names
    """

    wrappingName: StringProperty(default="Wrapping Name")


@PluginManager.register_property_group()
class RDScaler(bpy.types.PropertyGroup):
    """
    Property Group in order to limit scaling options
    """

    def scale_all_update(self, context):

        obj = bpy.data.objects[global_properties.mesh_name.get(bpy.context.scene)]
        scale_object = obj.RobotDesigner.scaling
        obj.scale[0] = scale_object.scale_all
        obj.scale[1] = scale_object.scale_all
        obj.scale[2] = scale_object.scale_all

    def scale_radius_update(self, context):

        obj = bpy.data.objects[global_properties.mesh_name.get(bpy.context.scene)]
        scale_object = obj.RobotDesigner.scaling
        obj.scale[0] = scale_object.scale_radius
        obj.scale[1] = scale_object.scale_radius

    def scale_depth_update(self, context):

        obj = bpy.data.objects[global_properties.mesh_name.get(bpy.context.scene)]
        scale_object = obj.RobotDesigner.scaling
        obj.scale[2] = scale_object.scale_depth

    scale_all: FloatProperty(name="Scale All", default=1.0, update=scale_all_update)
    scale_radius: FloatProperty(
        name="Scale Radius", default=1.0, update=scale_radius_update
    )
    scale_depth: FloatProperty(
        name="Scale Depth", default=1.0, update=scale_depth_update
    )

@PluginManager.register_property_group()
class RDWrapScaler(bpy.types.PropertyGroup):
    """
    Property Group in order to limit wrapping scaling options
    """

    def scale_all_update(self, context):

        obj = bpy.data.objects[global_properties.wrapping_name.get(bpy.context.scene)]
        scale_object = obj.RobotDesigner.wrap_scaling
        obj.scale[0] = scale_object.scale_all
        obj.scale[1] = scale_object.scale_all
        obj.scale[2] = scale_object.scale_all

    def scale_radius_update(self, context):

        obj = bpy.data.objects[global_properties.wrapping_name.get(bpy.context.scene)]
        scale_object = obj.RobotDesigner.wrap_scaling
        obj.scale[0] = scale_object.scale_radius
        obj.scale[1] = scale_object.scale_radius

    def scale_depth_update(self, context):

        obj = bpy.data.objects[global_properties.wrapping_name.get(bpy.context.scene)]
        scale_object = obj.RobotDesigner.wrap_scaling
        obj.scale[2] = scale_object.scale_depth

    scale_all: FloatProperty(name="Scale All", default=1.0, update=scale_all_update)
    scale_radius: FloatProperty(
        name="Scale Radius", default=1.0, update=scale_radius_update
    )
    scale_depth: FloatProperty(
        name="Scale Depth", default=1.0, update=scale_depth_update
    )


@PluginManager.register_property_group()
class RDWrap(bpy.types.PropertyGroup):
    """
    Property group that contains muscle wrapping object parameters
    """

    WrappingType: EnumProperty(
        items=[
            ("WRAPPING_SPHERE", "Wrapping Sphere", "Wrapping Sphere"),
            ("WRAPPING_CYLINDER", "Wrapping Cylinder", "Wrapping Cylinder"),
        ]
    )

    bpy.utils.register_class(RDMuscleNames)
    muscleNames: CollectionProperty(type=RDMuscleNames)


@PluginManager.register_property_group()
class RDMuscle(bpy.types.PropertyGroup):
    """
    Property group that contains muscle parameters
    """

    def muscle_type_update(self, context):
        active_muscle = global_properties.active_muscle.get(bpy.context.scene)

        # if bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType == 'MYOROBOTICS':
        #    color = (1.0,0.0,0.0)
        if (
            bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType
            == "MILLARD_EQUIL"
        ):
            color = (0.8, 0.3, 0.0, 1.0)
        elif (
            bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType
            == "MILLARD_ACCEL"
        ):
            color = (0.3, 0.8, 0.0, 1.0)
        elif (
            bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType == "THELEN"
        ):
            color = (1.0, 0.0, 0.0, 1.0)
        elif (
            bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType
            == "RIGID_TENDON"
        ):
            color = (0.0, 0.0, 1.0, 1.0)
        elif (
            bpy.data.objects[active_muscle].RobotDesigner.muscles.muscleType
            == "MYOROBOTICS"
        ):
            color = (0.0, 1.0, 1.0, 1.0)

        bpy.data.objects[active_muscle].data.materials[
            active_muscle + "_vis"
        ].diffuse_color = color

    muscleType: EnumProperty(
        items=[  # ('MYOROBOTICS', 'Myorobotics', 'Myorobotics Muscle'),
            (
                "MILLARD_EQUIL",
                "Millard Equilibrium 2012",
                "Millard Equilibrium 2012 Muscle",
            ),
            (
                "MILLARD_ACCEL",
                "Millard Acceleration 2012",
                "Millard Acceleration 2012 Muscle",
            ),
            ("THELEN", "Thelen 2003", "Thelen 2003 Muscle"),
            ("RIGID_TENDON", "Rigid Tendon", "Rigid Tendon Muscle"),
            ("MYOROBOTICS", "Myorobotics Muscle", "Myorobotics Muscle"),
        ],
        name="Muscle Type:",
        update=muscle_type_update,
    )

    robotName: StringProperty(name="RobotName")
    length: FloatProperty(name="Muscle Length", default=0.0, precision=2)
    max_isometric_force: FloatProperty(name="Max Isometric Force", default=1000)

    bpy.utils.register_class(RDMusclePoints)
    pathPoints: CollectionProperty(type=RDMusclePoints)

    bpy.utils.register_class(RDWrappingObjects)
    connectedWraps: CollectionProperty(type=RDWrappingObjects)


@PluginManager.register_property_group()
class RDModelMeta(bpy.types.PropertyGroup):
    """
    Property group that contains model meta data suc as name, version and description
    """

    model_config: StringProperty(name="Config Name")
    model_version: StringProperty(name="Version", default="1.0")
    model_folder: StringProperty(name="Folder", default="")
    model_description: StringProperty(name="Description")


@PluginManager.register_property_group()
class ModelMeta(bpy.types.PropertyGroup):
    """
    Property group that contains model meta data suc as name, version and description
    """

    var1: StringProperty(name="Var1")
    var2: StringProperty(name="Var2")


@PluginManager.register_property_group()
class RobotSelfCollision(bpy.types.PropertyGroup):
    """
    Property group that contains information about self collision
    """

    robot_self_collide: BoolProperty(name="Self Collide")


@PluginManager.register_property_group()
class LinkInfo(bpy.types.PropertyGroup):
    """
    Property group that contains information about link's gravity and self collision
    """

    link_self_collide: BoolProperty(name="Self Collide", default=False)
    gravity: BoolProperty(name="Gravity", default=True)


@PluginManager.register_property_group()
class Ode(bpy.types.PropertyGroup):
    """
    Property group that contains ODE data
    """

    cfm_damping: BoolProperty(name="CFM Damping", default=False)
    i_s_damper: BoolProperty(name="Implicit-Spring-Damper", default=False)
    cfm: FloatProperty(name="CFM", default=0)
    erp: FloatProperty(name="ERP", default=0.2)


@PluginManager.register_property_group()
class WorldPhysics(bpy.types.PropertyGroup):
    """
    Property group that contains data about the world's physics engine.
    """

    name: StringProperty(name="Name", default="default_physics")
    max_step_size: FloatProperty(name="Max Step Size", default=0.001, precision=5)
    real_time_factor: FloatProperty(name="Real Time Factor", default=1)
    real_time_update_rate: FloatProperty(name="Real Time Update Rate", default=1000)
    max_contacts: IntProperty(name="Max Contacts", default=20)
    physics_engine: EnumProperty(
        items=[
            ("ODE", "ODE", "Select Open Dynamics Engine (ODE)"),
            ("SIMBODY", "Simbody", "Select Simbody as Physics Engine"),
            ("OPENSIM", "OpenSim", "Select OpenSim as Physics Engine"),
            ("DART", "DART", "Select DART as Physics Engine"),
        ],
        default="ODE",
    )


@PluginManager.register_property_group()
class WorldODE(bpy.types.PropertyGroup):
    """
    Property group that contains ODE parameters if selected as world's physics engine.
    """

    # Solver
    type: EnumProperty(
        items=[
            ("quick", "Quick", "Select Quick as type"),
            ("world", "World", "Select World as type"),
        ],
        default="quick",
    )
    min_step_size: FloatProperty(name="Min Step Size", default=0.0001, precision=6)
    iters: IntProperty(name="Iters", default=50)
    precon_iters: IntProperty(name="Precon Iters", default=0)
    sor: FloatProperty(name="Sor", default=1.3)
    use_dynamic_moi_rescaling: BoolProperty(
        name="Use Dynamic Moi Rescaling", default=False
    )

    # Constraints
    cfm: FloatProperty(name="Cfm", default=0.0)
    erp: FloatProperty(name="Erp", default=0.2)
    contact_max_correcting_vel: FloatProperty(
        name="Contact Max Correcting Vel", default=100
    )
    contact_surface_layer: FloatProperty(
        name="Contact Surface Layer", default=0.001, precision=5
    )


@PluginManager.register_property_group()
class WorldSimbody(bpy.types.PropertyGroup):
    """
    Property group that contains Simbody parameters if selected as world's physics engine.
    """

    min_step_size: FloatProperty(name="Min Step Size", default=0.0001, precision=5)
    accuracy: FloatProperty(name="Accuracy", default=0.001, precision=4, min=0, max=1)
    max_transient_velocity: FloatProperty(
        name="Max Transient Velocity", default=0.01, precision=3
    )

    # Contact
    stiffness: FloatProperty(name="Stiffness", default=1e8)
    dissipation: FloatProperty(name="Dissipation", default=100)
    plastic_coef_restitution: FloatProperty(
        name="Plastic Coef Restitution", default=0.5
    )
    plastic_impact_velocity: FloatProperty(name="Plastic Impact Velocity", default=0.5)
    static_friction: FloatProperty(name="Static Friction", default=0.9)
    dynamic_friction: FloatProperty(name="Dynamic Friction", default=0.9)
    viscous_friction: FloatProperty(name="Viscous Friction", default=0)
    override_impact_capture_velocity: FloatProperty(
        name="Override Impact Capture Velocity", default=0.001, precision=4
    )
    override_stiction_transition_velocity: FloatProperty(
        name="Override Stiction Transition Velocity", default=0.001, precision=4
    )


@PluginManager.register_property_group()
class WorldOpenSim(bpy.types.PropertyGroup):
    """
    Property group that contains OpenSim parameters if selected as world's physics engine.
    """

    min_step_size: FloatProperty(name="Min Step Size", default=0.0001, precision=5)
    accuracy: FloatProperty(name="Accuracy", default=0.001, precision=4, min=0, max=1)
    max_transient_velocity: FloatProperty(
        name="Max Transient Velocity", default=0.01, precision=3
    )

    # Contact
    stiffness: FloatProperty(name="Stiffness", default=1e8)
    dissipation: FloatProperty(name="Dissipation", default=100)
    plastic_coef_restitution: FloatProperty(
        name="Plastic Coef Restitution", default=0.5
    )
    plastic_impact_velocity: FloatProperty(name="Plastic Impact Velocity", default=0.5)
    static_friction: FloatProperty(name="Static Friction", default=0.9)
    dynamic_friction: FloatProperty(name="Dynamic Friction", default=0.9)
    viscous_friction: FloatProperty(name="Viscous Friction", default=0)
    override_impact_capture_velocity: FloatProperty(
        name="Override Impact Capture Velocity", default=0.001, precision=4
    )
    override_stiction_transition_velocity: FloatProperty(
        name="Override Stiction Transition Velocity", default=0.001, precision=4
    )


@PluginManager.register_property_group()
class SDFCollisionProperties(bpy.types.PropertyGroup):
    """
    Property group that contains SDF-Collision-parameters
    """

    def dissipation_update(self, context):
        self.osim_stiffness = self.elastic_modulus / (1 - self.poissons_ratio ** 2)

    restitution_coeff: FloatProperty(name="Restitution Coeff.", default=0, min=0, max=1)
    threshold: FloatProperty(name="Threshold", default=100000, min=0)
    coefficient: FloatProperty(name="Coefficient", default=1, min=0, max=1)
    use_patch_radius: BoolProperty(name="Use Patch Radius", default=True)
    patch_radius: FloatProperty(name="Patch Radius", default=0, min=0)
    surface_radius: FloatProperty(name="Surface Radius", default=0, min=0)
    slip: FloatProperty(name="Slip", default=0, min=0, max=1)
    mu: FloatProperty(name="Mu", default=1)
    mu2: FloatProperty(name="Mu2", default=1)
    fdir1: FloatVectorProperty(name="FDir1", default=(0, 0, 0), min=0, max=1)
    slip1: FloatProperty(name="Slip1", default=0, min=0, max=1)
    slip2: FloatProperty(name="Slip2", default=0, min=0, max=1)
    collide_wo_contact: BoolProperty(name="Colide Without Contact", default=False)
    collide_wo_contact_bitmask: IntProperty(
        name="Colide Without Contact Bitmask", default=1, min=0
    )
    collide_bitmask: IntProperty(name="Collide Bitmask", default=65535, min=0)
    category_bitmask: IntProperty(
        name="Category Bitmask", default=65535, min=0
    )  # if not specified, same as collide bitmask
    poissons_ratio: FloatProperty(
        name="Poissons Ratio",
        default=0.3,
        min=-1,
        max=0.5,
        update=dissipation_update,
        description="steel_poisson = 0.3 \n"
        + "concrete_poisson = 0.3 \n"
        + "nylon_poisson = 0.4 \n"
        + "rubber_poisson = 0.5 \n",
    )
    elastic_modulus: FloatProperty(
        name="Young Elastic Modulus",
        default=-1,
        min=-1,
        update=dissipation_update,
        description="steel_young = 200e9 \n"
        + "concrete_young = 25e9 \n"
        + "nylon_young = 2.5e9 \n"
        + "rubber_young = 0.01e9",
    )
    osim_stiffness: FloatProperty(
        name="Stiffness",
        default=1000000000,
        description="According to the SimbodyTheoryManual: stiffness = E* = E/(1 - v*v), \n"
        + "is the plane-strain modulus, where E is the Young's Elastic Modulus and v is Poisson's Ratio. \n"
        + "\nStiffness automatically calculated!",
    )
    # default 1e9 for contact playground
    osim_dissipation: FloatProperty(
        name="Dissipation",
        default=0.005,
        description="The dissipation coefficient c can be estimated as the slope of the \n"
        + "coefficient of restitution-vs-velocity curve at low velocities: e = 1. - c * v_i \n"
        + "with impact velocity v_i. \n\n"
        + "steel_dissipation = 0.001 \n"
        + "concrete_dissipation = 0.005 \n"
        + "nylon_dissipation = 0.005 \n"
        + "rubber_dissipation = 0.005",
    )  # default 0.05 for concrete ground
    soft_cfm: FloatProperty(name="Soft CFM", default=0, min=0)
    soft_erp: FloatProperty(name="Soft ERP", default=0.2, min=0, max=1)
    kp: FloatProperty(
        name="Kp", default=1000000000000, min=0, max=1000000000000
    )  # max number cannot be displayed in blender
    kd: FloatProperty(name="Kd", default=1, min=0, max=1)
    max_vel: FloatProperty(
        name="Max. Vel.", default=0.01, min=0, max=1
    )  # TODO: check validity of limit
    min_depth: FloatProperty(
        name="Min. Depth", default=0, min=0, max=10
    )  # TODO: check validity of limit
    bone_attachment: FloatProperty(name="Bone Attachment", default=100, min=0, max=1000)
    dart_stiffness: FloatProperty(name="Stiffness", default=100, min=0, max=10000)
    damping: FloatProperty(name="Damping", default=10, min=0, max=100)
    flesh_mass_fraction: FloatProperty(
        name="Flesh Mass Fraction", default=0.05, min=0, max=1
    )


@PluginManager.register_property_group()
class RDAuthor(bpy.types.PropertyGroup):
    """
    Property group that contains author details such as name and email
    """

    authorName: StringProperty(name="Author Name")
    authorEmail: StringProperty(name="Author Email")


@PluginManager.register_property_group()
class RDWorldsRobotListItem(bpy.types.PropertyGroup):
    """
    Store information which robot is included in the world and maybe some other information
    about how the robot should be included in the world to enable randomization of the environment
    """

    name: StringProperty(name="Name", default="Robot")
    export: BoolProperty(name="Export", default=False)


@PluginManager.register_property_group()
class RDWorlds(bpy.types.PropertyGroup):
    """
    Porperty group that contains world parameters and settings
    """

    name: StringProperty(name="Name", default="World")
    export_name: StringProperty(name="Export Name", default="World")
    gravity: FloatVectorProperty(name="Gravity", default=[0, 0, -9.81])
    # Magnetic field is multiplied with 10⁵ for better representation in GUI
    magnetic_field: FloatVectorProperty(
        name="Magnetic Field", precision=3, default=[0.6, 2.3, -4.2]
    )
    wind_active: BoolProperty(name="Wind Boolean", default=False)
    wind_vector: FloatVectorProperty(name="Wind Vector", default=[0, 0, 0])
    robot_list: CollectionProperty(type=RDWorldsRobotListItem)


@PluginManager.register_property_group(bpy.types.Object)
class RDObjects(bpy.types.PropertyGroup):
    """
    Property group that stores general information for individual Blender
    objects with respect to the RobotDesigner
    """

    fileName: StringProperty(name="Mesh File Name")
    tag: EnumProperty(
        items=[
            ("DEFAULT", "Default", "Default"),
            ("MARKER", "Marker", "Marker"),
            ("PHYSICS_FRAME", "Physics Frame", "Physics Frame"),
            ("ARMATURE", "Armature", "Armature"),
            ("COLLISION", "Collision", "Collision"),
            ("WRAPPING", "Wrapping", "Wrapping"),
            ("SENSOR", "Sensor", "Sensor"),
            ("BASIC_COLLISION_BOX", "Basic Collision Box", "Basic Collision Box"),
            (
                "BASIC_COLLISION_CYLINDER",
                "Basic Collision Cylinder",
                "Basic Collision Cylinder",
            ),
            (
                "BASIC_COLLISION_SPHERE",
                "Basic Collision Sphere",
                "Basic Collision Sphere",
            ),
            ("WORLD", "World", "World"),
        ]
    )

    sensor_type: EnumProperty(
        items=[
            ("CAMERA_SENSOR", "Camera Sensor", "Camera Sensor"),
            ("LASER_SENSOR", "Laser Sensor", "Laser Sensor"),
            ("CONTACT_SENSOR", "Contact Sensors", "Edit contact sensors"),
            (
                "FORCE_TORQUE_SENSOR",
                "Force Torque Sensors",
                "Edit Force Torque Sensors",
            ),
            (
                "DEPTH_CAMERA_SENSOR",
                "Depth Camera Sensors",
                "Edit Depth Camera Sensors",
            ),
            ("ALTIMETER_SENSOR", "Altimeter Sensors", "Edit Altimeter Sensors"),
            ("IMU_SENSOR", "IMU Sensors", "Edit IMU Sensors"),
        ]
    )

    dynamics: PointerProperty(type=RDDynamics)
    modelMeta: PointerProperty(type=RDModelMeta)

    physics_engine: EnumProperty(
        items=[
            ("ODE", "ODE", "Select Open Dynamics Engine (ODE)"),
            ("SIMBODY", "Simbody", "Select Simbody as Physics Engine"),
            ("OPENSIM", "OpenSim", "Select OpenSim as Physics Engine"),
            ("DART", "DART", "Select DART as Physics Engine"),
        ]
    )

    modelMeta1: PointerProperty(type=ModelMeta)
    robotSelfCollision: PointerProperty(type=RobotSelfCollision)
    linkInfo: PointerProperty(type=LinkInfo)
    ode: PointerProperty(type=Ode)
    sdfCollisionProps: PointerProperty(type=SDFCollisionProperties)

    author: PointerProperty(type=RDAuthor)
    cameraSensor: PointerProperty(type=RDCamera)
    contactSensor: PointerProperty(type=RDContactSensor)
    forceTorqueSensor: PointerProperty(type=RDForceTorqueSensor)
    depthCameraSensor: PointerProperty(type=RDDepthCameraSensor)
    altimeterSensor: PointerProperty(type=RDAltimeterSensor)
    imuSensor: PointerProperty(type=RDIMUSensor)
    laserSensor: PointerProperty(type=RDLaserSensor)
    muscles: PointerProperty(type=RDMuscle)
    wrap: PointerProperty(type=RDWrap)
    wrap_scaling: PointerProperty(type=RDWrapScaler)
    scaling: PointerProperty(type=RDScaler)
    worlds: PointerProperty(type=RDWorlds)
    worldPhysics: PointerProperty(type=WorldPhysics)
    worldODE: PointerProperty(type=WorldODE)
    worldSimbody: PointerProperty(type=WorldSimbody)
    worldOpenSim: PointerProperty(type=WorldOpenSim)
