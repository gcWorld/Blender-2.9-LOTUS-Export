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
import bpy

import sys
import argparse
 
if '--' in sys.argv:
    argv = sys.argv[sys.argv.index('--') + 1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', '--sample_1', dest='p', metavar='PATH', required=True)
    parser.add_argument('-file', '--sample_2', dest='f', metavar='FILE', required=True)
    args = parser.parse_known_args(argv)[0]

#bpy.ops.wm.read_factory_settings(use_empty=True)

#for window in bpy.context.window_manager.windows:
#    screen = window.screen#

#    for area in screen.areas:
#        if area.type == 'VIEW_3D':
#            override = {'window': window, 'screen': screen, 'area': area}
#            bpy.ops.view3d.pastebuffer(override)
#            break

bpy.ops.wm.collada_import(filepath=os.path.join(os.path.dirname(args.p),args.f+".dae"))

bpy.ops.export_scene.x3d(filepath=os.path.join(os.path.dirname(args.p),args.f+".x3d"), check_existing=False, axis_forward='Y', axis_up='Z', use_selection=False, use_normals=True)
bpy.ops.wm.quit_blender()