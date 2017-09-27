# ./robot_designer_plugin/export/osim/osim_dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-09-27 11:40:58.781173 by PyXB version 1.2.5 using Python 3.5.2.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f77ec00c-a367-11e7-8362-4ccc6ab01b83')

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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 140, 2)
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 5, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Model'), 'Model', '__AbsentNamespace0_CTD_ANON_Model', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 7, 8), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__AbsentNamespace0_CTD_ANON_Version', pyxb.binding.datatypes.string)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 28, 6)
    __Version._UseLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 28, 6)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 8, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ForceSet uses Python identifier ForceSet
    __ForceSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ForceSet'), 'ForceSet', '__AbsentNamespace0_CTD_ANON__ForceSet', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 10, 14), )

    
    ForceSet = property(__ForceSet.value, __ForceSet.set, None, None)

    _ElementMap.update({
        __ForceSet.name() : __ForceSet
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 11, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objects uses Python identifier objects
    __objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objects'), 'objects', '__AbsentNamespace0_CTD_ANON_2_objects', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 13, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 14, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Millard2012EquilibriumMuscle uses Python identifier Millard2012EquilibriumMuscle
    __Millard2012EquilibriumMuscle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Millard2012EquilibriumMuscle'), 'Millard2012EquilibriumMuscle', '__AbsentNamespace0_CTD_ANON_3_Millard2012EquilibriumMuscle', True, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 16, 26), )

    
    Millard2012EquilibriumMuscle = property(__Millard2012EquilibriumMuscle.value, __Millard2012EquilibriumMuscle.set, None, None)

    
    # Element Millard2012AccelerationMuscle uses Python identifier Millard2012AccelerationMuscle
    __Millard2012AccelerationMuscle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Millard2012AccelerationMuscle'), 'Millard2012AccelerationMuscle', '__AbsentNamespace0_CTD_ANON_3_Millard2012AccelerationMuscle', True, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 17, 26), )

    
    Millard2012AccelerationMuscle = property(__Millard2012AccelerationMuscle.value, __Millard2012AccelerationMuscle.set, None, None)

    _ElementMap.update({
        __Millard2012EquilibriumMuscle.name() : __Millard2012EquilibriumMuscle,
        __Millard2012AccelerationMuscle.name() : __Millard2012AccelerationMuscle
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Activation dynamics model with a lower boundactivation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 77, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element minimum_activation uses Python identifier minimum_activation
    __minimum_activation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'minimum_activation'), 'minimum_activation', '__AbsentNamespace0_CTD_ANON_4_minimum_activation', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 79, 12), )

    
    minimum_activation = property(__minimum_activation.value, __minimum_activation.set, None, 'Activation lower bound.')

    _ElementMap.update({
        __minimum_activation.name() : __minimum_activation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type Millard2012EquilibriumMuscle with content type ELEMENT_ONLY
class Millard2012EquilibriumMuscle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Millard2012EquilibriumMuscle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Millard2012EquilibriumMuscle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element max_isometric_force uses Python identifier max_isometric_force
    __max_isometric_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), 'max_isometric_force', '__AbsentNamespace0_Millard2012EquilibriumMuscle_max_isometric_force', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 35, 4), )

    
    max_isometric_force = property(__max_isometric_force.value, __max_isometric_force.set, None, 'Maximum isometric force that the fibers can generate.')

    
    # Element min_control uses Python identifier min_control
    __min_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_control'), 'min_control', '__AbsentNamespace0_Millard2012EquilibriumMuscle_min_control', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 40, 4), )

    
    min_control = property(__min_control.value, __min_control.set, None, None)

    
    # Element max_control uses Python identifier max_control
    __max_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_control'), 'max_control', '__AbsentNamespace0_Millard2012EquilibriumMuscle_max_control', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 41, 4), )

    
    max_control = property(__max_control.value, __max_control.set, None, 'Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.')

    
    # Element optimal_fiber_length uses Python identifier optimal_fiber_length
    __optimal_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), 'optimal_fiber_length', '__AbsentNamespace0_Millard2012EquilibriumMuscle_optimal_fiber_length', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 46, 4), )

    
    optimal_fiber_length = property(__optimal_fiber_length.value, __optimal_fiber_length.set, None, 'Optimal length of the muscle fibers.')

    
    # Element tendon_slack_length uses Python identifier tendon_slack_length
    __tendon_slack_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), 'tendon_slack_length', '__AbsentNamespace0_Millard2012EquilibriumMuscle_tendon_slack_length', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 51, 4), )

    
    tendon_slack_length = property(__tendon_slack_length.value, __tendon_slack_length.set, None, 'Resting length of the tendonResting length of the tendon.')

    
    # Element pennation_angle_at_optimal uses Python identifier pennation_angle_at_optimal
    __pennation_angle_at_optimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), 'pennation_angle_at_optimal', '__AbsentNamespace0_Millard2012EquilibriumMuscle_pennation_angle_at_optimal', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 56, 4), )

    
    pennation_angle_at_optimal = property(__pennation_angle_at_optimal.value, __pennation_angle_at_optimal.set, None, 'Angle between tendon and fibers at optimal fiber length expressed in radians.')

    
    # Element fiber_damping uses Python identifier fiber_damping
    __fiber_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fiber_damping'), 'fiber_damping', '__AbsentNamespace0_Millard2012EquilibriumMuscle_fiber_damping', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 66, 6), )

    
    fiber_damping = property(__fiber_damping.value, __fiber_damping.set, None, None)

    
    # Element default_fiber_velocity uses Python identifier default_fiber_velocity
    __default_fiber_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity'), 'default_fiber_velocity', '__AbsentNamespace0_Millard2012EquilibriumMuscle_default_fiber_velocity', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 67, 6), )

    
    default_fiber_velocity = property(__default_fiber_velocity.value, __default_fiber_velocity.set, None, None)

    
    # Element default_fiber_length uses Python identifier default_fiber_length
    __default_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_fiber_length'), 'default_fiber_length', '__AbsentNamespace0_Millard2012EquilibriumMuscle_default_fiber_length', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 68, 6), )

    
    default_fiber_length = property(__default_fiber_length.value, __default_fiber_length.set, None, 'Assumed initial fiber length if none is assigned.')

    
    # Element MuscleFirstOrderActivationDynamicModel uses Python identifier MuscleFirstOrderActivationDynamicModel
    __MuscleFirstOrderActivationDynamicModel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel'), 'MuscleFirstOrderActivationDynamicModel', '__AbsentNamespace0_Millard2012EquilibriumMuscle_MuscleFirstOrderActivationDynamicModel', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 73, 6), )

    
    MuscleFirstOrderActivationDynamicModel = property(__MuscleFirstOrderActivationDynamicModel.value, __MuscleFirstOrderActivationDynamicModel.set, None, 'Activation dynamics model with a lower boundactivation.')

    
    # Element GeometryPath uses Python identifier GeometryPath
    __GeometryPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), 'GeometryPath', '__AbsentNamespace0_Millard2012EquilibriumMuscle_GeometryPath', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 106, 2), )

    
    GeometryPath = property(__GeometryPath.value, __GeometryPath.set, None, 'The set of points defining the path of the muscle.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Millard2012EquilibriumMuscle_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 95, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 95, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __max_isometric_force.name() : __max_isometric_force,
        __min_control.name() : __min_control,
        __max_control.name() : __max_control,
        __optimal_fiber_length.name() : __optimal_fiber_length,
        __tendon_slack_length.name() : __tendon_slack_length,
        __pennation_angle_at_optimal.name() : __pennation_angle_at_optimal,
        __fiber_damping.name() : __fiber_damping,
        __default_fiber_velocity.name() : __default_fiber_velocity,
        __default_fiber_length.name() : __default_fiber_length,
        __MuscleFirstOrderActivationDynamicModel.name() : __MuscleFirstOrderActivationDynamicModel,
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 98, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element max_isometric_force uses Python identifier max_isometric_force
    __max_isometric_force = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), 'max_isometric_force', '__AbsentNamespace0_Millard2012AccelerationMuscle_max_isometric_force', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 35, 4), )

    
    max_isometric_force = property(__max_isometric_force.value, __max_isometric_force.set, None, 'Maximum isometric force that the fibers can generate.')

    
    # Element min_control uses Python identifier min_control
    __min_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_control'), 'min_control', '__AbsentNamespace0_Millard2012AccelerationMuscle_min_control', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 40, 4), )

    
    min_control = property(__min_control.value, __min_control.set, None, None)

    
    # Element max_control uses Python identifier max_control
    __max_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_control'), 'max_control', '__AbsentNamespace0_Millard2012AccelerationMuscle_max_control', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 41, 4), )

    
    max_control = property(__max_control.value, __max_control.set, None, 'Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.')

    
    # Element optimal_fiber_length uses Python identifier optimal_fiber_length
    __optimal_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), 'optimal_fiber_length', '__AbsentNamespace0_Millard2012AccelerationMuscle_optimal_fiber_length', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 46, 4), )

    
    optimal_fiber_length = property(__optimal_fiber_length.value, __optimal_fiber_length.set, None, 'Optimal length of the muscle fibers.')

    
    # Element tendon_slack_length uses Python identifier tendon_slack_length
    __tendon_slack_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), 'tendon_slack_length', '__AbsentNamespace0_Millard2012AccelerationMuscle_tendon_slack_length', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 51, 4), )

    
    tendon_slack_length = property(__tendon_slack_length.value, __tendon_slack_length.set, None, 'Resting length of the tendonResting length of the tendon.')

    
    # Element pennation_angle_at_optimal uses Python identifier pennation_angle_at_optimal
    __pennation_angle_at_optimal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), 'pennation_angle_at_optimal', '__AbsentNamespace0_Millard2012AccelerationMuscle_pennation_angle_at_optimal', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 56, 4), )

    
    pennation_angle_at_optimal = property(__pennation_angle_at_optimal.value, __pennation_angle_at_optimal.set, None, 'Angle between tendon and fibers at optimal fiber length expressed in radians.')

    
    # Element fiber_damping uses Python identifier fiber_damping
    __fiber_damping = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fiber_damping'), 'fiber_damping', '__AbsentNamespace0_Millard2012AccelerationMuscle_fiber_damping', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 66, 6), )

    
    fiber_damping = property(__fiber_damping.value, __fiber_damping.set, None, None)

    
    # Element default_fiber_velocity uses Python identifier default_fiber_velocity
    __default_fiber_velocity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity'), 'default_fiber_velocity', '__AbsentNamespace0_Millard2012AccelerationMuscle_default_fiber_velocity', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 67, 6), )

    
    default_fiber_velocity = property(__default_fiber_velocity.value, __default_fiber_velocity.set, None, None)

    
    # Element default_fiber_length uses Python identifier default_fiber_length
    __default_fiber_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default_fiber_length'), 'default_fiber_length', '__AbsentNamespace0_Millard2012AccelerationMuscle_default_fiber_length', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 68, 6), )

    
    default_fiber_length = property(__default_fiber_length.value, __default_fiber_length.set, None, 'Assumed initial fiber length if none is assigned.')

    
    # Element MuscleFirstOrderActivationDynamicModel uses Python identifier MuscleFirstOrderActivationDynamicModel
    __MuscleFirstOrderActivationDynamicModel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel'), 'MuscleFirstOrderActivationDynamicModel', '__AbsentNamespace0_Millard2012AccelerationMuscle_MuscleFirstOrderActivationDynamicModel', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 73, 6), )

    
    MuscleFirstOrderActivationDynamicModel = property(__MuscleFirstOrderActivationDynamicModel.value, __MuscleFirstOrderActivationDynamicModel.set, None, 'Activation dynamics model with a lower boundactivation.')

    
    # Element GeometryPath uses Python identifier GeometryPath
    __GeometryPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), 'GeometryPath', '__AbsentNamespace0_Millard2012AccelerationMuscle_GeometryPath', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 106, 2), )

    
    GeometryPath = property(__GeometryPath.value, __GeometryPath.set, None, 'The set of points defining the path of the muscle.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_Millard2012AccelerationMuscle_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 103, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 103, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __max_isometric_force.name() : __max_isometric_force,
        __min_control.name() : __min_control,
        __max_control.name() : __max_control,
        __optimal_fiber_length.name() : __optimal_fiber_length,
        __tendon_slack_length.name() : __tendon_slack_length,
        __pennation_angle_at_optimal.name() : __pennation_angle_at_optimal,
        __fiber_damping.name() : __fiber_damping,
        __default_fiber_velocity.name() : __default_fiber_velocity,
        __default_fiber_length.name() : __default_fiber_length,
        __MuscleFirstOrderActivationDynamicModel.name() : __MuscleFirstOrderActivationDynamicModel,
        __GeometryPath.name() : __GeometryPath
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.Millard2012AccelerationMuscle = Millard2012AccelerationMuscle
Namespace.addCategoryObject('typeBinding', 'Millard2012AccelerationMuscle', Millard2012AccelerationMuscle)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """The set of points defining the path of the muscle."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 110, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PathPointSet uses Python identifier PathPointSet
    __PathPointSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'PathPointSet'), 'PathPointSet', '__AbsentNamespace0_CTD_ANON_5_PathPointSet', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 112, 8), )

    
    PathPointSet = property(__PathPointSet.value, __PathPointSet.set, None, None)

    _ElementMap.update({
        __PathPointSet.name() : __PathPointSet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 113, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objects uses Python identifier objects
    __objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'objects'), 'objects', '__AbsentNamespace0_CTD_ANON_6_objects', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 115, 14), )

    
    objects = property(__objects.value, __objects.set, None, None)

    
    # Element groups uses Python identifier groups
    __groups = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'groups'), 'groups', '__AbsentNamespace0_CTD_ANON_6_groups', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 122, 14), )

    
    groups = property(__groups.value, __groups.set, None, None)

    _ElementMap.update({
        __objects.name() : __objects,
        __groups.name() : __groups
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 116, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element PathPoint uses Python identifier PathPoint
    __PathPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PathPoint'), 'PathPoint', '__AbsentNamespace0_CTD_ANON_7_PathPoint', True, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 130, 2), )

    
    PathPoint = property(__PathPoint.value, __PathPoint.set, None, None)

    _ElementMap.update({
        __PathPoint.name() : __PathPoint
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 131, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_CTD_ANON_8_location', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 133, 8), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element body uses Python identifier body
    __body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'body'), 'body', '__AbsentNamespace0_CTD_ANON_8_body', False, pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 134, 8), )

    
    body = property(__body.value, __body.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_8_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 136, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 136, 6)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __location.name() : __location,
        __body.name() : __body
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


OpenSimDocument = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpenSimDocument'), CTD_ANON, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', OpenSimDocument.name().localName(), OpenSimDocument)

GeometryPath = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_5, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 106, 2))
Namespace.addCategoryObject('elementBinding', GeometryPath.name().localName(), GeometryPath)

PathPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PathPoint'), CTD_ANON_8, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 130, 2))
Namespace.addCategoryObject('elementBinding', PathPoint.name().localName(), PathPoint)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Model'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 7, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'Model')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 7, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ForceSet'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 10, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'ForceSet')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 10, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objects'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 13, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, 'objects')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 13, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Millard2012EquilibriumMuscle'), Millard2012EquilibriumMuscle, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 16, 26)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Millard2012AccelerationMuscle'), Millard2012AccelerationMuscle, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 17, 26)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 15, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'Millard2012EquilibriumMuscle')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 16, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'Millard2012AccelerationMuscle')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 17, 26))
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
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'minimum_activation'), pyxb.binding.datatypes.float, scope=CTD_ANON_4, documentation='Activation lower bound.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 79, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'minimum_activation')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 79, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Maximum isometric force that the fibers can generate.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 35, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_control'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 40, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_control'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 41, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Optimal length of the muscle fibers.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 46, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Resting length of the tendonResting length of the tendon.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 51, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Angle between tendon and fibers at optimal fiber length expressed in radians.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 56, 4)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fiber_damping'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 66, 6)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 67, 6)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_fiber_length'), pyxb.binding.datatypes.float, scope=Millard2012EquilibriumMuscle, documentation='Assumed initial fiber length if none is assigned.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 68, 6)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel'), CTD_ANON_4, scope=Millard2012EquilibriumMuscle, documentation='Activation dynamics model with a lower boundactivation.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 73, 6)))

Millard2012EquilibriumMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_5, scope=Millard2012EquilibriumMuscle, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 106, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 40, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 41, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 56, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 66, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 67, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 68, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 73, 6))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 34, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_isometric_force')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 35, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'min_control')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 40, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_control')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 41, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 46, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'tendon_slack_length')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 51, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 56, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'fiber_damping')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 66, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 67, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_fiber_length')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 68, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012EquilibriumMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 73, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
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
Millard2012EquilibriumMuscle._Automaton = _BuildAutomaton_5()




Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_isometric_force'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Maximum isometric force that the fibers can generate.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 35, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_control'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 40, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_control'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Maximum allowed value for control signal. Used primarily when solving for control values.Maximum allowed value for control signal.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 41, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Optimal length of the muscle fibers.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 46, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tendon_slack_length'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Resting length of the tendonResting length of the tendon.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 51, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Angle between tendon and fibers at optimal fiber length expressed in radians.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 56, 4)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fiber_damping'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 66, 6)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 67, 6)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default_fiber_length'), pyxb.binding.datatypes.float, scope=Millard2012AccelerationMuscle, documentation='Assumed initial fiber length if none is assigned.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 68, 6)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel'), CTD_ANON_4, scope=Millard2012AccelerationMuscle, documentation='Activation dynamics model with a lower boundactivation.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 73, 6)))

Millard2012AccelerationMuscle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath'), CTD_ANON_5, scope=Millard2012AccelerationMuscle, documentation='The set of points defining the path of the muscle.', location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 106, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 40, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 41, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 56, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 66, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 67, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 68, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 73, 6))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeometryPath')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 34, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_isometric_force')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 35, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'min_control')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 40, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'max_control')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 41, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'optimal_fiber_length')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 46, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'tendon_slack_length')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 51, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'pennation_angle_at_optimal')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 56, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'fiber_damping')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 66, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_fiber_velocity')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 67, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'default_fiber_length')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 68, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Millard2012AccelerationMuscle._UseForTag(pyxb.namespace.ExpandedName(None, 'MuscleFirstOrderActivationDynamicModel')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 73, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
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
Millard2012AccelerationMuscle._Automaton = _BuildAutomaton_6()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'PathPointSet'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 112, 8)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'PathPointSet')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 112, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_7()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'objects'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 115, 14)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'groups'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 122, 14)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 122, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'objects')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 115, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, 'groups')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 122, 14))
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
CTD_ANON_6._Automaton = _BuildAutomaton_8()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PathPoint'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 130, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 117, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PathPoint')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 118, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_9()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), vector3, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 133, 8)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'body'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 134, 8)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 133, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'body')), pyxb.utils.utility.Location('/mnt/work/BlenderRobotDesigner/robot_designer_plugin/resources/osim_muscles.xsd', 134, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_10()

