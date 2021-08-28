# Blender-2.9-LOTUS-Export
 
## Requirements
- [Blender 2.79(b)](https://www.blender.org/download/releases/2-79/)
- [Blender 2.93.3](https://www.blender.org/download) (Only tested with this version. Might work with others)

## Installation
1. Download a .zip file from the latest release.
2. Open Blender 2.93
3. Click on _Edit_ -> _Preferences_
4. Select _Addons_ on the left and click on _Install..._ in the top right
5. Select the downloaded .zip file
6. Activate the just installed addon (should be under _Community_, called "LOTUS Exporter")
7. Expand the Addon entry and fill in the path to the Blender.exe for version 2.79

## Usage
1. Select all parts of the model you want to export
2. Click on _File_ -> _Export_ -> _X3D Extensible 3D for LOTUS (.x3d)_
3. Depending on the size of the model it might take a moment for the process to finish. You should now have an .x3d file with the same name as your blend file in the same folder
4. For issues and errors check the Blender console and submit an issue ticket

##Limitations
- Your .blend file has to have been saved before starting the export.
- Probably some more ...
