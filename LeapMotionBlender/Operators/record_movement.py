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
    bl_label = "Start Recording"

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        props= context.scene.RecordProperties

        props.recording = not props.recording
        props.move_bones = True

        return self.execute(context)