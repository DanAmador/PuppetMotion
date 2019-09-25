from ws4py.websocket import WebSocket as _WebSocket
import json

import communicator

class WebSocketApp(_WebSocket):
    def opened(self):
        #send_state([self])
        communicator.sockets.append(self)
        
    def closed(self, code, reason=None):
        communicator.sockets.remove(self)
        
    def received_message(self, message):
        communicator.message_queue.put(json.loads(message.data.decode(message.encoding)))