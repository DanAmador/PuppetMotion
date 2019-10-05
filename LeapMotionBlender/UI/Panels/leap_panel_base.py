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
        return context.object is not None and bpy.context.mode == "POSE"