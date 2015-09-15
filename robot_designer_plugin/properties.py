# Blender-specific imports (catch exception for sphinx documentation)
import bpy
from mathutils import Euler, Matrix
from bpy.props import *

from math import radians
from . import armatures, meshes


# property group that contains all controller-related parameters
class RobotEditor_ControllerProperty(bpy.types.PropertyGroup):
    maxVelocity = FloatProperty(name="max. Velocity", precision=4, step=100)
    maxTorque = FloatProperty(name="max. Torque", precision=4, step=100)
    isActive = BoolProperty(name="acitve?")
    acceleration = FloatProperty(name="Acceleration", precision=4, step=100)
    deceleration = FloatProperty(name="Deceleration", precision=4, step=100)


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
    controlEnum = EnumProperty(
        items=[('armatures', 'Robot', 'Modify the Robot'),
               ('bones', 'Segments', 'Modify segements'),
               ('meshes', 'Geometries', 'Assign meshes to segments'),
               # ('markers', 'Markers', 'Assign markers to bones'),
               #('controller', 'Controller', 'Modify controller parameter'),
               ('tools', 'Tools', 'Tools'),
               ('files', 'Files', 'Export Armature')],
        name="RobotEditor Control Panel"
    )
    meshType = EnumProperty(
        items=[('DEFAULT', 'Visual', 'Set visual meshes'), ('COLLISION', 'Collision', 'Set collision meshes')]
    )
    listMeshes = EnumProperty(items=[("all",'List all','Show all meshes in menu'),
                                ("connected", 'List connected', 'Show only connected meshes in menu'),
                                ('disconnected', 'List disconnected', 'Show only disconnected meshes in menu')])

    hideMeshType =  EnumProperty(
        items=[('all', 'Show All connected', 'Show all mesh objects in viewport'),
               ('collision', 'Show collision models', 'Show only connected collision models'),
               ('visual', 'Show visual models', 'Show only connected visual models')], update=meshes.displayMeshes)

    listBones = EnumProperty(items=[("all",'List all','Show all bones in menu'),
                                     ("connected", 'List connected', 'Show only bones with connected meshes in menu'),
                                     ('disconnected', 'List disconnected',
                                      'List only bones without connected meshes in menu')])
    storageMode = EnumProperty(items=[('temporary', 'Non-persistant GIT', 'Stores/retrieves files from GIT temporary' +
                                       ' repository'),
                                      ('git','Persitant GIT','Stores/retrieves files from persistent GIT repository'),
                                      ('local','Local','Stores/retrieves from local hard disk')])
    gitURL = StringProperty(name='GIT URL')
    gitRepository = StringProperty(name='GIT Repository')
    modelFolderName = StringProperty(name='Model folder')

    boneMode = EnumProperty(items=[('kinematics', 'Kinematics', 'Edit kinematic properties'),
                                      ('dynamics','Dynamics','Edit Dynamic properties'),
                                        ('controller','Controller','Edit Controller properties')])
    boneLength = FloatProperty(name="Global bone length", default=1, min=0.001, update=updateGlobals)
    subdivisionLevels = IntProperty(name="Subdivision Levels", default=2)
    shrinkWrapOffset = FloatProperty(name="Shrinkwrap Offset", default=0.001, unit='LENGTH', min=0, max=0.5)
    doKinematicUpdate = BoolProperty(name="Import Update", default=True)
    liveSearchBones = StringProperty(name="Live Search for Bones", default="")
    liveSearchMeshes = StringProperty(name="Live Search for Meshes", default="")
    liveSearchMarkers = StringProperty(name="Live Search for Markers", default="")

    #collapsable bone elements
    collapseBoneEdit = BoolProperty(name="Edit Bones")
    collapseGlobalSettings = BoolProperty(name="Robot Designer global settings")
    collapseController = BoolProperty(name="Collapse controller box")
    collapseControllerLimits = BoolProperty(name="Collapse controller limits box")
    collapseCollision = BoolProperty(name="Collapse collision mesh limits box", default=False)
    collapseDisconnectMesh = BoolProperty(name="Collapse collision mesh limits box", default=True)
    collapseConnectMesh = BoolProperty(name="Collapse collision mesh limits box", default=True)
    collapseCFSelection = BoolProperty(name="Collapse coordinate frame selection box", default=False)
# property group that defines a degree of freedom
class RobotEditor_DoF(bpy.types.PropertyGroup):
    def updateDoF(self, context):
        if context.scene.RobotEditor.doKinematicUpdate:
            armName = context.active_object.name
            boneName = context.active_bone.name

            armatures.updateKinematics(armName, boneName)

    value = FloatProperty(name="Value", update=updateDoF, precision=4, step=100)
    offset = FloatProperty(name="Offset", update=updateDoF, precision=4, step=100)
    min = FloatProperty(name="Min", precision=4, step=100)
    max = FloatProperty(name="Max", precision=4, step=100)


# property group that contains dynamics values
class RobotEditor_Dynamics(bpy.types.PropertyGroup):
    # from mathutils import Vector
    # def updateCoM(self, context):
    #    frame = bpy.data.objects[bpy.context.scene.RobotEditor.physicsFrameName]
    #    position = Vector((frame.RobotEditor.dynamics.CoM[0],frame.RobotEditor.dynamics.CoM[1],
    # frame.RobotEditor.dynamics.CoM[2]))
    #    frame.location = position

    # CoM = FloatVectorProperty(name = "Center of Mass", update=updateCoM, subtype = 'XYZ')
    mass = FloatProperty(name="Mass", precision=4, step=0.1)
    inertiaTensor = FloatVectorProperty(name="Inertia Tensor", precision=10, step=0.1)


# property group that stores general information for individual Blender objects with respect to the RobotEditor
class RobotEditor_Properties(bpy.types.PropertyGroup):
    dynamics = PointerProperty(type=RobotEditor_Dynamics)
    fileName = StringProperty(name="fileName")
    tag = EnumProperty(
        items=[('DEFAULT', 'Default', 'Default'),
               ('MARKER', 'Marker', 'Marker'),
               ('PHYSICS_FRAME', 'Physics Frame', 'Physics Frame'),
               ('ARMATURE', 'Armature', 'Armature'),
               ('COLLISION', 'Collision', 'Collision')]
    )


# property group that defines a joint in Euler mode
class RobotEditor_Euler(bpy.types.PropertyGroup):
    def getTransformFromParent(self):
        rot = Euler((radians(self.alpha.value), radians(self.beta.value), radians(self.gamma.value)), 'XYZ').to_matrix()
        rot.resize_4x4()

        transl = Matrix.Translation((self.x.value, self.y.value, self.z.value))
        #print("here",transl * rot)
        return transl * rot

    x = PointerProperty(type=RobotEditor_DoF)
    y = PointerProperty(type=RobotEditor_DoF)
    z = PointerProperty(type=RobotEditor_DoF)
    alpha = PointerProperty(type=RobotEditor_DoF)
    beta = PointerProperty(type=RobotEditor_DoF)
    gamma = PointerProperty(type=RobotEditor_DoF)


# property group that defines a joint in DH mode
class RobotEditor_DH(bpy.types.PropertyGroup):
    def getTransformFromParent(self):
        alphaMatrix = Euler((radians(self.alpha.value), 0, 0), 'XYZ').to_matrix()
        alphaMatrix.resize_4x4()

        thetaMatrix = Euler((0, 0, radians(self.theta.value)), 'XYZ').to_matrix()
        thetaMatrix.resize_4x4()

        translation = Matrix.Translation((self.a.value, 0, self.d.value, 1))

        return translation * alphaMatrix * thetaMatrix

    theta = PointerProperty(type=RobotEditor_DoF)
    d = PointerProperty(type=RobotEditor_DoF)
    alpha = PointerProperty(type=RobotEditor_DoF)
    a = PointerProperty(type=RobotEditor_DoF)

# property group for joint controllers
class RobotEditor_JointControllerType(bpy.types.PropertyGroup):

    isActive = BoolProperty(name="Active", default=False)

    controllerType = EnumProperty(
        items=[('position', 'Position', 'Position'),
               ('velocity', 'Velocity', 'Velocity')],
        name="Controller mode:"
    )

    # controllerType = EnumProperty(
    #     items=[('PID', 'PID controller', 'PID controller'),
    #            ('P', 'P controller', 'P controller')],
    #     name="Controller type:"
    # )

    P = FloatProperty(name="P", precision=4, step=100)
    I = FloatProperty(name="I", precision=4, step=100)
    D = FloatProperty(name="D", precision=4, step=100)

# bone property, contains all relevant bone information for RobotEditor
class RobotEditor_BoneProperty(bpy.types.PropertyGroup):
    def updateBoneProperty(self, context):
        armName = context.active_object.name
        boneName = context.active_bone.name

        armatures.updateKinematics(armName, boneName)

    def getTransform(self):
        # returned transform matrix is of the form translation*parentMatrix*rotation
        # parent is dependent of parent mode, that is either Euler or DH
        # either translation or rotation is I_4 dependent of the joint type,
        # whereas a revolute joints contributes a rotation only and a
        # prismatic joint contributes a translation only

        translation = Matrix()  # initialize as I_4 matrix
        rotation = Matrix()  # initialize as I_4 matrix
        axis_matrix = Matrix()  # contains axis information which should be applied to parentMatrix

        if self.axis_revert:
            inverted = -1
        else:
            inverted = 1

        if self.parentMode == 'EULER':
            parentMatrix = self.Euler.getTransformFromParent()
        else:  # self.parentMode == 'DH'
            parentMatrix = self.DH.getTransformFromParent()

        if self.jointMode == 'REVOLUTE':
            if self.axis == 'X':
                # rotation = Euler((radians(self.theta.value +
                #  self.theta.offset + 180 * (1-inverted)/2),0,0),'XYZ').to_matrix()
                rotation = Euler((radians(self.theta.value + self.theta.offset), 0, 0), 'XYZ').to_matrix()
                rotation.resize_4x4()
                axis_matrix = Euler((radians(180 * (1 - inverted) / 2), 0, 0), 'XYZ').to_matrix()
                axis_matrix.resize_4x4()
            elif self.axis == 'Y':
                # rotation = Euler((0,radians(self.theta.value +
                #  self.theta.offset + 180 * (1-inverted)/2),0),'XYZ').to_matrix()
                rotation = Euler((0, radians(self.theta.value + self.theta.offset), 0), 'XYZ').to_matrix()
                rotation.resize_4x4()
                axis_matrix = Euler((0, radians(180 * (1 - inverted) / 2), 0), 'XYZ').to_matrix()
                axis_matrix.resize_4x4()
            elif self.axis == 'Z':
                # rotation = Euler((0,0,radians(self.theta.value +
                # self.theta.offset + 180 * (1-inverted)/2)),'XYZ').to_matrix()
                rotation = Euler((0, 0, radians(self.theta.value + self.theta.offset)), 'XYZ').to_matrix()
                rotation.resize_4x4()
                axis_matrix = Euler((0, 0, radians(180 * (1 - inverted) / 2)), 'XYZ').to_matrix()
                axis_matrix.resize_4x4()

        if self.jointMode == 'PRISMATIC':
            if self.axis == 'X':
                translation = Matrix.Translation((inverted * (self.d.value + self.d.offset), 0, 0, 1))
            elif self.axis == 'Y':
                translation = Matrix.Translation((0, inverted * (self.d.value + self.d.offset), 0, 1))
            elif self.axis == 'Z':
                translation = Matrix.Translation((0, 0, inverted * (self.d.value + self.d.offset), 1))

        if self.jointMode == 'FIXED': # todo: check if this is right for fixed joint type
            translation = Matrix.Translation((0, 0, 0, 1))

        return parentMatrix * axis_matrix, translation * rotation
        # return parentMatrix, translation*rotation

    jointMode = EnumProperty(
        items=[('REVOLUTE', 'Revolute', 'revolute joint'),
               ('PRISMATIC', 'Prismatic', 'prismatic joint'),
               ('FIXED', 'Fixed', 'fixed joint')],
        name="Joint Mode", update=updateBoneProperty
    )

    parentMode = EnumProperty(
        items=[('EULER', 'Euler', 'Euler mode'),
               ('DH', 'DH', 'DH mode')],
        name="Parent Mode", update=updateBoneProperty
    )

    axis = EnumProperty(
        items=[('X', 'X', 'X Axis'),
               ('Y', 'Y', 'Y Axis'),
               ('Z', 'Z', 'Z Axis')],
        name="Active Axis", default='Z', update=updateBoneProperty
    )

    d = PointerProperty(type=RobotEditor_DoF)
    theta = PointerProperty(type=RobotEditor_DoF)
    Euler = PointerProperty(type=RobotEditor_Euler)
    DH = PointerProperty(type=RobotEditor_DH)
    axis_revert = BoolProperty(name="Axis reverted?", default=False, update=updateBoneProperty)
    controller = PointerProperty(type=RobotEditor_ControllerProperty)
    jointController = PointerProperty(type=RobotEditor_JointControllerType)

    # TODO: Add flags!


def register():
    bpy.utils.register_class(RobotEditor_ControllerProperty)
    bpy.utils.register_class(RobotEditor_JointControllerType)
    bpy.utils.register_class(RobotEditor_Globals)
    bpy.utils.register_class(RobotEditor_DoF)
    bpy.utils.register_class(RobotEditor_Dynamics)
    bpy.utils.register_class(RobotEditor_Properties)
    bpy.utils.register_class(RobotEditor_Euler)
    bpy.utils.register_class(RobotEditor_DH)
    bpy.utils.register_class(RobotEditor_BoneProperty)


def unregister():
    bpy.utils.unregister_class(RobotEditor_ControllerProperty)
    bpy.utils.unregister_class(RobotEditor_JointControllerType)
    bpy.utils.unregister_class(RobotEditor_Globals)
    bpy.utils.unregister_class(RobotEditor_DoF)
    bpy.utils.unregister_class(RobotEditor_Dynamics)
    bpy.utils.unregister_class(RobotEditor_Properties)
    bpy.utils.unregister_class(RobotEditor_Euler)
    bpy.utils.unregister_class(RobotEditor_DH)
    bpy.utils.unregister_class(RobotEditor_BoneProperty)
