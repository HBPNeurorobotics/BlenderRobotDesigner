# ./model_config_dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f3c005e9b9c52e1326beb2c149090b5a0e4f220c
# Generated 2017-05-02 10:54:34.704797 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://schemas.humanbrainproject.eu/SP10/2017/model_config

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f6f001cc-2f14-11e7-9f46-847beb469236')

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
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.humanbrainproject.eu/SP10/2017/model_config', create_if_missing=True)
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


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/model_config}ModelConfiguration with content type ELEMENT_ONLY
class ModelConfiguration (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/model_config}ModelConfiguration with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ModelConfiguration')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 9, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/model_config}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpschemas_humanbrainproject_euSP102017model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017model_configname', False, pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 11, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/model_config}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__httpschemas_humanbrainproject_euSP102017model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017model_configversion', False, pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 12, 12), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/model_config}thumbnail uses Python identifier thumbnail
    __thumbnail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'thumbnail'), 'thumbnail', '__httpschemas_humanbrainproject_euSP102017model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017model_configthumbnail', False, pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 13, 12), )

    
    thumbnail = property(__thumbnail.value, __thumbnail.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/model_config}sdf uses Python identifier sdf
    __sdf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sdf'), 'sdf', '__httpschemas_humanbrainproject_euSP102017model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017model_configsdf', False, pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 14, 12), )

    
    sdf = property(__sdf.value, __sdf.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/model_config}author uses Python identifier author
    __author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'author'), 'author', '__httpschemas_humanbrainproject_euSP102017model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017model_configauthor', False, pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 15, 12), )

    
    author = property(__author.value, __author.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/model_config}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpschemas_humanbrainproject_euSP102017model_config_ModelConfiguration_httpschemas_humanbrainproject_euSP102017model_configdescription', False, pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 16, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __version.name() : __version,
        __thumbnail.name() : __thumbnail,
        __sdf.name() : __sdf,
        __author.name() : __author,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ModelConfiguration = ModelConfiguration
Namespace.addCategoryObject('typeBinding', 'ModelConfiguration', ModelConfiguration)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/model_config}sdf_versioned with content type SIMPLE
class sdf_versioned (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/model_config}sdf_versioned with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sdf_versioned')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 20, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpschemas_humanbrainproject_euSP102017model_config_sdf_versioned_version', pyxb.binding.datatypes.decimal)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 23, 16)
    __version._UseLocation = pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 23, 16)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.sdf_versioned = sdf_versioned
Namespace.addCategoryObject('typeBinding', 'sdf_versioned', sdf_versioned)


# Complex type {http://schemas.humanbrainproject.eu/SP10/2017/model_config}author_type with content type ELEMENT_ONLY
class author_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://schemas.humanbrainproject.eu/SP10/2017/model_config}author_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'author_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 29, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/model_config}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpschemas_humanbrainproject_euSP102017model_config_author_type_httpschemas_humanbrainproject_euSP102017model_configname', True, pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 31, 13), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://schemas.humanbrainproject.eu/SP10/2017/model_config}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__httpschemas_humanbrainproject_euSP102017model_config_author_type_httpschemas_humanbrainproject_euSP102017model_configemail', True, pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 32, 13), )

    
    email = property(__email.value, __email.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __email.name() : __email
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.author_type = author_type
Namespace.addCategoryObject('typeBinding', 'author_type', author_type)


model = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'model'), ModelConfiguration, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', model.name().localName(), model)



ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=ModelConfiguration, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 11, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), pyxb.binding.datatypes.decimal, scope=ModelConfiguration, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 12, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thumbnail'), pyxb.binding.datatypes.string, scope=ModelConfiguration, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 13, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sdf'), sdf_versioned, scope=ModelConfiguration, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 14, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'author'), author_type, scope=ModelConfiguration, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 15, 12)))

ModelConfiguration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), pyxb.binding.datatypes.string, scope=ModelConfiguration, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 16, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 15, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 12, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'thumbnail')), pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 13, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sdf')), pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 14, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'author')), pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 15, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ModelConfiguration._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 16, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ModelConfiguration._Automaton = _BuildAutomaton()




author_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=author_type, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 31, 13)))

author_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), pyxb.binding.datatypes.string, scope=author_type, location=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 32, 13)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 30, 9))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(author_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 31, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(author_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('/home/user/WORK/NRP/RobotDesigner/Epics/2-generateConfigFile/model_configuration.xsd', 32, 13))
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
author_type._Automaton = _BuildAutomaton_()

