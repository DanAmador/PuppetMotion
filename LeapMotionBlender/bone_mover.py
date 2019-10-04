import bpy
import json
import mathutils
from .Properties import Leap2BoneProperty
from .communicator import message_queue as mq

def move_bones():
    props = bpy.context.scene.RecordProperties
    bones_in_group = Leap2BoneProperty.get_bones_in_selected_group()
    while not mq.empty():
        try:
            actions = mq.get()
            for bone in bones_in_group:
                leap = bone.LeapProperties
                if leap.handedness == "None":
                    continue
                bone_action = actions[leap.handedness][leap.finger_select]["bones"][leap.finger_joint]
                if leap.rot_pos[0]:
                    bone.rotation_mode = "QUATERNION"
                    # quat = mathutils.Quaternion(*tuple(bone_action["Rotation"]))
                    bone.rotation_quaternion = list(bone_action["Rotation"].values())
                if leap.rot_pos[1]:
                    for indx,val in enumerate(bone_action["Position"].values()):
                        bone.location[indx] += val
                    # translation = mathutils.Vector(tuple(bone_action["Position"].values()))
                    # print(translation)

                    # bone.translate(translation)
                # if leap.rot_pos[1]:
                #     print(bone_)
                # if props.recording:
                #     print("Bruh")
        except Exception as e:
            print(e)



    
    return 1/props.framerate

    