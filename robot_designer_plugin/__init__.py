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

from importlib import reload
import sys
import os

try:

    from . import core
    reload(core)  # Must be the first to reload


    third_party_path = os.path.join(core.config.resource_path,'third-party')
    if third_party_path not in sys.path:
        sys.path.append(third_party_path)

except Exception as e:
    print("Could not load core functionality!", type(e).__name__, e)
    raise e
    def register(): pass
    def unregister(): pass

try:
    from . import export
    from . import interface
    from . import operators
    from . import properties

    core.PluginManager.clear()

    reload(operators)
    reload(properties)
    reload(export)
    reload(interface)

    core.PluginManager.load_icon('hbp', 'icons/hbp.png')

    def register():
        import sys

        additionalModulePath = True
        try:
            from . import generatedAdditionalModulePath
        except ImportError:
            additionalModulePath = False

        if (additionalModulePath):
            print('Adding the following path to sys.path: ' + str(generatedAdditionalModulePath.venvPath))
            sys.path = sys.path + generatedAdditionalModulePath.venvPath

        core.PluginManager.register()


    def unregister():
        import sys
        core.PluginManager.unregister()

        additionalModulePath = True
        try:
            from . import generatedAdditionalModulePath
        except ImportError:
            additionalModulePath = False
        if (additionalModulePath):
            for path in generatedAdditionalModulePath.venvPath:
                sys.path.remove(path)

except Exception as e:
    from .core.logfile import RD_logger, EXCEPTION_MESSAGE, log_callstack
    RD_logger.error("Could not import submodules:\n" + EXCEPTION_MESSAGE,
                    type(e).__name__, e, log_callstack(), log_callstack(True))

    def register(): pass
    def unregister(): pass



bl_info = {
    "name": "NRP Robot Designer",
    "author": "Stefan Ulbrich (FZI), Michael Bechtel",
    "version": (0, 1),
    "blender": (2, 69, 0),
    "location": "View3D > Tools",
    "category": "Editor"}

additionalModulePath = True


