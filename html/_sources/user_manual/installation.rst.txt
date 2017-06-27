.. _manual_install:

Manual Installation
===================

Get a copy
----------

The RobotDesigner of the *HBP-SP10: Neurorobotics* is hosted on
`GitHUB <https://github.com/HBPNeurorobotics/BlenderRobotDesigner>`_ and its newest version can be downloaded
as a zipped file from `here <https://github.com/HBPNeurorobotics/BlenderRobotDesigner/archive/master.zip>`_, or
if the GIT version control system is installed, like this:

.. code-block:: console

   user@hbp ~$ cd projects
   user@hbp ~/projects $ git clone https://github.com/HBPNeurorobotics/BlenderRobotDesigner.git
   user@hbp ~/projects$ cd BlenderRobotDesigner/


Installer
---------

Current
^^^^^^^
Currently, the installer is disabled and in the process
of development for simplification and reflect new dependencies on external software.
Please refer to the :ref:`manual installation <manual_install>` for now.

Planned installer
^^^^^^^^^^^^^^^^^

For the next version of the installer, we investigate the usage of the ``venv`` environment shipped with
Python starting from version 3.3, which will allow the installation of external (pure python) packages to
a Blender.

Manual install (Unix)
---------------------

Replace ``<installed_blender_version>`` in below's instructions by the Blender version you got installed (e.g., ``2.77``)


Linux
^^^^^

.. code-block:: console

   user@hbp ~$ cd projects
   user@hbp ~/projects$ cd BlenderRobotDesigner/
   user@hbp ~/projects/BlenderRobotDesigner$ mkdir -p ~/.config/blender/<installed_blender_version>/scripts/addons/
   user@hbp ~/projects/BlenderRobotDesigner$ ln -s $PWD/robot_designer_plugin ~/.config/blender/<installed_blender_version>/scripts/addons/

Mac Os X
^^^^^^^^

.. code-block:: console

   user@hbp ~$ cd projects
   user@hbp ~/projects$ cd BlenderRobotDesigner/
   user@hbp ~/projects/BlenderRobotDesigner$ mkdir -p ~/Library/Application\ Support/Blender/<installed_blender_version>/scripts/addons/
   user@hbp ~/projects/BlenderRobotDesigner$ ln -s $PWD/robot_designer_pluting ~/Library/Application\ Support/Blender/<installed_blender_version>/scripts/addons/

Windows
^^^^^^^

Copy the folder ``robot_designer_plugin`` in the ``BlenderRobotDesigner`` folder to::

   C:\Documents and Settings\$USERNAME\AppData\Roaming\Blender Foundation\Blender\<installed_blender_version>\



