using System;
using Leap.Unity;
using UnityEngine;

namespace Communicator {
    public class Communicator : MonoBehaviour {
        public RigidHand rightHand, leftHand;
        private SocketPacket _sp;


        void Start() {
            _sp = new SocketPacket();
        }

        void Update() {
            _sp.UpdateHands(leftHand, rightHand);
            
            Debug.Log(_sp.ToJson());
        }
    }
}