Debugging
=========

Logging output is generated in order to debug the Robot Designer. The debugging
level can be selected in the *Files* pane of the Robot Designer user interface in
Blender. Generic logging can be found in the terminal Blender is started from.
Additionally, all logging is saved to file which can be found depending on your
operating system in:

Linux
"""""

.. code-block:: console

   ~/.config/blender/<installed_blender_version>/scripts/addons/robot_designer_plugin/resources/log.txt

Mac Os X
""""""""

.. code-block:: console

   ~/Library/Application\ Support/Blender/<installed_blender_version>/scripts/addons/robot_designer_plugin/resources/log.txt

Windows
"""""""

.. code-block:: console

   C:\Documents and Settings\$USERNAME\AppData\Roaming\Blender Foundation\Blender\<installed_blender_version>\scripts\addons\robot_designer_plugin/resources/log.txt





An example log output is depicted below:

.. literalinclude:: log_example.txt
