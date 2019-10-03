import bpy
from bpy.props import EnumProperty
from bpy.types import PropertyGroup
from ..general_helpers import RegisterMixin

class BoneSelectProperty(RegisterMixin, PropertyGroup):
    def get_available_armatures(scene, context):
        armatures = context.scene.objects
        items = []
        for idx, obj in enumerate(armatures):
            if obj.type == "ARMATURE":
                items.append((obj.name, obj.name, '', "BONE_DATA", idx))
        
        return items if len(items) > 0 else  [("Empty", "No items available", '', "ERROR", 0)]
    
    def get_bone_groups_in_armature(scene, context):
        items = []
        arm = bpy.context.scene.BoneSelectProperty.armature_select_enum
        if arm:        
            bgs = bpy.data.objects[arm].pose.bone_groups
            for idx, bg in enumerate(bgs):
                items.append((bg.name, bg.name, '', "BONE_DATA", idx))

        return items
    
    armature_select_enum : EnumProperty(
        name="Armature",
        items= get_available_armatures,
        description="Select Armature"
    )

    bone_group_enum : EnumProperty(
        name="Bone Group",
        items=get_bone_groups_in_armature,
        # update=create_leap2bone_props,
        description="Select Bone Group"
    )
