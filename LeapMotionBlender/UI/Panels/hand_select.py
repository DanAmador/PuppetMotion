import bpy
from bpy.types import Panel
from .leap_panel_base import LeapPanel
from ...Properties import BoneSelectProperty, Leap2BoneProperty


class HandSelect(LeapPanel):
    bl_idname = "OBJECT_PT_hand_select"
    bl_label = "Hand Select"

    _classes = (BoneSelectProperty, Leap2BoneProperty)

    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty
        
        layout.prop(bone_select, "armature_select_enum")        
        
        if bone_select.armature_select_enum:
            layout.prop(bone_select, "bone_group_enum")

        if bone_select.bone_group_enum:
            leap2bone = bpy.context.scene.Leap2BoneProperty        
            col = layout.column()
            pose = context.scene.objects[bone_select.armature_select_enum].pose
            for col_prop in bpy.context.scene.Leap2BoneProperty:
                row = col.row()
                
                row.label(text=col_prop.name.split(":")[-1])
                row.prop(col_prop, "handedness")
    
