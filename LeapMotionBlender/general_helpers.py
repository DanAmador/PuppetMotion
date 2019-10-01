from bpy.props import PointerProperty
from bpy.types import PropertyGroup, Scene

def register_with_extras(classes):
    from bpy.utils import register_class
    for c in classes:
        register_class(c)
        try:
            c._register_extra()
        except AttributeError:
            print(f"{c.__name__} doesn't register any classes")
            continue

def unregister_with_extras(classes):
    from bpy.utils import unregister_class
    for c in reversed(classes):
        try:
            c._unregister_extra()
        except AttributeError:
            continue
        finally:
            unregister_class(c)

class RegisterMixin:
    @classmethod
    def _register_extra(cls):
        if(issubclass(cls, PropertyGroup)):
            setattr(Scene, cls.__name__, PointerProperty(type=cls))
            
        classes = getattr(cls, "_classes")
        register_with_extras(classes)


    @classmethod
    def _unregister_extra(cls):
        if(issubclass(cls, PropertyGroup)):
            obj = getattr(Scene, cls)
            del obj

        classes = getattr(cls, "_classes")
        unregister_with_extras(classes)
