import socketio
from aiohttp import web

from . import communicator
def spawn_server():
    sio = socketio.AsyncServer(async_mode='aiohttp')

    def say_hello(request):
        print("bitch mother fuck")
        communicator.message_queue.put("hello motherfucker")
        sio.emit('fuck')
        return web.Response(text='Hello, world')

    @sio.on('beep')
    def beep(sid, data):
        print("beep")

    app = web.Application()

    app.add_routes([web.get('/', say_hello)])

    sio.attach(app)

    runner = web.AppRunner(app)
    return runner
