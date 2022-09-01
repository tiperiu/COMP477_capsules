import bpy
import random
from . import globals

data_ops = globals.DATA["operators"]

class AddBowl(bpy.types.Operator):
    bl_idname      = data_ops["add_bowl"]["bl_idname"]
    bl_label       = data_ops["add_bowl"]["bl_label"]
    bl_description = data_ops["add_bowl"]["bl_description"]
    bl_options      = set(data_ops["add_bowl"]["bl_options"])

    @classmethod
    def poll(cls, context):
        try:
            # Enable button only if in Object Mode
            if (context.active_object is None) or (context.active_object.mode == 'OBJECT'):
                for scene in dict(bpy.data.scenes).values():
                    for ob_name in dict(scene.collection.all_objects):
                        if ob_name == 'Bowl':
                            return False
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def execute(self, context):

        bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

        bpy.context.object.scale[0] = 2.2
        bpy.context.object.scale[1] = 2.2
        bpy.context.object.scale[2] = 2.2

        bpy.context.active_object.name = 'Bowl'

        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')

        bpy.ops.object.mode_set(mode="OBJECT")
        
        for vertex in bpy.context.object.data.vertices:
            vertex.select = False

        for vertex in bpy.context.object.data.vertices:
            if vertex.co[2] > 0:
                vertex.select = True
            else:
                vertex.select = False

        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.object.mode_set(mode="OBJECT")

        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.type = 'PASSIVE'
        bpy.context.object.rigid_body.collision_shape = 'MESH'

        ob = bpy.context.active_object
        mat = bpy.data.materials.new(name="Base_Material_Bowl")
        mat.diffuse_color = [0.6, 0.2, 0.7, 1.0]
        ob.data.materials.append(mat)

        return {'FINISHED'}

class AddCubes(bpy.types.Operator):
    bl_idname      = data_ops["add_cubes"]["bl_idname"]
    bl_label       = data_ops["add_cubes"]["bl_label"]
    bl_description = data_ops["add_cubes"]["bl_description"]
    bl_options      = set(data_ops["add_cubes"]["bl_options"])

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        for i in range(10):
            bpy.ops.mesh.primitive_cube_add(
                enter_editmode=False,
                align='WORLD',
                location=(
                    ((random.random() - 0.5) * 3),
                    ((random.random() - 0.5) * 3),
                    random.random() * 6, # drop from higher up
                ),
                scale=(
                    random.random() * 0.4,
                    random.random() * 0.4,
                    random.random() * 0.6
                )
            )

            bpy.context.active_object.name = 'Cube'

            bpy.ops.rigidbody.object_add()

            ob = bpy.context.active_object
            mat = bpy.data.materials.new(name="Base_Material_Bowl")
            mat.diffuse_color = [random.random(), random.random(), random.random(), 1.0]
            ob.data.materials.append(mat)

        return {'FINISHED'}

class AddScene(bpy.types.Operator):
    bl_idname      = data_ops["create_scene"]["bl_idname"]
    bl_label       = data_ops["create_scene"]["bl_label"]
    bl_description = data_ops["create_scene"]["bl_description"]
    bl_options      = set(data_ops["create_scene"]["bl_options"])

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.type = 'PASSIVE'
        bpy.context.object.rigid_body.collision_shape = 'MESH'

        ob = bpy.context.active_object
        mat = bpy.data.materials.new(name="Base_Material_Bowl")
        mat.diffuse_color = [0.4, 0.2, 0.7, 1.0]
        ob.data.materials.append(mat)

        LIM = 4.

        MIN = -4
        MAX =  4

        ESCALE = LIM / (MAX*12)

        for x in range(MIN, MAX, 1):
            for y in range(MIN, MAX, 1):
                for z in range(MAX):

                    bpy.ops.mesh.primitive_cube_add(
                        enter_editmode=False,
                        align='WORLD',
                        location=(
                            x / LIM,
                            y / LIM,
                            (z / LIM) + ESCALE,
                        ),
                        scale=(
                            ESCALE,
                            ESCALE,
                            ESCALE,
                        )
                    )

                    bpy.context.active_object.name = 'Cube'

                    bpy.ops.rigidbody.object_add()

                    ob = bpy.context.active_object
                    mat = bpy.data.materials.new(name="Base_Material_Bowl")
                    mat.diffuse_color = [random.random(), random.random(), random.random(), 1.0]
                    ob.data.materials.append(mat)

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

OPERATORS = [
    RemAll,
    AddBowl,
    AddCubes,
    AddScene,
]