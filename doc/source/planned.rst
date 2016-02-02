Roadmap
=======

Planned features
----------------

- Override splash screen / modify gui (C coding separated Blender build) (? SP)
  `info<http://blender.stackexchange.com/questions/7055/creating-own-editor-type>`_
- Add debugger to Blender development (5SP)
- Better Blender stubs (2SP)
- Better methods for property handling (2SP)
- custom icons (HBP, NRP) (3SP)
- Mesh generation (8 SP)
- More selecting and view option (modal operators) (5SP)
- Resource loading (3 SP)
- Storage with NRP (?SP)
- Storage with GIT (?SP)
- Mass/Inertia revised (13 SP)
- SDF / Collada support (>=21 SP / 21 SP)
- Muscle / tendon support (? SP)
- Deformable meshes export (2 SP)
- Gazebo package installation (8 SP)
- Mannequin improvements (involves defining new skins for Makehuman) (8? SP)
- User documentation
- Videos / Tutorials
- Developer documentation polish
- Jenkins Pep8/Pylint/MyPy/..
- launch URDF from gazebo `see this page<http://gazebosim.org/tutorials?tut=ros_roslaunch>`_ and `here
<http://projects.csail.mit.edu/pr2/wiki/index.php?title=Launching_Locally>`_




Make a dedicated *editor type* for the Robot designer
-----------------------------------------------------

Currently, this can only be done in C code right now. See `this tutorial <http://wiki.blender.org/index.php/Dev:2.6/Source/Tutorials/AddAnEditor>`_
for more details. Even in the development version of Blender `this seems not be to be possible (yet) <https://www.blender.org/api/blender_python_api_2_75_release/info_quickstart.html>`_.

Custom icons
------------

This became possible in the newest `version of Blender <http://blender.stackexchange.com/questions/32335/how-to-implement-custom-icons-for-my-script-addon>`_.

