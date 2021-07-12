# #####
#  This file is part of the RobotDesigner developed in the Neurorobotics
#  subproject of the Human Brain Project (https://www.humanbrainproject.eu).
#
#  The Human Brain Project is a European Commission funded project
#  in the frame of the Horizon2020 FET Flagship plan.
#  (http://ec.europa.eu/programmes/horizon2020/en/h2020-section/fet-flagships)
#
#  The Robot Designer has initially been forked from the RobotEditor
#  (https://gitlab.com/h2t/roboteditor) developed at the Karlsruhe Institute
#  of Technology in the High Performance Humanoid Technologies Laboratory (H2T).
# #####

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####



import xml.etree.cElementTree as etree
import logging

logging.basicConfig(format='[%(levelname)s|%(name)s:%(lineno)03d] %(message)s')


class COLLADA(object):
    def __init__(self, doc=None):
        self.doc = doc
        if self.doc:
            self.root = self.doc.getroot()
        else:
            self.root = None
        self.logger = logging.getLogger("COLLADA")
        # self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)

        self.namespace = 'http://www.collada.org/2008/03/COLLADASchema'
        self.ns = '{%s}' % self.namespace

        # Required simply for adding rigid_bodies
        self.physics_model = None
        self.instance_physics_model = None

    # searches the root node and replaces {ns} by the namespace prefix.
    # Additional replacements are given as keywordarguments.
    def iterfind(self, s, root=None, **kw):
        kw.update({'ns': self.ns})
        if root is None:
            root = self.root
        return root.iterfind(s.format(**kw))

    def findall(self, s, root=None, warning=True, **kw):
        kw.update({'ns': self.ns})
        if root is None:
            root = self.root
        result = root.findall(s.format(**kw))
        if len(result) == 0 and warning:
            self.logger.warning('No results for query: %s\nKW:%s\nroot:%s', s, kw, root)
            raise Exception('XML element found')
        return result

    def find(self, s, root=None, warning=True, **kw):
        kw.update({'ns': self.ns})
        if root is None:
            root = self.root
        result = root.find(s.format(**kw))
        if result is None and warning:
            self.logger.warning('No results for query: %s\nKW:%s\nroot:%s', s, kw, root)
            raise Exception('XML element found')
        return result

    def getParent(self, element, root=None):
        if root is None:
            root = self.root
        it = (i for i in root.iter() if element in i)
        try:
            return next(it)
        except:
            return None

    def getID(self, instance):
        return instance.get('url').lstrip('#')

    def setID(self, instance, target):
        instance.set('url', target.get('id'))

    def makeSIDREF(self, id_, *sid):
        return '/'.join([id_.get('id')] + [i.get('sid') for i in sid])

    def makeSID(self, id_, *sid):
        try:
            return '@'.join([id_.get('id')] + [i.get('sid') for i in sid])
        except Exception as e:
            print(id_, sid, [i.get('sid') for i in sid])
            raise e

    def findByText(self, s, text, root=None, **kw):
        return next((i for i in self.findall(s, root, **kw) if i.text == text))  # ,None)
        # return next((i for i in self.iterfind(s,root,**kw) if i.text==text))#,None)

    def read(self, filename):
        self.doc = etree.parse(filename)
        self.root = doc.getroot()

    # Searchstrings formulated in ElemenPath (XPath for Elementree)
    # Helps resolving cross references within the collada document
    # should be used with collada.find() and collada.iterfind()
    # variables (in curly brackets) should then be specified as
    # keyword arguments in these functions with the exception of `root' which is
    # reserved with the topmost Element to look in.
    # E.g., collada.find(KINEMATICS_MODEL_ID,id="Armar4")

    VISUAL_SCENE = '{ns}library_visual_scenes/{ns}visual_scene'
    VISUAL_SCENE_ID = VISUAL_SCENE + '[@id="{id}"]'
    VISUAL_SCENE_TYPE_SID = VISUAL_SCENE_ID + \
                            '//{ns}node[@sid="{sid}"][@type="{type}"]'  # Type either 'JOINT' or 'NODE'
    VISUAL_SCENE_SID = VISUAL_SCENE_ID + '//{ns}node[@sid="{sid}"]'
    VISUAL_SCENE_NAME = VISUAL_SCENE_ID + '//{ns}node[@name="{name}"]'
    VISUAL_SCENE_2SID = VISUAL_SCENE_SID + '//*[@sid="{sid2}"]'

    JOINT = '{ns}library_joints/{ns}joint'
    JOINT_ID = JOINT + '[@id="{id}"]'
    JOINT_SID = JOINT_ID + '//*[@sid="{sid}"]'

    KINEMATICS_MODEL = '{ns}library_kinematics_models/{ns}kinematics_model'
    KINEMATICS_MODEL_ID = KINEMATICS_MODEL + '[@id="{id}"]'
    KINEMATICS_MODEL_SID = KINEMATICS_MODEL_ID + '//*[@sid="{sid}"]'

    ARTICULATED_SYSTEMS_MOTION = '{ns}library_articulated_systems/{ns}articulated_system[{ns}motion]'
    ARTICULATED_SYSTEMS_MOTION_ID = ARTICULATED_SYSTEMS_MOTION + '[@id="{id}"]'
    ARTICULATED_SYSTEMS_MOTION_SID = ARTICULATED_SYSTEMS_MOTION_ID + '//*[@sid="{sid}"]'
    ARTICULATED_SYSTEMS_MOTION_AXIS_INFO = ARTICULATED_SYSTEMS_MOTION_ID + \
                                           '/{ns}motion/{ns}technique_common/{ns}axis_info[@axis="{axis}"]'

    ARTICULATED_SYSTEMS_KINEMATICS = '{ns}library_articulated_systems/{ns}articulated_system[{ns}kinematics]'
    ARTICULATED_SYSTEMS_KINEMATICS_ID = ARTICULATED_SYSTEMS_KINEMATICS + '[@id="{id}"]'
    ARTICULATED_SYSTEMS_KINEMATICS_SID = ARTICULATED_SYSTEMS_KINEMATICS_ID + '//*[@sid="{sid}"]'
    ARTICULATED_SYSTEMS_KINEMATICS_AXIS_INFO = ARTICULATED_SYSTEMS_KINEMATICS_ID + \
                                               '/{ns}kinematics/{ns}technique_common/{ns}axis_info[@axis="{axis}"]'

    KINEMATICS_SCENES = '{ns}library_kinematics_scenes/{ns}kinematics_scene'
    KINEMATICS_SCENES_ID = KINEMATICS_SCENES + '[@id="{id}"]'
    KINEMATICS_SCENES_SYMBOL = KINEMATICS_SCENES_ID + '//*[@symbol="{symbol}"]'

    SCENE = '{ns}scene'
    SCENE_INSTANCE_KINEMATICS_SCENE = '{ns}scene/{ns}instance_kinematics_scene'
    SCENE_INSTANCE_VISUAL_SCENE = '{ns}scene/{ns}instance_visual_scene'

    SCENE_BIND_JOINT_AXIS = SCENE_INSTANCE_KINEMATICS_SCENE + '/{ns}bind_joint_axis'
    SCENE_BIND_JOINT_AXIS_TARGET = SCENE_BIND_JOINT_AXIS + '[@target="{target}"]'
    SCENE_BIND_KINEMATICS_MODEL = SCENE_INSTANCE_KINEMATICS_SCENE + '/{ns}bind_kinematics_model'
    SCENE_BIND_KINEMATICS_MODEL_NODE = SCENE_BIND_KINEMATICS_MODEL + '[@node="{node}"]'

    LIBRARY_PHYSICS_SCENES = '{ns}library_physics_scenes'
    LIBRARY_PHYSICS_MODELS = '{ns}library_physics_models'

    def SubElement(self, parent, tag, attrib=None):
        if not attrib:
            attrib = {}
        return etree.SubElement(parent, tag.format(ns=self.ns), attrib)

    def SubInstance(self, parent, element):
        tag = element.tag.replace(self.ns, '{ns}instance_')
        # self.logger.debug('tag: %s', tag)
        return self.SubElement(parent, tag,
                               attrib={'url': '#' + element.get('id'), 'sid': "inst_" + element.get('id')})

    def import14(self, filename):
        self.read(filename)
        old_namespace = 'http://www.collada.org/2005/11/COLLADASchema'

        self.root.set('version', '1.5.0')
        for i in self.root.iter():
            i.tag = i.tag.replace('{%s}' % old_namespace, self.ns)

    def export14(self, filename):
        """Warning modifies the whole tree!!!"""
        old_namespace = 'http://www.collada.org/2005/11/COLLADASchema'
        self.root.set('version', '1.4.1')
        for i in self.root.iter():
            i.tag = i.tag.replace('{%s}' % self.ns, old_namespace)

        for joint in (i for i in self.root.iter() if i.get('type') == "JOINT"):
            joint.set('type', "NODE")
        self.write(filename)

    def read(self, filename):
        self.doc = etree.parse(filename)
        self.root = self.doc.getroot()

    def write(self, filename):
        # Output does not look nice. Use `xmllint --format <input> > <output>'
        # to get a nice format (part of libxml2)

        etree.register_namespace('', self.namespace)
        self.doc.write(filename, encoding="UTF-8")

    def attach(self, armature, meshes=None):

        if meshes is not None:
            armature.connectMeshes(meshes)

        library_kinematics_scenes = self.SubElement(self.root, '{ns}library_kinematics_scenes')
        library_kinematics_models = self.SubElement(self.root, '{ns}library_kinematics_models')
        library_articulated_systems = self.SubElement(self.root, '{ns}library_articulated_systems')
        library_joints = self.SubElement(self.root, '{ns}library_joints')

        kinematics_model = self.SubElement(library_kinematics_models,
                                           '{ns}kinematics_model', {'id': armature.name + '_kinematics_model'})
        self.logger.debug('kin mod:%s', etree.tostring(kinematics_model))
        kinematics_model_technique = self.SubElement(kinematics_model,
                                                     '{ns}technique_common')

        AS_kinematics = self.SubElement(library_articulated_systems,
                                        '{ns}articulated_system', {'id': armature.name + '_kinematics'})
        kinematics = self.SubElement(AS_kinematics, '{ns}kinematics')

        instance_kinematics_model = self.SubInstance(kinematics, kinematics_model)
        newparam = self.SubElement(instance_kinematics_model, '{ns}newparam',
                                   {'sid': self.makeSID(AS_kinematics, instance_kinematics_model)})
        self.SubElement(newparam, '{ns}SIDREF').text = self.makeSIDREF(AS_kinematics, instance_kinematics_model)
        AS_kinematics_technique = self.SubElement(kinematics, '{ns}technique_common')

        AS_motion = self.SubElement(library_articulated_systems,
                                    '{ns}articulated_system', {'id': armature.name + '_motion'})
        motion = self.SubElement(AS_motion, '{ns}motion')
        instance_AS_kinematics = self.SubInstance(motion, AS_kinematics)
        newparam2 = self.SubElement(instance_AS_kinematics, '{ns}newparam',
                                    {'sid': self.makeSID(AS_motion, newparam)})
        self.SubElement(newparam2, '{ns}SIDREF').text = self.makeSIDREF(AS_kinematics, newparam)
        AS_motion_technique = self.SubElement(motion, '{ns}technique_common')

        kinematics_scene = self.SubElement(library_kinematics_scenes,
                                           '{ns}kinematics_scene', {'id': armature.name + '_kinematics_scene'})
        instance_AS_motion = self.SubInstance(kinematics_scene, AS_motion)
        bind = self.SubElement(instance_AS_motion, '{ns}bind',
                               {'symbol': self.makeSID(kinematics_scene, newparam2)})
        self.SubElement(bind, '{ns}param', {'ref': self.makeSIDREF(AS_motion, newparam2)})

        scene = self.find(COLLADA.SCENE)

        # Create and export the tags required for rigid body dynamics!
        # Models are still attached in a separate function (TODO)
        library_physics_models = self.SubElement(self.root, '{ns}library_physics_models')
        library_physics_scenes = self.SubElement(self.root, '{ns}library_physics_scenes')
        self.physics_model = self.SubElement(library_physics_models, '{ns}physics_model',
                                             {'id': armature.name + '_physics_model'})
        physics_scene = self.SubElement(library_physics_scenes, 'physics_scene',
                                        {'id': armature.name + '_physics_scene'})
        self.instance_physics_model = self.SubInstance(physics_scene, self.physics_model)
        self.SubElement(physics_scene, '{ns}technique_common')
        scene = self.find(COLLADA.SCENE)
        self.SubElement(scene, '{ns}instance_physics_scene', {
            'url': '#' + armature.name + '_physics_scene'})
        # TODO make a method that creates a referenceable node (adding the #)

        # scene gotta be the last element!
        self.root.remove(scene)
        self.root.append(scene)

        instance_visual_scene = self.find(COLLADA.SCENE_INSTANCE_VISUAL_SCENE)
        # visual_scene = self.find(COLLADA.VISUAL_SCENE_ID,id=self.getID(instance_visual_scene))

        # root_node = self.find(COLLADA.VISUAL_SCENE_SID,
        #            id=self.getID(instance_visual_scene),sid=armature.name)
        # Note that this is irrelevant for import. If this changes, the root
        # node has to be addressed through an ID tag - not an SID!

        # OpenRAVE specific entries
        extra = self.SubElement(AS_motion, '{ns}extra', {'type': 'manipulator'})
        OR_technique = self.SubElement(extra, '{ns}technique', {'profile': 'OpenRAVE'})

        instance_kinematics_scene = self.SubInstance(scene, kinematics_scene)
        bind_kinematics_model = self.SubElement(instance_kinematics_scene,
                                                '{ns}bind_kinematics_model',
                                                {'node': armature.name})  # as soon as we can.
        self.SubElement(bind_kinematics_model, '{ns}param').text = bind.get('symbol')

        def parseArmature(armatureJoint, parent, depth=0):

            joint = self.SubElement(library_joints, '{ns}joint',
                                    {'id': armatureJoint.name + '_joint', 'name': armatureJoint.name + '_joint'})
            axis_type = self.SubElement(joint, '{ns}' + armatureJoint.axis_type, {'sid': 'axis0'})
            self.SubElement(axis_type, '{ns}axis').text = " ".join(str(i) for i in armatureJoint.axis)
            instance_joint = self.SubInstance(kinematics_model_technique, joint)
            # Preserve order of elements. Insert Joints from above.
            kinematics_model_technique.remove(instance_joint)
            kinematics_model_technique.insert(0, instance_joint)

            # Axis
            newparam = self.SubElement(instance_kinematics_model, '{ns}newparam',
                                       {'sid': self.makeSID(AS_kinematics, instance_kinematics_model, instance_joint,
                                                            axis_type)})
            self.SubElement(newparam, '{ns}SIDREF').text = \
                self.makeSIDREF(AS_kinematics, instance_kinematics_model, instance_joint, axis_type)
            newparam2 = self.SubElement(instance_AS_kinematics, '{ns}newparam',
                                        {'sid': self.makeSID(AS_motion, newparam)})
            self.SubElement(newparam2, '{ns}SIDREF').text = self.makeSIDREF(AS_kinematics, newparam)

            bind = self.SubElement(instance_AS_motion, '{ns}bind',
                                   {'symbol': self.makeSID(kinematics_scene, newparam2)})
            self.SubElement(bind, '{ns}param', {'ref': self.makeSIDREF(AS_motion, newparam2)})

            # Target node & transformation

            joint_node = self.find(COLLADA.VISUAL_SCENE_TYPE_SID,
                                   id=self.getID(instance_visual_scene),
                                   sid=armatureJoint.name,
                                   type='JOINT')
            transform = joint_node.find('./*[@sid="transform"]')
            # Ist eine Matrix - eventuell durch einfache rotation/translation ersetzen.

            bind_joint_axis = self.SubElement(instance_kinematics_scene,
                                              '{ns}bind_joint_axis',
                                              {'target': armatureJoint.name + '/transform'})  # As soon as we can ...

            axis = self.SubElement(bind_joint_axis, '{ns}axis')
            self.SubElement(axis, '{ns}param').text = bind.get('symbol')

            # Initial Values
            newparam = self.SubElement(instance_kinematics_model, '{ns}newparam',
                                       {'sid': self.makeSID(AS_kinematics, instance_kinematics_model,
                                                            instance_joint) + '_value'})
            self.SubElement(newparam, '{ns}float').text = armatureJoint.initialValue

            newparam2 = self.SubElement(instance_AS_kinematics, '{ns}newparam',
                                        {'sid': self.makeSID(AS_motion, newparam)})
            self.SubElement(newparam2, '{ns}SIDREF').text = self.makeSIDREF(AS_kinematics, newparam)

            bind = self.SubElement(instance_AS_motion, '{ns}bind',
                                   {'symbol': self.makeSID(kinematics_scene, newparam2)})
            self.SubElement(bind, '{ns}param', {'ref': self.makeSIDREF(AS_motion, newparam2)})

            value = self.SubElement(bind_joint_axis, '{ns}value')
            self.SubElement(value, '{ns}param').text = bind.get('symbol')

            # Axis information in <kinematics>
            axis_info_kinematics = self.SubElement(AS_kinematics_technique,
                                                   '{ns}axis_info', {
                                                       'axis': self.makeSIDREF(kinematics_model, instance_joint,
                                                                               axis_type),
                                                       'sid': instance_joint.get('sid') + '_info'})
            self.SubElement(self.SubElement(axis_info_kinematics, '{ns}active'),
                            '{ns}bool').text = armatureJoint.active
            self.SubElement(self.SubElement(axis_info_kinematics, '{ns}locked'),
                            '{ns}bool').text = armatureJoint.locked

            limits = self.SubElement(axis_info_kinematics, '{ns}limits')
            self.SubElement(self.SubElement(limits, '{ns}min'), '{ns}float').text = str(armatureJoint.min)
            self.SubElement(self.SubElement(limits, '{ns}max'), '{ns}float').text = str(armatureJoint.max)

            # Axis information in <motoin>
            axis_info_motion = self.SubElement(AS_motion_technique,
                                               '{ns}axis_info',
                                               {'axis': self.makeSIDREF(AS_kinematics, axis_info_kinematics)})

            self.SubElement(self.SubElement(axis_info_motion, '{ns}speed'),
                            '{ns}float').text = str(armatureJoint.speed)
            self.SubElement(self.SubElement(axis_info_motion, '{ns}acceleration'),
                            '{ns}float').text = str(armatureJoint.acceleration)
            self.SubElement(self.SubElement(axis_info_motion, '{ns}deceleration'),
                            '{ns}float').text = str(armatureJoint.deceleration)
            self.SubElement(self.SubElement(axis_info_motion, '{ns}jerk'),
                            '{ns}float').text = str(armatureJoint.jerk)

            attachment = self.SubElement(parent, '{ns}attachment_full',
                                         {'joint': self.makeSIDREF(kinematics_model, instance_joint)})

            for trafo in armatureJoint.transformations:
                if len(trafo) == 3:
                    el = self.SubElement(attachment, '{ns}translate')
                elif len(trafo) == 4:
                    el = self.SubElement(attachment, '{ns}rotate')
                el.text = " ".join(str(i) for i in trafo)
            # # Add offset transformation
            #            if len(armatureJoint.offsetTransformation)==3:
            #                el=self.SubElement(attachment,'{ns}translate')
            #            elif len(armatureJoint.offsetTransformation)==4:
            #                el=self.SubElement(attachment,'{ns}rotate')
            #            el.text = " ".join(str(i) for i in armatureJoint.offsetTransformation)
            #            el.set('sid','offset')

            link = self.SubElement(attachment, '{ns}link',
                                   {'sid': armatureJoint.name + '_link', 'name': armatureJoint.name + '_link'})

            # OpenRAVE specific
            if armatureJoint.frame_origin:
                self.SubElement(OR_technique, '{ns}frame_origin', {'link': self.makeSIDREF(kinematics_model, parent)})
            if armatureJoint.frame_tip:
                self.SubElement(OR_technique, '{ns}frame_tip', {'link': self.makeSIDREF(kinematics_model, link)})
            if armatureJoint.isGripper:
                e = self.SubElement(OR_technique, '{ns}gripper_joint',
                                    {'joint': self.makeSIDREF(kinematics_model, instance_joint)})
                e = self.SubElement(e, 'closing_direction', {'axis': axis_type.get('sid')})
                self.SubElement(e, 'float').text = str(armatureJoint.closingDirection)

            # for sensor in [i for i in armatureJoint.meshes if i.find ('VICON_')==0]:
            for sensor, position in armatureJoint.markers:
                extra = self.SubElement(AS_motion, '{ns}extra',
                                        {'type': 'attach_sensor', 'name': sensor})  # .replace('VICON_','')})
                technique = self.SubElement(extra, '{ns}technique', {'profile': 'OpenRAVE'})
                # node = self.find(COLLADA.VISUAL_SCENE_NAME,  id=self.getID(instance_visual_scene), name=sensor)
                frame_origin = self.SubElement(technique, '{ns}frame_origin',
                                               {'link': self.makeSIDREF(kinematics_model, link)})
                # Add the same trafos as in the visual scene!
                # for transform in (i for i in node.getchildren() if i.tag.find('instance_') == -1 ):
                #    frame_origin.append(transform)
                self.SubElement(frame_origin, '{ns}translate').text = " ".join(str(i) for i in position)
                self.SubElement(technique, '{ns}instance_sensor', {'url': 'sensors.dae#Vicon'})

            # Continue Recursion
            for child in armatureJoint.children:
                parseArmature(child, link, depth + 1)

        root_link = self.SubElement(kinematics_model_technique, '{ns}link',
                                    {'sid': armature.name + '_root_link', 'name': armature.name + '_root_link'})

        # OpenRAVE specific
        if armature.frame_origin:
            self.SubElement(OR_technique, '{ns}frame_origin', {'link': self.makeSIDREF(kinematics_model, root_link)})

        for joint in armature.children:
            parseArmature(joint, root_link)

    def addSensors(self):
        # TODO
        pass

    def extract(self):

        armature = Tree()

        # Import of COLLADA v1.5:
        # Outline:
        # 1) explore the <scene>/<instance_kinematics_scene>, look for bindings of the kinematics model.
        # 2) In <kinematics_scene> the model is either directly instantiated (NOT supported)
        #    or combined with dynamics and/or additional kinematic information (both required).
        #    Only the <articulated_system> with a <motion> element is instantiated in the
        #    <kinematics_scene>. The <articulated_system> with the <kinematics_element> is intatiated
        #    in there. This last element is the place where the <kinematics_model> is finally
        #    intatiated. This second step resolves/finds the correct model.
        # 3) The tree structure of the <kinematics_model> is parsed. Every joint(-axis) encountered
        #    gets its kinematic and dynamic information extracted. This requires visiting the
        #    whole structure up to the <scene>-object. That way the associated <node> of the
        #    current <visual_scene> is found.
        # 4) With the <node> known for each joint, the meshes can be connected. This is done by getting
        #    The parent node of the transformation in the visual scene. Every <instance_geometry> deeper in
        #    the hierarchy is assigned to the joint. This assignment takes place in the recursion of 3)
        #    The assignment consequently gets overriden by child joints. The association is stored in a global
        #    dict that is returned at the end.
        # 5) OpenRAVE requires additional information stored in the <extra>/<technique profile="OpenRAVE">
        #    element. Parameters are stored in local variables/dictionaries. (This step is actually
        #    performed earlier during 2) when the <articulated_system> with <motion> is detected)
        #    Limitations: 1 axis per joint,

        instance_kinematics_scene = self.find(COLLADA.SCENE_INSTANCE_KINEMATICS_SCENE)
        try:
            instance_visual_scene = self.find(COLLADA.SCENE_INSTANCE_VISUAL_SCENE)
            visual_scene = self.find(COLLADA.VISUAL_SCENE_ID, id=self.getID(instance_visual_scene))
        except:
            self.logger.warning('No visual scene found!')

        for bind_kinematics_model in self.findall(COLLADA.SCENE_BIND_KINEMATICS_MODEL):
            sid = bind_kinematics_model.get('node')
            if None:  # sid:
                # print(sid)
                armature.root_node = self.find(COLLADA.VISUAL_SCENE_SID,
                                               id=self.getID(instance_visual_scene), sid=sid)  # irrelevant for import
            #
            symbol = self.find('{ns}param', bind_kinematics_model).text
            bind = self.find(COLLADA.KINEMATICS_SCENES_SYMBOL,
                             id=self.getID(instance_kinematics_scene), symbol=symbol)

            # Convenience: articulated_system -> AS
            instance_AS_motion = self.getParent(bind)
            AS_motion = self.find(COLLADA.ARTICULATED_SYSTEMS_MOTION_ID,
                                  id=self.getID(instance_AS_motion))

            instance_AS_kinematics = self.find('{ns}motion/{ns}instance_articulated_system',
                                               AS_motion)
            AS_kinematics = self.find(COLLADA.ARTICULATED_SYSTEMS_KINEMATICS,
                                      id=self.getID(instance_AS_kinematics))

            [id, sid] = self.find('{ns}param', bind).get('ref').split('/')
            assert (id == AS_motion.get('id'))
            newparam = self.find(COLLADA.ARTICULATED_SYSTEMS_MOTION_SID, id=id, sid=sid)
            [id, sid] = self.find('{ns}SIDREF', newparam).text.split('/')
            newparam = self.find(COLLADA.ARTICULATED_SYSTEMS_KINEMATICS_SID, id=id, sid=sid)
            [id, sid] = self.find('{ns}SIDREF', newparam).text.split('/')
            instance_kinematics_model = self.find(COLLADA.ARTICULATED_SYSTEMS_KINEMATICS_SID,
                                                  id=id, sid=sid)

            id_kinematics_model = self.getID(instance_kinematics_model)
            kinematics_model = self.find(COLLADA.KINEMATICS_MODEL, id=id_kinematics_model)

            self.logger.info('Found kinematics model: %s', kinematics_model)
            self.logger.info('Creating Armature: %s', kinematics_model[:-9])

            # Fetch the extra OpenRAVE information
            frame_origin = None
            frame_tip = None
            gripper_axes = {}
            try:
                [id, sid] = self.find(
                    '{ns}extra[@type="manipulator"]/{ns}technique[@profile="OpenRAVE"]/{ns}frame_origin',
                    root=AS_motion).get('link').split('/')
                frame_origin = self.find(COLLADA.KINEMATICS_MODEL_SID, id=id, sid=sid)
                [id, sid] = self.find(
                    '{ns}extra[@type="manipulator"]/{ns}technique[@profile="OpenRAVE"]/{ns}frame_tip',
                    root=AS_motion).get('link').split('/')
                frame_tip = self.find(COLLADA.KINEMATICS_MODEL_SID, id=id, sid=sid)
                # dictionary: <revolute> or <prismatic> -> closing direction.

                gripper_joints = self.findall(
                    '{ns}extra[@type="manipulator"]/{ns}technique[@profile="OpenRAVE"]/{ns}gripper_joint',
                    root=AS_motion)
                for gj in gripper_joints:
                    [id, sid] = gj.get('joint').split('/')
                    joint = self.getID(self.find(COLLADA.KINEMATICS_MODEL_SID, id=id, sid=sid))

                    # dictionary: <revolute> or <prismatic> -> closing direction.
                    ga = {self.find(COLLADA.JOINT_SID, id=joint, sid=i.get('axis')): float(i[0].text)
                          for i in gj.getchildren()}
                    gripper_axes.update(ga)
            except:
                self.logger.warning('Failed to load OpenRAVE tags')

            # Dictionary in which the mesh -> joint relation is stored:
            meshes = {}

            # Now we start to recursively parse the kinematics model and
            # fetch the information for each joint.
            def parseLink(link, armature_, depth=0):
                space = '.' * depth
                self.logger.debug('%sLink: %s', space, link.get('sid'))
                if link == frame_origin:
                    self.logger.debug('%sFrame origin', space)
                    armature_.frame_origin = True

                if link == frame_tip:
                    self.logger.debug('%sFrame tip', space)
                    armature_.frame_tip = True

                for attachment in self.findall('{ns}attachment_full', link, warning=False):
                    self.logger.debug('%s%s', space, attachment.get('joint'))

                    [id, sid] = attachment.get('joint').split('/')
                    instance_joint = self.find(COLLADA.KINEMATICS_MODEL_SID, id=id, sid=sid)
                    joint = self.find(COLLADA.JOINT_ID, id=self.getID(instance_joint))

                    armatureJoint = Tree(joint.get('id').replace('_Joint', '').replace('_joint', ''))
                    armature_.addChild(armatureJoint)

                    for element in attachment:
                        if element.tag.find('link') > -1:
                            break
                        armatureJoint.addTrafo([float(i) for i in element.text.split()])

                    for axis in joint.findall('*[@sid]'):  # TODO We limit ourselves to one axis per joint!
                        armatureJoint.axis_type = axis.tag.replace(self.ns, '')
                        armatureJoint.axis = [int(i) for i in axis[0].text.split()]

                        self.logger.debug('%sAxis: %s', space, axis.get('sid'))
                        if axis in gripper_axes:
                            self.logger.debug('%sGripper Joint: Closing direction: %s', space, gripper_axes[axis])
                            armatureJoint.isGripper = True
                            armatureJoint.closingDirection = gripper_axes[axis]

                        # Where is the axis referred to in <articulated_system>/<kinematics>
                        sidref = self.findByText(
                            COLLADA.ARTICULATED_SYSTEMS_KINEMATICS_ID + '//{ns}SIDREF',
                            self.makeSIDREF(AS_kinematics, instance_kinematics_model,
                                            instance_joint, axis),
                            id=self.getID(instance_AS_kinematics)
                        )
                        newparam = self.getParent(sidref)
                        # Where is the axis referred to in <articulated_system>/<motion>
                        sidref = self.findByText(
                            COLLADA.ARTICULATED_SYSTEMS_MOTION_ID + '//{ns}SIDREF',
                            self.makeSIDREF(AS_kinematics, newparam),
                            id=self.getID(instance_AS_motion))
                        newparam = self.getParent(sidref)

                        # Where is the axis referred to in <kinematic_scene>
                        param = self.find(COLLADA.KINEMATICS_SCENES_ID + '//{ns}param[@ref="{ref}"]',
                                          ref=self.makeSIDREF(AS_motion, newparam),
                                          id=self.getID(instance_kinematics_scene))
                        bind = self.getParent(param)
                        # Where is the axis referred to in <scene>
                        param = self.findByText(COLLADA.SCENE_INSTANCE_KINEMATICS_SCENE + '//{ns}param',
                                                bind.get('symbol'))
                        bind_joint_axis = self.getParent(self.getParent(param))

                        self.logger.debug('%sBinding to node: %s', space, bind_joint_axis.get('target'))

                        # Find the connected meshes (it is an optional parameter!)
                        if bind_joint_axis.get('target'):
                            [node, trafo] = bind_joint_axis.get('target').split('/')
                            trafo = self.find(COLLADA.VISUAL_SCENE_2SID, id=visual_scene.get('id'),
                                              sid=node, sid2=trafo)
                            node = self.getParent(trafo)
                            for geometry in self.findall('.//{ns}instance_geometry', root=node):
                                meshes[self.getID(geometry)] = joint.get('id')

                        # Now, let's get the initial joint value (all the way back)
                        symbol = self.find('{ns}value/{ns}param', bind_joint_axis).text
                        param = self.find(COLLADA.KINEMATICS_SCENES_SYMBOL + '/{ns}param',
                                          id=self.getID(instance_kinematics_scene), symbol=symbol)
                        [id, sid] = param.get('ref').split('/')
                        newparam = self.find(COLLADA.ARTICULATED_SYSTEMS_MOTION_SID, id=id, sid=sid)
                        [id, sid] = self.find('{ns}SIDREF', newparam).text.split('/')
                        newparam = self.find(COLLADA.ARTICULATED_SYSTEMS_KINEMATICS_SID, id=id, sid=sid)

                        self.logger.debug('%sInitial value:%s', space, newparam[0].text)
                        armatureJoint.initialValue = newparam[0].text

                        # it should be easier to obtain the <axis_info>
                        axis_info_kinematics = self.find(
                            COLLADA.ARTICULATED_SYSTEMS_KINEMATICS_AXIS_INFO,
                            id=self.getID(instance_AS_kinematics),
                            axis=self.makeSIDREF(kinematics_model, instance_joint, axis))
                        self.logger.debug('%sactive: %s, locked: %s, min: %s, max: %s', space,
                                          axis_info_kinematics[0][0].text, axis_info_kinematics[1][0].text,
                                          axis_info_kinematics[2][0][0].text,
                                          axis_info_kinematics[2][1][0].text)
                        armatureJoint.active = axis_info_kinematics[0][0].text
                        armatureJoint.locked = axis_info_kinematics[1][0].text
                        armatureJoint.min = float(axis_info_kinematics[2][0][0].text)
                        armatureJoint.max = float(axis_info_kinematics[2][1][0].text)

                        axis_info_motion = self.find(
                            COLLADA.ARTICULATED_SYSTEMS_MOTION_AXIS_INFO,
                            id=self.getID(instance_AS_motion),
                            axis=self.makeSIDREF(AS_kinematics, axis_info_kinematics))
                        self.logger.debug('%sspeed: %s, acceleration: %s, deceleration: %s, jerk: %s', space,
                                          axis_info_motion[0][0].text, axis_info_motion[1][0].text,
                                          axis_info_motion[2][0].text,
                                          axis_info_motion[3][0].text)
                        armatureJoint.speed = float(axis_info_motion[0][0].text)
                        armatureJoint.acceleration = float(axis_info_motion[1][0].text)
                        armatureJoint.deceleration = float(axis_info_motion[2][0].text)
                        armatureJoint.jerk = float(axis_info_motion[3][0].text)

                    nextLink = self.find('{ns}link', attachment)

                    parseLink(nextLink, armatureJoint, depth + 1)

            for link in self.findall('{ns}technique_common/{ns}link', kinematics_model):
                parseLink(link, armature)

        self.logger.debug("Meshes:\n%s", meshes)

        return armature, meshes

    def addMassObject(self, name, transformations, inertia, mass, collisionModels=None,
                      collisionModelTransformations=None):

        """Incrementally learns the **previously** set training data.

        :param name: Name of the mass object
        :type name: string
        :param transformations: List of transformations to the local coordinate frame.
        :type transformations: list of tuples (with 3 or 4 elements each,
        representing translations and rotations respectively)
        :param inertia: The diagonal elements of the inertia tensor (note that it has to be axis aligned to the local
        coordinate frame)
        :type inertia: tuple or list with three elements
        :param mass: mass of the object
        :type mass: scalar
        :param collisionModels: names of the collision models
        :type collisionModels: list of strings
        :param collisionModelTransformations: Transformations of the collision models
        :type collisionModelTransformations: dictionary relating strings to list of transformations
        """
        if not collisionModels:
            collisionModels = []
        if not collisionModelTransformations:
            collisionModelTransformations = {}

        rigid_body = self.SubElement(self.physics_model, '{ns}rigid_body', {'sid': name + '_rigid_body'})
        tc = self.SubElement(rigid_body, '{ns}technique_common')
        self.SubElement(tc, 'mass').text = str(mass)
        mass_frame = self.SubElement(tc, '{ns}mass_frame')
        for t in transformations:
            if len(t) == 3:
                self.SubElement(mass_frame, '{ns}translate').text = " ".join(
                    str(i) for i in t)
            else:
                self.SubElement(mass_frame, '{ns}rotate').text = " ".join(
                    str(i) for i in t)

        self.SubElement(tc, '{ns}inertia', {'sid': 'inertia'}).text = " ".join(str(i) for i in inertia)

        instance_rigid_body = self.SubElement(self.instance_physics_model, '{ns}instance_rigid_body',
                                              {'target': "#" + name,
                                               'body': self.physics_model.get('id') + '/' + rigid_body.get('sid')})

        for model in collisionModels:
            shape = self.SubElement(rigid_body, '{ns}shape')
            self.SubElement(shape, '{ns}instance_geometry', {'url': '#' + model})
            for t in collisionModelTransformations[model]:
                if len(t) == 3:
                    self.SubElement(shape, '{ns}translate').text = " ".join(str(i) for i in t)
                else:
                    self.SubElement(shape, '{ns}rotate').text = " ".join(str(i) for i in t)


class Tree(object):
    def __init__(self, name='armature'):
        self.children = []  # Trees! check   check
        self.name = name  # check  check
        self.transformations = []  # check    check
        self.frame_origin = 'False'  # check check
        self.frame_tip = 'False'  # check check
        self.meshes = None  # check? format unclear
        self.markers = None  # check? format unclear
        self.speed = 0.0  # not yet in the GUI/boneproperty
        self.acceleration = 0.0  # not yet in the GUI/boneproperty
        self.deceleration = 0.0  # not yet in the GUI/boneproperty
        self.jerk = 0.0  # not yet in the GUI/boneproperty
        self.min = None  # check check
        self.max = None  # check check
        self.active = 'True'  # not yet in the GUI/boneproperty
        self.locked = 'False'  # not yet in the GUI/boneproperty
        self.initialValue = None  # check check
        self.axis_type = None  # check check
        self.axis = None  # check
        self.isGripper = None  # check check
        self.closingDirection = 1.0  # check check

    def addTrafo(self, trafo):
        self.transformations.append(trafo)

    def addChild(self, t):
        self.children.append(t)
        return t

    def traverse(self):
        for c in self.children:
            pass
            c.traverse()

    def connectMarkers(self, markers):
        """markers dictionary, marker_name -> tupel(joint name, relative position)"""
        pass

    def connectMeshes(self, meshes):
        self.meshes = [mesh for mesh, joint in meshes.items() if joint == self.name]
        for c in self.children:
            c.connectMeshes(meshes)

    def compare(self, other, depth=0):
        def check(v1, v2, depth, marker):
            if v1 == v2:
                match = '(OK)'
            else:
                match = '(Failed)'
            print("%s %s %s %s %s %s" % (
                str(marker * 2 * depth), str(v1), str(v2), str(type(v1)), str(type(v1)), str(match)))

        check(self.name, other.name, depth, '-')
        check(len(self.transformations), len(other.transformations), depth + 1, ' ')
        # print(str(self.transformations[0]))
        check(self.frame_origin, other.frame_origin, depth + 1, ' ')
        check(self.frame_tip, other.frame_tip, depth + 1, ' ')
        check(self.speed, other.speed, depth + 1, ' ')
        check(self.acceleration, other.acceleration, depth + 1, ' ')
        check(self.deceleration, other.deceleration, depth + 1, ' ')
        check(self.jerk, other.jerk, depth + 1, ' ')
        check(self.active, other.active, depth + 1, ' ')
        check(self.locked, other.locked, depth + 1, ' ')
        check(self.initialValue, other.initialValue, depth + 1, ' ')
        check(self.min, other.min, depth + 1, ' ')
        check(self.max, other.max, depth + 1, ' ')
        check(self.axis_type, other.axis_type, depth + 1, ' ')
        check(self.axis, other.axis, depth + 1, ' ')
        check(self.isGripper, other.isGripper, depth + 1, ' ')
        check(self.closingDirection, other.closingDirection, depth + 1, ' ')

        assert (len(self.children) == len(other.children))
        for c1, c2 in zip(self.children, other.children):
            c1.compare(c2, depth + 1)

    # Then traverse the tree
    pass


if __name__ == '__main__':

    collada = COLLADA()
    collada.read('virtual_armar3b_new_helmet.dae')
    tree, meshes = collada.extract()

    # This must be read from the old file!
    if False:
        collada = COLLADA()
        collada.import14(filename)
    else:
        root = etree.Element('%scollada' % collada.ns, {'version': '1.5'})
        scene = etree.SubElement(root, '%sscene' % collada.ns)
        doc = etree.ElementTree(root)
        collada = COLLADA(doc)

    collada.attach(tree, meshes)
    collada.write('test.dae')

    collada = COLLADA(doc)
    newtree, meshes = collada.extract()

    newtree.compare(tree)

    pass


# JUNK CODE
#    def iterJointNodes(self):
#        return self.iterfind(".//{ns}node[@type='JOINT']")
#        # Find a regular Node with id:
#        #list(root.iterfind(".//{ns}node[@type='NODE'][@id='robot']".format(**locals())))
#
#    # Replace these functions by strings!
#
#    # JOINT or JOINT_SID
#    def resolveJoint(self,id, sid=None):
#        # id and sid do NOT need double quotes! e.g.:not '"palm_Joint"' and  '"axis0"'
#        if sid:
#            return self.find('{ns}library_joints/{ns}joint[@id="{id}"]/*[@sid="{sid}"]',id=id,sid=sid)
#        else:
#            return self.find('{ns}library_joints/{ns}joint[@id="{id}"]',id=id)
#
#    # KINEMATICS_MODEL KINEMATICS_MODEL_SID
#    def resolveKinematicsModel(self,id,sid=None):
#        if sid:
#            return self.find('{ns}library_kinematics_models/{ns}kinematics_model' +
#               '[@id="{id}"]/{ns}technique_common//*[@sid="{sid}"]',
#                id=id,sid=sid)
#        else:
#            pass
#    return self.find('{ns}library_kinematics_models/{ns}kinematics_model[@id="{id}"]',id=id)
