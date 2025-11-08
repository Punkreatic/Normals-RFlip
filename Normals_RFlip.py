import bpy
import sys
import os

bl_info = {
    "name": "Fix Normals",
    "author": "Adeline_Off",
    "version": (0, 0, 2),
    "blender": (4, 0, 0),
    "location": "3D View > Sidebar > Normals RFlip",
    "description": "Script to expand the normals of the entire model",
    "warning": "",
    "category": "Mesh",
}

def flip_inverted_normals():
    
    if len(bpy.context.scene.objects) == 0:
        return

    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH' and obj.visible_get():
            
            bpy.context.view_layer.objects.active = obj

            if bpy.context.view_layer.objects.active != obj:
                continue

            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

            bpy.ops.mesh.customdata_custom_splitnormals_clear()

            if obj.mode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')

            bpy.ops.mesh.remove_doubles()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.ops.mesh.normals_tools(mode='RESET')

            bpy.ops.object.mode_set(mode='OBJECT')

            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.shade_smooth()
            bpy.ops.object.select_all(action='DESELECT')

    bpy.context.window_manager.popup_menu(
        lambda self, context: self.layout.label(text="Normals flipped!"),
        title="Information",
        icon='INFO'
    )



class FixNormalsOperator(bpy.types.Operator):
    bl_idname = "mesh.fix_normals"
    bl_label = "Fix Model Normals"
    
    def execute(self, context):
        flip_inverted_normals()
        return {'FINISHED'}


class PANEL_UI_RFLIP(bpy.types.Panel):
    bl_label = "Normals RFlip"
    bl_idname = "OBJECT_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Normals RFlip"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("mesh.fix_normals", text="Fix model normals", icon="MODIFIER")


def register():
    bpy.utils.register_class(FixNormalsOperator)
    bpy.utils.register_class(PANEL_UI_RFLIP)


def unregister():
    bpy.utils.unregister_class(FixNormalsOperator)
    bpy.utils.unregister_class(PANEL_UI_RFLIP)


if __name__ == "__main__":
    register()






# Author: Adeline Offstern
# Created on: 03/11/2025
# Description: Script to expand the normals of the entire model
# Version: 1.0
# Contact///

# End of script
