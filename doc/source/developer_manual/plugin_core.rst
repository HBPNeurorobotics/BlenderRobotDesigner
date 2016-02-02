The Plugin Core
===============

Introduction
------------

The core of the *HBP/NRP RobotDesigner* is a package located at :mod:`robot_designer_plugin.core`.

.. automodule:: robot_designer_plugin.core
    :members:
    :undoc-members:
    :show-inheritance:

.. _blender_concepts:

Blender concepts
----------------

Blender uses special terminology when developing plugins. Whenever possible, this documentation links to the official
`Blender API documentation <https://www.blender.org/api/blender_python_api_current/contents.html>`_
and `Blender user manual <https://www.blender.org/manual/>`_.

Operators
    All functionality that modifies a :term:`scene` in Blender is (or at least, should be) encapsulated in
    :term:`operators<operator>`. These are Python class objects with methods which implement the desired functionality.
    In addition, operators can be added as buttons to a GUI defined by the plugin.

    These classes have to be *registered* to Blender, that is, Blender adds the functionality to its namespace (under
    a different name). This concept is makes it difficult to exploit the full power provided by modern
    :term:`IDEs<IDE>` which offer auto completion, introspection and refactoring.
    This gap is filled by the :class:`robot_designer_plugin.core.operators.RDOperator` class. See its documentation
    for information and examples on how to use it. All functionality in the RobotDesigner is supposed to be
    encapsulated in classes derived from it.

Objects
    All entitis in a :term:`scene` are :class:`bpy.types.Object` in Blender. Their possible types (that is
    their associated :attr:`bpy.types.Object.data`) include

    Armatures (:class:`bpy.types.Armature`)
        Skeleton-based articulated objects. In the RobotDesigner they are referred to as (*kinematic* or *robot*)
        *models*. They include nested data objects called *bones* (:attr:`bpy.types.Armature.bones`) which define
        the kinematic structure of the articulated object. In the RobotDesigner, they are referred to as *segments*.
        See section :ref:`segments` in the user manual)

    Meshes (:class:`bpy.types.Mesh`)
        Mesh objects have assiciated 3D data in form of connected vertices that define a *surface* in form of
        polygonial meshes. In the Robot designer, they are referred to (*rigid body*) *geometries*.

    Empty (no data assiciated):
        Can be used to mark coordinate frames. The RobotDesigner uses them to mark the :term:`pose` of mass
        distributions for instance.

    Lights, Camera, etc:
        Various other object types exist that are of no special interest for the RobotDesigner.

    Various Operators defined in the RobotDesigner act upon these objects and are describe blow and in the :ref:`api`.

Properties
    All values / structures that should be stored in the *current* file have to be stored in classes derived from
    :class:`bpy.types.Property`. They can be inserted as input fields in a GUI defined in the plugin.

    There are different predefined types for common data types (e.g.,
    :class:`bpy.types.StringProperty` and :class:`bpy.types.FloatProperty`) but also structures can be user-defined
    by subclasses of :class:`bpy.types.PropertyGroup` which have to be registered to Blender when the plugin is loaded.
    Properties must be associated with objects. That way, *global* properties are associated with the current
    *scene object* (of type :class:`bpy.types.Scene` in :attr:`bpy.context.scene`), information about models are
    with *armature object* and segment specifications with *bone data*.

    Facilities for registering user-defined data structures are provided by the
    :class:`robot_designer_plugin.core.pluginmanager.Pluginmanager` class in the core package.

Panels
    Panels (:class:`bpy.types.Panel`) represent a *canvas* where a plugin can place its GUI elements on. Like all
    classes that should be usable by Blender, these have to be registered as well on plugin initialization.
    In the :meth:`bpy.types.Panel.draw` the GUI elements, different graphical types of elements can be placed:

    - Static: e.g. labels, boxes, icons, etc.
    - Properties: Registered properties can be used to enable user input (e.g., check boxes
      (:class:`bpy.types.BoolProperty`), or numerical value fields)
    - Operators: Are represented as buttons that executes the operator's functionality on button press.

    The elements are defined *sequentially*, that is, they are described in the order they should appear. Support
    for column and row layouts are given.
    In the :mod:`robot_designer_plugin.core.gui` module some additional classes are given that help defining a gui.
    Currently, these are collapsible boxes and automatic display of status messages of operators.

.. _core_templates:

Suggested plugin structure and templates
----------------------------------------

A plugin using the core should be structured as follows.

::

    <plugin_name>/
    ├── LICENSE  (A text file describing the licence you are using)
    ├── README.md (A readme file describing the plugin)
    ├── __init__.py (The plugin intialization)
    ├── core (The core package)
    │   ├── __init__.py
    │   ├── conditions.py
    │   ├── config.py
    │   ├── gui.py
    │   ├── logfile.py
    │   ├── operators.py
    │   ├── pluginmanager.py
    │   ├── property.py
    │   └── resources.py
    ├── interface ((suggested) organize your gui files in separate submodules in a separate package)
    │   ├── __init__.py
    │   ├── <submodule1>.py
    │   └── <submodule2>.py
    ├── operators ((suggested) organize your operators in separate submodules in a separate package)
    │   ├── __init__.py
    │   ├── <submodule3>.py
    │   └── <submodule4>.py
    ├── properties ((suggested) organize your properties in separate submodules in a separate package)
    │   ├── __init__.py
    │   ├── <submodule5>.py
    │   └── <submodule6>.py
    └── resources (place ressource blend files and additional material (e.g., templates for export) as well as additional python packages
        ├── blender_api (can be autogenerated)
        └── log.txt


A template for the toplevel ``__init__.py`` should look like this (in order to allow for reloading which is
recommended for development:

.. literalinclude:: ../../../resources/templates/__init__.py
    :lines: 19-
    :linenos:

A template for the sub-packages ``__init__.py`` should look like this.

.. literalinclude:: ../../../resources/templates/submodule__init__.py
    :lines: 37-
    :linenos:

Other templates are given in the module and class descriptions linked in the next section.
They can also be found in the RobotDesigner repository in the ``resources/templates/`` directory.

API reference
-------------

How to use the classes and the core framework package can be seen in the :ref:`core_template` section and in the
reference. It is suggested to read the documentation of all sub modules and classes before you start writing
your own plugin or add additional functionality to the RobotDesigner.


.. toctree::
   :maxdepth: 4

   ../apidoc/robot_designer_plugin.core.conditions
   ../apidoc/robot_designer_plugin.core.config
   ../apidoc/robot_designer_plugin.core.gui
   ../apidoc/robot_designer_plugin.core.logfile
   ../apidoc/robot_designer_plugin.core.operators
   ../apidoc/robot_designer_plugin.core.pluginmanager
   ../apidoc/robot_designer_plugin.core.property
   ../apidoc/robot_designer_plugin.core.resources





