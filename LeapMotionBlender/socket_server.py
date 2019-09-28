import socketio
import asyncio 
import websockets
from . import communicator

async def websocket_server(websocket, path):
    async for message in websocket:
        print(message)
        communicator.message_queue.put(message)




def server_thread_starter( host, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    start_server = websockets.serve(websocket_server, host=host, port=port)
    loop.run_until_complete(start_server)
    loop.run_forever()