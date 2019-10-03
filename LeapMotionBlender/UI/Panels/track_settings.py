import bpy
from bpy.types import Panel
from ..bone_select_PROP import BoneSelectProperty
from ..leap_to_bone_PROP import Leap2BoneProperty
from .leap_panel_base import LeapPanel


class TrackSettings(LeapPanel):
    bl_idname = "OBJECT_PT_track_settings"
    bl_label = "Track Settings"

    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty

        if bone_select.bone_group_enum:
            leap2bone = bpy.context.scene.Leap2BoneProperty        
            col = layout.column()
            pose = context.scene.objects[bone_select.armature_select_enum].pose
            amount = 0 
            for col_prop in leap2bone:
                if col_prop.handedness == "None":
                    continue
                amount +=1
                box = col.box()
                head = box.row()
                head.split(factor=0.1)
                head.prop(col_prop, "expanded", text="")
                icon = "TRIA_RIGHT" if col_prop.handedness == "Right" else "TRIA_LEFT"
                head.label(text=col_prop.name.split(":")[-1], icon=icon)
                if col_prop.expanded:
                    settings = box.box()
                    settings.prop(col_prop, "finger_joint")
                    bools = settings.row()
                    bools.prop(col_prop, "rot_pos", index=0, text="Rotation")
                    bools.prop(col_prop, "rot_pos", index=1, text="Position")
                    settings.prop(col_prop, "scale_factor")
            if amount == 0:
                layout.label(text="No bones have hand settings!")