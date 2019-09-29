using Leap.Unity;
using UnityEngine;

namespace Communicator {
    [RequireComponent(typeof(SocketComponent))]
    public class Communicator : MonoBehaviour {
        public RigidHand rightHand, leftHand;
        private SocketPacket _sp;
        [Range(1, 60)] public int sampleRate = 1;

        private float _timePerSample;

        private float _lastSample;

        private SocketComponent _socketComponent;

        void Start() {
            _sp = new SocketPacket();
            _lastSample = Time.time;
            ChangeSampleRate(sampleRate);
            _socketComponent = GetComponent<SocketComponent>();
        }

        void LateUpdate() {
            if (Time.time - _lastSample > _timePerSample) {
                _sp.UpdateHands(leftHand, rightHand);
            
                if(_socketComponent.isActiveAndEnabled){
                    _socketComponent.Send(_sp.ToJson());
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