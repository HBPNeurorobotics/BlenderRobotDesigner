Usage
=====

Blender
-------

Blender is a feature-rich and very powerful 3D modelling software. For this reason, however,
learning how to use this software can be challenging for the beginner. The RobotDesigner plugin
intends to improve the user experience as much as possible---a basic understanding of the user face and
controls of Blender is mandatory. At this point, we would like to refer to a large set of
tutorials provided on this matter which can be found `here <https://www.blender.org/support/tutorials/>`_ for instance.

The RobotDesigner
-----------------

Panel Overview
^^^^^^^^^^^^^^

The Robot properties tab
************************

.. figure:: images/robot_example.png
    :align: center

    The Robot properties tab of the NRP RobotDesigner

The Robot properties tab allows us to create a new robot model or select an existing one. Hier we can also rename
it or merge with another model. New segments for expanding the robot model can be created and deleted here as well.
These segments are called *bones* in blender.

The Segments properties tab
***************************

.. figure:: images/segments_example.png
    :align: center

    The Segments properties tab of the NRP RobotDesigner

In the Segments properties tab we can modify the properties of the previously created segments by setting joint type,
joint limits, orientation and position in relation to the parent bone.

The Geometries properties tab
*****************************

.. figure:: images/geometries_example_expanded.png
    :align: center

    The Geometries properties tab of the NRP RobotDesigner

The Geometries properties tab allows us to connect the kinematics model or armature created by the NRP RobotDesigner with
an existing geometrical model, generate such a model or disconnect it once it has been attached.

The Sensors properties tab
**************************

.. figure:: images/sensors_empty.png
    :align: center

    The Sensors properties tab of the NRP RobotDesigner

The Tools properties tab
************************

.. figure:: images/tools_empty.png
    :align: center

    The Tools properties tab of the NRP RobotDesigner

The Files properties tab
************************

.. figure:: images/files_example.png
    :align: center

    The Files properties tab of the NRP RobotDesigner

Here we can export the created robot model as a an URDF file/package or import a robot model from an URDF file/package.

Creating and maintaining robot models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/robot_example.png
    :align: center

    The robot properties tab in the NRP RobotDesigner.

.. figure:: gifs/create_new_model.gif
    :align: center

    Creating a new armature.

In order to use the Robot Designer, one has first to create a blank robot model instance.
Note that, in Blender, such robot models are called *armatures*. Through the enrichment by additional
properties related to robotics they are  interpreted as robot models.

In the RobotDesigner, there is a tab for modifying the *robot model* (see figure). In there, you can
modify the name of the robot model, merge it with another model. In there, you can also modify the
structure of the kinematics such as adding new / deleting segments, reparent segments (move them to a different position
in the kinematics tree) and modify the names.

You can also assign different visualizations of coordinate frames (blender objects) for a more cleaned up look.



Creating Robot Joint/links
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/segments_example.png
    :align: center

    The kinematics settings in the segments properties tab of the NRP RobotDesigner.

.. figure:: images/dynamics_example.png
    :align: center

    The dynamics settings in the segments properties tab of the NRP RobotDesigner.

.. figure:: images/controller_example_expanded.png
    :align: center

    The controller settings in the segments properties tab of the NRP RobotDesigner.

.. figure:: gifs/create_child_bone.gif
    :align: center

    Adding a new segment to an armature.

In the RobotDesigner, the smallest unit of a robot is a compound of a *joint* and a subsequent *link* called *segment*.
That way, it becomes easy to define forked kinematics such as anthropomorphic hands. Note that, in terms of Blender,
these are referred to as *bones*. Once a robot model has been created and selected, segments can be added
to the structure to create a tree-shaped kinematics in the *robots tab*.

To add a new segment go to the 'Segment structure' field, select a *parent bone* from the drop-down menu and click on
**Create new child Bone**. The new bone will be attached to the *parent bone*.
In this field you can rename and delete segments as well.

In the segments properties tab, you can modify the kinematic and dynamic properties as well as the settings for the
control software automatically assigned to the robot model when loaded into the *Neurorobotics Platform*.
The kinematics properties basically represent transformation to the following segment (i.e., its length and orientation
transformation from the parent), its rotation axis and the joint limits.
Dynamics are defined via mass objects (called *physics frames*) that represent a mass and an inertia tensor.
The controller properties include settings for maximal velocities, torques, etc. as well as the specification about
how the joint of the segment is to be controlled (e.g., position or velocity controlled).


Adding and removing geometric models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/geometries_example_expanded.png
    :align: center

    The geometrical model properties tab of the NRP RobotDesigner.

.. figure:: gifs/attach_meshes.gif
    :align: center

    Connecting the kinematics and geometrical models of a robot.

Geometric models are *meshes* that can be connected to a segment. In the *Geometries tab*. Modelling of meshes
requires knowledge on how to design with Blender. The RobotDesigner unfortunately cannot support the user
significantly with this task. However, existing models (e.g., those that are imported from standard CAD/Mesh file
formats) can be conveniently connected to the robot model using the interface provided by the RobotDesigner in
this tab.

In order to connect the kinematics model, created by the NRP RobotDesigner and the geometric model select the field
**Attach Geometry**. First select the segment to be attached on the left and the mesh it is to be attached to on the right.
Then click on **Assign selected geometry to active segment**.

In a similar way geometries can be easily disconnected in the field **Detach Geometry**. First select the mesh to be
disconneccted, then click on **Detach selected geometry**.
Alternatively all meshes can be disconnected at once by selecting **Detach all geometries**.


Import and export
^^^^^^^^^^^^^^^^^

.. figure:: images/files_example.png
    :align: center

    The file properties tab of the NRP RobotDesigner.

.. figure:: gifs/import_URDF_hollie_arm.gif
    :align: center

    Importing a robot model of Schunk robot arm from a plain URDF file

.. figure:: gifs/export_URDF_lauron.gif
    :align: center

    Exporting a robot model of the robot Lauron as a plain URDF file

One of the main strengths of the RobotDesigner is the possibility to import from and export to URDF files.
This is the file format the Neurorobotics Platform (or Gazebo/ROS in general) depends on. The file format
has been extended to support for controller definitions such that loading a finished model into the NRP does not
require the deployment of additional control software.

Note that, in order to load URDF models that use the ``package`` directive, the environment variable has to be
accessible in Blender (i.e., blender has to be invoked from a shell) or a model folder has to be specified
in the respective text box (which is also used for export).











