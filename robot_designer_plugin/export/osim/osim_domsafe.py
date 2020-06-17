# /home/user/Desktop/osim_dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2020-04-21 17:48:24.940004 by PyXB version 1.2.5 using Python 2.7.15.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:89145efc-83e7-11ea-b196-e4b31839886b')

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
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 258, 2)
    _Documentation = None
vector3._CF_pattern = pyxb.binding.facets.CF_pattern()
vector3._CF_pattern.addPattern(pattern='(\\s*(\\-?\\+?)(\\d+)(\\d*\\.*\\d*)e?E?(\\-?\\+?)[0-9]*\\s+){2}(\\s*(\\-?\\+?)(\\d+)(\\d*\\.*\\d*)e?E?(\\-?\\+?)[0-9]*\\s*)')
vector3._InitializeFacetMap(vector3._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'vector3', vector3)
_module_typeBindings.vector3 = vector3

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 5, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Model'), 'Model', '__AbsentNamespace0_CTD_ANON_Model', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 7, 8), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__AbsentNamespace0_CTD_ANON_Version', pyxb.binding.datatypes.string)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 32, 6)
    __Version._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 32, 6)
    
    Version = property(__Version.value, __Version.set, None, None)

    _ElementMap.update({
        __Model.name() : __Model
    })
    _AttributeMap.update({
        __Version.name() : __Version
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 8, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ForceSet uses Python identifier ForceSet
    __ForceSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ForceSet'), 'ForceSet', '__AbsentNamespace0_CTD_ANON__ForceSet', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 10, 14), )

    
    ForceSet = property(__ForceSet.value, __ForceSet.set, None, None)

    
    # Element BodySet uses Python identifier BodySet
    __BodySet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BodySet'), 'BodySet', '__AbsentNamespace0_CTD_ANON__BodySet', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 27, 14), )

    
    BodySet = property(__BodySet.value, __BodySet.set, None, None)

    _ElementMap.update({
        __ForceSet.name() : __ForceSet,
        __BodySet.name() : __BodySet
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
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 11, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objects uses Python identifier objects
    __objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objects'), 'objects', '__AbsentNamespace0_CTD_ANON_2_objects', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 13, 20), )

    
    objects = property(__objects.value, __objects.set, None, None)

    _ElementMap.update({
        __objects.name() : __objects
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 14, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Millard2012EquilibriumMuscle uses Python identifier Millard2012EquilibriumMuscle
    __Millard2012EquilibriumMuscle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Millard2012EquilibriumMuscle'), 'Millard2012EquilibriumMuscle', '__AbsentNamespace0_CTD_ANON_3_Millard2012EquilibriumMuscle', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 16, 26), )

    
    Millard2012EquilibriumMuscle = property(__Millard2012EquilibriumMuscle.value, __Millard2012EquilibriumMuscle.set, None, None)

    
    # Element Millard2012AccelerationMuscle uses Python identifier Millard2012AccelerationMuscle
    __Millard2012AccelerationMuscle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Millard2012AccelerationMuscle'), 'Millard2012AccelerationMuscle', '__AbsentNamespace0_CTD_ANON_3_Millard2012AccelerationMuscle', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 17, 26), )

    
    Millard2012AccelerationMuscle = property(__Millard2012AccelerationMuscle.value, __Millard2012AccelerationMuscle.set, None, None)

    
    # Element Thelen2003Muscle uses Python identifier Thelen2003Muscle
    __Thelen2003Muscle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Thelen2003Muscle'), 'Thelen2003Muscle', '__AbsentNamespace0_CTD_ANON_3_Thelen2003Muscle', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 18, 26), )

    
    Thelen2003Muscle = property(__Thelen2003Muscle.value, __Thelen2003Muscle.set, None, None)

    
    # Element RigidTendonMuscle uses Python identifier RigidTendonMuscle
    __RigidTendonMuscle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RigidTendonMuscle'), 'RigidTendonMuscle', '__AbsentNamespace0_CTD_ANON_3_RigidTendonMuscle', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 19, 26), )

    
    RigidTendonMuscle = property(__RigidTendonMuscle.value, __RigidTendonMuscle.set, None, None)

    
    # Element MyoroboticsMuscle uses Python identifier MyoroboticsMuscle
    __MyoroboticsMuscle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MyoroboticsMuscle'), 'MyoroboticsMuscle', '__AbsentNamespace0_CTD_ANON_3_MyoroboticsMuscle', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 20, 26), )

    
    MyoroboticsMuscle = property(__MyoroboticsMuscle.value, __MyoroboticsMuscle.set, None, None)

    _ElementMap.update({
        __Millard2012EquilibriumMuscle.name() : __Millard2012EquilibriumMuscle,
        __Millard2012AccelerationMuscle.name() : __Millard2012AccelerationMuscle,
        __Thelen2003Muscle.name() : __Thelen2003Muscle,
        __RigidTendonMuscle.name() : __RigidTendonMuscle,
        __MyoroboticsMuscle.name() : __MyoroboticsMuscle
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type BodySet with content type ELEMENT_ONLY
class BodySet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BodySet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BodySet')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 72, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objects uses Python identifier objects
    __objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objects'), 'objects', '__AbsentNamespace0_BodySet_objects', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 74, 6), )

    
    objects = property(__objects.value, __objects.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_BodySet_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 82, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 82, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __objects.name() : __objects
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.BodySet = BodySet
Namespace.addCategoryObject('typeBinding', 'BodySet', BodySet)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 75, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Body'), 'Body', '__AbsentNamespace0_CTD_ANON_4_Body', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 77, 12), )

    
    Body = property(__Body.value, __Body.set, None, None)

    _ElementMap.update({
        __Body.name() : __Body
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type Body with content type ELEMENT_ONLY
class Body (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Body with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Body')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 85, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element WrapObjectSet uses Python identifier WrapObjectSet
    __WrapObjectSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'WrapObjectSet'), 'WrapObjectSet', '__AbsentNamespace0_Body_WrapObjectSet', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 87, 6), )

    
    WrapObjectSet = property(__WrapObjectSet.value, __WrapObjectSet.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Body_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 89, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 89, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __WrapObjectSet.name() : __WrapObjectSet
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.Body = Body
Namespace.addCategoryObject('typeBinding', 'Body', Body)


# Complex type WrapObjectSet with content type ELEMENT_ONLY
class WrapObjectSet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type WrapObjectSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WrapObjectSet')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 92, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objects uses Python identifier objects
    __objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objects'), 'objects', '__AbsentNamespace0_WrapObjectSet_objects', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 94, 6), )

    
    objects = property(__objects.value, __objects.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_WrapObjectSet_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 103, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 103, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __objects.name() : __objects
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.WrapObjectSet = WrapObjectSet
Namespace.addCategoryObject('typeBinding', 'WrapObjectSet', WrapObjectSet)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 95, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element WrapCylinder uses Python identifier WrapCylinder
    __WrapCylinder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'WrapCylinder'), 'WrapCylinder', '__AbsentNamespace0_CTD_ANON_5_WrapCylinder', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 97, 12), )

    
    WrapCylinder = property(__WrapCylinder.value, __WrapCylinder.set, None, None)

    
    # Element WrapSphere uses Python identifier WrapSphere
    __WrapSphere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'WrapSphere'), 'WrapSphere', '__AbsentNamespace0_CTD_ANON_5_WrapSphere', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 98, 12), )

    
    WrapSphere = property(__WrapSphere.value, __WrapSphere.set, None, None)

    _ElementMap.update({
        __WrapCylinder.name() : __WrapCylinder,
        __WrapSphere.name() : __WrapSphere
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type Millard2012EquilibriumMuscle with content type ELEMENT_ONLY
class Millard2012EquilibriumMuscle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Millard2012EquilibriumMuscle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Millard2012EquilibriumMuscle')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 106, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element optimal_force uses Python identifier optimal_force
    __optimal_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_force'), 'optimal_force', '__AbsentNamespace0_Millard2012EquilibriumMuscle_optimal_force', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4), )

    
    optimal_force = property(__optimal_force.value, __optimal_force.set, None, None)

    
    # Element max_isometric_force uses Python identifier max_isometric_force
    __max_isometric_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), 'max_isometric_force', '__AbsentNamespace0_Millard2012EquilibriumMuscle_max_isometric_force', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4), )

    
    max_isometric_force = property(__max_isometric_force.value, __max_isometric_force.set, None, 'Maximum isometric force that the fibers can generate.')

    
    # Element min_control uses Python identifier min_control
    __min_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_control'), 'min_control', '__AbsentNamespace0_Millard2012EquilibriumMuscle_min_control', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4), )

    
    min_control = property(__min_control.value, __min_control.set, None, None)

    
    # Element max_control uses Python identifier max_control
    __max_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_control'), 'max_control', '__AbsentNamespace0_Millard2012EquilibriumMuscle_max_control', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4), )

    
    max_control = property(__max_control.value, __max_control.set, None, 'Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.')

    
    # Element optimal_fiber_length uses Python identifier optimal_fiber_length
    __optimal_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), 'optimal_fiber_length', '__AbsentNamespace0_Millard2012EquilibriumMuscle_optimal_fiber_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4), )

    
    optimal_fiber_length = property(__optimal_fiber_length.value, __optimal_fiber_length.set, None, 'Optimal length of the muscle fibers.')

    
    # Element tendon_slack_length uses Python identifier tendon_slack_length
    __tendon_slack_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), 'tendon_slack_length', '__AbsentNamespace0_Millard2012EquilibriumMuscle_tendon_slack_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4), )

    
    tendon_slack_length = property(__tendon_slack_length.value, __tendon_slack_length.set, None, 'Resting length of the tendonResting length of the tendon.')

    
    # Element pennation_angle_at_optimal uses Python identifier pennation_angle_at_optimal
    __pennation_angle_at_optimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), 'pennation_angle_at_optimal', '__AbsentNamespace0_Millard2012EquilibriumMuscle_pennation_angle_at_optimal', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4), )

    
    pennation_angle_at_optimal = property(__pennation_angle_at_optimal.value, __pennation_angle_at_optimal.set, None, 'Angle between tendon and fibers at optimal fiber length expressed in radians.')

    
    # Element max_contraction_velocity uses Python identifier max_contraction_velocity
    __max_contraction_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity'), 'max_contraction_velocity', '__AbsentNamespace0_Millard2012EquilibriumMuscle_max_contraction_velocity', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4), )

    
    max_contraction_velocity = property(__max_contraction_velocity.value, __max_contraction_velocity.set, None, None)

    
    # Element ignore_tendon_compliance uses Python identifier ignore_tendon_compliance
    __ignore_tendon_compliance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance'), 'ignore_tendon_compliance', '__AbsentNamespace0_Millard2012EquilibriumMuscle_ignore_tendon_compliance', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4), )

    
    ignore_tendon_compliance = property(__ignore_tendon_compliance.value, __ignore_tendon_compliance.set, None, None)

    
    # Element ignore_activation_dynamics uses Python identifier ignore_activation_dynamics
    __ignore_activation_dynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics'), 'ignore_activation_dynamics', '__AbsentNamespace0_Millard2012EquilibriumMuscle_ignore_activation_dynamics', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4), )

    
    ignore_activation_dynamics = property(__ignore_activation_dynamics.value, __ignore_activation_dynamics.set, None, None)

    
    # Element fiber_damping uses Python identifier fiber_damping
    __fiber_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fiber_damping'), 'fiber_damping', '__AbsentNamespace0_Millard2012EquilibriumMuscle_fiber_damping', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 109, 8), )

    
    fiber_damping = property(__fiber_damping.value, __fiber_damping.set, None, None)

    
    # Element default_activation uses Python identifier default_activation
    __default_activation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_activation'), 'default_activation', '__AbsentNamespace0_Millard2012EquilibriumMuscle_default_activation', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 110, 8), )

    
    default_activation = property(__default_activation.value, __default_activation.set, None, None)

    
    # Element default_fiber_length uses Python identifier default_fiber_length
    __default_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_fiber_length'), 'default_fiber_length', '__AbsentNamespace0_Millard2012EquilibriumMuscle_default_fiber_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 111, 8), )

    
    default_fiber_length = property(__default_fiber_length.value, __default_fiber_length.set, None, None)

    
    # Element activation_time_constant uses Python identifier activation_time_constant
    __activation_time_constant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'activation_time_constant'), 'activation_time_constant', '__AbsentNamespace0_Millard2012EquilibriumMuscle_activation_time_constant', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 112, 8), )

    
    activation_time_constant = property(__activation_time_constant.value, __activation_time_constant.set, None, None)

    
    # Element deactivation_time_constant uses Python identifier deactivation_time_constant
    __deactivation_time_constant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deactivation_time_constant'), 'deactivation_time_constant', '__AbsentNamespace0_Millard2012EquilibriumMuscle_deactivation_time_constant', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 113, 8), )

    
    deactivation_time_constant = property(__deactivation_time_constant.value, __deactivation_time_constant.set, None, None)

    
    # Element minimum_activation uses Python identifier minimum_activation
    __minimum_activation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'minimum_activation'), 'minimum_activation', '__AbsentNamespace0_Millard2012EquilibriumMuscle_minimum_activation', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 114, 8), )

    
    minimum_activation = property(__minimum_activation.value, __minimum_activation.set, None, None)

    
    # Element GeometryPath uses Python identifier GeometryPath
    __GeometryPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), 'GeometryPath', '__AbsentNamespace0_Millard2012EquilibriumMuscle_GeometryPath', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2), )

    
    GeometryPath = property(__GeometryPath.value, __GeometryPath.set, None, 'The set of points defining the path of the muscle.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Millard2012EquilibriumMuscle_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 116, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 116, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __optimal_force.name() : __optimal_force,
        __max_isometric_force.name() : __max_isometric_force,
        __min_control.name() : __min_control,
        __max_control.name() : __max_control,
        __optimal_fiber_length.name() : __optimal_fiber_length,
        __tendon_slack_length.name() : __tendon_slack_length,
        __pennation_angle_at_optimal.name() : __pennation_angle_at_optimal,
        __max_contraction_velocity.name() : __max_contraction_velocity,
        __ignore_tendon_compliance.name() : __ignore_tendon_compliance,
        __ignore_activation_dynamics.name() : __ignore_activation_dynamics,
        __fiber_damping.name() : __fiber_damping,
        __default_activation.name() : __default_activation,
        __default_fiber_length.name() : __default_fiber_length,
        __activation_time_constant.name() : __activation_time_constant,
        __deactivation_time_constant.name() : __deactivation_time_constant,
        __minimum_activation.name() : __minimum_activation,
        __GeometryPath.name() : __GeometryPath
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.Millard2012EquilibriumMuscle = Millard2012EquilibriumMuscle
Namespace.addCategoryObject('typeBinding', 'Millard2012EquilibriumMuscle', Millard2012EquilibriumMuscle)


# Complex type Millard2012AccelerationMuscle with content type ELEMENT_ONLY
class Millard2012AccelerationMuscle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Millard2012AccelerationMuscle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Millard2012AccelerationMuscle')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 119, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element optimal_force uses Python identifier optimal_force
    __optimal_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_force'), 'optimal_force', '__AbsentNamespace0_Millard2012AccelerationMuscle_optimal_force', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4), )

    
    optimal_force = property(__optimal_force.value, __optimal_force.set, None, None)

    
    # Element max_isometric_force uses Python identifier max_isometric_force
    __max_isometric_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), 'max_isometric_force', '__AbsentNamespace0_Millard2012AccelerationMuscle_max_isometric_force', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4), )

    
    max_isometric_force = property(__max_isometric_force.value, __max_isometric_force.set, None, 'Maximum isometric force that the fibers can generate.')

    
    # Element min_control uses Python identifier min_control
    __min_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_control'), 'min_control', '__AbsentNamespace0_Millard2012AccelerationMuscle_min_control', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4), )

    
    min_control = property(__min_control.value, __min_control.set, None, None)

    
    # Element max_control uses Python identifier max_control
    __max_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_control'), 'max_control', '__AbsentNamespace0_Millard2012AccelerationMuscle_max_control', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4), )

    
    max_control = property(__max_control.value, __max_control.set, None, 'Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.')

    
    # Element optimal_fiber_length uses Python identifier optimal_fiber_length
    __optimal_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), 'optimal_fiber_length', '__AbsentNamespace0_Millard2012AccelerationMuscle_optimal_fiber_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4), )

    
    optimal_fiber_length = property(__optimal_fiber_length.value, __optimal_fiber_length.set, None, 'Optimal length of the muscle fibers.')

    
    # Element tendon_slack_length uses Python identifier tendon_slack_length
    __tendon_slack_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), 'tendon_slack_length', '__AbsentNamespace0_Millard2012AccelerationMuscle_tendon_slack_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4), )

    
    tendon_slack_length = property(__tendon_slack_length.value, __tendon_slack_length.set, None, 'Resting length of the tendonResting length of the tendon.')

    
    # Element pennation_angle_at_optimal uses Python identifier pennation_angle_at_optimal
    __pennation_angle_at_optimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), 'pennation_angle_at_optimal', '__AbsentNamespace0_Millard2012AccelerationMuscle_pennation_angle_at_optimal', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4), )

    
    pennation_angle_at_optimal = property(__pennation_angle_at_optimal.value, __pennation_angle_at_optimal.set, None, 'Angle between tendon and fibers at optimal fiber length expressed in radians.')

    
    # Element max_contraction_velocity uses Python identifier max_contraction_velocity
    __max_contraction_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity'), 'max_contraction_velocity', '__AbsentNamespace0_Millard2012AccelerationMuscle_max_contraction_velocity', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4), )

    
    max_contraction_velocity = property(__max_contraction_velocity.value, __max_contraction_velocity.set, None, None)

    
    # Element ignore_tendon_compliance uses Python identifier ignore_tendon_compliance
    __ignore_tendon_compliance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance'), 'ignore_tendon_compliance', '__AbsentNamespace0_Millard2012AccelerationMuscle_ignore_tendon_compliance', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4), )

    
    ignore_tendon_compliance = property(__ignore_tendon_compliance.value, __ignore_tendon_compliance.set, None, None)

    
    # Element ignore_activation_dynamics uses Python identifier ignore_activation_dynamics
    __ignore_activation_dynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics'), 'ignore_activation_dynamics', '__AbsentNamespace0_Millard2012AccelerationMuscle_ignore_activation_dynamics', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4), )

    
    ignore_activation_dynamics = property(__ignore_activation_dynamics.value, __ignore_activation_dynamics.set, None, None)

    
    # Element default_activation uses Python identifier default_activation
    __default_activation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_activation'), 'default_activation', '__AbsentNamespace0_Millard2012AccelerationMuscle_default_activation', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 122, 8), )

    
    default_activation = property(__default_activation.value, __default_activation.set, None, None)

    
    # Element default_fiber_length uses Python identifier default_fiber_length
    __default_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_fiber_length'), 'default_fiber_length', '__AbsentNamespace0_Millard2012AccelerationMuscle_default_fiber_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 123, 8), )

    
    default_fiber_length = property(__default_fiber_length.value, __default_fiber_length.set, None, None)

    
    # Element default_fiber_velocity uses Python identifier default_fiber_velocity
    __default_fiber_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity'), 'default_fiber_velocity', '__AbsentNamespace0_Millard2012AccelerationMuscle_default_fiber_velocity', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 124, 8), )

    
    default_fiber_velocity = property(__default_fiber_velocity.value, __default_fiber_velocity.set, None, None)

    
    # Element MuscleFirstOrderActivationDynamicModel uses Python identifier MuscleFirstOrderActivationDynamicModel
    __MuscleFirstOrderActivationDynamicModel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel'), 'MuscleFirstOrderActivationDynamicModel', '__AbsentNamespace0_Millard2012AccelerationMuscle_MuscleFirstOrderActivationDynamicModel', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 125, 8), )

    
    MuscleFirstOrderActivationDynamicModel = property(__MuscleFirstOrderActivationDynamicModel.value, __MuscleFirstOrderActivationDynamicModel.set, None, 'Activation dynamics model with a lower boundactivation.')

    
    # Element fiber_damping uses Python identifier fiber_damping
    __fiber_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fiber_damping'), 'fiber_damping', '__AbsentNamespace0_Millard2012AccelerationMuscle_fiber_damping', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 139, 8), )

    
    fiber_damping = property(__fiber_damping.value, __fiber_damping.set, None, None)

    
    # Element fiber_force_length_damping uses Python identifier fiber_force_length_damping
    __fiber_force_length_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fiber_force_length_damping'), 'fiber_force_length_damping', '__AbsentNamespace0_Millard2012AccelerationMuscle_fiber_force_length_damping', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 140, 8), )

    
    fiber_force_length_damping = property(__fiber_force_length_damping.value, __fiber_force_length_damping.set, None, None)

    
    # Element fiber_compressive_force_length_damping uses Python identifier fiber_compressive_force_length_damping
    __fiber_compressive_force_length_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fiber_compressive_force_length_damping'), 'fiber_compressive_force_length_damping', '__AbsentNamespace0_Millard2012AccelerationMuscle_fiber_compressive_force_length_damping', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 141, 8), )

    
    fiber_compressive_force_length_damping = property(__fiber_compressive_force_length_damping.value, __fiber_compressive_force_length_damping.set, None, None)

    
    # Element fiber_compressive_force_cos_pennation_damping uses Python identifier fiber_compressive_force_cos_pennation_damping
    __fiber_compressive_force_cos_pennation_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fiber_compressive_force_cos_pennation_damping'), 'fiber_compressive_force_cos_pennation_damping', '__AbsentNamespace0_Millard2012AccelerationMuscle_fiber_compressive_force_cos_pennation_damping', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 142, 8), )

    
    fiber_compressive_force_cos_pennation_damping = property(__fiber_compressive_force_cos_pennation_damping.value, __fiber_compressive_force_cos_pennation_damping.set, None, None)

    
    # Element tendon_force_length_damping uses Python identifier tendon_force_length_damping
    __tendon_force_length_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tendon_force_length_damping'), 'tendon_force_length_damping', '__AbsentNamespace0_Millard2012AccelerationMuscle_tendon_force_length_damping', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 143, 8), )

    
    tendon_force_length_damping = property(__tendon_force_length_damping.value, __tendon_force_length_damping.set, None, None)

    
    # Element mass uses Python identifier mass
    __mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mass'), 'mass', '__AbsentNamespace0_Millard2012AccelerationMuscle_mass', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 144, 8), )

    
    mass = property(__mass.value, __mass.set, None, None)

    
    # Element GeometryPath uses Python identifier GeometryPath
    __GeometryPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), 'GeometryPath', '__AbsentNamespace0_Millard2012AccelerationMuscle_GeometryPath', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2), )

    
    GeometryPath = property(__GeometryPath.value, __GeometryPath.set, None, 'The set of points defining the path of the muscle.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Millard2012AccelerationMuscle_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 146, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 146, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __optimal_force.name() : __optimal_force,
        __max_isometric_force.name() : __max_isometric_force,
        __min_control.name() : __min_control,
        __max_control.name() : __max_control,
        __optimal_fiber_length.name() : __optimal_fiber_length,
        __tendon_slack_length.name() : __tendon_slack_length,
        __pennation_angle_at_optimal.name() : __pennation_angle_at_optimal,
        __max_contraction_velocity.name() : __max_contraction_velocity,
        __ignore_tendon_compliance.name() : __ignore_tendon_compliance,
        __ignore_activation_dynamics.name() : __ignore_activation_dynamics,
        __default_activation.name() : __default_activation,
        __default_fiber_length.name() : __default_fiber_length,
        __default_fiber_velocity.name() : __default_fiber_velocity,
        __MuscleFirstOrderActivationDynamicModel.name() : __MuscleFirstOrderActivationDynamicModel,
        __fiber_damping.name() : __fiber_damping,
        __fiber_force_length_damping.name() : __fiber_force_length_damping,
        __fiber_compressive_force_length_damping.name() : __fiber_compressive_force_length_damping,
        __fiber_compressive_force_cos_pennation_damping.name() : __fiber_compressive_force_cos_pennation_damping,
        __tendon_force_length_damping.name() : __tendon_force_length_damping,
        __mass.name() : __mass,
        __GeometryPath.name() : __GeometryPath
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.Millard2012AccelerationMuscle = Millard2012AccelerationMuscle
Namespace.addCategoryObject('typeBinding', 'Millard2012AccelerationMuscle', Millard2012AccelerationMuscle)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Activation dynamics model with a lower boundactivation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 129, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element minimum_activation uses Python identifier minimum_activation
    __minimum_activation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'minimum_activation'), 'minimum_activation', '__AbsentNamespace0_CTD_ANON_6_minimum_activation', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 131, 14), )

    
    minimum_activation = property(__minimum_activation.value, __minimum_activation.set, None, 'Activation lower bound.')

    _ElementMap.update({
        __minimum_activation.name() : __minimum_activation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type Thelen2003Muscle with content type ELEMENT_ONLY
class Thelen2003Muscle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Thelen2003Muscle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Thelen2003Muscle')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 149, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element optimal_force uses Python identifier optimal_force
    __optimal_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_force'), 'optimal_force', '__AbsentNamespace0_Thelen2003Muscle_optimal_force', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4), )

    
    optimal_force = property(__optimal_force.value, __optimal_force.set, None, None)

    
    # Element max_isometric_force uses Python identifier max_isometric_force
    __max_isometric_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), 'max_isometric_force', '__AbsentNamespace0_Thelen2003Muscle_max_isometric_force', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4), )

    
    max_isometric_force = property(__max_isometric_force.value, __max_isometric_force.set, None, 'Maximum isometric force that the fibers can generate.')

    
    # Element min_control uses Python identifier min_control
    __min_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_control'), 'min_control', '__AbsentNamespace0_Thelen2003Muscle_min_control', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4), )

    
    min_control = property(__min_control.value, __min_control.set, None, None)

    
    # Element max_control uses Python identifier max_control
    __max_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_control'), 'max_control', '__AbsentNamespace0_Thelen2003Muscle_max_control', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4), )

    
    max_control = property(__max_control.value, __max_control.set, None, 'Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.')

    
    # Element optimal_fiber_length uses Python identifier optimal_fiber_length
    __optimal_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), 'optimal_fiber_length', '__AbsentNamespace0_Thelen2003Muscle_optimal_fiber_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4), )

    
    optimal_fiber_length = property(__optimal_fiber_length.value, __optimal_fiber_length.set, None, 'Optimal length of the muscle fibers.')

    
    # Element tendon_slack_length uses Python identifier tendon_slack_length
    __tendon_slack_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), 'tendon_slack_length', '__AbsentNamespace0_Thelen2003Muscle_tendon_slack_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4), )

    
    tendon_slack_length = property(__tendon_slack_length.value, __tendon_slack_length.set, None, 'Resting length of the tendonResting length of the tendon.')

    
    # Element pennation_angle_at_optimal uses Python identifier pennation_angle_at_optimal
    __pennation_angle_at_optimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), 'pennation_angle_at_optimal', '__AbsentNamespace0_Thelen2003Muscle_pennation_angle_at_optimal', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4), )

    
    pennation_angle_at_optimal = property(__pennation_angle_at_optimal.value, __pennation_angle_at_optimal.set, None, 'Angle between tendon and fibers at optimal fiber length expressed in radians.')

    
    # Element max_contraction_velocity uses Python identifier max_contraction_velocity
    __max_contraction_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity'), 'max_contraction_velocity', '__AbsentNamespace0_Thelen2003Muscle_max_contraction_velocity', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4), )

    
    max_contraction_velocity = property(__max_contraction_velocity.value, __max_contraction_velocity.set, None, None)

    
    # Element ignore_tendon_compliance uses Python identifier ignore_tendon_compliance
    __ignore_tendon_compliance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance'), 'ignore_tendon_compliance', '__AbsentNamespace0_Thelen2003Muscle_ignore_tendon_compliance', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4), )

    
    ignore_tendon_compliance = property(__ignore_tendon_compliance.value, __ignore_tendon_compliance.set, None, None)

    
    # Element ignore_activation_dynamics uses Python identifier ignore_activation_dynamics
    __ignore_activation_dynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics'), 'ignore_activation_dynamics', '__AbsentNamespace0_Thelen2003Muscle_ignore_activation_dynamics', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4), )

    
    ignore_activation_dynamics = property(__ignore_activation_dynamics.value, __ignore_activation_dynamics.set, None, None)

    
    # Element activation_time_constant uses Python identifier activation_time_constant
    __activation_time_constant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'activation_time_constant'), 'activation_time_constant', '__AbsentNamespace0_Thelen2003Muscle_activation_time_constant', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 152, 6), )

    
    activation_time_constant = property(__activation_time_constant.value, __activation_time_constant.set, None, None)

    
    # Element deactivation_time_constant uses Python identifier deactivation_time_constant
    __deactivation_time_constant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deactivation_time_constant'), 'deactivation_time_constant', '__AbsentNamespace0_Thelen2003Muscle_deactivation_time_constant', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 153, 6), )

    
    deactivation_time_constant = property(__deactivation_time_constant.value, __deactivation_time_constant.set, None, None)

    
    # Element FmaxTendonStrain uses Python identifier FmaxTendonStrain
    __FmaxTendonStrain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FmaxTendonStrain'), 'FmaxTendonStrain', '__AbsentNamespace0_Thelen2003Muscle_FmaxTendonStrain', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 154, 6), )

    
    FmaxTendonStrain = property(__FmaxTendonStrain.value, __FmaxTendonStrain.set, None, None)

    
    # Element FmaxMuscleStrain uses Python identifier FmaxMuscleStrain
    __FmaxMuscleStrain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'FmaxMuscleStrain'), 'FmaxMuscleStrain', '__AbsentNamespace0_Thelen2003Muscle_FmaxMuscleStrain', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 155, 6), )

    
    FmaxMuscleStrain = property(__FmaxMuscleStrain.value, __FmaxMuscleStrain.set, None, None)

    
    # Element KshapeActive uses Python identifier KshapeActive
    __KshapeActive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'KshapeActive'), 'KshapeActive', '__AbsentNamespace0_Thelen2003Muscle_KshapeActive', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 156, 6), )

    
    KshapeActive = property(__KshapeActive.value, __KshapeActive.set, None, None)

    
    # Element KshapePassive uses Python identifier KshapePassive
    __KshapePassive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'KshapePassive'), 'KshapePassive', '__AbsentNamespace0_Thelen2003Muscle_KshapePassive', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 157, 6), )

    
    KshapePassive = property(__KshapePassive.value, __KshapePassive.set, None, None)

    
    # Element Af uses Python identifier Af
    __Af = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Af'), 'Af', '__AbsentNamespace0_Thelen2003Muscle_Af', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 158, 6), )

    
    Af = property(__Af.value, __Af.set, None, None)

    
    # Element Flen uses Python identifier Flen
    __Flen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Flen'), 'Flen', '__AbsentNamespace0_Thelen2003Muscle_Flen', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 159, 6), )

    
    Flen = property(__Flen.value, __Flen.set, None, None)

    
    # Element fv_linear_extrap_threshold uses Python identifier fv_linear_extrap_threshold
    __fv_linear_extrap_threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fv_linear_extrap_threshold'), 'fv_linear_extrap_threshold', '__AbsentNamespace0_Thelen2003Muscle_fv_linear_extrap_threshold', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 160, 6), )

    
    fv_linear_extrap_threshold = property(__fv_linear_extrap_threshold.value, __fv_linear_extrap_threshold.set, None, None)

    
    # Element GeometryPath uses Python identifier GeometryPath
    __GeometryPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), 'GeometryPath', '__AbsentNamespace0_Thelen2003Muscle_GeometryPath', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2), )

    
    GeometryPath = property(__GeometryPath.value, __GeometryPath.set, None, 'The set of points defining the path of the muscle.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Thelen2003Muscle_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 162, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 162, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __optimal_force.name() : __optimal_force,
        __max_isometric_force.name() : __max_isometric_force,
        __min_control.name() : __min_control,
        __max_control.name() : __max_control,
        __optimal_fiber_length.name() : __optimal_fiber_length,
        __tendon_slack_length.name() : __tendon_slack_length,
        __pennation_angle_at_optimal.name() : __pennation_angle_at_optimal,
        __max_contraction_velocity.name() : __max_contraction_velocity,
        __ignore_tendon_compliance.name() : __ignore_tendon_compliance,
        __ignore_activation_dynamics.name() : __ignore_activation_dynamics,
        __activation_time_constant.name() : __activation_time_constant,
        __deactivation_time_constant.name() : __deactivation_time_constant,
        __FmaxTendonStrain.name() : __FmaxTendonStrain,
        __FmaxMuscleStrain.name() : __FmaxMuscleStrain,
        __KshapeActive.name() : __KshapeActive,
        __KshapePassive.name() : __KshapePassive,
        __Af.name() : __Af,
        __Flen.name() : __Flen,
        __fv_linear_extrap_threshold.name() : __fv_linear_extrap_threshold,
        __GeometryPath.name() : __GeometryPath
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.Thelen2003Muscle = Thelen2003Muscle
Namespace.addCategoryObject('typeBinding', 'Thelen2003Muscle', Thelen2003Muscle)


# Complex type RigidTendonMuscle with content type ELEMENT_ONLY
class RigidTendonMuscle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RigidTendonMuscle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RigidTendonMuscle')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 165, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element optimal_force uses Python identifier optimal_force
    __optimal_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_force'), 'optimal_force', '__AbsentNamespace0_RigidTendonMuscle_optimal_force', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4), )

    
    optimal_force = property(__optimal_force.value, __optimal_force.set, None, None)

    
    # Element max_isometric_force uses Python identifier max_isometric_force
    __max_isometric_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), 'max_isometric_force', '__AbsentNamespace0_RigidTendonMuscle_max_isometric_force', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4), )

    
    max_isometric_force = property(__max_isometric_force.value, __max_isometric_force.set, None, 'Maximum isometric force that the fibers can generate.')

    
    # Element min_control uses Python identifier min_control
    __min_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_control'), 'min_control', '__AbsentNamespace0_RigidTendonMuscle_min_control', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4), )

    
    min_control = property(__min_control.value, __min_control.set, None, None)

    
    # Element max_control uses Python identifier max_control
    __max_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_control'), 'max_control', '__AbsentNamespace0_RigidTendonMuscle_max_control', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4), )

    
    max_control = property(__max_control.value, __max_control.set, None, 'Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.')

    
    # Element optimal_fiber_length uses Python identifier optimal_fiber_length
    __optimal_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), 'optimal_fiber_length', '__AbsentNamespace0_RigidTendonMuscle_optimal_fiber_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4), )

    
    optimal_fiber_length = property(__optimal_fiber_length.value, __optimal_fiber_length.set, None, 'Optimal length of the muscle fibers.')

    
    # Element tendon_slack_length uses Python identifier tendon_slack_length
    __tendon_slack_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), 'tendon_slack_length', '__AbsentNamespace0_RigidTendonMuscle_tendon_slack_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4), )

    
    tendon_slack_length = property(__tendon_slack_length.value, __tendon_slack_length.set, None, 'Resting length of the tendonResting length of the tendon.')

    
    # Element pennation_angle_at_optimal uses Python identifier pennation_angle_at_optimal
    __pennation_angle_at_optimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), 'pennation_angle_at_optimal', '__AbsentNamespace0_RigidTendonMuscle_pennation_angle_at_optimal', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4), )

    
    pennation_angle_at_optimal = property(__pennation_angle_at_optimal.value, __pennation_angle_at_optimal.set, None, 'Angle between tendon and fibers at optimal fiber length expressed in radians.')

    
    # Element max_contraction_velocity uses Python identifier max_contraction_velocity
    __max_contraction_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity'), 'max_contraction_velocity', '__AbsentNamespace0_RigidTendonMuscle_max_contraction_velocity', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4), )

    
    max_contraction_velocity = property(__max_contraction_velocity.value, __max_contraction_velocity.set, None, None)

    
    # Element ignore_tendon_compliance uses Python identifier ignore_tendon_compliance
    __ignore_tendon_compliance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance'), 'ignore_tendon_compliance', '__AbsentNamespace0_RigidTendonMuscle_ignore_tendon_compliance', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4), )

    
    ignore_tendon_compliance = property(__ignore_tendon_compliance.value, __ignore_tendon_compliance.set, None, None)

    
    # Element ignore_activation_dynamics uses Python identifier ignore_activation_dynamics
    __ignore_activation_dynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics'), 'ignore_activation_dynamics', '__AbsentNamespace0_RigidTendonMuscle_ignore_activation_dynamics', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4), )

    
    ignore_activation_dynamics = property(__ignore_activation_dynamics.value, __ignore_activation_dynamics.set, None, None)

    
    # Element GeometryPath uses Python identifier GeometryPath
    __GeometryPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), 'GeometryPath', '__AbsentNamespace0_RigidTendonMuscle_GeometryPath', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2), )

    
    GeometryPath = property(__GeometryPath.value, __GeometryPath.set, None, 'The set of points defining the path of the muscle.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_RigidTendonMuscle_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 169, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 169, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __optimal_force.name() : __optimal_force,
        __max_isometric_force.name() : __max_isometric_force,
        __min_control.name() : __min_control,
        __max_control.name() : __max_control,
        __optimal_fiber_length.name() : __optimal_fiber_length,
        __tendon_slack_length.name() : __tendon_slack_length,
        __pennation_angle_at_optimal.name() : __pennation_angle_at_optimal,
        __max_contraction_velocity.name() : __max_contraction_velocity,
        __ignore_tendon_compliance.name() : __ignore_tendon_compliance,
        __ignore_activation_dynamics.name() : __ignore_activation_dynamics,
        __GeometryPath.name() : __GeometryPath
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.RigidTendonMuscle = RigidTendonMuscle
Namespace.addCategoryObject('typeBinding', 'RigidTendonMuscle', RigidTendonMuscle)


# Complex type MyoroboticsMuscle with content type ELEMENT_ONLY
class MyoroboticsMuscle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MyoroboticsMuscle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MyoroboticsMuscle')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 172, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element GeometryPath uses Python identifier GeometryPath
    __GeometryPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), 'GeometryPath', '__AbsentNamespace0_MyoroboticsMuscle_GeometryPath', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2), )

    
    GeometryPath = property(__GeometryPath.value, __GeometryPath.set, None, 'The set of points defining the path of the muscle.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_MyoroboticsMuscle_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 178, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 178, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __GeometryPath.name() : __GeometryPath
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.MyoroboticsMuscle = MyoroboticsMuscle
Namespace.addCategoryObject('typeBinding', 'MyoroboticsMuscle', MyoroboticsMuscle)


# Complex type WrapCylinder with content type ELEMENT_ONLY
class WrapCylinder (pyxb.binding.basis.complexTypeDefinition):
    """Complex type WrapCylinder with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WrapCylinder')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 181, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element xyz_body_rotation uses Python identifier xyz_body_rotation
    __xyz_body_rotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xyz_body_rotation'), 'xyz_body_rotation', '__AbsentNamespace0_WrapCylinder_xyz_body_rotation', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 183, 6), )

    
    xyz_body_rotation = property(__xyz_body_rotation.value, __xyz_body_rotation.set, None, None)

    
    # Element translation uses Python identifier translation
    __translation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'translation'), 'translation', '__AbsentNamespace0_WrapCylinder_translation', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 184, 6), )

    
    translation = property(__translation.value, __translation.set, None, None)

    
    # Element active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'active'), 'active', '__AbsentNamespace0_WrapCylinder_active', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 185, 6), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_WrapCylinder_radius', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 186, 6), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Element length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_WrapCylinder_length', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 187, 6), )

    
    length = property(__length.value, __length.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_WrapCylinder_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 189, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 189, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __xyz_body_rotation.name() : __xyz_body_rotation,
        __translation.name() : __translation,
        __active.name() : __active,
        __radius.name() : __radius,
        __length.name() : __length
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.WrapCylinder = WrapCylinder
Namespace.addCategoryObject('typeBinding', 'WrapCylinder', WrapCylinder)


# Complex type WrapSphere with content type ELEMENT_ONLY
class WrapSphere (pyxb.binding.basis.complexTypeDefinition):
    """Complex type WrapSphere with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WrapSphere')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 192, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element translation uses Python identifier translation
    __translation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'translation'), 'translation', '__AbsentNamespace0_WrapSphere_translation', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 194, 6), )

    
    translation = property(__translation.value, __translation.set, None, None)

    
    # Element active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'active'), 'active', '__AbsentNamespace0_WrapSphere_active', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 195, 6), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element radius uses Python identifier radius
    __radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_WrapSphere_radius', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 196, 6), )

    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_WrapSphere_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 198, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 198, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __translation.name() : __translation,
        __active.name() : __active,
        __radius.name() : __radius
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.WrapSphere = WrapSphere
Namespace.addCategoryObject('typeBinding', 'WrapSphere', WrapSphere)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """The set of points defining the path of the muscle."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 205, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PathPointSet uses Python identifier PathPointSet
    __PathPointSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PathPointSet'), 'PathPointSet', '__AbsentNamespace0_CTD_ANON_7_PathPointSet', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 207, 8), )

    
    PathPointSet = property(__PathPointSet.value, __PathPointSet.set, None, None)

    
    # Element PathWrapSet uses Python identifier PathWrapSet
    __PathWrapSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PathWrapSet'), 'PathWrapSet', '__AbsentNamespace0_CTD_ANON_7_PathWrapSet', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 221, 2), )

    
    PathWrapSet = property(__PathWrapSet.value, __PathWrapSet.set, None, None)

    _ElementMap.update({
        __PathPointSet.name() : __PathPointSet,
        __PathWrapSet.name() : __PathWrapSet
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
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 208, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objects uses Python identifier objects
    __objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objects'), 'objects', '__AbsentNamespace0_CTD_ANON_8_objects', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 210, 14), )

    
    objects = property(__objects.value, __objects.set, None, None)

    
    # Element groups uses Python identifier groups
    __groups = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'groups'), 'groups', '__AbsentNamespace0_CTD_ANON_8_groups', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 217, 14), )

    
    groups = property(__groups.value, __groups.set, None, None)

    _ElementMap.update({
        __objects.name() : __objects,
        __groups.name() : __groups
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 211, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PathPoint uses Python identifier PathPoint
    __PathPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PathPoint'), 'PathPoint', '__AbsentNamespace0_CTD_ANON_9_PathPoint', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 248, 2), )

    
    PathPoint = property(__PathPoint.value, __PathPoint.set, None, None)

    _ElementMap.update({
        __PathPoint.name() : __PathPoint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 222, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objects uses Python identifier objects
    __objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objects'), 'objects', '__AbsentNamespace0_CTD_ANON_10_objects', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 224, 4), )

    
    objects = property(__objects.value, __objects.set, None, None)

    _ElementMap.update({
        __objects.name() : __objects
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 225, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PathWrap uses Python identifier PathWrap
    __PathWrap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PathWrap'), 'PathWrap', '__AbsentNamespace0_CTD_ANON_11_PathWrap', True, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 238, 2), )

    
    PathWrap = property(__PathWrap.value, __PathWrap.set, None, None)

    _ElementMap.update({
        __PathWrap.name() : __PathWrap
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 239, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element wrap_object uses Python identifier wrap_object
    __wrap_object = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'wrap_object'), 'wrap_object', '__AbsentNamespace0_CTD_ANON_12_wrap_object', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 241, 2), )

    
    wrap_object = property(__wrap_object.value, __wrap_object.set, None, None)

    
    # Element method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'method'), 'method', '__AbsentNamespace0_CTD_ANON_12_method', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 242, 2), )

    
    method = property(__method.value, __method.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_12_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 244, 3)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 244, 3)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __wrap_object.name() : __wrap_object,
        __method.name() : __method
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 249, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_CTD_ANON_13_location', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 251, 8), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element body uses Python identifier body
    __body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'body'), 'body', '__AbsentNamespace0_CTD_ANON_13_body', False, pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 252, 8), )

    
    body = property(__body.value, __body.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_13_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 254, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 254, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __location.name() : __location,
        __body.name() : __body
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


OpenSimDocument = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpenSimDocument'), CTD_ANON, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', OpenSimDocument.name().localName(), OpenSimDocument)

GeometryPath = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_7, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2))
Namespace.addCategoryObject('elementBinding', GeometryPath.name().localName(), GeometryPath)

PathWrap = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PathWrap'), CTD_ANON_12, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 238, 2))
Namespace.addCategoryObject('elementBinding', PathWrap.name().localName(), PathWrap)

PathPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PathPoint'), CTD_ANON_13, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 248, 2))
Namespace.addCategoryObject('elementBinding', PathPoint.name().localName(), PathPoint)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Model'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 7, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Model')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 7, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ForceSet'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 10, 14)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BodySet'), BodySet, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 27, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 27, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'ForceSet')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 10, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'BodySet')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 27, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objects'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 13, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'objects')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 13, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Millard2012EquilibriumMuscle'), Millard2012EquilibriumMuscle, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 16, 26)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Millard2012AccelerationMuscle'), Millard2012AccelerationMuscle, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 17, 26)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Thelen2003Muscle'), Thelen2003Muscle, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 18, 26)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RigidTendonMuscle'), RigidTendonMuscle, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 19, 26)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MyoroboticsMuscle'), MyoroboticsMuscle, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 20, 26)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 15, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'Millard2012EquilibriumMuscle')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 16, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'Millard2012AccelerationMuscle')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 17, 26))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'Thelen2003Muscle')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 18, 26))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'RigidTendonMuscle')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 19, 26))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'MyoroboticsMuscle')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 20, 26))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




BodySet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objects'), CTD_ANON_4, scope=BodySet, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 74, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BodySet._UseForTag(pyxb.namespace.ExpandedName(None, 'objects')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 74, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BodySet._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Body'), Body, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 77, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 77, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'Body')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 77, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




Body._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'WrapObjectSet'), WrapObjectSet, scope=Body, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 87, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 87, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Body._UseForTag(pyxb.namespace.ExpandedName(None, 'WrapObjectSet')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 87, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Body._Automaton = _BuildAutomaton_6()




WrapObjectSet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objects'), CTD_ANON_5, scope=WrapObjectSet, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 94, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WrapObjectSet._UseForTag(pyxb.namespace.ExpandedName(None, 'objects')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 94, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WrapObjectSet._Automaton = _BuildAutomaton_7()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'WrapCylinder'), WrapCylinder, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 97, 12)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'WrapSphere'), WrapSphere, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 98, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 96, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'WrapCylinder')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 97, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'WrapSphere')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 98, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_8()




Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_force'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Maximum isometric force that the fibers can generate.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_control'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_control'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Optimal length of the muscle fibers.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Resting length of the tendonResting length of the tendon.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Angle between tendon and fibers at optimal fiber length expressed in radians.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fiber_damping'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 109, 8)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_activation'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 110, 8)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_fiber_length'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 111, 8)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'activation_time_constant'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 112, 8)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deactivation_time_constant'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 113, 8)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'minimum_activation'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 114, 8)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_7, scope=Millard2012EquilibriumMuscle, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 109, 8))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 110, 8))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 111, 8))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 112, 8))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 113, 8))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 114, 8))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 38, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_force')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_isometric_force')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'min_control')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_control')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'tendon_slack_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'fiber_damping')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 109, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_activation')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 110, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_fiber_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 111, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'activation_time_constant')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 112, 8))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'deactivation_time_constant')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 113, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'minimum_activation')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 114, 8))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Millard2012EquilibriumMuscle._Automaton = _BuildAutomaton_9()




Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_force'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Maximum isometric force that the fibers can generate.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_control'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_control'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Optimal length of the muscle fibers.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Resting length of the tendonResting length of the tendon.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Angle between tendon and fibers at optimal fiber length expressed in radians.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_activation'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 122, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_fiber_length'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 123, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 124, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel'), CTD_ANON_6, scope=Millard2012AccelerationMuscle, documentation='Activation dynamics model with a lower boundactivation.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 125, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fiber_damping'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 139, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fiber_force_length_damping'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 140, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fiber_compressive_force_length_damping'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 141, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fiber_compressive_force_cos_pennation_damping'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 142, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tendon_force_length_damping'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 143, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mass'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 144, 8)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_7, scope=Millard2012AccelerationMuscle, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 122, 8))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 123, 8))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 124, 8))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 125, 8))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 139, 8))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 140, 8))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 141, 8))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 142, 8))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 143, 8))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 144, 8))
    counters.add(cc_16)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 38, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_force')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_isometric_force')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'min_control')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_control')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'tendon_slack_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_activation')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 122, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_fiber_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 123, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 124, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 125, 8))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'fiber_damping')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 139, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'fiber_force_length_damping')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 140, 8))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'fiber_compressive_force_length_damping')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 141, 8))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'fiber_compressive_force_cos_pennation_damping')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 142, 8))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'tendon_force_length_damping')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 143, 8))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'mass')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 144, 8))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
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
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
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
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Millard2012AccelerationMuscle._Automaton = _BuildAutomaton_10()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'minimum_activation'), pyxb.binding.datatypes.float, scope=CTD_ANON_6, documentation='Activation lower bound.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 131, 14)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'minimum_activation')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 131, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_11()




Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_force'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, documentation='Maximum isometric force that the fibers can generate.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_control'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_control'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, documentation='Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, documentation='Optimal length of the muscle fibers.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, documentation='Resting length of the tendonResting length of the tendon.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, documentation='Angle between tendon and fibers at optimal fiber length expressed in radians.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'activation_time_constant'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 152, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deactivation_time_constant'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 153, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FmaxTendonStrain'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 154, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'FmaxMuscleStrain'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 155, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'KshapeActive'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 156, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'KshapePassive'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 157, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Af'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 158, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Flen'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 159, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fv_linear_extrap_threshold'), pyxb.binding.datatypes.float, scope=Thelen2003Muscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 160, 6)))

Thelen2003Muscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_7, scope=Thelen2003Muscle, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 152, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 153, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 154, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 155, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 156, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 157, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 158, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 159, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 160, 6))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 38, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_force')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_isometric_force')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'min_control')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_control')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'tendon_slack_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'activation_time_constant')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 152, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'deactivation_time_constant')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 153, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'FmaxTendonStrain')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 154, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'FmaxMuscleStrain')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 155, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'KshapeActive')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 156, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'KshapePassive')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 157, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'Af')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 158, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'Flen')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 159, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(Thelen2003Muscle._UseForTag(pyxb.namespace.ExpandedName(None, 'fv_linear_extrap_threshold')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 160, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
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
    transitions.append(fac.Transition(st_19, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
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
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Thelen2003Muscle._Automaton = _BuildAutomaton_12()




RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_force'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, documentation='Maximum isometric force that the fibers can generate.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_control'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_control'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, documentation='Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, documentation='Optimal length of the muscle fibers.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, documentation='Resting length of the tendonResting length of the tendon.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, documentation='Angle between tendon and fibers at optimal fiber length expressed in radians.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics'), pyxb.binding.datatypes.float, scope=RigidTendonMuscle, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4)))

RigidTendonMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_7, scope=RigidTendonMuscle, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 38, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_force')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 39, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_isometric_force')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 40, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'min_control')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 45, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_control')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 46, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 51, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'tendon_slack_length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 56, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 61, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_contraction_velocity')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 66, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore_tendon_compliance')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 67, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RigidTendonMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore_activation_dynamics')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 68, 4))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RigidTendonMuscle._Automaton = _BuildAutomaton_13()




MyoroboticsMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_7, scope=MyoroboticsMuscle, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 201, 2)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MyoroboticsMuscle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 175, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MyoroboticsMuscle._Automaton = _BuildAutomaton_14()




WrapCylinder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xyz_body_rotation'), vector3, scope=WrapCylinder, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 183, 6)))

WrapCylinder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'translation'), vector3, scope=WrapCylinder, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 184, 6)))

WrapCylinder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'active'), pyxb.binding.datatypes.string, scope=WrapCylinder, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 185, 6)))

WrapCylinder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), pyxb.binding.datatypes.float, scope=WrapCylinder, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 186, 6)))

WrapCylinder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'length'), pyxb.binding.datatypes.float, scope=WrapCylinder, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 187, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WrapCylinder._UseForTag(pyxb.namespace.ExpandedName(None, 'xyz_body_rotation')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 183, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WrapCylinder._UseForTag(pyxb.namespace.ExpandedName(None, 'translation')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 184, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WrapCylinder._UseForTag(pyxb.namespace.ExpandedName(None, 'active')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 185, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WrapCylinder._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 186, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WrapCylinder._UseForTag(pyxb.namespace.ExpandedName(None, 'length')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 187, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WrapCylinder._Automaton = _BuildAutomaton_15()




WrapSphere._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'translation'), vector3, scope=WrapSphere, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 194, 6)))

WrapSphere._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'active'), pyxb.binding.datatypes.string, scope=WrapSphere, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 195, 6)))

WrapSphere._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radius'), pyxb.binding.datatypes.float, scope=WrapSphere, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 196, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WrapSphere._UseForTag(pyxb.namespace.ExpandedName(None, 'translation')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 194, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WrapSphere._UseForTag(pyxb.namespace.ExpandedName(None, 'active')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 195, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WrapSphere._UseForTag(pyxb.namespace.ExpandedName(None, 'radius')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 196, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WrapSphere._Automaton = _BuildAutomaton_16()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PathPointSet'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 207, 8)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PathWrapSet'), CTD_ANON_10, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 221, 2)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 221, 2))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'PathPointSet')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 207, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, 'PathWrapSet')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 221, 2))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_17()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objects'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 210, 14)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'groups'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 217, 14)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 217, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'objects')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 210, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'groups')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 217, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_18()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PathPoint'), CTD_ANON_13, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 248, 2)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 212, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PathPoint')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 213, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_19()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objects'), CTD_ANON_11, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 224, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'objects')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 224, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_20()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PathWrap'), CTD_ANON_12, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 238, 2)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 226, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PathWrap')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 227, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_21()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'wrap_object'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 241, 2)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'method'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 242, 2)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'wrap_object')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 241, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, 'method')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 242, 2))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_22()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), vector3, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 251, 8)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'body'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 252, 8)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 251, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, 'body')), pyxb.utils.utility.Location('/home/user/CODE/NRP/RobotDesigner/CODE/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles_new.xsd', 252, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_23()

