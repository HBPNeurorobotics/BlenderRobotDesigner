import bpy
from mathutils import Euler, Vector
from math import pi
import xml.etree.cElementTree as etree
import itertools

def tolower(element):
    """Convert all tags in the XML file to lower case."""
    element.tag = element.tag.lower()
    for i in element.getchildren():
        tolower(i)

def read(filepath):
    """Read the MMM File from disc and sets keyframes."""
    start=bpy.context.scene.frame_current
    fps=bpy.context.scene.render.fps
    scale_factor=0.001
    doc=etree.parse(filepath)
    root=doc.getroot()
    tolower(root)
    names=[e.get("name").replace('_joint','') for e in root.findall(".//jointorder/joint")]
    missing = []
    for i in names:
        if not i in bpy.context.object.data.bones.keys():
            print("Could not find joint: %s" % i)
            names.remove(i)
            missing.append(i)

    print(missing)

    timestamps=[float(e.text.strip()) for e in root.findall(".//motionframes/motionframe/timestep")]
    root_positions=[[float(i)*scale_factor for i in e.text.strip().split()] for e in root.findall(".//motionframes/motionframe/rootposition")]
    root_rotations=[[float(i) for i in e.text.strip().split()] for e in root.findall(".//motionframes/motionframe/rootrotation")]
    joint_positions=[[float(i) for i in e.text.strip().split()] for e in root.findall(".//motionframes/motionframe/jointposition")]

    print(len(root_positions), len(root_rotations))
    bpy.ops.object.mode_set(mode='OBJECT')

    #lastFrame = start -20
    counter = 3                 # frame counter for skipping frames, value of 3 ensures that first frame is used
    frameCounter = start        # count the current frame in blender
    
    for [i,[timestamp,root_position,root_rotation,joint_position]] in enumerate(itertools.zip_longest(timestamps,root_positions,root_rotations,joint_positions,fillvalue=[])):
        counter = counter + 1   # increase counter
        if counter != 4:        # process frame only if counter equals 4 => use every 4th frame
            print('Skipping')   # inform that we're skipping
            continue            # skip frame
        counter = 0             # reset counter

        #bpy.context.scene.frame_current = start + timestamp * fps * 10
        bpy.context.scene.frame_current = frameCounter      # set current frame in blender
        frameCounter = frameCounter + 1                     # increase frameCounter for next frame
        #if bpy.context.scene.frame_current - lastFrame < 12: #or bpy.context.scene.frame_current > 100:
        #    print('Skipping')
        #    continue
        #lastFrame = bpy.context.scene.frame_current

        print(bpy.context.scene.frame_current)
        bpy.context.active_object.location = Vector(root_position)
        bpy.context.active_object.rotation_euler = Euler(root_rotation, "XYZ")

        bpy.ops.anim.keyframe_insert(type="Location")
        bpy.ops.anim.keyframe_insert(type="Rotation")

        bpy.context.active_object.location = Vector(root_position)
        bpy.context.active_object.rotation_euler = Euler(root_rotation, "XYZ")
        for [x,value] in enumerate(joint_position):
            if x < len(names):
                bpy.ops.roboteditor.selectbone(boneName = names[x])
                try:
                    bpy.context.active_bone.RobotEditor.theta.value=value/pi*180.0
                except KeyError:
                    print("Error updating %s" %s)
                print(names[x], value/pi*180, bpy.context.active_bone.RobotEditor.theta.value)

        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='SELECT')
        bpy.ops.anim.keyframe_insert(type='Rotation')
        bpy.ops.object.mode_set(mode='OBJECT')

#if __name__ == "__main__":
#    import sys
#    read(sys.argv[0])
