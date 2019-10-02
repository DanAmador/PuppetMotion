import bpy
from bpy.props import EnumProperty
from bpy.types import PropertyGroup, Panel
from ..general_helpers import RegisterMixin

class BoneSelectProperty(RegisterMixin, PropertyGroup):
    def get_armature_callbacks(scene, context):
        armatures = context.scene.objects
        items = []
        for idx, obj in enumerate(armatures):
            if obj.type == "ARMATURE":
                items.append((obj.name, obj.name, '', "BONE_DATA", idx))
        
        return items
    
    def bone_item_callback(scene, context):
        items = []
        arm = bpy.context.scene.BoneSelectProperty.armature_select_enum
        if arm:        
            bgs = bpy.data.objects[arm].pose.bone_groups
            for idx, bg in enumerate(bgs):
                items.append((bg.name, bg.name, '', "BONE_DATA", idx))

        return items

    armature_select_enum : EnumProperty(
        name="Armature",
        items= get_armature_callbacks,
        description="Select Armature"
    )

    bone_group_enum : EnumProperty(
        name="Bone Group",
        items=bone_item_callback,
        description="Select Bone Group"
    )
    



class AnimationPanel(RegisterMixin, Panel ):
    bl_idname = "LEAP_PT_panel"
    bl_label = "Leap"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Leap"

    _classes = (BoneSelectProperty,)

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty


        
        layout.prop(bone_select, "armature_select_enum")        
        if bone_select.armature_select_enum:
            layout.prop(bone_select, "bone_group_enum")

        if bone_select.bone_group_enum:
            col = layout.column()
            pose = bpy.data.objects[bone_select.armature_select_enum].pose
            for pose_bone in pose.bones:
                try:
                    if bone_select.bone_group_enum == pose_bone.bone_group.name: 
                        row = col.row()
                        row.label(text=pose_bone.name)
                except AttributeError:
                    continue
        # for armature in obj:
        #     layout.label(text=obj.name)

