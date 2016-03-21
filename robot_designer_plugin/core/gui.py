# # This file is part of the RobotDesigner of the Neurorobotics subproject (SP10)
# in the Human Brain Project (HBP).
# It has been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
# developed at the Karlsruhe Institute of Technology in the
# High Performance Humanoid Technologies Laboratory (H2T).
# 
# #
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
# 
# #
# Copyright (c)
#
# Changes:
#
#   2016-01-15: Stefan Ulbrich (FZI), First version of the plugin framework core
#
"""
This submodule provides helper classes for creating blender guis.
"""


class InfoBox(object):
    """
    This class collects messages (e.g., from :meth:`.operators.operators.RDOperator.poll`) and displays them
    with an info, either in a separated box or the current layout.

    See :ref:`gui_develpment` for an example.
    """

    global_message=[]

    def __init__(self, layout):
        """
        Constructor.

        :param layout: Blender gui element as passed to the
            :meth:`robot_designer_plugin.interface.main.UserInterface.draw` method.
        """
        self.messages = []
        self.layout = layout

    def add_message(self, message):
        """
        Adds a string message to the info box.

        :param message: message
        :type message: str
        """
        self.messages.append(message)

    def draw_info(self, additional_messages=[]):
        """
        Draws the info box onto the layout.

        :param additional_messages: Additional messages can be appended.
        """
        messages = self.messages + additional_messages
        if messages:

            column = self.layout.column(align=True)
            for text in set(messages):
                column.label(text=text, icon='INFO')

    @classmethod
    def draw_global_info(cls, layout):
        if cls.global_message:
            box = layout.box()
            ib = InfoBox(layout)
            ib.draw_info(additional_messages=cls.global_message)


class CollapsibleBase(object):
    """
    By default, Blender does not offer collapsible boxes. For this, this create subclasses and use the
    :meth:`.pluginmanager.PluginManager.register` decorator. This decorator creates a boolean property
    that is stored with the :term:`scene` object (and is therefore persistent with your current file)
    that is used for remembering the state of the box.
    The subclass needs to specify a unique identifier for a :class:`bpy.types.BoolProperty` in the attribute
    ``property_name`` attribute, for instance:

    .. code-block:: python

        @PluginManager.register_class
        class ControllerBox(CollapsibleBase):
            property_name="controller_box"

    This parameter is used in the :meth:`.pluginmanager.PluginManager.register` method which calls
    :meth:`.pluginmanager.PluginManager.register_collapsible`
    """

    @classmethod
    def get(cls, layout, context, label, icon='NONE'):
        """
        Create a collapsible box element and adds it to the gui element

        :param layout: Blender gui element as passed to the
            :meth:`robot_designer_plugin.interface.main.UserInterface.draw` method.
        :param context: Blender context object (see above)
        :param label: Label label of the box
        :param icon: optionally place a label (must be a name known to Blender)
        """
        box = layout.box()
        row = box.row()
        row.prop(context.scene, cls.property_name,
                 icon="TRIA_DOWN" if getattr(context.scene, cls.property_name) else "TRIA_RIGHT",
                 icon_only=True, emboss=False
                 )
        row.label(text=label, icon=icon)
        if getattr(context.scene, cls.property_name):
            return box
        else:
            return None
