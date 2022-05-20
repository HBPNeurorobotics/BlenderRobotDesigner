The BlenderRobotDesigner of the Neurorobotics Platform (NRP)
============================================================

Introduction
------------

Welcome
^^^^^^^

This is the documentation of the RobotDesigner belonging to the *Neurorobotics Platform (NRP)* of the
`Human Brain Project (HBP) <https://www.humanbrainproject.eu>`_ developed in the
`sub-project Neurorobotics <http://neurorobotics.net/>`_.
It is realized as a plugin for the `Blender 3D modeling suite <http://blender.org>`_ written in the Python language.
This document provides information about the plugin, its installation, its features and usage, as well as the
programming reference for developers.

About
~~~~~

The *NRP RobotDesigner* software developed in the scope of the `Human
Brain Project <https://www.humanbrainproject.eu>`__ in the sub-project
`SP10 Neurorobtics <http://neurorobotics.net/>`__. It is part
of the *Neurorobotics Platform* which aims at providing easy accessible
and usable tools to neuro-scientists and neuro-roboticists for
simulating robots that are controlled by artificial brains in virtual
environments. The *RobotDesinger* is a modeling tool that allows to
generate *geometric*, *kinematic* and *dynamic* models, and sensor
placement that can be used in the simulation environment of NRP–or any
ROS/Gazebo-based environment. While other services of the NRP are
created as web-based services that do not require installation and,
therefore, administration expertise, the *RobotDesigner* is a plugin for
the freely available (GPL licensed) `Blender 3D modeling
suite <http://blender.org>`__. This design decision has been made due to
three reasons:

1. The full capabilities of a feature-rich modeling suite such as
   Blender is an enormous undertaking.
2. Robot design is a process that requires advanced engineering
   expertise and is time consuming justifying a more complex
   installation process and interruption of the web-based workflow.
3. Blender is freely available for a wide range of platforms and
   installation is very easy.
4. It is easily extendible.

Under the hood, the plugin extends the built-in data types and provides
an improved and clear interface to the modeling software. Future
development plans of the robot designer, however, include provide a
simplified web-based interface integrated into the NRP to construct
robots from building blocks. Therefore, the code base of the standalone
software is planned to be used and will be further maintained.

The RobotDesigner project was started under the lead
of the `Intelligent Systems and Production Engineering
department <http://www.fzi.de/en/about-us/organisation/research-divisions/ispe/>`__
of the `FZI Forschungszentrum Informatik <http://www.fzi.de/en/home/>`__
in Karlsruhe. Currently the RobotDesigner is developed and maintained towards NRP
compliance and biomimetic robot design capabilities under the lead of
`Benedikt Feldotto <http://www6.in.tum.de/en/people/benedikt-feldotto-msc/>`__ at
the `Chair of Robotics, Artificial Intelligence and Real-Time Systems
<http://www6.in.tum.de/en/home/>`__ at Technical University of Munich.

History
^^^^^^^

The foundations of the *NRP RobotDesigner* has been initially developed
under the name *OpenGRASP RobotEditor* from 2008-2012 at the `Humanoids
and Intelligence Systems Lab (HIS) at the Institute for Anthropomatics
and Robotics
(IAR) <http://his.anthropomatik.kit.edu/english/index.php>`__ of the
`Karlsruhe Institute of
Technology <http://www.kit.edu/english/index.php>`__ during the
`European GRASP
project <http://www.csc.kth.se/grasp/>`_ [#]_ [#]_
as port of the `OpenGRASP
software <http://opengrasp.sourceforge.net/>`__. This simulation
environment has been published under the `GPL
v2 <http://www.gnu.org/licenses/gpl-2.0.html>`__ license. This Python
plugin restricted to the Blender version 2.49 was mainly developed by
`Stefan Ulbrich (FZI) <mailto:stefan.ulbrich@fzi.de>`__. One of the most
notable features of the *RobotEditor* was support for the `Collada
v1.5 <https://www.khronos.org/collada/>`__ data 3D asset exchange
format. This file format has large support from the industry including
companies such as Daimler and Sony. The RobotEditor was the only freely
available tool creating valid models for Collada v1.5 which supported
the new description facilities for kinematics and dynamics.

Afterwards, the *RobotEditor* [#]_  has been completely
rewritten to comply the programming interface of newer Blender versions
(>2.69) at the `High Perfomance Humanoid Technologies Lab (H2T) at the
(IAR) <http://h2t.anthropomatik.kit.edu/enligsh/index.php>`__ of
`KIT <http://www.kit.edu/english/index.php>`__ by the main authors
`Michael Bechtel <mailto:michael.bechtel@kit.edu>`__ and `Stefan Ulbrich
(FZI) <mailto:stefan.ulbrich@fzi.de>`__. Many new feature such as
*physical properties*, *joint dynamics*, *sensors for matching motion
capture data* support for the `Simox robot
simulator <http://simox.sourceforge.net/>`__ [#]_  have been
added to the software. This software is still developed and available
`under the open source GPL
license <http://www.gnu.org/licenses/gpl-2.0.html>`__ from
`here <https://gitlab.com/h2t/roboteditor>`__.

The *NRP RobotDesigner* is a fork of the *RobotEditor*, which has been
chosen as the basis after a comparison to competing projects (e.g.,
`phobos <https://github.com/rock-simulation/phobos>`__). It will enrich
the existing project by components required for the NRP (e.g., for
communication/file exchange), additional file formats, support for
simulators, an installer and an adapted user interface.

License
^^^^^^^

Similar to its predecessor *the RobotEditor* the NRP RobotDesigner is
published as open source software under the `GPLv2
license <http://www.gnu.org/licenses/gpl-2.0.html>`__.

The NRP RobotDesigner
---------------------

The Human Brain Project [#]_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The European Commission has selected the `Human Brain
Project <https://www.humanbrainproject.eu>`__ as one of its two
Flagship projects. Over the course of 10 years, the HBP will create an
integrated system of six ICT platforms, one dedicated to Neurorobotics.
The Neurorobotics Subproject of the HBP is coordinated by a research
group led by `Prof. Alois Knoll <http://www6.in.tum.de/Main/Knoll>`__.
The Human Brain Project is part of the FET Flagship Programme, which is
a new initiative launched by the European Commission as part of its
`Future and Emerging Technologies
(FET) <http://cordis.europa.eu/fp7/ict/programme/fet/flagship/>`__
initiative. The goal is to encourage visionary, “mission-oriented”
research with the potential to deliver breakthroughs in information
technology with major benefits for European society and industry. The
Commission envisages the Flagship program as a highly ambitious
initiative involving close collaboration with National and Regional
funding agencies, industry and partners from outside the European Union.
`Read more... <http://neurorobotics.net/the-human-brain-project/>`__

The Neurorobotics Platform [#]_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Neurorobotics sub-project will develop the `Neurorobotics Platform
<http://neurorobotics.net>`__ which will
offer scientists and technology developers a software and
hardware infrastructure allowing them to connect pre-validated brain
models to detailed simulations of robot bodies and environments and to
use the resulting neurorobotic systems in in silico experiments and
technology development. The Neurorobotics Platform allows
researchers to design and run simple experiments in cognitive
neuroscience using simulated robots and simulated environments linked to
simplified versions of HBP brain models. The *Neurorobotics Platform*
includes a Robot Designer, an Environment Builder, and a Closed-Loop
engine, as well as the *Neurorobotics Platform* host facility. The
*Neurorobotics Platform* will exploit the 3D modelling capabilities
provided by commercial and open source gaming platforms. The *HBP
Neurorobotics Platform* allows researchers to conduct closed-loop
experiments, in which a virtual robot is connected to a brain model,
running on the HPC platform or on neuromorphic hardware (E.g., the
`SpiNNaker boards <http://apt.cs.manchester.ac.uk/projects/SpiNNaker/>`__ ).
Although the capabilities to model virtual robots and
environments already exist, and although various labs have created
closed-loop set-ups with simple brain models, the HBP platform is
the first to couple robots to detailed models of the brain. This will
make it possible to perform experiments exploring the link between low
level brain circuitry and high-level function.

The Neurorobotics Platform will provide a flexible environment in which
researchers can perform experiments using simulated robots connected to
different classes of brain model – simplified versions of the models
provided by the Brain Simulation Platform, high level models coming from
the `Cognitive
Architectures <https://www.humanbrainproject.eu/de/cognitive-architectures>`__
and `Theoretical
Neuroscience <https://www.humanbrainproject.eu/de/theoretical-neuroscience>`__
sub-projects.

Installation
------------

We currently support Blender version 2.8. Ubuntu users please download the archived Blender version, the apt-get installed Blender version is currently not supported.

To install the plugin on Linux and Windows follow these steps:

1.  Download a supported Blender version from the dedicated website. Windows users download and install the  `*.msi` installer. `Go to Blender download page <https://download.blender.org/release/>`__

2.  Download the Robot Designer installation file “robotdesigner_installer.blend” from our GitHub repository . `Download installation file <https://github.com/hbpneurorobotics/BlenderRobotDesigner/raw/master/robotdesigner_installer.blend>`__

3.  Launch Blender and open the downloaded "robotdesigner_installer.blend" file, then click on the triangle above the script to execute it. The installation may take a bit of time while Blender is remaining passive. Once the installation is done you will see the Robot Designer plugin opening on the right side along with the "Tool", "View" and "Edit" tabs, as shown in the image below.

.. figure:: RobotDesignerInstall_plugin.png
	:align: center

	After running the Robot Designer installation script (on the left) you will find the plugin opening up on the right side of the 3D view.

.. figure:: RobotDesignerInstall_open.png
	:align: center

	If the plugin does not pop up, you will find it by opening the pane on the right of the 3D view with clicking on the small arrow.

Troubleshooting
--------
- `Start Blender from terminal <https://docs.blender.org/manual/en/2.79/advanced/command_line/introduction.html>`__  to see log output during the installation process and runtime.
- In newer versions you can open the terminal view via ``Window->Toggle System Console``.
- If the plugin does not show up or does not show up anymore after restarting Blender make sure it is enabled: Navigate to ``Edit->Preferences->Add-Ons`` tab. Search for the NRP Robot Designer add-on and check the box to enable the plugin. You may need to restart Blender thereafter.
- If you see the error ``No module named 'pyxb'`` in the terminal try the following:

   In your terminal go to ``[blender-version]/[version]/python/bin`` and run ``./python3.7m -m pip install pyxb==1.2.5``

- Additional logs during runtime of the plugin are written to ``blender_module_path/robot_designer_plugin/resources/log.txt``

   - Ubuntu: ``blender_module_path =  $HOME/.config/blender/[version]/scripts/addons/``
   - Windows: ``blender_module_path =   C:\Users\[profile]\AppData\Roaming\Blender Foundation\blender\[version]\scripts\addons``

Features
--------

-   **Installer**

    The installer comes in a form of a ``.blend`` file that contains an
    installer script that can be directly executed from within Blender. That
    way, it can detect the used operating system and Blender version and
    link the files to the correct location as well as select the correct
    binaries for the platform.

-   **Robot modeling**

    The robot designer adds functionality to the Blender software with
    respect to robotics:

    -  Kinematic modeling in a scientific/engineering way (e.g., entering
       transformations in *Denavit-Hartenberg* convention)
    -  Editing of dynamic properties (center of mass and distribution,
       friction, etc.)
    -  Automatic mesh generation
    -  Creation of collision models using geometries with fixed size of
       vertices and safety distance
    -  Convex hull computation
    -  Conversion from deformable meshes to rigid bodies. This is useful to
       transform deformable actors such as those created by
       `MakeHuman <http://www.makehumancommunity.org/>`__ into robots. This is used
       to provide a standard humanoid robot model to the NRP.
    -  Generation of links and joint geometries based on the kinematic
       description (*still experimental*).
    -  Placing of sensors (*Note: Currently, this includes cameras only.
       More to follow on request by the NRP and users*)
    -  Graphically defining muscles and its pathpoints on skeletal models.
    -  Building of world files with multiple robots.


-   **File format and ROS/Gazebo support**

    In order to interchange models with the *Neurorobotics platform* the
    Robot designer has to support additional file formats.

    In the file section robot models can be imported and exported as single files or zipped packages in the
    `Simulator Description Format (SDF) <http://sdformat.org/spec?elem=sdf>`__ file format.
    It will be enriched by additional information tags supported
    by the `Gazebo <http://gazebosim.org/>`__ simulator–especially for
    supporting a plugin developed for the NRP to include joint controllers
    directly in the robot description file. This file support relies on `the
    PyXB package <http://pyxb.sourceforge.net/>`__–a software that
    translates XML scheme definitions (XSD) into a Python document object
    model.


-   **Plugin Core Framework**

    Although the RobotEditor is already feature rich, development is
    cumbersome due to Blender's conventions for plugin design. The
    ``Plugin Core`` framework is a python package that abstracts and
    simplifies many of the boiler plate thus allowing the design of larger
    applications based on Blender. The RobotEditor, therefore, had to be
    refactored and rewritten in large parts to comply with this framework.

    Especially the dynamic nature of how functionality is added to Blender
    makes a modern Python development with IDEs (Integrated Development
    Environments) such as the excellent
    `PyCharmTM <https://www.jetbrains.com/pycharm/>`__ which support code
    completion and refactoring difficult. By using decorators (`PEP
    0318 <https://www.python.org/dev/peps/pep-0318/>`__) and handlers for
    `Blender
    Operators <https://www.blender.org/api/blender_python_api_current/bpy.types.Operator.html#bpy.types.Operator>`__
    and
    `Properties <https://www.blender.org/api/blender_python_api_current/bpy.types.Property.html#bpy.types.Property>`__,
    and *extended exception handling* and *logging*, developers can easily
    create even larger projects comfortably. Integration of *external
    debugging* is planned and currently under development. Further, mock ups
    for the Blender API can be generated and used for code completion.

    Current development focuses on extending the framework to support
    `static type
    checking <https://en.wikipedia.org/wiki/Type_system#Type_checking>`__
    using `MyPy <http://mypy-lang.org/>`__ and code analysis
    (`PyLint <https://www.pylint.org/>`__) on plugin loading.

    The ``Plugin Core`` has an extensive documentation and might be released
    as a separated project in the future for inclusion in different
    projects.

-   **Documentation** and coding standards

    The RobotDesigner comes with extensive documentation in form of a user's
    and developers manual which explains all steps necessary to setup and
    run the software as well on how to extend it and use the ``Plugin Core``
    in general. The code aims at being well-documented (the original code
    base is currently in the process of being documented) and to meet coding
    standards such as `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`__.

Planned features
----------------

One of the key aspects of the ongoing development is data persistence,
that is, the ability to store robot models in different file formats and
different storage mechanisms. More file formats will be supported upon demand.
By the inclusion and abstraction of the ``PyXB`` interface XML-based systems can be integrated easily.

As well, further model properties and in particular sensor modalities including its various
sensor parameters will be implemented.

Acknowledgement
--------
This open source software code was developed in part or in whole in the Human Brain Project,
funded from the European Union’s Horizon 2020 Framework Programme for Research and Innovation
under Specific Grant Agreements No. 720270 and No. 785907 (Human Brain Project SGA1 and SGA2).

--------------

Footnotes
^^^^^^^^^

.. [#] Funded by the European Commission through its Cognition Unit under the
    Information Society Technologies of the seventh Framework Programme (FP7)
.. [#] B. Leon, S. Ulbrich, R. Diankov, G. Puche, M. Przybylski, A. Morales,
    T. Asfour, S. Moisio, J. Bohg, J. Kuffner and R. Dillmann, *"OpenGRASP:
    A Toolkit for Robot Grasping Simulation",* 2nd International Conference
    on Simulation, Modeling, and Programming for Autonomous Robots (SIMPAR),
    November 15, 2010
.. [#] N. Vahrenkamp, M. Kröhnert, S. Ulbrich, T. Asfour, G. Metta, R.
    Dillmann and G. Sandini, *"Simox: A Robotics Toolbox for Simulation,
    Motion and Grasp Planning"*, International Conference on Intelligent
    Autonomous Systems (IAS), pp. 585 - 594, 2012
.. [#] C. Mandery, Ö. Terlemez, M. Do, N. Vahrenkamp and T. Asfour, *"The KIT
    Whole-Body Human Motion Database"*, International Conference on Advanced
    Robotics (ICAR), pp. 0 - 0, July, 2015
.. [#] From `the project's website <http://www.humanbrainproject.eu>`__
.. [#] From `the Neurorobotics website <neurorobotics.net>`__
