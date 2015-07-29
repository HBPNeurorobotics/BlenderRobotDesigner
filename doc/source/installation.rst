Installation
============

Get a copy
----------

The NRP RobotDesigner is currently hosted at the EPFL server and will be migrated to an open repository in the
near future. To obtain a copy you need to have the distributed version control system `GIT <https://git-scm.com/>`_
installed on your system. On Mac/Linux, run the following command:

.. code-block:: bash

    git clone ssh://ulbrich@bbpcode.epfl.ch/neurorobotics/RobotDesigner

Installation
------------

The RobotDesigner is a plugin for the `Blender 3D modelling suite <http://blender.org>`_ written in Python.
So far, there are no dependencies on external packages not shipped with blender.

.. warning::

    This will change in the near future as `lxml` package and GIT access have to be included. These will be binary
    packages so the installation process will be more complex (OS and blender version dependent)

.. note::

    Installation will be done in the future by executing a Python script included in a `.blend` file. There will
    no manual shell scripts be necessary.
    The installation procedure so far is described in the following.

To install the plugin, it must be copied (or linked) into the blender add-on folder of a local user (or in the global
installation directory which is discouraged)

Linux
^^^^^

To create a link run the following command at the root of your GIT repository

.. code-block:: bash

    RobotDesigner$> ln -s "$PWD"/robot_designer_plugin ~/﻿.config/blender/<Blender_version>/scripts/addons/

where `<Blender_version>` refers to the version of your blender installation (e.g., `2.69`, `2.74` etc).

Mac OS X
^^^^^^^^

To create a link run the following command at the root of your GIT repository

.. code-block:: bash

    RobotDesigner$> ln -s "$PWD"/robot_designer_plugin ~/Library/Application\ Support/Blender/<Blender_version>/scripts/addons/

where `<Blender_version>` refers to the version of your blender installation (e.g., `2.69`, `2.74` etc).

Windows
^^^^^^^

.. todo::

    Document windows installation


Activation
----------

The plugin has to be enabled in blender before it can be used. To do so open the `File` menu in the top bar (in the
default file) and select `User Preferences`. In the appearing window select the `Add-ons` tab and enter
`NRP RobotDesigner` (the first letters should suffice) into the box. Enable the checkbox to load the plugin and
save the settings by clicking on `Save User Settings`.

The plugin should appear on a panel left on the `3D view` window under the `Misc` tab. If this panel is not visible
hit the `t` key while the mouse is over the `3D view` window (key events are always passed to the window under the
mouse pointer only).
The procedure is depicted in the below figure.

.. note::
    The activation process will be automated by the future installation script.

.. figure:: images/install.png
   :align: center

   Screenshot of how to activate the plugin.


