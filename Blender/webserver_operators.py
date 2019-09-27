from bpy.types import Operator
from . import communicator


class Start(Operator):
    """Start WebSocket server"""
    bl_idname = "websocket_server.start"
    bl_label = "Start WebSocket server"
    
    def execute(self, context):
        addon_prefs = context.preferences.addons[__package__].preferences
        (started_server, reason) = communicator.start_server(str(addon_prefs.host), int(addon_prefs.port)) 
        if not started_server:
            self.report({"ERROR"}, reason)
            return {"CANCELLED"}
        self.report(reason)
        return {"FINISHED"}

# class Stop(Operator):
#     """Stop WebSocket server"""
#     bl_idname = "websocket_server.stop"
#     bl_label = "Stop WebSocket server"
    
#     def execute(self, context):
#         if not communicator.stop_server():
#             self.report({"ERROR"}, "The server is not started.")
#             return {"CANCELLED"}
#         return {"FINISHED"}
    