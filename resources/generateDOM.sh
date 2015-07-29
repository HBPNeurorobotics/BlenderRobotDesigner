#!/bin/bash

cd ../robot_designer_plugin/export/urdf/
generateDS.py -f -o urdf_dom.py ../../../resources/urdf.xsd
2to3 urdf_dom.py -w
sed -i '' 's/\.encode(ExternalEncoding)//g' urdf_dom.py
