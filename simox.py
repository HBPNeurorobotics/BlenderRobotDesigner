import xml.etree.cElementTree as etree

from mathutils import *
from math import *
from pprint import pprint

class Tree(object):
    def __init__(self,name='armature'):
        self.children = []
        self.name = name
        self.transformations= []
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
        self.axis= None
        self.isGripper = None
        self.closingDirection = 1.0

def tolower(element):
    element.tag = element.tag.lower()
    for i in element.getchildren():
        tolower(i)

def parse(element,root,createTree):

    matrix=element.find('transform/matrix4x4')
    T=[]
    if matrix is not None:
        M=[]
        print( element.get('name'))

        for i in range(1,5):
            row = []
            for j in range(1,5):
                row.append(float(matrix.find('row%d'%i).get('c%d'%j)))
            M.append(row)
        M=Matrix(M)
        T.append(M.translation.to_tuple())
        e=M.to_euler('XYZ')
        T.append((1,0,0,e.x))
        T.append((0,1,0,e.y))
        T.append((0,0,1,e.z))

    axis = element.find('joint/axis')
    if axis is None:
        axis = element.find('joint/translationdirection')

    children = [root.find('./robotnode[@name="%s"]' % i.get('name'))  for i in element.findall('child')]

    if createTree:
        tree = Tree(element.get('name'))
        tree.transformations += T
        print (tree.transformations)
        if element.find('joint') is not None:
            tree.axis_type = element.find('joint').get('type')
            tree.min = float(element.find('joint/limits').get('lo'))
            tree.max = float(element.find('joint/limits').get('hi'))
            tree.acceleration = float(element.find('joint/maxacceleration').get('value'))
            tree.speed = float(element.find('joint/maxvelocity').get('value'))
            tree.jerk = float(element.find('joint/maxtorque').get('value'))
            tree.axis = [float(axis.get('x')),float(axis.get('y')),float(axis.get('z'))]

        if None in children:
            print(children, element.get('name'))

        tree.children = [parse(i,root,createTree) for i in children]
        return tree

    else:
        param={
            'name': element.get('name')
        }

        if element.find('joint') is not None:
            try:
                param.update( {
                'param': {
                'type': element.find('joint').get('type'),
                'lo':  element.find('joint/limits').get('lo'),
                'hi':     element.find('joint/limits').get('hi'),
                'units':     element.find('joint/limits').get('units'),
                'axis': [axis.get('x'),axis.get('y'),axis.get('z')],
                'transform': M,
                'acceleration': element.find('joint/maxacceleration').get('value'),
                'velocity': element.find('joint/maxvelocity').get('value'),
                'torque': element.find('joint/maxtorque').get('value'),
                }})
            except:
                print("No param ",param['name'])
                raise

        param.update({'zchildren': [parse(i,root,createTree) for i in children]})
        return param

def read(filename,createTree=True):
    doc=etree.parse(filename)
    root=doc.getroot()

    root.get('name')

    root.get('StandardName')

    tolower(root)
    rootNode = root.find('./robotnode[@name="%s"]' % root.get('RootNode'))
    return parse(rootNode,root,createTree)


#if __name__ == "__main__":
#    import sys, pprint
#    print(sys.argv[1])
#    structure = read(sys.argv[1],False)
#    pprint.pprint(structure)
#    pass
