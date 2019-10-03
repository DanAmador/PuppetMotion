import bpy
from bpy.types import Panel
from ..bone_select_PROP import BoneSelectProperty
from ..leap_to_bone_PROP import Leap2BoneProperty
from .leap_panel_base import LeapPanel


class HandSelect(LeapPanel):
    bl_idname = "OBJECT_PT_hand_select"
    bl_label = "Hand Select"

    _classes = (BoneSelectProperty, Leap2BoneProperty)

    def custom_draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty

        if bone_select.bone_group_enum:
            leap2bone = bpy.context.scene.Leap2BoneProperty        
            col = layout.column()
            pose = context.scene.objects[bone_select.armature_select_enum].pose
            for col_prop in bpy.context.scene.Leap2BoneProperty:
                row = col.row()
                
                row.label(text=col_prop.name.split(":")[-1])
                row.prop(col_prop, "handedness")
    