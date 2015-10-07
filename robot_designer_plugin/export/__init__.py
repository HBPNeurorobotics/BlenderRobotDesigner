"""
This module includes import and export functions for different file formats for robot descriptions.
"""

from . import urdf
# todo add all import export plugins into this directory. The file dialog should have a selection box for the format
# todo that includes all plugins and draw the operators and arguments required (a draw function has to be included)
__author__ = 'ulbrich'


# draft for creating a plugin mechanism
plugins = [('urdf', 'URDF', '.urdf', True, True), ('sdf', 'SDF', '.sdf', True, True),
           ('simox', 'SIMOX XML', '.xml', True, False), ('collada', 'COLLADA v1.5', '.dae', False, True)]
