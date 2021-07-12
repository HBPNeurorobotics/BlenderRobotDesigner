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

# System imports
import os
import sys
import unittest
import pyxb
import osim_dom


class XmlBuildLearningTest(unittest.TestCase):
    def runTest(self):
        # generate bindings by $pyxbgen-py3 -u osim_muscles.xsd -m osim_dom
        # Note: Use the pyxbgen that comes with the blender install. That is
        # because even minor version mismatches of the generated xsd bindings
        # with the included pyxb version will cause errors.
        doc = osim_dom.OpenSimDocument()
        doc.Model = pyxb.BIND(
            ForceSet=pyxb.BIND(
                objects=pyxb.BIND(
                    Millard2012EquilibriumMuscle=[], Millard2012AccelerationMuscle=[]
                )
            )
        )

        m = osim_dom.Millard2012EquilibriumMuscle(
            GeometryPath=osim_dom.GeometryPath(
                PathPointSet=pyxb.BIND(objects=pyxb.BIND(PathPoint=[]))
            ),
            max_isometric_force=1000.0,
            optimal_fiber_length=0.01,
            tendon_slack_length=0.01,
        )

        pps = m.GeometryPath.PathPointSet.objects.PathPoint
        pps += [
            osim_dom.PathPoint(
                location=osim_dom.vector3("0. 1. 2."), body="body1", name="pp_body1"
            ),
            osim_dom.PathPoint(
                location=osim_dom.vector3("3. 4. 5."), body="body2", name="pp_body2"
            ),
        ]

        doc.Model.ForceSet.objects.Millard2012EquilibriumMuscle.append(m)
        doc.Version = "??"
        xmlstr = doc.toDOM().toprettyxml()

        # sys.stderr.write("Generated XML:\n"+xmlstr)
        newdoc = osim_dom.CreateFromDocument(xmlstr)
        self.assertIsNotNone(newdoc)
        self.assertTrue(newdoc.Model.ForceSet.objects.Millard2012EquilibriumMuscle)


class SchemaSanityCheck(unittest.TestCase):
    def runTest(self):
        import subprocess

        schemafile = os.path.join(
            os.path.dirname(__file__), "..", "..", "resources", "osim_muscles.xsd"
        )
        samplexml = os.path.join(
            os.path.dirname(__file__), "test_sample_muscle_file.osim"
        )
        out = subprocess.check_output(["xmllint", "-schema", schemafile, samplexml])


class SchemaSanityCheckBindings(unittest.TestCase):
    def runTest(self):
        with open(
            os.path.join(os.path.dirname(__file__), "test_sample_muscle_file.osim"), "r"
        ) as f:
            sample_xml = f.read()
        osim_dom.CreateFromDocument(sample_xml)


if __name__ == "__main__":
    unittest.main()
