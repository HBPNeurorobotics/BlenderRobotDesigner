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

# RobotDesigner imports
from . import menus
from .helpers import SolverBox, ConstraintsBox, SimbodyBox
from ..operators import world
from ..export.sdf import sdf_world_export, sdf_world_import
from ..core.logfile import LogFunction


@LogFunction
def draw(layout, context):
    """
    Draws the user interface for geometric modelling.

    :param layout: Current GUI element (e.g., collapsible box, row, etc.)
    :param context: Blender context
    """
    world_selected = True

    # Check if world is currently selected
    if not check_world(context):
        layout.menu(menus.WorldMenu.bl_idname, text="Select World")
        world_selected = False
    else:
        layout.menu(menus.WorldMenu.bl_idname, text=context.active_object.name)

    if world_selected:
        # Display general parameters of the world
        box_general = layout.box()
        box_general.label(text="General Parameters")
        row = box_general.row()
        row.prop(context.active_object, "name", text="Name")

        box_environment = layout.box()
        box_environment.label(text="Environment")
        row = box_environment.row()
        row.prop(context.active_object.RobotDesigner.worlds, "gravity", text="Gravity")
        row = box_environment.row()
        row.prop(
            context.active_object.RobotDesigner.worlds,
            "magnetic_field",
            text="Magnetic Field (*10⁵)",
        )
        row = box_environment.row()
        row.prop(context.active_object.RobotDesigner.worlds, "wind_active", text="Wind")
        row.prop(context.active_object.RobotDesigner.worlds, "wind_vector", text="")

        # Display Physics Engine
        box_physics = layout.box()
        box_physics.label(text="Physics Engine")

        row = box_physics.row()
        row.prop(context.active_object.RobotDesigner.worldPhysics, "name")
        row = box_physics.row()
        row.prop(context.active_object.RobotDesigner.worldPhysics, "max_step_size")
        row = box_physics.row()
        row.prop(context.active_object.RobotDesigner.worldPhysics, "real_time_factor")
        row = box_physics.row()
        row.prop(
            context.active_object.RobotDesigner.worldPhysics, "real_time_update_rate"
        )
        row = box_physics.row()
        row.prop(context.active_object.RobotDesigner.worldPhysics, "max_contacts")
        row = box_physics.row()
        row.prop(
            context.active_object.RobotDesigner.worldPhysics,
            "physics_engine",
            text="Type",
        )
        sub_box = box_physics.box()
        sub_box.label(
            text=context.active_object.RobotDesigner.worldPhysics.physics_engine
        )

        # Display ODE properties if selected as physics engine
        if context.active_object.RobotDesigner.worldPhysics.physics_engine == "ODE":
            solver = SolverBox.get(sub_box, context, "Solver")
            if solver:
                row = solver.row()
                row.prop(context.active_object.RobotDesigner.worldODE, "type")
                row = solver.row()
                row.prop(context.active_object.RobotDesigner.worldODE, "min_step_size")
                row = solver.row()
                row.prop(context.active_object.RobotDesigner.worldODE, "iters")
                row = solver.row()
                row.prop(context.active_object.RobotDesigner.worldODE, "precon_iters")
                row = solver.row()
                row.prop(context.active_object.RobotDesigner.worldODE, "sor")
                row = solver.row()
                row.prop(
                    context.active_object.RobotDesigner.worldODE,
                    "use_dynamic_moi_rescaling",
                )

            constraints = ConstraintsBox.get(sub_box, context, "Constraints")
            if constraints:
                row = constraints.row()
                row.prop(context.active_object.RobotDesigner.worldODE, "cfm")
                row = constraints.row()
                row.prop(context.active_object.RobotDesigner.worldODE, "erp")
                row = constraints.row()
                row.prop(
                    context.active_object.RobotDesigner.worldODE,
                    "contact_max_correcting_vel",
                )
                row = constraints.row()
                row.prop(
                    context.active_object.RobotDesigner.worldODE,
                    "contact_surface_layer",
                )

        # Display Simbody properties if selected as physics engine
        elif (
            context.active_object.RobotDesigner.worldPhysics.physics_engine == "SIMBODY"
        ):
            row = sub_box.row()
            row.prop(context.active_object.RobotDesigner.worldSimbody, "min_step_size")
            row = sub_box.row()
            row.prop(context.active_object.RobotDesigner.worldSimbody, "accuracy")
            row = sub_box.row()
            row.prop(
                context.active_object.RobotDesigner.worldSimbody,
                "max_transient_velocity",
            )

            contact = SimbodyBox.get(sub_box, context, "Contact")
            if contact:
                row = contact.row()
                row.prop(context.active_object.RobotDesigner.worldSimbody, "stiffness")
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldSimbody, "dissipation"
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldSimbody,
                    "plastic_coef_restitution",
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldSimbody,
                    "plastic_impact_velocity",
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldSimbody, "static_friction"
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldSimbody, "dynamic_friction"
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldSimbody, "viscous_friction"
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldSimbody,
                    "override_impact_capture_velocity",
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldSimbody,
                    "override_stiction_transition_velocity",
                )

        # Display OpenSim properties if selected as physics engine
        elif (
            context.active_object.RobotDesigner.worldPhysics.physics_engine == "OPENSIM"
        ):
            row = sub_box.row()
            row.prop(context.active_object.RobotDesigner.worldOpenSim, "min_step_size")
            row = sub_box.row()
            row.prop(context.active_object.RobotDesigner.worldOpenSim, "accuracy")
            row = sub_box.row()
            row.prop(
                context.active_object.RobotDesigner.worldOpenSim,
                "max_transient_velocity",
            )

            contact = SimbodyBox.get(sub_box, context, "Contact")
            if contact:
                row = contact.row()
                row.prop(context.active_object.RobotDesigner.worldOpenSim, "stiffness")
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldOpenSim, "dissipation"
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldOpenSim,
                    "plastic_coef_restitution",
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldOpenSim,
                    "plastic_impact_velocity",
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldOpenSim, "static_friction"
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldOpenSim, "dynamic_friction"
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldOpenSim, "viscous_friction"
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldOpenSim,
                    "override_impact_capture_velocity",
                )
                row = contact.row()
                row.prop(
                    context.active_object.RobotDesigner.worldOpenSim,
                    "override_stiction_transition_velocity",
                )

        # Display robots that are included in the world
        box_robots = layout.box()
        box_robots.label(text="Robots")
        box_robots.menu(menus.AddRobotMenu.bl_idname, text=menus.AddRobotMenu.bl_label)
        robot_list = context.active_object.RobotDesigner.worlds.robot_list
        bots = [
            obj
            for obj in context.scene.objects
            if obj.type == "ARMATURE" and obj.name in robot_list
        ]

        for bot in bots:
            row = box_robots.row(align=True)
            row.label(text=bot.name)
            row.prop(
                context.active_object.RobotDesigner.worlds.robot_list[bot.name],
                "export",
            )
            world.RemoveRobot.place_button(
                row, text="remove", icon="CANCEL"
            ).robot_name = bot.name

    # Display menu to export/import a world
    box_sdf = layout.box()
    box_sdf.label(text="Import/Export SDF")
    if world_selected:
        row = box_sdf.row(align=True)
        row.prop(
            context.active_object.RobotDesigner.worlds,
            "export_name",
            text="Export Filename",
        )
        sdf_world_export.ExportPlainWorld.place_button(box_sdf, text="Export World SDF")
    sdf_world_import.ImportPlainWorld.place_button(box_sdf, text="Import World SDF")


def check_world(context):
    """
    Helper function that checks whether a :ref:'world' is selected.

    :param context: Blender contet
    :return: Whether a world is selected (Bool).
    """
    if (
        context.active_object is not None
        and context.active_object.RobotDesigner.tag == "WORLD"
    ):
        return True
    else:
        return False

