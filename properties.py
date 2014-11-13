import bpy, mathutils, math
from bpy.props import *
from mathutils import Euler, Matrix
from math import radians
from . import armatures



# property group that contains all controller-related parameters
class RobotEditor_ControllerProperty(bpy.types.PropertyGroup):
    maxVelocity = FloatProperty(name="max. Velocity", precision = 4, step = 100)
    maxTorque = FloatProperty(name="max. Torque", precision = 4, step = 100)
    isActive = BoolProperty(name = "acitve?")
    acceleration = FloatProperty(name = "Acceleration", precision = 4, step = 100)
    deceleration = FloatProperty(name = "Deceleration", precision = 4, step = 100)

# property group that contains all globally defined parameters
class RobotEditor_Globals(bpy.types.PropertyGroup):
    def updateGlobals(self, context):
        armName = context.active_object.name
        boneName = context.active_bone.name

        armatures.updateKinematics(armName, boneName)

    armatureName = StringProperty(name="armatureName")
    boneName = StringProperty(name="boneName")
    meshName = StringProperty(name="meshName")
    markerName = StringProperty(name="markerName")
    physicsFrameName = StringProperty(name="physicsFrameName")
    controlEnum = EnumProperty \
        (
        items = [('bones', 'Bones','Modify selected Bone'),
             ('meshes', 'Meshes', 'Assign meshes to bones'),
             ('markers', 'Markers', 'Assign markers to bones'),
             ('physics','Physics','Assign Physics Frames to bones'),
             ('controller','Controller','Modify controller parameter'),
             ('files', 'Files', 'Export Armature')],
        name = "RobotEditor Control Panel"
        )
    boneLength = FloatProperty(name="Global bone length", default = 1.0, min=0.001, update = updateGlobals)
    subdivisionLevels = IntProperty(name="Subdivision Levels", default = 2)
    shrinkWrapOffset = FloatProperty(name="Shrinkwrap Offset", default = 0.001)


# property group that defines a degree of freedom
class RobotEditor_DoF(bpy.types.PropertyGroup):

    def updateDoF(self, context):
        print("updateDoF")
        armName = context.active_object.name
        boneName = context.active_bone.name

        armatures.updateKinematics(armName,boneName)
        # print("updateDoF Done")

    value = FloatProperty(name="Value", update = updateDoF, precision = 4,step=100 )
    offset = FloatProperty(name="Offset", update = updateDoF, precision = 4, step=100)
    min = FloatProperty(name="Min", precision = 4, step=100)
    max = FloatProperty(name="Max", precision = 4, step=100)

# property group that contains dynamics values
class RobotEditor_Dynamics(bpy.types.PropertyGroup):
    #from mathutils import Vector
    #def updateCoM(self, context):
    #    frame = bpy.data.objects[bpy.context.scene.RobotEditor.physicsFrameName]
    #    position = Vector((frame.RobotEditor.dynamics.CoM[0],frame.RobotEditor.dynamics.CoM[1],frame.RobotEditor.dynamics.CoM[2]))
    #    frame.location = position

    #CoM = FloatVectorProperty(name = "Center of Mass", update=updateCoM, subtype = 'XYZ')
    mass = FloatProperty(name= "Mass")
    inertiaTensor = FloatVectorProperty(name = "Inertia Tensor")



# property group that stores general information for individual Blender objects with respect to the RobotEditor
class RobotEditor_Properties(bpy.types.PropertyGroup):
    dynamics = PointerProperty(type=RobotEditor_Dynamics)
    tag = EnumProperty \
        (
        items=
        [('DEFAULT','Default','Default'),
        ('MARKER', 'Marker', 'Marker'),
        ('PHYSICS_FRAME','Physics Frame','Physics Frame'),
        ('ARMATURE','Armature','Armature  ')]
        )


# property group that defines a joint in Euler mode
class RobotEditor_Euler(bpy.types.PropertyGroup):
        def getTransformFromParent(self):
            rot = Euler((radians(self.alpha.value), radians(self.beta.value), radians(self.gamma.value)),'XYZ').to_matrix()
            rot.resize_4x4()

            transl = Matrix.Translation((self.x.value,self.y.value,self.z.value))
            return transl*rot

        x = PointerProperty(type=RobotEditor_DoF)
        y = PointerProperty(type=RobotEditor_DoF)
        z = PointerProperty(type=RobotEditor_DoF)
        alpha = PointerProperty(type=RobotEditor_DoF)
        beta = PointerProperty(type=RobotEditor_DoF)
        gamma = PointerProperty(type=RobotEditor_DoF)


# property group that defines a joint in DH mode
class RobotEditor_DH(bpy.types.PropertyGroup):
    def getTransformFromParent(self):
        alphaMatrix = Euler((radians(self.alpha.value),0,0),'XYZ').to_matrix()
        alphaMatrix.resize_4x4()

        thetaMatrix = Euler((0,0,radians(self.theta.value)),'XYZ').to_matrix()
        thetaMatrix.resize_4x4()

        translation = Matrix.Translation((self.a.value,0,self.d.value,1))

        return translation*alphaMatrix*thetaMatrix

    theta = PointerProperty(type=RobotEditor_DoF)
    d = PointerProperty(type=RobotEditor_DoF)
    alpha = PointerProperty(type=RobotEditor_DoF)
    a = PointerProperty(type=RobotEditor_DoF)


# bone property, contains all relevant bone information for RobotEditor
class RobotEditor_BoneProperty(bpy.types.PropertyGroup):
    def updateBoneProperty(self, context):
        armName = context.active_object.name
        boneName = context.active_bone.name

        armatures.updateKinematics(armName, boneName)

    def getTransform(self):
        # returned transform matrix is of the form translation*parentMatrix*rotation
        # parent is dependet of parent mode, that is either Euler or DH
        # either translation or rotation is I_4 dependent of the joint type,
        # whereas a revolute joints contributes a rotation only and a
        # prismatic joint contributes a translation only

        translation = Matrix() # initialize as I_4 matrix
        rotation = Matrix() #initialize as I_4 matrix

        if self.axis_revert:
            inverted = -1
        else:
            inverted = 1

        if (self.parentMode == 'EULER'):
            parentMatrix = self.Euler.getTransformFromParent()
        else: # self.parentMode == 'DH'
            parentMatrix = self.DH.getTransformFromParent()

        if (self.jointMode == 'REVOLUTE'):
            if(self.axis == 'X'):
                rotation = Euler((radians(self.theta.value + self.theta.offset + 180 * (1-inverted)/2),0,0),'XYZ').to_matrix()
                rotation.resize_4x4()
            elif(self.axis == 'Y'):
                rotation = Euler((0,radians(self.theta.value + self.theta.offset + 180 * (1-inverted)/2),0),'XYZ').to_matrix()
                rotation.resize_4x4()
            elif(self.axis == 'Z'):
                rotation = Euler((0,0,radians(self.theta.value + self.theta.offset + 180 * (1-inverted)/2)),'XYZ').to_matrix()
                rotation.resize_4x4()

        else: #self.jointMode == 'PRISMATIC'
            if(self.axis == 'X'):
                translation = Matrix.Translation((inverted*(self.d.value + self.d.offset),0,0,1))
            elif(self.axis == 'Y'):
                translation = Matrix.Translation((0,inverted*(self.d.value + self.d.offset),0,1))
            elif(self.axis == 'Z'):
                translation = Matrix.Translation((0,0,inverted*(self.d.value + self.d.offset),1))

        return parentMatrix, translation*rotation

    jointMode = EnumProperty \
        (
        items = [('REVOLUTE','Revolute', 'revolute joint'),
             ('PRISMATIC', 'Prismatic', 'prismatic joint')],
        name = "Joint Mode", update = updateBoneProperty
        )

    parentMode = EnumProperty \
        (
        items = [('EULER', 'Euler','Euler mode'),
             ('DH', 'DH', 'DH mode')],
        name = "Parent Mode", update = updateBoneProperty
        )

    axis = EnumProperty \
        (
        items = [('X', 'X','X Axis'),
             ('Y', 'Y','Y Axis'),
             ('Z', 'Z','Z Axis')],
        name = "Active Axis", default = 'Z', update = updateBoneProperty
        )

    d = PointerProperty(type=RobotEditor_DoF)
    theta = PointerProperty(type=RobotEditor_DoF)
    Euler = PointerProperty(type=RobotEditor_Euler)
    DH = PointerProperty(type=RobotEditor_DH)
    axis_revert = BoolProperty(name="Axis reverted?", default = False, update = updateBoneProperty)
    controller = PointerProperty(type=RobotEditor_ControllerProperty)
    # TODO: Add flags!

def register():
    bpy.utils.register_class(RobotEditor_ControllerProperty)
    bpy.utils.register_class(RobotEditor_Globals)
    bpy.utils.register_class(RobotEditor_DoF)
    bpy.utils.register_class(RobotEditor_Dynamics)
    bpy.utils.register_class(RobotEditor_Properties)
    bpy.utils.register_class(RobotEditor_Euler)
    bpy.utils.register_class(RobotEditor_DH)
    bpy.utils.register_class(RobotEditor_BoneProperty)



def unregister():
    bpy.utils.unregister_class(RobotEditor_ControllerProperty)
    bpy.utils.unregister_class(RobotEditor_Globals)
    bpy.utils.unregister_class(RobotEditor_DoF)
    bpy.utils.unregister_class(RobotEditor_Dynamics)
    bpy.utils.unregister_class(RobotEditor_Properties)
    bpy.utils.unregister_class(RobotEditor_Euler)
    bpy.utils.unregister_class(RobotEditor_DH)
    bpy.utils.unregister_class(RobotEditor_BoneProperty)



