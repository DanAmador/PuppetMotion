using UnityEngine;
using WebSocketSharp;

namespace Communicator {
    public class SocketComponent : MonoBehaviour {
        private WebSocket _webSocket;

        public string host = "localhost";
        public int port = 4567;


        private void InterpretMessage(string data) {
            Debug.Log(data);
        }

        public void Send(string data) {
            if (_webSocket != null) {
                _webSocket.Send(data);
            }
        }

        public void SetUpConnection(string host, int port) {
            DisposeConnection();

            this.host = host;
            this.port = port;
            _webSocket = new WebSocket($"ws://{host}:{port}");
            _webSocket.Connect();

            _webSocket.OnMessage += InterpretMessageCallback;
        }

        private void DisposeConnection() {
            if (_webSocket != null) {
                _webSocket.OnMessage -= InterpretMessageCallback;
                _webSocket.Close();
            }
        }


        private void InterpretMessageCallback(object sender, MessageEventArgs e) {
            InterpretMessage(e.Data);
        }
    }
}