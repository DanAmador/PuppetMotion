import bpy
from .leap_panel_base import LeapPanel
from ...Properties import BoneSelectProperty, Leap2BoneProperty


class MainLeapPanel(LeapPanel):
    bl_label = "Leap Main"


    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty
        
        layout.prop(bone_select, "armature_select_enum")        
        
        if bone_select.armature_select_enum:
            layout.prop(bone_select, "bone_group_enum")