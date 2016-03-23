About
=====

The *NRP RobotDesigner* software developed in the scope
of the `Human Brain Project <hhttps://www.humanbrainproject.eu>`_ in the sub-project
`SP10 Neurorobtics <http://neurorobotics.net/index.php>`_. It is part of the *Neurorobotics Platform* which
aims at providing easy accessible and usable tools to neuro-scientists and neuro-roboticists for simulating robots
that are controlled by artificial brains in virtual environments. The *RobotDesinger* is a modelling tool that
allows to generate *geometric*, *kinematic* and *dynamic* models that can be used in the simulation environment.
While other services of the NRP are created as web-based services that do not require installation and, therefore,
administration expertise, the *RobotDesigner* is a plugin for the freely available (GPL licensed)
`Blender 3D modeling suite <http://blender.org>`_.
This is because of three reasons:

1. The full capabilities of a feature-rich modelling suite such as Blender is an enormous undertaking.
2. If someone is willing to model her/his own model, expertise in this field can be expected.
3. Blender is freely available for a wide range of platforms and installation is very easy.

Under the hood, the plugin extends the built-in data types and provides an improved and clear interface to
the modelling software.

History
-------

The *NRP RobotDesigner* has been initially developed under the name *OpenGRASP RobotEditor*
from 2008-2012 at the `HIS -- Humanoids and Intelligence Systens Lab
(IAR -- Institute for Anthropomatics and Robotics) <http://his.anthropomatik.kit.edu/english/index.php>`_  of the
`Karlsruhe Institute of Technology <http://www.kit.edu/english/index.php>`_ the in the
`European GRASP project <http://www.csc.kth.se/grasp/>`_ [#f1]_ [#f2]_
in the context of the `OpenGRASP software <http://opengrasp.sourceforge.net/>`_.
It is published under the GPL license.
This Python plugin restricted to the
Blender version 2.49 was mainly developed by `Stefan Ulbrich (FZI) <mailto:stefan.ulbrich@fzi.de>`_.
One of the most notable features of the *RobotEditor* was support for the
`Collada v1.5 <https://www.khronos.org/collada/>`_ 3D asset exchange format. This file format has large support from
the industry including companies such as Daimler and Sony. The RobotEditor was the only freely available
tool creating valid models for Collada v1.5 which supported the new description facilities for kinematics and dynamics.

Afterwards, the *RobotEditor* [#f3]_ has been completely rewritten to comply the programming interface of newer Blender
versions (>2.69) at the `H2T -- High Perfomance Humanoid Technologies Lab (IAR -- Institute for Anthropomatics
and Robotics) <http://h2t.anthropomatik.kit.edu/enligsh/index.php>`_ of the
`Karlsruhe Institute of Technology <http://www.kit.edu/english/index.php>`_ by the main authors
`Michael Bechtel <mailto:michael.bechtel@kit.edu>`_ and `Stefan Ulbrich (FZI) <mailto:stefan.ulbrich@fzi.de>`_. Many new
feature such as *physical properties*, *joint dynamics*, *sensors for matching motion capture data* support for
the `Simox robot simulator <http://simox.sourceforge.net/>`_ [#f4]_ have been added to the software. The current is still
developed and the current state is `available under the GPL license <https://gitlab.com/h2t/roboteditor>`_.

The *RobotEditor* has been chosen as the basis of the *NRP RobotDesigner* after a comparison to competing projects
(e.g., `phobos <https://github.com/rock-simulation/phobos>`_). It will enrich the existing projects
by components required for the NRP (e.g., for communication/file exchange), additional file formats,
support for simulators, an installer and  an adapted user interface.


The RobotDesigner
-----------------

The Human Brain Project [#f5]_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The European Commission has selected the Human Brain Project as one of its two Flagship projects. Over the course of
10 years the HBP will create an integrated system of six ICT platforms, one dedicated to Neurorobotics.
The Neurorobotics Subproject of the HBP is coordinated by a research group led by Prof. Alois Knoll.
The Human Brain Project is part of the FET Flagship Programme, which is a new initiative launched by the
European Commission as part of its
`Future and Emerging Technologies (FET) <http://cordis.europa.eu/fp7/ict/programme/fet/flagship/>`_ initiative.
The goal is to encourage
visionary, “mission-oriented” research with the potential to deliver breakthroughs in information technology
with major benefits for European society and industry. The Commission envisages the Flagship program as a highly
ambitious initiative involving close collaboration with National and Regional funding agencies, industry and
partners from outside the European Union. `Read more <http://neurorobotics.net/the-human-brain-project/>`_

The Neurorobotics Platform [#f5]_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Neurorobotics sub-project will develop the Neurorobotics Platform which will offer scientists and technology
developers a software and hardware infrastructure allowing them to connect pre-validated brain models to detailed
simulations of robot bodies and environments and to use the resulting neurorobotic systems in in silico experiments
and technology development.
The goal for the ramp-up phase will be to develop the Neurorobotics Platform version 1 which will allow researchers
to design and run simple experiments in cognitive neuroscience using simulated robots and simulated environments
linked to simplified versions of HBP brain models. The *Neurorobotics Platform* will include a Robot Designer, an
Environment Builder, and a Closed-Loop engine, as well as the *Neurorobotics Platform* host facility.
The *Neurorobotics Platform* will exploit the 3D modelling capabilities provided by commercial and open source gaming
platforms (the choice of platform will be made in the early stage of the project). The *HBP Neurorobotics Platform*
will allow researchers to conduct closed-loop experiments, in which a virtual robot is connected to a brain model,
running on the HPC platform or on neuromorphic hardware. Although the capabilities to model virtual robots and
environments already exist, and although various labs have created closed-loop set-ups with simple brain models,
the HBP platform will be the first to couple robots to detailed models of the brain. This will make it possible to
perform experiments exploring the link between low level brain circuitry and high-level function. The first release
of the *Neurorobotics Platform* will offer extremely simple functionality. The majority of technical development work
will focus on the goals fixed for the second release, which will provide a flexible environment in which researchers
can perform experiments using simulated robots connected to different classes of brain model – simplified versions of
the models provided by the Brain Simulation Platform, high level models coming from the
`Cognitive Architectures <https://www.humanbrainproject.eu/de/cognitive-architectures>`_ and
`Theoretical Neuroscience <https://www.humanbrainproject.eu/de/theoretical-neuroscience>`_ subprojects.



Features
--------

Installer
^^^^^^^^^

The installer comes in a form of a `.blend` file that contains an installer script that can
be directly executed from within Blender. That way, it can detect the used operating system and
Blender version and link the files to the correct location as well as select the
correct binaries for the platform.

For more information, refer to :ref:`installation`.


Robot modelling
^^^^^^^^^^^^^^^

The robot designer adds functionality to the Blender software with respect to robotics:

* Kinematic modelling in a scientific/engineering way
  (e.g., entering transformations in *Denavit-Hartenberg* convention)
* Editing of dynamic properties (center of mass and distribution, friction, etc.)
* Generation of simplified collision models
* Placing of sensors

File format support
^^^^^^^^^^^^^^^^^^^

In order to interchange models with the *Neurorobotics platform* the Robot designer has to support additional file
formats.

At first, this will be the `URDF <http://wiki.ros.org/urdf/XML>`_ format which is very popular in the `Robot Operating
System (ROS) <http://wiki.ros.org>`_ community. It will be enriched by additional information tags supported by the
`Gazebo <http://gazebosim.org/>`_ simulator---especially for supporting a plugin developed for the NRP to
include joint controllers directly in the robot description file. This file support relies on
`generateDS <https://pypi.python.org/pypi/generateDS>`_---a software that translates XML scheme definitions (XSD)
into a Python document object model. Currently, the RobotDesigner supports export and limited import of these
files.

In the future, support for the `SDF <http://sdformat.org/spec?elem=sdf>`_ file format is planned although
conversion in between URDF and SDF is possible in a limited way.


GIT integration
^^^^^^^^^^^^^^^

The distributed version control system `GIT <https://git-scm.com/>`_ will be used to directly upload exported models
to a remote repository that can be accessed by the *Neurorobotics Platform*. That way, it will not be necessary
to upload and store robot models and create a seamless integration of the RobotDesigner in the web-based NRP.


.. rubric:: Footnotes

.. [#f1] Funded by the European Commission through its Cognition Unit under the Information Society Technologies of the seventh Framework Programme (FP7)
.. [#f2] B. Leon, S. Ulbrich, R. Diankov, G. Puche, M. Przybylski, A. Morales, T. Asfour, S. Moisio, J. Bohg, J. Kuffner and R. Dillmann , *OpenGRASP: A Toolkit for Robot Grasping Simulation,* 2nd International Conference on Simulation, Modeling, and Programming for Autonomous Robots (SIMPAR), November 15, 2010
.. [#f3] N. Vahrenkamp, M. Kröhnert, S. Ulbrich, T. Asfour, G. Metta, R. Dillmann  and G. Sandini, *Simox: A Robotics Toolbox for Simulation, Motion and Grasp Planning*, International Conference on Intelligent Autonomous Systems (IAS), pp. 585 - 594, 2012
.. [#f4] C. Mandery, Ö. Terlemez, M. Do, N. Vahrenkamp and T. Asfour, *The KIT Whole-Body Human Motion Database*, International Conference on Advanced Robotics (ICAR), pp. 0 - 0, July, 2015
.. [#f5] From `the Neurorobotics website <neurorobotics.net>`_
