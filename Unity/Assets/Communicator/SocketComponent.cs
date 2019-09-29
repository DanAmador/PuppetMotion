using System.Collections;
using System.Collections.Generic;
using Newtonsoft.Json;
using UnityEngine;
using WebSocketSharp;

namespace Communicator {
    public class SocketComponent : MonoBehaviour {
        private WebSocket _webSocket;

        public string host = "localhost";
        public int port = 4567;

        void Start() {
            _webSocket = new WebSocket($"ws://{host}:{port}");
            _webSocket.Connect();
            _webSocket.OnMessage += (sender, e) => InterpretMessage(e.Data);
        }

        private void InterpretMessage(string data) {
            Debug.Log(data);
        }

        public void Send(string data) {
            _webSocket.Send(data);
        }

        void Update() { }

    }
}