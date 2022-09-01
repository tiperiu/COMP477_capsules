import bpy
from . import globals

data_ops = globals.DATA["operators"]

class AddMonkey(bpy.types.Operator):
    bl_idname      = data_ops["add_monkey"]["bl_idname"]
    bl_label       = data_ops["add_monkey"]["bl_label"]
    bl_description = data_ops["add_monkey"]["bl_description"]
    bl_options      = set(data_ops["add_monkey"]["bl_options"])

    @classmethod
    def poll(cls, context):
        try:
            # Enable button only if in Object Mode
            if (context.active_object is None) or (context.active_object.mode == 'OBJECT'):
                for scene in dict(bpy.data.scenes).values():
                    for ob_name in dict(scene.collection.all_objects):
                        if ob_name == 'Monkey_Mesh':
                            return False
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def execute(self, context):

        bpy.ops.mesh.primitive_monkey_add(
            size=1,
            enter_editmode=False,
            align='WORLD'
        )

        bpy.context.object.scale[0] = 1.6
        bpy.context.object.scale[1] = 1.6
        bpy.context.object.scale[2] = 1.6

        ob = bpy.context.active_object
        mat = bpy.data.materials.new(name="Base_Material_Monkey")
        mat.diffuse_color = [0., 0., 0., 1.0]
        ob.data.materials.append(mat)

        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 1
        bpy.context.object.modifiers["Subdivision"].render_levels = 1

        bpy.ops.object.modifier_apply(modifier="Subdivision")

        bpy.ops.object.modifier_add(type='COLLISION')

        bpy.context.active_object.name = 'Monkey_Mesh'

        return {'FINISHED'}

class AddCloth(bpy.types.Operator):
    bl_idname      = data_ops["add_cloth"]["bl_idname"]
    bl_label       = data_ops["add_cloth"]["bl_label"]
    bl_description = data_ops["add_cloth"]["bl_description"]
    bl_options      = set(data_ops["add_cloth"]["bl_options"])

    @classmethod
    def poll(cls, context):
        try:
            # Enable button only if in Object Mode
            if (context.active_object is None) or (context.active_object.mode == 'OBJECT'):
                for scene in dict(bpy.data.scenes).values():
                    for ob_name in dict(scene.collection.all_objects):
                        if ob_name == 'Cloth':
                            return False
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def execute(self, context):

        bpy.ops.mesh.primitive_plane_add(
            size=1,
            enter_editmode=False,
            align='WORLD'
        )  

        ob = bpy.context.active_object
        mat = bpy.data.materials.new(name="Base_Material_Cloth")
        mat.diffuse_color = [1., 0., 0., 0.5]
        ob.data.materials.append(mat)

        bpy.context.object.location[2] = 2.0

        bpy.context.object.scale[0] = 2.0
        bpy.context.object.scale[1] = 2.0
        bpy.context.object.scale[2] = 2.0

        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].subdivision_type = 'SIMPLE'
        bpy.context.object.modifiers["Subdivision"].levels = 5
        bpy.context.object.modifiers["Subdivision"].render_levels = 5

        bpy.ops.object.modifier_apply(modifier="Subdivision")

        bpy.ops.object.modifier_add(type='CLOTH')

        bpy.context.active_object.name = 'Cloth'

        return {'FINISHED'}

class RemAll(bpy.types.Operator):
    bl_idname      = data_ops["rem_all"]["bl_idname"]
    bl_label       = data_ops["rem_all"]["bl_label"]
    bl_description = data_ops["rem_all"]["bl_description"]
    bl_options      = set(data_ops["rem_all"]["bl_options"])

    @classmethod
    def poll(cls, context):
        try:
            # Enable button only if in Object Mode
            if (context.active_object is not None) or (context.active_object.mode == 'OBJECT'):
                for scene in dict(bpy.data.scenes).values():
                    if len(list(dict(scene.collection.all_objects))) > 0:
                        return True
                return False
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def deleteAllObjects(self):
        """
        https://blender.stackexchange.com/questions/192871/how-to-delete-all-objects-cameras-meshes-etc-using-python-scripting
        
        Deletes all objects in the current scene
        """
        deleteListObjects = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'HAIR', 'POINTCLOUD', 'VOLUME', 'GPENCIL',
                        'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'LIGHT_PROBE', 'CAMERA', 'SPEAKER']

        # Select all objects in the scene to be deleted:

        for o in bpy.context.scene.objects:
            for i in deleteListObjects:
                if o.type == i:
                    o.select_set(False)
                else:
                    o.select_set(True)
        # Deletes all selected objects in the scene:

        bpy.ops.object.delete() 
        
    def execute(self, context):

        self.deleteAllObjects()

        bpy.context.scene.frame_set(0)

        return {'FINISHED'}

class AddFlag(bpy.types.Operator):
    bl_idname      = data_ops["add_flag"]["bl_idname"]
    bl_label       = data_ops["add_flag"]["bl_label"]
    bl_description = data_ops["add_flag"]["bl_description"]
    bl_options      = set(data_ops["add_flag"]["bl_options"])

    @classmethod
    def poll(cls, context):
        try:
            # Enable button only if in Object Mode
            if (context.active_object is None) or (context.active_object.mode == 'OBJECT'):
                for scene in dict(bpy.data.scenes).values():
                    for ob_name in dict(scene.collection.all_objects):
                        if ob_name == 'Flag':
                            return False
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def execute(self, context):

        bpy.ops.mesh.primitive_plane_add(
            size=1,
            enter_editmode=False,
            align='WORLD'
        )  

        ob = bpy.context.active_object
        mat = bpy.data.materials.new(name="Base_Material_Cloth")
        mat.diffuse_color = [0., 1., 0., 0.5]
        ob.data.materials.append(mat)

        bpy.context.object.location[2] = 2.0

        bpy.context.object.scale[0] = 2.0
        bpy.context.object.scale[1] = 2.0
        bpy.context.object.scale[2] = 2.0

        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].subdivision_type = 'SIMPLE'
        bpy.context.object.modifiers["Subdivision"].levels = 5
        bpy.context.object.modifiers["Subdivision"].render_levels = 5

        bpy.ops.object.modifier_apply(modifier="Subdivision")

        bpy.ops.object.modifier_add(type='CLOTH')

        bpy.context.active_object.name = 'Flag'

        return {'FINISHED'}

OPERATORS = [
    AddMonkey,
    AddCloth,
    AddFlag,
    RemAll
]