# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "LeapMotionBlender",
    "author" : "Dan Amador",
    "description": "Communicate with an external Unity process and share Leap Motion hand data",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Animation"
}

import bpy
from bpy.app.handlers import persistent
from bpy.props import BoolProperty, EnumProperty, IntProperty, PointerProperty, StringProperty
from bpy.types import AddonPreferences


from . import communicator
from .Operators import Start, ForceStart
from .settingsPanel import SettingsPanel

classes = (SettingsPanel, Start, ForceStart)

def register():
    from bpy.utils import register_class
    for c in classes:
        register_class(c)
    
    bpy.app.handlers.frame_change_post.append(communicator.handle_messages)

    pref = bpy.context.preferences.addons[__package__].preferences
    
    if pref.auto_start:
        communicator.start_server(pref.host, pref.port)
    
def unregister():
    from bpy.utils import unregister_class
    for c in reversed(classes):
        unregister_class(c)


if __name__ == "__main__":
    register()