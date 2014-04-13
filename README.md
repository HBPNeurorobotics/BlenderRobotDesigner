#  RobotEditor

The RobotEditor is a modelling tool that allows to easily create models of scientific robots.

## Features

   * Geometric modeling: The modelling of new robots requires a tool that excels in modeling of the geometrical components (i.e. meshes).
   * Semantic modeling: Even more important is the ability to allow the description of semantic properties of the robot manipulator, such as the definition of kinematic chains or rigid body dynamics parameter.
	
	
## Software requirements

Blender: The plguin has been developed under version 2.69 and it is hence required to at least use this version (Download it here: http://www.blender.org/download/).
	
## Installation:
After cloning/downloading the plugin from the Github repository, copy the (unzipped) folder containing all the RobotEditor files to `/.../Blender/2.69/scripts/addons`. Then open Blender and navigate to the *Addons* tab
located in *File -> User Preferences*. Find *RobotEditor* in the list and activate the plugin by checking the checkbox in the top right corner.
Now the User Interface of the plugin can be found at the bottom of the toolbar on the left side of the 3D View (expand the toolbar by clicking the (+) in the top left corner).


**Tip**: If you don't want to activate the plugin on every start-up of Blender,
click the *Save User Settings* button in the bottom left corner of the *User Preferences* window after activating it for the first time.


## Usage:
The RobotEditor differentiates between the *semantic properties* of a robot (that is its kinematics and optionally visual markers and physical properties) and the actual *visualization* of the robot (which is defined through meshes for the individual links).

### Kinematics:
The first step is to create the kinematics representation of a robot. The plugin aggregates the kinematics within a so called *Armature* object. The *Select Armature* menu allows to create a new *Armature* by choosing the *New* list entry.
This list will also contain all previously defined kinematic chains.

A newly created *Armature* will appear at the current position of the 3D pointer in the 3D View. Additionally, a *Bone* object is created. *Bone* objects represent the reference frames through which a kinematic chain
is defined **and** the actual joint configuration of the joint within this reference frame. By convention, the tail of the bone is located in the actual point origin of the reference frame while the head points at the direction of the local y-axis (and thus, is perpendicular to the x-z plane).

Transformations of *Bones* from parent reference frames can be defined in two ways:
	1. Euler mode: the transformation is defined through three translations along the local axes and three rotations (around the local x-axis, around the resulting new local y'-axis and finally around the resulting new local z''-axis)
	2. DH mode: the transformation is defined through two rotations and two rotations according to the Denavit-Hartenberg convention 

Joints always represent one Degree of Freedom and can either be revolute(rotational) or prismatic(translational). By selecting the active axis, the joint type and value, offset, minimum and maximum, the configuration of a joint can be set.

New children *Bones* can be created by clicking on the *Create new child bone* button.

The hierarchy of the kinematic chain can be seen in the *Outliner* which can be found in the top right corner of the Blender User Interface.

**Tip:** If parts of the User Interface of the RobotEditor seem to have disappeared from the toolbar, make sure to re-select an *Armature* by right-clicking on it in the 3D View or left-clicking in the Outliner or by selecting it from the *Armature* drop-down menu in the toolbar. Also, **always** return back to either *Object Mode* or *Pose Mode* if you should accidentally or intentionally end up in *Edit Mode* before further interacting with the RobotEditor interface.

**Tip:** To better visualize the location and orientation of the reference frame defined by a *Bone* object, change the *Interaction mode* from *Object Mode* to *Pose Mode* and change the *Transformation orientation* from *Global* to *Local*.

**Tip:** 
*Bones* can be either selected through the *Active Bone* drop-down menu in the RobotEditor toolbar or by left-clicking on them in the Outliner.


**Tip:** To create spherical joints, create three *Bones* within the same position but with different active axes to account for the three Degrees of Freedom.