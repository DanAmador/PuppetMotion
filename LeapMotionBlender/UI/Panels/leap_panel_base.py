import bpy
from bpy.types import Panel
from ...general_helpers import RegisterMixin

class LeapPanel(RegisterMixin, Panel):
    bl_idname = "OBJECT_PT_leap_panel"
    bl_label = "Leap Base"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Leap"


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty
        
        layout.prop(bone_select, "armature_select_enum")        
        
        if bone_select.armature_select_enum:
            layout.prop(bone_select, "bone_group_enum")

        try:
            self.custom_draw(context)
        except NotImplementedError:
            pass

    
    def custom_draw(self,context):
        raise NotImplementedError
