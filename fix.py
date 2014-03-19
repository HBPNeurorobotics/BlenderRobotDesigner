import xml.etree.cElementTree as etree
import bpy

def fixCollada(in_filename,out_filename):
    doc = etree.parse(in_filename)
    root = doc.getroot()

    for obj in [i for i in bpy.data.objects if i.type=='MESH']:
         print(obj.name)
         if obj.parent is not None:
            element = root.find('.//{http://www.collada.org/2005/11/COLLADASchema}node[@name="%s"]'%obj.name)
            if not element == None: # sometimes, element is None
                matrix=etree.Element("{http://www.collada.org/2005/11/COLLADASchema}matrix")
                bone = obj.parent.data.bones[obj.parent_bone]
                #matrix.text = " ".join([str(j) for i in bone.matrix_local.inverted() for j in i])
                matrix.set('sid','Inverted')
                matrix.text = " ".join([str(j) for i in list(obj.matrix_parent_inverse) for j in i])
                element.insert(0,matrix)

    doc.write(out_filename, encoding="UTF-8")
    doc.write("test.xml", encoding="UTF-8")

