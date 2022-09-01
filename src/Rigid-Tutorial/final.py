## CLICK PLAY TO RUN THIS --------------^
## SCRIPT BEFORE STARTING

## ONCE CLICKED A NEW
## PANEL WILL APPEAR

import bpy
import random

DATA = {
    "data": [
        {
            "Type": "Header",
            "Text": "Intro",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "The following file will guide you through rigid body simulation in Blender. This will follow a similar layout as the previous tutorial - enjoy!",
            "Icon": "NONE"
        },
        {
            "Type": "Header",
            "Text": "Objects in Bowl",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "Lets create a rigid body simulation where we drop a bunch of objects in to a small bowl and allow for collisions so they interact with each other and the bowl surface",
            "Icon": "NONE"
        },
        {
            "Type": "Operator",
            "Text": "Add Bowl",
            "ID": "scene.add_bowl",
            "Details": [
                {
                    "Type": "Paragraph",
                    "Text": "To create the bowl manually start by adding a UV Sphere in to the scene from Add > Mesh > UV Sphere. Then switch to 'Edit Mode' by clicking on the dropdown on the left of the 'View' tab (it should say 'Object Mode' currently)",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "In 'Edit Mode' you can select individual vertices and deform meshes. Here we are going to select some of the vertices and delete them to create a bowl",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Click and drag to create a box around all the vertices on the upper half of the sphere - with the vertices selected press 'X' on your keyboard and select 'Delete Vertices'. Make sure to delete all vertices on the top half of the sphere (some may remain even as black dots)",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Once the bowl is ready switch back to 'Object Mode' from the top left dropwdown. Now we can convert this shape to a RIGID BODY - Start by clicking on the blue physics properties button on the bottom right panel",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "PHYSICS"
                },
                {
                    "Type": "Paragraph",
                    "Text": "With the bowl selected click on the 'Rigid Body' button - This will enable more options, set the 'Type' to passive (if its active gravity will drop down the object)",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Under the Rigid Body settings scroll to the Collisions and set the 'Shape' to 'Mesh' - this will make the new cut up mesh the interaction shape rather than the original sphere",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Lets apply a material to color the mesh. In order to see materials switch the shading to show materials. For this you will see four sphere icons on the top right of the 3D viewer panel, click on this following sphere",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "SHADING_TEXTURE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Now you should be able to see the white texture. To change this texture click on the materials icon from the bottom right panel it should be red",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "MATERIAL"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Add a new material on the shape by clicking 'New', then a bunch of properties will appear. Dropdown the 'Surface' tab and click on the white 'Base Color' to change it to anything you'd like",
                    "Icon": "NONE"
                }
            ]
        },
        {
            "Type": "Paragraph",
            "Text": "Now lets add a set of rigid body shapes in to the scene that will drop in to the bowl",
            "Icon": "NONE"
        },
        {
            "Type": "Operator",
            "Text": "Add Cubes",
            "ID": "scene.add_cubes",
            "Details": [
                {
                    "Type": "Paragraph",
                    "Text": "We will start by making one Rigid Body cube and then copying it to create a whole set",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Start by adding a cube from Add > Mesh > Cube. With cube selected press 'S' and then move the mouse to scale it down to a very small size and click to set the size",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Now click on the blue Physics button on the bottom right panel",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "PHYSICS"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Set the object by clicking on the 'Rigid Body' button - keep the settings as is" ,
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Now with cube selected press 'Ctrl+C' to copy it and then 'Ctrl+V' to make a clone - move the clone using the red, green and blue arrows (Press G on keyboard or click on Move icon ). Add as many clones as you'd like and change their position, size, rotation too",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "We can now play the animation - click on the play button on the bottom Timeline",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "PLAY"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Drag the timeline around or pless play again to pause the animation",
                    "Icon": "NONE"
                }
            ]
        },
        {
            "Type": "Header",
            "Text": "Interacting in real time",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "For this we will create a scene filled with rigid body ojects and then interact with it in real time. Creating the scene can be tedious so for the demo use the button below to set it up instantly - you can also create your own custom scene if you'd like (Make sure you setup a passive floor and active objects)",
            "Icon": "NONE"
        },
        {
            "Type": "Operator",
            "Text": "Create Scene",
            "ID": "scene.create_scene",
            "Details": [
                {
                    "Type": "Paragraph",
                    "Text": "Creating this scene is straightforward. Start by adding a plane and applying the rigid body modifier to it - also enable the 'Passive' option. Then create a single Rigid Body cube as in the previous section and then duplicate it to create more and position them in the scene",
                    "Icon": "NONE"
                }
            ]
        },
        {
            "Type": "Paragraph",
            "Text": "Now we will add an object and interact with the scene in real time. Start by adding any mesh of your choice from Add > Mesh. Then press 'G' on your keyboard and move the object off the side somewhere. Then apply the rigid body modifier on the object and from the rigid body setting drop down - tick the boxes for 'Dynamic' and 'Animated'",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "You can now play the scene by pressing spacebar and then with your mesh selected press 'G' on your keyboard to move it around - the mesh can now interact with the other rigid bodies in the scene in realtime. This can be used to setup collisions or animations",
            "Icon": "NONE"
        },
        {
            "Type": "Header",
            "Text": "Changing Parameters",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "Revist the setup from the first part of the Tutorial. Under the rigid body settings for the bowl - in the 'Surface Response' section, change the 'Friction' and 'Bounciness' parameters - how does this change the behaviour?",
            "Icon": "NONE"
        },
        
    ],
    "operators": {
        "add_bowl": {
            "bl_idname": "scene.add_bowl",
            "bl_label": "Add Bowl",
            "bl_description": "Adds a Rigid Body bowl to the scene",
            "bl_options": ["REGISTER", "UNDO"]
        },
        "add_cubes": {
            "bl_idname": "scene.add_cubes",
            "bl_label": "Add Cubes",
            "bl_description": "Adds a number of various cubes to the scene",
            "bl_options": ["REGISTER", "UNDO"]
        },
        "rem_all": {
            "bl_idname": "scene.rem_all",
            "bl_label": "Remove All",
            "bl_description": "Remove all objects from scene",
            "bl_options": ["REGISTER", "UNDO"]
        },
        "create_scene": {
            "bl_idname": "scene.create_scene",
            "bl_label": "Add Scene",
            "bl_description": "Adds a scene for rigid body playground",
            "bl_options": ["REGISTER", "UNDO"]
        },
    }
}

data_ops = DATA["operators"]

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

for key in DATA["operators"]:
    setattr(bpy.types.WindowManager, key, bpy.props.BoolProperty(default=False))
    
import textwrap

def header(layout, text, width=50, level=1):
    row = layout.row()
    row.scale_y = 0.5
    row.label(text="."*1000)

    sub_lns = textwrap.fill(text, width)
    spl = sub_lns.split("\n")

    row = layout.row()
    if level == 1:
        row.label(text=sub_lns, icon="KEYTYPE_KEYFRAME_VEC")
    else:
        row.label(text=sub_lns)

    row = layout.row()
    row.scale_y = 0.2
    row.label(text="."*1000)

    row = layout.row()
    row.scale_y = 0.5
    row.label(text="")

def paragraph(layout, text, width=50, icon=None):
    col = layout.column()

    sub_lns = textwrap.fill(text, width)
    spl = sub_lns.split("\n")
    for s in spl:
        row = col.row()
        row.label(text=s, icon=icon if icon is not None else "NONE")

data = DATA["data"]

class TutorialPanel(bpy.types.Panel):
    bl_label = "Tutorial Guide"
    bl_category = "Tutorial"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
      layout = self.layout

      self.width = 50

      for d in  data:

        if d["Type"] == "Header":

          header(layout, d["Text"], self.width, level=d["Level"])

        elif d["Type"] == "Paragraph":

          paragraph(layout, d["Text"], self.width, icon=d["Icon"])

        elif d["Type"] == "Operator":

          column = layout.column()
          column.operator(d["ID"], text=d["Text"])

          if len(d["Details"]) > 0:

            box = column.box()

            box_c = box.row()

            box_c.prop(
              context.window_manager,
              d["ID"].split(".")[1],
              icon='TRIA_DOWN' if getattr(context.window_manager, d["ID"].split(".")[1]) else 'TRIA_RIGHT',
              emboss=True,
              icon_only=True
            )
            box_c.label(text="Manual Guide", icon='HELP')

          if getattr(context.window_manager, d["ID"].split(".")[1]):
            for d_ in d["Details"]:

              paragraph(
                box,
                d_["Text"],
                icon=d_["Icon"]
              )

UI_CLASSES = [
    TutorialPanel
]

OPERATORS = [
    RemAll,
    AddBowl,
    AddCubes,
    AddScene,
]

for ui_class in UI_CLASSES:
    bpy.utils.register_class(ui_class)

for operator in OPERATORS:
    bpy.utils.register_class(operator)