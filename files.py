import bpy
from mathutils import *
from math import *
from . import collada as c, fix, armatures

from bpy.props import StringProperty
import xml.etree.cElementTree as etree


try:
    from . import simox
    use_simox = True
except ImportError:
    use_simox = False

try:
    from . import mmm
    use_mmm = True
except ImportError:
    use_mmm = False

def parseTree(tree, parentName):
    print("parsetree")
    armName = bpy.context.active_object.name
    armatures.createBone(armName, tree.name, parentName)
    bpy.ops.roboteditor.selectbone(boneName = tree.name)
    print (tree.name)
    boneProp = bpy.context.active_bone.RobotEditor

    m = Matrix()
    print(tree.transformations)
    for i in tree.transformations:
        # We expect a matrix here!
        # Todo accept rotation and translations too!
        if type(i[0]) is list:
            m=m*Matrix(i)
        elif len(i)==3:
            #TODO
            pass
        elif len(i)==4:
            #TODO
            pass
        else:
            raise Exception("ParsingError")
        print(m)

    bpy.context.active_bone.RobotEditor.Euler.x.value = m.translation[0]/1000
    bpy.context.active_bone.RobotEditor.Euler.y.value = m.translation[1]/1000
    bpy.context.active_bone.RobotEditor.Euler.z.value = m.translation[2]/1000

    bpy.context.active_bone.RobotEditor.Euler.gamma.value = degrees(m.to_euler().z)
    bpy.context.active_bone.RobotEditor.Euler.beta.value = degrees(m.to_euler().y)
    bpy.context.active_bone.RobotEditor.Euler.alpha.value = degrees(m.to_euler().x)

    if(tree.axis_type == 'revolute'):
        bpy.context.active_bone.RobotEditor.jointMode = 'REVOLUTE'
        #boneProp.theta.value = float(tree.initalValue)
        bpy.context.active_bone.RobotEditor.theta.max = float(tree.max)
        bpy.context.active_bone.RobotEditor.theta.min = float(tree.min)
    else:
        bpy.context.active_bone.RobotEditor.jointMode = 'PRISMATIC'
        #boneProp.d.value = float(tree.initialValue)
        bpy.context.active_bone.RobotEditor.d.max = float(tree.max)
        bpy.context.active_bone.RobotEditor.d.min = float(tree.min)

    if tree.axis is not None:
        for i,axis in enumerate(tree.axis):
            if axis == -1.0:
                bpy.context.active_bone.RobotEditor.axis_revert = True
                tree.axis[i]=1.0

        if tree.axis==[1.0,0.0,0.0]:
            bpy.context.active_bone.RobotEditor.axis = 'X'
        elif tree.axis==[0.0,1.0,0.0]:
            bpy.context.active_bone.RobotEditor.axis = 'Y'
        elif tree.axis==[0.0,0.0,1.0]:
            bpy.context.active_bone.RobotEditor.axis = 'Z'
    print("parsetree done")
    for child in tree.children:
        parseTree(child, tree.name)



def extractData(boneName):
    tree = c.Tree()
    arm = bpy.context.active_object

    bpy.ops.roboteditor.selectbone(boneName = boneName)
    currentBone = bpy.context.active_bone

    tree.name = boneName

    if currentBone.parent:
        parentName = currentBone.parent.name
    else:
        parentName = None

    if currentBone.RobotEditor.axis_revert:
        inverted = -1
    else:
        inverted = 1

    axis = ["0", "0", "0"]
    if currentBone.RobotEditor.axis == 'X':
        axis[0] = str(inverted)
    elif currentBone.RobotEditor.axis == 'Y':
        axis[1] = str(inverted)
    elif currentBone.RobotEditor.axis == 'Z':
        axis[2] = str(inverted)

    tree.axis = axis

    trafo, dummy = currentBone.RobotEditor.getTransform()
    # translation
    tree.addTrafo([str(e) for e in trafo.translation])
    # rotation
    rotation = trafo.to_euler()
    tree.addTrafo([str(e) for e in [0,0,1, rotation.z]])
    tree.addTrafo([str(e) for e in [0,1,0, rotation.y]])
    tree.addTrafo([str(e) for e in [1,0,0, rotation.x]])

    if(currentBone.RobotEditor.jointMode == 'REVOLUTE'):
        tree.initialValue = str(currentBone.RobotEditor.theta.offset)
        tree.min = str(currentBone.RobotEditor.theta.min)
        tree.max = str(currentBone.RobotEditor.theta.max)
        tree.axis_type = 'revolute'
    else:
        tree.initialValue = str(currentBone.RobotEditor.d.offset)
        tree.min = str(currentBone.RobotEditor.d.min)
        tree.max = str(currentBone.RobotEditor.d.max)
        tree.axis_type = 'prismatic'
    children = [child.name for child in currentBone.children]

    tree.meshes = [mesh.name for mesh in bpy.data.objects if mesh.type == 'MESH' and mesh.parent_bone == boneName]

    markers = [m for m in bpy.data.objects if m.RobotEditor.tag == 'MARKER' and m.parent_bone == boneName]
    #tree.markers = [(m.name,(currentBone.matrix_local.inverted()*m.matrix_world.translation).to_tuple()) for m in markers]
    #tree.markers = [(m.name,(m.matrix_parent_inverse*m.matrix_world.translation).to_tuple()) for m in markers]

    poseBone = arm.pose.bones[boneName]
    tree.markers = [(m.name, (poseBone.matrix.inverted()*arm.matrix_world.inverted()*m.matrix_world.translation).to_tuple() ) for m in markers]

    for child in children:
        tree.addChild(extractData(child))

    return tree

# operator to export an armature to COLLADA 1.5
class RobotEditor_exportCollada(bpy.types.Operator):
    bl_idname = "roboteditor.colladaexport"
    bl_label = "Export to COLLADA 1.5"

    filepath = StringProperty(subtype = 'FILE_PATH')

    def execute(self, context):
        bpy.ops.wm.collada_export(filepath=self.filepath, \
                check_existing=False, filter_blender=False,\
                filter_image=False, filter_movie=False, \
                filter_python=False, filter_font=False, \
                filter_sound=False, filter_text=False,\
                filter_btx=False, filter_collada=True, \
                filter_folder=True)

        fix.fixCollada(self.filepath, self.filepath)
        handler = c.COLLADA()
        handler.import14(self.filepath)

        arm = context.active_object
        baseBoneName = arm.data.bones[0].name

        tree = c.Tree()
        tree.name = arm.name
        tree.addChild(extractData(baseBoneName))


        handler.attach(tree)

        massFrames = [obj for obj in bpy.data.objects if obj.RobotEditor.tag == 'PHYSICS_FRAME' and not obj.parent_bone is '']
        for frame in massFrames:
            #transform = frame.parent.data.bones[frame.parent_bone].matrix_local.inverted() * frame.matrix_local
            boneName = frame.parent.data.bones[frame.parent_bone].name
            poseBone = arm.pose.bones[boneName]
            transform = poseBone.matrix.inverted()*arm.matrix_world.inverted()*frame.matrix_world
            frameTrafos = []
            frameTrafos.append(tuple(v for v in transform.translation))
            frameRotation = transform.to_euler()
            frameTrafos.append(tuple([0,0,1,frameRotation.z]))
            frameTrafos.append(tuple([0,1,0,frameRotation.y]))
            frameTrafos.append(tuple([1,0,0,frameRotation.x]))

            collisionModels = []
            collisionModelTransformations = {}
            for model in [i for i in bpy.data.objects if i.parent == frame]:
                modelName = model.data.name.replace('.','_')+'-mesh'
                collisionModels.append(modelName)
                #matrix = model.parent.data.bones[model.parent_bone].matrix_local.inverted() * model.matrix_local
                matrix =  model.matrix_local
                collisionModelTransformations[modelName]=[tuple(v for v in matrix.translation)]
                rotation = matrix.to_euler()
                collisionModelTransformations[modelName].append(tuple([0,0,1,rotation.z]))
                collisionModelTransformations[modelName].append(tuple([0,1,0,rotation.y]))
                collisionModelTransformations[modelName].append(tuple([1,0,0,rotation.x]))



            #TODO also bring the matrix_local to all collisionmodels
            print ("mass frames", frame.name, collisionModels)
            handler.addMassObject(frame.name, frameTrafos, tuple(v for v in frame.RobotEditor.dynamics.inertiaTensor), frame.RobotEditor.dynamics.mass, collisionModels,collisionModelTransformations)

        handler.write(self.filepath)
        return{'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


# operator to import an MMM-Motion
class RobotEditor_importMMM(bpy.types.Operator):
    bl_idname = "roboteditor.mmmimport"
    bl_label = "Import MMM"
    filepath = StringProperty(subtype = 'FILE_PATH')

    def execute(self, context):

        mmm.read(self.filepath)
        return{'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def draw(layout, context):
    layout.operator("roboteditor.colladaexport")
    layout.operator("roboteditor.mmmimport")


# operator to import the kinematics in a SIMOX-XML file
class RobotEditor_importSIMOX(bpy.types.Operator):
    bl_idname = "roboteditor.simoximport"
    bl_label = "Import SIMOX XML"
    filepath = StringProperty(subtype = 'FILE_PATH')

    def execute(self, context):
        tree=simox.read(self.filepath)
        parseTree(tree,None)
        return{'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def draw(layout, context):
    layout.operator("roboteditor.colladaexport")
    if use_simox:
        layout.operator("roboteditor.simoximport")
    if use_mmm:
        layout.operator("roboteditor.mmmimport")






def register():
    bpy.utils.register_class(RobotEditor_exportCollada)
    if use_simox:
        bpy.utils.register_class(RobotEditor_importSIMOX)
    if use_mmm:
        bpy.utils.register_class(RobotEditor_importMMM)


def unregister():
    bpy.utils.unregister_class(RobotEditor_exportCollada)
    if use_simox:
        bpy.utils.unregister_class(RobotEditor_importSIMOX)
    if use_mmm:
        bpy.utils.unregister_class(RobotEditor_importMMM)



