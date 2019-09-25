# context.area: VIEW_3D
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
    "name" : "Leap Motion",
    "author" : "Dan Amador",
    "description": "Communicate with an external Unity process and share Leap Motion hand data",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Animation"
}


import bpy



import bpy
from bpy.app.handlers import persistent
from bpy.props import BoolProperty, EnumProperty, IntProperty, PointerProperty, StringProperty
from bpy.types import AddonPreferences

from .settings import *
from .webserver_operators import *
import communicator


classes = (WebSocketServerSettings, Start, Stop)

def register():
    from bpy.utils import register_class
    for c in classes:
        register_class(c)
    
    
    addon_prefs = bpy.context.user_preferences.addons["leapSettings"].preferences
    if bool(addon_prefs.auto_start):
        print("hi")
        communicator.start_server(str(addon_prefs.host), int(addon_prefs.port))

def unregister():
    communicator.stop_server()

    from bpy.utils import unregister_class
    for c in reversed(classes):
        unregister_class(c)
    


if __name__ == "__main__":
    register()