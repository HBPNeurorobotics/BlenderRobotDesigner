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

bl_info = {
    "name": "RobotEditor",
    "author": "Stefan Ulbrich, Michael Bechtel",
    "version": (0, 3),
    "blender": (2, 69, 0),
    "location": "View3D > Tools",
    "category": "Editor"}

import bpy


def register():
    from . import properties
    from . import main
    from . import armatures
    from . import bones
    from . import meshes
    from . import markers
    from . import physics
    from . import files

    properties.register()
    main.init()
    main.register()
    armatures.register()
    bones.register()
    meshes.register()
    markers.register()
    physics.register()
    files.register()
    # bpy.utils.register_module(__name__)


def unregister():
    from . import properties
    from . import main
    from . import armatures
    from . import bones
    from . import meshes
    from . import physics
    from . import files

    properties.unregister()
    main.unregister()
    armatures.unregister()
    bones.unregister()
    meshes.unregister()
    markers.unregister()
    physics.unregister()
    files.unregister()
    # bpy.utils.unregister_module(__name__)
