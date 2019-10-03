import bpy
from bpy.types import Panel
from ...Properties import Leap2BoneProperty, BoneSelectProperty
from .leap_panel_base import LeapPanel


class TrackSettings(LeapPanel):
    bl_idname = "OBJECT_PT_track_settings"
    bl_label = "Track Settings"

    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty

        if bone_select.bone_group_enum:
            col = layout.column()
            pose = context.scene.objects[bone_select.armature_select_enum].pose
            amount = 0 
            
            bone_select = context.scene.BoneSelectProperty
            arm = bone_select.armature_select_enum
            pose = bpy.context.scene.objects[arm].pose
            for pose_bone in pose.bones:
                try:
                    pb_leap_prop = pose_bone.LeapProperties
                    if pb_leap_prop.handedness == "None" or pose_bone.bone_group.name != bone_select.bone_group_enum :
                        continue
                    amount +=1
                    box = col.box()
                    head = box.row()
                    head.split(factor=0.1)
                    head.prop(pb_leap_prop, "expanded", text="")
                    icon = "TRIA_RIGHT" if pb_leap_prop.handedness == "Right" else "TRIA_LEFT"
                    head.label(text=pose_bone.name, icon=icon)
                    if pb_leap_prop.expanded:
                        settings = box.box()
                        settings.prop(pb_leap_prop, "finger_joint")
                        bools = settings.row()
                        bools.prop(pb_leap_prop, "rot_pos", index=0, text="Rotation")
                        bools.prop(pb_leap_prop, "rot_pos", index=1, text="Position")
                        settings.prop(pb_leap_prop, "scale_factor")
                except AttributeError:
                    continue
            if amount == 0:
                layout.label(text="No bones have hand settings!")
                