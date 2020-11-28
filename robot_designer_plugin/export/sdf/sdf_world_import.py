# ######
# System imports
import os
import sys

# ######
# Blender imports
import bpy
from bpy.props import StringProperty, BoolProperty

# ######
# RobotDesigner imports
from ...core import config, PluginManager, RDOperator
from .generic import sdf_root_dom
from .generic.helpers import list_to_string, string_to_list
from . import sdf_export
from ...operators import world
from ...operators.helpers import ModelSelected, ObjectMode
from . import sdf_import


def import_sdf(context, filepath: str):
    """
    Creates world and robot objects and sets parameters as defined in an sdf-file.
    """

    base_dir = os.path.dirname(filepath)
    FILE_URL_RELATIVE = "model://"

    root_xml = open(filepath).read()
    sdf = sdf_root_dom.CreateFromDocument(root_xml)

    for sdf_world in sdf.world:
        world.CreateNewWorld.run(sdf_world.name)
        obj = context.active_object
        world_obj = context.active_object.RobotDesigner.worlds
        world_obj.gravity = string_to_list(sdf_world.gravity[0])
        world_obj.magnetic_field = [element * pow(10, 5) for element in string_to_list(sdf_world.magnetic_field[0])]
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

            if physics_obj.physics_engine == 'ODE':
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

            elif physics_obj.physics_engine == 'SIMBODY':
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

        for incl in sdf_world.include:
            uri = incl.uri[0]
            if uri.startswith(FILE_URL_RELATIVE):
                robot_name = uri.replace(FILE_URL_RELATIVE, '')
                sdf_import.ImportPlain.run(filepath=base_dir+'/'+robot_name+'/model.sdf')
                name = context.active_object.name
                context.view_layer.objects.active = obj
                world.AddRobot.run(robot_name=name)


@RDOperator.Preconditions(ObjectMode)
@PluginManager.register_class
class ImportPlainWorld(RDOperator):
    """
    :term:`Operator<operator>` for importing a world from a SDF plain file
    """

    bl_idname = config.OPERATOR_PREFIX + 'import_world_from_sdf_plain'
    bl_label = "Import World SDF - plain"

    filter_glob: StringProperty(
        default="*.world",
        options={'HIDDEN'},
    )

    filepath: StringProperty(name="Filename", subtype='FILE_PATH')

    @RDOperator.OperatorLogger
    @RDOperator.Postconditions()
    def execute(self, context):
        import_sdf(context, self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}