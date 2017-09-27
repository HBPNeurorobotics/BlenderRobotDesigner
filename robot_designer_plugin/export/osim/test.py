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
          Millard2012EquilibriumMuscle = [],
          Millard2012AccelerationMuscle = []
        )
      )
    )

    m = osim_dom.Millard2012EquilibriumMuscle(
      GeometryPath=osim_dom.GeometryPath(
        PathPointSet = pyxb.BIND(
          objects = pyxb.BIND(
            PathPoint = []
          )
        )
      ),
      max_isometric_force = 1000.,
      optimal_fiber_length = 0.01,
      tendon_slack_length = 0.01
    )

    pps = m.GeometryPath.PathPointSet.objects.PathPoint
    pps += [
      osim_dom.PathPoint(
        location = osim_dom.vector3("0. 1. 2."),
        body = "body1",
        name = "pp_body1"
      ),
      osim_dom.PathPoint(
        location=osim_dom.vector3("3. 4. 5."),
        body="body2",
        name="pp_body2"
      )
    ]

    doc.Model.ForceSet.objects.Millard2012EquilibriumMuscle.append(m)

    doc.Version = "??"

    xmlstr = doc.toDOM().toprettyxml()

    print("---- Generated XML: ------")
    print(xmlstr)

    newdoc = osim_dom.CreateFromDocument(xmlstr)

    print("---- Loaded Doc: -------")
    print(newdoc)
    self.assertIsNotNone(newdoc)
    print("Is the muscle present?")
    print(newdoc.Model.ForceSet.objects.Millard2012EquilibriumMuscle)
    self.assertTrue(newdoc.Model.ForceSet.objects.Millard2012EquilibriumMuscle)

if __name__ == '__main__':
  unittest.main()