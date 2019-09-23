using Leap.Unity;
using SocketIO;
using UnityEngine;

namespace Communicator {
    [RequireComponent(typeof(SocketIOComponent))]
    public class Communicator : MonoBehaviour {
        public RigidHand rightHand, leftHand;
        private SocketPacket _sp;
        [Range(1, 60)] public int sampleRate = 1;

        private float _timePerSample;

        private float _lastSample;

        private SocketIOComponent _socketIoComponent;

        void Start() {
            _sp = new SocketPacket();
            _lastSample = Time.time;
            ChangeSampleRate(sampleRate);
            _socketIoComponent = GetComponent<SocketIOComponent>();
            _socketIoComponent.On("boop",
                (SocketIOEvent e) => { Debug.Log("Fuck me "); });
        }

        void LateUpdate() {
            if (Time.time - _lastSample > _timePerSample) {
                _sp.UpdateHands(leftHand, rightHand);
                if (_socketIoComponent.isActiveAndEnabled && _socketIoComponent.IsConnected) {
                    _socketIoComponent.Emit("unityBones", _sp.ToJson());
                }

                _lastSample = Time.time;
            }
        }


        public void ChangeSampleRate(int n) {
            sampleRate = n;

            _timePerSample = 1 / (float) n;
        }
    }
}