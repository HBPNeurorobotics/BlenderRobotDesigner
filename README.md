#  RobotEditor

The RobotEditor is a modelling tool that allows to easily create models of scientific robots.

## Features

   * Geometric modeling: The modelling of new robots requires a tool that excels in modeling of the geometrical components (i.e. meshes).
   * Semantic modeling: Even more important is the ability to allow the description of semantic properties of the robot manipulator, such as the definition of kinematic chains or rigid body dynamics parameter.
	
	
## Software requirements

Blender: The plguin has been developed under version 2.69 and it is hence required to also use this version (Download it here: http://www.blender.org/download/).
	
## Installation:
After cloning/downloading the plugin from the Github repository, copy the (unzipped) folder containing all the RobotEditor files to `/.../Blender/2.69/scripts/addons`. Then open Blender and navigate to the *Addons* tab
located in *File -> User Preferences*. Find *RobotEditor* in the list and activate the plugin by checking the checkbox in the top right corner.
Now the User Interface of the plugin can be found at the bottom of the toolbar on the left side of the 3D View (expand the toolbar by clicking the (+) in the top left corner).


**Tip**: If you don't want to activate the plugin on every start-up of Blender,
click the *Save User Settings* button in the bottom left corner of the *User Preferences* window after activating it for the first time.


## Usage:
The RobotEditor differentiates between the *semantic properties* of a robot (that is its kinematics and optionally markers and physical properties) and the actual *visualization* of the robot (which is defined through meshes
for the individual links).

The first step is to create the kinematics representation of a robot. The plugin aggregates the kinematics within a so called *Armature* object. The *Select Armature* menu allows to create a new *Armature* by choosing the *New* list entry.
This list will also contain all previously defined kinematic chains.

A newly created *Armature* will appear at the current position of the 3D pointer in the 3D View. Additionally, a *Bone* object is created. These *Bone* objects represent the origin of the reference frames through which the kinematic chain
is defined. By convention, the tail of the bone is located in the actual origin of the reference frame while the head points in the direction of the local y-axis (and thus, is perpendicular to the x-z plane).



## Tutorial:
To be added.
	

