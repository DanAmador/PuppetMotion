using System;
using UnityEngine;
using WebSocketSharp;

namespace Communicator {
    public partial class SocketComponent : MonoBehaviour {
        private WebSocket _webSocket;

        public string host = "localhost";
        public int port = 4567;


        private void InterpretMessage(string data) {
            Debug.Log(data);
        }

        public void Send(string data) {
            if ((object)_webSocket != null)
            {
                _webSocket.Send(data);
            }
        }


    }
}