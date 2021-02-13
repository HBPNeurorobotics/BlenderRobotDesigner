import logging

import sdf_model_dom

# from helpers import list_to_string
from pyxb import ContentNondeterminismExceededError
import os
import re
import sys
from pathlib import Path

from pprint import pprint

logger = logging.getLogger('SDF')
logger.setLevel(logging.DEBUG)


# ~/Documents/blender-2.78-d35bf3f-linux-glibc219-x86_64/2.78/python/bin/pyxbgen -u sdf_model.xsd -m sdf_model_dom

def set_value(l):
    """
    helper function that creates a string out of a list of floats
    :param l: python list of floats
    :return: string representing the list
    """
    return ' '.join(i for i in l)


def list_to_string(l):
    """
    Converts a python list of floats to a string. If there are no decimals behind the comma separator they will be
    cut off (e.g., :math:`1.0 \rightarrow 1`)

    :param l:
    :return:
    """
    return " ".join([str(i).rstrip('0').rstrip('.') for i in l])


def string_to_list(s):
    """
    Converts a XML string representing a float vector to python list of float.

    :param s: the XML string
    :return: the python list
    """
    # todo move to helper module one level above (and create it)
    v = [float(i) for i in re.findall("[-+]?\d*\.?\d+[eE]?[-+]?\d*", s)]
    return v


class SDFTree(object):
    """
    A class that parses and represents a robot described by a SDF file.
    The data is stored in a tree of linked instances of this class. Therefore, a root element (or several) has to be
    detectable in the file excluding closed kinematic loops at the moment.
    Each instance represents a *blender/RobotDesigner bone* that is a compound of joint and link.
    It uses a document object model (DOM) created by pyxbgen.py (in version 1.2.5 -- pyxb).
    """

    def __init__(self, connected_joints=None, connected_links=None, robot=None):
        """ Constructor
        :param root: if specified, the constructor copies the cross-references in the XML file from another
        SDFTree instance.
        :param connected_joints: If specified, the connectedJoints (cross-reference in the XML file) is set.
        :param connected_links: If specified, the connectedLinks (cross-reference in the XML file) is set.
        :return:
        """
        self.children = []

        self.robot = robot
        self.joint = None
        self.link = None

        self.connectedLinks = connected_links
        self.connectedJoints = connected_joints

    @staticmethod
    def parse(file_name):
        """ Parses a SDF file and builds up a tree representing the kinematic structure of a robot.
        Explanation: The SDF file format stores links (i.e., rigid bodies) and joints (i.e., connection between links)
        in a flat structure (as opposed to a tree data structure). Links have no references while joints refer to the
        NAMES of have exactly one parent (link) and child (link). This method first resolves these cross references
        and calls the recursive SDFTree.build() method to create a tree-like data structure representing the
        kinematic tree(s) of the robot.
        :param file_name: the name of the file to open
        """

        # read the file
        # robot = sdf_model_dom.parse(file_name, silence=True)
        try:
            root = sdf_model_dom.CreateFromDocument(open(file_name).read())
        except ContentNondeterminismExceededError as e:
            logger.error("Error raised %s, %s", e, e.instance.name)
            raise e
        robot = root.model[0]
        print('The name of the robot ', robot)

        for link in robot.link:
            #  print(link.visual[0].name)
            #  print(link.visual[0].geometry[0].mesh[0].uri[0])
            #  print(link.visual[0].pose[0])
            #  print(string_to_list(link.visual[0].pose[0])[0:3])
            #  print(string_to_list(link.visual[0].pose[0])[3:])

            # mesh_url = link.visual[0].geometry[0].mesh[0].uri
            # mesh_path = mesh_url.replace('model://', '')

            # Path('C:\Program Files').parent

            #  if (link.visual[0].geometry[0].mesh[0].scale) == []:
            print('No scale')
            #  for visual in link.visual:
            # for geometry in visual.geometry:
            # if visual.geometry.mesh is not None:
            #          print('Having mesh')

            #  gg = link.visual[0].geometry
            #  for fg in gg:
            #      print(fg.mesh)

        for joint in robot.joint:
            print('Parent link:', joint.parent[0])
            print('Child link:', joint.child[0])
            print('Joint type:', joint.type)
            print('Dynamic:', joint.type)
            print('Axis xyz:', joint.axis[0].xyz[0])

        # for link in robot.link:
        #    print('Link pose:', link.pose)

        # create mapping from (parent) links to joints  (a list)
        connected_joints = {link: [joint for joint in robot.joint if link.name == joint.parent[0]] for link
                            in robot.link}

        print("connected joints: ", {j.name: l for j, l in connected_joints.items()})

        for joint in robot.joint:
            print(joint.child[0])

        # create mapping from joints to their child links (a dictionary)
        connected_links = {joint: link for link in robot.link for joint in robot.joint if
                           link.name == joint.child[0]}

        print("connected links: ", {j.name: l.name for j, l in connected_links.items()})

        # find root links (i.e., links that are NOT connected to a joint)
        child_links = [link.name for link in robot.link for joint in robot.joint if
                       link.name == joint.child[0]]

        print('child link')
        print(child_links)
        for link in child_links:
            print(link)

        print(link.name for link in robot.link if link.name not in child_links)

        ###  the link, not link name
        root_links = [link for link in robot.link if link.name not in child_links]

        print('root link')
        for link in root_links:
            print(link.name)

        logger.debug("Root links: %s", [i.name for i in root_links])
        logger.debug("connected links: %s", {j.name: l.name for j, l in connected_links.items()})

        kinematic_chains = []

        # Skips the basis links
        print('kinematic chain')
        for link in root_links:
            print(link.name)
            connected_joints[link]
            for joint in connected_joints[link]:
                print(joint.name)
                tree = SDFTree(connected_links=connected_links, connected_joints=connected_joints, robot=robot)
                print({j.name: l.name for j, l in tree.connectedLinks.items()})
                kinematic_chains.append(tree)
                tree.build(connected_links[joint], joint)

                # todo: parse joint controllers

        for chain in kinematic_chains:
            print(repr(chain.joint.name))
            print(repr(chain.link.name))
            print("connected links: ", {j.name: l.name for j, l in chain.connectedLinks.items()})
            print("connected joints: ", {j.name: l for j, l in chain.connectedJoints.items()})
            print("chain child: ", chain.children)

        # logger.debug("kinematic chains: %s", kinematic_chains)
        # print(repr(kinematic_chains))
        return robot.name, root_links, kinematic_chains  # , controller_cache, gazebo_tags

    def build(self, link, joint=None, depth=0):
        """
        Recursive function that builds up the tree representation of the robot. You do not have to call it manually (
        Called by parse).
        :param link: The link the kinematics subtree starts with
        :param joint: The joint connecting to the previous link (if any)
        """
        self.children = []
        self.joint = joint
        self.link = link
        # self.set_defaults() # todo:set defaults

        children = self.connectedJoints[link]

        for joint in children:
            tree = SDFTree(connected_links=self.connectedLinks, connected_joints=self.connectedJoints,
                           robot=self.robot)
            self.children.append(tree)
            tree.build(self.connectedLinks[joint], joint, depth + 1)

    @staticmethod
    def create_empty(name, base_link_name="base_link"):
        """
        Creates an empty tree object.

        :param name: the name of the robot the tree is representing the model of.
        :type name: string
        :return: The tree instance.
        """

        tree = SDFTree(connected_links={}, connected_joints={}, robot=urdf_dom.RobotType())
        tree.robot.name = name
        tree.link = sdf_model_dom.CTD_ANON_60()
        tree.link.name = base_link_name
        tree.robot.link.append(tree.link)
        tree.joint = sdf_model_dom.CTD_ANON_48()

        # tree.set_defaults() # todo set defaults

        # build empty gazebo tag for control plugins
        # tree.gazebo_tag = urdf_dom.GazeboType()
        # tree.robot.gazebo.append(tree.gazebo_tag)

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

        if not os.path.exists(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name))

        with open(file_name, "w") as f:
            # f.write('<?xml version="1.0" ?>')
            output = self.robot.toxml("utf-8", element_name="model").decode("utf-8")
            # output = output.replace(">", ">\n")
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

        tree = SDFTree(connected_links=self.connectedLinks, connected_joints=self.connectedJoints, robot=self.robot)
        tree.joint = sdf_model_dom.CTD_ANON_48()
        tree.link = sdf_model_dom.CTD_ANON_60()
        tree.robot.link.append(tree.link)
        tree.robot.joint.append(tree.joint)
        tree.set_defaults()
        tree.joint.child = sdf_model_dom.CTD_ANON_48_child()
        tree.joint.parent = sdf_model_dom.CTD_ANON_48_parent()

        self.connectedLinks[tree.joint] = tree.link
        if self.link in self.connectedJoints:
            self.connectedJoints[self.link].append(tree.joint)
        else:
            self.connectedJoints[self.link] = [tree.joint]

        return tree

    def add_mesh(self, file_name, scale_factor=(1.0, 1.0, 1.0)):
        """
        Adds a mesh to current segment.

        :param file_name: Name of the file
        :type file_name: string
        :return:
        """
        visual = sdf_model_dom.CTD_ANON_96()  # CTD_ANON_60_visual  CTD_ANON_96
        self.link.visual.append(visual)
        visual.geometry = sdf_model_dom.CTD_ANON_96.geometry()
        visual.origin = sdf_model_dom.CTD_ANON_96.pose()
        visual.geometry.mesh = sdf_model_dom.CTD_ANON_70()
        visual.geometry.mesh.filename = file_name
        visual.geometry.mesh.scale = list_to_string(scale_factor)
        return visual

    def add_collisionmodel(self, file_name, scale_factor=(1.0, 1.0, 1.0)):
        """
        Add a collision model to a mesh object

        :param   file_name:  name of the mesh object for which the col_model is generated
        :type    file_name:  string
        :return: string:     Collision file that is used in the urdf
        """
        collision = sdf_model_dom.CTD_ANON_15()
        self.link.collision.append(collision)
        collision.geometry = sdf_model_dom.CTD_ANON_15.geometry()
        collision.origin = sdf_model_dom.CTD_ANON_15.pose()
        collision.geometry.mesh = sdf_model_dom.CTD_ANON_70()
        # print('debug add_collisionmodel: ' + file_name)
        collision.geometry.mesh.filename = file_name
        collision.geometry.mesh.scale = list_to_string(scale_factor)
        return collision

    def add_inertial(self):
        """
        Add a inertial definition to a link object

        :return: string:     reference to inertial object
        """
        inertial = sdf_model_dom.CTD_ANON_46()
        self.link.inertial.append(inertial)
        inertial.mass = sdf_model_dom.CTD_ANON_46.mass()
        inertial.mass.value_ = "1.0"
        inertial.inertia = sdf_model_dom.CTD_ANON_46()
        inertial.inertia.ixx = inertial.inertia.izz = inertial.inertia.iyy = "1.0"
        inertial.inertia.ixy = inertial.inertia.ixz = inertial.inertia.iyz = "0.0"
        inertial.origin = sdf_model_dom.CTD_ANON_46.pose()
        inertial.origin.xyz = "0 0 0"
        inertial.origin.rpy = "0 0 0"

        # print('debug add_inertial: ')
        return inertial

        # def add_joint_control_plugin(self):
        #    """
        #    Adds a reference to the generic control plugin of the NRP backend.

        #   :return: Reference to the plugin type defined in the URDF
        #   """

        #   plugin = urdf_dom.GazeboPluginType()
        #   plugin.name = "generic_controller"
        #   plugin.filename = "libgeneric_controller_plugin.so"
        #   self.gazebo_tag.plugin.append(plugin)

    #    return plugin

    # def add_joint_controller(self, control_plugin):
    #    """
    #    Add a controller definition to a robot object

    #    :return: string:     reference to inertial object
    #    """
    #    joint_controller = urdf_dom.GenericControllerPluginDefType()
    #    if joint_controller.pid == "1.0 1.0 1.0":
    #        joint_controller.pid = "100.0 1.0 1.0"
    #        print("Debug: Joint Controller set")

    #    control_plugin.append(joint_controller)
    #    print("Added joint controller.")

    #    return joint_controller

    def set_defaults(self):
        """
        Adds defaults to missing values.
        """

        joint = self.joint
        link = self.link
        if joint.axis is None:
            joint.axis = sdf_model_dom.CTD_ANON_49()

        if joint.limit is None:
            joint.limit = sdf_model_dom.CTD_ANON_51()
            # this had to be completely defined (missing effor argument caused conversion to SDF to fail)
            joint.limit.effort = 100.0
            joint.limit.lower = joint.limit.upper = joint.limit.velocity = 1.0

        # if joint.calibration is None:  # todo calibration tag ignored
        #    joint.calibration = sdf_model_dom.CalibrationType()
        #    joint.calibration.reference_position = 0.0
        #    joint.calibration.rising = 0.0  # there are no default values in the XSD?
        #    joint.calibration.falling = 0.0

        if joint.origin is None:
            joint.origin = sdf_model_dom.CTD_ANON_48.pose()
            # joint.rpy =

        for visual in link.visual:
            if visual.origin is None:
                visual.origin = sdf_model_dom.CTD_ANON_96.pose()

        for collision in link.collision:
            if collision.origin is None:
                collision.origin = sdf_model_dom.CTD_ANON_15.pose()

        if joint.dynamics is None:
            joint.dynamics = sdf_model_dom.CTD_ANON_49.dynamics()
            joint.dynamics.damping = 1.0

        if link.inertial is None:
            logger.debug("Inertial is None, creating default one.")
            link.inertial = sdf_model_dom.CTD_ANON_46()

        for inertial in link.inertial:
            if inertial.mass is None:
                inertial.mass = sdf_model_dom.CTD_ANON_46.mass()
            if inertial.inertia is None:
                inertial.inertia = sdf_model_dom.CTD_ANON_46()

                # if joint.mimic is None: # truely optional
                # if joint.safety_controller is None: # ignored

                # if link.inertial is None:

                # todo continue and remove if statements from urdf_blender

    def show(self, depth=0):
        """geometry
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
    robot = SDFTree()
    robot.parse("/home/gchen/Dropbox/project/HBP-RD/Models/husky_model/model.sdf")
    robot.show()
