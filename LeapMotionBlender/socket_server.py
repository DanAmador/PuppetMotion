import socketio
import asyncio 
import websockets
import json
from websockets.exceptions import ConnectionClosedError
from . import communicator

async def websocket_server(websocket, path):
    try:
        async for message in websocket:
            communicator.message_queue.put(json.loads(message))
    except ConnectionClosedError:
        print("Disconnect")
    except JsonDecodeError:
        print("error loading json")


def server_thread_starter( host, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    start_server = websockets.serve(websocket_server, host=host, port=port)
    loop.run_until_complete(start_server)
    loop.run_forever()