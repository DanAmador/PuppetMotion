import bpy
from bpy.props import EnumProperty
from bpy.types import PropertyGroup, Panel
from ..general_helpers import RegisterMixin

def bone_item_callback(scene, context):

    items = [
        ('LOC', "Location", ""),
        ('ROT', "Rotation", ""),
        ('SCL', "Scale", ""),
    ]

    ob = context.object
    if ob is not None:
        if ob.type == 'LAMP':
            items.append(('NRG', "Energy", ""))
            items.append(('COL', "Color", ""))

    return items


class BoneSelectProperty(RegisterMixin, PropertyGroup):
    _ptrProp = True
    mode_options = [
        ("mesh.primitive_plane_add", "Plane", '', 'MESH_PLANE', 0),
        ("mesh.primitive_cube_add", "Cube", '', 'MESH_CUBE', 1),
        ("mesh.primitive_circle_add", "Circle", '', 'MESH_CIRCLE', 2),
        ("mesh.primitive_uv_sphere_add", "UV Sphere", '', 'MESH_UVSPHERE', 3),
        ("mesh.primitive_ico_sphere_add", "Ico Sphere", '', 'MESH_ICOSPHERE', 4),
        ("mesh.primitive_cylinder_add", "Cylinder", '', 'MESH_CYLINDER', 5),
        ("mesh.primitive_cone_add", "Cone", '', 'MESH_CONE', 6),
        ("mesh.primitive_torus_add", "Torus", '', 'MESH_TORUS', 7)
    ]
    bone_group_enum : EnumProperty(
        name="Choose Bone Group",
        items=mode_options,
        description="Choose bone group"
    )
    


class AnimationPanel(RegisterMixin, Panel ):
    bl_idname = "LEAP_PT_panel"
    bl_label = "Leap"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Leap"

    _classes = (BoneSelectProperty,)

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout 


        col = layout.column()
        for obj in bpy.data.objects:
            layout.label(text=obj.name)
        
        bone_select = bpy.context.scene.BoneSelectProperty
        col.prop(bone_select, "bone_group_enum")
        # for armature in obj:
        #     layout.label(text=obj.name)

