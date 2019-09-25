using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

namespace UMotionEditor
{
    public static class HandlesUtility
    {
        //********************************************************************************
        // Public Properties
        //********************************************************************************

        //********************************************************************************
        // Private Properties
        //********************************************************************************

        //********************************************************************************
        // Public Methods
        //********************************************************************************

        public static Vector3 HandlesSliderArrowCap(Vector3 position, Vector3 direction, float size, float snap)
        {
            #if UNITY_5_6_OR_NEWER
            return Handles.Slider(position, direction, size, new Handles.CapFunction(Handles.ArrowHandleCap), snap);
            #else
            return Handles.Slider(position, direction, size, new Handles.DrawCapFunction(Handles.ArrowCap), snap);
            #endif
        }

        public static Vector3 FreeMoveHandleRectangleCap(Vector3 position, Quaternion rotation, float size, Vector3 snap)
        {
            #if UNITY_5_6_OR_NEWER
            return Handles.FreeMoveHandle(position, rotation, size, snap, new Handles.CapFunction(Handles.RectangleHandleCap));
            #else
            return Handles.FreeMoveHandle(position, rotation, size, snap, new Handles.DrawCapFunction(Handles.RectangleCap));
            #endif
        }

        public static float ScaleValueHandleCubeCap(float value, Vector3 position, Quaternion rotation, float size, float snap)
        {
            #if UNITY_5_6_OR_NEWER
            return Handles.ScaleValueHandle(value, position, rotation, size, new Handles.CapFunction(Handles.CubeHandleCap), snap);
            #else
            return Handles.ScaleValueHandle(value, position, rotation, size, new Handles.DrawCapFunction(Handles.CubeCap), snap);
            #endif
        }

        public static Vector3 Slider2DRectangleCap(int id, Vector3 handlePos, Vector3 offset, Vector3 handleDir, Vector3 sliderDir1, Vector3 sliderDir2, float handleSize, Vector2 snap)
        {
            #if UNITY_5_6_OR_NEWER
            return Handles.Slider2D(id, handlePos, offset, handleDir, sliderDir1, sliderDir2, handleSize, new Handles.CapFunction(Handles.RectangleHandleCap), snap);
            #else
            return Handles.Slider2D(id, handlePos, offset, handleDir, sliderDir1, sliderDir2, handleSize, new Handles.DrawCapFunction(Handles.RectangleCap), snap);
            #endif
        }

        public static RenderTexture CopyRenderTexture(RenderTexture textureToCopy)
        {
            #if UNITY_2017_1_OR_NEWER
            return new RenderTexture(textureToCopy);
            #else
            RenderTexture renderTexture = new RenderTexture(textureToCopy.width, textureToCopy.height, textureToCopy.depth, textureToCopy.format);
            renderTexture.antiAliasing = textureToCopy.antiAliasing;
            renderTexture.hideFlags = textureToCopy.hideFlags;

            return renderTexture;
            #endif
        }

        //********************************************************************************
        // Private Methods
        //********************************************************************************
    }
}