# ./sdf_model.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-09-25 19:01:05.718182 by PyXB version 1.2.5 using Python 3.5.1.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a086fa40-8341-11e6-9413-a434d9cb994f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: vector3
class vector3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vector3')
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/types.xsd', 3, 2)
    _Documentation = None
vector3._CF_pattern = pyxb.binding.facets.CF_pattern()
vector3._CF_pattern.addPattern(pattern='(\\s*(-|\\+)?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+)\\s+){2}((-|\\+)?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+))\\s*')
vector3._InitializeFacetMap(vector3._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'vector3', vector3)
_module_typeBindings.vector3 = vector3

# Atomic simple type: quaternion
class quaternion (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'quaternion')
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/types.xsd', 9, 2)
    _Documentation = None
quaternion._CF_pattern = pyxb.binding.facets.CF_pattern()
quaternion._CF_pattern.addPattern(pattern='(\\s*(-|\\+)?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+)\\s+){3}((-|\\+)?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+))\\s*')
quaternion._InitializeFacetMap(quaternion._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'quaternion', quaternion)
_module_typeBindings.quaternion = quaternion

# Atomic simple type: vector2d
class vector2d (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vector2d')
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/types.xsd', 15, 2)
    _Documentation = None
vector2d._CF_pattern = pyxb.binding.facets.CF_pattern()
vector2d._CF_pattern.addPattern(pattern='(\\s*(-|\\+)?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+)\\s+)((-|\\+)?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+))\\s*')
vector2d._InitializeFacetMap(vector2d._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'vector2d', vector2d)
_module_typeBindings.vector2d = vector2d

# Atomic simple type: vector2i
class vector2i (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vector2i')
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/types.xsd', 21, 2)
    _Documentation = None
vector2i._CF_pattern = pyxb.binding.facets.CF_pattern()
vector2i._CF_pattern.addPattern(pattern='\\s*(-|\\+)?\\d+\\s+(-|\\+)?\\d+\\s*')
vector2i._InitializeFacetMap(vector2i._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'vector2i', vector2i)
_module_typeBindings.vector2i = vector2i

# Atomic simple type: pose
class pose (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pose')
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/types.xsd', 27, 2)
    _Documentation = None
pose._CF_pattern = pyxb.binding.facets.CF_pattern()
pose._CF_pattern.addPattern(pattern='(\\s*(-|\\+)?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+)\\s+){5}((-|\\+)?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+))\\s*')
pose._InitializeFacetMap(pose._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'pose', pose)
_module_typeBindings.pose = pose

# Atomic simple type: time
class time (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'time')
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/types.xsd', 33, 2)
    _Documentation = None
time._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'time', time)
_module_typeBindings.time = time

# Atomic simple type: color
class color (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'color')
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/types.xsd', 38, 2)
    _Documentation = None
color._CF_pattern = pyxb.binding.facets.CF_pattern()
color._CF_pattern.addPattern(pattern='(\\s*\\+?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+)\\s+){3}\\+?(\\d+(\\.\\d*)?|\\.\\d+|\\d+\\.\\d+[eE][-\\+]?[0-9]+)\\s*')
color._InitializeFacetMap(color._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'color', color)
_module_typeBindings.color = color

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element static uses Python identifier static
    __static = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'static'), 'static', '__AbsentNamespace0_CTD_ANON_static', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 17, 8), )

    
    static = property(__static.value, __static.set, None, '\n              If set to true, the model is immovable. Otherwise the model is simulated in the dynamics engine.\n            ')

    
    # Element self_collide uses Python identifier self_collide
    __self_collide = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'self_collide'), 'self_collide', '__AbsentNamespace0_CTD_ANON_self_collide', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 26, 8), )

    
    self_collide = property(__self_collide.value, __self_collide.set, None, '\n              If set to true, all links in the model will collide with each other (except those connected by a joint). Can be overridden by the link or collision element self_collide property. Two links within a model will collide if link1.self_collide OR link2.self_collide. Links connected by a joint will never collide.\n            ')

    
    # Element allow_auto_disable uses Python identifier allow_auto_disable
    __allow_auto_disable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'allow_auto_disable'), 'allow_auto_disable', '__AbsentNamespace0_CTD_ANON_allow_auto_disable', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 35, 8), )

    
    allow_auto_disable = property(__allow_auto_disable.value, __allow_auto_disable.set, None, '\n              Allows a model to auto-disable, which is means the physics engine can skip updating the model when the model is at rest. This parameter is only used by models with no joints.\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_pose', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 44, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              A position and orientation in the global coordinate frame for the model. Position(x,y,z) and rotation (roll, pitch yaw) in the global coordinate frame.\n            ')

    
    # Element include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'include'), 'include', '__AbsentNamespace0_CTD_ANON_include', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 53, 8), )

    
    include = property(__include.value, __include.set, None, '\n              Include resources from a URI. This can be used to nest models.\n            ')

    
    # Element gripper uses Python identifier gripper
    __gripper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gripper'), 'gripper', '__AbsentNamespace0_CTD_ANON_gripper', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 4, 2), )

    
    gripper = property(__gripper.value, __gripper.set, None, None)

    
    # Element joint uses Python identifier joint
    __joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'joint'), 'joint', '__AbsentNamespace0_CTD_ANON_joint', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 10, 2), )

    
    joint = property(__joint.value, __joint.set, None, None)

    
    # Element link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'link'), 'link', '__AbsentNamespace0_CTD_ANON_link', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 16, 2), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Element plugin uses Python identifier plugin
    __plugin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'plugin'), 'plugin', '__AbsentNamespace0_CTD_ANON_plugin', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2), )

    
    plugin = property(__plugin.value, __plugin.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 106, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 106, 6)
    
    name = property(__name.value, __name.set, None, '\n            A unique name for the model. This name must not match another model in the world.\n          ')

    _ElementMap.update({
        __static.name() : __static,
        __self_collide.name() : __self_collide,
        __allow_auto_disable.name() : __allow_auto_disable,
        __pose.name() : __pose,
        __include.name() : __include,
        __gripper.name() : __gripper,
        __joint.name() : __joint,
        __link.name() : __link,
        __plugin.name() : __plugin
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
              Include resources from a URI. This can be used to nest models.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 59, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__AbsentNamespace0_CTD_ANON__uri', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 62, 14), )

    
    uri = property(__uri.value, __uri.set, None, '\n                    URI to a resource, such as a model\n                  ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON__pose', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 71, 14), )

    
    pose = property(__pose.value, __pose.set, None, '\n                    Override the pose of the included model. A position and orientation in the global coordinate frame for the model. Position(x,y,z) and rotation (roll, pitch yaw) in the global coordinate frame.\n                  ')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON__name', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 80, 14), )

    
    name = property(__name.value, __name.set, None, '\n                    Override the name of the included model.\n                  ')

    
    # Element static uses Python identifier static
    __static = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'static'), 'static', '__AbsentNamespace0_CTD_ANON__static', True, pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 89, 14), )

    
    static = property(__static.value, __static.set, None, '\n                    Override the static value of the included model.\n                  ')

    _ElementMap.update({
        __uri.name() : __uri,
        __pose.name() : __pose,
        __name.name() : __name,
        __static.name() : __static
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vertical_position uses Python identifier vertical_position
    __vertical_position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vertical_position'), 'vertical_position', '__AbsentNamespace0_CTD_ANON_2_vertical_position', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 13, 8), )

    
    vertical_position = property(__vertical_position.value, __vertical_position.set, None, '\n              \n      Noise parameters for vertical position\n    \n            ')

    
    # Element vertical_velocity uses Python identifier vertical_velocity
    __vertical_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vertical_velocity'), 'vertical_velocity', '__AbsentNamespace0_CTD_ANON_2_vertical_velocity', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 28, 8), )

    
    vertical_velocity = property(__vertical_velocity.value, __vertical_velocity.set, None, '\n              \n      Noise parameters for vertical velocity\n    \n            ')

    _ElementMap.update({
        __vertical_position.name() : __vertical_position,
        __vertical_velocity.name() : __vertical_velocity
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Noise parameters for vertical position
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 21, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Noise parameters for vertical velocity
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 36, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__AbsentNamespace0_CTD_ANON_5_uri', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 13, 8), )

    
    uri = property(__uri.value, __uri.set, None, '\n              URI of the audio media.\n            ')

    
    # Element pitch uses Python identifier pitch
    __pitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pitch'), 'pitch', '__AbsentNamespace0_CTD_ANON_5_pitch', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 22, 8), )

    
    pitch = property(__pitch.value, __pitch.set, None, '\n              Pitch for the audio media, in Hz\n            ')

    
    # Element gain uses Python identifier gain
    __gain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gain'), 'gain', '__AbsentNamespace0_CTD_ANON_5_gain', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 31, 8), )

    
    gain = property(__gain.value, __gain.set, None, '\n              Gain for the audio media, in dB.\n            ')

    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact'), 'contact', '__AbsentNamespace0_CTD_ANON_5_contact', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 40, 8), )

    
    contact = property(__contact.value, __contact.set, None, '\n              List of collision objects that will trigger audio playback.\n            ')

    
    # Element loop uses Python identifier loop
    __loop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'loop'), 'loop', '__AbsentNamespace0_CTD_ANON_5_loop', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 62, 8), )

    
    loop = property(__loop.value, __loop.set, None, '\n              True to make the audio source loop playback.\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_5_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 71, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              A position and orientation in the parent coordinate frame for the audio source. Position(x,y,z) and rotation (roll, pitch yaw) in the parent coordinate frame.\n            ')

    _ElementMap.update({
        __uri.name() : __uri,
        __pitch.name() : __pitch,
        __gain.name() : __gain,
        __contact.name() : __contact,
        __loop.name() : __loop,
        __pose.name() : __pose
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """
              List of collision objects that will trigger audio playback.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 46, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element collision uses Python identifier collision
    __collision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collision'), 'collision', '__AbsentNamespace0_CTD_ANON_6_collision', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 49, 14), )

    
    collision = property(__collision.value, __collision.set, None, '\n                    Name of child collision element that will trigger audio playback.\n                  ')

    _ElementMap.update({
        __collision.name() : __collision
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/box_shape.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_CTD_ANON_7_size', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/box_shape.xsd', 13, 8), )

    
    size = property(__size.value, __size.set, None, '\n              The three side lengths of the box. The origin of the box is in its geometric center (inside the center of the box).\n            ')

    _ElementMap.update({
        __size.name() : __size
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_8_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 13, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              A position and orientation in the parent coordinate frame for the camera.\n            ')

    
    # Element horizontal_fov uses Python identifier horizontal_fov
    __horizontal_fov = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'horizontal_fov'), 'horizontal_fov', '__AbsentNamespace0_CTD_ANON_8_horizontal_fov', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 22, 8), )

    
    horizontal_fov = property(__horizontal_fov.value, __horizontal_fov.set, None, '\n              Horizontal field of view\n            ')

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__AbsentNamespace0_CTD_ANON_8_image', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 31, 8), )

    
    image = property(__image.value, __image.set, None, '\n              The image size in pixels and format.\n            ')

    
    # Element clip uses Python identifier clip
    __clip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'clip'), 'clip', '__AbsentNamespace0_CTD_ANON_8_clip', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 71, 8), )

    
    clip = property(__clip.value, __clip.set, None, '\n              The near and far clip planes. Objects closer or farther than these planes are not rendered.\n            ')

    
    # Element save uses Python identifier save
    __save = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'save'), 'save', '__AbsentNamespace0_CTD_ANON_8_save', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 102, 8), )

    
    save = property(__save.value, __save.set, None, '\n              Enable or disable saving of camera frames.\n            ')

    
    # Element depth_camera uses Python identifier depth_camera
    __depth_camera = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'depth_camera'), 'depth_camera', '__AbsentNamespace0_CTD_ANON_8_depth_camera', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 131, 8), )

    
    depth_camera = property(__depth_camera.value, __depth_camera.set, None, '\n              Depth camera parameters\n            ')

    
    # Element noise uses Python identifier noise
    __noise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'noise'), 'noise', '__AbsentNamespace0_CTD_ANON_8_noise', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 153, 8), )

    
    noise = property(__noise.value, __noise.set, None, '\n              The properties of the noise model that should be applied to generated images\n            ')

    
    # Element distortion uses Python identifier distortion
    __distortion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'distortion'), 'distortion', '__AbsentNamespace0_CTD_ANON_8_distortion', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 193, 8), )

    
    distortion = property(__distortion.value, __distortion.set, None, '\n              Lens distortion to be applied to camera images. See http://en.wikipedia.org/wiki/Distortion_(optics)#Software_correction\n            ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_8_name', pyxb.binding.datatypes.string, unicode_default='__default__')
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 260, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 260, 6)
    
    name = property(__name.value, __name.set, None, '\n            An optional name for the camera.\n          ')

    _ElementMap.update({
        __pose.name() : __pose,
        __horizontal_fov.name() : __horizontal_fov,
        __image.name() : __image,
        __clip.name() : __clip,
        __save.name() : __save,
        __depth_camera.name() : __depth_camera,
        __noise.name() : __noise,
        __distortion.name() : __distortion
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """
              The image size in pixels and format.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 37, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_CTD_ANON_9_width', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 40, 14), )

    
    width = property(__width.value, __width.set, None, '\n                    Width in pixels\n                  ')

    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_CTD_ANON_9_height', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 49, 14), )

    
    height = property(__height.value, __height.set, None, '\n                    Height in pixels \n                  ')

    
    # Element format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__AbsentNamespace0_CTD_ANON_9_format', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 58, 14), )

    
    format = property(__format.value, __format.set, None, '\n                    (L8|R8G8B8|B8G8R8|BAYER_RGGB8|BAYER_BGGR8|BAYER_GBRG8|BAYER_GRBG8)\n                  ')

    _ElementMap.update({
        __width.name() : __width,
        __height.name() : __height,
        __format.name() : __format
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """
              The near and far clip planes. Objects closer or farther than these planes are not rendered.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 77, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element near uses Python identifier near
    __near = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'near'), 'near', '__AbsentNamespace0_CTD_ANON_10_near', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 80, 14), )

    
    near = property(__near.value, __near.set, None, '\n                    Near clipping plane\n                  ')

    
    # Element far uses Python identifier far
    __far = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'far'), 'far', '__AbsentNamespace0_CTD_ANON_10_far', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 89, 14), )

    
    far = property(__far.value, __far.set, None, '\n                    Far clipping plane\n                  ')

    _ElementMap.update({
        __near.name() : __near,
        __far.name() : __far
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """
              Enable or disable saving of camera frames.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 108, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element path uses Python identifier path
    __path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'path'), 'path', '__AbsentNamespace0_CTD_ANON_11_path', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 111, 14), )

    
    path = property(__path.value, __path.set, None, '\n                    The path name which will hold the frame data. If path name is relative, then directory is relative to current working directory.\n                  ')

    
    # Attribute enabled uses Python identifier enabled
    __enabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'enabled'), 'enabled', '__AbsentNamespace0_CTD_ANON_11_enabled', pyxb.binding.datatypes.boolean, required=True)
    __enabled._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 120, 12)
    __enabled._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 120, 12)
    
    enabled = property(__enabled.value, __enabled.set, None, '\n                  True = saving enabled\n                ')

    _ElementMap.update({
        __path.name() : __path
    })
    _AttributeMap.update({
        __enabled.name() : __enabled
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """
              Depth camera parameters
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 137, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output'), 'output', '__AbsentNamespace0_CTD_ANON_12_output', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 140, 14), )

    
    output = property(__output.value, __output.set, None, '\n                    Type of output\n                  ')

    _ElementMap.update({
        __output.name() : __output
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """
              The properties of the noise model that should be applied to generated images
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 159, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_13_type', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 162, 14), )

    
    type = property(__type.value, __type.set, None, '\n                    The type of noise.  Currently supported types are: "gaussian" (draw additive noise values independently for each pixel from a Gaussian distribution).\n                  ')

    
    # Element mean uses Python identifier mean
    __mean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mean'), 'mean', '__AbsentNamespace0_CTD_ANON_13_mean', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 171, 14), )

    
    mean = property(__mean.value, __mean.set, None, '\n                    For type "gaussian," the mean of the Gaussian distribution from which noise values are drawn.\n                  ')

    
    # Element stddev uses Python identifier stddev
    __stddev = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stddev'), 'stddev', '__AbsentNamespace0_CTD_ANON_13_stddev', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 180, 14), )

    
    stddev = property(__stddev.value, __stddev.set, None, '\n                    For type "gaussian," the standard deviation of the Gaussian distribution from which noise values are drawn.\n                  ')

    _ElementMap.update({
        __type.name() : __type,
        __mean.name() : __mean,
        __stddev.name() : __stddev
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """
              Lens distortion to be applied to camera images. See http://en.wikipedia.org/wiki/Distortion_(optics)#Software_correction
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 199, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element k1 uses Python identifier k1
    __k1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'k1'), 'k1', '__AbsentNamespace0_CTD_ANON_14_k1', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 202, 14), )

    
    k1 = property(__k1.value, __k1.set, None, '\n                    The radial distortion coefficient k1\n                  ')

    
    # Element k2 uses Python identifier k2
    __k2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'k2'), 'k2', '__AbsentNamespace0_CTD_ANON_14_k2', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 211, 14), )

    
    k2 = property(__k2.value, __k2.set, None, '\n                    The radial distortion coefficient k2\n                  ')

    
    # Element k3 uses Python identifier k3
    __k3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'k3'), 'k3', '__AbsentNamespace0_CTD_ANON_14_k3', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 220, 14), )

    
    k3 = property(__k3.value, __k3.set, None, '\n                    The radial distortion coefficient k3\n                  ')

    
    # Element p1 uses Python identifier p1
    __p1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'p1'), 'p1', '__AbsentNamespace0_CTD_ANON_14_p1', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 229, 14), )

    
    p1 = property(__p1.value, __p1.set, None, '\n                    The tangential distortion coefficient p1\n                  ')

    
    # Element p2 uses Python identifier p2
    __p2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'p2'), 'p2', '__AbsentNamespace0_CTD_ANON_14_p2', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 238, 14), )

    
    p2 = property(__p2.value, __p2.set, None, '\n                    The tangential distortion coefficient p2\n                  ')

    
    # Element center uses Python identifier center
    __center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'center'), 'center', '__AbsentNamespace0_CTD_ANON_14_center', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 247, 14), )

    
    center = property(__center.value, __center.set, None, '\n                    The distortion center or principal point\n                  ')

    _ElementMap.update({
        __k1.name() : __k1,
        __k2.name() : __k2,
        __k3.name() : __k3,
        __p1.name() : __p1,
        __p2.name() : __p2,
        __center.name() : __center
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 12, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element laser_retro uses Python identifier laser_retro
    __laser_retro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'laser_retro'), 'laser_retro', '__AbsentNamespace0_CTD_ANON_15_laser_retro', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 15, 8), )

    
    laser_retro = property(__laser_retro.value, __laser_retro.set, None, '\n              intensity value returned by laser sensor.\n            ')

    
    # Element max_contacts uses Python identifier max_contacts
    __max_contacts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_contacts'), 'max_contacts', '__AbsentNamespace0_CTD_ANON_15_max_contacts', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 24, 8), )

    
    max_contacts = property(__max_contacts.value, __max_contacts.set, None, '\n              Maximum number of contacts allowed between two entities. This value overrides the max_contacts element defined in physics.\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_15_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 33, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              The reference frame of the collision element, relative to the reference frame of the link.\n            ')

    
    # Element geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geometry'), 'geometry', '__AbsentNamespace0_CTD_ANON_15_geometry', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 17, 2), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Element surface uses Python identifier surface
    __surface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'surface'), 'surface', '__AbsentNamespace0_CTD_ANON_15_surface', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 9, 2), )

    
    surface = property(__surface.value, __surface.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_15_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 44, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 44, 6)
    
    name = property(__name.value, __name.set, None, '\n            Unique name for the collision element within the scope of the parent link.\n          ')

    _ElementMap.update({
        __laser_retro.name() : __laser_retro,
        __max_contacts.name() : __max_contacts,
        __pose.name() : __pose,
        __geometry.name() : __geometry,
        __surface.name() : __surface
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element collision uses Python identifier collision
    __collision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collision'), 'collision', '__AbsentNamespace0_CTD_ANON_16_collision', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 13, 8), )

    
    collision = property(__collision.value, __collision.set, None, '\n              name of the collision element within a link that acts as the contact sensor.\n            ')

    
    # Element topic uses Python identifier topic
    __topic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'topic'), 'topic', '__AbsentNamespace0_CTD_ANON_16_topic', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 22, 8), )

    
    topic = property(__topic.value, __topic.set, None, '\n              Topic on which contact data is published.\n            ')

    _ElementMap.update({
        __collision.name() : __collision,
        __topic.name() : __topic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_CTD_ANON_17_radius', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 13, 8), )

    
    radius = property(__radius.value, __radius.set, None, '\n              Radius of the cylinder\n            ')

    
    # Element length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_CTD_ANON_17_length', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 22, 8), )

    
    length = property(__length.value, __length.set, None, '\n              Length of the cylinder\n            ')

    _ElementMap.update({
        __radius.name() : __radius,
        __length.name() : __length
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element frame uses Python identifier frame
    __frame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'frame'), 'frame', '__AbsentNamespace0_CTD_ANON_18_frame', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 13, 8), )

    
    frame = property(__frame.value, __frame.set, None, '\n              \n      Frame in which to report the wrench values. Currently supported frames are:\n        "parent" report the wrench expressed in the orientation of the parent link frame,\n        "child" report the wrench expressed in the orientation of the child link frame,\n        "sensor" report the wrench expressed in the orientation of the joint sensor frame.\n      Note that for each option the point with respect to which the \n      torque component of the wrench is expressed is the joint origin.\n    \n            ')

    
    # Element measure_direction uses Python identifier measure_direction
    __measure_direction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'measure_direction'), 'measure_direction', '__AbsentNamespace0_CTD_ANON_18_measure_direction', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 29, 8), )

    
    measure_direction = property(__measure_direction.value, __measure_direction.set, None, '\n              \n      Direction of the wrench measured by the sensor. The supported options are:\n        "parent_to_child" if the measured wrench is the one applied by parent link on the child link,\n        "child_to_parent" if the measured wrench is the one applied by the child link on the parent link.\n    \n            ')

    _ElementMap.update({
        __frame.name() : __frame,
        __measure_direction.name() : __measure_direction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 18, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element box uses Python identifier box
    __box = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'box'), 'box', '__AbsentNamespace0_CTD_ANON_19_box', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/box_shape.xsd', 9, 2), )

    
    box = property(__box.value, __box.set, None, None)

    
    # Element cylinder uses Python identifier cylinder
    __cylinder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cylinder'), 'cylinder', '__AbsentNamespace0_CTD_ANON_19_cylinder', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 9, 2), )

    
    cylinder = property(__cylinder.value, __cylinder.set, None, None)

    
    # Element empty uses Python identifier empty
    __empty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'empty'), 'empty', '__AbsentNamespace0_CTD_ANON_19_empty', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 21, 8), )

    
    empty = property(__empty.value, __empty.set, None, '\n              You can use the empty tag to make empty geometries.\n            ')

    
    # Element heightmap uses Python identifier heightmap
    __heightmap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heightmap'), 'heightmap', '__AbsentNamespace0_CTD_ANON_19_heightmap', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 9, 2), )

    
    heightmap = property(__heightmap.value, __heightmap.set, None, None)

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'image'), 'image', '__AbsentNamespace0_CTD_ANON_19_image', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 9, 2), )

    
    image = property(__image.value, __image.set, None, None)

    
    # Element mesh uses Python identifier mesh
    __mesh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mesh'), 'mesh', '__AbsentNamespace0_CTD_ANON_19_mesh', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 9, 2), )

    
    mesh = property(__mesh.value, __mesh.set, None, None)

    
    # Element plane uses Python identifier plane
    __plane = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'plane'), 'plane', '__AbsentNamespace0_CTD_ANON_19_plane', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 9, 2), )

    
    plane = property(__plane.value, __plane.set, None, None)

    
    # Element polyline uses Python identifier polyline
    __polyline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'polyline'), 'polyline', '__AbsentNamespace0_CTD_ANON_19_polyline', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 9, 2), )

    
    polyline = property(__polyline.value, __polyline.set, None, None)

    
    # Element sphere uses Python identifier sphere
    __sphere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sphere'), 'sphere', '__AbsentNamespace0_CTD_ANON_19_sphere', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sphere_shape.xsd', 9, 2), )

    
    sphere = property(__sphere.value, __sphere.set, None, None)

    _ElementMap.update({
        __box.name() : __box,
        __cylinder.name() : __cylinder,
        __empty.name() : __empty,
        __heightmap.name() : __heightmap,
        __image.name() : __image,
        __mesh.name() : __mesh,
        __plane.name() : __plane,
        __polyline.name() : __polyline,
        __sphere.name() : __sphere
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """
              You can use the empty tag to make empty geometries.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 27, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element position_sensing uses Python identifier position_sensing
    __position_sensing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'position_sensing'), 'position_sensing', '__AbsentNamespace0_CTD_ANON_21_position_sensing', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 13, 8), )

    
    position_sensing = property(__position_sensing.value, __position_sensing.set, None, '\n              \n      Parameters related to GPS position measurement.\n    \n            ')

    
    # Element velocity_sensing uses Python identifier velocity_sensing
    __velocity_sensing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'velocity_sensing'), 'velocity_sensing', '__AbsentNamespace0_CTD_ANON_21_velocity_sensing', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 58, 8), )

    
    velocity_sensing = property(__velocity_sensing.value, __velocity_sensing.set, None, '\n              \n      Parameters related to GPS position measurement.\n    \n            ')

    _ElementMap.update({
        __position_sensing.name() : __position_sensing,
        __velocity_sensing.name() : __velocity_sensing
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Parameters related to GPS position measurement.
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 21, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element horizontal uses Python identifier horizontal
    __horizontal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'horizontal'), 'horizontal', '__AbsentNamespace0_CTD_ANON_22_horizontal', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 24, 14), )

    
    horizontal = property(__horizontal.value, __horizontal.set, None, '\n                    \n        Noise parameters for horizontal position measurement, in units of meters.\n      \n                  ')

    
    # Element vertical uses Python identifier vertical
    __vertical = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vertical'), 'vertical', '__AbsentNamespace0_CTD_ANON_22_vertical', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 39, 14), )

    
    vertical = property(__vertical.value, __vertical.set, None, '\n                    \n        Noise parameters for vertical position measurement, in units of meters.\n      \n                  ')

    _ElementMap.update({
        __horizontal.name() : __horizontal,
        __vertical.name() : __vertical
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """
                    
        Noise parameters for horizontal position measurement, in units of meters.
      
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 32, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """
                    
        Noise parameters for vertical position measurement, in units of meters.
      
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 47, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Parameters related to GPS position measurement.
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 66, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element horizontal uses Python identifier horizontal
    __horizontal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'horizontal'), 'horizontal', '__AbsentNamespace0_CTD_ANON_25_horizontal', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 69, 14), )

    
    horizontal = property(__horizontal.value, __horizontal.set, None, '\n                    \n        Noise parameters for horizontal velocity measurement, in units of meters/second.\n      \n                  ')

    
    # Element vertical uses Python identifier vertical
    __vertical = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vertical'), 'vertical', '__AbsentNamespace0_CTD_ANON_25_vertical', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 84, 14), )

    
    vertical = property(__vertical.value, __vertical.set, None, '\n                    \n        Noise parameters for vertical velocity measurement, in units of meters/second.\n      \n                  ')

    _ElementMap.update({
        __horizontal.name() : __horizontal,
        __vertical.name() : __vertical
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """
                    
        Noise parameters for horizontal velocity measurement, in units of meters/second.
      
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 77, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_26 = CTD_ANON_26


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """
                    
        Noise parameters for vertical velocity measurement, in units of meters/second.
      
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 92, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_27 = CTD_ANON_27


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 5, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element grasp_check uses Python identifier grasp_check
    __grasp_check = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'grasp_check'), 'grasp_check', '__AbsentNamespace0_CTD_ANON_28_grasp_check', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 8, 8), )

    
    grasp_check = property(__grasp_check.value, __grasp_check.set, None, None)

    
    # Element gripper_link uses Python identifier gripper_link
    __gripper_link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gripper_link'), 'gripper_link', '__AbsentNamespace0_CTD_ANON_28_gripper_link', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 28, 8), )

    
    gripper_link = property(__gripper_link.value, __gripper_link.set, None, None)

    
    # Element palm_link uses Python identifier palm_link
    __palm_link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'palm_link'), 'palm_link', '__AbsentNamespace0_CTD_ANON_28_palm_link', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 32, 8), )

    
    palm_link = property(__palm_link.value, __palm_link.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_28_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 36, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 36, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __grasp_check.name() : __grasp_check,
        __gripper_link.name() : __gripper_link,
        __palm_link.name() : __palm_link
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_28 = CTD_ANON_28


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 9, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element detach_steps uses Python identifier detach_steps
    __detach_steps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'detach_steps'), 'detach_steps', '__AbsentNamespace0_CTD_ANON_29_detach_steps', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 12, 14), )

    
    detach_steps = property(__detach_steps.value, __detach_steps.set, None, None)

    
    # Element attach_steps uses Python identifier attach_steps
    __attach_steps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'attach_steps'), 'attach_steps', '__AbsentNamespace0_CTD_ANON_29_attach_steps', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 16, 14), )

    
    attach_steps = property(__attach_steps.value, __attach_steps.set, None, None)

    
    # Element min_contact_count uses Python identifier min_contact_count
    __min_contact_count = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_contact_count'), 'min_contact_count', '__AbsentNamespace0_CTD_ANON_29_min_contact_count', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 20, 14), )

    
    min_contact_count = property(__min_contact_count.value, __min_contact_count.set, None, None)

    _ElementMap.update({
        __detach_steps.name() : __detach_steps,
        __attach_steps.name() : __attach_steps,
        __min_contact_count.name() : __min_contact_count
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_29 = CTD_ANON_29


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__AbsentNamespace0_CTD_ANON_30_uri', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 13, 8), )

    
    uri = property(__uri.value, __uri.set, None, '\n              URI to a grayscale image file\n            ')

    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_CTD_ANON_30_size', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 22, 8), )

    
    size = property(__size.value, __size.set, None, '\n              The size of the heightmap in world units.\n      When loading an image: "size" is used if present, otherwise defaults to 1x1x1.\n      When loading a DEM: "size" is used if present, otherwise defaults to true size of DEM.\n  \n            ')

    
    # Element pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pos'), 'pos', '__AbsentNamespace0_CTD_ANON_30_pos', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 34, 8), )

    
    pos = property(__pos.value, __pos.set, None, '\n              A position offset.\n            ')

    
    # Element texture uses Python identifier texture
    __texture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'texture'), 'texture', '__AbsentNamespace0_CTD_ANON_30_texture', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 43, 8), )

    
    texture = property(__texture.value, __texture.set, None, '\n              The heightmap can contain multiple textures. The order of the texture matters. The first texture will appear at the lowest height, and the last texture at the highest height. Use blend to control the height thresholds and fade between textures.\n            ')

    
    # Element blend uses Python identifier blend
    __blend = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'blend'), 'blend', '__AbsentNamespace0_CTD_ANON_30_blend', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 83, 8), )

    
    blend = property(__blend.value, __blend.set, None, '\n              The blend tag controls how two adjacent textures are mixed. The number of blend elements should equal one less than the number of textures.\n            ')

    
    # Element use_terrain_paging uses Python identifier use_terrain_paging
    __use_terrain_paging = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'use_terrain_paging'), 'use_terrain_paging', '__AbsentNamespace0_CTD_ANON_30_use_terrain_paging', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 114, 8), )

    
    use_terrain_paging = property(__use_terrain_paging.value, __use_terrain_paging.set, None, '\n              Set if the rendering engine will use terrain paging\n            ')

    _ElementMap.update({
        __uri.name() : __uri,
        __size.name() : __size,
        __pos.name() : __pos,
        __texture.name() : __texture,
        __blend.name() : __blend,
        __use_terrain_paging.name() : __use_terrain_paging
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_30 = CTD_ANON_30


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """
              The heightmap can contain multiple textures. The order of the texture matters. The first texture will appear at the lowest height, and the last texture at the highest height. Use blend to control the height thresholds and fade between textures.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 49, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_CTD_ANON_31_size', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 52, 14), )

    
    size = property(__size.value, __size.set, None, '\n                    Size of the applied texture in meters.\n                  ')

    
    # Element diffuse uses Python identifier diffuse
    __diffuse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'diffuse'), 'diffuse', '__AbsentNamespace0_CTD_ANON_31_diffuse', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 61, 14), )

    
    diffuse = property(__diffuse.value, __diffuse.set, None, '\n                    Diffuse texture image filename\n                  ')

    
    # Element normal uses Python identifier normal
    __normal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'normal'), 'normal', '__AbsentNamespace0_CTD_ANON_31_normal', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 70, 14), )

    
    normal = property(__normal.value, __normal.set, None, '\n                    Normalmap texture image filename\n                  ')

    _ElementMap.update({
        __size.name() : __size,
        __diffuse.name() : __diffuse,
        __normal.name() : __normal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_31 = CTD_ANON_31


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """
              The blend tag controls how two adjacent textures are mixed. The number of blend elements should equal one less than the number of textures.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 89, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element min_height uses Python identifier min_height
    __min_height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_height'), 'min_height', '__AbsentNamespace0_CTD_ANON_32_min_height', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 92, 14), )

    
    min_height = property(__min_height.value, __min_height.set, None, '\n                    Min height of a blend layer\n                  ')

    
    # Element fade_dist uses Python identifier fade_dist
    __fade_dist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fade_dist'), 'fade_dist', '__AbsentNamespace0_CTD_ANON_32_fade_dist', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 101, 14), )

    
    fade_dist = property(__fade_dist.value, __fade_dist.set, None, '\n                    Distance over which the blend occurs\n                  ')

    _ElementMap.update({
        __min_height.name() : __min_height,
        __fade_dist.name() : __fade_dist
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_32 = CTD_ANON_32


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__AbsentNamespace0_CTD_ANON_33_uri', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 13, 8), )

    
    uri = property(__uri.value, __uri.set, None, '\n              URI of the grayscale image file\n            ')

    
    # Element scale uses Python identifier scale
    __scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'scale'), 'scale', '__AbsentNamespace0_CTD_ANON_33_scale', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 22, 8), )

    
    scale = property(__scale.value, __scale.set, None, '\n              Scaling factor applied to the image\n            ')

    
    # Element threshold uses Python identifier threshold
    __threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'threshold'), 'threshold', '__AbsentNamespace0_CTD_ANON_33_threshold', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 31, 8), )

    
    threshold = property(__threshold.value, __threshold.set, None, '\n              Grayscale threshold\n            ')

    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_CTD_ANON_33_height', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 40, 8), )

    
    height = property(__height.value, __height.set, None, '\n              Height of the extruded boxes\n            ')

    
    # Element granularity uses Python identifier granularity
    __granularity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'granularity'), 'granularity', '__AbsentNamespace0_CTD_ANON_33_granularity', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 49, 8), )

    
    granularity = property(__granularity.value, __granularity.set, None, '\n              The amount of error in the model\n            ')

    _ElementMap.update({
        __uri.name() : __uri,
        __scale.name() : __scale,
        __threshold.name() : __threshold,
        __height.name() : __height,
        __granularity.name() : __granularity
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_33 = CTD_ANON_33


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element topic uses Python identifier topic
    __topic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'topic'), 'topic', '__AbsentNamespace0_CTD_ANON_34_topic', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 13, 8), )

    
    topic = property(__topic.value, __topic.set, None, '\n              Topic on which data is published.\n            ')

    
    # Element angular_velocity uses Python identifier angular_velocity
    __angular_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'angular_velocity'), 'angular_velocity', '__AbsentNamespace0_CTD_ANON_34_angular_velocity', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 22, 8), )

    
    angular_velocity = property(__angular_velocity.value, __angular_velocity.set, None, '\n              These elements are specific to body-frame angular velocity,\n    which is expressed in radians per second\n            ')

    
    # Element linear_acceleration uses Python identifier linear_acceleration
    __linear_acceleration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'linear_acceleration'), 'linear_acceleration', '__AbsentNamespace0_CTD_ANON_34_linear_acceleration', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 75, 8), )

    
    linear_acceleration = property(__linear_acceleration.value, __linear_acceleration.set, None, '\n              These elements are specific to body-frame linear acceleration,\n    which is expressed in meters per second squared\n            ')

    
    # Element noise uses Python identifier noise
    __noise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'noise'), 'noise', '__AbsentNamespace0_CTD_ANON_34_noise', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 128, 8), )

    
    noise = property(__noise.value, __noise.set, None, '\n              The properties of the noise model that should be applied to generated data\n            ')

    _ElementMap.update({
        __topic.name() : __topic,
        __angular_velocity.name() : __angular_velocity,
        __linear_acceleration.name() : __linear_acceleration,
        __noise.name() : __noise
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_34 = CTD_ANON_34


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """
              These elements are specific to body-frame angular velocity,
    which is expressed in radians per second
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 29, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__AbsentNamespace0_CTD_ANON_35_x', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 32, 14), )

    
    x = property(__x.value, __x.set, None, '\n                    Angular velocity about the X axis\n                  ')

    
    # Element y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__AbsentNamespace0_CTD_ANON_35_y', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 45, 14), )

    
    y = property(__y.value, __y.set, None, '\n                    Angular velocity about the Y axis\n                  ')

    
    # Element z uses Python identifier z
    __z = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'z'), 'z', '__AbsentNamespace0_CTD_ANON_35_z', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 58, 14), )

    
    z = property(__z.value, __z.set, None, '\n                    Angular velocity about the Z axis\n                  ')

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __z.name() : __z
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_35 = CTD_ANON_35


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Angular velocity about the X axis
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 38, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_36 = CTD_ANON_36


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Angular velocity about the Y axis
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 51, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_37 = CTD_ANON_37


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Angular velocity about the Z axis
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 64, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_38 = CTD_ANON_38


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """
              These elements are specific to body-frame linear acceleration,
    which is expressed in meters per second squared
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 82, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__AbsentNamespace0_CTD_ANON_39_x', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 85, 14), )

    
    x = property(__x.value, __x.set, None, '\n                    Linear acceleration about the X axis\n                  ')

    
    # Element y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__AbsentNamespace0_CTD_ANON_39_y', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 98, 14), )

    
    y = property(__y.value, __y.set, None, '\n                    Linear acceleration about the Y axis\n                  ')

    
    # Element z uses Python identifier z
    __z = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'z'), 'z', '__AbsentNamespace0_CTD_ANON_39_z', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 111, 14), )

    
    z = property(__z.value, __z.set, None, '\n                    Linear acceleration about the Z axis\n                  ')

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __z.name() : __z
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_39 = CTD_ANON_39


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Linear acceleration about the X axis
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 91, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_40 = CTD_ANON_40


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Linear acceleration about the Y axis
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 104, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_41 = CTD_ANON_41


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_42 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Linear acceleration about the Z axis
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 117, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_42 = CTD_ANON_42


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_43 (pyxb.binding.basis.complexTypeDefinition):
    """
              The properties of the noise model that should be applied to generated data
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 134, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_43_type', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 137, 14), )

    
    type = property(__type.value, __type.set, None, '\n                    The type of noise.  Currently supported types are: "gaussian" (draw noise values independently for each beam from a Gaussian distribution).\n                  ')

    
    # Element rate uses Python identifier rate
    __rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rate'), 'rate', '__AbsentNamespace0_CTD_ANON_43_rate', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 146, 14), )

    
    rate = property(__rate.value, __rate.set, None, '\n                    Noise parameters for angular rates.\n                  ')

    
    # Element accel uses Python identifier accel
    __accel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_CTD_ANON_43_accel', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 195, 14), )

    
    accel = property(__accel.value, __accel.set, None, '\n                    Noise parameters for linear accelerations.\n                  ')

    _ElementMap.update({
        __type.name() : __type,
        __rate.name() : __rate,
        __accel.name() : __accel
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_43 = CTD_ANON_43


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_44 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Noise parameters for angular rates.
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 152, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mean uses Python identifier mean
    __mean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mean'), 'mean', '__AbsentNamespace0_CTD_ANON_44_mean', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 155, 20), )

    
    mean = property(__mean.value, __mean.set, None, '\n                          For type "gaussian," the mean of the Gaussian distribution from which noise values are drawn.\n                        ')

    
    # Element stddev uses Python identifier stddev
    __stddev = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stddev'), 'stddev', '__AbsentNamespace0_CTD_ANON_44_stddev', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 164, 20), )

    
    stddev = property(__stddev.value, __stddev.set, None, '\n                          For type "gaussian," the standard deviation of the Gaussian distribution from which noise values are drawn.\n                        ')

    
    # Element bias_mean uses Python identifier bias_mean
    __bias_mean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bias_mean'), 'bias_mean', '__AbsentNamespace0_CTD_ANON_44_bias_mean', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 173, 20), )

    
    bias_mean = property(__bias_mean.value, __bias_mean.set, None, '\n                          For type "gaussian," the mean of the Gaussian distribution from which bias values are drawn.\n                        ')

    
    # Element bias_stddev uses Python identifier bias_stddev
    __bias_stddev = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bias_stddev'), 'bias_stddev', '__AbsentNamespace0_CTD_ANON_44_bias_stddev', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 182, 20), )

    
    bias_stddev = property(__bias_stddev.value, __bias_stddev.set, None, '\n                          For type "gaussian," the standard deviation of the Gaussian distribution from which bias values are drawn.\n                        ')

    _ElementMap.update({
        __mean.name() : __mean,
        __stddev.name() : __stddev,
        __bias_mean.name() : __bias_mean,
        __bias_stddev.name() : __bias_stddev
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_44 = CTD_ANON_44


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_45 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Noise parameters for linear accelerations.
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 201, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mean uses Python identifier mean
    __mean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mean'), 'mean', '__AbsentNamespace0_CTD_ANON_45_mean', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 204, 20), )

    
    mean = property(__mean.value, __mean.set, None, '\n                          For type "gaussian," the mean of the Gaussian distribution from which noise values are drawn.\n                        ')

    
    # Element stddev uses Python identifier stddev
    __stddev = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stddev'), 'stddev', '__AbsentNamespace0_CTD_ANON_45_stddev', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 213, 20), )

    
    stddev = property(__stddev.value, __stddev.set, None, '\n                          For type "gaussian," the standard deviation of the Gaussian distribution from which noise values are drawn.\n                        ')

    
    # Element bias_mean uses Python identifier bias_mean
    __bias_mean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bias_mean'), 'bias_mean', '__AbsentNamespace0_CTD_ANON_45_bias_mean', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 222, 20), )

    
    bias_mean = property(__bias_mean.value, __bias_mean.set, None, '\n                          For type "gaussian," the mean of the Gaussian distribution from which bias values are drawn.\n                        ')

    
    # Element bias_stddev uses Python identifier bias_stddev
    __bias_stddev = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bias_stddev'), 'bias_stddev', '__AbsentNamespace0_CTD_ANON_45_bias_stddev', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 231, 20), )

    
    bias_stddev = property(__bias_stddev.value, __bias_stddev.set, None, '\n                          For type "gaussian," the standard deviation of the Gaussian distribution from which bias values are drawn.\n                        ')

    _ElementMap.update({
        __mean.name() : __mean,
        __stddev.name() : __stddev,
        __bias_mean.name() : __bias_mean,
        __bias_stddev.name() : __bias_stddev
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_45 = CTD_ANON_45


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_46 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mass uses Python identifier mass
    __mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mass'), 'mass', '__AbsentNamespace0_CTD_ANON_46_mass', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 13, 8), )

    
    mass = property(__mass.value, __mass.set, None, '\n              The mass of the link.\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_46_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 22, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              This is the pose of the inertial reference frame, relative to the link reference frame. The origin of the inertial reference frame needs to be at the center of gravity. The axes of the inertial reference frame do not need to be aligned with the principal axes of the inertia.\n            ')

    
    # Element inertia uses Python identifier inertia
    __inertia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inertia'), 'inertia', '__AbsentNamespace0_CTD_ANON_46_inertia', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 31, 8), )

    
    inertia = property(__inertia.value, __inertia.set, None, '\n              The 3x3 rotational inertia matrix. Because the rotational inertia matrix is symmetric, only 6 above-diagonal elements of this matrix are specified here, using the attributes ixx, ixy, ixz, iyy, iyz, izz.\n            ')

    _ElementMap.update({
        __mass.name() : __mass,
        __pose.name() : __pose,
        __inertia.name() : __inertia
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_46 = CTD_ANON_46


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_47 (pyxb.binding.basis.complexTypeDefinition):
    """
              The 3x3 rotational inertia matrix. Because the rotational inertia matrix is symmetric, only 6 above-diagonal elements of this matrix are specified here, using the attributes ixx, ixy, ixz, iyy, iyz, izz.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 37, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ixx uses Python identifier ixx
    __ixx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ixx'), 'ixx', '__AbsentNamespace0_CTD_ANON_47_ixx', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 40, 14), )

    
    ixx = property(__ixx.value, __ixx.set, None, None)

    
    # Element ixy uses Python identifier ixy
    __ixy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ixy'), 'ixy', '__AbsentNamespace0_CTD_ANON_47_ixy', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 44, 14), )

    
    ixy = property(__ixy.value, __ixy.set, None, None)

    
    # Element ixz uses Python identifier ixz
    __ixz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ixz'), 'ixz', '__AbsentNamespace0_CTD_ANON_47_ixz', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 48, 14), )

    
    ixz = property(__ixz.value, __ixz.set, None, None)

    
    # Element iyy uses Python identifier iyy
    __iyy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'iyy'), 'iyy', '__AbsentNamespace0_CTD_ANON_47_iyy', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 52, 14), )

    
    iyy = property(__iyy.value, __iyy.set, None, None)

    
    # Element iyz uses Python identifier iyz
    __iyz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'iyz'), 'iyz', '__AbsentNamespace0_CTD_ANON_47_iyz', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 56, 14), )

    
    iyz = property(__iyz.value, __iyz.set, None, None)

    
    # Element izz uses Python identifier izz
    __izz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'izz'), 'izz', '__AbsentNamespace0_CTD_ANON_47_izz', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 60, 14), )

    
    izz = property(__izz.value, __izz.set, None, None)

    _ElementMap.update({
        __ixx.name() : __ixx,
        __ixy.name() : __ixy,
        __ixz.name() : __ixz,
        __iyy.name() : __iyy,
        __iyz.name() : __iyz,
        __izz.name() : __izz
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_47 = CTD_ANON_47


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_48 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element parent uses Python identifier parent
    __parent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parent'), 'parent', '__AbsentNamespace0_CTD_ANON_48_parent', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 14, 8), )

    
    parent = property(__parent.value, __parent.set, None, '\n              Name of the parent link\n            ')

    
    # Element child uses Python identifier child
    __child = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'child'), 'child', '__AbsentNamespace0_CTD_ANON_48_child', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 23, 8), )

    
    child = property(__child.value, __child.set, None, '\n              Name of the child link\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_48_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 32, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              Pose offset from child link frame to joint frame (expressed in child link frame).\n            ')

    
    # Element gearbox_ratio uses Python identifier gearbox_ratio
    __gearbox_ratio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gearbox_ratio'), 'gearbox_ratio', '__AbsentNamespace0_CTD_ANON_48_gearbox_ratio', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 41, 8), )

    
    gearbox_ratio = property(__gearbox_ratio.value, __gearbox_ratio.set, None, '\n              Parameter for gearbox joints.  Given theta_1 and theta_2 defined in description for gearbox_reference_body, theta_2 = -gearbox_ratio * theta_1.\n            ')

    
    # Element gearbox_reference_body uses Python identifier gearbox_reference_body
    __gearbox_reference_body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gearbox_reference_body'), 'gearbox_reference_body', '__AbsentNamespace0_CTD_ANON_48_gearbox_reference_body', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 50, 8), )

    
    gearbox_reference_body = property(__gearbox_reference_body.value, __gearbox_reference_body.set, None, '\n              Parameter for gearbox joints.  Gearbox ratio is enforced over two joint angles.  First joint angle (theta_1) is the angle from the gearbox_reference_body to the parent link in the direction of the axis element and the second joint angle (theta_2) is the angle from the gearbox_reference_body to the child link in the direction of the axis2 element.\n            ')

    
    # Element thread_pitch uses Python identifier thread_pitch
    __thread_pitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'thread_pitch'), 'thread_pitch', '__AbsentNamespace0_CTD_ANON_48_thread_pitch', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 59, 8), )

    
    thread_pitch = property(__thread_pitch.value, __thread_pitch.set, None, '\n              Parameter for screw joints.\n            ')

    
    # Element axis uses Python identifier axis
    __axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'axis'), 'axis', '__AbsentNamespace0_CTD_ANON_48_axis', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 68, 8), )

    
    axis = property(__axis.value, __axis.set, None, '\n              \n      Parameters related to the axis of rotation for revolute joints,\n      the axis of translation for prismatic joints.\n    \n            ')

    
    # Element axis2 uses Python identifier axis2
    __axis2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'axis2'), 'axis2', '__AbsentNamespace0_CTD_ANON_48_axis2', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 226, 8), )

    
    axis2 = property(__axis2.value, __axis2.set, None, '\n              \n      Parameters related to the second axis of rotation for revolute2 joints and universal joints.\n    \n            ')

    
    # Element physics uses Python identifier physics
    __physics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'physics'), 'physics', '__AbsentNamespace0_CTD_ANON_48_physics', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 378, 8), )

    
    physics = property(__physics.value, __physics.set, None, '\n              Parameters that are specific to a certain physics engine.\n            ')

    
    # Element sensor uses Python identifier sensor
    __sensor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sensor'), 'sensor', '__AbsentNamespace0_CTD_ANON_48_sensor', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 23, 2), )

    
    sensor = property(__sensor.value, __sensor.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_48_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 569, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 569, 6)
    
    name = property(__name.value, __name.set, None, '\n            A unique name for the joint within the scope of the model.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_48_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 576, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 576, 6)
    
    type = property(__type.value, __type.set, None, '\n            The type of joint, which must be one of the following:\n      (revolute) a hinge joint that rotates on a single axis with either a fixed or continuous range of motion,\n      (gearbox) geared revolute joints,\n      (revolute2) same as two revolute joints connected in series,\n      (prismatic) a sliding joint that slides along an axis with a limited range specified by upper and lower limits,\n      (ball) a ball and socket joint,\n      (screw) a single degree of freedom joint with coupled sliding and rotational motion,\n      (universal) like a ball joint, but constrains one degree of freedom,\n      (fixed) a joint with zero degrees of freedom that rigidly connects two links.\n    \n          ')

    _ElementMap.update({
        __parent.name() : __parent,
        __child.name() : __child,
        __pose.name() : __pose,
        __gearbox_ratio.name() : __gearbox_ratio,
        __gearbox_reference_body.name() : __gearbox_reference_body,
        __thread_pitch.name() : __thread_pitch,
        __axis.name() : __axis,
        __axis2.name() : __axis2,
        __physics.name() : __physics,
        __sensor.name() : __sensor
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_48 = CTD_ANON_48


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_49 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Parameters related to the axis of rotation for revolute joints,
      the axis of translation for prismatic joints.
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 77, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element xyz uses Python identifier xyz
    __xyz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xyz'), 'xyz', '__AbsentNamespace0_CTD_ANON_49_xyz', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 80, 14), )

    
    xyz = property(__xyz.value, __xyz.set, None, '\n                    \n        Represents the x,y,z components of the axis unit vector. The axis is\n        expressed in the joint frame unless the use_parent_model_frame\n        flag is set to true. The vector should be normalized.\n      \n                  ')

    
    # Element use_parent_model_frame uses Python identifier use_parent_model_frame
    __use_parent_model_frame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'use_parent_model_frame'), 'use_parent_model_frame', '__AbsentNamespace0_CTD_ANON_49_use_parent_model_frame', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 93, 14), )

    
    use_parent_model_frame = property(__use_parent_model_frame.value, __use_parent_model_frame.set, None, '\n                    \n        Flag to interpret the axis xyz element in the parent model frame instead\n        of joint frame. Provided for Gazebo compatibility\n        (see https://bitbucket.org/osrf/gazebo/issue/494 ).\n      \n                  ')

    
    # Element dynamics uses Python identifier dynamics
    __dynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dynamics'), 'dynamics', '__AbsentNamespace0_CTD_ANON_49_dynamics', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 106, 14), )

    
    dynamics = property(__dynamics.value, __dynamics.set, None, '\n                    An element specifying physical properties of the joint. These values are used to specify modeling properties of the joint, particularly useful for simulation.\n                  ')

    
    # Element limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'limit'), 'limit', '__AbsentNamespace0_CTD_ANON_49_limit', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 155, 14), )

    
    limit = property(__limit.value, __limit.set, None, '\n                    specifies the limits of this joint\n                  ')

    _ElementMap.update({
        __xyz.name() : __xyz,
        __use_parent_model_frame.name() : __use_parent_model_frame,
        __dynamics.name() : __dynamics,
        __limit.name() : __limit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_49 = CTD_ANON_49


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_50 (pyxb.binding.basis.complexTypeDefinition):
    """
                    An element specifying physical properties of the joint. These values are used to specify modeling properties of the joint, particularly useful for simulation.
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 112, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element damping uses Python identifier damping
    __damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'damping'), 'damping', '__AbsentNamespace0_CTD_ANON_50_damping', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 115, 20), )

    
    damping = property(__damping.value, __damping.set, None, '\n                          The physical velocity dependent viscous damping coefficient of the joint.\n                        ')

    
    # Element friction uses Python identifier friction
    __friction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'friction'), 'friction', '__AbsentNamespace0_CTD_ANON_50_friction', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 124, 20), )

    
    friction = property(__friction.value, __friction.set, None, '\n                          The physical static friction value of the joint.\n                        ')

    
    # Element spring_reference uses Python identifier spring_reference
    __spring_reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'spring_reference'), 'spring_reference', '__AbsentNamespace0_CTD_ANON_50_spring_reference', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 133, 20), )

    
    spring_reference = property(__spring_reference.value, __spring_reference.set, None, '\n                          The spring reference position for this joint axis.\n                        ')

    
    # Element spring_stiffness uses Python identifier spring_stiffness
    __spring_stiffness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'spring_stiffness'), 'spring_stiffness', '__AbsentNamespace0_CTD_ANON_50_spring_stiffness', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 142, 20), )

    
    spring_stiffness = property(__spring_stiffness.value, __spring_stiffness.set, None, '\n                          The spring stiffness for this joint axis.\n                        ')

    _ElementMap.update({
        __damping.name() : __damping,
        __friction.name() : __friction,
        __spring_reference.name() : __spring_reference,
        __spring_stiffness.name() : __spring_stiffness
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_50 = CTD_ANON_50


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_51 (pyxb.binding.basis.complexTypeDefinition):
    """
                    specifies the limits of this joint
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 161, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lower uses Python identifier lower
    __lower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lower'), 'lower', '__AbsentNamespace0_CTD_ANON_51_lower', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 164, 20), )

    
    lower = property(__lower.value, __lower.set, None, '\n                          An attribute specifying the lower joint limit (radians for revolute joints, meters for prismatic joints). Omit if joint is continuous.\n                        ')

    
    # Element upper uses Python identifier upper
    __upper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'upper'), 'upper', '__AbsentNamespace0_CTD_ANON_51_upper', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 173, 20), )

    
    upper = property(__upper.value, __upper.set, None, '\n                          An attribute specifying the upper joint limit (radians for revolute joints, meters for prismatic joints). Omit if joint is continuous.\n                        ')

    
    # Element effort uses Python identifier effort
    __effort = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'effort'), 'effort', '__AbsentNamespace0_CTD_ANON_51_effort', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 182, 20), )

    
    effort = property(__effort.value, __effort.set, None, '\n                          An attribute for enforcing the maximum joint effort applied by Joint::SetForce.  Limit is not enforced if value is negative.\n                        ')

    
    # Element velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'velocity'), 'velocity', '__AbsentNamespace0_CTD_ANON_51_velocity', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 191, 20), )

    
    velocity = property(__velocity.value, __velocity.set, None, '\n                          (not implemented) An attribute for enforcing the maximum joint velocity.\n                        ')

    
    # Element stiffness uses Python identifier stiffness
    __stiffness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stiffness'), 'stiffness', '__AbsentNamespace0_CTD_ANON_51_stiffness', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 200, 20), )

    
    stiffness = property(__stiffness.value, __stiffness.set, None, '\n                          Joint stop stiffness. Support physics engines: SimBody.\n                        ')

    
    # Element dissipation uses Python identifier dissipation
    __dissipation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dissipation'), 'dissipation', '__AbsentNamespace0_CTD_ANON_51_dissipation', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 209, 20), )

    
    dissipation = property(__dissipation.value, __dissipation.set, None, '\n                          Joint stop dissipation.\n                        ')

    _ElementMap.update({
        __lower.name() : __lower,
        __upper.name() : __upper,
        __effort.name() : __effort,
        __velocity.name() : __velocity,
        __stiffness.name() : __stiffness,
        __dissipation.name() : __dissipation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_51 = CTD_ANON_51


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_52 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Parameters related to the second axis of rotation for revolute2 joints and universal joints.
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 234, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element xyz uses Python identifier xyz
    __xyz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xyz'), 'xyz', '__AbsentNamespace0_CTD_ANON_52_xyz', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 237, 14), )

    
    xyz = property(__xyz.value, __xyz.set, None, '\n                    \n        Represents the x,y,z components of the axis unit vector. The axis is\n        expressed in the joint frame unless the use_parent_model_frame\n        flag is set to true. The vector should be normalized.\n      \n                  ')

    
    # Element use_parent_model_frame uses Python identifier use_parent_model_frame
    __use_parent_model_frame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'use_parent_model_frame'), 'use_parent_model_frame', '__AbsentNamespace0_CTD_ANON_52_use_parent_model_frame', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 250, 14), )

    
    use_parent_model_frame = property(__use_parent_model_frame.value, __use_parent_model_frame.set, None, '\n                    \n        Flag to interpret the axis xyz element in the parent model frame instead\n        of joint frame. Provided for Gazebo compatibility\n        (see https://bitbucket.org/osrf/gazebo/issue/494 ).\n      \n                  ')

    
    # Element dynamics uses Python identifier dynamics
    __dynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dynamics'), 'dynamics', '__AbsentNamespace0_CTD_ANON_52_dynamics', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 263, 14), )

    
    dynamics = property(__dynamics.value, __dynamics.set, None, '\n                    An element specifying physical properties of the joint. These values are used to specify modeling properties of the joint, particularly useful for simulation.\n                  ')

    
    # Element limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'limit'), 'limit', '__AbsentNamespace0_CTD_ANON_52_limit', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 312, 14), )

    
    limit = property(__limit.value, __limit.set, None, None)

    _ElementMap.update({
        __xyz.name() : __xyz,
        __use_parent_model_frame.name() : __use_parent_model_frame,
        __dynamics.name() : __dynamics,
        __limit.name() : __limit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_52 = CTD_ANON_52


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_53 (pyxb.binding.basis.complexTypeDefinition):
    """
                    An element specifying physical properties of the joint. These values are used to specify modeling properties of the joint, particularly useful for simulation.
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 269, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element damping uses Python identifier damping
    __damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'damping'), 'damping', '__AbsentNamespace0_CTD_ANON_53_damping', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 272, 20), )

    
    damping = property(__damping.value, __damping.set, None, '\n                          The physical velocity dependent viscous damping coefficient of the joint.  EXPERIMENTAL: if damping coefficient is negative and implicit_spring_damper is true, adaptive damping is used.\n                        ')

    
    # Element friction uses Python identifier friction
    __friction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'friction'), 'friction', '__AbsentNamespace0_CTD_ANON_53_friction', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 281, 20), )

    
    friction = property(__friction.value, __friction.set, None, '\n                          The physical static friction value of the joint.\n                        ')

    
    # Element spring_reference uses Python identifier spring_reference
    __spring_reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'spring_reference'), 'spring_reference', '__AbsentNamespace0_CTD_ANON_53_spring_reference', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 290, 20), )

    
    spring_reference = property(__spring_reference.value, __spring_reference.set, None, '\n                          The spring reference position for this joint axis.\n                        ')

    
    # Element spring_stiffness uses Python identifier spring_stiffness
    __spring_stiffness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'spring_stiffness'), 'spring_stiffness', '__AbsentNamespace0_CTD_ANON_53_spring_stiffness', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 299, 20), )

    
    spring_stiffness = property(__spring_stiffness.value, __spring_stiffness.set, None, '\n                          The spring stiffness for this joint axis.\n                        ')

    _ElementMap.update({
        __damping.name() : __damping,
        __friction.name() : __friction,
        __spring_reference.name() : __spring_reference,
        __spring_stiffness.name() : __spring_stiffness
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_53 = CTD_ANON_53


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_54 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 313, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lower uses Python identifier lower
    __lower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lower'), 'lower', '__AbsentNamespace0_CTD_ANON_54_lower', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 316, 20), )

    
    lower = property(__lower.value, __lower.set, None, '\n                          An attribute specifying the lower joint limit (radians for revolute joints, meters for prismatic joints). Omit if joint is continuous.\n                        ')

    
    # Element upper uses Python identifier upper
    __upper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'upper'), 'upper', '__AbsentNamespace0_CTD_ANON_54_upper', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 325, 20), )

    
    upper = property(__upper.value, __upper.set, None, '\n                          An attribute specifying the upper joint limit (radians for revolute joints, meters for prismatic joints). Omit if joint is continuous.\n                        ')

    
    # Element effort uses Python identifier effort
    __effort = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'effort'), 'effort', '__AbsentNamespace0_CTD_ANON_54_effort', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 334, 20), )

    
    effort = property(__effort.value, __effort.set, None, '\n                          An attribute for enforcing the maximum joint effort applied by Joint::SetForce.  Limit is not enforced if value is negative.\n                        ')

    
    # Element velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'velocity'), 'velocity', '__AbsentNamespace0_CTD_ANON_54_velocity', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 343, 20), )

    
    velocity = property(__velocity.value, __velocity.set, None, '\n                          (not implemented) An attribute for enforcing the maximum joint velocity.\n                        ')

    
    # Element stiffness uses Python identifier stiffness
    __stiffness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stiffness'), 'stiffness', '__AbsentNamespace0_CTD_ANON_54_stiffness', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 352, 20), )

    
    stiffness = property(__stiffness.value, __stiffness.set, None, '\n                          Joint stop stiffness. Supported physics engines: SimBody.\n                        ')

    
    # Element dissipation uses Python identifier dissipation
    __dissipation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dissipation'), 'dissipation', '__AbsentNamespace0_CTD_ANON_54_dissipation', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 361, 20), )

    
    dissipation = property(__dissipation.value, __dissipation.set, None, '\n                          Joint stop dissipation. Supported physics engines: SimBody.\n                        ')

    _ElementMap.update({
        __lower.name() : __lower,
        __upper.name() : __upper,
        __effort.name() : __effort,
        __velocity.name() : __velocity,
        __stiffness.name() : __stiffness,
        __dissipation.name() : __dissipation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_54 = CTD_ANON_54


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_55 (pyxb.binding.basis.complexTypeDefinition):
    """
              Parameters that are specific to a certain physics engine.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 384, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element simbody uses Python identifier simbody
    __simbody = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'simbody'), 'simbody', '__AbsentNamespace0_CTD_ANON_55_simbody', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 387, 14), )

    
    simbody = property(__simbody.value, __simbody.set, None, '\n                    Simbody specific parameters\n                  ')

    
    # Element ode uses Python identifier ode
    __ode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ode'), 'ode', '__AbsentNamespace0_CTD_ANON_55_ode', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 409, 14), )

    
    ode = property(__ode.value, __ode.set, None, '\n                    ODE specific parameters\n                  ')

    
    # Element provide_feedback uses Python identifier provide_feedback
    __provide_feedback = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'provide_feedback'), 'provide_feedback', '__AbsentNamespace0_CTD_ANON_55_provide_feedback', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 555, 14), )

    
    provide_feedback = property(__provide_feedback.value, __provide_feedback.set, None, '\n                    If provide feedback is set to true, physics engine will compute the constraint forces at this joint.  For now, provide_feedback under ode block will override this tag and given user warning about the migration.  provide_feedback under ode is scheduled to be removed in SDF 1.5.\n                  ')

    _ElementMap.update({
        __simbody.name() : __simbody,
        __ode.name() : __ode,
        __provide_feedback.name() : __provide_feedback
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_55 = CTD_ANON_55


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_56 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Simbody specific parameters
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 393, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element must_be_loop_joint uses Python identifier must_be_loop_joint
    __must_be_loop_joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'must_be_loop_joint'), 'must_be_loop_joint', '__AbsentNamespace0_CTD_ANON_56_must_be_loop_joint', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 396, 20), )

    
    must_be_loop_joint = property(__must_be_loop_joint.value, __must_be_loop_joint.set, None, '\n                          Force cut in the multibody graph at this joint.\n                        ')

    _ElementMap.update({
        __must_be_loop_joint.name() : __must_be_loop_joint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_56 = CTD_ANON_56


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_57 (pyxb.binding.basis.complexTypeDefinition):
    """
                    ODE specific parameters
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 415, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element provide_feedback uses Python identifier provide_feedback
    __provide_feedback = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'provide_feedback'), 'provide_feedback', '__AbsentNamespace0_CTD_ANON_57_provide_feedback', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 418, 20), )

    
    provide_feedback = property(__provide_feedback.value, __provide_feedback.set, None, '\n                          (DEPRECATION WARNING:  In SDF 1.5 this tag will be replaced by the same tag directly under the physics-block.  For now, this tag overrides the one outside of ode-block, but in SDF 1.5 this tag will be removed completely.)  If provide feedback is set to true, ODE will compute the constraint forces at this joint.\n                        ')

    
    # Element cfm_damping uses Python identifier cfm_damping
    __cfm_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cfm_damping'), 'cfm_damping', '__AbsentNamespace0_CTD_ANON_57_cfm_damping', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 427, 20), )

    
    cfm_damping = property(__cfm_damping.value, __cfm_damping.set, None, '\n                          If cfm damping is set to true, ODE will use CFM to simulate damping, allows for infinite damping, and one additional constraint row (previously used for joint limit) is always active.\n                        ')

    
    # Element implicit_spring_damper uses Python identifier implicit_spring_damper
    __implicit_spring_damper = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'implicit_spring_damper'), 'implicit_spring_damper', '__AbsentNamespace0_CTD_ANON_57_implicit_spring_damper', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 436, 20), )

    
    implicit_spring_damper = property(__implicit_spring_damper.value, __implicit_spring_damper.set, None, '\n                          If implicit_spring_damper is set to true, ODE will use CFM, ERP to simulate stiffness and damping, allows for infinite damping, and one additional constraint row (previously used for joint limit) is always active.  This replaces cfm_damping parameter in sdf 1.4.\n                        ')

    
    # Element fudge_factor uses Python identifier fudge_factor
    __fudge_factor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fudge_factor'), 'fudge_factor', '__AbsentNamespace0_CTD_ANON_57_fudge_factor', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 445, 20), )

    
    fudge_factor = property(__fudge_factor.value, __fudge_factor.set, None, '\n                          Scale the excess for in a joint motor at joint limits. Should be between zero and one.\n                        ')

    
    # Element cfm uses Python identifier cfm
    __cfm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cfm'), 'cfm', '__AbsentNamespace0_CTD_ANON_57_cfm', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 454, 20), )

    
    cfm = property(__cfm.value, __cfm.set, None, '\n                          Constraint force mixing for constrained directions\n                        ')

    
    # Element erp uses Python identifier erp
    __erp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'erp'), 'erp', '__AbsentNamespace0_CTD_ANON_57_erp', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 463, 20), )

    
    erp = property(__erp.value, __erp.set, None, '\n                          Error reduction parameter for constrained directions\n                        ')

    
    # Element bounce uses Python identifier bounce
    __bounce = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bounce'), 'bounce', '__AbsentNamespace0_CTD_ANON_57_bounce', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 472, 20), )

    
    bounce = property(__bounce.value, __bounce.set, None, '\n                          Bounciness of the limits\n                        ')

    
    # Element max_force uses Python identifier max_force
    __max_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_force'), 'max_force', '__AbsentNamespace0_CTD_ANON_57_max_force', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 481, 20), )

    
    max_force = property(__max_force.value, __max_force.set, None, '\n                          Maximum force or torque used to reach the desired velocity.\n                        ')

    
    # Element velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'velocity'), 'velocity', '__AbsentNamespace0_CTD_ANON_57_velocity', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 490, 20), )

    
    velocity = property(__velocity.value, __velocity.set, None, '\n                          The desired velocity of the joint. Should only be set if you want the joint to move on load.\n                        ')

    
    # Element limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'limit'), 'limit', '__AbsentNamespace0_CTD_ANON_57_limit', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 499, 20), )

    
    limit = property(__limit.value, __limit.set, None, None)

    
    # Element suspension uses Python identifier suspension
    __suspension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'suspension'), 'suspension', '__AbsentNamespace0_CTD_ANON_57_suspension', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 525, 20), )

    
    suspension = property(__suspension.value, __suspension.set, None, None)

    _ElementMap.update({
        __provide_feedback.name() : __provide_feedback,
        __cfm_damping.name() : __cfm_damping,
        __implicit_spring_damper.name() : __implicit_spring_damper,
        __fudge_factor.name() : __fudge_factor,
        __cfm.name() : __cfm,
        __erp.name() : __erp,
        __bounce.name() : __bounce,
        __max_force.name() : __max_force,
        __velocity.name() : __velocity,
        __limit.name() : __limit,
        __suspension.name() : __suspension
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_57 = CTD_ANON_57


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_58 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 500, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element cfm uses Python identifier cfm
    __cfm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cfm'), 'cfm', '__AbsentNamespace0_CTD_ANON_58_cfm', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 503, 26), )

    
    cfm = property(__cfm.value, __cfm.set, None, '\n                                Constraint force mixing parameter used by the joint stop\n                              ')

    
    # Element erp uses Python identifier erp
    __erp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'erp'), 'erp', '__AbsentNamespace0_CTD_ANON_58_erp', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 512, 26), )

    
    erp = property(__erp.value, __erp.set, None, '\n                                Error reduction parameter used by the joint stop\n                              ')

    _ElementMap.update({
        __cfm.name() : __cfm,
        __erp.name() : __erp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_58 = CTD_ANON_58


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_59 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 526, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element cfm uses Python identifier cfm
    __cfm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cfm'), 'cfm', '__AbsentNamespace0_CTD_ANON_59_cfm', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 529, 26), )

    
    cfm = property(__cfm.value, __cfm.set, None, '\n                                Suspension constraint force mixing parameter\n                              ')

    
    # Element erp uses Python identifier erp
    __erp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'erp'), 'erp', '__AbsentNamespace0_CTD_ANON_59_erp', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 538, 26), )

    
    erp = property(__erp.value, __erp.set, None, '\n                                Suspension error reduction parameter\n                              ')

    _ElementMap.update({
        __cfm.name() : __cfm,
        __erp.name() : __erp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_59 = CTD_ANON_59


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_60 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 17, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element audio_sink uses Python identifier audio_sink
    __audio_sink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audio_sink'), 'audio_sink', '__AbsentNamespace0_CTD_ANON_60_audio_sink', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_sink.xsd', 9, 2), )

    
    audio_sink = property(__audio_sink.value, __audio_sink.set, None, None)

    
    # Element audio_source uses Python identifier audio_source
    __audio_source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'audio_source'), 'audio_source', '__AbsentNamespace0_CTD_ANON_60_audio_source', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 9, 2), )

    
    audio_source = property(__audio_source.value, __audio_source.set, None, None)

    
    # Element collision uses Python identifier collision
    __collision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'collision'), 'collision', '__AbsentNamespace0_CTD_ANON_60_collision', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 11, 2), )

    
    collision = property(__collision.value, __collision.set, None, None)

    
    # Element inertial uses Python identifier inertial
    __inertial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inertial'), 'inertial', '__AbsentNamespace0_CTD_ANON_60_inertial', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 9, 2), )

    
    inertial = property(__inertial.value, __inertial.set, None, None)

    
    # Element gravity uses Python identifier gravity
    __gravity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gravity'), 'gravity', '__AbsentNamespace0_CTD_ANON_60_gravity', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 20, 8), )

    
    gravity = property(__gravity.value, __gravity.set, None, '\n              If true, the link is affected by gravity.\n            ')

    
    # Element self_collide uses Python identifier self_collide
    __self_collide = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'self_collide'), 'self_collide', '__AbsentNamespace0_CTD_ANON_60_self_collide', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 29, 8), )

    
    self_collide = property(__self_collide.value, __self_collide.set, None, '\n              If true, the link can collide with other links in the model. Two links within a model will collide if link1.self_collide OR link2.self_collide. Links connected by a joint will never collide.\n            ')

    
    # Element kinematic uses Python identifier kinematic
    __kinematic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'kinematic'), 'kinematic', '__AbsentNamespace0_CTD_ANON_60_kinematic', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 38, 8), )

    
    kinematic = property(__kinematic.value, __kinematic.set, None, '\n              If true, the link is kinematic only\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_60_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 47, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              This is the pose of the link reference frame, relative to the model reference frame.\n            ')

    
    # Element must_be_base_link uses Python identifier must_be_base_link
    __must_be_base_link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'must_be_base_link'), 'must_be_base_link', '__AbsentNamespace0_CTD_ANON_60_must_be_base_link', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 56, 8), )

    
    must_be_base_link = property(__must_be_base_link.value, __must_be_base_link.set, None, '\n              If true, the link will have 6DOF and be a direct child of world.\n            ')

    
    # Element velocity_decay uses Python identifier velocity_decay
    __velocity_decay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'velocity_decay'), 'velocity_decay', '__AbsentNamespace0_CTD_ANON_60_velocity_decay', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 65, 8), )

    
    velocity_decay = property(__velocity_decay.value, __velocity_decay.set, None, "\n              Exponential damping of the link's velocity.\n            ")

    
    # Element projector uses Python identifier projector
    __projector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'projector'), 'projector', '__AbsentNamespace0_CTD_ANON_60_projector', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 5, 2), )

    
    projector = property(__projector.value, __projector.set, None, None)

    
    # Element sensor uses Python identifier sensor
    __sensor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sensor'), 'sensor', '__AbsentNamespace0_CTD_ANON_60_sensor', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 23, 2), )

    
    sensor = property(__sensor.value, __sensor.set, None, None)

    
    # Element visual uses Python identifier visual
    __visual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'visual'), 'visual', '__AbsentNamespace0_CTD_ANON_60_visual', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 12, 2), )

    
    visual = property(__visual.value, __visual.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_60_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 103, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 103, 6)
    
    name = property(__name.value, __name.set, None, '\n            A unique name for the link within the scope of the model.\n          ')

    _ElementMap.update({
        __audio_sink.name() : __audio_sink,
        __audio_source.name() : __audio_source,
        __collision.name() : __collision,
        __inertial.name() : __inertial,
        __gravity.name() : __gravity,
        __self_collide.name() : __self_collide,
        __kinematic.name() : __kinematic,
        __pose.name() : __pose,
        __must_be_base_link.name() : __must_be_base_link,
        __velocity_decay.name() : __velocity_decay,
        __projector.name() : __projector,
        __sensor.name() : __sensor,
        __visual.name() : __visual
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_60 = CTD_ANON_60


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_61 (pyxb.binding.basis.complexTypeDefinition):
    """
              Exponential damping of the link's velocity.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 71, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element linear uses Python identifier linear
    __linear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'linear'), 'linear', '__AbsentNamespace0_CTD_ANON_61_linear', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 74, 14), )

    
    linear = property(__linear.value, __linear.set, None, '\n                    Linear damping\n                  ')

    
    # Element angular uses Python identifier angular
    __angular = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'angular'), 'angular', '__AbsentNamespace0_CTD_ANON_61_angular', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 83, 14), )

    
    angular = property(__angular.value, __angular.set, None, '\n                    Angular damping\n                  ')

    _ElementMap.update({
        __linear.name() : __linear,
        __angular.name() : __angular
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_61 = CTD_ANON_61


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_62 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element near uses Python identifier near
    __near = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'near'), 'near', '__AbsentNamespace0_CTD_ANON_62_near', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 13, 8), )

    
    near = property(__near.value, __near.set, None, '\n              Near clipping distance of the view frustum\n            ')

    
    # Element far uses Python identifier far
    __far = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'far'), 'far', '__AbsentNamespace0_CTD_ANON_62_far', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 22, 8), )

    
    far = property(__far.value, __far.set, None, '\n              Far clipping distance of the view frustum\n            ')

    
    # Element aspect_ratio uses Python identifier aspect_ratio
    __aspect_ratio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'aspect_ratio'), 'aspect_ratio', '__AbsentNamespace0_CTD_ANON_62_aspect_ratio', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 31, 8), )

    
    aspect_ratio = property(__aspect_ratio.value, __aspect_ratio.set, None, '\n              Aspect ratio of the near and far planes. This is the width divided by the height of the near or far planes.\n            ')

    
    # Element horizontal_fov uses Python identifier horizontal_fov
    __horizontal_fov = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'horizontal_fov'), 'horizontal_fov', '__AbsentNamespace0_CTD_ANON_62_horizontal_fov', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 40, 8), )

    
    horizontal_fov = property(__horizontal_fov.value, __horizontal_fov.set, None, "\n              Horizontal field of view of the frustum, in radians. This is the angle between the frustum's vertex and the edges of the near or far plane.\n            ")

    _ElementMap.update({
        __near.name() : __near,
        __far.name() : __far,
        __aspect_ratio.name() : __aspect_ratio,
        __horizontal_fov.name() : __horizontal_fov
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_62 = CTD_ANON_62


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_63 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__AbsentNamespace0_CTD_ANON_63_x', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 13, 8), )

    
    x = property(__x.value, __x.set, None, '\n              \n      Parameters related to the body-frame X axis of the magnetometer\n    \n            ')

    
    # Element y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__AbsentNamespace0_CTD_ANON_63_y', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 28, 8), )

    
    y = property(__y.value, __y.set, None, '\n              \n      Parameters related to the body-frame Y axis of the magnetometer\n    \n            ')

    
    # Element z uses Python identifier z
    __z = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'z'), 'z', '__AbsentNamespace0_CTD_ANON_63_z', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 43, 8), )

    
    z = property(__z.value, __z.set, None, '\n              \n      Parameters related to the body-frame Z axis of the magnetometer\n    \n            ')

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __z.name() : __z
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_63 = CTD_ANON_63


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_64 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Parameters related to the body-frame X axis of the magnetometer
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 21, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_64 = CTD_ANON_64


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_65 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Parameters related to the body-frame Y axis of the magnetometer
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 36, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_65 = CTD_ANON_65


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_66 (pyxb.binding.basis.complexTypeDefinition):
    """
              
      Parameters related to the body-frame Z axis of the magnetometer
    
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 51, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_66 = CTD_ANON_66


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_67 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element script uses Python identifier script
    __script = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'script'), 'script', '__AbsentNamespace0_CTD_ANON_67_script', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 13, 8), )

    
    script = property(__script.value, __script.set, None, '\n              Name of material from an installed script file. This will override the color element if the script exists.\n            ')

    
    # Element shader uses Python identifier shader
    __shader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shader'), 'shader', '__AbsentNamespace0_CTD_ANON_67_shader', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 44, 8), )

    
    shader = property(__shader.value, __shader.set, None, None)

    
    # Element lighting uses Python identifier lighting
    __lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lighting'), 'lighting', '__AbsentNamespace0_CTD_ANON_67_lighting', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 68, 8), )

    
    lighting = property(__lighting.value, __lighting.set, None, '\n              If false, dynamic lighting will be disabled\n            ')

    
    # Element ambient uses Python identifier ambient
    __ambient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ambient'), 'ambient', '__AbsentNamespace0_CTD_ANON_67_ambient', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 77, 8), )

    
    ambient = property(__ambient.value, __ambient.set, None, '\n              The ambient color of a material specified by set of four numbers representing red/green/blue, each in the range of [0,1].\n            ')

    
    # Element diffuse uses Python identifier diffuse
    __diffuse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'diffuse'), 'diffuse', '__AbsentNamespace0_CTD_ANON_67_diffuse', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 86, 8), )

    
    diffuse = property(__diffuse.value, __diffuse.set, None, '\n              The diffuse color of a material specified by set of four numbers representing red/green/blue/alpha, each in the range of [0,1].\n            ')

    
    # Element specular uses Python identifier specular
    __specular = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'specular'), 'specular', '__AbsentNamespace0_CTD_ANON_67_specular', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 95, 8), )

    
    specular = property(__specular.value, __specular.set, None, '\n              The specular color of a material specified by set of four numbers representing red/green/blue/alpha, each in the range of [0,1].\n            ')

    
    # Element emissive uses Python identifier emissive
    __emissive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emissive'), 'emissive', '__AbsentNamespace0_CTD_ANON_67_emissive', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 104, 8), )

    
    emissive = property(__emissive.value, __emissive.set, None, '\n              The emissive color of a material specified by set of four numbers representing red/green/blue, each in the range of [0,1].\n            ')

    _ElementMap.update({
        __script.name() : __script,
        __shader.name() : __shader,
        __lighting.name() : __lighting,
        __ambient.name() : __ambient,
        __diffuse.name() : __diffuse,
        __specular.name() : __specular,
        __emissive.name() : __emissive
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_67 = CTD_ANON_67


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_68 (pyxb.binding.basis.complexTypeDefinition):
    """
              Name of material from an installed script file. This will override the color element if the script exists.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 19, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__AbsentNamespace0_CTD_ANON_68_uri', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 22, 14), )

    
    uri = property(__uri.value, __uri.set, None, '\n                    URI of the material script file\n                  ')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_68_name', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 31, 14), )

    
    name = property(__name.value, __name.set, None, '\n                    Name of the script within the script file\n                  ')

    _ElementMap.update({
        __uri.name() : __uri,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_68 = CTD_ANON_68


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_69 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 45, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element normal_map uses Python identifier normal_map
    __normal_map = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'normal_map'), 'normal_map', '__AbsentNamespace0_CTD_ANON_69_normal_map', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 48, 14), )

    
    normal_map = property(__normal_map.value, __normal_map.set, None, '\n                    filename of the normal map\n                  ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_69_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 57, 12)
    __type._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 57, 12)
    
    type = property(__type.value, __type.set, None, '\n                  vertex, pixel, normal_map_objectspace, normal_map_tangentspace\n                ')

    _ElementMap.update({
        __normal_map.name() : __normal_map
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_69 = CTD_ANON_69


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_70 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__AbsentNamespace0_CTD_ANON_70_uri', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 13, 8), )

    
    uri = property(__uri.value, __uri.set, None, '\n              Mesh uri\n            ')

    
    # Element submesh uses Python identifier submesh
    __submesh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'submesh'), 'submesh', '__AbsentNamespace0_CTD_ANON_70_submesh', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 22, 8), )

    
    submesh = property(__submesh.value, __submesh.set, None, '\n              Use a named submesh. The submesh must exist in the mesh specified by the uri\n            ')

    
    # Element scale uses Python identifier scale
    __scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'scale'), 'scale', '__AbsentNamespace0_CTD_ANON_70_scale', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 53, 8), )

    
    scale = property(__scale.value, __scale.set, None, '\n              Scaling factor applied to the mesh\n            ')

    _ElementMap.update({
        __uri.name() : __uri,
        __submesh.name() : __submesh,
        __scale.name() : __scale
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_70 = CTD_ANON_70


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_71 (pyxb.binding.basis.complexTypeDefinition):
    """
              Use a named submesh. The submesh must exist in the mesh specified by the uri
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 28, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_71_name', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 31, 14), )

    
    name = property(__name.value, __name.set, None, '\n                    Name of the submesh within the parent mesh\n                  ')

    
    # Element center uses Python identifier center
    __center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'center'), 'center', '__AbsentNamespace0_CTD_ANON_71_center', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 40, 14), )

    
    center = property(__center.value, __center.set, None, '\n                    Set to true to center the vertices of the submesh at 0,0,0. This will effectively remove any transformations on the submesh before the poses from parent links and models are applied.\n                  ')

    _ElementMap.update({
        __name.name() : __name,
        __center.name() : __center
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_71 = CTD_ANON_71


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_72 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element normal uses Python identifier normal
    __normal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'normal'), 'normal', '__AbsentNamespace0_CTD_ANON_72_normal', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 13, 8), )

    
    normal = property(__normal.value, __normal.set, None, '\n              Normal direction for the plane\n            ')

    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_CTD_ANON_72_size', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 22, 8), )

    
    size = property(__size.value, __size.set, None, '\n              Length of each side of the plane\n            ')

    _ElementMap.update({
        __normal.name() : __normal,
        __size.name() : __size
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_72 = CTD_ANON_72


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_73 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_73_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 14, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 14, 6)
    
    name = property(__name.value, __name.set, None, '\n            A unique name for the plugin, scoped to its parent.\n          ')

    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__AbsentNamespace0_CTD_ANON_73_filename', pyxb.binding.datatypes.string, required=True)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 21, 6)
    __filename._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 21, 6)
    
    filename = property(__filename.value, __filename.set, None, '\n            Name of the shared library to load. If the filename is not a full path name, the file will be searched for in the configuration paths.\n          ')

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __filename.name() : __filename
    })
_module_typeBindings.CTD_ANON_73 = CTD_ANON_73


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_74 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_CTD_ANON_74_point', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 13, 8), )

    
    point = property(__point.value, __point.set, None, '\n              \n      A series of points that define the path of the polyline.\n    \n            ')

    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_CTD_ANON_74_height', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 24, 8), )

    
    height = property(__height.value, __height.set, None, '\n              Height of the polyline\n            ')

    _ElementMap.update({
        __point.name() : __point,
        __height.name() : __height
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_74 = CTD_ANON_74


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_75 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 6, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element plugin uses Python identifier plugin
    __plugin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'plugin'), 'plugin', '__AbsentNamespace0_CTD_ANON_75_plugin', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2), )

    
    plugin = property(__plugin.value, __plugin.set, None, None)

    
    # Element texture uses Python identifier texture
    __texture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'texture'), 'texture', '__AbsentNamespace0_CTD_ANON_75_texture', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 9, 8), )

    
    texture = property(__texture.value, __texture.set, None, '\n              Texture name\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_75_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 18, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              Pose of the projector\n            ')

    
    # Element fov uses Python identifier fov
    __fov = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fov'), 'fov', '__AbsentNamespace0_CTD_ANON_75_fov', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 27, 8), )

    
    fov = property(__fov.value, __fov.set, None, '\n              Field of view\n            ')

    
    # Element near_clip uses Python identifier near_clip
    __near_clip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'near_clip'), 'near_clip', '__AbsentNamespace0_CTD_ANON_75_near_clip', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 36, 8), )

    
    near_clip = property(__near_clip.value, __near_clip.set, None, '\n              Near clip distance\n            ')

    
    # Element far_clip uses Python identifier far_clip
    __far_clip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'far_clip'), 'far_clip', '__AbsentNamespace0_CTD_ANON_75_far_clip', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 45, 8), )

    
    far_clip = property(__far_clip.value, __far_clip.set, None, '\n              far clip distance\n            ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_75_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 55, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 55, 6)
    
    name = property(__name.value, __name.set, None, '\n            Name of the projector\n          ')

    _ElementMap.update({
        __plugin.name() : __plugin,
        __texture.name() : __texture,
        __pose.name() : __pose,
        __fov.name() : __fov,
        __near_clip.name() : __near_clip,
        __far_clip.name() : __far_clip
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_75 = CTD_ANON_75


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_76 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element scan uses Python identifier scan
    __scan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'scan'), 'scan', '__AbsentNamespace0_CTD_ANON_76_scan', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 13, 8), )

    
    scan = property(__scan.value, __scan.set, None, None)

    
    # Element range uses Python identifier range
    __range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'range'), 'range', '__AbsentNamespace0_CTD_ANON_76_range', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 99, 8), )

    
    range = property(__range.value, __range.set, None, '\n              specifies range properties of each simulated ray\n            ')

    
    # Element noise uses Python identifier noise
    __noise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'noise'), 'noise', '__AbsentNamespace0_CTD_ANON_76_noise', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 139, 8), )

    
    noise = property(__noise.value, __noise.set, None, '\n              The properties of the noise model that should be applied to generated scans\n            ')

    _ElementMap.update({
        __scan.name() : __scan,
        __range.name() : __range,
        __noise.name() : __noise
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_76 = CTD_ANON_76


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_77 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 14, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element horizontal uses Python identifier horizontal
    __horizontal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'horizontal'), 'horizontal', '__AbsentNamespace0_CTD_ANON_77_horizontal', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 17, 14), )

    
    horizontal = property(__horizontal.value, __horizontal.set, None, None)

    
    # Element vertical uses Python identifier vertical
    __vertical = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vertical'), 'vertical', '__AbsentNamespace0_CTD_ANON_77_vertical', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 56, 14), )

    
    vertical = property(__vertical.value, __vertical.set, None, None)

    _ElementMap.update({
        __horizontal.name() : __horizontal,
        __vertical.name() : __vertical
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_77 = CTD_ANON_77


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_78 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 18, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samples uses Python identifier samples
    __samples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samples'), 'samples', '__AbsentNamespace0_CTD_ANON_78_samples', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 21, 20), )

    
    samples = property(__samples.value, __samples.set, None, '\n                          The number of simulated rays to generate per complete laser sweep cycle.\n                        ')

    
    # Element resolution uses Python identifier resolution
    __resolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'resolution'), 'resolution', '__AbsentNamespace0_CTD_ANON_78_resolution', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 30, 20), )

    
    resolution = property(__resolution.value, __resolution.set, None, '\n                          This number is multiplied by samples to determine the number of range data points returned. If resolution is less than one, range data is interpolated. If resolution is greater than one, range data is averaged.\n                        ')

    
    # Element min_angle uses Python identifier min_angle
    __min_angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_angle'), 'min_angle', '__AbsentNamespace0_CTD_ANON_78_min_angle', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 39, 20), )

    
    min_angle = property(__min_angle.value, __min_angle.set, None, None)

    
    # Element max_angle uses Python identifier max_angle
    __max_angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_angle'), 'max_angle', '__AbsentNamespace0_CTD_ANON_78_max_angle', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 43, 20), )

    
    max_angle = property(__max_angle.value, __max_angle.set, None, '\n                          Must be greater or equal to min_angle\n                        ')

    _ElementMap.update({
        __samples.name() : __samples,
        __resolution.name() : __resolution,
        __min_angle.name() : __min_angle,
        __max_angle.name() : __max_angle
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_78 = CTD_ANON_78


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_79 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 57, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element samples uses Python identifier samples
    __samples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'samples'), 'samples', '__AbsentNamespace0_CTD_ANON_79_samples', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 60, 20), )

    
    samples = property(__samples.value, __samples.set, None, '\n                          The number of simulated rays to generate per complete laser sweep cycle.\n                        ')

    
    # Element resolution uses Python identifier resolution
    __resolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'resolution'), 'resolution', '__AbsentNamespace0_CTD_ANON_79_resolution', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 69, 20), )

    
    resolution = property(__resolution.value, __resolution.set, None, '\n                          This number is multiplied by samples to determine the number of range data points returned. If resolution is less than one, range data is interpolated. If resolution is greater than one, range data is averaged.\n                        ')

    
    # Element min_angle uses Python identifier min_angle
    __min_angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_angle'), 'min_angle', '__AbsentNamespace0_CTD_ANON_79_min_angle', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 78, 20), )

    
    min_angle = property(__min_angle.value, __min_angle.set, None, None)

    
    # Element max_angle uses Python identifier max_angle
    __max_angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_angle'), 'max_angle', '__AbsentNamespace0_CTD_ANON_79_max_angle', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 82, 20), )

    
    max_angle = property(__max_angle.value, __max_angle.set, None, '\n                          Must be greater or equal to min_angle\n                        ')

    _ElementMap.update({
        __samples.name() : __samples,
        __resolution.name() : __resolution,
        __min_angle.name() : __min_angle,
        __max_angle.name() : __max_angle
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_79 = CTD_ANON_79


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_80 (pyxb.binding.basis.complexTypeDefinition):
    """
              specifies range properties of each simulated ray
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 105, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element min uses Python identifier min
    __min = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__AbsentNamespace0_CTD_ANON_80_min', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 108, 14), )

    
    min = property(__min.value, __min.set, None, '\n                    The minimum distance for each ray.\n                  ')

    
    # Element max uses Python identifier max
    __max = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__AbsentNamespace0_CTD_ANON_80_max', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 117, 14), )

    
    max = property(__max.value, __max.set, None, '\n                    The maximum distance for each ray.\n                  ')

    
    # Element resolution uses Python identifier resolution
    __resolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'resolution'), 'resolution', '__AbsentNamespace0_CTD_ANON_80_resolution', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 126, 14), )

    
    resolution = property(__resolution.value, __resolution.set, None, '\n                    Linear resolution of each ray.\n                  ')

    _ElementMap.update({
        __min.name() : __min,
        __max.name() : __max,
        __resolution.name() : __resolution
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_80 = CTD_ANON_80


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_81 (pyxb.binding.basis.complexTypeDefinition):
    """
              The properties of the noise model that should be applied to generated scans
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 145, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_81_type', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 148, 14), )

    
    type = property(__type.value, __type.set, None, '\n                    The type of noise.  Currently supported types are: "gaussian" (draw noise values independently for each beam from a Gaussian distribution).\n                  ')

    
    # Element mean uses Python identifier mean
    __mean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mean'), 'mean', '__AbsentNamespace0_CTD_ANON_81_mean', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 157, 14), )

    
    mean = property(__mean.value, __mean.set, None, '\n                    For type "gaussian," the mean of the Gaussian distribution from which noise values are drawn.\n                  ')

    
    # Element stddev uses Python identifier stddev
    __stddev = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stddev'), 'stddev', '__AbsentNamespace0_CTD_ANON_81_stddev', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 166, 14), )

    
    stddev = property(__stddev.value, __stddev.set, None, '\n                    For type "gaussian," the standard deviation of the Gaussian distribution from which noise values are drawn.\n                  ')

    _ElementMap.update({
        __type.name() : __type,
        __mean.name() : __mean,
        __stddev.name() : __stddev
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_81 = CTD_ANON_81


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_82 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element altimeter uses Python identifier altimeter
    __altimeter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'altimeter'), 'altimeter', '__AbsentNamespace0_CTD_ANON_82_altimeter', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 9, 2), )

    
    altimeter = property(__altimeter.value, __altimeter.set, None, None)

    
    # Element camera uses Python identifier camera
    __camera = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'camera'), 'camera', '__AbsentNamespace0_CTD_ANON_82_camera', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 9, 2), )

    
    camera = property(__camera.value, __camera.set, None, None)

    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contact'), 'contact', '__AbsentNamespace0_CTD_ANON_82_contact', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 9, 2), )

    
    contact = property(__contact.value, __contact.set, None, None)

    
    # Element force_torque uses Python identifier force_torque
    __force_torque = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'force_torque'), 'force_torque', '__AbsentNamespace0_CTD_ANON_82_force_torque', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 9, 2), )

    
    force_torque = property(__force_torque.value, __force_torque.set, None, None)

    
    # Element gps uses Python identifier gps
    __gps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'gps'), 'gps', '__AbsentNamespace0_CTD_ANON_82_gps', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 9, 2), )

    
    gps = property(__gps.value, __gps.set, None, None)

    
    # Element imu uses Python identifier imu
    __imu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'imu'), 'imu', '__AbsentNamespace0_CTD_ANON_82_imu', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 9, 2), )

    
    imu = property(__imu.value, __imu.set, None, None)

    
    # Element logical_camera uses Python identifier logical_camera
    __logical_camera = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'logical_camera'), 'logical_camera', '__AbsentNamespace0_CTD_ANON_82_logical_camera', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 9, 2), )

    
    logical_camera = property(__logical_camera.value, __logical_camera.set, None, None)

    
    # Element magnetometer uses Python identifier magnetometer
    __magnetometer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'magnetometer'), 'magnetometer', '__AbsentNamespace0_CTD_ANON_82_magnetometer', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 9, 2), )

    
    magnetometer = property(__magnetometer.value, __magnetometer.set, None, None)

    
    # Element plugin uses Python identifier plugin
    __plugin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'plugin'), 'plugin', '__AbsentNamespace0_CTD_ANON_82_plugin', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2), )

    
    plugin = property(__plugin.value, __plugin.set, None, None)

    
    # Element ray uses Python identifier ray
    __ray = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ray'), 'ray', '__AbsentNamespace0_CTD_ANON_82_ray', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 9, 2), )

    
    ray = property(__ray.value, __ray.set, None, None)

    
    # Element rfidtag uses Python identifier rfidtag
    __rfidtag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rfidtag'), 'rfidtag', '__AbsentNamespace0_CTD_ANON_82_rfidtag', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/rfid.xsd', 4, 2), )

    
    rfidtag = property(__rfidtag.value, __rfidtag.set, None, None)

    
    # Element rfid uses Python identifier rfid
    __rfid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rfid'), 'rfid', '__AbsentNamespace0_CTD_ANON_82_rfid', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/rfidtag.xsd', 4, 2), )

    
    rfid = property(__rfid.value, __rfid.set, None, None)

    
    # Element always_on uses Python identifier always_on
    __always_on = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'always_on'), 'always_on', '__AbsentNamespace0_CTD_ANON_82_always_on', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 27, 8), )

    
    always_on = property(__always_on.value, __always_on.set, None, '\n              If true the sensor will always be updated according to the update rate.\n            ')

    
    # Element update_rate uses Python identifier update_rate
    __update_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'update_rate'), 'update_rate', '__AbsentNamespace0_CTD_ANON_82_update_rate', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 36, 8), )

    
    update_rate = property(__update_rate.value, __update_rate.set, None, '\n              The frequency at which the sensor data is generated. If left unspecified, the sensor will generate data every cycle.\n            ')

    
    # Element visualize uses Python identifier visualize
    __visualize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visualize'), 'visualize', '__AbsentNamespace0_CTD_ANON_82_visualize', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 45, 8), )

    
    visualize = property(__visualize.value, __visualize.set, None, '\n              If true, the sensor is visualized in the GUI\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_82_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 54, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              This is the pose of the sensor, relative to the parent (link or joint) reference frame.\n            ')

    
    # Element topic uses Python identifier topic
    __topic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'topic'), 'topic', '__AbsentNamespace0_CTD_ANON_82_topic', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 63, 8), )

    
    topic = property(__topic.value, __topic.set, None, '\n              Name of the topic on which data is published. This is necessary for visualization\n            ')

    
    # Element sonar uses Python identifier sonar
    __sonar = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sonar'), 'sonar', '__AbsentNamespace0_CTD_ANON_82_sonar', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 9, 2), )

    
    sonar = property(__sonar.value, __sonar.set, None, None)

    
    # Element transceiver uses Python identifier transceiver
    __transceiver = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transceiver'), 'transceiver', '__AbsentNamespace0_CTD_ANON_82_transceiver', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 9, 2), )

    
    transceiver = property(__transceiver.value, __transceiver.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_82_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 86, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 86, 6)
    
    name = property(__name.value, __name.set, None, '\n            A unique name for the sensor. This name must not match another model in the model.\n          ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_82_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 93, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 93, 6)
    
    type = property(__type.value, __type.set, None, '\n            The type name of the sensor. By default, SDF supports types\n                  altimeter,\n                  camera,\n                  contact,\n                  depth,\n                  force_torque,\n                  gps,\n                  gpu_ray,\n                  imu,\n                  logical_camera,\n                  magnetometer,\n                  multicamera,\n                  ray,\n                  rfid,\n                  rfidtag,\n                  sonar,\n                  wireless_receiver, and\n                  wireless_transmitter.\n          ')

    _ElementMap.update({
        __altimeter.name() : __altimeter,
        __camera.name() : __camera,
        __contact.name() : __contact,
        __force_torque.name() : __force_torque,
        __gps.name() : __gps,
        __imu.name() : __imu,
        __logical_camera.name() : __logical_camera,
        __magnetometer.name() : __magnetometer,
        __plugin.name() : __plugin,
        __ray.name() : __ray,
        __rfidtag.name() : __rfidtag,
        __rfid.name() : __rfid,
        __always_on.name() : __always_on,
        __update_rate.name() : __update_rate,
        __visualize.name() : __visualize,
        __pose.name() : __pose,
        __topic.name() : __topic,
        __sonar.name() : __sonar,
        __transceiver.name() : __transceiver
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_82 = CTD_ANON_82


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_83 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element min uses Python identifier min
    __min = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__AbsentNamespace0_CTD_ANON_83_min', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 13, 8), )

    
    min = property(__min.value, __min.set, None, '\n              Minimum range\n            ')

    
    # Element max uses Python identifier max
    __max = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__AbsentNamespace0_CTD_ANON_83_max', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 22, 8), )

    
    max = property(__max.value, __max.set, None, '\n              Max range\n            ')

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_CTD_ANON_83_radius', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 31, 8), )

    
    radius = property(__radius.value, __radius.set, None, '\n              Radius of the sonar cone at max range.\n            ')

    _ElementMap.update({
        __min.name() : __min,
        __max.name() : __max,
        __radius.name() : __radius
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_83 = CTD_ANON_83


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_84 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/sphere_shape.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_CTD_ANON_84_radius', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/sphere_shape.xsd', 13, 8), )

    
    radius = property(__radius.value, __radius.set, None, '\n              radius of the sphere\n            ')

    _ElementMap.update({
        __radius.name() : __radius
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_84 = CTD_ANON_84


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_85 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element bounce uses Python identifier bounce
    __bounce = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bounce'), 'bounce', '__AbsentNamespace0_CTD_ANON_85_bounce', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 13, 8), )

    
    bounce = property(__bounce.value, __bounce.set, None, None)

    
    # Element friction uses Python identifier friction
    __friction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'friction'), 'friction', '__AbsentNamespace0_CTD_ANON_85_friction', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 39, 8), )

    
    friction = property(__friction.value, __friction.set, None, None)

    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact'), 'contact', '__AbsentNamespace0_CTD_ANON_85_contact', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 149, 8), )

    
    contact = property(__contact.value, __contact.set, None, None)

    
    # Element soft_contact uses Python identifier soft_contact
    __soft_contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'soft_contact'), 'soft_contact', '__AbsentNamespace0_CTD_ANON_85_soft_contact', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 318, 8), )

    
    soft_contact = property(__soft_contact.value, __soft_contact.set, None, None)

    _ElementMap.update({
        __bounce.name() : __bounce,
        __friction.name() : __friction,
        __contact.name() : __contact,
        __soft_contact.name() : __soft_contact
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_85 = CTD_ANON_85


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_86 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 14, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element restitution_coefficient uses Python identifier restitution_coefficient
    __restitution_coefficient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'restitution_coefficient'), 'restitution_coefficient', '__AbsentNamespace0_CTD_ANON_86_restitution_coefficient', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 17, 14), )

    
    restitution_coefficient = property(__restitution_coefficient.value, __restitution_coefficient.set, None, '\n                    Bounciness coefficient of restitution, from [0...1], where 0=no bounciness.\n                  ')

    
    # Element threshold uses Python identifier threshold
    __threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'threshold'), 'threshold', '__AbsentNamespace0_CTD_ANON_86_threshold', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 26, 14), )

    
    threshold = property(__threshold.value, __threshold.set, None, '\n                    Bounce capture velocity, below which effective coefficient of restitution is 0.\n                  ')

    _ElementMap.update({
        __restitution_coefficient.name() : __restitution_coefficient,
        __threshold.name() : __threshold
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_86 = CTD_ANON_86


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_87 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 40, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ode uses Python identifier ode
    __ode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ode'), 'ode', '__AbsentNamespace0_CTD_ANON_87_ode', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 43, 14), )

    
    ode = property(__ode.value, __ode.set, None, '\n                    ODE friction parameters\n                  ')

    
    # Element bullet uses Python identifier bullet
    __bullet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bullet'), 'bullet', '__AbsentNamespace0_CTD_ANON_87_bullet', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 101, 14), )

    
    bullet = property(__bullet.value, __bullet.set, None, None)

    _ElementMap.update({
        __ode.name() : __ode,
        __bullet.name() : __bullet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_87 = CTD_ANON_87


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_88 (pyxb.binding.basis.complexTypeDefinition):
    """
                    ODE friction parameters
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 49, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mu uses Python identifier mu
    __mu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mu'), 'mu', '__AbsentNamespace0_CTD_ANON_88_mu', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 52, 20), )

    
    mu = property(__mu.value, __mu.set, None, '\n                          Coefficient of friction in the range of [0..1].\n                        ')

    
    # Element mu2 uses Python identifier mu2
    __mu2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mu2'), 'mu2', '__AbsentNamespace0_CTD_ANON_88_mu2', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 61, 20), )

    
    mu2 = property(__mu2.value, __mu2.set, None, '\n                          Second coefficient of friction in the range of [0..1]\n                        ')

    
    # Element fdir1 uses Python identifier fdir1
    __fdir1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fdir1'), 'fdir1', '__AbsentNamespace0_CTD_ANON_88_fdir1', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 70, 20), )

    
    fdir1 = property(__fdir1.value, __fdir1.set, None, '\n                          3-tuple specifying direction of mu1 in the collision local reference frame.\n                        ')

    
    # Element slip1 uses Python identifier slip1
    __slip1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'slip1'), 'slip1', '__AbsentNamespace0_CTD_ANON_88_slip1', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 79, 20), )

    
    slip1 = property(__slip1.value, __slip1.set, None, '\n                          Force dependent slip direction 1 in collision local frame, between the range of [0..1].\n                        ')

    
    # Element slip2 uses Python identifier slip2
    __slip2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'slip2'), 'slip2', '__AbsentNamespace0_CTD_ANON_88_slip2', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 88, 20), )

    
    slip2 = property(__slip2.value, __slip2.set, None, '\n                          Force dependent slip direction 2 in collision local frame, between the range of [0..1].\n                        ')

    _ElementMap.update({
        __mu.name() : __mu,
        __mu2.name() : __mu2,
        __fdir1.name() : __fdir1,
        __slip1.name() : __slip1,
        __slip2.name() : __slip2
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_88 = CTD_ANON_88


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_89 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 102, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element friction uses Python identifier friction
    __friction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'friction'), 'friction', '__AbsentNamespace0_CTD_ANON_89_friction', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 105, 20), )

    
    friction = property(__friction.value, __friction.set, None, '\n                          Coefficient of friction in the range of [0..1].\n                        ')

    
    # Element friction2 uses Python identifier friction2
    __friction2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'friction2'), 'friction2', '__AbsentNamespace0_CTD_ANON_89_friction2', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 114, 20), )

    
    friction2 = property(__friction2.value, __friction2.set, None, '\n                          Coefficient of friction in the range of [0..1].\n                        ')

    
    # Element fdir1 uses Python identifier fdir1
    __fdir1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fdir1'), 'fdir1', '__AbsentNamespace0_CTD_ANON_89_fdir1', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 123, 20), )

    
    fdir1 = property(__fdir1.value, __fdir1.set, None, '\n                          3-tuple specifying direction of mu1 in the collision local reference frame.\n                        ')

    
    # Element rolling_friction uses Python identifier rolling_friction
    __rolling_friction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rolling_friction'), 'rolling_friction', '__AbsentNamespace0_CTD_ANON_89_rolling_friction', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 132, 20), )

    
    rolling_friction = property(__rolling_friction.value, __rolling_friction.set, None, '\n                           coefficient of friction in the range of [0..1]\n                        ')

    _ElementMap.update({
        __friction.name() : __friction,
        __friction2.name() : __friction2,
        __fdir1.name() : __fdir1,
        __rolling_friction.name() : __rolling_friction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_89 = CTD_ANON_89


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_90 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 150, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element collide_without_contact uses Python identifier collide_without_contact
    __collide_without_contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collide_without_contact'), 'collide_without_contact', '__AbsentNamespace0_CTD_ANON_90_collide_without_contact', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 153, 14), )

    
    collide_without_contact = property(__collide_without_contact.value, __collide_without_contact.set, None, '\n                    Flag to disable contact force generation, while still allowing collision checks and contact visualization to occur.\n                  ')

    
    # Element collide_without_contact_bitmask uses Python identifier collide_without_contact_bitmask
    __collide_without_contact_bitmask = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collide_without_contact_bitmask'), 'collide_without_contact_bitmask', '__AbsentNamespace0_CTD_ANON_90_collide_without_contact_bitmask', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 162, 14), )

    
    collide_without_contact_bitmask = property(__collide_without_contact_bitmask.value, __collide_without_contact_bitmask.set, None, '\n                    Bitmask for collision filtering when collide_without_contact is on \n                  ')

    
    # Element collide_bitmask uses Python identifier collide_bitmask
    __collide_bitmask = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collide_bitmask'), 'collide_bitmask', '__AbsentNamespace0_CTD_ANON_90_collide_bitmask', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 171, 14), )

    
    collide_bitmask = property(__collide_bitmask.value, __collide_bitmask.set, None, '\n                    Bitmask for collision filtering. This will override collide_without_contact\n                  ')

    
    # Element ode uses Python identifier ode
    __ode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ode'), 'ode', '__AbsentNamespace0_CTD_ANON_90_ode', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 180, 14), )

    
    ode = property(__ode.value, __ode.set, None, '\n                    ODE contact parameters\n                  ')

    
    # Element bullet uses Python identifier bullet
    __bullet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bullet'), 'bullet', '__AbsentNamespace0_CTD_ANON_90_bullet', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 247, 14), )

    
    bullet = property(__bullet.value, __bullet.set, None, '\n                    Bullet contact parameters\n                  ')

    _ElementMap.update({
        __collide_without_contact.name() : __collide_without_contact,
        __collide_without_contact_bitmask.name() : __collide_without_contact_bitmask,
        __collide_bitmask.name() : __collide_bitmask,
        __ode.name() : __ode,
        __bullet.name() : __bullet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_90 = CTD_ANON_90


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_91 (pyxb.binding.basis.complexTypeDefinition):
    """
                    ODE contact parameters
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 186, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element soft_cfm uses Python identifier soft_cfm
    __soft_cfm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'soft_cfm'), 'soft_cfm', '__AbsentNamespace0_CTD_ANON_91_soft_cfm', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 189, 20), )

    
    soft_cfm = property(__soft_cfm.value, __soft_cfm.set, None, '\n                          Soft constraint force mixing.\n                        ')

    
    # Element soft_erp uses Python identifier soft_erp
    __soft_erp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'soft_erp'), 'soft_erp', '__AbsentNamespace0_CTD_ANON_91_soft_erp', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 198, 20), )

    
    soft_erp = property(__soft_erp.value, __soft_erp.set, None, '\n                          Soft error reduction parameter\n                        ')

    
    # Element kp uses Python identifier kp
    __kp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'kp'), 'kp', '__AbsentNamespace0_CTD_ANON_91_kp', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 207, 20), )

    
    kp = property(__kp.value, __kp.set, None, '\n                          dynamically "stiffness"-equivalent coefficient for contact joints\n                        ')

    
    # Element kd uses Python identifier kd
    __kd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'kd'), 'kd', '__AbsentNamespace0_CTD_ANON_91_kd', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 216, 20), )

    
    kd = property(__kd.value, __kd.set, None, '\n                          dynamically "damping"-equivalent coefficient for contact joints\n                        ')

    
    # Element max_vel uses Python identifier max_vel
    __max_vel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_vel'), 'max_vel', '__AbsentNamespace0_CTD_ANON_91_max_vel', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 225, 20), )

    
    max_vel = property(__max_vel.value, __max_vel.set, None, '\n                          maximum contact correction velocity truncation term.\n                        ')

    
    # Element min_depth uses Python identifier min_depth
    __min_depth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_depth'), 'min_depth', '__AbsentNamespace0_CTD_ANON_91_min_depth', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 234, 20), )

    
    min_depth = property(__min_depth.value, __min_depth.set, None, '\n                          minimum allowable depth before contact correction impulse is applied\n                        ')

    _ElementMap.update({
        __soft_cfm.name() : __soft_cfm,
        __soft_erp.name() : __soft_erp,
        __kp.name() : __kp,
        __kd.name() : __kd,
        __max_vel.name() : __max_vel,
        __min_depth.name() : __min_depth
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_91 = CTD_ANON_91


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_92 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Bullet contact parameters
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 253, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element soft_cfm uses Python identifier soft_cfm
    __soft_cfm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'soft_cfm'), 'soft_cfm', '__AbsentNamespace0_CTD_ANON_92_soft_cfm', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 256, 20), )

    
    soft_cfm = property(__soft_cfm.value, __soft_cfm.set, None, '\n                          Soft constraint force mixing.\n                        ')

    
    # Element soft_erp uses Python identifier soft_erp
    __soft_erp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'soft_erp'), 'soft_erp', '__AbsentNamespace0_CTD_ANON_92_soft_erp', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 265, 20), )

    
    soft_erp = property(__soft_erp.value, __soft_erp.set, None, '\n                          Soft error reduction parameter\n                        ')

    
    # Element kp uses Python identifier kp
    __kp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'kp'), 'kp', '__AbsentNamespace0_CTD_ANON_92_kp', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 274, 20), )

    
    kp = property(__kp.value, __kp.set, None, '\n                          dynamically "stiffness"-equivalent coefficient for contact joints\n                        ')

    
    # Element kd uses Python identifier kd
    __kd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'kd'), 'kd', '__AbsentNamespace0_CTD_ANON_92_kd', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 283, 20), )

    
    kd = property(__kd.value, __kd.set, None, '\n                          dynamically "damping"-equivalent coefficient for contact joints\n                        ')

    
    # Element split_impulse uses Python identifier split_impulse
    __split_impulse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'split_impulse'), 'split_impulse', '__AbsentNamespace0_CTD_ANON_92_split_impulse', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 292, 20), )

    
    split_impulse = property(__split_impulse.value, __split_impulse.set, None, "\n                          Similar to ODE's max_vel implementation.  See http://bulletphysics.org/mediawiki-1.5.8/index.php/BtContactSolverInfo#Split_Impulse for more information.\n                        ")

    
    # Element split_impulse_penetration_threshold uses Python identifier split_impulse_penetration_threshold
    __split_impulse_penetration_threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'split_impulse_penetration_threshold'), 'split_impulse_penetration_threshold', '__AbsentNamespace0_CTD_ANON_92_split_impulse_penetration_threshold', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 301, 20), )

    
    split_impulse_penetration_threshold = property(__split_impulse_penetration_threshold.value, __split_impulse_penetration_threshold.set, None, "\n                          Similar to ODE's max_vel implementation.  See http://bulletphysics.org/mediawiki-1.5.8/index.php/BtContactSolverInfo#Split_Impulse for more information.\n                        ")

    _ElementMap.update({
        __soft_cfm.name() : __soft_cfm,
        __soft_erp.name() : __soft_erp,
        __kp.name() : __kp,
        __kd.name() : __kd,
        __split_impulse.name() : __split_impulse,
        __split_impulse_penetration_threshold.name() : __split_impulse_penetration_threshold
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_92 = CTD_ANON_92


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_93 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 319, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element dart uses Python identifier dart
    __dart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dart'), 'dart', '__AbsentNamespace0_CTD_ANON_93_dart', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 322, 14), )

    
    dart = property(__dart.value, __dart.set, None, '\n                    soft contact pamameters based on paper:\n             http://www.cc.gatech.edu/graphics/projects/Sumit/homepage/papers/sigasia11/jain_softcontacts_siga11.pdf\n      \n                  ')

    _ElementMap.update({
        __dart.name() : __dart
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_93 = CTD_ANON_93


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_94 (pyxb.binding.basis.complexTypeDefinition):
    """
                    soft contact pamameters based on paper:
             http://www.cc.gatech.edu/graphics/projects/Sumit/homepage/papers/sigasia11/jain_softcontacts_siga11.pdf
      
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 330, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element bone_attachment uses Python identifier bone_attachment
    __bone_attachment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bone_attachment'), 'bone_attachment', '__AbsentNamespace0_CTD_ANON_94_bone_attachment', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 333, 20), )

    
    bone_attachment = property(__bone_attachment.value, __bone_attachment.set, None, '\n                          This is variable k_v in the soft contacts paper.  Its unit is N/m.\n                        ')

    
    # Element stiffness uses Python identifier stiffness
    __stiffness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stiffness'), 'stiffness', '__AbsentNamespace0_CTD_ANON_94_stiffness', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 342, 20), )

    
    stiffness = property(__stiffness.value, __stiffness.set, None, '\n                          This is variable k_e in the soft contacts paper.  Its unit is N/m.\n                        ')

    
    # Element damping uses Python identifier damping
    __damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'damping'), 'damping', '__AbsentNamespace0_CTD_ANON_94_damping', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 351, 20), )

    
    damping = property(__damping.value, __damping.set, None, '\n                          Viscous damping of point velocity in body frame.  Its unit is N/m/s.\n                        ')

    
    # Element flesh_mass_fraction uses Python identifier flesh_mass_fraction
    __flesh_mass_fraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flesh_mass_fraction'), 'flesh_mass_fraction', '__AbsentNamespace0_CTD_ANON_94_flesh_mass_fraction', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 360, 20), )

    
    flesh_mass_fraction = property(__flesh_mass_fraction.value, __flesh_mass_fraction.set, None, '\n                          Fraction of mass to be distributed among deformable nodes.\n                        ')

    _ElementMap.update({
        __bone_attachment.name() : __bone_attachment,
        __stiffness.name() : __stiffness,
        __damping.name() : __damping,
        __flesh_mass_fraction.name() : __flesh_mass_fraction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_94 = CTD_ANON_94


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_95 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element essid uses Python identifier essid
    __essid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'essid'), 'essid', '__AbsentNamespace0_CTD_ANON_95_essid', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 13, 8), )

    
    essid = property(__essid.value, __essid.set, None, '\n              Service set identifier (network name)\n            ')

    
    # Element frequency uses Python identifier frequency
    __frequency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'frequency'), 'frequency', '__AbsentNamespace0_CTD_ANON_95_frequency', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 22, 8), )

    
    frequency = property(__frequency.value, __frequency.set, None, '\n              Specifies the frequency of transmission in MHz\n            ')

    
    # Element min_frequency uses Python identifier min_frequency
    __min_frequency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_frequency'), 'min_frequency', '__AbsentNamespace0_CTD_ANON_95_min_frequency', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 31, 8), )

    
    min_frequency = property(__min_frequency.value, __min_frequency.set, None, '\n              Only a frequency range is filtered. Here we set the lower bound (MHz).\n    \n            ')

    
    # Element max_frequency uses Python identifier max_frequency
    __max_frequency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_frequency'), 'max_frequency', '__AbsentNamespace0_CTD_ANON_95_max_frequency', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 41, 8), )

    
    max_frequency = property(__max_frequency.value, __max_frequency.set, None, '\n              Only a frequency range is filtered. Here we set the upper bound (MHz).\n    \n            ')

    
    # Element gain uses Python identifier gain
    __gain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gain'), 'gain', '__AbsentNamespace0_CTD_ANON_95_gain', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 51, 8), )

    
    gain = property(__gain.value, __gain.set, None, '\n              Specifies the antenna gain in dBi\n            ')

    
    # Element power uses Python identifier power
    __power = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'power'), 'power', '__AbsentNamespace0_CTD_ANON_95_power', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 60, 8), )

    
    power = property(__power.value, __power.set, None, '\n              Specifies the transmission power in dBm\n            ')

    
    # Element sensitivity uses Python identifier sensitivity
    __sensitivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sensitivity'), 'sensitivity', '__AbsentNamespace0_CTD_ANON_95_sensitivity', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 69, 8), )

    
    sensitivity = property(__sensitivity.value, __sensitivity.set, None, '\n              Mininum received signal power in dBm\n            ')

    _ElementMap.update({
        __essid.name() : __essid,
        __frequency.name() : __frequency,
        __min_frequency.name() : __min_frequency,
        __max_frequency.name() : __max_frequency,
        __gain.name() : __gain,
        __power.name() : __power,
        __sensitivity.name() : __sensitivity
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_95 = CTD_ANON_95


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_96 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 13, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'geometry'), 'geometry', '__AbsentNamespace0_CTD_ANON_96_geometry', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 17, 2), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Element material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'material'), 'material', '__AbsentNamespace0_CTD_ANON_96_material', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 9, 2), )

    
    material = property(__material.value, __material.set, None, None)

    
    # Element plugin uses Python identifier plugin
    __plugin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'plugin'), 'plugin', '__AbsentNamespace0_CTD_ANON_96_plugin', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2), )

    
    plugin = property(__plugin.value, __plugin.set, None, None)

    
    # Element cast_shadows uses Python identifier cast_shadows
    __cast_shadows = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cast_shadows'), 'cast_shadows', '__AbsentNamespace0_CTD_ANON_96_cast_shadows', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 16, 8), )

    
    cast_shadows = property(__cast_shadows.value, __cast_shadows.set, None, '\n              If true the visual will cast shadows.\n            ')

    
    # Element laser_retro uses Python identifier laser_retro
    __laser_retro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'laser_retro'), 'laser_retro', '__AbsentNamespace0_CTD_ANON_96_laser_retro', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 25, 8), )

    
    laser_retro = property(__laser_retro.value, __laser_retro.set, None, '\n              will be implemented in the future release.\n            ')

    
    # Element transparency uses Python identifier transparency
    __transparency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transparency'), 'transparency', '__AbsentNamespace0_CTD_ANON_96_transparency', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 34, 8), )

    
    transparency = property(__transparency.value, __transparency.set, None, '\n              The amount of transparency( 0=opaque, 1 = fully transparent)\n            ')

    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_CTD_ANON_96_pose', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 43, 8), )

    
    pose = property(__pose.value, __pose.set, None, '\n              The reference frame of the visual element, relative to the reference frame of the link.\n            ')

    
    # Element meta uses Python identifier meta
    __meta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meta'), 'meta', '__AbsentNamespace0_CTD_ANON_96_meta', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 52, 8), )

    
    meta = property(__meta.value, __meta.set, None, '\n              Optional meta information for the visual. The information contained within this element should be used to provide additional feedback to an end user.\n            ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_96_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 77, 6)
    __name._UseLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 77, 6)
    
    name = property(__name.value, __name.set, None, '\n            Unique name for the visual element within the scope of the parent link.\n          ')

    _ElementMap.update({
        __geometry.name() : __geometry,
        __material.name() : __material,
        __plugin.name() : __plugin,
        __cast_shadows.name() : __cast_shadows,
        __laser_retro.name() : __laser_retro,
        __transparency.name() : __transparency,
        __pose.name() : __pose,
        __meta.name() : __meta
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_96 = CTD_ANON_96


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_97 (pyxb.binding.basis.complexTypeDefinition):
    """
              Optional meta information for the visual. The information contained within this element should be used to provide additional feedback to an end user.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 58, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element layer uses Python identifier layer
    __layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'layer'), 'layer', '__AbsentNamespace0_CTD_ANON_97_layer', True, pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 61, 14), )

    
    layer = property(__layer.value, __layer.set, None, '\n                    The layer in which this visual is displayed. The layer number is useful for programs, such as Gazebo, that put visuals in different layers for enhanced visualization.\n                  ')

    _ElementMap.update({
        __layer.name() : __layer
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_97 = CTD_ANON_97


audio_sink = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audio_sink'), pyxb.binding.datatypes.anyType, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_sink.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', audio_sink.name().localName(), audio_sink)

rfidtag = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rfidtag'), pyxb.binding.datatypes.anyType, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/rfid.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', rfidtag.name().localName(), rfidtag)

rfid = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rfid'), pyxb.binding.datatypes.anyType, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/rfidtag.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', rfid.name().localName(), rfid)

model = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'model'), CTD_ANON, location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 13, 2))
Namespace.addCategoryObject('elementBinding', model.name().localName(), model)

altimeter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'altimeter'), CTD_ANON_2, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', altimeter.name().localName(), altimeter)

audio_source = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audio_source'), CTD_ANON_5, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', audio_source.name().localName(), audio_source)

box = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'box'), CTD_ANON_7, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/box_shape.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', box.name().localName(), box)

camera = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'camera'), CTD_ANON_8, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', camera.name().localName(), camera)

collision = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collision'), CTD_ANON_15, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 11, 2))
Namespace.addCategoryObject('elementBinding', collision.name().localName(), collision)

contact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contact'), CTD_ANON_16, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', contact.name().localName(), contact)

cylinder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cylinder'), CTD_ANON_17, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', cylinder.name().localName(), cylinder)

force_torque = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'force_torque'), CTD_ANON_18, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', force_torque.name().localName(), force_torque)

geometry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geometry'), CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 17, 2))
Namespace.addCategoryObject('elementBinding', geometry.name().localName(), geometry)

gps = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gps'), CTD_ANON_21, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', gps.name().localName(), gps)

gripper = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gripper'), CTD_ANON_28, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', gripper.name().localName(), gripper)

heightmap = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heightmap'), CTD_ANON_30, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', heightmap.name().localName(), heightmap)

image = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), CTD_ANON_33, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', image.name().localName(), image)

imu = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'imu'), CTD_ANON_34, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', imu.name().localName(), imu)

inertial = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inertial'), CTD_ANON_46, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', inertial.name().localName(), inertial)

joint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'joint'), CTD_ANON_48, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 10, 2))
Namespace.addCategoryObject('elementBinding', joint.name().localName(), joint)

link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), CTD_ANON_60, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 16, 2))
Namespace.addCategoryObject('elementBinding', link.name().localName(), link)

logical_camera = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logical_camera'), CTD_ANON_62, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', logical_camera.name().localName(), logical_camera)

magnetometer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'magnetometer'), CTD_ANON_63, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', magnetometer.name().localName(), magnetometer)

material = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'material'), CTD_ANON_67, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', material.name().localName(), material)

mesh = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mesh'), CTD_ANON_70, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', mesh.name().localName(), mesh)

plane = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plane'), CTD_ANON_72, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', plane.name().localName(), plane)

plugin = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plugin'), CTD_ANON_73, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', plugin.name().localName(), plugin)

polyline = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'polyline'), CTD_ANON_74, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', polyline.name().localName(), polyline)

projector = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'projector'), CTD_ANON_75, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 5, 2))
Namespace.addCategoryObject('elementBinding', projector.name().localName(), projector)

ray = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ray'), CTD_ANON_76, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', ray.name().localName(), ray)

sensor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sensor'), CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 23, 2))
Namespace.addCategoryObject('elementBinding', sensor.name().localName(), sensor)

sonar = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sonar'), CTD_ANON_83, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', sonar.name().localName(), sonar)

sphere = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sphere'), CTD_ANON_84, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sphere_shape.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', sphere.name().localName(), sphere)

surface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'surface'), CTD_ANON_85, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', surface.name().localName(), surface)

transceiver = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transceiver'), CTD_ANON_95, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 9, 2))
Namespace.addCategoryObject('elementBinding', transceiver.name().localName(), transceiver)

visual = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'visual'), CTD_ANON_96, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 12, 2))
Namespace.addCategoryObject('elementBinding', visual.name().localName(), visual)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'static'), pyxb.binding.datatypes.boolean, scope=CTD_ANON, documentation='\n              If set to true, the model is immovable. Otherwise the model is simulated in the dynamics engine.\n            ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 17, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'self_collide'), pyxb.binding.datatypes.boolean, scope=CTD_ANON, documentation='\n              If set to true, all links in the model will collide with each other (except those connected by a joint). Can be overridden by the link or collision element self_collide property. Two links within a model will collide if link1.self_collide OR link2.self_collide. Links connected by a joint will never collide.\n            ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 26, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'allow_auto_disable'), pyxb.binding.datatypes.boolean, scope=CTD_ANON, documentation='\n              Allows a model to auto-disable, which is means the physics engine can skip updating the model when the model is at rest. This parameter is only used by models with no joints.\n            ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 35, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON, documentation='\n              A position and orientation in the global coordinate frame for the model. Position(x,y,z) and rotation (roll, pitch yaw) in the global coordinate frame.\n            ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 44, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'include'), CTD_ANON_, scope=CTD_ANON, documentation='\n              Include resources from a URI. This can be used to nest models.\n            ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 53, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gripper'), CTD_ANON_28, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 4, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'joint'), CTD_ANON_48, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 10, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), CTD_ANON_60, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 16, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plugin'), CTD_ANON_73, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 16, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 25, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 34, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 43, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 52, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'static')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 17, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'self_collide')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 26, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'allow_auto_disable')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 35, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 44, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'include')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 53, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'link')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 101, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'joint')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 102, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'plugin')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 103, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gripper')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 104, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uri'), pyxb.binding.datatypes.string, scope=CTD_ANON_, documentation='\n                    URI to a resource, such as a model\n                  ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 62, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_, documentation='\n                    Override the pose of the included model. A position and orientation in the global coordinate frame for the model. Position(x,y,z) and rotation (roll, pitch yaw) in the global coordinate frame.\n                  ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 71, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_, documentation='\n                    Override the name of the included model.\n                  ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 80, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'static'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_, documentation='\n                    Override the static value of the included model.\n                  ', location=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 89, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 70, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 79, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 88, 14))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'uri')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 62, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 71, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 80, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'static')), pyxb.utils.utility.Location('/home/gchen/Dropbox/project/HBP-RD/BlenderRobotDesigner/resources/sdf_model.xsd', 89, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vertical_position'), CTD_ANON_3, scope=CTD_ANON_2, documentation='\n              \n      Noise parameters for vertical position\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 13, 8)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vertical_velocity'), CTD_ANON_4, scope=CTD_ANON_2, documentation='\n              \n      Noise parameters for vertical velocity\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 28, 8)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 27, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'vertical_position')), pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'vertical_velocity')), pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 28, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uri'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, documentation='\n              URI of the audio media.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 13, 8)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pitch'), pyxb.binding.datatypes.double, scope=CTD_ANON_5, documentation='\n              Pitch for the audio media, in Hz\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 22, 8)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gain'), pyxb.binding.datatypes.double, scope=CTD_ANON_5, documentation='\n              Gain for the audio media, in dB.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 31, 8)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact'), CTD_ANON_6, scope=CTD_ANON_5, documentation='\n              List of collision objects that will trigger audio playback.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 40, 8)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'loop'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_5, documentation='\n              True to make the audio source loop playback.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 62, 8)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_5, documentation='\n              A position and orientation in the parent coordinate frame for the audio source. Position(x,y,z) and rotation (roll, pitch yaw) in the parent coordinate frame.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 71, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 21, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 30, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 39, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 61, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 70, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'uri')), pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'pitch')), pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'gain')), pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 31, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'contact')), pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 40, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'loop')), pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 62, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 71, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collision'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, documentation='\n                    Name of child collision element that will trigger audio playback.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 49, 14)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'collision')), pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 49, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'size'), vector3, scope=CTD_ANON_7, documentation='\n              The three side lengths of the box. The origin of the box is in its geometric center (inside the center of the box).\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/box_shape.xsd', 13, 8)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'size')), pyxb.utils.utility.Location('http://sdformat.org/schemas/box_shape.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_8, documentation='\n              A position and orientation in the parent coordinate frame for the camera.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 13, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'horizontal_fov'), pyxb.binding.datatypes.double, scope=CTD_ANON_8, documentation='\n              Horizontal field of view\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 22, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), CTD_ANON_9, scope=CTD_ANON_8, documentation='\n              The image size in pixels and format.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 31, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'clip'), CTD_ANON_10, scope=CTD_ANON_8, documentation='\n              The near and far clip planes. Objects closer or farther than these planes are not rendered.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 71, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'save'), CTD_ANON_11, scope=CTD_ANON_8, documentation='\n              Enable or disable saving of camera frames.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 102, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'depth_camera'), CTD_ANON_12, scope=CTD_ANON_8, documentation='\n              Depth camera parameters\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 131, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'noise'), CTD_ANON_13, scope=CTD_ANON_8, documentation='\n              The properties of the noise model that should be applied to generated images\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 153, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'distortion'), CTD_ANON_14, scope=CTD_ANON_8, documentation='\n              Lens distortion to be applied to camera images. See http://en.wikipedia.org/wiki/Distortion_(optics)#Software_correction\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 193, 8)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 101, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 130, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 152, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 192, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'horizontal_fov')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 31, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'clip')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 71, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'save')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 102, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'depth_camera')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 131, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'noise')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 153, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'distortion')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 193, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'width'), pyxb.binding.datatypes.int, scope=CTD_ANON_9, documentation='\n                    Width in pixels\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 40, 14)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), pyxb.binding.datatypes.int, scope=CTD_ANON_9, documentation='\n                    Height in pixels \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 49, 14)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'format'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, documentation='\n                    (L8|R8G8B8|B8G8R8|BAYER_RGGB8|BAYER_BGGR8|BAYER_GBRG8|BAYER_GRBG8)\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 58, 14)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 57, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'width')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 40, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 49, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, 'format')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 58, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'near'), pyxb.binding.datatypes.double, scope=CTD_ANON_10, documentation='\n                    Near clipping plane\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 80, 14)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'far'), pyxb.binding.datatypes.double, scope=CTD_ANON_10, documentation='\n                    Far clipping plane\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 89, 14)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'near')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 80, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'far')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 89, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'path'), pyxb.binding.datatypes.string, scope=CTD_ANON_11, documentation='\n                    The path name which will hold the frame data. If path name is relative, then directory is relative to current working directory.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 111, 14)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, 'path')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 111, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, documentation='\n                    Type of output\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 140, 14)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'output')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 140, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, documentation='\n                    The type of noise.  Currently supported types are: "gaussian" (draw additive noise values independently for each pixel from a Gaussian distribution).\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 162, 14)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mean'), pyxb.binding.datatypes.double, scope=CTD_ANON_13, documentation='\n                    For type "gaussian," the mean of the Gaussian distribution from which noise values are drawn.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 171, 14)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stddev'), pyxb.binding.datatypes.double, scope=CTD_ANON_13, documentation='\n                    For type "gaussian," the standard deviation of the Gaussian distribution from which noise values are drawn.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 180, 14)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 170, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 179, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 162, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'mean')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 171, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'stddev')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 180, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_13()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'k1'), pyxb.binding.datatypes.double, scope=CTD_ANON_14, documentation='\n                    The radial distortion coefficient k1\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 202, 14)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'k2'), pyxb.binding.datatypes.double, scope=CTD_ANON_14, documentation='\n                    The radial distortion coefficient k2\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 211, 14)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'k3'), pyxb.binding.datatypes.double, scope=CTD_ANON_14, documentation='\n                    The radial distortion coefficient k3\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 220, 14)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'p1'), pyxb.binding.datatypes.double, scope=CTD_ANON_14, documentation='\n                    The tangential distortion coefficient p1\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 229, 14)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'p2'), pyxb.binding.datatypes.double, scope=CTD_ANON_14, documentation='\n                    The tangential distortion coefficient p2\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 238, 14)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'center'), vector2d, scope=CTD_ANON_14, documentation='\n                    The distortion center or principal point\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 247, 14)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 201, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 210, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 219, 14))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 228, 14))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 237, 14))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 246, 14))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'k1')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 202, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'k2')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 211, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'k3')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 220, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'p1')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 229, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'p2')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 238, 14))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, 'center')), pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 247, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'laser_retro'), pyxb.binding.datatypes.double, scope=CTD_ANON_15, documentation='\n              intensity value returned by laser sensor.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 15, 8)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_contacts'), pyxb.binding.datatypes.int, scope=CTD_ANON_15, documentation='\n              Maximum number of contacts allowed between two entities. This value overrides the max_contacts element defined in physics.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 24, 8)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_15, documentation='\n              The reference frame of the collision element, relative to the reference frame of the link.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 33, 8)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geometry'), CTD_ANON_19, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 17, 2)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'surface'), CTD_ANON_85, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 9, 2)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 14, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 23, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 32, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'laser_retro')), pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 15, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'max_contacts')), pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 24, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 33, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geometry')), pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 41, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'surface')), pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 42, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_15()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collision'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, documentation='\n              name of the collision element within a link that acts as the contact sensor.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 13, 8)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'topic'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, documentation='\n              Topic on which contact data is published.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 22, 8)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'collision')), pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, 'topic')), pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_16()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), pyxb.binding.datatypes.double, scope=CTD_ANON_17, documentation='\n              Radius of the cylinder\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 13, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'length'), pyxb.binding.datatypes.double, scope=CTD_ANON_17, documentation='\n              Length of the cylinder\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 22, 8)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, 'length')), pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_17()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'frame'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, documentation='\n              \n      Frame in which to report the wrench values. Currently supported frames are:\n        "parent" report the wrench expressed in the orientation of the parent link frame,\n        "child" report the wrench expressed in the orientation of the child link frame,\n        "sensor" report the wrench expressed in the orientation of the joint sensor frame.\n      Note that for each option the point with respect to which the \n      torque component of the wrench is expressed is the joint origin.\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 13, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'measure_direction'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, documentation='\n              \n      Direction of the wrench measured by the sensor. The supported options are:\n        "parent_to_child" if the measured wrench is the one applied by parent link on the child link,\n        "child_to_parent" if the measured wrench is the one applied by the child link on the parent link.\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 29, 8)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 28, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'frame')), pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(None, 'measure_direction')), pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 29, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_18()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'box'), CTD_ANON_7, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/box_shape.xsd', 9, 2)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cylinder'), CTD_ANON_17, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/cylinder_shape.xsd', 9, 2)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'empty'), CTD_ANON_20, scope=CTD_ANON_19, documentation='\n              You can use the empty tag to make empty geometries.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 21, 8)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heightmap'), CTD_ANON_30, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 9, 2)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'image'), CTD_ANON_33, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 9, 2)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mesh'), CTD_ANON_70, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 9, 2)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plane'), CTD_ANON_72, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 9, 2)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'polyline'), CTD_ANON_74, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 9, 2)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sphere'), CTD_ANON_84, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sphere_shape.xsd', 9, 2)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 20, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(None, 'empty')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 21, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'box')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 33, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cylinder')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 34, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heightmap')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 35, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'image')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 36, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mesh')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 37, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'plane')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 38, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'polyline')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 39, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sphere')), pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 40, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_19()




def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_20()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'position_sensing'), CTD_ANON_22, scope=CTD_ANON_21, documentation='\n              \n      Parameters related to GPS position measurement.\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 13, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'velocity_sensing'), CTD_ANON_25, scope=CTD_ANON_21, documentation='\n              \n      Parameters related to GPS position measurement.\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 58, 8)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 57, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'position_sensing')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(None, 'velocity_sensing')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 58, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_21()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'horizontal'), CTD_ANON_23, scope=CTD_ANON_22, documentation='\n                    \n        Noise parameters for horizontal position measurement, in units of meters.\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 24, 14)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vertical'), CTD_ANON_24, scope=CTD_ANON_22, documentation='\n                    \n        Noise parameters for vertical position measurement, in units of meters.\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 39, 14)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 23, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 38, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'horizontal')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 24, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(None, 'vertical')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 39, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_22()




def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_23()




def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_24()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'horizontal'), CTD_ANON_26, scope=CTD_ANON_25, documentation='\n                    \n        Noise parameters for horizontal velocity measurement, in units of meters/second.\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 69, 14)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vertical'), CTD_ANON_27, scope=CTD_ANON_25, documentation='\n                    \n        Noise parameters for vertical velocity measurement, in units of meters/second.\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 84, 14)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 68, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 83, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, 'horizontal')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 69, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(None, 'vertical')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 84, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_25()




def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_26()




def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_27()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'grasp_check'), CTD_ANON_29, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 8, 8)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gripper_link'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 28, 8)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'palm_link'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 32, 8)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 7, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(None, 'grasp_check')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 8, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(None, 'gripper_link')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 28, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(None, 'palm_link')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 32, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_28()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'detach_steps'), pyxb.binding.datatypes.int, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 12, 14)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'attach_steps'), pyxb.binding.datatypes.int, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 16, 14)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_contact_count'), pyxb.binding.datatypes.unsignedInt, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 20, 14)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 11, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 15, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 19, 14))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'detach_steps')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 12, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'attach_steps')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 16, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(None, 'min_contact_count')), pyxb.utils.utility.Location('http://sdformat.org/schemas/gripper.xsd', 20, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_29()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uri'), pyxb.binding.datatypes.string, scope=CTD_ANON_30, documentation='\n              URI to a grayscale image file\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 13, 8)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'size'), vector3, scope=CTD_ANON_30, documentation='\n              The size of the heightmap in world units.\n      When loading an image: "size" is used if present, otherwise defaults to 1x1x1.\n      When loading a DEM: "size" is used if present, otherwise defaults to true size of DEM.\n  \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 22, 8)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pos'), vector3, scope=CTD_ANON_30, documentation='\n              A position offset.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 34, 8)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'texture'), CTD_ANON_31, scope=CTD_ANON_30, documentation='\n              The heightmap can contain multiple textures. The order of the texture matters. The first texture will appear at the lowest height, and the last texture at the highest height. Use blend to control the height thresholds and fade between textures.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 43, 8)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'blend'), CTD_ANON_32, scope=CTD_ANON_30, documentation='\n              The blend tag controls how two adjacent textures are mixed. The number of blend elements should equal one less than the number of textures.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 83, 8)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'use_terrain_paging'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_30, documentation='\n              Set if the rendering engine will use terrain paging\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 114, 8)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 21, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 33, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 42, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 82, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 113, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'uri')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'size')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'pos')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 34, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'texture')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 43, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'blend')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 83, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(None, 'use_terrain_paging')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 114, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_30()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'size'), pyxb.binding.datatypes.double, scope=CTD_ANON_31, documentation='\n                    Size of the applied texture in meters.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 52, 14)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'diffuse'), pyxb.binding.datatypes.string, scope=CTD_ANON_31, documentation='\n                    Diffuse texture image filename\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 61, 14)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'normal'), pyxb.binding.datatypes.string, scope=CTD_ANON_31, documentation='\n                    Normalmap texture image filename\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 70, 14)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'size')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 52, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'diffuse')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 61, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(None, 'normal')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 70, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_31()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_height'), pyxb.binding.datatypes.double, scope=CTD_ANON_32, documentation='\n                    Min height of a blend layer\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 92, 14)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fade_dist'), pyxb.binding.datatypes.double, scope=CTD_ANON_32, documentation='\n                    Distance over which the blend occurs\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 101, 14)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(None, 'min_height')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 92, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(None, 'fade_dist')), pyxb.utils.utility.Location('http://sdformat.org/schemas/heightmap_shape.xsd', 101, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_32()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uri'), pyxb.binding.datatypes.string, scope=CTD_ANON_33, documentation='\n              URI of the grayscale image file\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 13, 8)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'scale'), pyxb.binding.datatypes.double, scope=CTD_ANON_33, documentation='\n              Scaling factor applied to the image\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 22, 8)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'threshold'), pyxb.binding.datatypes.int, scope=CTD_ANON_33, documentation='\n              Grayscale threshold\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 31, 8)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), pyxb.binding.datatypes.double, scope=CTD_ANON_33, documentation='\n              Height of the extruded boxes\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 40, 8)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'granularity'), pyxb.binding.datatypes.int, scope=CTD_ANON_33, documentation='\n              The amount of error in the model\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 49, 8)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(None, 'uri')), pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(None, 'scale')), pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(None, 'threshold')), pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 31, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 40, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(None, 'granularity')), pyxb.utils.utility.Location('http://sdformat.org/schemas/image_shape.xsd', 49, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_33()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'topic'), pyxb.binding.datatypes.string, scope=CTD_ANON_34, documentation='\n              Topic on which data is published.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 13, 8)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'angular_velocity'), CTD_ANON_35, scope=CTD_ANON_34, documentation='\n              These elements are specific to body-frame angular velocity,\n    which is expressed in radians per second\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 22, 8)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'linear_acceleration'), CTD_ANON_39, scope=CTD_ANON_34, documentation='\n              These elements are specific to body-frame linear acceleration,\n    which is expressed in meters per second squared\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 75, 8)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'noise'), CTD_ANON_43, scope=CTD_ANON_34, documentation='\n              The properties of the noise model that should be applied to generated data\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 128, 8)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 21, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 74, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 127, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'topic')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'angular_velocity')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'linear_acceleration')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 75, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(None, 'noise')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 128, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_34()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'x'), CTD_ANON_36, scope=CTD_ANON_35, documentation='\n                    Angular velocity about the X axis\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 32, 14)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'y'), CTD_ANON_37, scope=CTD_ANON_35, documentation='\n                    Angular velocity about the Y axis\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 45, 14)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'z'), CTD_ANON_38, scope=CTD_ANON_35, documentation='\n                    Angular velocity about the Z axis\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 58, 14)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 31, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 44, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 57, 14))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'x')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 32, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'y')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 45, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(None, 'z')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 58, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_35()




def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_36()




def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_37()




def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_38()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'x'), CTD_ANON_40, scope=CTD_ANON_39, documentation='\n                    Linear acceleration about the X axis\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 85, 14)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'y'), CTD_ANON_41, scope=CTD_ANON_39, documentation='\n                    Linear acceleration about the Y axis\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 98, 14)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'z'), CTD_ANON_42, scope=CTD_ANON_39, documentation='\n                    Linear acceleration about the Z axis\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 111, 14)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 84, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 97, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 110, 14))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(None, 'x')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 85, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(None, 'y')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 98, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(None, 'z')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 111, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_39()




def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_40._Automaton = _BuildAutomaton_40()




def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_41._Automaton = _BuildAutomaton_41()




def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_42._Automaton = _BuildAutomaton_42()




CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=CTD_ANON_43, documentation='\n                    The type of noise.  Currently supported types are: "gaussian" (draw noise values independently for each beam from a Gaussian distribution).\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 137, 14)))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rate'), CTD_ANON_44, scope=CTD_ANON_43, documentation='\n                    Noise parameters for angular rates.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 146, 14)))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'accel'), CTD_ANON_45, scope=CTD_ANON_43, documentation='\n                    Noise parameters for linear accelerations.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 195, 14)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 137, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(None, 'rate')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 146, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(None, 'accel')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 195, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_43._Automaton = _BuildAutomaton_43()




CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mean'), pyxb.binding.datatypes.double, scope=CTD_ANON_44, documentation='\n                          For type "gaussian," the mean of the Gaussian distribution from which noise values are drawn.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 155, 20)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stddev'), pyxb.binding.datatypes.double, scope=CTD_ANON_44, documentation='\n                          For type "gaussian," the standard deviation of the Gaussian distribution from which noise values are drawn.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 164, 20)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bias_mean'), pyxb.binding.datatypes.double, scope=CTD_ANON_44, documentation='\n                          For type "gaussian," the mean of the Gaussian distribution from which bias values are drawn.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 173, 20)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bias_stddev'), pyxb.binding.datatypes.double, scope=CTD_ANON_44, documentation='\n                          For type "gaussian," the standard deviation of the Gaussian distribution from which bias values are drawn.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 182, 20)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 154, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 163, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 172, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 181, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(None, 'mean')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 155, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(None, 'stddev')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 164, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(None, 'bias_mean')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 173, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(None, 'bias_stddev')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 182, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_44._Automaton = _BuildAutomaton_44()




CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mean'), pyxb.binding.datatypes.double, scope=CTD_ANON_45, documentation='\n                          For type "gaussian," the mean of the Gaussian distribution from which noise values are drawn.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 204, 20)))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stddev'), pyxb.binding.datatypes.double, scope=CTD_ANON_45, documentation='\n                          For type "gaussian," the standard deviation of the Gaussian distribution from which noise values are drawn.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 213, 20)))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bias_mean'), pyxb.binding.datatypes.double, scope=CTD_ANON_45, documentation='\n                          For type "gaussian," the mean of the Gaussian distribution from which bias values are drawn.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 222, 20)))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bias_stddev'), pyxb.binding.datatypes.double, scope=CTD_ANON_45, documentation='\n                          For type "gaussian," the standard deviation of the Gaussian distribution from which bias values are drawn.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 231, 20)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 203, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 212, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 221, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 230, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(None, 'mean')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 204, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(None, 'stddev')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 213, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(None, 'bias_mean')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 222, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(None, 'bias_stddev')), pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 231, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_45._Automaton = _BuildAutomaton_45()




CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mass'), pyxb.binding.datatypes.double, scope=CTD_ANON_46, documentation='\n              The mass of the link.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 13, 8)))

CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_46, documentation='\n              This is the pose of the inertial reference frame, relative to the link reference frame. The origin of the inertial reference frame needs to be at the center of gravity. The axes of the inertial reference frame do not need to be aligned with the principal axes of the inertia.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 22, 8)))

CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inertia'), CTD_ANON_47, scope=CTD_ANON_46, documentation='\n              The 3x3 rotational inertia matrix. Because the rotational inertia matrix is symmetric, only 6 above-diagonal elements of this matrix are specified here, using the attributes ixx, ixy, ixz, iyy, iyz, izz.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 31, 8)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 21, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 30, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(None, 'mass')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(None, 'inertia')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 31, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_46._Automaton = _BuildAutomaton_46()




CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ixx'), pyxb.binding.datatypes.double, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 40, 14)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ixy'), pyxb.binding.datatypes.double, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 44, 14)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ixz'), pyxb.binding.datatypes.double, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 48, 14)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'iyy'), pyxb.binding.datatypes.double, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 52, 14)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'iyz'), pyxb.binding.datatypes.double, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 56, 14)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'izz'), pyxb.binding.datatypes.double, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 60, 14)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(None, 'ixx')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 40, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(None, 'ixy')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 44, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(None, 'ixz')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 48, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(None, 'iyy')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 52, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(None, 'iyz')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 56, 14))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(None, 'izz')), pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 60, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_47._Automaton = _BuildAutomaton_47()




CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parent'), pyxb.binding.datatypes.string, scope=CTD_ANON_48, documentation='\n              Name of the parent link\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 14, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'child'), pyxb.binding.datatypes.string, scope=CTD_ANON_48, documentation='\n              Name of the child link\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 23, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_48, documentation='\n              Pose offset from child link frame to joint frame (expressed in child link frame).\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 32, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gearbox_ratio'), pyxb.binding.datatypes.double, scope=CTD_ANON_48, documentation='\n              Parameter for gearbox joints.  Given theta_1 and theta_2 defined in description for gearbox_reference_body, theta_2 = -gearbox_ratio * theta_1.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 41, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gearbox_reference_body'), pyxb.binding.datatypes.string, scope=CTD_ANON_48, documentation='\n              Parameter for gearbox joints.  Gearbox ratio is enforced over two joint angles.  First joint angle (theta_1) is the angle from the gearbox_reference_body to the parent link in the direction of the axis element and the second joint angle (theta_2) is the angle from the gearbox_reference_body to the child link in the direction of the axis2 element.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 50, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'thread_pitch'), pyxb.binding.datatypes.double, scope=CTD_ANON_48, documentation='\n              Parameter for screw joints.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 59, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'axis'), CTD_ANON_49, scope=CTD_ANON_48, documentation='\n              \n      Parameters related to the axis of rotation for revolute joints,\n      the axis of translation for prismatic joints.\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 68, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'axis2'), CTD_ANON_52, scope=CTD_ANON_48, documentation='\n              \n      Parameters related to the second axis of rotation for revolute2 joints and universal joints.\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 226, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'physics'), CTD_ANON_55, scope=CTD_ANON_48, documentation='\n              Parameters that are specific to a certain physics engine.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 378, 8)))

CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sensor'), CTD_ANON_82, scope=CTD_ANON_48, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 23, 2)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 31, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 40, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 49, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 58, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 67, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 225, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 377, 8))
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'parent')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 14, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'child')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 23, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 32, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'gearbox_ratio')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 41, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'gearbox_reference_body')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 50, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'thread_pitch')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 59, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'axis')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 68, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'axis2')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 226, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(None, 'physics')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 378, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sensor')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 567, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_48._Automaton = _BuildAutomaton_48()




CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xyz'), vector3, scope=CTD_ANON_49, documentation='\n                    \n        Represents the x,y,z components of the axis unit vector. The axis is\n        expressed in the joint frame unless the use_parent_model_frame\n        flag is set to true. The vector should be normalized.\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 80, 14)))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'use_parent_model_frame'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_49, documentation='\n                    \n        Flag to interpret the axis xyz element in the parent model frame instead\n        of joint frame. Provided for Gazebo compatibility\n        (see https://bitbucket.org/osrf/gazebo/issue/494 ).\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 93, 14)))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dynamics'), CTD_ANON_50, scope=CTD_ANON_49, documentation='\n                    An element specifying physical properties of the joint. These values are used to specify modeling properties of the joint, particularly useful for simulation.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 106, 14)))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'limit'), CTD_ANON_51, scope=CTD_ANON_49, documentation='\n                    specifies the limits of this joint\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 155, 14)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 105, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(None, 'xyz')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 80, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(None, 'use_parent_model_frame')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 93, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(None, 'dynamics')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 106, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(None, 'limit')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 155, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_49._Automaton = _BuildAutomaton_49()




CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'damping'), pyxb.binding.datatypes.double, scope=CTD_ANON_50, documentation='\n                          The physical velocity dependent viscous damping coefficient of the joint.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 115, 20)))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'friction'), pyxb.binding.datatypes.double, scope=CTD_ANON_50, documentation='\n                          The physical static friction value of the joint.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 124, 20)))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'spring_reference'), pyxb.binding.datatypes.double, scope=CTD_ANON_50, documentation='\n                          The spring reference position for this joint axis.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 133, 20)))

CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'spring_stiffness'), pyxb.binding.datatypes.double, scope=CTD_ANON_50, documentation='\n                          The spring stiffness for this joint axis.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 142, 20)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 114, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 123, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(None, 'damping')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 115, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(None, 'friction')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 124, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(None, 'spring_reference')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 133, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(None, 'spring_stiffness')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 142, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_50._Automaton = _BuildAutomaton_50()




CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lower'), pyxb.binding.datatypes.double, scope=CTD_ANON_51, documentation='\n                          An attribute specifying the lower joint limit (radians for revolute joints, meters for prismatic joints). Omit if joint is continuous.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 164, 20)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'upper'), pyxb.binding.datatypes.double, scope=CTD_ANON_51, documentation='\n                          An attribute specifying the upper joint limit (radians for revolute joints, meters for prismatic joints). Omit if joint is continuous.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 173, 20)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'effort'), pyxb.binding.datatypes.double, scope=CTD_ANON_51, documentation='\n                          An attribute for enforcing the maximum joint effort applied by Joint::SetForce.  Limit is not enforced if value is negative.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 182, 20)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'velocity'), pyxb.binding.datatypes.double, scope=CTD_ANON_51, documentation='\n                          (not implemented) An attribute for enforcing the maximum joint velocity.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 191, 20)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stiffness'), pyxb.binding.datatypes.double, scope=CTD_ANON_51, documentation='\n                          Joint stop stiffness. Support physics engines: SimBody.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 200, 20)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dissipation'), pyxb.binding.datatypes.double, scope=CTD_ANON_51, documentation='\n                          Joint stop dissipation.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 209, 20)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 181, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 190, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 199, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 208, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(None, 'lower')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 164, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(None, 'upper')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 173, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(None, 'effort')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 182, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(None, 'velocity')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 191, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(None, 'stiffness')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 200, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(None, 'dissipation')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 209, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_51._Automaton = _BuildAutomaton_51()




CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xyz'), vector3, scope=CTD_ANON_52, documentation='\n                    \n        Represents the x,y,z components of the axis unit vector. The axis is\n        expressed in the joint frame unless the use_parent_model_frame\n        flag is set to true. The vector should be normalized.\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 237, 14)))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'use_parent_model_frame'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_52, documentation='\n                    \n        Flag to interpret the axis xyz element in the parent model frame instead\n        of joint frame. Provided for Gazebo compatibility\n        (see https://bitbucket.org/osrf/gazebo/issue/494 ).\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 250, 14)))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dynamics'), CTD_ANON_53, scope=CTD_ANON_52, documentation='\n                    An element specifying physical properties of the joint. These values are used to specify modeling properties of the joint, particularly useful for simulation.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 263, 14)))

CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'limit'), CTD_ANON_54, scope=CTD_ANON_52, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 312, 14)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 262, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 311, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(None, 'xyz')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 237, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(None, 'use_parent_model_frame')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 250, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(None, 'dynamics')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 263, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(None, 'limit')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 312, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_52._Automaton = _BuildAutomaton_52()




CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'damping'), pyxb.binding.datatypes.double, scope=CTD_ANON_53, documentation='\n                          The physical velocity dependent viscous damping coefficient of the joint.  EXPERIMENTAL: if damping coefficient is negative and implicit_spring_damper is true, adaptive damping is used.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 272, 20)))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'friction'), pyxb.binding.datatypes.double, scope=CTD_ANON_53, documentation='\n                          The physical static friction value of the joint.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 281, 20)))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'spring_reference'), pyxb.binding.datatypes.double, scope=CTD_ANON_53, documentation='\n                          The spring reference position for this joint axis.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 290, 20)))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'spring_stiffness'), pyxb.binding.datatypes.double, scope=CTD_ANON_53, documentation='\n                          The spring stiffness for this joint axis.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 299, 20)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 271, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 280, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(None, 'damping')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 272, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(None, 'friction')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 281, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(None, 'spring_reference')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 290, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(None, 'spring_stiffness')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 299, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_53._Automaton = _BuildAutomaton_53()




CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lower'), pyxb.binding.datatypes.double, scope=CTD_ANON_54, documentation='\n                          An attribute specifying the lower joint limit (radians for revolute joints, meters for prismatic joints). Omit if joint is continuous.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 316, 20)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'upper'), pyxb.binding.datatypes.double, scope=CTD_ANON_54, documentation='\n                          An attribute specifying the upper joint limit (radians for revolute joints, meters for prismatic joints). Omit if joint is continuous.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 325, 20)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'effort'), pyxb.binding.datatypes.double, scope=CTD_ANON_54, documentation='\n                          An attribute for enforcing the maximum joint effort applied by Joint::SetForce.  Limit is not enforced if value is negative.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 334, 20)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'velocity'), pyxb.binding.datatypes.double, scope=CTD_ANON_54, documentation='\n                          (not implemented) An attribute for enforcing the maximum joint velocity.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 343, 20)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stiffness'), pyxb.binding.datatypes.double, scope=CTD_ANON_54, documentation='\n                          Joint stop stiffness. Supported physics engines: SimBody.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 352, 20)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dissipation'), pyxb.binding.datatypes.double, scope=CTD_ANON_54, documentation='\n                          Joint stop dissipation. Supported physics engines: SimBody.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 361, 20)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 315, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 324, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 333, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 342, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 351, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 360, 20))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(None, 'lower')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 316, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(None, 'upper')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 325, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(None, 'effort')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 334, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(None, 'velocity')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 343, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(None, 'stiffness')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 352, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(None, 'dissipation')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 361, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_54._Automaton = _BuildAutomaton_54()




CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'simbody'), CTD_ANON_56, scope=CTD_ANON_55, documentation='\n                    Simbody specific parameters\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 387, 14)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ode'), CTD_ANON_57, scope=CTD_ANON_55, documentation='\n                    ODE specific parameters\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 409, 14)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'provide_feedback'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_55, documentation='\n                    If provide feedback is set to true, physics engine will compute the constraint forces at this joint.  For now, provide_feedback under ode block will override this tag and given user warning about the migration.  provide_feedback under ode is scheduled to be removed in SDF 1.5.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 555, 14)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 386, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 408, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 554, 14))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(None, 'simbody')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 387, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(None, 'ode')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 409, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(None, 'provide_feedback')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 555, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_55._Automaton = _BuildAutomaton_55()




CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'must_be_loop_joint'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_56, documentation='\n                          Force cut in the multibody graph at this joint.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 396, 20)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 395, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(None, 'must_be_loop_joint')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 396, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_56._Automaton = _BuildAutomaton_56()




CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'provide_feedback'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_57, documentation='\n                          (DEPRECATION WARNING:  In SDF 1.5 this tag will be replaced by the same tag directly under the physics-block.  For now, this tag overrides the one outside of ode-block, but in SDF 1.5 this tag will be removed completely.)  If provide feedback is set to true, ODE will compute the constraint forces at this joint.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 418, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cfm_damping'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_57, documentation='\n                          If cfm damping is set to true, ODE will use CFM to simulate damping, allows for infinite damping, and one additional constraint row (previously used for joint limit) is always active.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 427, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'implicit_spring_damper'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_57, documentation='\n                          If implicit_spring_damper is set to true, ODE will use CFM, ERP to simulate stiffness and damping, allows for infinite damping, and one additional constraint row (previously used for joint limit) is always active.  This replaces cfm_damping parameter in sdf 1.4.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 436, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fudge_factor'), pyxb.binding.datatypes.double, scope=CTD_ANON_57, documentation='\n                          Scale the excess for in a joint motor at joint limits. Should be between zero and one.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 445, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cfm'), pyxb.binding.datatypes.double, scope=CTD_ANON_57, documentation='\n                          Constraint force mixing for constrained directions\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 454, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'erp'), pyxb.binding.datatypes.double, scope=CTD_ANON_57, documentation='\n                          Error reduction parameter for constrained directions\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 463, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bounce'), pyxb.binding.datatypes.double, scope=CTD_ANON_57, documentation='\n                          Bounciness of the limits\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 472, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_force'), pyxb.binding.datatypes.double, scope=CTD_ANON_57, documentation='\n                          Maximum force or torque used to reach the desired velocity.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 481, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'velocity'), pyxb.binding.datatypes.double, scope=CTD_ANON_57, documentation='\n                          The desired velocity of the joint. Should only be set if you want the joint to move on load.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 490, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'limit'), CTD_ANON_58, scope=CTD_ANON_57, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 499, 20)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'suspension'), CTD_ANON_59, scope=CTD_ANON_57, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 525, 20)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 417, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 426, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 435, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 444, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 453, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 462, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 471, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 480, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 489, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 498, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 524, 20))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'provide_feedback')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 418, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'cfm_damping')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 427, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'implicit_spring_damper')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 436, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'fudge_factor')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 445, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'cfm')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 454, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'erp')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 463, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'bounce')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 472, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'max_force')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 481, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'velocity')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 490, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'limit')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 499, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(None, 'suspension')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 525, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_57._Automaton = _BuildAutomaton_57()




CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cfm'), pyxb.binding.datatypes.double, scope=CTD_ANON_58, documentation='\n                                Constraint force mixing parameter used by the joint stop\n                              ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 503, 26)))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'erp'), pyxb.binding.datatypes.double, scope=CTD_ANON_58, documentation='\n                                Error reduction parameter used by the joint stop\n                              ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 512, 26)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(None, 'cfm')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 503, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(None, 'erp')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 512, 26))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_58._Automaton = _BuildAutomaton_58()




CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cfm'), pyxb.binding.datatypes.double, scope=CTD_ANON_59, documentation='\n                                Suspension constraint force mixing parameter\n                              ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 529, 26)))

CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'erp'), pyxb.binding.datatypes.double, scope=CTD_ANON_59, documentation='\n                                Suspension error reduction parameter\n                              ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 538, 26)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(None, 'cfm')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 529, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(None, 'erp')), pyxb.utils.utility.Location('http://sdformat.org/schemas/joint.xsd', 538, 26))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_59._Automaton = _BuildAutomaton_59()




CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audio_sink'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_sink.xsd', 9, 2)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'audio_source'), CTD_ANON_5, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/audio_source.xsd', 9, 2)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'collision'), CTD_ANON_15, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/collision.xsd', 11, 2)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inertial'), CTD_ANON_46, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/inertial.xsd', 9, 2)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gravity'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_60, documentation='\n              If true, the link is affected by gravity.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 20, 8)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'self_collide'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_60, documentation='\n              If true, the link can collide with other links in the model. Two links within a model will collide if link1.self_collide OR link2.self_collide. Links connected by a joint will never collide.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 29, 8)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'kinematic'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_60, documentation='\n              If true, the link is kinematic only\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 38, 8)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_60, documentation='\n              This is the pose of the link reference frame, relative to the model reference frame.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 47, 8)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'must_be_base_link'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_60, documentation='\n              If true, the link will have 6DOF and be a direct child of world.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 56, 8)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'velocity_decay'), CTD_ANON_61, scope=CTD_ANON_60, documentation="\n              Exponential damping of the link's velocity.\n            ", location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 65, 8)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'projector'), CTD_ANON_75, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 5, 2)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sensor'), CTD_ANON_82, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 23, 2)))

CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'visual'), CTD_ANON_96, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 12, 2)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 19, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 28, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 37, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 46, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 55, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 64, 8))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(None, 'gravity')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 20, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(None, 'self_collide')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 29, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(None, 'kinematic')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 38, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 47, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(None, 'must_be_base_link')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 56, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(None, 'velocity_decay')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 65, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inertial')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 95, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'collision')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 96, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'visual')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 97, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sensor')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 98, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'projector')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 99, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audio_sink')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 100, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'audio_source')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 101, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_60._Automaton = _BuildAutomaton_60()




CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'linear'), pyxb.binding.datatypes.double, scope=CTD_ANON_61, documentation='\n                    Linear damping\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 74, 14)))

CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'angular'), pyxb.binding.datatypes.double, scope=CTD_ANON_61, documentation='\n                    Angular damping\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 83, 14)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 73, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 82, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(None, 'linear')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 74, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(None, 'angular')), pyxb.utils.utility.Location('http://sdformat.org/schemas/link.xsd', 83, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_61._Automaton = _BuildAutomaton_61()




CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'near'), pyxb.binding.datatypes.double, scope=CTD_ANON_62, documentation='\n              Near clipping distance of the view frustum\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 13, 8)))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'far'), pyxb.binding.datatypes.double, scope=CTD_ANON_62, documentation='\n              Far clipping distance of the view frustum\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 22, 8)))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'aspect_ratio'), pyxb.binding.datatypes.double, scope=CTD_ANON_62, documentation='\n              Aspect ratio of the near and far planes. This is the width divided by the height of the near or far planes.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 31, 8)))

CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'horizontal_fov'), pyxb.binding.datatypes.double, scope=CTD_ANON_62, documentation="\n              Horizontal field of view of the frustum, in radians. This is the angle between the frustum's vertex and the edges of the near or far plane.\n            ", location=pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 40, 8)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(None, 'near')), pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(None, 'far')), pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(None, 'aspect_ratio')), pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 31, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(None, 'horizontal_fov')), pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 40, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_62._Automaton = _BuildAutomaton_62()




CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'x'), CTD_ANON_64, scope=CTD_ANON_63, documentation='\n              \n      Parameters related to the body-frame X axis of the magnetometer\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 13, 8)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'y'), CTD_ANON_65, scope=CTD_ANON_63, documentation='\n              \n      Parameters related to the body-frame Y axis of the magnetometer\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 28, 8)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'z'), CTD_ANON_66, scope=CTD_ANON_63, documentation='\n              \n      Parameters related to the body-frame Z axis of the magnetometer\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 43, 8)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 27, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 42, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(None, 'x')), pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(None, 'y')), pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 28, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(None, 'z')), pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 43, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_63._Automaton = _BuildAutomaton_63()




def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_64._Automaton = _BuildAutomaton_64()




def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_65._Automaton = _BuildAutomaton_65()




def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_66._Automaton = _BuildAutomaton_66()




CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'script'), CTD_ANON_68, scope=CTD_ANON_67, documentation='\n              Name of material from an installed script file. This will override the color element if the script exists.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 13, 8)))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shader'), CTD_ANON_69, scope=CTD_ANON_67, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 44, 8)))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lighting'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_67, documentation='\n              If false, dynamic lighting will be disabled\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 68, 8)))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ambient'), color, scope=CTD_ANON_67, documentation='\n              The ambient color of a material specified by set of four numbers representing red/green/blue, each in the range of [0,1].\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 77, 8)))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'diffuse'), color, scope=CTD_ANON_67, documentation='\n              The diffuse color of a material specified by set of four numbers representing red/green/blue/alpha, each in the range of [0,1].\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 86, 8)))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'specular'), color, scope=CTD_ANON_67, documentation='\n              The specular color of a material specified by set of four numbers representing red/green/blue/alpha, each in the range of [0,1].\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 95, 8)))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emissive'), color, scope=CTD_ANON_67, documentation='\n              The emissive color of a material specified by set of four numbers representing red/green/blue, each in the range of [0,1].\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 104, 8)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 43, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 67, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 76, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 85, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 94, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 103, 8))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(None, 'script')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(None, 'shader')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 44, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(None, 'lighting')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 68, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(None, 'ambient')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 77, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(None, 'diffuse')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 86, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(None, 'specular')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 95, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(None, 'emissive')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 104, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_67._Automaton = _BuildAutomaton_67()




CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uri'), pyxb.binding.datatypes.string, scope=CTD_ANON_68, documentation='\n                    URI of the material script file\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 22, 14)))

CTD_ANON_68._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_68, documentation='\n                    Name of the script within the script file\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 31, 14)))

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(None, 'uri')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 22, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_68._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 31, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_68._Automaton = _BuildAutomaton_68()




CTD_ANON_69._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'normal_map'), pyxb.binding.datatypes.string, scope=CTD_ANON_69, documentation='\n                    filename of the normal map\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 48, 14)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 47, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_69._UseForTag(pyxb.namespace.ExpandedName(None, 'normal_map')), pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 48, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_69._Automaton = _BuildAutomaton_69()




CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'uri'), pyxb.binding.datatypes.string, scope=CTD_ANON_70, documentation='\n              Mesh uri\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 13, 8)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'submesh'), CTD_ANON_71, scope=CTD_ANON_70, documentation='\n              Use a named submesh. The submesh must exist in the mesh specified by the uri\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 22, 8)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'scale'), vector3, scope=CTD_ANON_70, documentation='\n              Scaling factor applied to the mesh\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 53, 8)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 21, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 52, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(None, 'uri')), pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(None, 'submesh')), pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(None, 'scale')), pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 53, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_70._Automaton = _BuildAutomaton_70()




CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_71, documentation='\n                    Name of the submesh within the parent mesh\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 31, 14)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'center'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_71, documentation='\n                    Set to true to center the vertices of the submesh at 0,0,0. This will effectively remove any transformations on the submesh before the poses from parent links and models are applied.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 40, 14)))

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 39, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 31, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(None, 'center')), pyxb.utils.utility.Location('http://sdformat.org/schemas/mesh_shape.xsd', 40, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_71._Automaton = _BuildAutomaton_71()




CTD_ANON_72._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'normal'), vector3, scope=CTD_ANON_72, documentation='\n              Normal direction for the plane\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 13, 8)))

CTD_ANON_72._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'size'), vector2d, scope=CTD_ANON_72, documentation='\n              Length of each side of the plane\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 22, 8)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(None, 'normal')), pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(None, 'size')), pyxb.utils.utility.Location('http://sdformat.org/schemas/plane_shape.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_72._Automaton = _BuildAutomaton_72()




def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 12, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 12, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_73._Automaton = _BuildAutomaton_73()




CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), vector2d, scope=CTD_ANON_74, documentation='\n              \n      A series of points that define the path of the polyline.\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 13, 8)))

CTD_ANON_74._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), pyxb.binding.datatypes.double, scope=CTD_ANON_74, documentation='\n              Height of the polyline\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 24, 8)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('http://sdformat.org/schemas/polyline_shape.xsd', 24, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_74._Automaton = _BuildAutomaton_74()




CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plugin'), CTD_ANON_73, scope=CTD_ANON_75, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2)))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'texture'), pyxb.binding.datatypes.string, scope=CTD_ANON_75, documentation='\n              Texture name\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 9, 8)))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_75, documentation='\n              Pose of the projector\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 18, 8)))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fov'), pyxb.binding.datatypes.double, scope=CTD_ANON_75, documentation='\n              Field of view\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 27, 8)))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'near_clip'), pyxb.binding.datatypes.double, scope=CTD_ANON_75, documentation='\n              Near clip distance\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 36, 8)))

CTD_ANON_75._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'far_clip'), pyxb.binding.datatypes.double, scope=CTD_ANON_75, documentation='\n              far clip distance\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 45, 8)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 17, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 26, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 35, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 44, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(None, 'texture')), pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 9, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 18, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(None, 'fov')), pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 27, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(None, 'near_clip')), pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 36, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(None, 'far_clip')), pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 45, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'plugin')), pyxb.utils.utility.Location('http://sdformat.org/schemas/projector.xsd', 53, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_75._Automaton = _BuildAutomaton_75()




CTD_ANON_76._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'scan'), CTD_ANON_77, scope=CTD_ANON_76, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 13, 8)))

CTD_ANON_76._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'range'), CTD_ANON_80, scope=CTD_ANON_76, documentation='\n              specifies range properties of each simulated ray\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 99, 8)))

CTD_ANON_76._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'noise'), CTD_ANON_81, scope=CTD_ANON_76, documentation='\n              The properties of the noise model that should be applied to generated scans\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 139, 8)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 138, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(None, 'scan')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(None, 'range')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 99, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(None, 'noise')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 139, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_76._Automaton = _BuildAutomaton_76()




CTD_ANON_77._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'horizontal'), CTD_ANON_78, scope=CTD_ANON_77, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 17, 14)))

CTD_ANON_77._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vertical'), CTD_ANON_79, scope=CTD_ANON_77, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 56, 14)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 55, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(None, 'horizontal')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 17, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(None, 'vertical')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 56, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_77._Automaton = _BuildAutomaton_77()




CTD_ANON_78._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samples'), pyxb.binding.datatypes.unsignedInt, scope=CTD_ANON_78, documentation='\n                          The number of simulated rays to generate per complete laser sweep cycle.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 21, 20)))

CTD_ANON_78._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'resolution'), pyxb.binding.datatypes.double, scope=CTD_ANON_78, documentation='\n                          This number is multiplied by samples to determine the number of range data points returned. If resolution is less than one, range data is interpolated. If resolution is greater than one, range data is averaged.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 30, 20)))

CTD_ANON_78._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_angle'), pyxb.binding.datatypes.double, scope=CTD_ANON_78, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 39, 20)))

CTD_ANON_78._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_angle'), pyxb.binding.datatypes.double, scope=CTD_ANON_78, documentation='\n                          Must be greater or equal to min_angle\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 43, 20)))

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(None, 'samples')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 21, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(None, 'resolution')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 30, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(None, 'min_angle')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 39, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(None, 'max_angle')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 43, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_78._Automaton = _BuildAutomaton_78()




CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'samples'), pyxb.binding.datatypes.unsignedInt, scope=CTD_ANON_79, documentation='\n                          The number of simulated rays to generate per complete laser sweep cycle.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 60, 20)))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'resolution'), pyxb.binding.datatypes.double, scope=CTD_ANON_79, documentation='\n                          This number is multiplied by samples to determine the number of range data points returned. If resolution is less than one, range data is interpolated. If resolution is greater than one, range data is averaged.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 69, 20)))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_angle'), pyxb.binding.datatypes.double, scope=CTD_ANON_79, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 78, 20)))

CTD_ANON_79._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_angle'), pyxb.binding.datatypes.double, scope=CTD_ANON_79, documentation='\n                          Must be greater or equal to min_angle\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 82, 20)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 68, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(None, 'samples')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 60, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(None, 'resolution')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 69, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(None, 'min_angle')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 78, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(None, 'max_angle')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 82, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_79._Automaton = _BuildAutomaton_79()




CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min'), pyxb.binding.datatypes.double, scope=CTD_ANON_80, documentation='\n                    The minimum distance for each ray.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 108, 14)))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max'), pyxb.binding.datatypes.double, scope=CTD_ANON_80, documentation='\n                    The maximum distance for each ray.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 117, 14)))

CTD_ANON_80._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'resolution'), pyxb.binding.datatypes.double, scope=CTD_ANON_80, documentation='\n                    Linear resolution of each ray.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 126, 14)))

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 125, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(None, 'min')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 108, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(None, 'max')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 117, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(None, 'resolution')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 126, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_80._Automaton = _BuildAutomaton_80()




CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=CTD_ANON_81, documentation='\n                    The type of noise.  Currently supported types are: "gaussian" (draw noise values independently for each beam from a Gaussian distribution).\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 148, 14)))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mean'), pyxb.binding.datatypes.double, scope=CTD_ANON_81, documentation='\n                    For type "gaussian," the mean of the Gaussian distribution from which noise values are drawn.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 157, 14)))

CTD_ANON_81._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stddev'), pyxb.binding.datatypes.double, scope=CTD_ANON_81, documentation='\n                    For type "gaussian," the standard deviation of the Gaussian distribution from which noise values are drawn.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 166, 14)))

def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 156, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 165, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 148, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(None, 'mean')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 157, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(None, 'stddev')), pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 166, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_81._Automaton = _BuildAutomaton_81()




CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'altimeter'), CTD_ANON_2, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/altimeter.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'camera'), CTD_ANON_8, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/camera.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contact'), CTD_ANON_16, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/contact.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'force_torque'), CTD_ANON_18, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/forcetorque.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gps'), CTD_ANON_21, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/gps.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'imu'), CTD_ANON_34, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/imu.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'logical_camera'), CTD_ANON_62, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/logical_camera.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'magnetometer'), CTD_ANON_63, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/magnetometer.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plugin'), CTD_ANON_73, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ray'), CTD_ANON_76, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/ray.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rfidtag'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/rfid.xsd', 4, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rfid'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/rfidtag.xsd', 4, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'always_on'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_82, documentation='\n              If true the sensor will always be updated according to the update rate.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 27, 8)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'update_rate'), pyxb.binding.datatypes.double, scope=CTD_ANON_82, documentation='\n              The frequency at which the sensor data is generated. If left unspecified, the sensor will generate data every cycle.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 36, 8)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visualize'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_82, documentation='\n              If true, the sensor is visualized in the GUI\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 45, 8)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_82, documentation='\n              This is the pose of the sensor, relative to the parent (link or joint) reference frame.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 54, 8)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'topic'), pyxb.binding.datatypes.string, scope=CTD_ANON_82, documentation='\n              Name of the topic on which data is published. This is necessary for visualization\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 63, 8)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sonar'), CTD_ANON_83, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 9, 2)))

CTD_ANON_82._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transceiver'), CTD_ANON_95, scope=CTD_ANON_82, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 9, 2)))

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 26, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 35, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 44, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 53, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 62, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(None, 'always_on')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 27, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(None, 'update_rate')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 36, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(None, 'visualize')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 45, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 54, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(None, 'topic')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 63, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'plugin')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 71, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'altimeter')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 72, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'camera')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 73, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contact')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 74, 8))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'gps')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 75, 8))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'imu')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 76, 8))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'logical_camera')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 77, 8))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'magnetometer')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 78, 8))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ray')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 79, 8))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rfidtag')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 80, 8))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rfid')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 81, 8))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sonar')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 82, 8))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transceiver')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 83, 8))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'force_torque')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sensor.xsd', 84, 8))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_82._Automaton = _BuildAutomaton_82()




CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min'), pyxb.binding.datatypes.double, scope=CTD_ANON_83, documentation='\n              Minimum range\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 13, 8)))

CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max'), pyxb.binding.datatypes.double, scope=CTD_ANON_83, documentation='\n              Max range\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 22, 8)))

CTD_ANON_83._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), pyxb.binding.datatypes.double, scope=CTD_ANON_83, documentation='\n              Radius of the sonar cone at max range.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 31, 8)))

def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(None, 'min')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(None, 'max')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sonar.xsd', 31, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_83._Automaton = _BuildAutomaton_83()




CTD_ANON_84._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), pyxb.binding.datatypes.double, scope=CTD_ANON_84, documentation='\n              radius of the sphere\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/sphere_shape.xsd', 13, 8)))

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_84._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('http://sdformat.org/schemas/sphere_shape.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_84._Automaton = _BuildAutomaton_84()




CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bounce'), CTD_ANON_86, scope=CTD_ANON_85, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 13, 8)))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'friction'), CTD_ANON_87, scope=CTD_ANON_85, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 39, 8)))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact'), CTD_ANON_90, scope=CTD_ANON_85, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 149, 8)))

CTD_ANON_85._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'soft_contact'), CTD_ANON_93, scope=CTD_ANON_85, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 318, 8)))

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 38, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 148, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 317, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(None, 'bounce')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(None, 'friction')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 39, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(None, 'contact')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 149, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_85._UseForTag(pyxb.namespace.ExpandedName(None, 'soft_contact')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 318, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_85._Automaton = _BuildAutomaton_85()




CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'restitution_coefficient'), pyxb.binding.datatypes.double, scope=CTD_ANON_86, documentation='\n                    Bounciness coefficient of restitution, from [0...1], where 0=no bounciness.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 17, 14)))

CTD_ANON_86._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'threshold'), pyxb.binding.datatypes.double, scope=CTD_ANON_86, documentation='\n                    Bounce capture velocity, below which effective coefficient of restitution is 0.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 26, 14)))

def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 16, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 25, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(None, 'restitution_coefficient')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 17, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_86._UseForTag(pyxb.namespace.ExpandedName(None, 'threshold')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 26, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_86._Automaton = _BuildAutomaton_86()




CTD_ANON_87._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ode'), CTD_ANON_88, scope=CTD_ANON_87, documentation='\n                    ODE friction parameters\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 43, 14)))

CTD_ANON_87._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bullet'), CTD_ANON_89, scope=CTD_ANON_87, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 101, 14)))

def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 42, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 100, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_87._UseForTag(pyxb.namespace.ExpandedName(None, 'ode')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 43, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_87._UseForTag(pyxb.namespace.ExpandedName(None, 'bullet')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 101, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_87._Automaton = _BuildAutomaton_87()




CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mu'), pyxb.binding.datatypes.double, scope=CTD_ANON_88, documentation='\n                          Coefficient of friction in the range of [0..1].\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 52, 20)))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mu2'), pyxb.binding.datatypes.double, scope=CTD_ANON_88, documentation='\n                          Second coefficient of friction in the range of [0..1]\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 61, 20)))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fdir1'), vector3, scope=CTD_ANON_88, documentation='\n                          3-tuple specifying direction of mu1 in the collision local reference frame.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 70, 20)))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'slip1'), pyxb.binding.datatypes.double, scope=CTD_ANON_88, documentation='\n                          Force dependent slip direction 1 in collision local frame, between the range of [0..1].\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 79, 20)))

CTD_ANON_88._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'slip2'), pyxb.binding.datatypes.double, scope=CTD_ANON_88, documentation='\n                          Force dependent slip direction 2 in collision local frame, between the range of [0..1].\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 88, 20)))

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 51, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 60, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 69, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 78, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 87, 20))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(None, 'mu')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 52, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(None, 'mu2')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 61, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(None, 'fdir1')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 70, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(None, 'slip1')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 79, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_88._UseForTag(pyxb.namespace.ExpandedName(None, 'slip2')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 88, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_88._Automaton = _BuildAutomaton_88()




CTD_ANON_89._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'friction'), pyxb.binding.datatypes.double, scope=CTD_ANON_89, documentation='\n                          Coefficient of friction in the range of [0..1].\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 105, 20)))

CTD_ANON_89._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'friction2'), pyxb.binding.datatypes.double, scope=CTD_ANON_89, documentation='\n                          Coefficient of friction in the range of [0..1].\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 114, 20)))

CTD_ANON_89._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fdir1'), vector3, scope=CTD_ANON_89, documentation='\n                          3-tuple specifying direction of mu1 in the collision local reference frame.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 123, 20)))

CTD_ANON_89._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rolling_friction'), pyxb.binding.datatypes.double, scope=CTD_ANON_89, documentation='\n                           coefficient of friction in the range of [0..1]\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 132, 20)))

def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 104, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 113, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 122, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 131, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_89._UseForTag(pyxb.namespace.ExpandedName(None, 'friction')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 105, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_89._UseForTag(pyxb.namespace.ExpandedName(None, 'friction2')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 114, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_89._UseForTag(pyxb.namespace.ExpandedName(None, 'fdir1')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 123, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_89._UseForTag(pyxb.namespace.ExpandedName(None, 'rolling_friction')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 132, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_89._Automaton = _BuildAutomaton_89()




CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collide_without_contact'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_90, documentation='\n                    Flag to disable contact force generation, while still allowing collision checks and contact visualization to occur.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 153, 14)))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collide_without_contact_bitmask'), pyxb.binding.datatypes.unsignedInt, scope=CTD_ANON_90, documentation='\n                    Bitmask for collision filtering when collide_without_contact is on \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 162, 14)))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collide_bitmask'), pyxb.binding.datatypes.unsignedInt, scope=CTD_ANON_90, documentation='\n                    Bitmask for collision filtering. This will override collide_without_contact\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 171, 14)))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ode'), CTD_ANON_91, scope=CTD_ANON_90, documentation='\n                    ODE contact parameters\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 180, 14)))

CTD_ANON_90._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bullet'), CTD_ANON_92, scope=CTD_ANON_90, documentation='\n                    Bullet contact parameters\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 247, 14)))

def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 152, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 161, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 170, 14))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 179, 14))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 246, 14))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(None, 'collide_without_contact')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 153, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(None, 'collide_without_contact_bitmask')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 162, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(None, 'collide_bitmask')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 171, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(None, 'ode')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 180, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_90._UseForTag(pyxb.namespace.ExpandedName(None, 'bullet')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 247, 14))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_90._Automaton = _BuildAutomaton_90()




CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'soft_cfm'), pyxb.binding.datatypes.double, scope=CTD_ANON_91, documentation='\n                          Soft constraint force mixing.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 189, 20)))

CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'soft_erp'), pyxb.binding.datatypes.double, scope=CTD_ANON_91, documentation='\n                          Soft error reduction parameter\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 198, 20)))

CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'kp'), pyxb.binding.datatypes.double, scope=CTD_ANON_91, documentation='\n                          dynamically "stiffness"-equivalent coefficient for contact joints\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 207, 20)))

CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'kd'), pyxb.binding.datatypes.double, scope=CTD_ANON_91, documentation='\n                          dynamically "damping"-equivalent coefficient for contact joints\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 216, 20)))

CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_vel'), pyxb.binding.datatypes.double, scope=CTD_ANON_91, documentation='\n                          maximum contact correction velocity truncation term.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 225, 20)))

CTD_ANON_91._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_depth'), pyxb.binding.datatypes.double, scope=CTD_ANON_91, documentation='\n                          minimum allowable depth before contact correction impulse is applied\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 234, 20)))

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 188, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 197, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 206, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 215, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 224, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 233, 20))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(None, 'soft_cfm')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 189, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(None, 'soft_erp')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 198, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(None, 'kp')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 207, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(None, 'kd')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 216, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(None, 'max_vel')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 225, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_91._UseForTag(pyxb.namespace.ExpandedName(None, 'min_depth')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 234, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_91._Automaton = _BuildAutomaton_91()




CTD_ANON_92._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'soft_cfm'), pyxb.binding.datatypes.double, scope=CTD_ANON_92, documentation='\n                          Soft constraint force mixing.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 256, 20)))

CTD_ANON_92._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'soft_erp'), pyxb.binding.datatypes.double, scope=CTD_ANON_92, documentation='\n                          Soft error reduction parameter\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 265, 20)))

CTD_ANON_92._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'kp'), pyxb.binding.datatypes.double, scope=CTD_ANON_92, documentation='\n                          dynamically "stiffness"-equivalent coefficient for contact joints\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 274, 20)))

CTD_ANON_92._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'kd'), pyxb.binding.datatypes.double, scope=CTD_ANON_92, documentation='\n                          dynamically "damping"-equivalent coefficient for contact joints\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 283, 20)))

CTD_ANON_92._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'split_impulse'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_92, documentation="\n                          Similar to ODE's max_vel implementation.  See http://bulletphysics.org/mediawiki-1.5.8/index.php/BtContactSolverInfo#Split_Impulse for more information.\n                        ", location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 292, 20)))

CTD_ANON_92._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'split_impulse_penetration_threshold'), pyxb.binding.datatypes.double, scope=CTD_ANON_92, documentation="\n                          Similar to ODE's max_vel implementation.  See http://bulletphysics.org/mediawiki-1.5.8/index.php/BtContactSolverInfo#Split_Impulse for more information.\n                        ", location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 301, 20)))

def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 255, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 264, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 273, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 282, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_92._UseForTag(pyxb.namespace.ExpandedName(None, 'soft_cfm')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 256, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_92._UseForTag(pyxb.namespace.ExpandedName(None, 'soft_erp')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 265, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_92._UseForTag(pyxb.namespace.ExpandedName(None, 'kp')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 274, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_92._UseForTag(pyxb.namespace.ExpandedName(None, 'kd')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 283, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_92._UseForTag(pyxb.namespace.ExpandedName(None, 'split_impulse')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 292, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_92._UseForTag(pyxb.namespace.ExpandedName(None, 'split_impulse_penetration_threshold')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 301, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_92._Automaton = _BuildAutomaton_92()




CTD_ANON_93._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dart'), CTD_ANON_94, scope=CTD_ANON_93, documentation='\n                    soft contact pamameters based on paper:\n             http://www.cc.gatech.edu/graphics/projects/Sumit/homepage/papers/sigasia11/jain_softcontacts_siga11.pdf\n      \n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 322, 14)))

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 321, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_93._UseForTag(pyxb.namespace.ExpandedName(None, 'dart')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 322, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_93._Automaton = _BuildAutomaton_93()




CTD_ANON_94._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bone_attachment'), pyxb.binding.datatypes.double, scope=CTD_ANON_94, documentation='\n                          This is variable k_v in the soft contacts paper.  Its unit is N/m.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 333, 20)))

CTD_ANON_94._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stiffness'), pyxb.binding.datatypes.double, scope=CTD_ANON_94, documentation='\n                          This is variable k_e in the soft contacts paper.  Its unit is N/m.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 342, 20)))

CTD_ANON_94._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'damping'), pyxb.binding.datatypes.double, scope=CTD_ANON_94, documentation='\n                          Viscous damping of point velocity in body frame.  Its unit is N/m/s.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 351, 20)))

CTD_ANON_94._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flesh_mass_fraction'), pyxb.binding.datatypes.double, scope=CTD_ANON_94, documentation='\n                          Fraction of mass to be distributed among deformable nodes.\n                        ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 360, 20)))

def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_94._UseForTag(pyxb.namespace.ExpandedName(None, 'bone_attachment')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 333, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_94._UseForTag(pyxb.namespace.ExpandedName(None, 'stiffness')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 342, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_94._UseForTag(pyxb.namespace.ExpandedName(None, 'damping')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 351, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_94._UseForTag(pyxb.namespace.ExpandedName(None, 'flesh_mass_fraction')), pyxb.utils.utility.Location('http://sdformat.org/schemas/surface.xsd', 360, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_94._Automaton = _BuildAutomaton_94()




CTD_ANON_95._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'essid'), pyxb.binding.datatypes.string, scope=CTD_ANON_95, documentation='\n              Service set identifier (network name)\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 13, 8)))

CTD_ANON_95._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'frequency'), pyxb.binding.datatypes.double, scope=CTD_ANON_95, documentation='\n              Specifies the frequency of transmission in MHz\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 22, 8)))

CTD_ANON_95._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_frequency'), pyxb.binding.datatypes.double, scope=CTD_ANON_95, documentation='\n              Only a frequency range is filtered. Here we set the lower bound (MHz).\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 31, 8)))

CTD_ANON_95._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_frequency'), pyxb.binding.datatypes.double, scope=CTD_ANON_95, documentation='\n              Only a frequency range is filtered. Here we set the upper bound (MHz).\n    \n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 41, 8)))

CTD_ANON_95._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gain'), pyxb.binding.datatypes.double, scope=CTD_ANON_95, documentation='\n              Specifies the antenna gain in dBi\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 51, 8)))

CTD_ANON_95._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'power'), pyxb.binding.datatypes.double, scope=CTD_ANON_95, documentation='\n              Specifies the transmission power in dBm\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 60, 8)))

CTD_ANON_95._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sensitivity'), pyxb.binding.datatypes.double, scope=CTD_ANON_95, documentation='\n              Mininum received signal power in dBm\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 69, 8)))

def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 12, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 21, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 30, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 40, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 68, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_95._UseForTag(pyxb.namespace.ExpandedName(None, 'essid')), pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 13, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_95._UseForTag(pyxb.namespace.ExpandedName(None, 'frequency')), pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 22, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_95._UseForTag(pyxb.namespace.ExpandedName(None, 'min_frequency')), pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 31, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_95._UseForTag(pyxb.namespace.ExpandedName(None, 'max_frequency')), pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 41, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_95._UseForTag(pyxb.namespace.ExpandedName(None, 'gain')), pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 51, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_95._UseForTag(pyxb.namespace.ExpandedName(None, 'power')), pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 60, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_95._UseForTag(pyxb.namespace.ExpandedName(None, 'sensitivity')), pyxb.utils.utility.Location('http://sdformat.org/schemas/transceiver.xsd', 69, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_95._Automaton = _BuildAutomaton_95()




CTD_ANON_96._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'geometry'), CTD_ANON_19, scope=CTD_ANON_96, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/geometry.xsd', 17, 2)))

CTD_ANON_96._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'material'), CTD_ANON_67, scope=CTD_ANON_96, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/material.xsd', 9, 2)))

CTD_ANON_96._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plugin'), CTD_ANON_73, scope=CTD_ANON_96, location=pyxb.utils.utility.Location('http://sdformat.org/schemas/plugin.xsd', 9, 2)))

CTD_ANON_96._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cast_shadows'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_96, documentation='\n              If true the visual will cast shadows.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 16, 8)))

CTD_ANON_96._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'laser_retro'), pyxb.binding.datatypes.double, scope=CTD_ANON_96, documentation='\n              will be implemented in the future release.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 25, 8)))

CTD_ANON_96._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transparency'), pyxb.binding.datatypes.double, scope=CTD_ANON_96, documentation='\n              The amount of transparency( 0=opaque, 1 = fully transparent)\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 34, 8)))

CTD_ANON_96._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pose, scope=CTD_ANON_96, documentation='\n              The reference frame of the visual element, relative to the reference frame of the link.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 43, 8)))

CTD_ANON_96._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meta'), CTD_ANON_97, scope=CTD_ANON_96, documentation='\n              Optional meta information for the visual. The information contained within this element should be used to provide additional feedback to an end user.\n            ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 52, 8)))

def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 15, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 24, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 33, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 42, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 51, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_96._UseForTag(pyxb.namespace.ExpandedName(None, 'cast_shadows')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 16, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_96._UseForTag(pyxb.namespace.ExpandedName(None, 'laser_retro')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 25, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_96._UseForTag(pyxb.namespace.ExpandedName(None, 'transparency')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 34, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_96._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 43, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_96._UseForTag(pyxb.namespace.ExpandedName(None, 'meta')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 52, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_96._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'material')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 73, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_96._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'geometry')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 74, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_96._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'plugin')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 75, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_96._Automaton = _BuildAutomaton_96()




CTD_ANON_97._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'layer'), pyxb.binding.datatypes.int, scope=CTD_ANON_97, documentation='\n                    The layer in which this visual is displayed. The layer number is useful for programs, such as Gazebo, that put visuals in different layers for enhanced visualization.\n                  ', location=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 61, 14)))

def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 60, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_97._UseForTag(pyxb.namespace.ExpandedName(None, 'layer')), pyxb.utils.utility.Location('http://sdformat.org/schemas/visual.xsd', 61, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_97._Automaton = _BuildAutomaton_97()

