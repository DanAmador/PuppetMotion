
import bpy
import queue
import threading
import asyncio
import socketio
import socket

from bpy.app.handlers import persistent
from aiohttp import web



wserver = None
running  = False
message_queue = queue.Queue()


def start_server(host, port):
    global running
    global wserver
    if wserver:
        return (False, "The server is already running")
    if is_port_open(host,port):
        return (False, "The port is not open")
    wserver = threading.Thread(target=run_server, args=(aiohttp_server(),host,port,))
    wserver.daemon = True
    wserver.start()

    return (True, "Server started at port: {}".format(port))



def run_server(runner, host, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, host, port)
    loop.run_until_complete(site.start())
    loop.run_forever()

def aiohttp_server():
    sio = socketio.AsyncServer(async_mode='aiohttp')

    def say_hello(request):
        print("bitch mother fuck")
        message_queue.put("hello motherfucker")
        return web.Response(text='Hello, world')

    @sio.on("beep")
    def beep(sid, data):
        print("beep")

    app = web.Application()

    app.add_routes([web.get('/', say_hello)])

    sio.attach(app)

    runner = web.AppRunner(app)
    return runner

def search_and_start(host, port):
    offset = 0

    while(not is_port_open(port + offset)):
        offset += 1
    
    start_server(host, port+offset)

    
def is_port_open(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False


@persistent
def handle_messages():
    while not message_queue.empty():
        message = message_queue.get()
        print(message)
