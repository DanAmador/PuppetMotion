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
        

        bone_generator = Leap2BoneProperty.get_bones_in_selected_group()
        col = layout.column()
        for pose_bone in bone_generator:
            pb_leap_prop = pose_bone.LeapProperties
            if pose_bone.bone_group.name != bone_select.bone_group_enum:
                continue
            row = col.box()

            row.label(text=pose_bone.name)
            col1 = row.row()
            col1.prop(pb_leap_prop, "handedness", text="")

            if pb_leap_prop.handedness != "None":
                col1.prop(pb_leap_prop, "track_type", text="")
