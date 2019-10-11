using System;
using Leap.Unity;
using UnityEngine;

namespace Communicator {
    [Serializable]
    public class SocketPacket {
        public Hand Left, Right;

        public SocketPacket() {
            Left = new Hand();
            Right = new Hand();
        }


        public void UpdateHands(RigidHand leftRH, RigidHand rightRH) {
            if (leftRH.IsTracked) {
                Left.UpdateHand(leftRH);
            }

            if (rightRH.IsTracked) {
                Right.UpdateHand(rightRH);
            }
        }

        public string ToJson() {
            return JsonUtility.ToJson(this);
        }


        #region Data Containers

        [Serializable]
        public class Bone {
            public Vector3 Rotation;
            public Vector3 Position;

            public void UpdateBone(Transform bone, bool local = false) {
                Rotation = ToBlenderQuaternionCoordinate(bone, local);
                Position = ToBlenderVectorCoordinate(bone, local);
            }

            private Vector3 ToBlenderQuaternionCoordinate(Transform bone, bool local) {
                Vector3
                    copy = local
                        ? bone.localEulerAngles
                        : bone.eulerAngles; //ToBlenderVectorCoordinate(rotationEulerAngles); // ToBlenderVectorCoordinate(rotationEulerAngles);
                copy.x = (copy.x + 180) * Mathf.Deg2Rad;
                copy.y = (copy.z + 180) * -Mathf.Deg2Rad;
                copy.z = (copy.y + 180) * Mathf.Deg2Rad;
                return copy;
            }

            private Vector3 ToBlenderVectorCoordinate(Transform bone, bool local) {
                Vector3 vec = local ? bone.localPosition : bone.position;
                Vector3 copy = vec;

                copy.x *= -1;
                copy.z = -vec.y;
                copy.y = -vec.z;

                return copy;
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
            public Finger Thumb, Index, Middle, Pinky, Ring;
            public Bone Palm;

            public Hand() {
                Thumb = new Finger();
                Index = new Finger();
                Middle = new Finger();
                Ring = new Finger();
                Pinky = new Finger();
                Palm = new Bone();
            }


            public void UpdateHand(RigidHand hand) {
                UpdateHand(hand.fingers);

                Palm.UpdateBone(hand.palm, false);
            }

            private void UpdateFingers(FingerModel thumb, FingerModel index, FingerModel middle, FingerModel pinky,
                FingerModel ring) {
                Thumb.UpdateFinger(thumb);
                Index.UpdateFinger(index);
                Middle.UpdateFinger(middle);
                Ring.UpdateFinger(ring);
                Pinky.UpdateFinger(pinky);
            }

            private void UpdateHand(FingerModel[] RhFingers) {
                try {
                    UpdateFingers(RhFingers[0],
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