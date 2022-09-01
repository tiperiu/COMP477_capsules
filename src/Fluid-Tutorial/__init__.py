bl_info = {
    "name": "Rigid Body Simulation - Tutorial",
    "author": "Nasir Khalid",
    "version": (2021, 8, 20),
    "blender": (3, 2, 0),
    "location": "Viewport > Right panel",
    "description": "A panel that renders markdown",
    "category": "Generic"
}


def register():
    import bpy
    from . import (
        ui,
        operators,
        properties
    )

    properties.define_props()

    for ui_class in ui.UI_CLASSES:
        bpy.utils.register_class(ui_class)

    for operator in operators.OPERATORS:
        bpy.utils.register_class(operator)

def unregister():
    import bpy
    from . import (
        ui,
        operators,
        properties
    )

    properties.destroy_props()

    for operator in reversed(operators.OPERATORS):
        bpy.utils.unregister_class(operator)

    for ui_class in reversed(ui.UI_CLASSES):
        bpy.utils.unregister_class(ui_class)