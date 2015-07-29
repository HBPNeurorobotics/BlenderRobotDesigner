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

Creating robot models
^^^^^^^^^^^^^^^^^^^^^

In order to use the Robot Designer, one has first to create a blank robot model instance.
In Blender, such robot models are called *armatures*. Through the enrichment by additional
properties related to robotics they are  interpreted as robot models.

.. todo::

    Rename every term *armature* to *robot model.*

.. todo::

    Improve this part of the documentation.

Creating Joint/links
^^^^^^^^^^^^^^^^^^^^

In the RobotDesigner, the smallest unit of a robot is a compound of a *joint* and a subsequent *link*.
That way, it becomes easy to define forked kinematics such as anthropomorphic hands. In terms of Blender,
these are referred to as *bones*. Once a robot model has been created and selected, bones can be added
to the structure to create a tree-shaped kinematics.

.. todo::

    Rename every term *bone* to *joint-link*.

.. todo::

    Improve this part of the documentation.

Connecting geometric models
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Geometric models are meshes that can be connected to a joint/link compound.

.. todo::

    Improve this part of the documentation.

Adding physics frames
^^^^^^^^^^^^^^^^^^^^^

A physics frame represents a mass distribution and is composed of a center of mass (the origin of the coordinate
frame) a mass distribution along its main axes, and an overall weight. Similar to geometric models, a physics frame
can be assigned to a joint/link compound.

Adding sensors
^^^^^^^^^^^^^^

.. todo::

    Improve this part of the documentation.

Adding controllers
^^^^^^^^^^^^^^^^^^

.. todo::

    Improve this part of the documentation.

Import and export
^^^^^^^^^^^^^^^^^

.. todo::
    Improve this part of the documentation.



GIT connection
^^^^^^^^^^^^^^

.. todo::

    Improve this part of the documentation.

Manipulating robot models
^^^^^^^^^^^^^^^^^^^^^^^^^

Merging and separating robot models.

.. todo::

    Improve this part of the documentation.
