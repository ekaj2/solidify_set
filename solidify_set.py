# Copyright 2016 Jake Dube
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import Operator
from bpy.props import FloatProperty

bl_info = {
    "name": "Solidify Set",
    "author": "Jake Dube",
    "version": (1, 0),
    "blender": (2, 77, 0),
    "location": "Spacebar > Solidify Raise/Lower",
    "category": "Object",
}

class RaiseSolidify(Operator):
    """Raises solidify modifier."""
    bl_idname = "object.solidify_raise"
    bl_label = "Solidify Raise"
    bl_options = {"REGISTER", "UNDO"}

    amount = FloatProperty(name="Amount", default=0.01)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'amount')
        
    def execute(self, context):
        scene = bpy.context.scene
        for obj in bpy.context.selected_objects:
            scene.objects.active = obj
            modifiers = obj.modifiers
            found = False
            for mod in modifiers:
                if mod.type == 'SOLIDIFY':
                    mod.thickness += self.amount
                    found = True
                    break
            if not found:
                bpy.ops.object.modifier_add(type='SOLIDIFY')
                for mod in modifiers:
                    if mod.type == 'SOLIDIFY':
                        mod.thickness += self.amount
        return {'FINISHED'}
    

class LowerSolidify(Operator):
    """Lowers solidify modifier."""
    bl_idname = "object.solidify_lower"
    bl_label = "Solidify Lower"
    bl_options = {"REGISTER", "UNDO"}

    amount = FloatProperty(name="Amount", default=0.01)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'amount')
        
    def execute(self, context):
        scene = bpy.context.scene
        for obj in bpy.context.selected_objects:
            scene.objects.active = obj
            modifiers = obj.modifiers
            found = False
            for mod in modifiers:
                if mod.type == 'SOLIDIFY':
                    mod.thickness -= self.amount
                    found = True
                    break
            if not found:
                bpy.ops.object.modifier_add(type='SOLIDIFY')
                for mod in modifiers:
                    if mod.type == 'SOLIDIFY':
                        mod.thickness -= self.amount
        return {'FINISHED'}
    

def register():
    bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_module(__name__)
    
if __name__ == '__main__':
    register()