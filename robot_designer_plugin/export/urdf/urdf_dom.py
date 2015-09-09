# ./urdf_dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2015-09-08 06:19:43.202451 by PyXB version 1.2.4 using Python 3.4.0.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d47d81f0-55e0-11e5-b199-6c71d9b2bdf1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

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


# Atomic simple type: ControllerEnumType
class ControllerEnumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ControllerEnumType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 237, 2)
    _Documentation = None
ControllerEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ControllerEnumType, enum_prefix=None)
ControllerEnumType.position = ControllerEnumType._CF_enumeration.addEnumeration(unicode_value='position', tag='position')
ControllerEnumType.velocity = ControllerEnumType._CF_enumeration.addEnumeration(unicode_value='velocity', tag='velocity')
ControllerEnumType._InitializeFacetMap(ControllerEnumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ControllerEnumType', ControllerEnumType)

# Complex type PoseType with content type EMPTY
class PoseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type PoseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PoseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute xyz uses Python identifier xyz
    __xyz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'xyz'), 'xyz', '__AbsentNamespace0_PoseType_xyz', pyxb.binding.datatypes.string, unicode_default='0 0 0')
    __xyz._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 9, 4)
    __xyz._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 9, 4)
    
    xyz = property(__xyz.value, __xyz.set, None, None)

    
    # Attribute rpy uses Python identifier rpy
    __rpy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rpy'), 'rpy', '__AbsentNamespace0_PoseType_rpy', pyxb.binding.datatypes.string, unicode_default='0 0 0')
    __rpy._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 10, 4)
    __rpy._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 10, 4)
    
    rpy = property(__rpy.value, __rpy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __xyz.name() : __xyz,
        __rpy.name() : __rpy
    })
Namespace.addCategoryObject('typeBinding', 'PoseType', PoseType)


# Complex type ColorType with content type EMPTY
class ColorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ColorType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ColorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 14, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rgba uses Python identifier rgba
    __rgba = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rgba'), 'rgba', '__AbsentNamespace0_ColorType_rgba', pyxb.binding.datatypes.string, unicode_default='0 0 0 0')
    __rgba._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 15, 4)
    __rgba._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 15, 4)
    
    rgba = property(__rgba.value, __rgba.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rgba.name() : __rgba
    })
Namespace.addCategoryObject('typeBinding', 'ColorType', ColorType)


# Complex type VerboseType with content type EMPTY
class VerboseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type VerboseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VerboseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 19, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_VerboseType_value', pyxb.binding.datatypes.string)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 20, 4)
    __value._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 20, 4)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', 'VerboseType', VerboseType)


# Complex type MassType with content type EMPTY
class MassType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MassType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MassType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 24, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_MassType_value', pyxb.binding.datatypes.double, unicode_default='0')
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 25, 4)
    __value._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 25, 4)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', 'MassType', MassType)


# Complex type InertiaType with content type EMPTY
class InertiaType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type InertiaType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InertiaType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ixx uses Python identifier ixx
    __ixx = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ixx'), 'ixx', '__AbsentNamespace0_InertiaType_ixx', pyxb.binding.datatypes.double, unicode_default='0')
    __ixx._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 30, 4)
    __ixx._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 30, 4)
    
    ixx = property(__ixx.value, __ixx.set, None, None)

    
    # Attribute ixy uses Python identifier ixy
    __ixy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ixy'), 'ixy', '__AbsentNamespace0_InertiaType_ixy', pyxb.binding.datatypes.double, unicode_default='0')
    __ixy._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 31, 4)
    __ixy._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 31, 4)
    
    ixy = property(__ixy.value, __ixy.set, None, None)

    
    # Attribute ixz uses Python identifier ixz
    __ixz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ixz'), 'ixz', '__AbsentNamespace0_InertiaType_ixz', pyxb.binding.datatypes.double, unicode_default='0')
    __ixz._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 32, 4)
    __ixz._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 32, 4)
    
    ixz = property(__ixz.value, __ixz.set, None, None)

    
    # Attribute iyy uses Python identifier iyy
    __iyy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iyy'), 'iyy', '__AbsentNamespace0_InertiaType_iyy', pyxb.binding.datatypes.double, unicode_default='0')
    __iyy._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 33, 4)
    __iyy._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 33, 4)
    
    iyy = property(__iyy.value, __iyy.set, None, None)

    
    # Attribute iyz uses Python identifier iyz
    __iyz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'iyz'), 'iyz', '__AbsentNamespace0_InertiaType_iyz', pyxb.binding.datatypes.double, unicode_default='0')
    __iyz._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 34, 4)
    __iyz._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 34, 4)
    
    iyz = property(__iyz.value, __iyz.set, None, None)

    
    # Attribute izz uses Python identifier izz
    __izz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'izz'), 'izz', '__AbsentNamespace0_InertiaType_izz', pyxb.binding.datatypes.double, unicode_default='0')
    __izz._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 35, 4)
    __izz._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 35, 4)
    
    izz = property(__izz.value, __izz.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ixx.name() : __ixx,
        __ixy.name() : __ixy,
        __ixz.name() : __ixz,
        __iyy.name() : __iyy,
        __iyz.name() : __iyz,
        __izz.name() : __izz
    })
Namespace.addCategoryObject('typeBinding', 'InertiaType', InertiaType)


# Complex type InertialType with content type ELEMENT_ONLY
class InertialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type InertialType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InertialType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 39, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'origin'), 'origin', '__AbsentNamespace0_InertialType_origin', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 41, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element mass uses Python identifier mass
    __mass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mass'), 'mass', '__AbsentNamespace0_InertialType_mass', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 42, 6), )

    
    mass = property(__mass.value, __mass.set, None, None)

    
    # Element inertia uses Python identifier inertia
    __inertia = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inertia'), 'inertia', '__AbsentNamespace0_InertialType_inertia', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 43, 6), )

    
    inertia = property(__inertia.value, __inertia.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __mass.name() : __mass,
        __inertia.name() : __inertia
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InertialType', InertialType)


# Complex type BoxType with content type EMPTY
class BoxType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BoxType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoxType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 48, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_BoxType_size', pyxb.binding.datatypes.string, unicode_default='0 0 0')
    __size._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 49, 4)
    __size._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 49, 4)
    
    size = property(__size.value, __size.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __size.name() : __size
    })
Namespace.addCategoryObject('typeBinding', 'BoxType', BoxType)


# Complex type CylinderType with content type EMPTY
class CylinderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CylinderType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CylinderType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 53, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute radius uses Python identifier radius
    __radius = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_CylinderType_radius', pyxb.binding.datatypes.double, required=True)
    __radius._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 54, 4)
    __radius._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 54, 4)
    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_CylinderType_length', pyxb.binding.datatypes.double, required=True)
    __length._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 55, 4)
    __length._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 55, 4)
    
    length = property(__length.value, __length.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __radius.name() : __radius,
        __length.name() : __length
    })
Namespace.addCategoryObject('typeBinding', 'CylinderType', CylinderType)


# Complex type SphereType with content type EMPTY
class SphereType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SphereType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SphereType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 59, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute radius uses Python identifier radius
    __radius = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_SphereType_radius', pyxb.binding.datatypes.double, required=True)
    __radius._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 60, 4)
    __radius._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 60, 4)
    
    radius = property(__radius.value, __radius.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __radius.name() : __radius
    })
Namespace.addCategoryObject('typeBinding', 'SphereType', SphereType)


# Complex type MeshType with content type EMPTY
class MeshType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MeshType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MeshType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 64, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__AbsentNamespace0_MeshType_filename', pyxb.binding.datatypes.anyURI, required=True)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 65, 4)
    __filename._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 65, 4)
    
    filename = property(__filename.value, __filename.set, None, None)

    
    # Attribute scale uses Python identifier scale
    __scale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'scale'), 'scale', '__AbsentNamespace0_MeshType_scale', pyxb.binding.datatypes.string, unicode_default='1 1 1')
    __scale._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 66, 4)
    __scale._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 66, 4)
    
    scale = property(__scale.value, __scale.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __filename.name() : __filename,
        __scale.name() : __scale
    })
Namespace.addCategoryObject('typeBinding', 'MeshType', MeshType)


# Complex type GeometryType with content type ELEMENT_ONLY
class GeometryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GeometryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeometryType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element box uses Python identifier box
    __box = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'box'), 'box', '__AbsentNamespace0_GeometryType_box', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 72, 6), )

    
    box = property(__box.value, __box.set, None, None)

    
    # Element cylinder uses Python identifier cylinder
    __cylinder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cylinder'), 'cylinder', '__AbsentNamespace0_GeometryType_cylinder', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 73, 6), )

    
    cylinder = property(__cylinder.value, __cylinder.set, None, None)

    
    # Element sphere uses Python identifier sphere
    __sphere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sphere'), 'sphere', '__AbsentNamespace0_GeometryType_sphere', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 74, 6), )

    
    sphere = property(__sphere.value, __sphere.set, None, None)

    
    # Element mesh uses Python identifier mesh
    __mesh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mesh'), 'mesh', '__AbsentNamespace0_GeometryType_mesh', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 75, 6), )

    
    mesh = property(__mesh.value, __mesh.set, None, None)

    _ElementMap.update({
        __box.name() : __box,
        __cylinder.name() : __cylinder,
        __sphere.name() : __sphere,
        __mesh.name() : __mesh
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GeometryType', GeometryType)


# Complex type TextureType with content type EMPTY
class TextureType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TextureType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TextureType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 80, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__AbsentNamespace0_TextureType_filename', pyxb.binding.datatypes.anyURI)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 81, 4)
    __filename._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 81, 4)
    
    filename = property(__filename.value, __filename.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __filename.name() : __filename
    })
Namespace.addCategoryObject('typeBinding', 'TextureType', TextureType)


# Complex type MaterialType with content type ELEMENT_ONLY
class MaterialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MaterialType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 85, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element color uses Python identifier color
    __color = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_MaterialType_color', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 88, 10), )

    
    color = property(__color.value, __color.set, None, None)

    
    # Element texture uses Python identifier texture
    __texture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'texture'), 'texture', '__AbsentNamespace0_MaterialType_texture', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 89, 10), )

    
    texture = property(__texture.value, __texture.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_MaterialType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 92, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 92, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __color.name() : __color,
        __texture.name() : __texture
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'MaterialType', MaterialType)


# Complex type VisualType with content type ELEMENT_ONLY
class VisualType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type VisualType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VisualType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 96, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'origin'), 'origin', '__AbsentNamespace0_VisualType_origin', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 98, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry'), 'geometry', '__AbsentNamespace0_VisualType_geometry', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 99, 6), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Element material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'material'), 'material', '__AbsentNamespace0_VisualType_material', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 100, 6), )

    
    material = property(__material.value, __material.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __geometry.name() : __geometry,
        __material.name() : __material
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'VisualType', VisualType)


# Complex type ContactType with content type EMPTY
class ContactType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ContactType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContactType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 105, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute mu uses Python identifier mu
    __mu = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mu'), 'mu', '__AbsentNamespace0_ContactType_mu', pyxb.binding.datatypes.double, unicode_default='0')
    __mu._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 106, 4)
    __mu._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 106, 4)
    
    mu = property(__mu.value, __mu.set, None, None)

    
    # Attribute kp uses Python identifier kp
    __kp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kp'), 'kp', '__AbsentNamespace0_ContactType_kp', pyxb.binding.datatypes.double, unicode_default='0')
    __kp._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 107, 4)
    __kp._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 107, 4)
    
    kp = property(__kp.value, __kp.set, None, None)

    
    # Attribute kd uses Python identifier kd
    __kd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kd'), 'kd', '__AbsentNamespace0_ContactType_kd', pyxb.binding.datatypes.double, unicode_default='0')
    __kd._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 108, 4)
    __kd._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 108, 4)
    
    kd = property(__kd.value, __kd.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __mu.name() : __mu,
        __kp.name() : __kp,
        __kd.name() : __kd
    })
Namespace.addCategoryObject('typeBinding', 'ContactType', ContactType)


# Complex type CollisionType with content type ELEMENT_ONLY
class CollisionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CollisionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CollisionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 112, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'origin'), 'origin', '__AbsentNamespace0_CollisionType_origin', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 114, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry'), 'geometry', '__AbsentNamespace0_CollisionType_geometry', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 115, 6), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Element contact_coefficients uses Python identifier contact_coefficients
    __contact_coefficients = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contact_coefficients'), 'contact_coefficients', '__AbsentNamespace0_CollisionType_contact_coefficients', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 116, 6), )

    
    contact_coefficients = property(__contact_coefficients.value, __contact_coefficients.set, None, None)

    
    # Element verbose uses Python identifier verbose
    __verbose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'verbose'), 'verbose', '__AbsentNamespace0_CollisionType_verbose', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 117, 6), )

    
    verbose = property(__verbose.value, __verbose.set, None, None)

    
    # Element material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'material'), 'material', '__AbsentNamespace0_CollisionType_material', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 118, 6), )

    
    material = property(__material.value, __material.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __geometry.name() : __geometry,
        __contact_coefficients.name() : __contact_coefficients,
        __verbose.name() : __verbose,
        __material.name() : __material
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CollisionType', CollisionType)


# Complex type LinkType with content type ELEMENT_ONLY
class LinkType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type LinkType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinkType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 123, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'origin'), 'origin', '__AbsentNamespace0_LinkType_origin', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 125, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element inertial uses Python identifier inertial
    __inertial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inertial'), 'inertial', '__AbsentNamespace0_LinkType_inertial', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 126, 6), )

    
    inertial = property(__inertial.value, __inertial.set, None, None)

    
    # Element visual uses Python identifier visual
    __visual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visual'), 'visual', '__AbsentNamespace0_LinkType_visual', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 127, 6), )

    
    visual = property(__visual.value, __visual.set, None, None)

    
    # Element collision uses Python identifier collision
    __collision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collision'), 'collision', '__AbsentNamespace0_LinkType_collision', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 128, 6), )

    
    collision = property(__collision.value, __collision.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_LinkType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 130, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 130, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __inertial.name() : __inertial,
        __visual.name() : __visual,
        __collision.name() : __collision
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'LinkType', LinkType)


# Complex type ParentType with content type EMPTY
class ParentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ParentType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ParentType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 136, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__AbsentNamespace0_ParentType_link', pyxb.binding.datatypes.string, required=True)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 137, 4)
    __link._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 137, 4)
    
    link = property(__link.value, __link.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })
Namespace.addCategoryObject('typeBinding', 'ParentType', ParentType)


# Complex type ChildType with content type EMPTY
class ChildType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ChildType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChildType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 141, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__AbsentNamespace0_ChildType_link', pyxb.binding.datatypes.string, required=True)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 142, 4)
    __link._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 142, 4)
    
    link = property(__link.value, __link.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })
Namespace.addCategoryObject('typeBinding', 'ChildType', ChildType)


# Complex type AxisType with content type EMPTY
class AxisType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type AxisType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AxisType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 146, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute xyz uses Python identifier xyz
    __xyz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'xyz'), 'xyz', '__AbsentNamespace0_AxisType_xyz', pyxb.binding.datatypes.string, unicode_default='1 0 0')
    __xyz._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 147, 4)
    __xyz._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 147, 4)
    
    xyz = property(__xyz.value, __xyz.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __xyz.name() : __xyz
    })
Namespace.addCategoryObject('typeBinding', 'AxisType', AxisType)


# Complex type CalibrationType with content type EMPTY
class CalibrationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CalibrationType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CalibrationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 151, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute reference_position uses Python identifier reference_position
    __reference_position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reference_position'), 'reference_position', '__AbsentNamespace0_CalibrationType_reference_position', pyxb.binding.datatypes.double)
    __reference_position._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 152, 4)
    __reference_position._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 152, 4)
    
    reference_position = property(__reference_position.value, __reference_position.set, None, None)

    
    # Attribute rising uses Python identifier rising
    __rising = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rising'), 'rising', '__AbsentNamespace0_CalibrationType_rising', pyxb.binding.datatypes.double)
    __rising._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 153, 4)
    __rising._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 153, 4)
    
    rising = property(__rising.value, __rising.set, None, None)

    
    # Attribute falling uses Python identifier falling
    __falling = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'falling'), 'falling', '__AbsentNamespace0_CalibrationType_falling', pyxb.binding.datatypes.double)
    __falling._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 154, 4)
    __falling._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 154, 4)
    
    falling = property(__falling.value, __falling.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __reference_position.name() : __reference_position,
        __rising.name() : __rising,
        __falling.name() : __falling
    })
Namespace.addCategoryObject('typeBinding', 'CalibrationType', CalibrationType)


# Complex type DynamicsType with content type EMPTY
class DynamicsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DynamicsType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DynamicsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 158, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute damping uses Python identifier damping
    __damping = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'damping'), 'damping', '__AbsentNamespace0_DynamicsType_damping', pyxb.binding.datatypes.double, unicode_default='0')
    __damping._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 159, 4)
    __damping._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 159, 4)
    
    damping = property(__damping.value, __damping.set, None, None)

    
    # Attribute friction uses Python identifier friction
    __friction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'friction'), 'friction', '__AbsentNamespace0_DynamicsType_friction', pyxb.binding.datatypes.double, unicode_default='0')
    __friction._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 160, 4)
    __friction._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 160, 4)
    
    friction = property(__friction.value, __friction.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __damping.name() : __damping,
        __friction.name() : __friction
    })
Namespace.addCategoryObject('typeBinding', 'DynamicsType', DynamicsType)


# Complex type LimitType with content type EMPTY
class LimitType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type LimitType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LimitType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 164, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute lower uses Python identifier lower
    __lower = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lower'), 'lower', '__AbsentNamespace0_LimitType_lower', pyxb.binding.datatypes.double, unicode_default='0')
    __lower._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 165, 4)
    __lower._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 165, 4)
    
    lower = property(__lower.value, __lower.set, None, None)

    
    # Attribute upper uses Python identifier upper
    __upper = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'upper'), 'upper', '__AbsentNamespace0_LimitType_upper', pyxb.binding.datatypes.double, unicode_default='0')
    __upper._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 166, 4)
    __upper._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 166, 4)
    
    upper = property(__upper.value, __upper.set, None, None)

    
    # Attribute effort uses Python identifier effort
    __effort = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'effort'), 'effort', '__AbsentNamespace0_LimitType_effort', pyxb.binding.datatypes.double, unicode_default='0')
    __effort._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 167, 4)
    __effort._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 167, 4)
    
    effort = property(__effort.value, __effort.set, None, None)

    
    # Attribute velocity uses Python identifier velocity
    __velocity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'velocity'), 'velocity', '__AbsentNamespace0_LimitType_velocity', pyxb.binding.datatypes.double, unicode_default='0')
    __velocity._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 168, 4)
    __velocity._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 168, 4)
    
    velocity = property(__velocity.value, __velocity.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lower.name() : __lower,
        __upper.name() : __upper,
        __effort.name() : __effort,
        __velocity.name() : __velocity
    })
Namespace.addCategoryObject('typeBinding', 'LimitType', LimitType)


# Complex type SafetyControllerType with content type EMPTY
class SafetyControllerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SafetyControllerType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SafetyControllerType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 172, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute soft_lower_limit uses Python identifier soft_lower_limit
    __soft_lower_limit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'soft_lower_limit'), 'soft_lower_limit', '__AbsentNamespace0_SafetyControllerType_soft_lower_limit', pyxb.binding.datatypes.double, unicode_default='0')
    __soft_lower_limit._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 173, 4)
    __soft_lower_limit._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 173, 4)
    
    soft_lower_limit = property(__soft_lower_limit.value, __soft_lower_limit.set, None, None)

    
    # Attribute soft_upper_limit uses Python identifier soft_upper_limit
    __soft_upper_limit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'soft_upper_limit'), 'soft_upper_limit', '__AbsentNamespace0_SafetyControllerType_soft_upper_limit', pyxb.binding.datatypes.double, unicode_default='0')
    __soft_upper_limit._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 174, 4)
    __soft_upper_limit._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 174, 4)
    
    soft_upper_limit = property(__soft_upper_limit.value, __soft_upper_limit.set, None, None)

    
    # Attribute k_position uses Python identifier k_position
    __k_position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'k_position'), 'k_position', '__AbsentNamespace0_SafetyControllerType_k_position', pyxb.binding.datatypes.double, unicode_default='0')
    __k_position._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 175, 4)
    __k_position._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 175, 4)
    
    k_position = property(__k_position.value, __k_position.set, None, None)

    
    # Attribute k_velocity uses Python identifier k_velocity
    __k_velocity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'k_velocity'), 'k_velocity', '__AbsentNamespace0_SafetyControllerType_k_velocity', pyxb.binding.datatypes.double, required=True)
    __k_velocity._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 176, 4)
    __k_velocity._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 176, 4)
    
    k_velocity = property(__k_velocity.value, __k_velocity.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __soft_lower_limit.name() : __soft_lower_limit,
        __soft_upper_limit.name() : __soft_upper_limit,
        __k_position.name() : __k_position,
        __k_velocity.name() : __k_velocity
    })
Namespace.addCategoryObject('typeBinding', 'SafetyControllerType', SafetyControllerType)


# Complex type MimicType with content type EMPTY
class MimicType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MimicType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MimicType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 180, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute joint uses Python identifier joint
    __joint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'joint'), 'joint', '__AbsentNamespace0_MimicType_joint', pyxb.binding.datatypes.string, required=True)
    __joint._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 181, 4)
    __joint._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 181, 4)
    
    joint = property(__joint.value, __joint.set, None, None)

    
    # Attribute multiplier uses Python identifier multiplier
    __multiplier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'multiplier'), 'multiplier', '__AbsentNamespace0_MimicType_multiplier', pyxb.binding.datatypes.double, unicode_default='1')
    __multiplier._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 182, 4)
    __multiplier._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 182, 4)
    
    multiplier = property(__multiplier.value, __multiplier.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offset'), 'offset', '__AbsentNamespace0_MimicType_offset', pyxb.binding.datatypes.double, unicode_default='0')
    __offset._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 183, 4)
    __offset._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 183, 4)
    
    offset = property(__offset.value, __offset.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __joint.name() : __joint,
        __multiplier.name() : __multiplier,
        __offset.name() : __offset
    })
Namespace.addCategoryObject('typeBinding', 'MimicType', MimicType)


# Complex type JointType with content type ELEMENT_ONLY
class JointType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type JointType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JointType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 187, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element origin uses Python identifier origin
    __origin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'origin'), 'origin', '__AbsentNamespace0_JointType_origin', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 189, 6), )

    
    origin = property(__origin.value, __origin.set, None, None)

    
    # Element parent uses Python identifier parent
    __parent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parent'), 'parent', '__AbsentNamespace0_JointType_parent', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 190, 6), )

    
    parent = property(__parent.value, __parent.set, None, None)

    
    # Element child uses Python identifier child
    __child = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'child'), 'child', '__AbsentNamespace0_JointType_child', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 191, 6), )

    
    child = property(__child.value, __child.set, None, None)

    
    # Element axis uses Python identifier axis
    __axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'axis'), 'axis', '__AbsentNamespace0_JointType_axis', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 192, 6), )

    
    axis = property(__axis.value, __axis.set, None, None)

    
    # Element calibration uses Python identifier calibration
    __calibration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'calibration'), 'calibration', '__AbsentNamespace0_JointType_calibration', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 193, 6), )

    
    calibration = property(__calibration.value, __calibration.set, None, None)

    
    # Element dynamics uses Python identifier dynamics
    __dynamics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dynamics'), 'dynamics', '__AbsentNamespace0_JointType_dynamics', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 194, 6), )

    
    dynamics = property(__dynamics.value, __dynamics.set, None, None)

    
    # Element limit uses Python identifier limit
    __limit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'limit'), 'limit', '__AbsentNamespace0_JointType_limit', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 195, 6), )

    
    limit = property(__limit.value, __limit.set, None, None)

    
    # Element safety_controller uses Python identifier safety_controller
    __safety_controller = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'safety_controller'), 'safety_controller', '__AbsentNamespace0_JointType_safety_controller', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 196, 6), )

    
    safety_controller = property(__safety_controller.value, __safety_controller.set, None, None)

    
    # Element mimic uses Python identifier mimic
    __mimic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mimic'), 'mimic', '__AbsentNamespace0_JointType_mimic', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 197, 6), )

    
    mimic = property(__mimic.value, __mimic.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_JointType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 199, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 199, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_JointType_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 200, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 200, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __origin.name() : __origin,
        __parent.name() : __parent,
        __child.name() : __child,
        __axis.name() : __axis,
        __calibration.name() : __calibration,
        __dynamics.name() : __dynamics,
        __limit.name() : __limit,
        __safety_controller.name() : __safety_controller,
        __mimic.name() : __mimic
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'JointType', JointType)


# Complex type ActuatorTransmissionType with content type ELEMENT_ONLY
class ActuatorTransmissionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ActuatorTransmissionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ActuatorTransmissionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 206, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element hardwareInterface uses Python identifier hardwareInterface
    __hardwareInterface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hardwareInterface'), 'hardwareInterface', '__AbsentNamespace0_ActuatorTransmissionType_hardwareInterface', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 208, 6), )

    
    hardwareInterface = property(__hardwareInterface.value, __hardwareInterface.set, None, None)

    
    # Element mechanicalReduction uses Python identifier mechanicalReduction
    __mechanicalReduction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mechanicalReduction'), 'mechanicalReduction', '__AbsentNamespace0_ActuatorTransmissionType_mechanicalReduction', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 209, 6), )

    
    mechanicalReduction = property(__mechanicalReduction.value, __mechanicalReduction.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_ActuatorTransmissionType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 211, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 211, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __hardwareInterface.name() : __hardwareInterface,
        __mechanicalReduction.name() : __mechanicalReduction
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'ActuatorTransmissionType', ActuatorTransmissionType)


# Complex type JointTransmissionType with content type ELEMENT_ONLY
class JointTransmissionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type JointTransmissionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JointTransmissionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 215, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element hardwareInterface uses Python identifier hardwareInterface
    __hardwareInterface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hardwareInterface'), 'hardwareInterface', '__AbsentNamespace0_JointTransmissionType_hardwareInterface', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 218, 12), )

    
    hardwareInterface = property(__hardwareInterface.value, __hardwareInterface.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_JointTransmissionType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 221, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 221, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __hardwareInterface.name() : __hardwareInterface
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'JointTransmissionType', JointTransmissionType)


# Complex type TransmissionType with content type ELEMENT_ONLY
class TransmissionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TransmissionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransmissionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 225, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_TransmissionType_type', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 227, 6), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element actuator uses Python identifier actuator
    __actuator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'actuator'), 'actuator', '__AbsentNamespace0_TransmissionType_actuator', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 228, 6), )

    
    actuator = property(__actuator.value, __actuator.set, None, None)

    
    # Element joint uses Python identifier joint
    __joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'joint'), 'joint', '__AbsentNamespace0_TransmissionType_joint', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 229, 6), )

    
    joint = property(__joint.value, __joint.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_TransmissionType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 231, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 231, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __actuator.name() : __actuator,
        __joint.name() : __joint
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'TransmissionType', TransmissionType)


# Complex type GazeboPluginBaseType with content type EMPTY
class GazeboPluginBaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GazeboPluginBaseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GazeboPluginBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 245, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute filename uses Python identifier filename
    __filename = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'filename'), 'filename', '__AbsentNamespace0_GazeboPluginBaseType_filename', pyxb.binding.datatypes.string)
    __filename._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 246, 4)
    __filename._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 246, 4)
    
    filename = property(__filename.value, __filename.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_GazeboPluginBaseType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 247, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 247, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __filename.name() : __filename,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'GazeboPluginBaseType', GazeboPluginBaseType)


# Complex type GenericControllerPluginDefType with content type ELEMENT_ONLY
class GenericControllerPluginDefType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GenericControllerPluginDefType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericControllerPluginDefType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 251, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_GenericControllerPluginDefType_type', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 253, 6), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element pid uses Python identifier pid
    __pid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pid'), 'pid', '__AbsentNamespace0_GenericControllerPluginDefType_pid', False, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 254, 6), )

    
    pid = property(__pid.value, __pid.set, None, None)

    
    # Attribute joint_name uses Python identifier joint_name
    __joint_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'joint_name'), 'joint_name', '__AbsentNamespace0_GenericControllerPluginDefType_joint_name', pyxb.binding.datatypes.string)
    __joint_name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 256, 4)
    __joint_name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 256, 4)
    
    joint_name = property(__joint_name.value, __joint_name.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __pid.name() : __pid
    })
    _AttributeMap.update({
        __joint_name.name() : __joint_name
    })
Namespace.addCategoryObject('typeBinding', 'GenericControllerPluginDefType', GenericControllerPluginDefType)


# Complex type ImageType with content type ELEMENT_ONLY
class ImageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ImageType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImageType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 309, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_ImageType_width', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 312, 10), )

    
    width = property(__width.value, __width.set, None, None)

    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_ImageType_height', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 313, 10), )

    
    height = property(__height.value, __height.set, None, None)

    
    # Element format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'format'), 'format', '__AbsentNamespace0_ImageType_format', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 314, 10), )

    
    format = property(__format.value, __format.set, None, None)

    _ElementMap.update({
        __width.name() : __width,
        __height.name() : __height,
        __format.name() : __format
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ImageType', ImageType)


# Complex type ClipType with content type ELEMENT_ONLY
class ClipType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ClipType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClipType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 320, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element near uses Python identifier near
    __near = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'near'), 'near', '__AbsentNamespace0_ClipType_near', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 323, 10), )

    
    near = property(__near.value, __near.set, None, None)

    
    # Element far uses Python identifier far
    __far = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'far'), 'far', '__AbsentNamespace0_ClipType_far', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 324, 10), )

    
    far = property(__far.value, __far.set, None, None)

    _ElementMap.update({
        __near.name() : __near,
        __far.name() : __far
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ClipType', ClipType)


# Complex type NoiseType with content type ELEMENT_ONLY
class NoiseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type NoiseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NoiseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 330, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_NoiseType_type', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 333, 10), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element mean uses Python identifier mean
    __mean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mean'), 'mean', '__AbsentNamespace0_NoiseType_mean', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 334, 10), )

    
    mean = property(__mean.value, __mean.set, None, None)

    
    # Element stddev uses Python identifier stddev
    __stddev = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stddev'), 'stddev', '__AbsentNamespace0_NoiseType_stddev', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 335, 10), )

    
    stddev = property(__stddev.value, __stddev.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __mean.name() : __mean,
        __stddev.name() : __stddev
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'NoiseType', NoiseType)


# Complex type CameraType with content type ELEMENT_ONLY
class CameraType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CameraType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CameraType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 341, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element horizontal_fov uses Python identifier horizontal_fov
    __horizontal_fov = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'horizontal_fov'), 'horizontal_fov', '__AbsentNamespace0_CameraType_horizontal_fov', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 344, 10), )

    
    horizontal_fov = property(__horizontal_fov.value, __horizontal_fov.set, None, None)

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__AbsentNamespace0_CameraType_image', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 345, 10), )

    
    image = property(__image.value, __image.set, None, None)

    
    # Element clip uses Python identifier clip
    __clip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'clip'), 'clip', '__AbsentNamespace0_CameraType_clip', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 346, 10), )

    
    clip = property(__clip.value, __clip.set, None, None)

    
    # Element noise uses Python identifier noise
    __noise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'noise'), 'noise', '__AbsentNamespace0_CameraType_noise', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 347, 10), )

    
    noise = property(__noise.value, __noise.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CameraType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 350, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 350, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __horizontal_fov.name() : __horizontal_fov,
        __image.name() : __image,
        __clip.name() : __clip,
        __noise.name() : __noise
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'CameraType', CameraType)


# Complex type GazeboSensorBaseType with content type ELEMENT_ONLY
class GazeboSensorBaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GazeboSensorBaseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GazeboSensorBaseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 354, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pose uses Python identifier pose
    __pose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pose'), 'pose', '__AbsentNamespace0_GazeboSensorBaseType_pose', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 357, 10), )

    
    pose = property(__pose.value, __pose.set, None, None)

    
    # Element update_rate uses Python identifier update_rate
    __update_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'update_rate'), 'update_rate', '__AbsentNamespace0_GazeboSensorBaseType_update_rate', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 358, 10), )

    
    update_rate = property(__update_rate.value, __update_rate.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_GazeboSensorBaseType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 361, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 361, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_GazeboSensorBaseType_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 362, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 362, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __pose.name() : __pose,
        __update_rate.name() : __update_rate
    })
    _AttributeMap.update({
        __name.name() : __name,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'GazeboSensorBaseType', GazeboSensorBaseType)


# Complex type GazeboMaterialType with content type EMPTY
class GazeboMaterialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GazeboMaterialType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GazeboMaterialType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 381, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_GazeboMaterialType_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 382, 4)
    __value._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 382, 4)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', 'GazeboMaterialType', GazeboMaterialType)


# Complex type GazeboType with content type ELEMENT_ONLY
class GazeboType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GazeboType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GazeboType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 386, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element plugin uses Python identifier plugin
    __plugin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'plugin'), 'plugin', '__AbsentNamespace0_GazeboType_plugin', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 388, 10), )

    
    plugin = property(__plugin.value, __plugin.set, None, None)

    
    # Element sensor uses Python identifier sensor
    __sensor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sensor'), 'sensor', '__AbsentNamespace0_GazeboType_sensor', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 389, 10), )

    
    sensor = property(__sensor.value, __sensor.set, None, None)

    
    # Element material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'material'), 'material', '__AbsentNamespace0_GazeboType_material', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 390, 10), )

    
    material = property(__material.value, __material.set, None, None)

    
    # Element gravity uses Python identifier gravity
    __gravity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gravity'), 'gravity', '__AbsentNamespace0_GazeboType_gravity', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 391, 10), )

    
    gravity = property(__gravity.value, __gravity.set, None, None)

    
    # Element self_collide uses Python identifier self_collide
    __self_collide = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'self_collide'), 'self_collide', '__AbsentNamespace0_GazeboType_self_collide', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 392, 10), )

    
    self_collide = property(__self_collide.value, __self_collide.set, None, None)

    
    # Attribute reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reference'), 'reference', '__AbsentNamespace0_GazeboType_reference', pyxb.binding.datatypes.string)
    __reference._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 394, 4)
    __reference._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 394, 4)
    
    reference = property(__reference.value, __reference.set, None, None)

    _ElementMap.update({
        __plugin.name() : __plugin,
        __sensor.name() : __sensor,
        __material.name() : __material,
        __gravity.name() : __gravity,
        __self_collide.name() : __self_collide
    })
    _AttributeMap.update({
        __reference.name() : __reference
    })
Namespace.addCategoryObject('typeBinding', 'GazeboType', GazeboType)


# Complex type RobotType with content type ELEMENT_ONLY
class RobotType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RobotType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RobotType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 401, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element joint uses Python identifier joint
    __joint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'joint'), 'joint', '__AbsentNamespace0_RobotType_joint', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 404, 10), )

    
    joint = property(__joint.value, __joint.set, None, None)

    
    # Element link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__AbsentNamespace0_RobotType_link', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 405, 10), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Element transmission uses Python identifier transmission
    __transmission = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transmission'), 'transmission', '__AbsentNamespace0_RobotType_transmission', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 406, 10), )

    
    transmission = property(__transmission.value, __transmission.set, None, None)

    
    # Element gazebo uses Python identifier gazebo
    __gazebo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gazebo'), 'gazebo', '__AbsentNamespace0_RobotType_gazebo', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 407, 10), )

    
    gazebo = property(__gazebo.value, __gazebo.set, None, None)

    
    # Element material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'material'), 'material', '__AbsentNamespace0_RobotType_material', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 408, 10), )

    
    material = property(__material.value, __material.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_RobotType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 411, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 411, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_RobotType_version', pyxb.binding.datatypes.string, unicode_default='1.0')
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 412, 4)
    __version._UseLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 412, 4)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __joint.name() : __joint,
        __link.name() : __link,
        __transmission.name() : __transmission,
        __gazebo.name() : __gazebo,
        __material.name() : __material
    })
    _AttributeMap.update({
        __name.name() : __name,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', 'RobotType', RobotType)


# Complex type GazeboPluginType with content type ELEMENT_ONLY
class GazeboPluginType (GazeboPluginBaseType):
    """Complex type GazeboPluginType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GazeboPluginType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 260, 2)
    _ElementMap = GazeboPluginBaseType._ElementMap.copy()
    _AttributeMap = GazeboPluginBaseType._AttributeMap.copy()
    # Base type is GazeboPluginBaseType
    
    # Element robotNamespace uses Python identifier robotNamespace
    __robotNamespace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'robotNamespace'), 'robotNamespace', '__AbsentNamespace0_GazeboPluginType_robotNamespace', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 265, 16), )

    
    robotNamespace = property(__robotNamespace.value, __robotNamespace.set, None, None)

    
    # Element robotSimType uses Python identifier robotSimType
    __robotSimType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'robotSimType'), 'robotSimType', '__AbsentNamespace0_GazeboPluginType_robotSimType', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 266, 16), )

    
    robotSimType = property(__robotSimType.value, __robotSimType.set, None, None)

    
    # Element robotParam uses Python identifier robotParam
    __robotParam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'robotParam'), 'robotParam', '__AbsentNamespace0_GazeboPluginType_robotParam', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 267, 16), )

    
    robotParam = property(__robotParam.value, __robotParam.set, None, None)

    
    # Element controller uses Python identifier controller
    __controller = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'controller'), 'controller', '__AbsentNamespace0_GazeboPluginType_controller', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 268, 16), )

    
    controller = property(__controller.value, __controller.set, None, None)

    
    # Attribute filename inherited from GazeboPluginBaseType
    
    # Attribute name inherited from GazeboPluginBaseType
    _ElementMap.update({
        __robotNamespace.name() : __robotNamespace,
        __robotSimType.name() : __robotSimType,
        __robotParam.name() : __robotParam,
        __controller.name() : __controller
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GazeboPluginType', GazeboPluginType)


# Complex type GazeboCameraPluginType with content type ELEMENT_ONLY
class GazeboCameraPluginType (GazeboPluginBaseType):
    """Complex type GazeboCameraPluginType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GazeboCameraPluginType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 276, 2)
    _ElementMap = GazeboPluginBaseType._ElementMap.copy()
    _AttributeMap = GazeboPluginBaseType._AttributeMap.copy()
    # Base type is GazeboPluginBaseType
    
    # Element baseline uses Python identifier baseline
    __baseline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'baseline'), 'baseline', '__AbsentNamespace0_GazeboCameraPluginType_baseline', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 281, 18), )

    
    baseline = property(__baseline.value, __baseline.set, None, None)

    
    # Element alwaysOn uses Python identifier alwaysOn
    __alwaysOn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'alwaysOn'), 'alwaysOn', '__AbsentNamespace0_GazeboCameraPluginType_alwaysOn', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 282, 18), )

    
    alwaysOn = property(__alwaysOn.value, __alwaysOn.set, None, None)

    
    # Element updateRate uses Python identifier updateRate
    __updateRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'updateRate'), 'updateRate', '__AbsentNamespace0_GazeboCameraPluginType_updateRate', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 283, 18), )

    
    updateRate = property(__updateRate.value, __updateRate.set, None, None)

    
    # Element cameraName uses Python identifier cameraName
    __cameraName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cameraName'), 'cameraName', '__AbsentNamespace0_GazeboCameraPluginType_cameraName', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 284, 18), )

    
    cameraName = property(__cameraName.value, __cameraName.set, None, None)

    
    # Element imageTopicName uses Python identifier imageTopicName
    __imageTopicName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'imageTopicName'), 'imageTopicName', '__AbsentNamespace0_GazeboCameraPluginType_imageTopicName', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 285, 18), )

    
    imageTopicName = property(__imageTopicName.value, __imageTopicName.set, None, None)

    
    # Element depthImageTopicName uses Python identifier depthImageTopicName
    __depthImageTopicName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'depthImageTopicName'), 'depthImageTopicName', '__AbsentNamespace0_GazeboCameraPluginType_depthImageTopicName', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 286, 18), )

    
    depthImageTopicName = property(__depthImageTopicName.value, __depthImageTopicName.set, None, None)

    
    # Element cameraInfoTopicName uses Python identifier cameraInfoTopicName
    __cameraInfoTopicName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cameraInfoTopicName'), 'cameraInfoTopicName', '__AbsentNamespace0_GazeboCameraPluginType_cameraInfoTopicName', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 287, 18), )

    
    cameraInfoTopicName = property(__cameraInfoTopicName.value, __cameraInfoTopicName.set, None, None)

    
    # Element depthImageCameraInfoTopicName uses Python identifier depthImageCameraInfoTopicName
    __depthImageCameraInfoTopicName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'depthImageCameraInfoTopicName'), 'depthImageCameraInfoTopicName', '__AbsentNamespace0_GazeboCameraPluginType_depthImageCameraInfoTopicName', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 288, 18), )

    
    depthImageCameraInfoTopicName = property(__depthImageCameraInfoTopicName.value, __depthImageCameraInfoTopicName.set, None, None)

    
    # Element frameName uses Python identifier frameName
    __frameName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'frameName'), 'frameName', '__AbsentNamespace0_GazeboCameraPluginType_frameName', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 289, 18), )

    
    frameName = property(__frameName.value, __frameName.set, None, None)

    
    # Element hackBaseline uses Python identifier hackBaseline
    __hackBaseline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'hackBaseline'), 'hackBaseline', '__AbsentNamespace0_GazeboCameraPluginType_hackBaseline', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 290, 18), )

    
    hackBaseline = property(__hackBaseline.value, __hackBaseline.set, None, None)

    
    # Element distortionK1 uses Python identifier distortionK1
    __distortionK1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'distortionK1'), 'distortionK1', '__AbsentNamespace0_GazeboCameraPluginType_distortionK1', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 291, 18), )

    
    distortionK1 = property(__distortionK1.value, __distortionK1.set, None, None)

    
    # Element distortionK2 uses Python identifier distortionK2
    __distortionK2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'distortionK2'), 'distortionK2', '__AbsentNamespace0_GazeboCameraPluginType_distortionK2', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 292, 18), )

    
    distortionK2 = property(__distortionK2.value, __distortionK2.set, None, None)

    
    # Element distortionK3 uses Python identifier distortionK3
    __distortionK3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'distortionK3'), 'distortionK3', '__AbsentNamespace0_GazeboCameraPluginType_distortionK3', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 293, 18), )

    
    distortionK3 = property(__distortionK3.value, __distortionK3.set, None, None)

    
    # Element distortionT1 uses Python identifier distortionT1
    __distortionT1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'distortionT1'), 'distortionT1', '__AbsentNamespace0_GazeboCameraPluginType_distortionT1', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 294, 18), )

    
    distortionT1 = property(__distortionT1.value, __distortionT1.set, None, None)

    
    # Element distortionT2 uses Python identifier distortionT2
    __distortionT2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'distortionT2'), 'distortionT2', '__AbsentNamespace0_GazeboCameraPluginType_distortionT2', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 295, 18), )

    
    distortionT2 = property(__distortionT2.value, __distortionT2.set, None, None)

    
    # Element CxPrime uses Python identifier CxPrime
    __CxPrime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'CxPrime'), 'CxPrime', '__AbsentNamespace0_GazeboCameraPluginType_CxPrime', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 296, 18), )

    
    CxPrime = property(__CxPrime.value, __CxPrime.set, None, None)

    
    # Element Cx uses Python identifier Cx
    __Cx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cx'), 'Cx', '__AbsentNamespace0_GazeboCameraPluginType_Cx', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 297, 18), )

    
    Cx = property(__Cx.value, __Cx.set, None, None)

    
    # Element Cy uses Python identifier Cy
    __Cy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Cy'), 'Cy', '__AbsentNamespace0_GazeboCameraPluginType_Cy', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 298, 18), )

    
    Cy = property(__Cy.value, __Cy.set, None, None)

    
    # Element focalLength uses Python identifier focalLength
    __focalLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'focalLength'), 'focalLength', '__AbsentNamespace0_GazeboCameraPluginType_focalLength', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 299, 18), )

    
    focalLength = property(__focalLength.value, __focalLength.set, None, None)

    
    # Element pointCloudCutoff uses Python identifier pointCloudCutoff
    __pointCloudCutoff = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pointCloudCutoff'), 'pointCloudCutoff', '__AbsentNamespace0_GazeboCameraPluginType_pointCloudCutoff', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 300, 18), )

    
    pointCloudCutoff = property(__pointCloudCutoff.value, __pointCloudCutoff.set, None, None)

    
    # Element pointCloudTopicName uses Python identifier pointCloudTopicName
    __pointCloudTopicName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pointCloudTopicName'), 'pointCloudTopicName', '__AbsentNamespace0_GazeboCameraPluginType_pointCloudTopicName', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 301, 18), )

    
    pointCloudTopicName = property(__pointCloudTopicName.value, __pointCloudTopicName.set, None, None)

    
    # Attribute filename inherited from GazeboPluginBaseType
    
    # Attribute name inherited from GazeboPluginBaseType
    _ElementMap.update({
        __baseline.name() : __baseline,
        __alwaysOn.name() : __alwaysOn,
        __updateRate.name() : __updateRate,
        __cameraName.name() : __cameraName,
        __imageTopicName.name() : __imageTopicName,
        __depthImageTopicName.name() : __depthImageTopicName,
        __cameraInfoTopicName.name() : __cameraInfoTopicName,
        __depthImageCameraInfoTopicName.name() : __depthImageCameraInfoTopicName,
        __frameName.name() : __frameName,
        __hackBaseline.name() : __hackBaseline,
        __distortionK1.name() : __distortionK1,
        __distortionK2.name() : __distortionK2,
        __distortionK3.name() : __distortionK3,
        __distortionT1.name() : __distortionT1,
        __distortionT2.name() : __distortionT2,
        __CxPrime.name() : __CxPrime,
        __Cx.name() : __Cx,
        __Cy.name() : __Cy,
        __focalLength.name() : __focalLength,
        __pointCloudCutoff.name() : __pointCloudCutoff,
        __pointCloudTopicName.name() : __pointCloudTopicName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GazeboCameraPluginType', GazeboCameraPluginType)


# Complex type GazeboSensorType with content type ELEMENT_ONLY
class GazeboSensorType (GazeboSensorBaseType):
    """Complex type GazeboSensorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GazeboSensorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 366, 2)
    _ElementMap = GazeboSensorBaseType._ElementMap.copy()
    _AttributeMap = GazeboSensorBaseType._AttributeMap.copy()
    # Base type is GazeboSensorBaseType
    
    # Element pose (pose) inherited from GazeboSensorBaseType
    
    # Element update_rate (update_rate) inherited from GazeboSensorBaseType
    
    # Element camera uses Python identifier camera
    __camera = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'camera'), 'camera', '__AbsentNamespace0_GazeboSensorType_camera', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 371, 14), )

    
    camera = property(__camera.value, __camera.set, None, None)

    
    # Element plugin uses Python identifier plugin
    __plugin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'plugin'), 'plugin', '__AbsentNamespace0_GazeboSensorType_plugin', True, pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 372, 14), )

    
    plugin = property(__plugin.value, __plugin.set, None, None)

    
    # Attribute name inherited from GazeboSensorBaseType
    
    # Attribute type inherited from GazeboSensorBaseType
    _ElementMap.update({
        __camera.name() : __camera,
        __plugin.name() : __plugin
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GazeboSensorType', GazeboSensorType)


robot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'robot'), RobotType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 400, 2))
Namespace.addCategoryObject('elementBinding', robot.name().localName(), robot)



InertialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'origin'), PoseType, scope=InertialType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 41, 6)))

InertialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mass'), MassType, scope=InertialType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 42, 6)))

InertialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inertia'), InertiaType, scope=InertialType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 43, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 41, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InertialType._UseForTag(pyxb.namespace.ExpandedName(None, 'origin')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 41, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 42, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InertialType._UseForTag(pyxb.namespace.ExpandedName(None, 'mass')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 42, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 43, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InertialType._UseForTag(pyxb.namespace.ExpandedName(None, 'inertia')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 43, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 41, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 42, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 43, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 40, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InertialType._Automaton = _BuildAutomaton()




GeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'box'), BoxType, scope=GeometryType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 72, 6)))

GeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cylinder'), CylinderType, scope=GeometryType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 73, 6)))

GeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sphere'), SphereType, scope=GeometryType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 74, 6)))

GeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mesh'), MeshType, scope=GeometryType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 75, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'box')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 72, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'cylinder')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 73, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'sphere')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 74, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GeometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'mesh')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 75, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GeometryType._Automaton = _BuildAutomaton_4()




MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'color'), ColorType, scope=MaterialType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 88, 10)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'texture'), TextureType, scope=MaterialType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 89, 10)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 87, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'color')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 88, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'texture')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 89, 10))
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
MaterialType._Automaton = _BuildAutomaton_5()




VisualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'origin'), PoseType, scope=VisualType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 98, 6)))

VisualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry'), GeometryType, scope=VisualType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 99, 6)))

VisualType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'material'), MaterialType, scope=VisualType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 100, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 98, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VisualType._UseForTag(pyxb.namespace.ExpandedName(None, 'origin')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 98, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 99, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VisualType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 99, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 100, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VisualType._UseForTag(pyxb.namespace.ExpandedName(None, 'material')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 100, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 98, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 99, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 100, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_7())
    sub_automata.append(_BuildAutomaton_8())
    sub_automata.append(_BuildAutomaton_9())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 97, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VisualType._Automaton = _BuildAutomaton_6()




CollisionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'origin'), PoseType, scope=CollisionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 114, 6)))

CollisionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry'), GeometryType, scope=CollisionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 115, 6)))

CollisionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contact_coefficients'), ContactType, scope=CollisionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 116, 6)))

CollisionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'verbose'), VerboseType, scope=CollisionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 117, 6)))

CollisionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'material'), MaterialType, scope=CollisionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 118, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 114, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CollisionType._UseForTag(pyxb.namespace.ExpandedName(None, 'origin')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 114, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CollisionType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 115, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 116, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CollisionType._UseForTag(pyxb.namespace.ExpandedName(None, 'contact_coefficients')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 116, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 117, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CollisionType._UseForTag(pyxb.namespace.ExpandedName(None, 'verbose')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 117, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 118, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CollisionType._UseForTag(pyxb.namespace.ExpandedName(None, 'material')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 118, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 114, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 116, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 117, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 118, 6))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_11())
    sub_automata.append(_BuildAutomaton_12())
    sub_automata.append(_BuildAutomaton_13())
    sub_automata.append(_BuildAutomaton_14())
    sub_automata.append(_BuildAutomaton_15())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 113, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CollisionType._Automaton = _BuildAutomaton_10()




LinkType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'origin'), PoseType, scope=LinkType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 125, 6)))

LinkType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inertial'), InertialType, scope=LinkType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 126, 6)))

LinkType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visual'), VisualType, scope=LinkType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 127, 6)))

LinkType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collision'), CollisionType, scope=LinkType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 128, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 124, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 125, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 126, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 127, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 128, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LinkType._UseForTag(pyxb.namespace.ExpandedName(None, 'origin')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 125, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LinkType._UseForTag(pyxb.namespace.ExpandedName(None, 'inertial')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 126, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(LinkType._UseForTag(pyxb.namespace.ExpandedName(None, 'visual')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 127, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(LinkType._UseForTag(pyxb.namespace.ExpandedName(None, 'collision')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 128, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LinkType._Automaton = _BuildAutomaton_16()




JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'origin'), PoseType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 189, 6)))

JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parent'), ParentType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 190, 6)))

JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'child'), ChildType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 191, 6)))

JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'axis'), AxisType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 192, 6)))

JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'calibration'), CalibrationType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 193, 6)))

JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dynamics'), DynamicsType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 194, 6)))

JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'limit'), LimitType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 195, 6)))

JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'safety_controller'), SafetyControllerType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 196, 6)))

JointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mimic'), MimicType, scope=JointType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 197, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 189, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'origin')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 189, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'parent')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 190, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'child')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 191, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 192, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'axis')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 192, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 193, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'calibration')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 193, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 194, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'dynamics')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 194, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 195, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'limit')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 195, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 196, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'safety_controller')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 196, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 197, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JointType._UseForTag(pyxb.namespace.ExpandedName(None, 'mimic')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 197, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 189, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 192, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 193, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 194, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 195, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 196, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 197, 6))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    sub_automata.append(_BuildAutomaton_25())
    sub_automata.append(_BuildAutomaton_26())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 188, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
JointType._Automaton = _BuildAutomaton_17()




ActuatorTransmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hardwareInterface'), pyxb.binding.datatypes.string, scope=ActuatorTransmissionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 208, 6)))

ActuatorTransmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mechanicalReduction'), pyxb.binding.datatypes.double, scope=ActuatorTransmissionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 209, 6)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 208, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ActuatorTransmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'hardwareInterface')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 208, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 209, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ActuatorTransmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'mechanicalReduction')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 209, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 208, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 209, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_28())
    sub_automata.append(_BuildAutomaton_29())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 207, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ActuatorTransmissionType._Automaton = _BuildAutomaton_27()




JointTransmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hardwareInterface'), pyxb.binding.datatypes.string, scope=JointTransmissionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 218, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 217, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(JointTransmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'hardwareInterface')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 218, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
JointTransmissionType._Automaton = _BuildAutomaton_30()




TransmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=TransmissionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 227, 6)))

TransmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'actuator'), ActuatorTransmissionType, scope=TransmissionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 228, 6)))

TransmissionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'joint'), JointTransmissionType, scope=TransmissionType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 229, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 227, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 228, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'actuator')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 228, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 229, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransmissionType._UseForTag(pyxb.namespace.ExpandedName(None, 'joint')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 229, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 228, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 229, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_32())
    sub_automata.append(_BuildAutomaton_33())
    sub_automata.append(_BuildAutomaton_34())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 226, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TransmissionType._Automaton = _BuildAutomaton_31()




GenericControllerPluginDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), ControllerEnumType, scope=GenericControllerPluginDefType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 253, 6)))

GenericControllerPluginDefType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pid'), pyxb.binding.datatypes.string, scope=GenericControllerPluginDefType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 254, 6), unicode_default='0 0 0'))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GenericControllerPluginDefType._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 253, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GenericControllerPluginDefType._UseForTag(pyxb.namespace.ExpandedName(None, 'pid')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 254, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GenericControllerPluginDefType._Automaton = _BuildAutomaton_35()




ImageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'width'), pyxb.binding.datatypes.integer, scope=ImageType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 312, 10)))

ImageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), pyxb.binding.datatypes.integer, scope=ImageType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 313, 10)))

ImageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'format'), pyxb.binding.datatypes.string, scope=ImageType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 314, 10)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 311, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 314, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ImageType._UseForTag(pyxb.namespace.ExpandedName(None, 'width')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 312, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ImageType._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 313, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ImageType._UseForTag(pyxb.namespace.ExpandedName(None, 'format')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 314, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ImageType._Automaton = _BuildAutomaton_36()




ClipType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'near'), pyxb.binding.datatypes.double, scope=ClipType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 323, 10)))

ClipType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'far'), pyxb.binding.datatypes.double, scope=ClipType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 324, 10)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 322, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClipType._UseForTag(pyxb.namespace.ExpandedName(None, 'near')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 323, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClipType._UseForTag(pyxb.namespace.ExpandedName(None, 'far')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 324, 10))
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
ClipType._Automaton = _BuildAutomaton_37()




NoiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), pyxb.binding.datatypes.string, scope=NoiseType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 333, 10)))

NoiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mean'), pyxb.binding.datatypes.double, scope=NoiseType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 334, 10)))

NoiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stddev'), pyxb.binding.datatypes.double, scope=NoiseType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 335, 10)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 332, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NoiseType._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 333, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NoiseType._UseForTag(pyxb.namespace.ExpandedName(None, 'mean')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 334, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NoiseType._UseForTag(pyxb.namespace.ExpandedName(None, 'stddev')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 335, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NoiseType._Automaton = _BuildAutomaton_38()




CameraType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'horizontal_fov'), pyxb.binding.datatypes.double, scope=CameraType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 344, 10)))

CameraType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), ImageType, scope=CameraType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 345, 10)))

CameraType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'clip'), ClipType, scope=CameraType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 346, 10)))

CameraType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'noise'), NoiseType, scope=CameraType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 347, 10)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 343, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 344, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 345, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 346, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 347, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CameraType._UseForTag(pyxb.namespace.ExpandedName(None, 'horizontal_fov')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 344, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CameraType._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 345, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CameraType._UseForTag(pyxb.namespace.ExpandedName(None, 'clip')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 346, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CameraType._UseForTag(pyxb.namespace.ExpandedName(None, 'noise')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 347, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CameraType._Automaton = _BuildAutomaton_39()




GazeboSensorBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pose'), pyxb.binding.datatypes.string, scope=GazeboSensorBaseType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 357, 10), unicode_default='0 0 0 0 0 0'))

GazeboSensorBaseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'update_rate'), pyxb.binding.datatypes.double, scope=GazeboSensorBaseType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 358, 10), unicode_default='0'))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 355, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 356, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 357, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 358, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GazeboSensorBaseType._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 357, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GazeboSensorBaseType._UseForTag(pyxb.namespace.ExpandedName(None, 'update_rate')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 358, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GazeboSensorBaseType._Automaton = _BuildAutomaton_40()




GazeboType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'plugin'), GazeboPluginType, scope=GazeboType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 388, 10)))

GazeboType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sensor'), GazeboSensorType, scope=GazeboType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 389, 10)))

GazeboType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'material'), GazeboMaterialType, scope=GazeboType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 390, 10)))

GazeboType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gravity'), pyxb.binding.datatypes.boolean, scope=GazeboType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 391, 10)))

GazeboType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'self_collide'), pyxb.binding.datatypes.boolean, scope=GazeboType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 392, 10)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 387, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboType._UseForTag(pyxb.namespace.ExpandedName(None, 'plugin')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 388, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboType._UseForTag(pyxb.namespace.ExpandedName(None, 'sensor')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 389, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboType._UseForTag(pyxb.namespace.ExpandedName(None, 'material')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 390, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboType._UseForTag(pyxb.namespace.ExpandedName(None, 'gravity')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 391, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboType._UseForTag(pyxb.namespace.ExpandedName(None, 'self_collide')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 392, 10))
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
GazeboType._Automaton = _BuildAutomaton_41()




RobotType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'joint'), JointType, scope=RobotType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 404, 10)))

RobotType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'link'), LinkType, scope=RobotType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 405, 10)))

RobotType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transmission'), TransmissionType, scope=RobotType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 406, 10)))

RobotType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gazebo'), GazeboType, scope=RobotType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 407, 10)))

RobotType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'material'), MaterialType, scope=RobotType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 408, 10)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 403, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RobotType._UseForTag(pyxb.namespace.ExpandedName(None, 'joint')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 404, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RobotType._UseForTag(pyxb.namespace.ExpandedName(None, 'link')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 405, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RobotType._UseForTag(pyxb.namespace.ExpandedName(None, 'transmission')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 406, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RobotType._UseForTag(pyxb.namespace.ExpandedName(None, 'gazebo')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 407, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RobotType._UseForTag(pyxb.namespace.ExpandedName(None, 'material')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 408, 10))
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
RobotType._Automaton = _BuildAutomaton_42()




GazeboPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'robotNamespace'), pyxb.binding.datatypes.string, scope=GazeboPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 265, 16)))

GazeboPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'robotSimType'), pyxb.binding.datatypes.string, scope=GazeboPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 266, 16)))

GazeboPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'robotParam'), pyxb.binding.datatypes.string, scope=GazeboPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 267, 16)))

GazeboPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'controller'), GenericControllerPluginDefType, scope=GazeboPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 268, 16)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 264, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'robotNamespace')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 265, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'robotSimType')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 266, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'robotParam')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 267, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GazeboPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'controller')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 268, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GazeboPluginType._Automaton = _BuildAutomaton_43()




GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'baseline'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 281, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'alwaysOn'), pyxb.binding.datatypes.boolean, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 282, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'updateRate'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 283, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cameraName'), pyxb.binding.datatypes.string, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 284, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'imageTopicName'), pyxb.binding.datatypes.string, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 285, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'depthImageTopicName'), pyxb.binding.datatypes.string, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 286, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cameraInfoTopicName'), pyxb.binding.datatypes.string, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 287, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'depthImageCameraInfoTopicName'), pyxb.binding.datatypes.string, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 288, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'frameName'), pyxb.binding.datatypes.string, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 289, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'hackBaseline'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 290, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'distortionK1'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 291, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'distortionK2'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 292, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'distortionK3'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 293, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'distortionT1'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 294, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'distortionT2'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 295, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'CxPrime'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 296, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cx'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 297, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Cy'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 298, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'focalLength'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 299, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pointCloudCutoff'), pyxb.binding.datatypes.double, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 300, 18)))

GazeboCameraPluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pointCloudTopicName'), pyxb.binding.datatypes.string, scope=GazeboCameraPluginType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 301, 18)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 280, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 281, 18))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 282, 18))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 283, 18))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 284, 18))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 285, 18))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 286, 18))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 287, 18))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 288, 18))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 289, 18))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 290, 18))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 291, 18))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 292, 18))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 293, 18))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 294, 18))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 295, 18))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 296, 18))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 297, 18))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 298, 18))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 299, 18))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 300, 18))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 301, 18))
    counters.add(cc_21)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'baseline')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 281, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'alwaysOn')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 282, 18))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'updateRate')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 283, 18))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'cameraName')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 284, 18))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'imageTopicName')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 285, 18))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'depthImageTopicName')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 286, 18))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'cameraInfoTopicName')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 287, 18))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'depthImageCameraInfoTopicName')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 288, 18))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'frameName')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 289, 18))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'hackBaseline')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 290, 18))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'distortionK1')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 291, 18))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'distortionK2')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 292, 18))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'distortionK3')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 293, 18))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'distortionT1')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 294, 18))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'distortionT2')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 295, 18))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'CxPrime')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 296, 18))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'Cx')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 297, 18))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'Cy')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 298, 18))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'focalLength')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 299, 18))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'pointCloudCutoff')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 300, 18))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(GazeboCameraPluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'pointCloudTopicName')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 301, 18))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_10, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_11, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_12, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_13, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_14, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_15, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_16, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_17, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_18, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_19, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_20, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_21, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GazeboCameraPluginType._Automaton = _BuildAutomaton_44()




GazeboSensorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'camera'), CameraType, scope=GazeboSensorType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 371, 14)))

GazeboSensorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'plugin'), GazeboCameraPluginType, scope=GazeboSensorType, location=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 372, 14)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 355, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 356, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 357, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 358, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 370, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 371, 14))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 372, 14))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GazeboSensorType._UseForTag(pyxb.namespace.ExpandedName(None, 'pose')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 357, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GazeboSensorType._UseForTag(pyxb.namespace.ExpandedName(None, 'update_rate')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 358, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(GazeboSensorType._UseForTag(pyxb.namespace.ExpandedName(None, 'camera')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 371, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(GazeboSensorType._UseForTag(pyxb.namespace.ExpandedName(None, 'plugin')), pyxb.utils.utility.Location('/home/igor/dev/hbp/RobotDesigner/resources/urdf.xsd', 372, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_3, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True),
        fac.UpdateInstruction(cc_5, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GazeboSensorType._Automaton = _BuildAutomaton_45()

