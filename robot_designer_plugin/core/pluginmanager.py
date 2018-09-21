# #####
# This file is part of the RobotDesigner of the Neurorobotics subproject (SP10)
# in the Human Brain Project (HBP).
# It has been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
# developed at the Karlsruhe Institute of Technology in the
# High Performance Humanoid Technologies Laboratory (H2T).
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

# #####
#
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#
#   2016-01-15: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######
"""
This sub module contains the :class:`PluginManager` that handles automatic registration of classes.
"""
import inspect
from enum import Enum
import os

import bpy
import bpy.utils

from .config import EXCEPTION_MESSAGE, resource_path
from .logfile import core_logger, log_callstack
from .operators import RDOperator
from .gui import CollapsibleBase


class PluginManager(object):
    """
    This class handles the automatic registration of classes to Blender.
    """

    _classes_to_register = []
    _registered_classes = []
    _property_groups_to_register = []
    _registered_properties = []
    _file_plugins = []
    _bools_to_register = []
    _registered_bools = []
    PluginTypes = Enum('PluginType', 'FILE GEOMETRY SEGMENTS MODEL')

    _bl_icons_dict = None
    _icons_to_register = []
    _property_fields = {}

    @staticmethod
    def register_property_group(base=None):

        propertyTypes = (bpy.props.EnumProperty, bpy.props.StringProperty, bpy.props.BoolProperty,
                         bpy.props.StringProperty,
                         bpy.props.PointerProperty)

        def decorator(cls):
            if issubclass(cls, bpy.types.PropertyGroup):
                # RD_logger.info("Dependencies: %s", base)
                PluginManager._property_groups_to_register.append((cls, base))
            return cls

        return decorator

    # bpy.props.PointerProperty(type=robot_designer_plugin.properties.segments.RDDegreeOfFreedom)[1]['type'] is robot_designer_plugin.properties.segments.RDDegreeOfFreedom



    @staticmethod
    def register_class(*args):
        """
        :term:`Class decorator<class decorator>` for :class:`.operators.RDOperator`, :class:`bpy.types.Menu`,
        :class:`bpy.types.PropertyGroup` (and more ``bpy`` classes) and :class:`.gui.CollapsibleBox`.

        An example of how to use this decorator is given in :class:`.operators.RDOperator`.

        :param args: For now, no arguments should be passed to the decorator.
        """

        def decorator(cls):
            if issubclass(cls, (RDOperator, bpy.types.Menu, bpy.types.Panel, bpy.types.Panel)):
                PluginManager._classes_to_register.append((cls, dependencies))
            elif issubclass(cls, CollapsibleBase):
                PluginManager._bools_to_register.append(cls.property_name)
            else:
                core_logger.error("Could not register %s, subclass of: %s\nDependencies: %s\n%s", cls, cls.mro(),
                                  dependencies, args)

                raise TypeError("Wrong with decorator")
            # print(cls)

            if not cls.__doc__:
                cls.__doc__ = "Missing documentation.\n\n"
            cls.__doc__ += "\n    **Automatically registered** to " \
                           ":class:`robot_designer_plugin.core.pluginmanager.Pluginmanager`\n"
            return cls

        if len(args) == 1 and inspect.isclass(args[0]):  # No arguments

            dependencies = []

            return decorator(args[0])
        else:  # Arguments given to decorator
            dependencies = args
            return decorator

    @classmethod
    def register_property_groups(cls, property_group, btype):
        """
        :term:`Properties<property>` have to be assigned to blender types.
        This function collects all properties and assigns them when :meth:`register` is called
        and unloads them when :meth:`unregister` is called.

        :param property_group: A class derived from :class:`bpy.types.PropertyGroup`.
        :param btype: Any type defined in :mod:`bpy.types`.
        :return:
        """
        # cls._property_groups_to_register.append((property_group, btype))

        # props = inspect.getmembers(property_group, lambda x: isinstance(x, tuple) and len(x) == 2)
        # print(props)
        # cls._property_fields[property_group]=[]
        # for name, prop in props:
        #     cls._property_fields[property_group].append((name, prop))
        #
        # for nested in inspect.getmembers(property_group, lambda x: isinstance(x, bpy.types.PropertyGroup)):
        #     cls._property_fields[property_group].append(
        #
        #     )

    @classmethod
    def register_plugin(cls, label, operators, draw_function=None, type_=PluginTypes.FILE):
        """
        .. warning::

            The plugin system is still under development.
        """
        cls._file_plugins.append((label, operators, draw_function, type_))

    @classmethod
    def get_property(cls, property):
        """
        .. warning::

            Better handling of properties is still under development.

        """
        return property[1]['attr']

    @classmethod
    def getFilePlugins(cls, type_=PluginTypes.FILE):
        """
        .. warning::

            The plugin system is still under development.
        """
        return cls._file_plugins

    @classmethod
    def register_collapsible(cls, property_name):
        """
        Called when a class of type :class:`.gui.CollapsibleBox` is created.
        """
        cls._bools_to_register.append(property_name)

    @classmethod
    def load_icon(cls, id: str, filename: str):
        '''

        :param id: ID of the label
        :param filename: Relative to :data:`.config/resource_path`
        :return: None
        '''
        file_path = os.path.join(resource_path, filename)
        if not os.path.exists(file_path):
            core_logger.debug("File does not exist: %s", file_path)
        else:
            cls._icons_to_register.append((id, file_path, 'IMAGE'))

    @classmethod
    def get_icon(cls, id: str):
        '''

        :param id:
        :return:
        '''

        if cls._bl_icons_dict and id in cls._bl_icons_dict:
            return cls._bl_icons_dict[id].icon_id
        else:
            return 0

    @classmethod
    def clear(cls):
        """
        When a plugin is required to be reloadable (which it should be during development) each module is imported
        twice. Therefore, this method is called before the modules are reloaded.
        """
        cls._classes_to_register.clear()
        cls._property_groups_to_register.clear()
        cls._bools_to_register.clear()
        cls._icons_to_register.clear()

    @classmethod
    def get_property(cls, obj, prop):
        '''

        :param obj:
        :param prop:
        :return:
        '''
        args, varargs, keywords, locals = inspect.getargvalues(inspect.currentframe())
        print(args, varargs, keywords, locals)

    @classmethod
    def register(cls):
        """
        Called from the top-level :func:`robot_designer_plugin.register` function in the ``__init__.py`` of the plugin.
        Registers all data collected during import.
        """
        report = ['\n']
        try:
            for class_, dependencies in cls._classes_to_register:
                bpy.utils.register_class(class_)
                report.append('\t+ class {0:35} in {1:40}'.format(class_.__name__,
                                                                  "/".join(class_.__module__.split('.')[1:])))
                cls._registered_classes.append(class_)
            core_logger.info('Done')

            core_logger.debug("Properties: %s", cls._property_groups_to_register)
            for prop, extends in cls._property_groups_to_register:
                report.append("\t+ propery {0:33} {1:8} in {2:40}".format(prop.__name__,
                                                                          "(%s)" % extends.__name__ if extends else '',
                                                                          "/".join(prop.__module__.split('.')[1:])))

                bpy.utils.register_class(prop)
                if extends in (bpy.types.Object, bpy.types.Scene, bpy.types.Bone):
                    setattr(extends, 'RobotDesigner', bpy.props.PointerProperty(type=getattr(bpy.types, prop.__name__)))
                cls._registered_properties.append((prop, extends))

            for i in cls._property_fields.items():
                print(i)

            for prop in cls._bools_to_register:
                setattr(bpy.types.Scene, prop, bpy.props.BoolProperty())
                cls._registered_bools.append(prop)

            if cls._icons_to_register:
                cls._bl_icons_dict = bpy.utils.previews.new()

                for icon in cls._icons_to_register:
                    report.append("\t+ icon {0:36} from {1:40}".format(icon[0], icon[1]))
                    cls._bl_icons_dict.load(*icon)
            core_logger.info("\n".join(report))

        except Exception as e:
            report.append("Error occured")
            core_logger.info("\n".join(report))
            core_logger.error(EXCEPTION_MESSAGE,
                              type(e).__name__, e, log_callstack(), log_callstack(back_trace=True))

        cls.clear()

    @classmethod
    def unregister(cls):
        """
        Called from the top-level :func:`robot_designer_plugin.unregister` function in the ``__init__.py`` of the
        plugin.
        Removes all data collected during import.
        """
        report = ['\n']
        try:
            for class_ in cls._registered_classes:
                bpy.utils.unregister_class(class_)
                report.append("\t- class {0:35} in {1:40}".format(class_.__name__,
                                                                  "/".join(class_.__module__.split('.')[1:])))

            for prop, extends in cls._registered_properties:
                bpy.utils.unregister_class(prop)
                if extends in (bpy.types.Object, bpy.types.Scene, bpy.types.Bone):
                    delattr(extends, "RobotDesigner")

            for prop in cls._registered_bools:
                delattr(bpy.types.Scene, prop)

            core_logger.info("\n".join(report))

            if cls._bl_icons_dict:
                bpy.utils.previews.remove(cls._bl_icons_dict)

        except Exception as e:
            report.append("Error occured during clean up. You should restart blender!")
            core_logger.info("\n".join(report) + '\n')
            core_logger.error(EXCEPTION_MESSAGE,
                              type(e).__name__, e, log_callstack(), log_callstack(back_trace=True))

        cls._registered_classes.clear()
        cls._property_groups_to_register.clear()
        cls._registered_bools.clear()
