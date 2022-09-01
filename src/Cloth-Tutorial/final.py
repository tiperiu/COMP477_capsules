## CLICK PLAY TO RUN THIS --------------^
## SCRIPT BEFORE STARTING

## ONCE CLICKED A NEW
## PANEL WILL APPEAR

import bpy

DATA = {
    "data": [
        {
            "Type": "Header",
            "Text": "Intro",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "The following file will guide you through Cloth Simulation in Blender. Each section has a 'Manual Guide' that you should try to follow but if for some reason you are unable to you may click on the relevant buttons instead",
            "Icon": "NONE"
        },
        {
            "Type": "Header",
            "Text": "Simple Cloth",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "Lets start by doing a simple cloth drop simulation. We will add a monkey mesh and drop a cloth represented by a plane mesh on top of it",
            "Icon": "NONE"
        },
        {
            "Type": "Operator",
            "Text": "Add Monkey",
            "ID": "scene.add_monkey",
            "Details": [
                {
                    "Type": "Paragraph",
                    "Text": "To add the monkey manually first click on Add > Mesh > Monkey",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Then increase the number of vertices on the monkey so it has more points for calculations. To do this first click on the object then click on the following blue icon",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "MODIFIER_ON"
                },
                {
                    "Type": "Paragraph",
                    "Text": " from the bottom right panel. From the dropdown 'Add Modifier' select the 'Subdivision Surface'",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Click on the 'Simple' button and set the Levels Viewport and Render to 1. Then press Ctrl+A to apply the process (or click the little down arrow above 'Simple' and click 'Apply')",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Next we add the 'Collision' modifier on the monkey object so the cloth knows to collide with it. To do this click on the monkey shape and then click the following blue icon on the same bottom right panel",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "PHYSICS"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Then click on 'Collision' to enable it, it will also show a bunch of properties that can be adjusted but the defaults should be fine",
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
            "Type": "Operator",
            "Text": "Add Cloth",
            "ID": "scene.add_cloth",
            "Details": [
                {
                    "Type": "Paragraph",
                    "Text": "To add the cloth manually repeat the same steps as for the monkey shape but instead select 'Plane' when adding the mesh; Instead of applying the 'Collision' physics modifier as for the monkey apply the 'Cloth' one instead; Perform the same subdivision but set levels and render to 5",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "The cloth and monkey are on the same plane so shift the plane upwards by dragging the blue arrow up or by increasing the 'Location Z' value from the 'Object Properties. Also set a material color as you like",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "OBJECT_DATA"
                },
            ]
        },
        {
            "Type": "Paragraph",
            "Text": "We can run a simulation now that the meshes are ready and their properties are applied. To do this look for the following icons on the bottom panel that looks like a video playback",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "",
            "Icon": "PLAY"
        },
        {
            "Type": "Paragraph",
            "Text": "Press play to start/stop the simulation - you can drag the playback along or use the other buttons to skip ahead or back. Once done click the following button to go back to the start",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "",
            "Icon": "REW"
        },
        {
            "Type": "Header",
            "Text": "Flag Animation",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "Lets reset the scene and implement a waving flag animation. Click below to remove all objects and set the frame back to zero",
            "Icon": "NONE"
        },
        {
            "Type": "Operator",
            "Text": "Reset Scene",
            "ID": "scene.rem_all",
            "Details": []
        },
        {
            "Type": "Paragraph",
            "Text": "Implementing a flag follows a similar process as the cloth but we introduce three new concepts: Vertex Groups/Pinning, Wind force, self intersection",
            "Icon": "NONE",
        },
        {
                    "Type": "Paragraph",
                    "Text": "Start by adding a plane from Add > Mesh > Plane on the top right. We then need to scale the plane so it looks more like a flag. From the object properties tab on the bottom left panel",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "OBJECT_DATA"
                },
                {
                    "Type": "Paragraph",
                    "Text": "Set the 'Scale Y' to 1.67 and Rotation Y to 90. We then need to subdivide the shape as the cloth before so there are more vertices for cloth simulation. From the modifier tab",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "MODIFIER_ON"
                },
                {
                    "Type": "Paragraph",
                    "Text": "From the dropdown 'Add Modifier' select the 'Subdivision Surface'",
                    "Icon": "NONE"
                },              
                {
                    "Type": "Paragraph",
                    "Text": "Click on the 'Simple' button and set the Levels Viewport and Render to 5. Then press Ctrl+A to apply the process (or click the little down arrow above 'Simple' and click 'Apply')",
                    "Icon": "NONE"
                },  
                {
                    "Type": "Paragraph",
                    "Text": "Click on the same dropdown 'Add Modifier' and this time select 'Cloth'. If you try to play the animation in its current state the entire cloth will fall down. We now introduct the concept of vertex groups and pinning. Start by clicking the 'Object Data Properties' tab",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "MESH_DATA"
                },
                {
                    "Type": "Paragraph",
                    "Text": "On the right panel under 'Vertex Groups' click on the + button on the right of it. It will add a new group called 'Group' - double click on the 'Group' and renamed it to 'Flag Pin'. We now switch to 'Edit Mode' from the top left of Blender under 'File' and 'Edit' it says 'Object Mode', click the dropdown and select 'Edit Mode'. You can now select individual vertices, drag and select all the vertices on one end side of the flag (these will be pinned)",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "The selected vertices will glow yellow, with the vertices selected click on 'Assign' button in the 'Vertex Groups' tab - this will set the selected vertices in the group. Switch back to 'Object Mode' by using the dropdown from the top left. Now click on the 'Physics Properties' tab from the bottom right",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "PHYSICS"
                },
                {
                    "Type": "Paragraph",
                    "Text": "In the physics tab scroll down until you see the 'Shape' dropdown tab click on it and you will see 'Pin Group' click on it and you will see the 'Flag Pin' group, select it",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "If you play the animation now the flag will droop down. To fix this lets add some wind, Click on 'Add' > 'Force Field' > 'Wind'. This will add a 'Wind' object in the scene - from the bottom right tab in the 'Physics' tab set the 'Strength' of the wind to a large number like 1500 - then go to the 'Object Properties' of the wind and change its rotation Y to -90 and rotation Z to 80.",
                    "Icon": "NONE"
                },
                {
                    "Type": "Paragraph",
                    "Text": "",
                    "Icon": "OBJECT_DATA"
                },
                {
                    "Type": "Paragraph",
                    "Text": "You can press play now to watch the flag in action but it might look weird because it self intersects and shading is off - to fix this click on the flag and then right click and select 'Shade Smooth'. Then from the flags 'Physics' tab scroll to 'Collisions' and turn on 'Self Collisions'",
                    "Icon": "NONE"
                },
        {
            "Type": "Header",
            "Text": "Edting Properties",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "From the 'Physics' tab set the vertex mass to 0.1 and a larger value - What happens when you  do so?",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Add some more points to the pin group can you create a different cloth simulation? A pinched table cloth or a wet cloth pinned to dry",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Experiment with the 'Stiffness' and 'Damping' properties such as Tension, Compression and Bending - what are their impact?",
            "Icon": "NONE"
        },
    ],
    "operators": {
        "add_monkey": {
            "bl_idname": "scene.add_monkey",
            "bl_label": "Add Monkey",
            "bl_description": "Adds a Rigid Body monkey to the scene",
            "bl_options": ["REGISTER", "UNDO"]
        },
        "add_cloth": {
            "bl_idname": "scene.add_cloth",
            "bl_label": "Add Cloth",
            "bl_description": "Adds a Cloth plane to the scene",
            "bl_options": ["REGISTER", "UNDO"]
        },
        "rem_all": {
            "bl_idname": "scene.rem_all",
            "bl_label": "Remove All",
            "bl_description": "Deletes all from scene and resets slider",
            "bl_options": ["REGISTER", "UNDO"]
        },
        "add_flag": {
            "bl_idname": "scene.add_flag",
            "bl_label": "Add Flag",
            "bl_description": "Adds a pinned Flag to the scene",
            "bl_options": ["REGISTER", "UNDO"]
        },
    }
}

data_ops = DATA["operators"]

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
    AddMonkey,
    AddCloth,
    AddFlag,
    RemAll
]

for ui_class in UI_CLASSES:
    bpy.utils.register_class(ui_class)

for operator in OPERATORS:
    bpy.utils.register_class(operator)