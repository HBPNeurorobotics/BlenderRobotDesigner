.. _installation:

Installation
============

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

Planned installer
^^^^^^^^^^^^^^^^^

Manual install (Unix)
---------------------

Replace ``<installed_blender_version>`` in below's instructions by the Blender version you got installed (e.g., ``2.77``)


Linux
^^^^^

.. code-block:: console

   user@hbp ~$ cd projects
   user@hbp ~/projects$ cd BlenderRobotDesigner/
   user@hbp ~/projects/BlenderRobotDesigner$ mkdir -p ~/.config/blender/<installed_blender_version>/scripts/addons/
   user@hbp ~/projects/BlenderRobotDesigner$ ln -s robot_designer_plugin ~/.config/blender/<installed_blender_version>/scripts/addons/

Mac Os X
^^^^^^^^

.. code-block:: console

   user@hbp ~$ cd projects
   user@hbp ~/projects$ cd BlenderRobotDesigner/
   user@hbp ~/projects/BlenderRobotDesigner$ mkdir -p ~/Library/Application\ Support/Blender/<installed_blender_version>/scripts/addons/
   user@hbp ~/projects/BlenderRobotDesigner$ ln -s robot_designer_pluting ~/Library/Application\ Support/Blender/<installed_blender_version>/scripts/addons/

Windows
^^^^^^^

Copy the folder ``robot_designer_plugin`` in the ``BlenderRobotDesigner`` folder to::

   C:\Documents and Settings\$USERNAME\AppData\Roaming\Blender Foundation\Blender\<installed_blender_version>\



