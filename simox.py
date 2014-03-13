import xml.etree.cElementTree as etree
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
        self.min = None
        self.max = None
        self.active = 'True'
        self.locked = 'False'
        self.initialValue = 0.0
        self.axis_type = None
        self.axis= None
        self.isGripper = None
        self.closingDirection = 1.0


def parse(element,root):

    matrix=element.find('Transform/matrix4x4')

    M=[]
    if matrix is not None:
        print( element.get('name'))

        for i in range(1,5):
            row = []
            for j in range(1,5):
                row.append(float(matrix.find('row%d'%i).get('c%d'%j)))
            M.append(row)
    axis = element.find('Joint/axis')
#    param={
#        'name': element.get('name'),
#        'param': {
#        'type': element.find('Joint').get('type'),
#        'lo':  element.find('Joint/Limits').get('lo'),
#        'hi':     element.find('Joint/Limits').get('hi'),
#        'units':     element.find('Joint/Limits').get('units'),
#        'axis': [axis.get('x'),axis.get('y'),axis.get('z')],
#        'transform': M
#    }
#    }
    tree = Tree(element.get('name'))
    tree.transformations.append(M)
    tree.axis_type = element.find('Joint').get('type')
    tree.min = float(element.find('Joint/Limits').get('lo'))
    tree.max = float(element.find('Joint/Limits').get('hi'))
    tree.axis = [float(axis.get('x')),float(axis.get('y')),float(axis.get('z'))]

    children = [root.find('./RobotNode[@name="%s"]' % i.get('name'))  for i in element.findall('Child')]
    if None in children:
        print(children, element.get('name'))

    tree.children = [parse(i,root) for i in children]
    return tree

#    param.update({'zchildren': [parse(i,root) for i in children]})
#    return param

def read(filename):
    doc=etree.parse('filename')
    root=doc.getroot()

    root.get('name')

    root.get('StandardName')

    rootNode = root.find('./RobotNode[@name="%s"]' % root.get('RootNode'))

    return parse(rootNode,root)
