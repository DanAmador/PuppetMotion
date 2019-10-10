import bpy
from bpy.props import (StringProperty, EnumProperty, PointerProperty,
                        IntProperty, BoolVectorProperty, 
                        FloatVectorProperty, BoolProperty)
from bpy.types import PropertyGroup, Scene
from ..general_helpers import RegisterMixin

class Leap2BoneProperty(RegisterMixin, PropertyGroup):
    @staticmethod
    def get_bones_in_selected_group():
        bone_select = bpy.context.scene.BoneSelectProperty
        bones = bpy.context.scene.objects[bone_select.armature_select_enum].pose.bones

        if bone_select.bone_group_enum:
            for bone in bones:
                try:
                    if bone.bone_group.name != bone_select.bone_group_enum:
                        continue
                    yield bone
                except AttributeError:
                    continue

    
    name :  StringProperty(
        name="Internal Name",
        description= " Property id made out of armature:bone_group:bone_name",
        # options='HIDDEN'
    )

    expanded : BoolProperty(
        name= "Expanded",
        description="Should the settings be viewable?",
        default=True
    )

    track_type : EnumProperty(
        name="Type",
        description="Type of tracking to be used, either track an entire hand or single bone",
        items=[
            ("Hand", "Hand", "", "VIEW_PAN",0),
            ("Bone", "Bone", "", "BONE_DATA",1),
        ],
        default = "Bone"
    )
    
    handedness : EnumProperty(
        name="Hand",
        description="Which hand should it map to?",
        items=[
            ("None", "None", "", "VIEW_PAN",0),
            ("Right", "Right","", "TRIA_RIGHT", 1),
            ("Left", "Left","", "TRIA_LEFT", 2),
        ],
        default = "None"
    )

    finger_select : EnumProperty(
        name="Finger",
        description="Which finger should it track?",
        items=[
            ("Thumb", "Thumb","", "VIEW_PAN", 0),
            ("Index", "Index","", "VIEW_PAN", 1),
            ("Middle", "Middle","", "VIEW_PAN", 2),
            ("Ring", "Ring","", "VIEW_PAN", 3),
            ("Pinky", "Pinky","", "VIEW_PAN", 4),
        ],
        default = "Thumb"
    )
    
    finger_joint : IntProperty(
        name="Joint",
        description="Choose the joint to track. From the palm outward",
        soft_max=2,
        soft_min=0,
        default=2
    )

    rot_pos : BoolVectorProperty(
        name= "Rotation/Position",
        description= "Choose which properties to track",
        size=2

    )

    scale_factor : FloatVectorProperty(
        name="Scale factor",
        description="Scale movement vector by these scalars",
        soft_min=-10,
        default=(1,1,1),
        soft_max=10,
        subtype="XYZ",
        size=3
    )

    rot_select  : BoolVectorProperty(
        name="Rotation Axis",
        description="Which axis should be used in the rotation?",
        default=(True,True,True),
        subtype="XYZ",
        size=3
    )

    @classmethod
    def _register_extra(cls):
        bpy.types.PoseBone.LeapProperties = bpy.props.PointerProperty(type=cls)