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



#  Copyright (c)
#

from .pluginmanager import PluginManager
import bpy
from bpy.props import PointerProperty, FloatProperty, StringProperty
from .logfile import core_logger


class PropertyHandler(object):
    """
    Wraps a Blender property factory functions (e.g., :func:`bpy.props.StringProperty`, :func:`bpy.props.FloatProperty` or
    :func:`bpy.props.IntProperty`). Use it in a :class:`PropertyGroupHandlerBase` instance.
    E.g.:

    .. code-block:: python

        class GuiProperties(PropertyGroupHandlerBase):
            def __init__(self):
                self.selected_mesh = PropertyHandler(StringProperty(name="meshName"))


    """

    def __init__(self, property):
        self.property = property
        self.reference = []

    def get(self, obj):
        """
        Resolves and returns the registered property given a reference to the (correct) object type.

        In the example in :class:`PropertyGroupWrapper`:

        .. code-block:: python

            mesh name = global_properties.gui_properties.selected_mesh.get(context.scene)


        :param obj: A Blender object with additional properties defined by the wrapper classes.
        :return: The property.
        """
        obj = getattr(obj, "RobotDesigner")
        for i in self.reference:
            obj = getattr(obj, i)
        return obj

    def set(self, obj, value):
        obj = getattr(obj, "RobotDesigner")
        for i in self.reference[:-1]:
            obj = getattr(obj, i)
        setattr(obj, self.reference[-1], value)

    def prop(self, obj, layout, *args, **kwargs):
        """
        Resolves and renders a registered property on a GUI :class:`bpy.types.UILayout` object given a
        reference to the (correct) object type.

        In the example in :class:`PropertyGroupWrapper`:

        .. code-block:: python

            def draw(context, layout):
                global_properties.gui_properties.selected_mesh.prop(context.scene)

        Additional positional arguments and keyword arguments are passed to :meth:`bpy.types.UIlayout.prop`

        :param obj: A Blender object with additional properties defined by the wrapper classes.
        :param layout:  A :class:`bpy.types.UIlayout` reference.
        """
        obj = getattr(obj, 'RobotDesigner')
        for i in self.reference[:-1]:
            obj = getattr(obj, i)

        layout.prop(obj, self.reference[-1], *args, **kwargs)

    def prop_search(self, obj, layout, *args, **kwargs):
        """
        Resolves and renders a :meth:`bpy.types.UIlayout.prop_search` connected to a registered property
        on a GUI :class:`bpy.types.UILayout` object given a
        reference to the (correct) object type.

        In the example in :class:`PropertyGroupWrapper`:

        .. code-block:: python

            def draw(context, layout):
                global_properties.gui_properties.selected_mesh.prop_search(context.scene, layout,
                                                     bpy.data,'objects', icon='VIEWZOOM', text='')

        Additional positional arguments and keyword arguments are passed to :meth:`bpy.types.UIlayout.prop`

        :param obj: A Blender object with additional properties defined by the wrapper classes.
        :param layout:  A :class:`bpy.types.UIlayout` reference.
        """
        obj = getattr(obj, 'RobotDesigner')
        for i in self.reference[:-1]:
            obj = getattr(obj, i)

        layout.prop_search(obj, self.reference[-1], *args, **kwargs)


class PropertyGroupHandlerBase(object):
    """
    Base class for wraps a :class:`bpy.types.PropertyGroup`-derived class object. Blender uses those classes as templates
    to dynamically generate properties for existing types (such as :class:`bpy.types.Object` or :class:`bpy.types.Bone`)
    This, however, makes developing cumbersome. Dynamically created properties are usually accessed by:

    .. code-block:: python

        context.current_object.plugin.propertygroup1.propertygroup2.property

    which cannot be resolved during programming time (as it is dynamically generated and aggregated to the blender
    objects. Using this wrapper class, you can build a delegation class structure that is known during programming
    and, therefore, for code completion and static analysis.

    Example:

    .. code-block:: python

        class GuiProperties(PropertyGroupHandlerBase):
        def __init__(self):
            self.selected_mesh = PropertyHandler(StringProperty(name="meshName"))

        class GlobalProperties(PropertyGroupHandlerBase):
            def __init__(self):
                self.gui_properties = GuiProperties()

        global_properties = GlobalProperties()
        global_properties.register(bpy.types.Scene)

    When calling the :meth:`register` method, the plugin core creates the class templates for Blender dynamically
    and registeres them to the software.
    """

    def register(self, btype, parent=[]):
        """
        Register the wrapped property group to blender. This needs only be called for property groups directly
        assigned to a blender type. Nested groups are automatically registered.

        .. todo::

            Register should use the standard registration mechanism of PluginManager. Right now, however,
            this would break the current registration process. This will be done once the properties for
            the robot designer have been clarified and migrated to this representation.

        @param btype: Blender type (e.g. :class:`bpy.types.Object` or :class:`bpy.types.Bone`)
        @param parent: For traversing nested groups
        @return: Reference to the generated :class:`bpy.types.PropertyGroup`-derived class (not used by the user).
        """

        if bpy.app.version == 'Mockup':
            return

        newPropertyGroup = type(self.__class__.__name__ + "_unwrapped", (bpy.types.PropertyGroup,), {'__annotations__': {}})

        for attr in self.__dict__.items():
            if isinstance(attr[1], PropertyHandler):

                attr[1].property[1]['attr'] = attr[0]
                property = attr[1].property

                newPropertyGroup.__annotations__.update({attr[0]: property})
                attr[1].reference = parent + [attr[0]]

            elif isinstance(attr[1], PropertyGroupHandlerBase):
                pg = attr[1].register(None, parent + [attr[0]])
                print(type(pg), pg.__bases__)
                p = PointerProperty(type=pg)
                p[1]['attr'] = attr[0]
                setattr(newPropertyGroup, attr[0], p)

        core_logger.debug("Registering generated property group: %s", newPropertyGroup.__name__)

        bpy.utils.register_class(newPropertyGroup)
        PluginManager._registered_properties.append((newPropertyGroup, btype))
        if btype:
            setattr(btype, 'RobotDesigner',
                    bpy.props.PointerProperty(type=newPropertyGroup))
            '''
            According to blender: 
            Classes registered by addons are no longer available in bpy.types. 
            Instead addons can import their own modules and access the classes directly.
            This is probably why the above code isn't working. But how to do it then? 
            '''
            core_logger.debug("Assigning property to: %s", btype)
        return newPropertyGroup
