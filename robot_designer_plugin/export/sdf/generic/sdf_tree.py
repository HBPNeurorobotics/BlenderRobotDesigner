import logging
import pyxb
from . import sdf_dom
from .helpers import list_to_string, string_to_list
from pyxb import ContentNondeterminismExceededError
import os

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
        self.sdf = None
        self.world = True

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
        # to add the root link to the kinematic chain, we create a virtual link on top of the root link. (temporal solution)

        try:
            root = sdf_dom.CreateFromDocument(open(file_name).read())
        except ContentNondeterminismExceededError as e:
            logger.error("Error raised %s, %s", e, e.instance.name)
            raise e
        robot = root.model[0]

        # set global pose if specified
        try:
            robot_location = string_to_list(root.model[0].pose[0])[0:3]
            robot_rotation = string_to_list(root.model[0].pose[0])[3:]
        except:
            robot_location = [0, 0, 0]
            robot_rotation = [0, 0, 0]

        # get muscles
        muscles = str(robot.muscles)
        logger.debug('Muscle Path:' + muscles)

        # get controller
        # parsing joint controllers
        # create a dictionary [ joint_name, controller ] which is
        # easily searchable during tree traversal
        controller_cache = {}
        gazebo_tags = []
        # logger.debug("Built controller cache:")
        #  logger.debug(robot.plugin[0].filename)

        for plugin in robot.plugin:
            if plugin.filename == "libgeneric_controller_plugin.so":
                # store the controller in cache, so it's accessible
                # print(robot.plugin[0].orderedContent()[0])
                element = robot.plugin[0].orderedContent()[0]
                #             logger.debug("Found controller for joint: " + element.value()[0].xsdConstraintsOK(location=None) + ", caching it.")
                # controller_cache[plugin.controller[0].joint_name] = plugin.controller
                controller_cache = {controller.joint_name: controller for controller in plugin.controller}
                #              # remove last tag from the last, it is handled by controller plugin differently
                #              gazebo_tags.pop()
                logger.debug("Built controller cache:")
                logger.debug(controller_cache)

        # create mapping from (parent) links to joints  (a list)
        connected_joints = {link: [joint for joint in robot.joint if link.name == joint.parent[0]] for link
                            in robot.link}

        # create mapping from joints to their child links (a dictionary)
        connected_links = {joint: link for link in robot.link for joint in robot.joint if
                           link.name == joint.child[0]}

        # find root links (i.e., links that are NOT connected to a joint)
        child_links = [link.name for link in robot.link for joint in robot.joint if
                       (link.name == joint.child[0] and joint.parent[0] != 'world')]

        ###  the link, not link name
        root_links = [link for link in robot.link if link.name not in child_links]

        logger.debug("Root links: %s", [i.name for i in root_links])
        logger.debug("connected links: %s", {j.name: l.name for j, l in connected_links.items()})

        kinematic_chains = []

        # Skips the basis links
        # for link in root_links:
        #     for joint in connected_joints[link]:
        #         tree = SDFTree(connected_links=connected_links, connected_joints=connected_joints, robot=robot)
        #         #print({j.name: l.name for j, l in tree.connectedLinks.items()})
        #         #print(tree.joint, tree.link)
        #         kinematic_chains.append(tree)
        #         tree.build(connected_links[joint], joint)
        #
        #         # todo: parse joint controllers
        # todo: here we assume that root link has only one child link
        for link in root_links:
            # for joint in connected_joints[link]:
            tree = SDFTree(connected_links=connected_links, connected_joints=connected_joints, robot=robot)
            # print({j.name: l.name for j, l in tree.connectedLinks.items()})
            # print(tree.joint, tree.link)
            kinematic_chains.append(tree)
            tree.build(link, None)

            # todo: parse joint controllers

        logger.debug("kinematic chains: %s", kinematic_chains)
        return muscles, robot.name, robot_location, robot_rotation, root_links, kinematic_chains, controller_cache # , gazebo_tags

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
        '''
        worldlink = [joint for joint in self.connectedLinks if
                     ('_world' in joint.name and self.connectedLinks[joint] == link)]  # maybe change this?
        '''
        worldlink = [joint for joint in self.connectedLinks if
                     (joint.parent[0] == 'world' and self.connectedLinks[joint] == link)]

        if worldlink:
            self.world = True
        else:
            self.world = False

        for joint in children:
            tree = SDFTree(connected_links=self.connectedLinks, connected_joints=self.connectedJoints,
                           robot=self.robot)
            self.children.append(tree)
            tree.build(self.connectedLinks[joint], joint, depth + 1)

    @staticmethod
    def create_empty(name):
        """
        Creates an empty tree object.

        :param name: the name of the robot the tree is representing the model of.
        :type name: string
        :return: The tree instance.
        """
        sdf = sdf_dom.sdf()
        sdf.version = '1.5'
        pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(None)

        if not sdf.model:
            sdf.model.append(sdf_dom.model())
        tree = SDFTree(connected_links={}, connected_joints={}, robot=sdf.model[0])
        tree.sdf = sdf

        tree.robot.name = name
        tree.link = sdf_dom.link()

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
        print("connected joints: ", {j.name: l for j, l in self.connectedJoints.items()})

        print("connected links: ", {j.name: l.name for j, l in self.connectedLinks.items()})

        print("root link name: ", self.link.name)

        for joint, link in self.connectedLinks.items():
            joint.child.append(link.name)

        for link, joints in self.connectedJoints.items():
            for joint in joints:
                print("connected link name:", link.name)
                print("connected link linked joint name: ", joint.name)
                joint.parent.append(link.name)

        # # Connect root joints to self.link (the root link)
        # for joint in self.robot.joint:
        #     print("robot joint name: ", joint.name)
        #
        #     if joint.parent is None:
        #         joint.parent = self.link.name

        # self.connectedLinks = {key: value for key, value in self.sdf.model[0].items() if key.name != 'rd_virtual_joint'}

        self.sdf.model[0].joint = [j for j in self.sdf.model[0].joint if j.parent]
        # for j in self.sdf.model[0].joint:
        #
        #     print(j.name)
        # set sdf fixed name

        ## write sdf file
        if not os.path.exists(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name))

        with open(file_name, "w") as f:
            # f.write('<?xml version="1.0" ?>')

            output = self.sdf.toDOM().toprettyxml()

            # output = self.sdf.toprettyxml()
            # output = self.sdf.toxml("utf-8", element_name="sdf").decode("utf-8")
            # output = output.replace(">", ">\n")
            f.write(output)

    def _write(self):
        """
        Recursion that builds the creates the cross links for the DOM (might not be necessary)
        """
        pass

    def add(self):
        """
        Creates and adds another SDFTree instance to this node. Do not add children to the subtree manually as
        references are not created then. Note that if there is no robot member defined yet (i.e., you are *exporting*),
        it will be created automatically.
        :param link: a sdf_dom link element
        :param joint: a sdf_dom joint element
        :return: a reference to the newly created SDFTree instance.
        """

        tree = SDFTree(connected_links=self.connectedLinks, connected_joints=self.connectedJoints, robot=self.robot)
        tree.joint = sdf_dom.joint()
        tree.link = sdf_dom.link()
        tree.robot.link.append(tree.link)
        tree.robot.joint.append(tree.joint)
        tree.set_defaults()

        # self.connectedLinks[tree.joint] = tree.link
        # if self.link in self.connectedJoints:
        #     self.connectedJoints[self.link].append(tree.joint)
        # else:
        #     self.connectedJoints[self.link] = [tree.joint]

        # e.g., virtual joint --> base link
        self.connectedLinks[tree.joint] = tree.link
        print("connected links (joint->link): ", {j.name: l.name for j, l in self.connectedLinks.items()})

        # if self.link not in self.connectedJoints:
        #     self.connectedJoints[self.link] = []

        # for j, l in self.connectedJoints.items():
        #     if j.name == tree.joint.:
        #         self.connectedJoints[j].append(tree.joint)
        #
        #     print("connected joints: ", {j.name: l for j, l in connected_joints.items()})


        #
        # if self.link in self.connectedJoints:
        #     self.connectedJoints[self.link].append(tree.link)
        # else:
        #     self.connectedJoints[self.link] = [tree.link]

        return tree

    def add_mesh(self, file_name, scale_factor=(1.0, 1.0, 1.0)):
        """
        Adds a mesh to current segment.

        :param file_name: Name of the file
        :type file_name: string
        :return:
        """
        link_visual = sdf_dom.visual()  # CTD_ANON_97()   # CTD_ANON_60_visual  CTD_ANON_97--sdf
        link_geometry = sdf_dom.geometry()  # CTD_ANON_17()
        self.link.visual.append(link_visual)
        link_visual.geometry.append(link_geometry)  # sdf_dom.CTD_ANON_97.geometry()
        # visual. = sdf_dom.CTD_ANON_96.pose()
        link_visual.geometry[0].mesh.append(sdf_dom.mesh())
        link_visual.geometry[0].mesh[0].uri.append(file_name)
        # link_visual.geometry[0].mesh[0].scale.append(sdf_dom.CTD_ANON_68().scale()  #list_to_string(scale_factor)
        link_visual.geometry[0].mesh[0].scale.append(list_to_string(scale_factor))
        return link_visual

    def add_collision(self, file_name, scale_factor=(1.0, 1.0, 1.0)):
        """
        Add a collision model to a mesh object

        :param   file_name:  name of the mesh object for which the col_model is generated
        :type    file_name:  string
        :return: string:     Collision file that is used in the sdf
        """
        link_collision = sdf_dom.collision()  # CTD_ANON_15()
        link_geometry = sdf_dom.geometry()
        self.link.collision.append(link_collision)
        link_collision.geometry.append(link_geometry)

        link_collision.geometry[0].mesh.append(sdf_dom.mesh())
        link_collision.geometry[0].mesh[0].uri.append(file_name)

        # collision.origin = sdf_dom.CTD_ANON_15.pose()
        # collision.geometry.mesh = sdf_dom.CTD_ANON_70()
        # print('debug add_collisionmodel: ' + file_name)
        # collision.geometry.mesh.filename = file_name
        link_collision.geometry[0].mesh[0].scale.append(list_to_string(scale_factor))
        return link_collision

    def add_basic(self, tag, scale_factor=(1.0, 1.0, 1.0)):
        """
        Add a basic collision model without a mesh

        :param tag: Basic collision tag
        :param scale_factor:
        :return: string: Collision file that is used in the sdf
        """

        link_collision = sdf_dom.collision()
        link_geometry = sdf_dom.geometry()
        self.link.collision.append(link_collision)
        link_collision.geometry.append(link_geometry)

        if tag == 'BASIC_COLLISION_BOX':
            link_collision.geometry[0].box.append(sdf_dom.box())
            link_collision.geometry[0].box[0].size.append(list_to_string(scale_factor))
        elif tag == 'BASIC_COLLISION_CYLINDER':
            link_collision.geometry[0].cylinder.append(sdf_dom.cylinder())
            link_collision.geometry[0].cylinder[0].radius.append(scale_factor[0])
            link_collision.geometry[0].cylinder[0].length.append(scale_factor[2])
        elif tag == 'BASIC_COLLISION_SPHERE':
            link_collision.geometry[0].sphere.append(sdf_dom.sphere())
            link_collision.geometry[0].sphere[0].radius.append(scale_factor[0])

        return link_collision

    def add_inertial(self):
        """
        Add a inertial definition to a link object

        :return: string:     reference to inertial object
        """
        # inertial = sdf_dom.inertial()#CTD_ANON_46()
        # self.link.inertial.append(inertial)
        self.link.inertial[0].mass.append('1.0')
        self.link.inertial[0].pose.append('0 0 0 0 0 0')
        # inertial.mass.value_ = "1.0"
        # inertial.inertia = sdf_dom.inertia() #CTD_ANON_45()
        self.link.inertial[0].inertia.ixx = '1.0'
        self.link.inertial[0].inertia.iyy = '1.0'
        self.link.inertial[0].inertia.izz = '1.0'
        self.link.inertial[0].inertia.ixy = '0.0'
        self.link.inertial[0].inertia.ixz = '0.0'
        self.link.inertial[0].inertia.iyz = '0.0'

        #     = inertial.inertia.izz =  inertial.inertia.iyy = "1.0"
        # inertial.inertia.ixy = inertial.inertia.ixz =  inertial.inertia.iyz = "0.0"
        # inertial.origin = sdf_dom.CTD_ANON_46.pose()
        # inertial.origin.xyz = "0 0 0"
        # inertial.origin.rpy = "0 0 0"

        # print('debug add_inertial: ')
        return self.link.inertial[0]

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

    def add_camera_sensor(self):
        """
        Adds a sensor to current segment.

        :param file_name: Name of the file
        :type file_name: string
        :return:
        """
        link_sensor = sdf_dom.sensor()
        self.link.sensor.append(link_sensor)
        link_sensor.pose.append('0 0 0 0 0 0')
        camera = sdf_dom.camera()
        link_sensor.append(camera)
      #  image = sdf_dom.image()
      #  camera.append(image)

        return link_sensor

    def set_defaults(self):
        """
        Adds defaults to missing values.
        """

        joint = self.joint
        link = self.link

        joint.child = ''
        joint.parent = ''

        joint_axis = sdf_dom.CTD_ANON_47()
        # if not joint_axis.xyz:
        #     print(vars(joint_axis.xyz))
        #     joint_axis.xyz.append('0 0 0 0')
        # joint_axis_limit = sdf_dom.CTD_ANON_49()

        link_inertial = sdf_dom.inertial()
        link_inertial_inertia = sdf_dom.CTD_ANON_45()
        # joint_axis_xyz = joint_axis.xyz.vector3
        print('Joint Axis')
        if not joint.axis:
            joint.axis.append(joint_axis)

        # if not joint.axis[0].limit:
        #     print('Set defaults: Joint Axis Limit ')
        #     joint.axis[0].limit.append(joint_axis_limit)
        #     # joint.axis[0].limit.append(BIND())

        if not link.inertial:
            print('Set defaults: Inertia ')
            link.inertial.append(link_inertial)

        if not link.inertial[0].inertia:
            link.inertial[0].inertia.append(link_inertial_inertia)

        link.inertial[0].mass.append('1.0')
        link.inertial[0].pose.append('0 0 0 0 0 0')
        link.inertial[0].inertia[0].ixx.append(1.0)
        link.inertial[0].inertia[0].iyy.append(1.0)
        link.inertial[0].inertia[0].izz.append(1.0)
        link.inertial[0].inertia[0].ixy.append(0.0)
        link.inertial[0].inertia[0].ixz.append(0.0)
        link.inertial[0].inertia[0].iyz.append(0.0)

        # if not joint.axis[0].xyz:
        # print('Set defaults: Joint Axis xyz ')
        # print(joint.axis[0].xyz)
        # joint.axis[0].xyz.append(joint_axis_xyz)

        # if joint.limit is None:
        #     joint.limit = sdf_dom.CTD_ANON_51()
        #     # this had to be completely defined (missing effor argument caused conversion to SDF to fail)
        #     joint.limit.effort = 100.0
        #     joint.limit.lower = joint.limit.upper = joint.limit.velocity = 1.0
        #
        # #if joint.calibration is None:  # todo calibration tag ignored
        # #    joint.calibration = sdf_model_dom.CalibrationType()
        # #    joint.calibration.reference_position = 0.0
        # #    joint.calibration.rising = 0.0  # there are no default values in the XSD?
        # #    joint.calibration.falling = 0.0
        #
        # if joint.origin is None:
        #     joint.origin = sdf_dom.CTD_ANON_48.pose()
        #     # joint.rpy =
        #
        # for visual in link.visual:
        #     if visual.origin is None:
        #         visual.origin = sdf_dom.CTD_ANON_96.pose()
        #
        # for collision in link.collision:
        #     if collision.origin is None:
        #         collision.origin = sdf_dom.CTD_ANON_15.pose()
        #
        # if joint.dynamics is None:
        #     joint.dynamics = sdf_dom.CTD_ANON_49.dynamics()
        #     joint.dynamics.damping = 1.0
        #
        # if link.pose is None:
        #     logger.debug("Link pose is None, creating default one.")
        #     link.inertial = sdf_dom.CTD_ANON_58.pose()
        #
        # if link.inertial is None:
        #     logger.debug("Inertial is None, creating default one.")
        #     link.inertial = sdf_dom.CTD_ANON_58.inertial()
        #
        # for inertial in link.inertial:
        #     if inertial.mass is None:
        #         inertial.mass = sdf_dom.CTD_ANON_46.mass()
        #     if inertial.inertia is None:
        #         inertial.inertia = sdf_dom.CTD_ANON_46()

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
    robot = SDFTree()
    robot.parse("/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/mouse_v2_model/model_wo_toproot.sdf")
    robot.show()
