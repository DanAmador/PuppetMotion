import bpy
from bpy.props import EnumProperty
from bpy.types import PropertyGroup
from ..general_helpers import RegisterMixin
from .leap_to_bone_mapper_properties import get_or_create

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
    
    def create_leap2bone_props(self, context):

        bone_group = context.scene.BoneSelectProperty.bone_group_enum
        leap2bone = bpy.context.scene.Leap2BoneProperty        
        
        #TODO DELETE THIS ONLY FOR DEBUG
        leap2bone.clear()
        for pose_bone in pose.bones:
            try:
                if bone_group == pose_bone.bone_group.name:
                    leap2bone = get_or_create(arm, bone_group, pose_bone.name)                    
                    # leap2bone.name = pose_bone.name
            except AttributeError as r:
                continue

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
