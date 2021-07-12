# #####
#  This file is part of the RobotDesigner developed in the Neurorobotics
#  subproject of the Human Brain Project (https://www.humanbrainproject.eu).
#
#  The Human Brain Project is a European Commission funded project
#  in the frame of the Horizon2020 FET Flagship plan.
#  (http://ec.europa.eu/programmes/horizon2020/en/h2020-section/fet-flagships)
#
#  The Robot Designer has initially been forked from the RobotEditor
#  (https://gitlab.com/h2t/roboteditor) developed at the Karlsruhe Institute
#  of Technology in the High Performance Humanoid Technologies Laboratory (H2T).
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

import bpy
from mathutils import Euler, Matrix, Quaternion, Vector

from math import pi
import xml.etree.cElementTree as etree
import itertools
from . import armatures


def tolower(element):
    """Convert all tags in the XML file to lower case."""
    element.tag = element.tag.lower()
    for i in element.getchildren():
        tolower(i)


def read(filepath):
    """Read the MMM File from disc and sets keyframes."""
    start = bpy.context.scene.frame_current
    fps = bpy.context.scene.render.fps
    scale_factor = 0.001
    doc = etree.parse(filepath)
    root = doc.getroot()
    tolower(root)
    names = [e.get("name").replace('_joint', '') for e in root.findall(".//jointorder/joint")]
    missing = []
    for i in names:
        if i not in bpy.context.object.data.bones.keys():
            print("Could not find joint: %s" % i)
            names.remove(i)
            missing.append(i)

    print(missing)

    timestamps = [float(e.text.strip()) for e in
                  root.findall(".//motionframes/motionframe/timestep")]
    root_positions = [[float(i) * scale_factor for i in e.text.strip().split()] for e in
                      root.findall(".//motionframes/motionframe/rootposition")]
    root_rotations = [[float(i) for i in e.text.strip().split()] for e in
                      root.findall(".//motionframes/motionframe/rootrotation")]
    joint_positions = [[float(i) for i in e.text.strip().split()] for e in
                       root.findall(".//motionframes/motionframe/jointposition")]

    print(len(root_positions), len(root_rotations))
    bpy.ops.object.mode_set(mode='OBJECT')

    # lastFrame = start -20
    counter = 3  # frame counter for skipping frames, value of 3 ensures that first frame is used
    frameCounter = start  # count the current frame in blender

    # disable kinematic updates for import
    bpy.context.scene.RobotDesigner.doKinematicUpdate = False

    for [i, [timestamp, root_position, root_rotation, joint_position]] in enumerate(
            itertools.zip_longest(timestamps, root_positions, root_rotations, joint_positions,
                                  fillvalue=[])):
        counter += 1  # increase counter
        if counter != 4:  # process frame only if counter equals 4 => use every 4th frame
            # print('Skipping')   # inform that we're skipping
            continue  # skip frame
        counter = 0  # reset counter

        # bpy.context.scene.frame_current = start + timestamp * fps * 10
        bpy.context.scene.frame_current = frameCounter  # set current frame in blender
        frameCounter += 1  # increase frameCounter for next frame
        # if bpy.context.scene.frame_current - lastFrame < 12: #or bpy.context.scene.frame_current > 100:
        #    print('Skipping')
        #    continue
        # lastFrame = bpy.context.scene.frame_current

        print(
            "Frame number: ", bpy.context.scene.frame_current, " of ", len(root_positions) / 4 - 1)
        armName = bpy.context.active_object.name
        segment_name = bpy.context.active_object.data.bones[0].name
        bpy.context.active_object.location = Vector(root_position)
        bpy.context.active_object.rotation_euler = Euler(root_rotation, "XYZ")

        bpy.ops.anim.keyframe_insert(type="Location")
        bpy.ops.anim.keyframe_insert(type="Rotation")

        # bpy.context.active_object.location = Vector(root_position)
        # bpy.context.active_object.rotation_euler = Euler(root_rotation, "XYZ")
        for [x, value] in enumerate(joint_position):
            if x < len(names):
                bpy.ops.RobotDesigner.select_segment(segment_name=names[x])
                try:
                    bpy.context.active_bone.RobotDesigner.theta.value = value / pi * 180.0
                except KeyError:
                    print("Error updating %s" % s)
                    # print(names[x], value/pi*180, bpy.context.active_bone.RobotDesigner.theta.value)

        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='SELECT')
        armatures.updateKinematics(armName, segment_name)
        bpy.ops.anim.keyframe_insert(type='Rotation')
        bpy.ops.object.mode_set(mode='OBJECT')

        # armatures.updateKinematics(armName,segment_name)

    bpy.context.scene.RobotDesigner.doKinematicUpdate = True

# if __name__ == "__main__":
#    import sys
#    read(sys.argv[0])
