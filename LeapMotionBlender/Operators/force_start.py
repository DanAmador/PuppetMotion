from bpy.types import Operator
from .. import communicator
class ForceStart(Operator):
    """Force start with some open port"""
    bl_idname = "websocket_server.force_start"
    bl_label = "Force start server"
    
    def execute(self, context):
        #Hardcoding is the shit 
        addon_prefs = context.preferences.addons["LeapMotionBlender"].preferences
        (did_start, reason, port) = communicator.force_start(str(addon_prefs.host), int(addon_prefs.port)) 
        if not did_start:
            self.report({"ERROR"}, reason)
            return {"CANCELLED"}
        self.report({"INFO"}, "Server running at port: {}".format(port))
        return {"FINISHED"}
