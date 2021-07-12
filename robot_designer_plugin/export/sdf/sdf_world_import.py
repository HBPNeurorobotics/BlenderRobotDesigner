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

# Blender imports
from bpy.props import StringProperty, BoolProperty

# RobotDesigner imports
from ...core import config, PluginManager, RDOperator
from .generic import sdf_world_dom
from .generic.helpers import string_to_list
from ...operators import world
from ...operators.helpers import ObjectMode
from . import sdf_import


def import_sdf(context, filepath: str):
    """
    Creates world and robot objects and sets parameters as defined in an sdf-file.
    """

    base_dir = os.path.dirname(filepath)
    FILE_URL_RELATIVE = "model://"

    root_xml = open(filepath).read()
    sdf = sdf_world_dom.CreateFromDocument(root_xml)

    for sdf_world in sdf.world:
        world.CreateNewWorld.run(sdf_world.name)
        obj = context.active_object
        world_obj = context.active_object.RobotDesigner.worlds
        world_obj.gravity = string_to_list(sdf_world.gravity[0])
        world_obj.magnetic_field = [
            element * pow(10, 5)
            for element in string_to_list(sdf_world.magnetic_field[0])
        ]
        if sdf_world.wind:
            world_obj.wind_active = True
            world_obj.wind_vector = string_to_list(sdf_world.wind[0].linear_velocity[0])

        for sdf_physics in sdf_world.physics:
            physics_obj = obj.RobotDesigner.worldPhysics
            physics_obj.name = sdf_physics.name
            for val in sdf_physics.max_step_size:
                physics_obj.max_step_size = val
            for val in sdf_physics.real_time_factor:
                physics_obj.real_time_factor = val
            for val in sdf_physics.real_time_update_rate:
                physics_obj.real_time_update_rate = val
            for val in sdf_physics.max_contacts:
                physics_obj.max_contacts = val
            physics_obj.physics_engine = sdf_physics.type

            if physics_obj.physics_engine == "ODE":
                ode_obj = obj.RobotDesigner.worldODE
                for sdf_ode in sdf_physics.ode:
                    for sdf_solver in sdf_ode.solver:
                        for val in sdf_solver.type:
                            ode_obj.type = val
                        for val in sdf_solver.min_step_size:
                            ode_obj.min_step_size = val
                        for val in sdf_solver.iters:
                            ode_obj.iters = val
                        for val in sdf_solver.precon_iters:
                            ode_obj.precon_iters = val
                        for val in sdf_solver.sor:
                            ode_obj.sor = val
                        for val in sdf_solver.use_dynamic_moi_rescaling:
                            ode_obj.use_dynamic_moi_rescaling = val
                    for sdf_constraints in sdf_ode.constraints:
                        for val in sdf_constraints.cfm:
                            ode_obj.cfm = val
                        for val in sdf_constraints.erp:
                            ode_obj.erp = val
                        for val in sdf_constraints.contact_max_correcting_vel:
                            ode_obj.contact_max_correcting_vel = val
                        for val in sdf_constraints.contact_surface_layer:
                            ode_obj.contact_surface_layer = val

            elif physics_obj.physics_engine == "SIMBODY":
                simbody_obj = obj.RobotDesigner.worldSimbody
                for sdf_simbody in sdf_physics.simbody:
                    for val in sdf_simbody.min_step_size:
                        simbody_obj.min_step_size = val
                    for val in sdf_simbody.accuracy:
                        simbody_obj.accuracy = val
                    for val in sdf_simbody.max_transient_velocity:
                        simbody_obj.max_transient_velocity = val
                    for sdf_contact in sdf_simbody.contact:
                        for val in sdf_contact.stiffness:
                            simbody_obj.stiffness = val
                        for val in sdf_contact.dissipation:
                            simbody_obj.dissipation = val
                        for val in sdf_contact.plastic_coef_restitution:
                            simbody_obj.plastic_coef_restitution = val
                        for val in sdf_contact.plastic_impact_velocity:
                            simbody_obj.plastic_impact_velocity = val
                        for val in sdf_contact.static_friction:
                            simbody_obj.static_friction = val
                        for val in sdf_contact.dynamic_friction:
                            simbody_obj.dynamic_friction = val
                        for val in sdf_contact.viscous_friction:
                            simbody_obj.viscous_friction = val
                        for val in sdf_contact.override_impact_capture_velocity:
                            simbody_obj.override_impact_capture_velocity = val
                        for val in sdf_contact.override_stiction_transition_velocity:
                            simbody_obj.override_stiction_transition_velocity = val

            elif physics_obj.physics_engine == "OPENSIM":
                opensim_obj = obj.RobotDesigner.worldOpenSim
                for sdf_opensim in sdf_physics.opensim:
                    for val in sdf_opensim.min_step_size:
                        opensim_obj.min_step_size = val
                    for val in sdf_opensim.accuracy:
                        opensim_obj.accuracy = val
                    for val in sdf_opensim.max_transient_velocity:
                        opensim_obj.max_transient_velocity = val
                    for sdf_contact in sdf_opensim.contact:
                        for val in sdf_contact.stiffness:
                            opensim_obj.stiffness = val
                        for val in sdf_contact.dissipation:
                            opensim_obj.dissipation = val
                        for val in sdf_contact.plastic_coef_restitution:
                            opensim_obj.plastic_coef_restitution = val
                        for val in sdf_contact.plastic_impact_velocity:
                            opensim_obj.plastic_impact_velocity = val
                        for val in sdf_contact.static_friction:
                            opensim_obj.static_friction = val
                        for val in sdf_contact.dynamic_friction:
                            opensim_obj.dynamic_friction = val
                        for val in sdf_contact.viscous_friction:
                            opensim_obj.viscous_friction = val
                        for val in sdf_contact.override_impact_capture_velocity:
                            opensim_obj.override_impact_capture_velocity = val
                        for val in sdf_contact.override_stiction_transition_velocity:
                            opensim_obj.override_stiction_transition_velocity = val

        for incl in sdf_world.include:
            uri = incl.uri[0]
            if uri.startswith(FILE_URL_RELATIVE):
                robot_name = uri.replace(FILE_URL_RELATIVE, "")
                sdf_import.ImportPlain.run(
                    filepath=base_dir + "/" + robot_name + "/model.sdf"
                )
                name = context.active_object.name
                context.view_layer.objects.active = obj
                world.AddRobot.run(robot_name=name)


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportPlainWorld(RDOperator):
    """
    :term:`Operator<operator>` for importing a world from a SDF plain file
    """

    bl_idname = config.OPERATOR_PREFIX + "import_world_from_sdf_plain"
    bl_label = "Import World SDF - plain"

    filter_glob: StringProperty(
        default="*.world",
        options={"HIDDEN"},
    )

    filepath: StringProperty(name="Filename", subtype="FILE_PATH")

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions()
    def execute(self, context):
        import_sdf(context, self.filepath)
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}
