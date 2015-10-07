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

Creating and maintaining robot models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. figure:: images/RobotTab.png
    :align: center

    The robot properties tab in the NRP RobotDesigner.

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

.. figure:: images/SegmentsTab.png
    :align: center

    The kinematics settings in the segments properties tab of the NRP RobotDesigner.

.. figure:: images/SegmentsTab2.png
    :align: center

    The dynamics settings in the segments properties tab of the NRP RobotDesigner.

.. figure:: images/SegmentsTab3.png
    :align: center

    The controller settings in the segments properties tab of the NRP RobotDesigner.


In the RobotDesigner, the smallest unit of a robot is a compound of a *joint* and a subsequent *link* called *segment*.
That way, it becomes easy to define forked kinematics such as anthropomorphic hands. Note that, in terms of Blender,
these are referred to as *bones*. Once a robot model has been created and selected, segments can be added
to the structure to create a tree-shaped kinematics in the *robots tab*.

In the segments properties tab, you can modify the kinematic and dynamic properties as well as the settings for the
control software automatically assigned to the robot model when loaded into the *Neurorobotics Platform*.
The kinematics properties basically represent transformation to the following segment (i.e., its length and orientation
transformation from the parent), its rotation axis and the joint limits.
Dynamics are defined via mass objects (called *physics frames*) that represent a mass and an inertia tensor.
The controller properties include settings for maximal velocities, torques, etc. as well as the specification about
how the joint of the segment is to be controlled (e.g., position or velocity controlled).


Adding geometric models
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/GeometriesTab.png
    :align: center

    The geometrical model properties tab of the NRP RobotDesigner.

Geometric models are *meshes* that can be connected to a segment. In the *Geometries tab*. Modelling of meshes
requires knowledge on how to design with Blender. The RobotDesigner unfortunately cannot support the user
significantly with this task. However, existing models (e.g., those that are imported from standard CAD/Mesh file
formats) can be conveniently be connected to the robot model using the interface provided by the RobotDesigner in
this tab.


Import and export
^^^^^^^^^^^^^^^^^

.. figure:: images/FilesTab.png
    :align: center

    The file properties tab of the NRP RobotDesigner.

One of the main strengths of the RobotDesigner is the possibility to import from and export to URDF files.
These is the file format the Neurorobotics Platform (or Gazebo/ROS in general) depends on. The file format
has been extended to support for controller definitions such that loading a finished model into the NRP does not
require the deployment of additional control software.

Note that, in order to load URDF models that use the ``package`` directive, the environment variable has to be
accessible in Blender (i.e., blender has to be invoked from a shell) or a model folder has to be specified
in the respective text box (which is also used for export).

.. todo::

    Improve the part of the documentation describing the GIT elements once the method of file upload has been clarified.

