# #####
#  This file is part of the RobotDesigner developed in the Neurorobotics subproject
#  of the Human Brain Project (https://www.humanbrainproject.eu).
#
#  The Human Brain Project is a European Commission funded project
#  in the frame of the Horizon2020 FET Flagship plan.
#  (http://ec.europa.eu/programmes/horizon2020/en/h2020-section/fet-flagships)
#
#  The Robot Designer has initially been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
#  developed at the Karlsruhe Institute of Technology in the
#  High Performance Humanoid Technologies Laboratory (H2T).
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

import xml.etree.cElementTree as etree

from pprint import pprint


class Tree(object):
    def __init__(self, name='armature'):
        self.children = []
        self.name = name
        self.transformations = []
        self.frame_origin = 'False'
        self.frame_tip = 'False'
        self.meshes = None
        self.markers = None
        self.speed = 0.0
        self.acceleration = 0.0
        self.deceleration = 0.0
        self.jerk = 0.0
        self.min = 0
        self.max = 0
        self.active = 'True'
        self.locked = 'False'
        self.initialValue = 0.0
        self.axis_type = None
        self.axis = None
        self.isGripper = None
        self.closingDirection = 1.0


def tolower(element):
    """Convert all element tags to lower (i.e., ignore case)"""
    element.tag = element.tag.lower()
    for i in element.getchildren():
        tolower(i)


# def inv(m):
#    m2=[]
#    for i in range(0,3):
#        row = []
#        for j in range(0,3):
#            row.append(m[j][i])
#        row.append(-m[i][3])
#        m2.append(row)
#    m2.append([0,0,0,1])
#    return m2

def parse(element, root):
    """Parse the document tree and store the extracted information in the tree class."""
    matrix = element.find('transform/matrix4x4')
    M = []
    if matrix is not None:
        print(element.get('name'))

        for i in range(1, 5):
            row = []
            for j in range(1, 5):
                row.append(float(matrix.find('row%d' % i).get('c%d' % j)))
            M.append(row)
            #        M=Matrix(M)
            #        T.append(M.translation.to_tuple())
            #        e=M.to_euler('XYZ')
            #        T.append((1,0,0,e.x))
            #        T.append((0,1,0,e.y))
            #        T.append((0,0,1,e.z))

    axis = element.find('joint/axis')
    if axis is None:
        axis = element.find('joint/translationdirection')

    children = [root.find('./robotnode[@name="%s"]' % i.get('name')) for i in element.findall('child')]

    if True:

        tree = Tree(element.get('name'))
        if len(M) > 0:
            tree.transformations.append(M)
        print(tree.transformations)
        if element.find('joint') is not None:
            tree.axis_type = element.find('joint').get('type')
            tree.min = float(element.find('joint/limits').get('lo'))
            tree.max = float(element.find('joint/limits').get('hi'))
            if element.find('joint/maxacceleration'):
                tree.acceleration = float(element.find('joint/maxacceleration').get('value'))
            if element.find('joint/maxvelocity'):
                tree.speed = float(element.find('joint/maxvelocity').get('value'))
            if element.find('joint/maxtorque'):
                tree.jerk = float(element.find('joint/maxtorque').get('value'))
            tree.axis = [float(axis.get('x')), float(axis.get('y')), float(axis.get('z'))]

        if None in children:
            print(children, element.get('name'))

        tree.children = [parse(i, root) for i in children]
        return tree

    else:  # Legacy debug
        param = {
            'name': element.get('name')
        }

        if element.find('joint') is not None:
            try:
                param.update({
                    'param': {
                        'type': element.find('joint').get('type'),
                        'lo': element.find('joint/limits').get('lo'),
                        'hi': element.find('joint/limits').get('hi'),
                        'units': element.find('joint/limits').get('units'),
                        'axis': [axis.get('x'), axis.get('y'), axis.get('z')],
                        'transform': M,
                        'acceleration': element.find('joint/maxacceleration').get('value'),
                        'velocity': element.find('joint/maxvelocity').get('value'),
                        'torque': element.find('joint/maxtorque').get('value'),
                    }})
            except:
                print("No param ", param['name'])
                raise

        param.update({'zchildren': [parse(i, root) for i in children]})
        return param


def read(filename, createTree=True):
    doc = etree.parse(filename)
    root = doc.getroot()

    root.get('name')

    root.get('StandardName')

    tolower(root)
    rootNode = root.find('./robotnode[@name="%s"]' % root.get('RootNode'))
    return parse(rootNode, root)

# if __name__ == "__main__":
#    import sys, pprint
#    print(sys.argv[1])
#    structure = read(sys.argv[1],False)
#    pprint.pprint(structure)
#    pass
