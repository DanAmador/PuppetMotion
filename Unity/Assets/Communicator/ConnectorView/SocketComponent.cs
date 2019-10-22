using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using WebSocketSharp;

namespace Communicator
{
    public partial class SocketComponent //another partial of this class already contains Monobehaviour
    {
        private void SetUpConnection()
        {
            _webSocket = new WebSocket($"ws://{host}:{port}");
            _webSocket.Connect();
            _webSocket.OnMessage += InterpretMessageCallback; // in this way I'm sure it's pointing the same point of memory for subscribe or desubscribe the event.
        }

        private void DisposeConnection()
        {
            if ((object)_webSocket != null)
            {
                _webSocket.OnMessage -= InterpretMessageCallback;
                _webSocket.Close();
            }
        }

        public void NewConnection(string host, int port)
        {
            DisposeConnection();
            this.host = host;
            this.port = port;
            SetUpConnection();
        }

        private void InterpretMessageCallback(object sender, MessageEventArgs e)
        {
            InterpretMessage(e.Data);
        }
    }
}
