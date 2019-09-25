using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

namespace UMotionEditor
{
    public static class PlayModeUtility
    {
        //********************************************************************************
        // Public Properties
        //********************************************************************************

        public static event EditorApplication.CallbackFunction OnPlayModeStateChanged
        {
            add
            {
                #if UNITY_2017_2_OR_NEWER
                onPlayModeStateChanged += value;

                if (!initialized)
                {
                    EditorApplication.playModeStateChanged += PlayModeStateChanged;
                    EditorApplication.pauseStateChanged += PauseStateChanged;
                    initialized = true;
                }
                #else
                EditorApplication.playmodeStateChanged += value;
                #endif
            }
            remove
            {
                #if UNITY_2017_2_OR_NEWER
                onPlayModeStateChanged -= value;
                #else
                EditorApplication.playmodeStateChanged -= value;
                #endif
            }
        }

        //********************************************************************************
        // Private Properties
        //********************************************************************************

        #if UNITY_2017_2_OR_NEWER
        private static event EditorApplication.CallbackFunction onPlayModeStateChanged;
        private static bool initialized = false;
        #endif

        //********************************************************************************
        // Public Methods
        //********************************************************************************

        //********************************************************************************
        // Private Methods
        //********************************************************************************

        #if UNITY_2017_2_OR_NEWER
        private static void PlayModeStateChanged(PlayModeStateChange state)
        {
            if (onPlayModeStateChanged != null)
            {
                onPlayModeStateChanged();
            }
        }

        private static void PauseStateChanged(PauseState state)
        {
            if (onPlayModeStateChanged != null)
            {
                onPlayModeStateChanged();
            }
        }
        #endif
    }
}
