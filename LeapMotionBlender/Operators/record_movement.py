from bpy.types import Operator
from .. import communicator

class RecordMovement(Operator):
    """Applies movement vectors obtained from the webserver at the specified frame and in the specified bone group"""
    bl_idname = "leap_operator.record_movement"
    bl_label = "Start recording"
    
    def execute(self, context):
        #Hardcoding is the shit 
        addon_prefs = context.preferences.addons["LeapMotionBlender"].preferences
        (did_start, reason, port) = communicator.force_start(str(addon_prefs.host), int(addon_prefs.port)) 
        if not did_start:
            self.report({"ERROR"}, reason)
            return {"CANCELLED"}
        self.report({"INFO"}, "Server running at port: {}".format(port))
        return {"FINISHED"}
