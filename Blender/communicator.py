bl_info = {
    "name": "Leap Motion Integration",
    "author": "Dan Amador",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "description": "Communicate with an external Unity process processing Leap motion Data",
    "category": "Import-Export"
}

import bpy
from bpy.app.handlers import persistent
from bpy.props import BoolProperty, EnumProperty, IntProperty, PointerProperty, StringProperty
from bpy.types import AddonPreferences, Operator, Panel, PropertyGroup, USERPREF_HT_header, WindowManager

import copy
import json
import mathutils
import queue
import threading

from wsgiref.simple_server import make_server
from ws4py.websocket import WebSocket as _WebSocket
from ws4py.server.wsgirefserver import WSGIServer, WebSocketWSGIRequestHandler
from ws4py.server.wsgiutils import WebSocketWSGIApplication


previous_context = {}
previous_data_keys = {}
previous_scenes = {}

def get_context(addon_prefs, diff):
    global previous_context
    
    current_context = {
        "filePath": bpy.data.filepath,
        "selectedObjects": hasattr(bpy.context, "selected_objects") and list(object.name for object in bpy.context.selected_objects)
    }
    
    if previous_context == current_context and diff:
        return
        
    previous_context = current_context
    return current_context


def get_scene(scene, addon_prefs, diff):
    global previous_scenes
    previous_scene = previous_scenes.get(scene.name, None)
    
    current_scene = {
        "activeObject": scene.objects.active and scene.objects.active.name,
        "camera": scene.camera and scene.camera.name,
        "fps": scene.render.fps / scene.render.fps_base,
        "frame": scene.frame_current,
        "frameEnd": scene.frame_end,
        "frameStart": scene.frame_start,
        "gravity": scene.gravity,
        "objects": list(object.name for object in scene.objects),
        "timelineMarkers": list(scene.timeline_markers),
        "world": scene.world and scene.world.name
    }
    
    if previous_scene == current_scene and diff:
        return
        
    previous_scenes[scene.name] = current_scene
    return current_scene

def broadcast(sockets, message):
    for socket in sockets:
        socket.send(message)


message_queue = queue.Queue()
sockets = []

class WebSocketApp(_WebSocket):
    def opened(self):
        send_state([self])
        sockets.append(self)
        
    def closed(self, code, reason=None):
        sockets.remove(self)
        
    def received_message(self, message):
        data = json.loads(message.data.decode(message.encoding))
        message_queue.put(data)
    
wserver = None

def start_server(host, port):
    global wserver
    if wserver:
        return False
    
    wserver = make_server(host, port,
        server_class=WSGIServer,
        handler_class=WebSocketWSGIRequestHandler,
        app=WebSocketWSGIApplication(handler_cls=WebSocketApp)
    )
    wserver.initialize_websockets_manager()
    
    wserver_thread = threading.Thread(target=wserver.serve_forever)
    wserver_thread.daemon = True
    wserver_thread.start()
    
    bpy.app.handlers.load_post.append(load_post)
    bpy.app.handlers.scene_update_post.append(scene_update_post)
    
    return True

def stop_server():
    global wserver
    if not wserver:
        return False
        
    wserver.shutdown()
    for socket in sockets:
        socket.close()
        
    wserver = None
    
#    bpy.app.handlers.load_post.remove(load_post)
 #   bpy.app.handlers.scene_update_post.remove(scene_update_post)
    
    return True


class WebSocketServerSettings(AddonPreferences):
    bl_idname = __name__
    
    auto_start = BoolProperty(
        name="Start automatically",
        description="Automatically start the server when loading the add-on",
        default=True
    )
    
    host = StringProperty(
        name="Host",
        description="Listen on host:port",
        default="localhost"
    )
    
    port = IntProperty(
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
        split = row.split(percentage=0.3)
        
        col = split.column()
        col.prop(self, "host")
        col.prop(self, "port")
        col.separator()
        
        col.prop(self, "auto_start")
        
        if wserver:
            col.operator(Stop.bl_idname, icon='QUIT', text="Stop server")
        else:
            col.operator(Start.bl_idname, icon='QUIT', text="Start server")
            
        col = split.column()
        col.label("Data to send:", icon='RECOVER_LAST')
        col.prop(self, "data_to_send", expand=True)

class Start(Operator):
    """Start WebSocket server"""
    bl_idname = "websocket_server.start"
    bl_label = "Start WebSocket server"
    
    def execute(self, context):
        addon_prefs = context.user_preferences.addons[__name__].preferences
        if not start_server(str(addon_prefs.host), int(addon_prefs.port)):
            self.report({"ERROR"}, "The server is already started.")
            return {"CANCELLED"}
        return {"FINISHED"}

class Stop(Operator):
    """Stop WebSocket server"""
    bl_idname = "websocket_server.stop"
    bl_label = "Stop WebSocket server"
    
    def execute(self, context):
        if not stop_server():
            self.report({"ERROR"}, "The server is not started.")
            return {"CANCELLED"}
        return {"FINISHED"}
    
def register():
    bpy.utils.register_module(__name__)
    
    addon_prefs = bpy.context.user_preferences.addons[__name__].preferences
    if bool(addon_prefs.auto_start):
        start_server(str(addon_prefs.host), int(addon_prefs.port))

def unregister():
    stop_server()
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()