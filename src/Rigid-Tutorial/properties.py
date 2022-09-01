import bpy
from . import globals

data = globals.DATA["operators"]

def define_props():
    # Store properties under WindowManager (not Scene) so that they are not saved
    # in .blend files and always show default values after loading
    for key in data:
        setattr(bpy.types.WindowManager, key, bpy.props.BoolProperty(default=False))

def destroy_props():

    for key in data:
        delattr(bpy.types.WindowManager, key)