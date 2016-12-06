import urllib
import os.path
from xml.dom import minidom

# this script will download the xsd files from sdf format website, and replace the url path of xsd by the relative local path
# this script is not a part of Blender Robot Designer
def urlxsdretrieve(xsd_local_savepath, xsd_web_savepath, main_xsd):

    pxsd_name = main_xsd.split('/')[-1]
    pxsd_path = os.path.join(xsd_web_savepath,pxsd_name)
    urllib.urlretrieve(main_xsd, pxsd_path)

    xsdreplaceurl2local(xsd_local_savepath, xsd_web_savepath, main_xsd)

    xmldoc = minidom.parse(pxsd_path)
    itemlist = xmldoc.getElementsByTagName('xsd:include')
    for s in itemlist:
        xsd_name = s.attributes['schemaLocation'].value.split('/')[-1]
        if not os.path.isfile(os.path.join(xsd_web_savepath,xsd_name)):
            urlxsdretrieve(xsd_local_savepath, xsd_web_savepath, s.attributes['schemaLocation'].value)


def xsdreplaceurl2local(xsd_local_savepath, xsd_web_savepath, main_xsd):
    pxsd_name = main_xsd.split('/')[-1]
    pxsd_path = os.path.join(xsd_web_savepath, pxsd_name)
    lxsd_path = os.path.join(xsd_local_savepath, pxsd_name)

    xmldoc = minidom.parse(pxsd_path)
    itemlist = xmldoc.getElementsByTagName('xsd:include')
    for s in itemlist:
        xsd_name = s.attributes['schemaLocation'].value.split('/')[-1]
        s.attributes['schemaLocation'].value = os.path.join('../../../robot_designer_plugin/resources/xsd_sdf', xsd_name)
    file_handle = open(lxsd_path, "wb")
    xmldoc.writexml(file_handle)
    file_handle.close()


if __name__ == "__main__":
    xsd_web_path = '../../../resources/xsd_sdf_web'
    xsd_local_path = '../../../resources/xsd_sdf'
    xsd_url = "http://sdformat.org/schemas/model.xsd"
    urlxsdretrieve(xsd_local_path, xsd_web_path,  xsd_url)
    #only for test
    #path = '../../main.xsd'
    #xmldoc = minidom.parse(path)
