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
import pathlib

# Blender imports
import bpy

# Robot Designer imports
from ..properties.globals import global_properties


def create_thumbnail(toplevel_directory):
    """
    Create a rendered thumbnail file and export it.
    """

    print("Create and Export thumbnail")

    if bpy.data.scenes["Scene"].camera == None:
        print("No camera found, thumbnail creation not possible")
        return

    if global_properties.display_physics_selection.get(bpy.context.scene) == True:
        global_properties.display_physics_selection.set(bpy.context.scene, False)
    for ob in bpy.context.scene.objects:
        ob.hide_render = ob.hide_get()

    # set storing parameters
    bpy.data.scenes["Scene"].render.filepath = toplevel_directory + "/thumbnail.png"
    bpy.context.scene.render.resolution_x = 600
    bpy.context.scene.render.resolution_y = 600

    # render and save file
    bpy.ops.render.render(write_still=True, use_viewport=True)


def export_rqtez_publisher(
    topic_list,
    path_to_output_file,
    min_value,
    max_value,
    publish_interval_value,
    is_repeat_value,
):
    """
    helper function to export the yaml file for the rqt_ez_publisher
    :param topic_list: list of topics to generate
    :param path_to_output_file: yaml export location
    :param min_value: min value for all publisher
    :param max_value: max value for all publisher
    :param publish_intervall: publishing time intervall
    :param is_repeat_value: if true repeated publishing for all topics
    :return:
    """

    pathlib.Path(os.path.dirname(path_to_output_file)).mkdir(exist_ok=True)

    with open(path_to_output_file, "w+") as output_file:
        string = "publish_interval: " + str(publish_interval_value) + "\n"
        output_file.write(string)
        string = "settings: \n"
        output_file.write(string)
        for topic_name in topic_list:
            string = (
                "  "
                + topic_name
                + ": {is_repeat: "
                + is_repeat_value
                + ", min: "
                + str(min_value)
                + ", max: "
                + str(max_value)
                + "}\n"
            )
            output_file.write(string)
        string = "texts: [" + ", ".join(topic_list) + "]\n"
        output_file.write(string)
    output_file.close()


def export_rqtez_publisher_muscle(toplevel_directory):
    """
    create and export an xml description for rqt_ez_publisher muscle actuation
    :param toplevel_directory:
    :return:
    """

    print("Export rqt_ez_publisher xml for muscles")

    # Parameters
    min_value = 0.0
    max_value = 1.0
    publish_interval_value = 100
    is_repeat_value = "false"
    path_to_output_file = os.path.join(
        toplevel_directory, "rqt/rqt_ez_pub_muscles.yaml"
    )
    model_name = global_properties.model_name.get(bpy.context.scene)

    muscles = [
        obj.name
        for obj in bpy.data.objects
        if obj.RobotDesigner.muscles.robotName
        == global_properties.model_name.get(bpy.context.scene)
    ]

    topic_list = [
        "/gazebo_muscle_interface/" + model_name + "/" + m + "/cmd_activation/data"
        for m in muscles
    ]

    if topic_list == []:
        print("No muscles found for rqt_ez_publisher")
        return

    # Write yaml file
    export_rqtez_publisher(
        topic_list=topic_list,
        path_to_output_file=path_to_output_file,
        min_value=min_value,
        max_value=max_value,
        publish_interval_value=publish_interval_value,
        is_repeat_value=is_repeat_value,
    )


def export_rqtez_publisher_controller(toplevel_directory):
    """
    create and export an xml description for rqt_ez_publisher joint controller actuation
    :param toplevel_directory:
    :return:
    """

    print("Export rqt_ez_publisher xml for joint controller")

    # Parameters
    min_value = -1.0
    max_value = 1.0
    publish_interval_value = 100
    is_repeat_value = "false"
    path_to_output_file = os.path.join(
        toplevel_directory, "rqt/rqt_ez_pub_jointcontroller.yaml"
    )

    model_name = global_properties.model_name.get(bpy.context.scene)
    controller_links = [
        obj
        for obj in bpy.data.objects[model_name].data.bones
        if obj.RobotDesigner.jointController.isActive
    ]

    topic_list_vel = [
        "/" + model_name + "/" + j.RobotDesigner.joint_name + "/cmd_vel/data"
        for j in controller_links
        if j.RobotDesigner.jointController.controllerType == "velocity"
    ]
    topic_list_pos = [
        "/" + model_name + "/" + j.RobotDesigner.joint_name + "/cmd_pos/data"
        for j in controller_links
        if j.RobotDesigner.jointController.controllerType == "position"
    ]

    topic_list = topic_list_pos + topic_list_vel

    if topic_list == []:
        print("No joint controller found for rqt_ez_publisher")
        return

    # Write yaml file
    export_rqtez_publisher(
        topic_list=topic_list,
        path_to_output_file=path_to_output_file,
        min_value=min_value,
        max_value=max_value,
        publish_interval_value=publish_interval_value,
        is_repeat_value=is_repeat_value,
    )


class RQT_Multiplot_Diagram:
    """
    Holds a rqt_multiplot diagram description
    """

    title_ = ""
    x_axis_description_ = ""
    y_axis_description_ = ""
    curve_titles = []
    rostopics_ = []
    fields_ = []
    types_ = []
    num_of_curves_ = 0

    def __init__(
        self,
        title,
        x_axis_description,
        y_axis_description,
        curve_titles,
        rostopics,
        fields,
        types,
    ):
        self.title_ = title
        self.x_axis_description_ = x_axis_description
        self.y_axis_description_ = y_axis_description
        self.curve_titles = curve_titles
        self.rostopics_ = rostopics
        self.fields_ = fields
        self.types_ = types
        self.num_of_curves_ = len(rostopics)


def export_rqt_multiplot(
    diagram_array, path_to_output_file, num_of_rows, num_of_columns, render_antialias
):
    """
    Create and export a rqt_multiplot configuration for the robot model

    TODO: change the code to use pyxb xml generation

    :param diagram_array: array of the diagram descriptions to be generated
    :param path_to_output_file: output file path
    :param num_of_rows: number of plot diagrams in a row
    :param num_of_columns: number of plot diagrams in a column
    :param render_antialias: antialias bool for all curves
    :return:
    """

    pathlib.Path(os.path.dirname(path_to_output_file)).mkdir(exist_ok=True)

    num_of_diagrams = len(diagram_array)

    # Write XML file
    with open(path_to_output_file, "w+") as output_file:
        # Start of file
        string = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            + "<rqt_multiplot>\n"
            + "    <table>\n"
            + "        <background_color>#000000</background_color>\n"
            + "        <foreground_color>#eeeeec</foreground_color>\n"
            + "        <link_cursor>false</link_cursor>\n"
            + "        <link_scale>false</link_scale>\n"
            + "        <plots>\n"
        )

        output_file.write(string)

        diagram_id = 0
        for row_id in range(num_of_rows):
            # Start of row for loop

            string = "\t\t\t<row_" + str(row_id) + ">\n"
            output_file.write(string)

            for column_id in range(num_of_columns):
                if diagram_id >= num_of_diagrams:
                    continue

                # Start of column for loop
                string = (
                    "\t\t\t\t<column_"
                    + str(column_id)
                    + ">\n"
                    + "\t\t\t\t\t<axes>\n"
                    + "\t\t\t\t\t\t<axes>\n"
                    + "\t\t\t\t\t\t\t<x_axis>\n"
                    + "\t\t\t\t\t\t\t\t<custom_title>"
                    + diagram_array[diagram_id].x_axis_description_
                    + "</custom_title>\n"
                    + "\t\t\t\t\t\t\t\t<title_type>0</title_type>\n"
                    + "\t\t\t\t\t\t\t\t<title_visible>true</title_visible>\n"
                    + "\t\t\t\t\t\t\t</x_axis>\n"
                    + "\t\t\t\t\t\t\t<y_axis>\n"
                    + "\t\t\t\t\t\t\t\t<custom_title>"
                    + diagram_array[diagram_id].y_axis_description_
                    + "</custom_title>\n"
                    + "\t\t\t\t\t\t\t\t<title_type>0</title_type>\n"
                    + "\t\t\t\t\t\t\t\t<title_visible>true</title_visible>\n"
                    + "\t\t\t\t\t\t\t</y_axis>\n"
                    + "\t\t\t\t\t\t</axes>\n"
                    + "\t\t\t\t\t</axes>\n"
                    + "\t\t\t\t\t<curves>\n"
                )
                output_file.write(string)

                for curve_id in range(diagram_array[diagram_id].num_of_curves_):
                    string = (
                        "\t\t\t\t\t\t<curve_"
                        + str(curve_id)
                        + ">\n"
                        + "\t\t\t\t\t\t\t<axes>\n"
                        + "\t\t\t\t\t\t\t\t<x_axis>\n"
                        + "\t\t\t\t\t\t\t\t\t<field></field>\n"
                        + "\t\t\t\t\t\t\t\t\t<field_type>1</field_type>\n"
                        + "\t\t\t\t\t\t\t\t\t<scale>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<absolute_maximum>1000</absolute_maximum>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<absolute_minimum>0</absolute_minimum>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<relative_maximum>0</relative_maximum>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<relative_minimum>-40</relative_minimum>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<type>2</type>\n"
                        + "\t\t\t\t\t\t\t\t\t</scale>\n"
                        + "\t\t\t\t\t\t\t\t\t<topic>"
                        + diagram_array[diagram_id].rostopics_[curve_id]
                        + "</topic>\n"
                        + "\t\t\t\t\t\t\t\t\t<type>"
                        + diagram_array[diagram_id].types_[curve_id]
                        + "</type>\n"
                        + "\t\t\t\t\t\t\t\t</x_axis>\n"
                        + "\t\t\t\t\t\t\t\t<y_axis>\n"
                        + "\t\t\t\t\t\t\t\t\t<field>"
                        + diagram_array[diagram_id].fields_[curve_id]
                        + "</field>\n"
                        + "\t\t\t\t\t\t\t\t\t<field_type>0</field_type>\n"
                        + "\t\t\t\t\t\t\t\t\t<scale>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<absolute_maximum>1000</absolute_maximum>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<absolute_minimum>0</absolute_minimum>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<relative_maximum>0</relative_maximum>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<relative_minimum>-1000</relative_minimum>\n"
                        + "\t\t\t\t\t\t\t\t\t\t<type>0</type>\n"
                        + "\t\t\t\t\t\t\t\t\t</scale>\n"
                        + "\t\t\t\t\t\t\t\t\t<topic>"
                        + diagram_array[diagram_id].rostopics_[curve_id]
                        + "</topic>\n"
                        + "\t\t\t\t\t\t\t\t\t<type>"
                        + diagram_array[diagram_id].types_[curve_id]
                        + "</type>\n"
                        + "\t\t\t\t\t\t\t\t</y_axis>\n"
                        + "\t\t\t\t\t\t\t</axes>\n"
                        + "\t\t\t\t\t\t\t<color>\n"
                        + "\t\t\t\t\t\t\t\t<custom_color>#000000</custom_color>\n"
                        + "\t\t\t\t\t\t\t\t<type>0</type>\n"
                        + "\t\t\t\t\t\t\t</color>\n"
                        + "\t\t\t\t\t\t\t<data>\n"
                        + "\t\t\t\t\t\t\t\t<circular_buffer_capacity>1000</circular_buffer_capacity>\n"
                        + "\t\t\t\t\t\t\t\t<time_frame_length>10</time_frame_length>\n"
                        + "\t\t\t\t\t\t\t\t<type>0</type>\n"
                        + "\t\t\t\t\t\t\t</data>\n"
                        + "\t\t\t\t\t\t\t<style>\n"
                        + "\t\t\t\t\t\t\t\t<lines_interpolate>false</lines_interpolate>\n"
                        + "\t\t\t\t\t\t\t\t<pen_style>1</pen_style>\n"
                        + "\t\t\t\t\t\t\t\t<pen_width>1</pen_width>\n"
                        + "\t\t\t\t\t\t\t\t<render_antialias>"
                        + render_antialias
                        + "</render_antialias>\n"
                        + "\t\t\t\t\t\t\t\t<steps_invert>false</steps_invert>\n"
                        + "\t\t\t\t\t\t\t\t<sticks_baseline>0</sticks_baseline>\n"
                        + "\t\t\t\t\t\t\t\t<sticks_orientation>2</sticks_orientation>\n"
                        + "\t\t\t\t\t\t\t\t<type>0</type>\n"
                        + "\t\t\t\t\t\t\t</style>\n"
                        + "\t\t\t\t\t\t\t<subscriber_queue_size>100</subscriber_queue_size>\n"
                        + "\t\t\t\t\t\t\t<title>"
                        + diagram_array[diagram_id].curve_titles[curve_id][0]
                        + "</title>\n"
                        + "\t\t\t\t\t\t</curve_"
                        + str(curve_id)
                        + ">\n"
                    )
                    output_file.write(string)


                # End of column for loop
                string = (
                    "\t\t\t\t\t</curves>\n"
                    + "\t\t\t\t\t<legend>\n"
                    + "\t\t\t\t\t\t<visible>true</visible>\n"
                    + "\t\t\t\t\t</legend>\n"
                    + "\t\t\t\t\t<plot_rate>30</plot_rate>\n"
                    + "\t\t\t\t\t<title>"
                    + diagram_array[diagram_id].title_
                    + "</title>\n"
                    + "\t\t\t\t</column_"
                    + str(column_id)
                    + ">\n"
                )
                output_file.write(string)

                diagram_id += 1


            # End of row for loop
            string = "\t\t\t</row_" + str(row_id) + ">\n"
            output_file.write(string)

        # End of file
        string = (
            "        </plots>\n"
            + "        <track_points>false</track_points>\n"
            + "    </table>\n"
            + "</rqt_multiplot>"
        )

        output_file.write(string)


def export_rqt_multiplot_muscles(toplevel_directory):
    """
    Export a rqt_multiplot configuration for muscles

    :param toplevel_directory: model directory to export configuration in
    :return:
    """

    print("Export rqt_multiplot xml for muscles")

    # Set parameters
    path_to_output_file = os.path.join(
        toplevel_directory, "rqt/rqt_multiplot_muscles.xml"
    )
    model_name = global_properties.model_name.get(bpy.context.scene)

    muscles = [
        obj.name
        for obj in bpy.data.objects
        if obj.RobotDesigner.muscles.robotName
        == global_properties.model_name.get(bpy.context.scene)
    ]

    topic_list = [
        "/gazebo_muscle_interface/" + model_name + "/" + m + "/cmd_activation"
        for m in muscles
    ]
    muscle_number = len(topic_list)

    num_of_rows = 2
    num_of_columns = 2
    render_antialias = "true"

    # Create an array of Diagram instances
    diagram_array = []
    diagram = RQT_Multiplot_Diagram(
        "Muscle Actuation",
        "time",
        "actuation",
        ["m" + str(i) for i in range(0, muscle_number)],
        topic_list,
        muscle_number * ["data"],
        muscle_number * ["Float64"],
    )
    diagram_array.append(diagram)

    for sensor in ["length", "lengthening_speed", "force"]:
        diagram = RQT_Multiplot_Diagram(
            "Muscle Sensors " + sensor,
            "time",
            sensor,
            muscles,
            muscle_number
            * ["/gazebo_muscle_interface/" + model_name + "/muscle_states"],
            ["muscles/" + str(i) + "/" + sensor for i in range(0, muscle_number)],
            muscle_number * ["gazebo_ros_muscle_interface/MuscleStates"],
        )
        diagram_array.append(diagram)

    export_rqt_multiplot(
        diagram_array=diagram_array,
        path_to_output_file=path_to_output_file,
        num_of_rows=num_of_rows,
        num_of_columns=num_of_columns,
        render_antialias=render_antialias,
    )


def export_rqt_multiplot_jointcontroller(toplevel_directory):
    """
    Export a rqt_multiplot configuration for joints

    :param toplevel_directory: model directory to export configuration in
    :return:
    """

    print("Export rqt_multiplot xml for joint controller")

    # Set parameters
    path_to_output_file = os.path.join(
        toplevel_directory, "rqt/rqt_multiplot_jointcontroller.xml"
    )

    model_name = global_properties.model_name.get(bpy.context.scene)
    controller_links = [
        obj
        for obj in bpy.data.objects[model_name].data.bones
        if obj.RobotDesigner.jointController.isActive
    ]

    topic_list_vel = [
        "/" + model_name + "/" + j.RobotDesigner.joint_name + "/cmd_vel"
        for j in controller_links
        if j.RobotDesigner.jointController.controllerType == "velocity"
    ]
    topic_list_pos = [
        "/" + model_name + "/" + j.RobotDesigner.joint_name + "/cmd_pos"
        for j in controller_links
        if j.RobotDesigner.jointController.controllerType == "position"
    ]

    topic_list = topic_list_vel + topic_list_pos
    joint_number = len(topic_list)

    if topic_list == []:
        print("No joint controller found for rqt_multiplot")
        return

    num_of_rows = 4
    num_of_columns = 1
    render_antialias = "true"

    # Create an array of Diagram instances
    diagram_array = []
    diagram = RQT_Multiplot_Diagram(
        "Joint Actuation",
        "time",
        "actuation",
        topic_list,
        topic_list,
        joint_number * ["data"],
        joint_number * ["Float64"],
    )
    diagram_array.append(diagram)

    for sensor in ["position", "velocity", "effort"]:
        diagram = RQT_Multiplot_Diagram(
            "Joint Sensors " + sensor,
            "time",
            sensor,
            [topic_list],
            joint_number * ["/" + model_name + "joint_states"],
            [sensor + "/" + str(i) for i in range(0, joint_number)],
            joint_number * ["sensor_msgs/JointStates"],
        )
        diagram_array.append(diagram)

    export_rqt_multiplot(
        diagram_array=diagram_array,
        path_to_output_file=path_to_output_file,
        num_of_rows=num_of_rows,
        num_of_columns=num_of_columns,
        render_antialias=render_antialias,
    )
