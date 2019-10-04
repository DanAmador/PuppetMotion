import bpy
from bpy.app.handlers import persistent
from bpy.props import BoolProperty, EnumProperty, IntProperty, PointerProperty, StringProperty
from bpy.types import AddonPreferences

from ...Operators import ForceStart
from ... import communicator 

class SettingsPanel(AddonPreferences):
    bl_idname = "LeapMotionBlender"
    
    auto_start : BoolProperty(
        name="Start automatically",
        description="Automatically start the server when loading the add-on",
        default=True
    )
    
    host : StringProperty(
        name="Host",
        description="Listen on host:port",
        default="localhost"
    )
    
    port : IntProperty(
        name="Port",
        description="Listen on host:port",
        default=4567,
        min=0,
        max=65535,
        subtype="UNSIGNED"
    )

        
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        split = row.split(factor=0.3)
        
        col = split.column()
        col.prop(self, "host")
        col.prop(self, "port")
        col.separator()

        col.prop(self, "auto_start")
        
        if communicator.server_port != 0:
            col.label(text="Running at port: {}".format(communicator.server_port))
        
        if not communicator.wserver:
            col.operator(ForceStart.bl_idname, icon='QUIT', text="Start server")


        col = split.column()