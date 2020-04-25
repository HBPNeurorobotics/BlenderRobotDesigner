#!/usr/bin/python
"""
Small tool for validating URDF files against the xml specification (urdf.xsd).
The generated python class urdf_dom (created with generateDS from urdf.xsd)
is used to load and check the specified XML file.
"""

__author__ = 'Lars Pfotzer'

import os
import sys, getopt
from lxml import etree

# main method of the urdf_xml_validator
def main(argv):
    xsd_file_name = 'urdf.xsd'  # default value
    xml_file_name = 'test.urdf' # default value
    try:
        opts, args = getopt.getopt(argv,"hd:l:",["xsdfile=","xmlfile="])
    except getopt.GetoptError:
        print 'urdf_xml_validator.py -d <xsdfile> -l <xmlfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'urdf_xml_validator.py -d <xsdfile> -l <xmlfile>'
            sys.exit()
        elif opt in ("-d", "--xsdfile"):
            xsd_file_name = arg
        elif opt in ("-l", "--xmlfile"):
            xml_file_name = arg

    print 'XSD file is', xsd_file_name
    print 'XML file is', xml_file_name

    # open xsd and read content
    with open(xsd_file_name, "r") as xsd_file:
        xml_schema_str = xsd_file.read()
        #print xml_schema_str
    xsd_file.close()

    # open xml and read content
    with open(xml_file_name, "r") as xml_file:
        xml_str = xml_file.read()
        #print xml_str
    xml_file.close()

    # create xml parser
    parser = etree.XMLParser(dtd_validation=True)

    schema_root = etree.XML(xml_schema_str)
    schema = etree.XMLSchema(schema_root)

    # validate xml file against xsd schema
    parser = etree.XMLParser(schema=schema)
    root = etree.fromstring(xml_str, parser)

    print 'validating successful'

if __name__ == "__main__":
   main(sys.argv[1:])
