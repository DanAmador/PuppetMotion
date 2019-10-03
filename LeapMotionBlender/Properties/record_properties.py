import bpy
from bpy.props import IntProperty,BoolProperty
from bpy.props import CollectionProperty
from bpy.types import PropertyGroup
from ..general_helpers import RegisterMixin


class Leap2BoneProperty(RegisterMixin, PropertyGroup):
    
    recording : BoolProperty(
        name="Start recording?",
        description="Should new keyframes be inserted from the data acquired?",
        default="False"
    )
    
    start_frame = IntProperty(
        name="Start frame",
        description="Frame offset used in the keyframe insertion"
    )