import bpy

def read(filepath):
        start=context.scene.frame_current=40
        fps=context.scene.render.fps

        doc=etree.parse(filepath)
        root=doc.getroot()
        names=[e.get('name') for e in root.findall('.//joint_order/joint')]
        timestamps=[float(e.text.strip()) for e in root.findall('.//motion/motion-data/timestamp')]
        root_positions=[[float(i) for i in e.text.strip().split()] for e in root.findall('.//motion/motion-data/root_position')]
        root_rotations=[[float(i) for i in e.text.strip().split()] for e in root.findall('.//motion/motion-data/root_rotation')]
        joint_positions=[[float(i) for i in e.text.strip().split()] for e in root.findall('.//motion/motion-data/joint_position')]

        print(len(root_positions), len(root_rotations))
        for [i,[timestamp,root_position,root_rotation,joint_position]] in enumerate(zip(timestamps,root_positions,root_rotations,joint_positions)):
            context.scene.frame_current=start+timestamp*fps
            bpy.ops.anim.keyframe_insert(type='Location')
            bpy.ops.anim.keyframe_insert(type='Rotation')
            context.active_object.location = Vector(root_position)
            context.active_object.rotation_euler = Euler([0.1,0.1,0.5],'XYZ')

            for [x,value] in enumerate(joint_position):
                print(names[x], value)
