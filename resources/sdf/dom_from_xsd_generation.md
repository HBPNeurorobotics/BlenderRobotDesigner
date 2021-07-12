
# To generate a dom file from the xsd root file:

# Install pyxb
pip install pyxbgen==1.2.5
or use from within Blender

## General
pyxbgen -m [dom_name] -u [absolute path to xsd] --binding-root [absolute path to save destination]

## Model dom
cd RobotDesigner/resources/sdf/Model/sdf/sdf16_xsd
pyxbgen -m dombf_test root.xsd  --binding-root output_path

## World dom
cd RobotDesigner/resources/sdf/World/root_xsd
pyxbgen -m dombf_test root.xsd --binding-root output_path


