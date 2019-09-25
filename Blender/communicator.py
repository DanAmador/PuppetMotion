import mathutils
import queue
import threading

from wsgiref.simple_server import make_server

from ws4py.server.wsgirefserver import WSGIServer, WebSocketWSGIRequestHandler
from ws4py.server.wsgiutils import WebSocketWSGIApplication


def broadcast(sockets, message):
    for socket in sockets:
        socket.send(message)


message_queue = queue.Queue()
sockets = []


    
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