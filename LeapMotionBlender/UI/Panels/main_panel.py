import bpy
from .leap_panel_base import LeapPanel
from ...Properties import BoneSelectProperty, Leap2BoneProperty
from ...Operators import RecordMovement
from ... import communicator 

class MainLeapPanel(LeapPanel):
    bl_label = "Leap Main"


    def draw(self, context):
        layout = self.layout
        bone_select = bpy.context.scene.BoneSelectProperty
        
        layout.prop(bone_select, "armature_select_enum")        
        
        if bone_select.armature_select_enum:
            props =  context.scene.RecordProperties
            layout.prop(bone_select, "bone_group_enum")
            col = layout.column()
            col.label(text="Running at port: {}".format(communicator.server_port))
            row = col.row()
            frame_col = row.column()
            frame_col.prop(props, "framerate")
            frame_col.prop(props, "record_rate")
            row.prop(props, "move_bones")
            col.operator(RecordMovement.bl_idname, text=props.button_text, icon=props.icon)
