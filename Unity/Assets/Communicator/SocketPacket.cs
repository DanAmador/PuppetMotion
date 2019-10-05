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
                Left.UpdateHand(leftRH.fingers);
            }

            if (rightRH.IsTracked) {
                Right.UpdateHand(rightRH.fingers);
            }
        }

        public string ToJson() {
            return JsonUtility.ToJson(this);
        }


        #region Data Containers

        [Serializable]
        public class Bone {
            private Vector3 lastPos, currPos;
            public Quaternion Rotation;
            public Vector3 Position;

            public void UpdateBone(Transform bone) {
                lastPos = currPos;
                currPos = bone.position;
                Rotation = bone.rotation;
                Position = ToBlenderCoordinate(currPos);
            }

            private Vector3 ToBlenderCoordinate(Vector3 vec) {
                Vector3 copy = vec;

                copy.x *= -1;
                copy.z = vec.y;
                copy.y = vec.z;

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

            public Hand() {
                Thumb = new Finger();
                Index = new Finger();
                Middle = new Finger();
                Ring = new Finger();
                Pinky = new Finger();
            }


            public void UpdateHand(FingerModel thumb, FingerModel index, FingerModel middle, FingerModel pinky,
                FingerModel ring) {
                Thumb.UpdateFinger(thumb);
                Index.UpdateFinger(index);
                Middle.UpdateFinger(middle);
                Ring.UpdateFinger(ring);
                Pinky.UpdateFinger(pinky);
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