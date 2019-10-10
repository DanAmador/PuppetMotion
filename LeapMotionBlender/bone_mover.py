import bpy
import json
import mathutils
from .Properties import Leap2BoneProperty
from .communicator import message_queue as mq
from math import radians

axes = ("X", "Y", "Z")
finger_names = ("Thumb", "Index", "Middle", "Ring", "Pinky")
def move_track_bone(bone_action, bone, leapProp = None):
    leap = bone.LeapProperties if leapProp is None else leapProp
    #Apply Rotation
    if leap.rot_pos[0]:
        bone.rotation_mode = "XYZ"
        rot_list = []
        
        # rot_list = list(bone_action["Rotation"].values())
        # bone.rotation_quaternion = rot_list
        for idx, val in enumerate(bone_action["Rotation"].values()):
            rot_list.append(val * leap.rot_select[idx])
        
        bone.rotation_euler = rot_list
    
    #Apply Translation
    if leap.rot_pos[1] and leapProp is not None:
        for indx,val in enumerate(bone_action["Position"].values()):
            bone.location[indx] = val *  leap.scale_factor[indx]


def move_track_hand(actions, bone):
    leap = bone.LeapProperties

    for finger in bone.children_recursive:
        (fin    ger_name, _ , joint_num) = finger.name.split(".")        
        joint_num = int(joint_num)
        bone_action = actions[leap.handedness][finger_name]["bones"][int(joint_num)]
        move_track_bone(bone_action, finger, leapProp=leap)
    
    palm_action = actions[leap.handedness]["Palm"]
    move_track_bone(palm_action, bone)
            
def move_bones():
    props = bpy.context.scene.RecordProperties
    bones_in_group = Leap2BoneProperty.get_bones_in_selected_group()
    while not mq.empty():
            actions = mq.get()
            for bone in bones_in_group:
                leap = bone.LeapProperties
                if leap.handedness == "None":
                    continue


                if leap.track_type == "Bone":
                    bone_action = actions[leap.handedness][leap.finger_select]["bones"][leap.finger_joint]            
                    move_track_bone(bone_action, bone)
                
                if leap.track_type == "Hand":
                    move_track_hand(actions, bone)

                if props.recording:
                    if props.frame_counter % props.record_rate == 0 and props.frame_counter != 0:
                        if leap.rot_pos[1]:
                            bone.keyframe_insert(data_path="location",frame=props.frame_counter + props.start_frame)
                        if leap.rot_pos[0]:
                            for idx, axis in enumerate(axes):
                                if leap.rot_select[idx]:
                                    bone.keyframe_insert(data_path="rotation_euler",frame=props.frame_counter + props.start_frame, index=idx)
            
            if props.recording:
                props.frame_counter += 1
    return 1/props.framerate

