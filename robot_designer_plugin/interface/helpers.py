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
# Copyright (c) 2015, Karlsruhe Institute of Technology (KIT)
# Copyright (c) 2016, FZI Forschungszentrum Informatik
#
# Changes:
#   2015:       Stefan Ulbrich (FZI), Gui redesigned
#   2015-01-16: Stefan Ulbrich (FZI), Major refactoring. Integrated into complex plugin framework.
#
# ######

# RobotDesigner imports
from . import menus
from ..core import Condition
from ..core.gui import CollapsibleBase
from ..core.pluginmanager import PluginManager
from ..properties.globals import global_properties

@PluginManager.register_class
class DisconnectGeometryBox(CollapsibleBase):
    property_name = "disconnect_geometry_box"


@PluginManager.register_class
class ConnectGeometryBox(CollapsibleBase):
    property_name = "connect_geometry_box"


@PluginManager.register_class
class CollisionBox(CollapsibleBase):
    property_name = "collision_box"


@PluginManager.register_class
class DeformableBox(CollapsibleBase):
    property_name = "deformable_box"


@PluginManager.register_class
class ModelPropertiesBox(CollapsibleBase):
    property_name = "coordinate_frame_box"


@PluginManager.register_class
class ControllerLimitsBox(CollapsibleBase):
    property_name = "controller_limits_box"


@PluginManager.register_class
class ControllerBox(CollapsibleBase):
    property_name = "controller_box"


@PluginManager.register_class
class MeshGenerationBox(CollisionBox):
    property_name = "mesh_generation_box"

@PluginManager.register_class
class AttachSensorBox(CollapsibleBase):
    property_name = "attach_sensor_box"

@PluginManager.register_class
class DetachSensorBox(CollapsibleBase):
    property_name = "detach_sensor_box"

@PluginManager.register_class
class SensorPropertiesBox(CollapsibleBase):
    property_name = "sensor_properties_box"

info_list = []


def push_info(message_or_condition):
    # Check if list or tuple .. print only if condition is not met.
    if issubclass(message_or_condition, Condition):
        info_list.append(message_or_condition.check()[1])
        print(info_list)
    else:
        info_list.append(message_or_condition)


def getSingleSegment(context):
    global info_list
    selected_segments = [i for i in context.active_object.data.bones if i.select]
    if len(selected_segments) == 1:
        return selected_segments[0]
    else:
        if len(selected_segments) == 0:
            info_list.append("No Segment selected, some operators not available")
        else:
            info_list.append("Multiple segments selected, some operators not available")
    return None

def getSingleObject(context):
    selected = [i for i in context.selected_objects if i.type != "ARMATURE"]
    if len(selected)==1:
        return selected[0]
    else:
        return None

def drawInfoBox(layout, context, infos=[]):
    global info_list

    if info_list + infos:
        box = layout.box()
        column = box.column(align=True)
        for text in info_list + infos:
            print(text)
            if text:
                column.label(text=text, icon='INFO')
        info_list.clear()


def create_segment_selector(layout, context):
    global info_list
    single_segment = getSingleSegment(context)
    layout.menu(menus.SegmentsMenu.bl_idname, text=single_segment.name if single_segment else "Select Segment")
    global_properties.segment_name.prop_search(context.scene, layout, context.active_object.data, 'bones',
                       icon='VIEWZOOM',
                       text='')
