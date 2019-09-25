using UnityEngine;
using UnityEditor;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;

#if UNITY_2017_3_OR_NEWER
using UnityEditor.Compilation;
#endif

namespace UMotionEditor
{
	public static class AnimatorUtility
	{
		//********************************************************************************
		// Public Properties
		//********************************************************************************

        public enum Muscle
        {
            SpineFrontBack = 0,
            SpineLeftRight,
            SpineTwistLeftRight,
            ChestFrontBack,
            ChestLeftRight,
            ChestTwistLeftRight,
            // Was added in Unity 5.6 and higher
            UpperChestFrontBack,
            UpperChestLeftRight,
            UpperChestTwistLeftRight,
            // End
            NeckNodDownUp,
            NeckTiltLeftRight,
            NeckTurnLeftRight,
            HeadNodDownUp,
            HeadTiltLeftRight,
            HeadTurnLeftRight,
            LeftEyeDownUp,
            LeftEyeInOut,
            RightEyeDownUp,
            RightEyeInOut,
            JawClose,
            JawLeftRight,
            LeftUpperLegFrontBack,
            LeftUpperLegInOut,
            LeftUpperLegTwistInOut,
            LeftLowerLegStretch,
            LeftLowerLegTwistInOut,
            LeftFootUpDown,
            LeftFootTwistInOut,
            LeftToesUpDown,
            RightUpperLegFrontBack,
            RightUpperLegInOut,
            RightUpperLegTwistInOut,
            RightLowerLegStretch,
            RightLowerLegTwistInOut,
            RightFootUpDown,
            RightFootTwistInOut,
            RightToesUpDown,
            LeftShoulderDownUp,
            LeftShoulderFrontBack,
            LeftArmDownUp,
            LeftArmFrontBack,
            LeftArmTwistInOut,
            LeftForearmStretch,
            LeftForearmTwistInOut,
            LeftHandDownUp,
            LeftHandInOut,
            RightShoulderDownUp,
            RightShoulderFrontBack,
            RightArmDownUp,
            RightArmFrontBack,
            RightArmTwistInOut,
            RightForearmStretch,
            RightForearmTwistInOut,
            RightHandDownUp,
            RightHandInOut,
            LeftThumb1Stretched,
            LeftThumbSpread,
            LeftThumb2Stretched,
            LeftThumb3Stretched,
            LeftIndex1Stretched,
            LeftIndexSpread,
            LeftIndex2Stretched,
            LeftIndex3Stretched,
            LeftMiddle1Stretched,
            LeftMiddleSpread,
            LeftMiddle2Stretched,
            LeftMiddle3Stretched,
            LeftRing1Stretched,
            LeftRingSpread,
            LeftRing2Stretched,
            LeftRing3Stretched,
            LeftLittle1Stretched,
            LeftLittleSpread,
            LeftLittle2Stretched,
            LeftLittle3Stretched,
            RightThumb1Stretched,
            RightThumbSpread,
            RightThumb2Stretched,
            RightThumb3Stretched,
            RightIndex1Stretched,
            RightIndexSpread,
            RightIndex2Stretched,
            RightIndex3Stretched,
            RightMiddle1Stretched,
            RightMiddleSpread,
            RightMiddle2Stretched,
            RightMiddle3Stretched,
            RightRing1Stretched,
            RightRingSpread,
            RightRing2Stretched,
            RightRing3Stretched,
            RightLittle1Stretched,
            RightLittleSpread,
            RightLittle2Stretched,
            RightLittle3Stretched,
        }

        public static HumanBodyBones LastBone
        {
            get
            {
                return HumanBodyBones.LastBone;
            }
        }

        public static HumanBodyBones UpperChest
        {
            get
            {
                #if UNITY_5_6_OR_NEWER
                return HumanBodyBones.UpperChest;
                #else
                return (HumanBodyBones)54;
                #endif
            }
        }

        public static bool HasUpperChest
        {
            get
            {
                #if UNITY_5_6_OR_NEWER
                return true;
                #else
                return false;
                #endif
            }
        }

        public static ReadOnlyCollection<HumanBodyBones> RequiredHumanoidBones
        {
            get
            {
                return requiredHumanoidBones;
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

        private static ReadOnlyCollection<HumanBodyBones> requiredHumanoidBones = new ReadOnlyCollection<HumanBodyBones>(new HumanBodyBones[] { HumanBodyBones.Hips,
                                                                                                                                                HumanBodyBones.Spine,
                                                                                                                                                HumanBodyBones.LeftUpperArm,
                                                                                                                                                HumanBodyBones.LeftLowerArm,
                                                                                                                                                HumanBodyBones.LeftHand,
                                                                                                                                                HumanBodyBones.RightUpperArm,
                                                                                                                                                HumanBodyBones.RightLowerArm,
                                                                                                                                                HumanBodyBones.RightHand,
                                                                                                                                                HumanBodyBones.LeftUpperLeg,
                                                                                                                                                HumanBodyBones.LeftLowerLeg,
                                                                                                                                                HumanBodyBones.LeftFoot,
                                                                                                                                                HumanBodyBones.RightUpperLeg,
                                                                                                                                                HumanBodyBones.RightLowerLeg,
                                                                                                                                                HumanBodyBones.RightFoot,
                                                                                                                                                HumanBodyBones.Head });

		//********************************************************************************
		// Public Methods
		//********************************************************************************
		
        public static void AnimatorStop(Animator animator)
        {
            #if UNITY_5_6_OR_NEWER
            animator.enabled = false;
            animator.enabled = true;
            #else
            animator.Stop();
            #endif
        }

        public static void AnimatorRebindIfRequired(Animator animator)
        {
            if ((animator != null) && !animator.isInitialized)
            {
                animator.Rebind();
            }
        }

        public static int GetMuscleIndex(Muscle muscle)
        {
            #if UNITY_5_6_OR_NEWER
            return (int)muscle;
            #else
            if ((muscle == Muscle.UpperChestFrontBack) ||
                (muscle == Muscle.UpperChestLeftRight) ||
                (muscle == Muscle.UpperChestTwistLeftRight))
            {
                throw new UnityException("Upper chest not available in this Unity version.");
            }
            else if (muscle >= Muscle.NeckNodDownUp)
            {
                return (int)muscle - 3; // Upper Chest was inserted
            }
            else
            {
                return (int)muscle;
            }
            #endif
        }

        public static string[] GetAssemblyNamesRelevantForEvents()
        {
            #if UNITY_2017_3_OR_NEWER
            List<string> assemblyNamesList = new List<string>();
            foreach (UnityEditor.Compilation.Assembly assembly in CompilationPipeline.GetAssemblies())
            {
                if ((assembly.flags & AssemblyFlags.EditorAssembly) == AssemblyFlags.None)
                {
                    assemblyNamesList.Add(assembly.name);
                }
            }
            return assemblyNamesList.ToArray();
            #else
            return new string[] { "Assembly-CSharp", "Assembly-UnityScript" };
            #endif
        }

        public static bool IsModelPrefab(GameObject gameObject)
        {
            #if UNITY_2018_3_OR_NEWER
            return (PrefabUtility.GetPrefabAssetType(gameObject) == PrefabAssetType.Model);
            #else
            return (PrefabUtility.GetPrefabType(gameObject) == PrefabType.ModelPrefab);
            #endif
        }

        public static bool IsPrefab(GameObject gameObject)
        {
            #if UNITY_2018_3_OR_NEWER
            return (PrefabUtility.GetPrefabAssetType(gameObject) != PrefabAssetType.NotAPrefab);
            #else
            return (PrefabUtility.GetPrefabType(gameObject) != PrefabType.None);
            #endif
        }

		//********************************************************************************
		// Private Methods
		//********************************************************************************
		
	}
}
