import bpy
import json
from bpy.types import Operator
from bpy.props import IntProperty, BoolProperty, StringProperty
from .. import communicator
from ..general_helpers import RegisterMixin
from ..Properties import RecordProperties,  Leap2BoneProperty

class RecordMovement(RegisterMixin, Operator):
    """Applies movement vectors obtained from the webserver at the specified frame and in the specified bone group"""
    _classes = (RecordProperties,)    
    bl_idname = "leap_operator.record_movement"
    bl_label = "Start Recordi asdasdng"

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        props= context.scene.RecordProperties

        props.recording = not props.recording
        props.move_bones = True

        return self.execute(context)
    
    def modal(self, context, event):
        props = context.scene.RecordProperties
        if event.type in ("LEFTMOUSE", "RIGHTMOUSE"):
            props.recording = not props.recording
        # if event.type =="TIMER":
        #      while not message_queue.empty():
        #         try:
        #             message = json.loads(mq.get())
        #             movement = message.get("movement")

        #             self.move_bones(movement)
        #         except JsonDecodeError as e :
        #             print(e)
        #             continue

        return {'RUNNING_MODAL'} if props.recording else {'FINISHED'}
