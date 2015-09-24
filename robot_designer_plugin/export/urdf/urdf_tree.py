"""
Module for importing robots specified in the URDF file format.
"""

__author__ = 'Stefan Ulbrich'
import sys

import pyxb
from . import urdf_dom
import logging
logger = logging.getLogger('URFD')
logger.setLevel(logging.DEBUG)

def set_value(l):
    """
    helper function that creates a string out of a list of floats
    :param l: python list of floats
    :return: string representing the list
    """
    return ' '.join(i for i in l)


class URDFTree(object):
    """
    A class that parses and represents a robot described by a URDF file.
    The data is stored in a tree of linked instances of this class. Therefore, a root element (or several) has to be
    detectable in the file excluding closed kinematic loops at the moment.
    Each instance represents a *blender/RobotDesigner bone* that is a compound of joint and link.
    It uses a document object model (DOM) created by generateDS.py (in version 2.14a -- the newest
    that does not depend on the lxml module, which is not included in blender).
    """

    def __init__(self, connected_joints, connected_links, robot=None):
        """ Constructor
        :param root: if specified, the constructor copies the cross-references in the XML file from another
        URDFTree instance.
        :param connected_joints: If specified, the connectedJoints (cross-reference in the XML file) is set.
        :param connected_links: If specified, the connectedLinks (cross-reference in the XML file) is set.
        :return:
        """
        # super(URDFTree, self).__init__()
        self.children = []

        self.robot = robot
        self.joint = None
        self.link = None

        self.connectedLinks = connected_links
        self.connectedJoints = connected_joints

    @staticmethod
    def parse(file_name):
        """ Parses a URDF file and builds up a tree representing the kinematic structure of a robot.
        Explanation: The URDF file format stores links (i.e., rigid bodies) and joints (i.e., connection between links)
        in a flat structure (as opposed to a tree data structure). Links have no references while joints refer to the
        NAMES of have exactly one parent (link) and child (link). This method first resolves these cross references
        and calls the recursive URDFTree.build() method to create a tree-like data structure representing the
        kinematic tree(s) of the robot.
        :param file_name: the name of the file to open
        """

        # read the file
        #robot = urdf_dom.parse(file_name, silence=True)
        robot = urdf_dom.CreateFromDocument(open(file_name).read())

        # parsing joint controllers
        # create a dictionary [ joint_name, controller ] which is
        # easily searchable during tree traversal
        controller_cache = {}
        for gazebo_tag in robot.gazebo:
            for plugin_tag in gazebo_tag.plugin:
                if plugin_tag.name == "generic_controller":
                    for controller in plugin_tag.controller:
                        # store the controller in cache, so it's accessible
                        logger.debug("Found controller for joint: " + controller.joint_name + ", caching it.")
                        controller_cache[controller.joint_name] = controller
        logger.debug("Built controller cache:")
        logger.debug(controller_cache)

        # create mapping from (parent) links to joints
        connected_joints = {link: [joint for joint in robot.joint if link.name == joint.parent.link] for link
                            in robot.link}

        # create mapping from joints to their child links
        connected_links = {joint: link for link in robot.link for joint in robot.joint if
                           link.name == joint.child.link}

        # find root links (i.e., links that are NOT connected to a joint)
        child_links = [link.name for link in robot.link for joint in robot.joint if
                       link.name == joint.child.link]
        root_links = [link for link in robot.link if link.name not in child_links]

        logger.debug("Root links: %s", [i.name for i in root_links])
        logger.debug("connected links: %s", {j.name: l.name for j, l in connected_links.items()})

        kinematic_chains = []

        # Skips the basis links
        for link in root_links:
            for joint in connected_joints[link]:
                tree = URDFTree(connected_links=connected_links, connected_joints=connected_joints, robot=robot)
                kinematic_chains.append(tree)
                tree.build(connected_links[joint], joint)

        # todo: parse joint controllers

        logger.debug("kinematic chains: %s", kinematic_chains)
        return robot.name, root_links, kinematic_chains, controller_cache

    def build(self, link, joint=None,depth=0):
        """
        Recursive function that builds up the tree representation of the robot. You do not have to call it manually (
        Called by parse).
        :param link: The link the kinematics subtree starts with
        :param joint: The joint connecting to the previous link (if any)
        """
        self.children = []
        self.joint = joint
        self.link = link
        self.set_defaults()

        children = self.connectedJoints[link]

        #logger.debug("%s %s, %s -> %s", '-'*depth, joint.name, link.name, [i.name for i in children] )
        #logger.debug("%s axis: '%s', type: '%s', xyz:'%s', rpy:'%s', limit:'%s-%s' ", ' '*depth,  joint.axis.xyz, joint.type_, joint.origin.xyz,joint.origin.rpy, joint.limit.lower, joint.limit.upper )

        for joint in children:
            tree = URDFTree(connected_links=self.connectedLinks, connected_joints=self.connectedJoints, robot=self.robot)
            self.children.append(tree)
            tree.build(self.connectedLinks[joint], joint, depth+1)


    @staticmethod
    def create_empty(name):

        tree = URDFTree(connected_links={}, connected_joints={}, robot=urdf_dom.RobotType())
        tree.robot.name = name
        tree.link = urdf_dom.LinkType()
        tree.link.name = "base_link"
        tree.robot.link.append(tree.link)
        tree.joint = urdf_dom.JointType()

        tree.set_defaults()

        # build empty gazebo tag for control plugins
        tree.gazebo_tag = urdf_dom.GazeboType()
        tree.robot.gazebo.append(tree.gazebo_tag)

        return tree


    def write(self, file_name):
        """
        Should only be called on the root element.
        :param file_name:
        :return:
        """

        for joint, link in self.connectedLinks.items():
            joint.child.link = link.name

        for link, joints in self.connectedJoints.items():
            for joint in joints:
                joint.parent.link = link.name

        # Connect root joints to self.link (the root link)
        for joint in self.robot.joint:
            if joint.parent is None:
                joint.parent = self.link.name

        with open(file_name, "w") as f:
            #f.write('<?xml version="1.0" ?>')
            output = self.robot.toxml("utf-8", element_name="robot").decode("utf-8")
            #output = output.replace(">", ">\n")
            f.write(output)
            # self.robot.export(f,0)


    def _write(self):
        """
        Recursion that builds the creates the cross links for the DOM (might not be necessary)
        """
        pass

    def add(self):
        """
        Creates and adds another URDFTree instance to this node. Do not add children to the subtree manually as
        references are not created then. Note that if there is no robot member defined yet (i.e., you are *exporting*),
        it will be created automatically.
        :param link: a urdf_dom link element
        :param joint: a urdf_dom joint element
        :return: a reference to the newly created URDFTree instance.
        """

        tree = URDFTree(connected_links=self.connectedLinks, connected_joints=self.connectedJoints, robot=self.robot)
        tree.joint = urdf_dom.JointType()
        tree.link = urdf_dom.LinkType()
        tree.robot.link.append(tree.link)
        tree.robot.joint.append(tree.joint)
        tree.set_defaults()
        tree.joint.child = urdf_dom.ChildType()
        tree.joint.parent = urdf_dom.ParentType()

        self.connectedLinks[tree.joint] = tree.link
        if self.link in self.connectedJoints:
            self.connectedJoints[self.link].append(tree.joint)
        else:
            self.connectedJoints[self.link] = [tree.joint]

        return tree

    def add_mesh(self, file_name):
        """

        :param link:
        :return:
        """
        visual = urdf_dom.VisualType()
        self.link.visual.append(visual)
        visual.geometry = urdf_dom.GeometryType()
        visual.origin = urdf_dom.PoseType()
        visual.geometry.mesh = urdf_dom.MeshType()
        visual.geometry.mesh.filename = file_name
        return visual

    def add_collisionmodel(self, file_name):
        """
        Add a collision model to a mesh object

        :param   file_name:  name of the mesh object for which the col_model is generated
        :type    file_name:  string
        :return: string:     Collision file that is used in the urdf
        """
        collision = urdf_dom.CollisionType()
        self.link.collision.append(collision)
        collision.geometry = urdf_dom.GeometryType()
        collision.origin = urdf_dom.PoseType()
        collision.geometry.mesh = urdf_dom.MeshType()
        #print('debug add_collisionmodel: ' + file_name)
        collision.geometry.mesh.filename = file_name
        return collision

    def add_inertial(self):
        """
        Add a inertial definition to a link object

        :return: string:     reference to inertial object
        """
        inertial = urdf_dom.InertialType()
        self.link.inertial.append(inertial)
        inertial.mass = urdf_dom.MassType()
        inertial.inertia = urdf_dom.InertiaType()
        inertial.origin = urdf_dom.PoseType()
        inertial.origin.xyz = "0 0 0"
        inertial.origin.rpy = "0 0 0"

        #print('debug add_inertial: ')
        return inertial

    def add_joint_control_plugin(self):

        plugin = urdf_dom.GazeboPluginType()
        plugin.name = "generic_controller"
        plugin.filename = "libgeneric_controller_plugin.so"
        self.gazebo_tag.plugin.append(plugin)
        return plugin

    def add_joint_controller(self, control_plugin):
        """
        Add a controller definition to a robot object

        :return: string:     reference to inertial object
        """
        joint_controller = urdf_dom.GenericControllerPluginDefType()
        if joint_controller.pid == "1.0 1.0 1.0":
            joint_controller.pid = "100.0 1.0 1.0"
            print("Debug: Joint Controller set")

        control_plugin.append(joint_controller)
        print("Added joint controller.")

        return joint_controller

    def set_defaults(self):
        """
        Adds some default values to the DOM.
        """

        joint = self.joint
        link = self.link
        if joint.axis is None:
            joint.axis = urdf_dom.AxisType()

        if joint.limit is None:
            joint.limit = urdf_dom.LimitType()
            # this had to be completely defined (missing effor argument caused conversion to SDF to fail)
            joint.limit.effort = 100.0
            joint.limit.lower = joint.limit.upper = joint.limit.velocity = 1.0

        if joint.calibration is None:
            joint.calibration = urdf_dom.CalibrationType()
            joint.calibration.reference_position = 0.0
            joint.calibration.rising = 0.0 # there are no default values in the XSD?
            joint.calibration.falling = 0.0

        if joint.origin is None:
            joint.origin = urdf_dom.PoseType()
            # joint.rpy =

        for visual in link.visual:
            if visual.origin is None:
                visual.origin = urdf_dom.PoseType()

        for collision in link.collision:
            if collision.origin is None:
                collision.origin = urdf_dom.PoseType()

        if joint.dynamics is None:
            joint.dynamics = urdf_dom.DynamicsType()
            joint.dynamics.damping = 1.0

        if link.inertial is None:
            logger.debug("Inertial is None, creating default one.")
            link.inertial = urdf_dom.InertialType()

        for inertial in link.inertial:
            if inertial.mass is None:
                inertial.mass = urdf_dom.MassType()
            if inertial.inertia is None:
                inertial.inertia = urdf_dom.InertiaType()

            # if joint.mimic is None: # truely optional
            # if joint.safety_controller is None: # ignored

            # if link.inertial is None:

            # todo continue and remove if statements from urdf_blender

    def show(self, depth=0):
        """
        Prints the kinematic tree to the command line (for debugging).
        This function serves as an example for export export.
        :param depth: the depth of the kinematics sub tree for indention
        """
        if depth > 1:
            print(
                "%s, link: %s, joint: %s, type: %s" % ("*" * depth, self.link.name, self.joint.name, self.joint.type_))
        elif depth == 1:
            print("Root link: %s" % self.link.name)
        for tree in self.children:
            tree.show(depth + 1)

# debugging the module
if __name__ == "__main__":
    robot = URDFTree()
    robot.parse("../../models/hollie.urdf")
    robot.show()
