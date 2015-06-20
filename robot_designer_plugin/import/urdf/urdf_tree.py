"""
Module for importing robots specified in the URDF file format.
"""

__author__ = 'Stefan Ulbrich'

import urdf_dom


class URDFTree(object):
    """
    A class that parses and represents a robot described by a URDF file.
    The data is stored in a tree of linked instances of this class. Therefore, a root element (or several) has to be
    detectable in the file excluding closed kinematic loops at the moment.
    Each instance represents a *blender/RobotDesigner bone* that is a compound of joint and link.
    It uses a document object model (DOM) created by generateDS.py (in version 2.14a -- the newest
    that does not depend on the lxml module, which is not included in blender).
    """

    def __init__(self, root=None):
        """ Constructor
        :param root: if specified, the constructor copies the cross-references in the XML file from another
        URDFTree instance.
        :return:
        """
        self.children = []
        self.joint = None
        self.link = None

        if root is not None:
            self.robot = root.robot
            self.connectedJoints = root.connectedJoints
            self.connectedLinks = root.connectedLinks
        else:
            self.robot = None
            self.connectedJoints = None
            self.connectedLinks = None

    def parse(self, file_name):
        """ Parses a URDF file and builds up a tree representing the kinematic structure of a robot.
        Explanation: The URDF file format stores links (i.e., rigid bodies) and joints (i.e., connection between links)
        in a flat structure (as opposed to a tree data structure). Links have no references while joints refer to the
        NAMES of have exactly one parent (link) and child (link). This method first resolves these cross references
        and calls the recursive URDFTree.build() method to create a tree-like data structure representing the
        kinematic tree(s) of the robot.
        :param file_name: the name of the file to open
        """

        # read the file
        self.robot = urdf_dom.parse(file_name, silence=True)

        # create mapping from (parent) links to joints
        self.connectedJoints = {link: [joint for joint in self.robot.joint if link.name == joint.parent.link] for link
                                in self.robot.link}

        # create mapping from joints to their child links
        self.connectedLinks = {joint: link for link in self.robot.link for joint in self.robot.joint if
                               link.name == joint.child.link}

        # find root links (i.e., links that are NOT connected to a joint)
        child_links = [link.name for link in self.robot.link for joint in self.robot.joint if
                       link.name == joint.child.link]
        root_links = [link for link in self.robot.link if link.name not in child_links]

        # print("Root links:", [i.name for i in root_links]) # Debug
        for link in root_links:
            tree = URDFTree(root=self)
            self.children.append(tree)
            tree.build(link)

    def add(self, link, joint=None):
        """
        Creates and adds another URDFTree instance to this node. Do not add children to the subtree manually as
        references are not created then. Note that if there is no robot member defined yet (i.e., you are *exporting*),
        it will be created automatically.
        :param link: a urdf_dom link element
        :param joint: a urdf_dom joint element
        :return: a reference to the newly created URDFTree instance.
        """

        # determine if we are exporting
        if self.robot is None:
            self.robot = urdf_dom.robot()

        tree = URDFTree(root=self)
        tree.joint = joint
        tree.link = link
        self.connectedLinks[joint] = link
        self.connectedJoints[self.link] = joint
        return tree

    def build(self, link, parent_joint=None):
        """
        Recursive function that builds up the tree representation of the robot. You do not have to call it manually (
        Called by parse).
        :param link: The link the kinematics subtree starts with
        :param parent_joint: The joint connecting to the previous link (if any)
        """
        self.children = []
        self.joint = parent_joint
        self.link = link

        children = self.connectedJoints[link]
        for joint in children:
            tree = URDFTree(root=self)
            self.children.append(tree)
            tree.build(self.connectedLinks[joint], joint)

    def show(self, depth=0):
        """
        Prints the kinematic tree to the command line (for debugging).
        This function serves as an example for import export.
        :param depth: the depth of the kinematics sub tree for indention
        """
        if depth > 1:
            print(
                "%s, link: %s, joint: %s, type: %s" % ("*" * depth, self.link.name, self.joint.name, self.joint.type_))
        elif depth == 1:
            print("Root link: %s" % self.link.name)
        for tree in self.children:
            tree.show(depth + 1)



def notes():
    """
    Code used for developing the URDFTree class.
    """
    # create a list of parent link - joint relations

    robot = urdf_dom.parse("../../models/hollie.urdf", silence=True)

    # wrong
    [(link.name, i.name) for link in robot.link if link.name == i.parent.link for i in robot.joint]

    # right:
    [(link.name, i.name) for link in robot.link for i in robot.joint if link.name == i.parent.link]

    # as dictionary
    # connectedJoints = {link.name: len([joint.name for joint in dom.joint if link.name==joint.parent.link]) for link in dom.link}
    connectedJoints = {link: [joint for joint in robot.joint if link.name == joint.parent.link] for link in robot.link}

    # dictionary mapping from joint to child
    connectedLinks = {joint: link for link in robot.link for joint in robot.joint if link.name == joint.child.link}

    # find non-root links
    children = [link for link in robot.link for joint in robot.joint if link.name == joint.child.link]

    # find root links
    roots = [link for link in robot.link if link.name not in children]

    def build_tree(link, depth=0):
        children = connectedJoints[link]
        for c in children:
            build_tree(connectedLinks[c], depth + 1)

    for root_link in roots:
        tree = Tree(root_link.name, root_link.type_)
        build_tree(root_link, )

# debugging the module
if __name__ == "__main__":
    robot = URDFTree()
    robot.parse("../../models/hollie.urdf")
    robot.show()
