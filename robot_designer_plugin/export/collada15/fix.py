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
#


import xml.etree.cElementTree as etree

# Blender-specific imports (catch exception for sphinx documentation)
import bpy


def fixCollada(in_filename, out_filename, context):
    doc = etree.parse(in_filename)
    root = doc.getroot()

    for obj in [i for i in context.scene.objects if i.type == 'MESH']:
        if obj.parent is not None:
            element = root.find(
                './/{http://www.collada.org/2005/11/COLLADASchema}node[@name="%s"][@type="NODE"]' % obj.name.replace(
                    '.', '_'))
            if element is not None:  # sometimes, element is None
                # Latest discovery: bpy.types.object.matrix_local_inverse()
                # gives only the matrix at the time of parenting!
                # bpy.types.bone.matrix_local() gives the matrix of the bone at rest position!
                ns = "{http://www.collada.org/2005/11/COLLADASchema}"
                matrix = etree.Element(ns + "matrix")
                if obj.parent_bone != "":
                    bone = obj.parent.data.bones[obj.parent_bone]
                    if bone.RobotDesigner.jointMode == "REVOLUTE":
                        # TODO: Place the transformation for the joint here!
                        pass

                    matrix.text = " ".join([str(j) for i in bone.matrix_local.inverted() for j in i])
                    matrix.set('sid', 'Inverted')
                    # matrix.text = " ".join([str(j) for i in list(obj.matrix_local_inverse) for j in i])
                    element.insert(0, matrix)
                if obj.parent.RobotDesigner.tag == "PHYSICS_FRAME":
                    for parent in root.iter():
                        if element in parent:
                            parent.remove(element)
                            break

    doc.write(out_filename, encoding="UTF-8")
