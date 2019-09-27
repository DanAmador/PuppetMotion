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
    "name" : "Leap Motion Integration",
    "author" : "Dan Amador",
    "description": "Communicate with an external Unity process and share Leap Motion hand data",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Animation"
}

def install_pip():
    """Bootstrap pip and any dependencies into Blender's Python configuration"""
    try:
        import pip
        print(pip.__version__)
    except ImportError:
        print("pip python package not found. Installing.")
        try:
            import ensurepip
            ensurepip.bootstrap(upgrade=True, default_pip=True)
        except ImportError:
            print("pip cannot be configured or installed. ")
    finally:
        packages = ("python-socketio", "aiohttp[speedups]")

        for package in packages:
            pip._internal.main(["install", package])


import bpy



import bpy
from bpy.app.handlers import persistent
from bpy.props import BoolProperty, EnumProperty, IntProperty, PointerProperty, StringProperty
from bpy.types import AddonPreferences


# install_pip()
from . import communicator

from .addon_settings import *
from .webserver_operators import *


classes = (WebSocketServerSettings, Start)

def register():
    from bpy.utils import register_class
    for c in classes:
        register_class(c)
    
    bpy.app.handlers.frame_change_post.append(communicator.handle_messages)

    pref = context.preferences.addons[__package__].preferences
    if pref.auto_start:
        communicator.search_and_start(pref.host, pref.port)
    # communicator.start_server()
    
def unregister():
    # communicator.stop_server()

    from bpy.utils import unregister_class
    for c in reversed(classes):
        unregister_class(c)


if __name__ == "__main__":
    register()