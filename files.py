import bpy
from . import collada as c, fix
from bpy.props import StringProperty



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
    
    trafo = currentBone.RobotEditor.getTransform()
    # translation
    tree.addTrafo([str(e) for e in trafo.translation])   
    # rotation
    rotation = trafo.to_euler()
    tree.addTrafo([str(e) for e in [0,0,1, rotation.z]])
    tree.addTrafo([str(e) for e in [0,1,0, rotation.y]])
    tree.addTrafo([str(e) for e in [1,0,0, rotation.x]])
    
    if(currentBone.RobotEditor.jointMode == 'REVOLUTE'):
        tree.initialValue = str(currentBone.RobotEditor.theta.value)
        tree.min = str(currentBone.RobotEditor.theta.min)
        tree.max = str(currentBone.RobotEditor.theta.max)
        tree.axis_type = 'revolute'
    else:
        tree.initialValue = str(currentBone.RobotEditor.d.value)
        tree.min = str(currentBone.RobotEditor.d.min)
        tree.max = str(currentBone.RobotEditor.d.max)
        tree.axis_type = 'prismatic'
        
    children = [child.name for child in currentBone.children]
    
    tree.meshes = [mesh.name for mesh in bpy.data.objects if mesh.type == 'MESH' and mesh.parent_bone == boneName]
    
    markers = [m for m in bpy.data.objects if m.RobotEditor.tag == 'MARKER' and m.parent_bone == boneName]
    tree.markers = [(m.name,(currentBone.matrix_local.inverted()*m.matrix_world.translation).to_tuple()) for m in markers]
    
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
        
        
        
        
        massFrames = [obj for obj in bpy.data.objects if obj.RobotEditor.tag == 'PHYSICS_FRAME' and not obj.parent_bone is '']
        for frame in massFrames:
            frameTrafos = []
            frameTrafos.append(tuple(v for v in frame.matrix_local.translation))
            frameRotation = frame.matrix_local.to_euler()
            frameTrafos.append(tuple([0,0,1,frameRotation.z]))
            frameTrafos.append(tuple([0,1,0,frameRotation.y]))
            frameTrafos.append(tuple([1,0,0,frameRotation.x]))
            
            handler.addMassObject(frame.name, frameTrafos, tuple(v for v in frame.RobotEditor.dynamics.inertiaTensor), frame.RobotEditor.dynamics.mass)
        
        handler.attach(tree)
        
        handler.write(self.filepath)
        return{'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
        
        
        
def draw(layout, context):
    layout.operator("roboteditor.colladaexport")
    

    
    


def register():
    bpy.utils.register_class(RobotEditor_exportCollada)
    

def unregister():
    bpy.utils.unregister_class(RobotEditor_exportCollada)
    
    
   