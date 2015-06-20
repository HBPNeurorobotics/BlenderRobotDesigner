"""
The module that encapsulates all blender calls and offers the importer and exporter for the RobotDesigner
"""

__author__ = 'ulbrich'

import urdf_dom
import urdf_tree


def rd_import(file_name):
    """
    asdf
    """
    robot = urdf_tree.URDFTree()
    robot.parse(file_name)

    def load_mesh(name, f, s, o):
        if o is not None:
            pass
        print(name, f, s, o)

    def parse(tree):
        # link information
        for visual in tree.link.visual:
            load_mesh(tree.link.name, visual.geometry.mesh.filename, visual.geometry.mesh.scale, visual.origin)

        for collision in tree.link.collision:
            load_mesh('col_' + tree.link.name, collision.geometry.mesh.filename, collision.geometry.mesh.scale,
                      collision.origin)

        if tree.link.inertial is not None:
            mass = tree.link.inertial.mass.value
            origin = tree.link.inertial.origin
            i = tree.link.inertial.inertia
            if i is not None:
                matrix = [[i.ixx, i.ixz, i.ixz], [i.iyy, i.iyz], [i.izz]]

        # joint information

        if tree.joint is None:
            # The root element
            pass
        else:

            if tree.joint.origin:
                print(tree.joint.origin.xyz, tree.joint.origin.rpy)
            print(tree.joint.axis)
            if tree.joint.dynamics:
                print(tree.joint.dynamics.damping, tree.joint.dynamics.friction)
            if tree.joint.limit:
                print(tree.joint.limit.lower, tree.joint.limit.upper, tree.joint.limit.velocity,
                      tree.joint.limit.effort)

        for sub_tree in tree.children:
            parse(sub_tree)

    # 1.st create the armature

    for child in robot.children:
        parse(child)


# Note: move to different file
def rd_export(file_name):
    """
    """
    pass

# debugging the module
if __name__ == "__main__":
    rd_import("../../models/hollie.urdf")
