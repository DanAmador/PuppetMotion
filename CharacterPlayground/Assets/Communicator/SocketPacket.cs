using System;
using Leap.Unity;
using UnityEngine;

namespace Communicator {
    [Serializable]
    public class SocketPacket {
        public Hand left, right;

        public SocketPacket() {
            left = new Hand();
            right = new Hand();
        }


        public void UpdateHands(RigidHand leftRH, RigidHand rightRH) {
            if (leftRH.IsTracked) {
                left.UpdateHand(leftRH.fingers);
            }

            if (rightRH.IsTracked) {
                right.UpdateHand(rightRH.fingers);
            }
        }

        public string ToJson() {
            return JsonUtility.ToJson(this);
        }


        #region Data Containers

        [Serializable]
        public class Bone {
            public Quaternion rotation;
            public Vector3 position;

            public void UpdateBone(Transform bone) {
                rotation = bone.rotation;
                position = bone.position;
            }
        }

        [Serializable]
        public class Finger {
            public Bone[] bones;

            public Finger() {
                bones = new Bone[3];
            }


            public void UpdateFinger(FingerModel finger) {
                int idx = 0;
                foreach (Transform bone in finger.bones) {
                    try {
                        if (bone == null) {
                            continue;
                        }

                        bones[idx++].UpdateBone(bone);
                    }
                    catch (Exception e) { }
                }
            }
        }


        [Serializable]
        public class Hand {
            public Finger thumb, index, middle, pinky, ring;

            public Hand() {
                thumb = new Finger();
                index = new Finger();
                middle = new Finger();
                ring = new Finger();
                pinky = new Finger();
            }


            public void UpdateHand(FingerModel thumb, FingerModel index, FingerModel middle, FingerModel pinky,
                FingerModel ring) {
                this.thumb.UpdateFinger(thumb);
                this.index.UpdateFinger(index);
                this.middle.UpdateFinger(middle);
                this.ring.UpdateFinger(ring);
                this.pinky.UpdateFinger(pinky);
            }


            public void UpdateHand(FingerModel[] RhFingers) {
                try {
                    UpdateHand(RhFingers[0],
                        RhFingers[1],
                        RhFingers[2],
                        RhFingers[3],
                        RhFingers[4]);
                }
                catch (IndexOutOfRangeException e) {
                    Debug.Log(e);
                }
            }
        }

        #endregion
    }
}