import bpy
import random
from . import globals

data_ops = globals.DATA["operators"]

class UpdateSimulation(bpy.types.Operator):
    bl_idname      = data_ops["update_simulation"]["bl_idname"]
    bl_label       = data_ops["update_simulation"]["bl_label"]
    bl_description = data_ops["update_simulation"]["bl_description"]
    bl_options      = set(data_ops["update_simulation"]["bl_options"])

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        for scene in dict(bpy.data.scenes).values():
            dict(scene.collection.all_objects)['Liquid Domain'].modifiers["Fluid"].domain_settings.use_adaptive_timesteps = False
            dict(scene.collection.all_objects)['Liquid Domain'].modifiers["Fluid"].domain_settings.use_adaptive_timesteps = True

        return {'FINISHED'}

OPERATORS = [
    UpdateSimulation,
]