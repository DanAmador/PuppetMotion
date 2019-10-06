import bpy
from bpy.props import IntProperty,BoolProperty, StringProperty
from bpy.types import PropertyGroup
from ..general_helpers import RegisterMixin
from ..bone_mover import move_bones
from ..communicator import message_queue as mq
from ..communicator import clear_queue
from .leap_bone_properties import Leap2BoneProperty

class RecordProperties(RegisterMixin, PropertyGroup):
    def record_toggle(self, context):
        clear_queue(    )
        props = context.scene.RecordProperties
        new_verb = "Stop" if props.recording else "Start"
        props.icon = "CANCEL" if props.recording else "VIEW_CAMERA"
        props.start_frame = context.scene.frame_current if props.recording else 0
        props.button_text  = f"{new_verb} Recording"
        

    def move_toggle(self, context):
        props = context.scene.RecordProperties
        bpy.ops.pose.user_transforms_clear()
        if not bpy.app.timers.is_registered(move_bones) and props.move_bones:
            bpy.app.timers.register(move_bones, first_interval=1, persistent=False)

        if not props.move_bones and bpy.app.timers.is_registered(move_bones):
            bpy.app.timers.unregister(move_bones)
        

    move_bones : BoolProperty(
        name="Move Bones",
        description="Should the bones be moved with incoming data?",
        default = False, 
        update = move_toggle
    )

    button_text : StringProperty(
        name="Name used in the operator",
        default="Start Recording"
    )

    icon : StringProperty(
        name="Icon used",
        default="VIEW_CAMERA"
    )
    
    recording: BoolProperty(
        name="Record",
        description="Should new keyframes be inserted from the data acquired?",
        default= False,
        update=record_toggle
    )
    
    start_frame : IntProperty(
        name="Start frame",
        description="Frame offset used in the keyframe insertion",
        default= 0
    )

    framerate : IntProperty(
        name="Framerate",
        description="How many frames per second should be sampled while moving the bone?",
        default = 24,
        soft_max = 60,
        soft_min = 12
    )

    record_rate : IntProperty(
        name="Record rate",
        description="How many movement samples must be taken before inserting a keyframe?",
        default = 12,
        soft_max = 60,
        soft_min = 12
    )

    frame_counter : IntProperty(
        name="Frame counter",
        description="Internal counter used to insert frames at every record_rate",
        default = 1,
        soft_min = 1
    )