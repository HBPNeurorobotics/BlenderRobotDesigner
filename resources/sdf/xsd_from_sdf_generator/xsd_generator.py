# #####
# This file is part of the RobotDesigner of the Neurorobotics subproject (SP10)
# in the Human Brain Project (HBP).
# It has been forked from the RobotEditor (https://gitlab.com/h2t/roboteditor)
# developed at the Karlsruhe Institute of Technology in the
# High Performance Humanoid Technologies Laboratory (H2T).
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


import os
import subprocess
import sys


# check if this is Python 3.x
if sys.version_info < (3, 0):
    sys.stdout.write("ERROR -- This is Python " + str(sys.version_info.major) + "." + str(sys.version_info.minor) + " - Restart Script with Python 3.X\n")
    sys.exit(1)
    
    
# INPUT/OUTPUT folder
input_folder = "../sdf16"
output_folder = "sdf16_xsd"

# current working directory
currentDirectory = os.getcwd()
input_path = os.path.join(currentDirectory, input_folder)
output_path = os.path.join(currentDirectory, output_folder)

print("\n Input path:", input_path)
print("\n Output path:", output_path)

# walk through the directory and process all .xsd files
for entry in os.scandir(input_path):
        if entry.name.endswith('.sdf') and entry.is_file():
        		subprocess.run(["ruby", "xmlschema.rb", "-i", os.path.join(input_path, entry.name), "-s", input_path, "-o", output_path],checkout_output=True)
        		print("Converted ", entry.name)
