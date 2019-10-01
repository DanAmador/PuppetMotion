import bpy


class AnimationPanel(bpy.types.Panel):
    bl_idname = "LEAP_PT_panel"
    bl_label = "Leap"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Leap"

    def draw(self, context):
        obj = bpy.data.objects['Armature']
        bone_groups = obj.pose.bone_groups

        layout = self.layout 
        for group in bone_groups:
            layout.label(text=group.name)