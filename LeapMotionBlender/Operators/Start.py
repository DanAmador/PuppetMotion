from bpy.types import Operator
from .. import communicator


class Start(Operator):
    """Start WebSocket server"""
    bl_idname = "websocket_server.start"
    bl_label = "Start WebSocket server"
    
    def execute(self, context):
        #Hardcoding is the shit 
        addon_prefs = context.preferences.addons["LeapMotionBlender"].preferences
        (started_server, reason) = communicator.start_server(str(addon_prefs.host), int(addon_prefs.port)) 
        if not started_server:
            self.report({"ERROR"}, reason)
            return {"CANCELLED"}
        self.report({"INFO"}, reason)
        return {"FINISHED"}
