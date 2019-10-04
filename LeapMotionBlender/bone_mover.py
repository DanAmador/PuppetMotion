import bpy
from .Properties import Leap2BoneProperty
from .communicator import message_queue as mq

def move_bones():
    props = bpy.context.scene.RecordProperties
    bones_in_group = Leap2BoneProperty.get_bones_in_selected_group()


    if props.recording:
        print("Bruh")

    
    return 1/props.framerate

    