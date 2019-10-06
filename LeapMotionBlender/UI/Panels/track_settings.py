import bpy
from ...Properties import Leap2BoneProperty, BoneSelectProperty
from .leap_panel_base import LeapPanel


class TrackSettings(LeapPanel):
    bl_idname = "OBJECT_PT_track_settings"
    bl_label = "Track Settings"

    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty
        axes = ("X", "Y", "Z")

        col = layout.column()
        amount = 0 
        
        bone_select = context.scene.BoneSelectProperty
        bones = Leap2BoneProperty.get_bones_in_selected_group()
        
        for pose_bone in bones:
            pb_leap_prop = pose_bone.LeapProperties
            if pb_leap_prop.handedness == "None":
                continue
            amount +=1
            box = col.box()
            head = box.row()
            head.split(factor=0.1)
            head.prop(pb_leap_prop, "expanded", text="")
            head.label(text=pose_bone.name)
            head.prop(pb_leap_prop, "handedness", text="")
            if pb_leap_prop.expanded:
                settings = box.box()
                settings.prop(pb_leap_prop, "finger_select")
                settings.prop(pb_leap_prop, "finger_joint")
                bools = settings.row()

                bools.prop(pb_leap_prop, "rot_pos", index=0, text="Rotation")
                bools.prop(pb_leap_prop, "rot_pos", index=1, text="Position")
                
                if pb_leap_prop.rot_pos[0]:
                    rot_box = settings.box()
                    row_box = rot_box.row()
                    for idx, value in enumerate(axes):
                        row_box.prop(pb_leap_prop, "rot_select", index=idx, text=value)
                    
                if pb_leap_prop.rot_pos[1]:
                    scale_box = settings.box()
                    scale_box.prop(pb_leap_prop, "scale_factor")


        if amount == 0:
            layout.label(text="No bones have hand settings!")
                