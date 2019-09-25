using UnityEngine;
using UnityEditor;
using System.Collections;
using System.Reflection;

namespace UMotionEditor
{
	public static class AnimationCurveUtilityRecent
	{
		//********************************************************************************
		// Public Properties
		//********************************************************************************

        public static bool WeightedTangentsImplemented
        {
            get
            {
                #if UNITY_2018_1_OR_NEWER
                return true;
                #else
                return false;
                #endif
            }
        }

		//********************************************************************************
		// Private Properties
		//********************************************************************************
		
		//----------------------
		// Inspector
		//----------------------
		
		//----------------------
		// Internal
		//----------------------
        #if !UNITY_2017_1_OR_NEWER
        private static MethodInfo getKeyBrokenMethodInfo = null;
        private static MethodInfo getKeyLeftTangentModeMethodInfo = null;
        private static MethodInfo getKeyRightTangentModeMethodInfo = null;
        #endif

		//********************************************************************************
		// Public Methods
		//********************************************************************************

        public static bool GetKeyBroken(AnimationCurve curve, int index)
        {
            #if UNITY_2017_1_OR_NEWER
            return AnimationUtility.GetKeyBroken(curve, index);
            #else
            if (getKeyBrokenMethodInfo == null)
            {
                getKeyBrokenMethodInfo = typeof(AnimationUtility).GetMethod("GetKeyBroken", BindingFlags.NonPublic | BindingFlags.Static);
            }

            return (bool)getKeyBrokenMethodInfo.Invoke(null, new object[] { curve[index] });
            #endif
        }

        public static AnimationUtility.TangentMode GetKeyLeftTangentMode(AnimationCurve curve, int index)
        {
            #if UNITY_2017_1_OR_NEWER
            return AnimationUtility.GetKeyLeftTangentMode(curve, index);
            #else
            if (getKeyLeftTangentModeMethodInfo == null)
            {
                getKeyLeftTangentModeMethodInfo = typeof(AnimationUtility).GetMethod("GetKeyLeftTangentMode", BindingFlags.NonPublic | BindingFlags.Static);
            }

            return (AnimationUtility.TangentMode)getKeyLeftTangentModeMethodInfo.Invoke(null, new object[] { curve[index] });
            #endif
        }

        public static AnimationUtility.TangentMode GetKeyRightTangentMode(AnimationCurve curve, int index)
        {
            #if UNITY_2017_1_OR_NEWER
            return AnimationUtility.GetKeyLeftTangentMode(curve, index);
            #else
            if (getKeyRightTangentModeMethodInfo == null)
            {
                getKeyRightTangentModeMethodInfo = typeof(AnimationUtility).GetMethod("GetKeyRightTangentMode", BindingFlags.NonPublic | BindingFlags.Static);
            }

            return (AnimationUtility.TangentMode)getKeyRightTangentModeMethodInfo.Invoke(null, new object[] { curve[index] });
            #endif
        }

        public static void SetKeyWeightedMode(ref Keyframe key, int weightedMode)
        {
            #if UNITY_2018_1_OR_NEWER
            key.weightedMode = (WeightedMode)weightedMode;
            #endif
        }

        public static int GetKeyWeightedMode(Keyframe key)
        {
            #if UNITY_2018_1_OR_NEWER
            return (int)key.weightedMode;
            #else
            return 0;
            #endif
        }

        public static void SetKeyLeftWeight(ref Keyframe key, float weight)
        {
            #if UNITY_2018_1_OR_NEWER
            key.inWeight = weight;
            #endif
        }

        public static float GetKeyLeftWeight(Keyframe key)
        {
            #if UNITY_2018_1_OR_NEWER
            return key.inWeight;
            #else
            return 1f / 3f;
            #endif
        }

        public static void SetKeyRightWeight(ref Keyframe key, float weight)
        {
            #if UNITY_2018_1_OR_NEWER
            key.outWeight = weight;
            #endif
        }        

        public static float GetKeyRightWeight(Keyframe key)
        {
            #if UNITY_2018_1_OR_NEWER
            return key.outWeight;
            #else
            return 1f / 3f;
            #endif
        }

        public static void InitializeKeyframe(int frame, float value, float inTangent, float outTangent,  int weightedMode, float leftWeight, float rightWeight, out Keyframe key)
        {
            key = new Keyframe(frame, value, inTangent, outTangent);

            #if UNITY_2018_1_OR_NEWER
            key.weightedMode = (WeightedMode)weightedMode;
            key.inWeight = leftWeight;
            key.outWeight = rightWeight;
            #endif
        }

        //********************************************************************************
        // Private Methods
        //********************************************************************************
    }
}
