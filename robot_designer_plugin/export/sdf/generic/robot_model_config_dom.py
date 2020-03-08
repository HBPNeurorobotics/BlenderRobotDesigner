# C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/export/sdf/generic\robot_model_config_dom_test.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:21e0df4f43fd2ef466c22083dc298aa5044036b7
# Generated 2020-01-05 23:12:58.959257 by PyXB version 1.2.5 using Python 3.7.0.final.0
# Namespace http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:87b7c586-3008-11ea-b4a5-bc8385d547cd')

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
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config', create_if_missing=True)
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


# Atomic simple type: {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}maturity_type
class maturity_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """This type denotes a maturity of a model. It can either be development or production."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'maturity_type')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 27, 4)
    _Documentation = 'This type denotes a maturity of a model. It can either be development or production.'
maturity_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=maturity_type, enum_prefix=None)
maturity_type.development = maturity_type._CF_enumeration.addEnumeration(unicode_value='development', tag='development')
maturity_type.production = maturity_type._CF_enumeration.addEnumeration(unicode_value='production', tag='production')
maturity_type._InitializeFacetMap(maturity_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'maturity_type', maturity_type)
_module_typeBindings.maturity_type = maturity_type

# Atomic simple type: {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}sensor_type
class sensor_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sensor_type')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 74, 4)
    _Documentation = None
sensor_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=sensor_type, enum_prefix=None)
sensor_type.camera = sensor_type._CF_enumeration.addEnumeration(unicode_value='camera', tag='camera')
sensor_type.audio = sensor_type._CF_enumeration.addEnumeration(unicode_value='audio', tag='audio')
sensor_type.contact = sensor_type._CF_enumeration.addEnumeration(unicode_value='contact', tag='contact')
sensor_type.laser = sensor_type._CF_enumeration.addEnumeration(unicode_value='laser', tag='laser')
sensor_type.ultrasound = sensor_type._CF_enumeration.addEnumeration(unicode_value='ultrasound', tag='ultrasound')
sensor_type.radar = sensor_type._CF_enumeration.addEnumeration(unicode_value='radar', tag='radar')
sensor_type.gps = sensor_type._CF_enumeration.addEnumeration(unicode_value='gps', tag='gps')
sensor_type.olfaction = sensor_type._CF_enumeration.addEnumeration(unicode_value='olfaction', tag='olfaction')
sensor_type.other = sensor_type._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
sensor_type.force_torque = sensor_type._CF_enumeration.addEnumeration(unicode_value='force_torque', tag='force_torque')
sensor_type._InitializeFacetMap(sensor_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'sensor_type', sensor_type)
_module_typeBindings.sensor_type = sensor_type

# Atomic simple type: {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}actuator_type
class actuator_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actuator_type')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 101, 4)
    _Documentation = None
actuator_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=actuator_type, enum_prefix=None)
actuator_type.motor = actuator_type._CF_enumeration.addEnumeration(unicode_value='motor', tag='motor')
actuator_type.muscle = actuator_type._CF_enumeration.addEnumeration(unicode_value='muscle', tag='muscle')
actuator_type.linear = actuator_type._CF_enumeration.addEnumeration(unicode_value='linear', tag='linear')
actuator_type.pneumatic = actuator_type._CF_enumeration.addEnumeration(unicode_value='pneumatic', tag='pneumatic')
actuator_type.hydraulic = actuator_type._CF_enumeration.addEnumeration(unicode_value='hydraulic', tag='hydraulic')
actuator_type.other = actuator_type._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
actuator_type._InitializeFacetMap(actuator_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'actuator_type', actuator_type)
_module_typeBindings.actuator_type = actuator_type

# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}ModelConfiguration with content type ELEMENT_ONLY
class ModelConfiguration (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}ModelConfiguration with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ModelConfiguration')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 7, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configname', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 9, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configversion', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 10, 12), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}maturity uses Python identifier maturity
    __maturity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maturity'), 'maturity', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configmaturity', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 11, 12), )

    
    maturity = property(__maturity.value, __maturity.set, None, 'The maturity of the model. Determines whether it is shown by default to the user or only browsable in dev mode.')

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'license'), 'license', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configlicense', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 16, 12), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}thumbnail uses Python identifier thumbnail
    __thumbnail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'thumbnail'), 'thumbnail', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configthumbnail', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 17, 12), )

    
    thumbnail = property(__thumbnail.value, __thumbnail.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}frontend_skin_model uses Python identifier frontend_skin_model
    __frontend_skin_model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'frontend_skin_model'), 'frontend_skin_model', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configfrontend_skin_model', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 18, 12), )

    
    frontend_skin_model = property(__frontend_skin_model.value, __frontend_skin_model.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}sdf uses Python identifier sdf
    __sdf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sdf'), 'sdf', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configsdf', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 19, 12), )

    
    sdf = property(__sdf.value, __sdf.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'author'), 'author', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configauthor', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 20, 12), )

    
    author = property(__author.value, __author.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configdescription', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 21, 12), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}website uses Python identifier website
    __website = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'website'), 'website', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configwebsite', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 22, 12), )

    
    website = property(__website.value, __website.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}documentation uses Python identifier documentation
    __documentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentation'), 'documentation', '__httpschemas_humanbrainproject_euSP102017robot_model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017robot_model_configdocumentation', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 23, 12), )

    
    documentation = property(__documentation.value, __documentation.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __version.name() : __version,
        __maturity.name() : __maturity,
        __license.name() : __license,
        __thumbnail.name() : __thumbnail,
        __frontend_skin_model.name() : __frontend_skin_model,
        __sdf.name() : __sdf,
        __author.name() : __author,
        __description.name() : __description,
        __website.name() : __website,
        __documentation.name() : __documentation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ModelConfiguration = ModelConfiguration
Namespace.addCategoryObject('typeBinding', 'ModelConfiguration', ModelConfiguration)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}sdf_versioned with content type SIMPLE
class sdf_versioned (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}sdf_versioned with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sdf_versioned')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 37, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpschemas_humanbrainproject_euSP102017robot_model_config_sdf_versioned_version', pyxb.binding.datatypes.decimal)
    __version._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 40, 16)
    __version._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 40, 16)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.sdf_versioned = sdf_versioned
Namespace.addCategoryObject('typeBinding', 'sdf_versioned', sdf_versioned)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}author_type with content type ELEMENT_ONLY
class author_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}author_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'author_type')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpschemas_humanbrainproject_euSP102017robot_model_config_author_type_httpschemas_humanbrainproject_euSP102017robot_model_configname', True, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 48, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__httpschemas_humanbrainproject_euSP102017robot_model_config_author_type_httpschemas_humanbrainproject_euSP102017robot_model_configemail', True, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 49, 12), )

    
    email = property(__email.value, __email.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __email.name() : __email
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.author_type = author_type
Namespace.addCategoryObject('typeBinding', 'author_type', author_type)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}documentation_type with content type ELEMENT_ONLY
class documentation_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}documentation_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'documentation_type')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 53, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}sensors uses Python identifier sensors
    __sensors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sensors'), 'sensors', '__httpschemas_humanbrainproject_euSP102017robot_model_config_documentation_type_httpschemas_humanbrainproject_euSP102017robot_model_configsensors', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 55, 12), )

    
    sensors = property(__sensors.value, __sensors.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}actuators uses Python identifier actuators
    __actuators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuators'), 'actuators', '__httpschemas_humanbrainproject_euSP102017robot_model_config_documentation_type_httpschemas_humanbrainproject_euSP102017robot_model_configactuators', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 56, 12), )

    
    actuators = property(__actuators.value, __actuators.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}publication uses Python identifier publication
    __publication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'publication'), 'publication', '__httpschemas_humanbrainproject_euSP102017robot_model_config_documentation_type_httpschemas_humanbrainproject_euSP102017robot_model_configpublication', True, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 57, 12), )

    
    publication = property(__publication.value, __publication.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}youtube uses Python identifier youtube
    __youtube = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'youtube'), 'youtube', '__httpschemas_humanbrainproject_euSP102017robot_model_config_documentation_type_httpschemas_humanbrainproject_euSP102017robot_model_configyoutube', True, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 58, 12), )

    
    youtube = property(__youtube.value, __youtube.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}picture uses Python identifier picture
    __picture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'picture'), 'picture', '__httpschemas_humanbrainproject_euSP102017robot_model_config_documentation_type_httpschemas_humanbrainproject_euSP102017robot_model_configpicture', True, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 59, 12), )

    
    picture = property(__picture.value, __picture.set, None, None)

    _ElementMap.update({
        __sensors.name() : __sensors,
        __actuators.name() : __actuators,
        __publication.name() : __publication,
        __youtube.name() : __youtube,
        __picture.name() : __picture
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.documentation_type = documentation_type
Namespace.addCategoryObject('typeBinding', 'documentation_type', documentation_type)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}sensors_type with content type ELEMENT_ONLY
class sensors_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}sensors_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sensors_type')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 63, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}sensor uses Python identifier sensor
    __sensor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sensor'), 'sensor', '__httpschemas_humanbrainproject_euSP102017robot_model_config_sensors_type_httpschemas_humanbrainproject_euSP102017robot_model_configsensor', True, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 65, 12), )

    
    sensor = property(__sensor.value, __sensor.set, None, None)

    _ElementMap.update({
        __sensor.name() : __sensor
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.sensors_type = sensors_type
Namespace.addCategoryObject('typeBinding', 'sensors_type', sensors_type)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}actuators_type with content type ELEMENT_ONLY
class actuators_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}actuators_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'actuators_type')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 90, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}actuator uses Python identifier actuator
    __actuator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actuator'), 'actuator', '__httpschemas_humanbrainproject_euSP102017robot_model_config_actuators_type_httpschemas_humanbrainproject_euSP102017robot_model_configactuator', True, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 92, 12), )

    
    actuator = property(__actuator.value, __actuator.set, None, None)

    _ElementMap.update({
        __actuator.name() : __actuator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.actuators_type = actuators_type
Namespace.addCategoryObject('typeBinding', 'actuators_type', actuators_type)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}youtube_resource with content type EMPTY
class youtube_resource (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}youtube_resource with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'youtube_resource')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 113, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpschemas_humanbrainproject_euSP102017robot_model_config_youtube_resource_title', pyxb.binding.datatypes.string, required=True)
    __title._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 114, 8)
    __title._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 114, 8)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute youtube-id uses Python identifier youtube_id
    __youtube_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'youtube-id'), 'youtube_id', '__httpschemas_humanbrainproject_euSP102017robot_model_config_youtube_resource_youtube_id', pyxb.binding.datatypes.string, required=True)
    __youtube_id._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 115, 8)
    __youtube_id._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 115, 8)
    
    youtube_id = property(__youtube_id.value, __youtube_id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __title.name() : __title,
        __youtube_id.name() : __youtube_id
    })
_module_typeBindings.youtube_resource = youtube_resource
Namespace.addCategoryObject('typeBinding', 'youtube_resource', youtube_resource)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}url_resource with content type EMPTY
class url_resource (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}url_resource with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'url_resource')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 118, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpschemas_humanbrainproject_euSP102017robot_model_config_url_resource_title', pyxb.binding.datatypes.string, required=True)
    __title._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 119, 8)
    __title._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 119, 8)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__httpschemas_humanbrainproject_euSP102017robot_model_config_url_resource_url', pyxb.binding.datatypes.string, required=True)
    __url._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 120, 8)
    __url._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 120, 8)
    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __title.name() : __title,
        __url.name() : __url
    })
_module_typeBindings.url_resource = url_resource
Namespace.addCategoryObject('typeBinding', 'url_resource', url_resource)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}publication_type with content type EMPTY
class publication_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}publication_type with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'publication_type')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 124, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpschemas_humanbrainproject_euSP102017robot_model_config_publication_type_title', pyxb.binding.datatypes.string, required=True)
    __title._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 125, 8)
    __title._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 125, 8)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__httpschemas_humanbrainproject_euSP102017robot_model_config_publication_type_url', pyxb.binding.datatypes.string, required=True)
    __url._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 126, 8)
    __url._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 126, 8)
    
    url = property(__url.value, __url.set, None, None)

    
    # Attribute authors uses Python identifier authors
    __authors = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'authors'), 'authors', '__httpschemas_humanbrainproject_euSP102017robot_model_config_publication_type_authors', pyxb.binding.datatypes.string, required=True)
    __authors._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 127, 8)
    __authors._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 127, 8)
    
    authors = property(__authors.value, __authors.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __title.name() : __title,
        __url.name() : __url,
        __authors.name() : __authors
    })
_module_typeBindings.publication_type = publication_type
Namespace.addCategoryObject('typeBinding', 'publication_type', publication_type)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}frontend_skin_model with content type ELEMENT_ONLY
class frontend_skin_model (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}frontend_skin_model with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'frontend_skin_model')
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 130, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}mesh uses Python identifier mesh
    __mesh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mesh'), 'mesh', '__httpschemas_humanbrainproject_euSP102017robot_model_config_frontend_skin_model_httpschemas_humanbrainproject_euSP102017robot_model_configmesh', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 132, 12), )

    
    mesh = property(__mesh.value, __mesh.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/robot_model_config}scale uses Python identifier scale
    __scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scale'), 'scale', '__httpschemas_humanbrainproject_euSP102017robot_model_config_frontend_skin_model_httpschemas_humanbrainproject_euSP102017robot_model_configscale', False, pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 133, 12), )

    
    scale = property(__scale.value, __scale.set, None, None)

    _ElementMap.update({
        __mesh.name() : __mesh,
        __scale.name() : __scale
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.frontend_skin_model = frontend_skin_model
Namespace.addCategoryObject('typeBinding', 'frontend_skin_model', frontend_skin_model)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 66, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpschemas_humanbrainproject_euSP102017robot_model_config_CTD_ANON_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 67, 20)
    __name._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 67, 20)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpschemas_humanbrainproject_euSP102017robot_model_config_CTD_ANON_type', _module_typeBindings.sensor_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 68, 20)
    __type._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 68, 20)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 93, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpschemas_humanbrainproject_euSP102017robot_model_config_CTD_ANON__name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 94, 20)
    __name._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 94, 20)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpschemas_humanbrainproject_euSP102017robot_model_config_CTD_ANON__type', _module_typeBindings.actuator_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 95, 20)
    __type._UseLocation = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 95, 20)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


model = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'model'), ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', model.name().localName(), model)



ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 9, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), pyxb.binding.datatypes.decimal, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 10, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maturity'), maturity_type, scope=ModelConfiguration, documentation='The maturity of the model. Determines whether it is shown by default to the user or only browsable in dev mode.', location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 11, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'license'), pyxb.binding.datatypes.string, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 16, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thumbnail'), pyxb.binding.datatypes.string, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 17, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'frontend_skin_model'), frontend_skin_model, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 18, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sdf'), sdf_versioned, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 19, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'author'), author_type, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 20, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 21, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'website'), pyxb.binding.datatypes.string, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 22, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), documentation_type, scope=ModelConfiguration, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 23, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 9, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 10, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 10, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 11, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maturity')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 16, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'license')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 16, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 17, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'thumbnail')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 17, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 18, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'frontend_skin_model')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 18, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sdf')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 20, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'author')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 20, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 21, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 22, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'website')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 22, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 23, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentation')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 10, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 11, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 16, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 17, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 18, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 20, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 22, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 23, 12))
    counters.add(cc_7)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    sub_automata.append(_BuildAutomaton_8())
    sub_automata.append(_BuildAutomaton_9())
    sub_automata.append(_BuildAutomaton_10())
    sub_automata.append(_BuildAutomaton_11())
    final_update = set()
    symbol = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 8, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ModelConfiguration._Automaton = _BuildAutomaton()




author_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=author_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 48, 12)))

author_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), pyxb.binding.datatypes.string, scope=author_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 49, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 47, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(author_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 48, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(author_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 49, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
author_type._Automaton = _BuildAutomaton_12()




documentation_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sensors'), sensors_type, scope=documentation_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 55, 12)))

documentation_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuators'), actuators_type, scope=documentation_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 56, 12)))

documentation_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publication'), publication_type, scope=documentation_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 57, 12)))

documentation_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'youtube'), youtube_resource, scope=documentation_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 58, 12)))

documentation_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'picture'), url_resource, scope=documentation_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 59, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 55, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 56, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 57, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 58, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 59, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(documentation_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sensors')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 55, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(documentation_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuators')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 56, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(documentation_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'publication')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 57, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(documentation_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'youtube')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 58, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(documentation_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'picture')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 59, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
documentation_type._Automaton = _BuildAutomaton_13()




sensors_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sensor'), CTD_ANON, scope=sensors_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 65, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 64, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sensors_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sensor')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 65, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
sensors_type._Automaton = _BuildAutomaton_14()




actuators_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actuator'), CTD_ANON_, scope=actuators_type, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 92, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 91, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(actuators_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actuator')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 92, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
actuators_type._Automaton = _BuildAutomaton_15()




frontend_skin_model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mesh'), pyxb.binding.datatypes.string, scope=frontend_skin_model, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 132, 12)))

frontend_skin_model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scale'), pyxb.binding.datatypes.float, scope=frontend_skin_model, location=pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 133, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(frontend_skin_model._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mesh')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 132, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(frontend_skin_model._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scale')), pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 133, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    final_update = set()
    symbol = pyxb.utils.utility.Location('file:///C:/Users/Jin-Ho/Desktop/HBP/BlenderRobotDesigner/robot_designer_plugin/resources/robot_model_configuration.xsd', 131, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
frontend_skin_model._Automaton = _BuildAutomaton_16()

