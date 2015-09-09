#!/usr/bin/python3

import os
import sys
virtualenvAvailable = True
bpyAvailable = True
# bpy module available if run from Blender
try:
    import bpy
except ImportError:
    bpyAvailable = False

# virtualenv not available from blender usually
try:
    import virtualenv
    print('virtualenv module found: '+virtualenv.__file__)
except ImportError:
    virtualenvAvailable = False


def main():
    venvName = 'py3env'
    blenderPythonVersion = str(sys.version_info.major) + '.' + str(sys.version_info.minor)
    if (sys.version_info.major < 3):
        print('You are running an old version of Blender - the built-in python has version < 3.x\nPlease update to a recent version of Blender (>=2.5)')
        return

    pathToModule = sys.argv[0]
    os.chdir(pathToModule)

    # sandboxing in a virtualenv
    if os.path.exists(venvName):
        print('Using existing virtualenv '+venvName)
    elif (virtualenvAvailable):
        print('Creating a virtualenv '+venvName)
        virtualenv.create_environment(venvName)
    else:
        print('Could not import virtualenv and could not find existing one at location '+venvName+'. Aborting')
        return

    pathToPip = os.path.join(venvName, 'bin/pip')
    pathToAddon = 'robot_designer_plugin'
    if (not os.path.exists(pathToPip)):
        print('Pip could not be found within the virtualenv '+os.path.join(os.getcwd(), pathToPip)+'. Aborting')
        return

    # install dependencies in the virtualEnv (we pre-compiled them into wheels)
    os.system(pathToPip+' install --use-wheel --find-links=wheels lxml gitpython gitdb pyxb')
    venvLibPath = os.path.join(venvName, 'lib')

    # get venv python version
    venvPythonVersions = [v[6:] for v in os.listdir(venvLibPath) if v.startswith('python')]
    if (not blenderPythonVersion in venvPythonVersions):
        venvVersionToBind = venvPythonVersions[-1]
        print('There is a mismatch between the virtualenv python version and Blender python version:\n'+
              'virtualenv: '+str(venvPythonVersions)+' Blender: '+blenderPythonVersion+'\n'+
              'This script will try to bind Blender with python version '+venvVersionToBind+'\n'+
              'Please consider creating a virtualenv version that matches your blender version')
    else:
        venvVersionToBind = blenderPythonVersion

    venvPythonBindFolder = 'python'+venvVersionToBind
    # make this virtualenv accessible from our addon
    # TODO: what is the equivalent of 'plat-x86_64-linux-gnu' for other architecture?
    libPath = ['plat-x86_64-linux-gnu', 'site-packages']
    additionalModulePath = list(map(lambda lib: os.path.join(pathToModule, venvLibPath, venvPythonBindFolder, lib), libPath ))

    print('Generating generatedAdditionalModulePath.py file with the follownig python path:')
    print(str(additionalModulePath))
    textToAppend = 'venvPath = '+ str(additionalModulePath) + '\n'
    with open(os.path.join(pathToAddon,'generatedAdditionalModulePath.py'), 'w') as modified: modified.write(textToAppend)

    # make our addon available to blender
    if (bpyAvailable):
        blenderVersion = str(bpy.app.version[0]) + '.' + str(bpy.app.version[1])
    else:
        blenderVersion = '2.72'

    linkPath = os.path.join(os.path.expanduser('~'), '.config/blender/', blenderVersion, 'scripts/addons/robot_designer_plugin')

    try:
        os.makedirs(os.path.dirname(linkPath))
    except OSError as e:
        print('Directory already exists')

    if os.path.lexists(linkPath):
        print('Removing previous symlink to module')
        os.remove(linkPath)


    print('Creating link from local blender addons to our module')
    print('Link name: '+linkPath)
    absPathToAddon = os.path.join(pathToModule, pathToAddon)
    os.symlink(absPathToAddon, linkPath)

if __name__ == '__main__':
    main()
