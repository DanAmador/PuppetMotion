import bpy
from bpy.props import (StringProperty, EnumProperty,
                        IntProperty, BoolVectorProperty, 
                        FloatVectorProperty)
from bpy.props import CollectionProperty
from bpy.types import PropertyGroup, Scene
from ..general_helpers import RegisterMixin

class Leap2BoneProperty(RegisterMixin, PropertyGroup):
    total = -1    
    
    @staticmethod
    def add_property(cls):
        global total
        total +=1
        return total


    @classmethod
    def remove_property(cls):
        global total
        total -=1
        return total

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
        name="Falange",
        description="Choose the falange (joint) to track. From the palm outward",
        soft_max=2,
        soft_min=0
    )

    rot_pos : BoolVectorProperty(
        name= "Rotation/Position",
        description= "Choose which properties to track",
        size=2

    )
    scale_factor : FloatVectorProperty(
        name="Scale factor",
        description="Scale movement vector by thexe scalars",
        min=0.01,
        max=10,
        subtype="XYZ",
        size=3
    )


    @classmethod
    def _register_extra(cls):
        bpy.types.Scene.Leap2BoneProperty = CollectionProperty(type=cls)
