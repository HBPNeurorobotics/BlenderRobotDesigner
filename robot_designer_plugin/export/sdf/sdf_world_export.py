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

# Blender imports
from bpy.props import StringProperty, BoolProperty

# RobotDesigner imports
from ...core import config, PluginManager, RDOperator
from .generic import sdf_world_dom
from .generic.helpers import list_to_string
from . import sdf_export
from ...operators.helpers import ObjectMode, WorldSelected


def create_sdf(context, abs_file_paths, gazebo, filepath):
    """
    Creates the SDF XML file and exports the world.

    :param operator: The calling operator
    :param context: The current context
    :param filepath: path to the SDF file
    :param meshpath: Path to the mesh directory
    :param toplevel_directory: The directory in which to export
    :param in_ros_package: Whether to export into a ros package or plain files
    :param abs_filepaths: If not installed into a ros package decides whether to use absolute file paths.
    :return:
    """
    world_obj = context.active_object
    world = context.active_object.RobotDesigner.worlds
    sdf = sdf_world_dom.sdf()
    sdf_world = sdf_world_dom.world()

    sdf_world.name = world.name
    sdf_world.gravity.append(list_to_string(world.gravity))
    sdf_world.magnetic_field.append(
        list_to_string([element * pow(10, -5) for element in world.magnetic_field])
    )

    if world.wind_active:
        sdf_world.wind.append(list_to_string(world.wind_vector))

    physics = context.active_object.RobotDesigner.worldPhysics

    sdf_physics = sdf_world_dom.physics()
    sdf_physics.name = physics.name
    sdf_physics.max_step_size.append(physics.max_step_size)
    sdf_physics.real_time_factor.append(physics.real_time_factor)
    sdf_physics.real_time_update_rate.append(physics.real_time_update_rate)
    sdf_physics.max_contacts.append(physics.max_contacts)
    sdf_physics.type = physics.physics_engine

    if physics.physics_engine == "ODE":
        ode = context.active_object.RobotDesigner.worldODE
        sdf_ode = sdf_world_dom.CTD_ANON_9()
        sdf_solver = sdf_world_dom.CTD_ANON_10()
        sdf_solver.type.append(ode.type)
        sdf_solver.min_step_size.append(ode.min_step_size)
        sdf_solver.iters.append(ode.iters)
        sdf_solver.precon_iters.append(ode.precon_iters)
        sdf_solver.sor.append(ode.sor)
        sdf_solver.use_dynamic_moi_rescaling.append(ode.use_dynamic_moi_rescaling)
        sdf_ode.solver.append(sdf_solver)
        sdf_constraints = sdf_world_dom.CTD_ANON_11()
        sdf_constraints.cfm.append(ode.cfm)
        sdf_constraints.erp.append(ode.erp)
        sdf_constraints.contact_max_correcting_vel.append(
            ode.contact_max_correcting_vel
        )
        sdf_constraints.contact_surface_layer.append(ode.contact_surface_layer)
        sdf_ode.constraints.append(sdf_constraints)

        sdf_physics.ode.append(sdf_ode)

    elif physics.physics_engine == "SIMBODY":
        simbody = context.active_object.RobotDesigner.worldSimbody
        sdf_simbody = sdf_world_dom.CTD_ANON_2()
        sdf_simbody.min_step_size.append(simbody.min_step_size)
        sdf_simbody.accuracy.append(simbody.accuracy)
        sdf_simbody.max_transient_velocity.append(simbody.max_transient_velocity)
        sdf_contact = sdf_world_dom.CTD_ANON_3()
        sdf_contact.stiffness.append(simbody.stiffness)
        sdf_contact.dissipation.append(simbody.dissipation)
        sdf_contact.plastic_coef_restitution.append(simbody.plastic_coef_restitution)
        sdf_contact.plastic_impact_velocity.append(simbody.plastic_impact_velocity)
        sdf_contact.static_friction.append(simbody.static_friction)
        sdf_contact.dynamic_friction.append(simbody.dynamic_friction)
        sdf_contact.viscous_friction.append(simbody.viscous_friction)
        sdf_contact.override_impact_capture_velocity.append(
            simbody.override_impact_capture_velocity
        )
        sdf_contact.override_stiction_transition_velocity.append(
            simbody.override_stiction_transition_velocity
        )
        sdf_simbody.contact.append(sdf_contact)

        sdf_physics.simbody.append(sdf_simbody)

    elif physics.physics_engine == "OPENSIM":
        opensim = context.active_object.RobotDesigner.worldOpenSim
        sdf_opensim = sdf_world_dom.CTD_ANON_4()
        sdf_opensim.min_step_size.append(opensim.min_step_size)
        sdf_opensim.accuracy.append(opensim.accuracy)
        sdf_opensim.max_transient_velocity.append(opensim.max_transient_velocity)
        sdf_contact = sdf_world_dom.CTD_ANON_5()
        sdf_contact.stiffness.append(opensim.stiffness)
        sdf_contact.dissipation.append(opensim.dissipation)
        sdf_contact.plastic_coef_restitution.append(opensim.plastic_coef_restitution)
        sdf_contact.plastic_impact_velocity.append(opensim.plastic_impact_velocity)
        sdf_contact.static_friction.append(opensim.static_friction)
        sdf_contact.dynamic_friction.append(opensim.dynamic_friction)
        sdf_contact.viscous_friction.append(opensim.viscous_friction)
        sdf_contact.override_impact_capture_velocity.append(
            opensim.override_impact_capture_velocity
        )
        sdf_contact.override_stiction_transition_velocity.append(
            opensim.override_stiction_transition_velocity
        )
        sdf_opensim.contact.append(sdf_contact)

        sdf_physics.opensim.append(sdf_opensim)

    sdf_world.physics.append(sdf_physics)

    armatures = [
        obj
        for obj in context.scene.objects
        if obj.type == "ARMATURE" and obj.name in world.robot_list
    ]

    for arm in armatures:
        if arm.RobotDesigner.modelMeta.model_folder == "":
            arm.RobotDesigner.modelMeta.model_folder = (
                arm.RobotDesigner.modelMeta.model_config
            )
        include_name = arm.RobotDesigner.modelMeta.model_folder
        sdf_include = sdf_world_dom.CTD_ANON_16()
        sdf_include.uri.append("model://" + include_name)
        sdf_world.include.append(sdf_include)

        context.view_layer.objects.active = arm
        if world.robot_list[arm.name].export:
            # export_plain_robot_sdf(filepath+"/"+arm.RobotDesigner.modelMeta.model_folder, context)
            sdf_export.ExportPlain.run(
                abs_file_paths,
                gazebo,
                filepath + "/" + arm.RobotDesigner.modelMeta.model_folder,
            )

    context.view_layer.objects.active = world_obj

    # TODO Does not match with XSD Files. They are a mixture of different versions
    sdf.version = "1.6"
    sdf.world.append(sdf_world)

    with open(filepath + world.export_name + ".world", "w") as f:
        output = sdf.toDOM().toprettyxml()
        f.write(output)
        f.close()


@RDOperator.Preconditions(ObjectMode, WorldSelected)
@PluginManager.register_class
class ExportPlainWorld(RDOperator):
    """
    :ref:`operator` for exporting  the selected world to a SDF File.
    """

    bl_idname = config.OPERATOR_PREFIX + "export_world_to_sdf_plain"
    bl_label = "Export World SDF - plain"

    filter_glob: StringProperty(
        default="*.world",
        options={"HIDDEN"},
    )

    abs_file_paths: BoolProperty(name="Absolute Filepaths", default=False)
    package_url = False

    gazebo: BoolProperty(name="Export Gazebo tags", default=True)
    filepath: StringProperty(name="Filename", subtype="FILE_PATH")

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions()
    def execute(self, context):
        create_sdf(
            context=context,
            abs_file_paths=self.abs_file_paths,
            gazebo=self.gazebo,
            filepath=self.filepath,
        )
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}
