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

# <pep8-80 compliant>

bl_info = {
    "name": "LOTUS Exporter",
    "author": "Jonas Elbers (www.gcmods.de)",
    "version": (1, 0, 0),
    "blender": (2, 81, 6),
    "location": "File > Import-Export",
    "description": "Export LOTUS X3D",
    "warning": "",
    "doc_url": "https://github.com/gcWorld/Blender-LOTUS-Export/",
    "category": "Import-Export",
}

import bpy
import os

class ExportLotus(bpy.types.Operator):
    """Export Lotus X3D Files"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "lotus.export_x3d_gcw"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Export Lotus X3D Files"         # Display name in the interface.
    #bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        #for window in bpy.context.window_manager.windows:
        #    screen = window.screen

        #    for area in screen.areas:
        #        if area.type == 'VIEW_3D':
        #            override = {'window': window, 'screen': screen, 'area': area}
        #            bpy.ops.view3d.copybuffer(override)
        #            break
        bpy.ops.wm.collada_export(filepath=os.path.join(os.path.dirname(bpy.context.blend_data.filepath),bpy.path.display_name_from_filepath(bpy.context.blend_data.filepath))+".dae", selected=True, apply_modifiers=True, use_object_instantiation=False, use_blender_profile=True, use_texture_copies=False)

        directory = bpy.utils.script_paths("addons")
        
        for d in directory:
            print("checking: "+os.path.join(d,__name__,"import_dae_export_x3d.py"))
            if(os.path.exists(os.path.join(d,__name__,"import_dae_export_x3d.py"))):
                print("Found script")
                print("Blender 2.79 Path: "+addon_prefs.blender27)
                print("Calling: "+'"'+addon_prefs.blender27+'" --python "'+os.path.join(d,__name__,"import_dae_export_x3d.py")+'" -- -path '+bpy.context.blend_data.filepath+' -file '+bpy.path.display_name_from_filepath(bpy.context.blend_data.filepath))
                import subprocess
                subprocess.call([addon_prefs.blender27, '--python', os.path.join(d,__name__,"import_dae_export_x3d.py"), "--", "-path",bpy.context.blend_data.filepath, "-file",bpy.path.display_name_from_filepath(bpy.context.blend_data.filepath)])                #os.system('""'+addon_prefs.blender27+'"" --python "'+os.path.join(d,"io_scene_lotus","import_dae_export_x3d.py")+'" -- -path '+bpy.context.blend_data.filepath+' -file '+bpy.path.display_name_from_filepath(bpy.context.blend_data.filepath))
                return {'FINISHED'}            # Lets Blender know the operator finished successfully.
        return {'ERROR'}

class ExportLotusPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    blender27: bpy.props.StringProperty(
        name="Blender 2.79 .exe File",
        subtype='FILE_PATH',
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text='Path to Blender 2.79')
        row = layout.row()
        row.prop(self, 'blender27', expand=True)

def menu_func_export(self, context):
    self.layout.operator(ExportLotus.bl_idname,
                         text="X3D Extensible 3D for LOTUS (.x3d)")

def register():
    print("Hello World")
    bpy.utils.register_class(ExportLotus)
    bpy.utils.register_class(ExportLotusPreferences)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
def unregister():
    print("Goodbye World")
    bpy.utils.unregister_class(ExportLotus)
    bpy.utils.unregister_class(ExportLotusPreferences)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

    if __name__ == "__main__":
        register()
