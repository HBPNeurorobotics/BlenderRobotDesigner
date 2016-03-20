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
#   2016-01-15: Stefan Ulbrich (FZI) (FZI Forschungszentrum Informatik)
#       Template created
#   Today: Your Name
#       Please add ALWAYS your modifications
#

from .pluginmanager import PluginManager
import bpy
from bpy.props import PointerProperty, FloatProperty, StringProperty

class PropertyWrapper(object):
    def __init__(self, property):
        self.property = property
        self.reference = []

    def get(self, obj):
        obj = getattr(obj,"RobotDesigner")
        for i in self.reference:
            obj = getattr(obj, i)
        return obj

    def prop(self, obj, layout, *args, **kwargs):
        obj = getattr(obj,'RobotDesigner')
        for i in self.reference[:-1]:
            obj = getattr(obj,i)

        layout.prop(obj, self.reference[-1], *args, **kwargs)

    def prop_search(self, obj, layout, *args, **kwargs):
        obj = getattr(obj,'RobotDesigner')
        for i in self.reference[:-1]:
            obj = getattr(obj,i)

        layout.prop_search(obj, self.reference[-1], *args, **kwargs)




class PropertyGroupWrapperBase(object):
    def register(self, btype, parent=[]):

        newPropertyGroup = type(self.__class__.__name__ + "_unwrapped", (bpy.types.PropertyGroup,), {})

        for attr in self.__dict__.items():
            if isinstance(attr[1], PropertyWrapper):
                attr[1].property[1]['attr'] = attr[0]
                # print(attr[0], attr[1].d)
                property=attr[1].property
                setattr(newPropertyGroup, attr[0], property) # property[0](**property[1]))
                attr[1].reference = parent + [attr[0]]
            elif isinstance(attr[1], PropertyGroupWrapperBase):
                pg = attr[1].register(None, parent + [attr[0]])
                print(type(pg), pg.__bases__)
                p = PointerProperty(type=pg)
                p[1]['attr'] = attr[0]
                setattr(newPropertyGroup, attr[0], p)

        print("!!!Registering this class to blender:", newPropertyGroup.__name__, newPropertyGroup.__dict__)
        bpy.utils.register_class(newPropertyGroup)
        PluginManager._registered_properties.append((newPropertyGroup,btype))
        if btype:
            setattr(btype,'RobotDesigner',
                    bpy.props.PointerProperty(type=getattr(bpy.types, newPropertyGroup.__name__)))
            print("Assigning property to:", btype)
        return newPropertyGroup


class PropertyGroupWrapper1(PropertyGroupWrapperBase):
    def __init__(self):
        print("Initializing %s" % self.__class__.__name__)
        self.y = PropertyWrapper(FloatProperty(name="min. Velocity", precision=4, step=100))


class GuiProperties(PropertyGroupWrapperBase):
    def __init__(self):
        self.selected_mesh = PropertyWrapper(StringProperty(name="meshName"))

class GlobalProperties(PropertyGroupWrapperBase):
    def __init__(self):
        self.gui_properties = GuiProperties()

class PropertyGroupWrapper2(PropertyGroupWrapperBase):
    def __init__(self):
        print("Initializing %s" % self.__class__.__name__)
        self.x = PropertyWrapper(FloatProperty(name="max. Velocity", precision=4, step=100))
        self.z = PropertyGroupWrapper1()

pgw2 = PropertyGroupWrapper2()
pgw2.register(bpy.types.Bone)

global_properties = GlobalProperties()
global_properties.register(bpy.types.Scene)