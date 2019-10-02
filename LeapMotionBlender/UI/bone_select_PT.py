import bpy
from bpy.types import Panel
from ..general_helpers import RegisterMixin
from .bone_select_PROP import BoneSelectProperty
from .leap_to_bone_PROP import Leap2BoneProperty

class BoneSelectPanel(RegisterMixin, Panel):
    bl_idname = "OBJECT_PT_bone_select"
    bl_label = "Leap"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Leap"

    _classes = (BoneSelectProperty, Leap2BoneProperty)

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty
        layout.prop(bone_select, "armature_select_enum")        
        
        if bone_select.armature_select_enum:
            layout.prop(bone_select, "bone_group_enum")

        if bone_select.bone_group_enum:
            col = layout.column()
            pose = context.scene.objects[bone_select.armature_select_enum].pose
            for col_prop in bpy.context.scene.Leap2BoneProperty:
                row = col.row()
                
                row.label(text=col_prop.name)
                row.prop(col_prop, "handedness")
