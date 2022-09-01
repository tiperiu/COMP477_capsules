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
            "Text": "The following file will guide you through inverse kinematics on a pre-rigged mesh on Blender - enjoy!",
            "Icon": "NONE"
        },
        {
            "Type": "Header",
            "Text": "Forward Kinematics",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "The current scene has a demo model that is prerigged - the texture and mesh should be lightly visible and under it you will see 'bones' that are rigged in conjuction with the character",
            "Icon": "NONE"
        },   
        {
            "Type": "Paragraph",
            "Text": "Click on the bones under the mesh to select them and then click on 'Object Mode' from the top left dropdown and switch to 'Pose Mode' - here you should be able to click on any bone and then move (press G on your keyboard) or scale it around - the current setup of the rig only allows for forward kinematics",
            "Icon": "NONE"
        }, 
        {
            "Type": "Header",
            "Text": "Inverse Kinematics",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "Start by selecting the tiny bone in the neck of the character and then on the panel on the right side of Blender with all the colorful icons select the one that has meat and bone icon (in blue)",
            "Icon": "NONE"
        }, 
        {
            "Type": "Paragraph",
            "Text": "",
            "Icon": "CONSTRAINT_BONE"
        }, 
        {
            "Type": "Paragraph",
            "Text": "Click on 'Add Bone Constraint' and select 'Inverse Kinematics' - with the same bone selected press G on your keyboard and move your mouse around. The figure should go wild as the bone is chained all the way down to the bottom of spine bone",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "From the Inverse Kinematics settings look for 'Chain Length' and set this value to 2 - try moving the joint again by pressing 'G' on your keyboard",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "Apply similar Inverse Kinematic constraints to the bone in the forearm and heel of the leg - edit the chain length and see what works best",
            "Icon": "NONE"
        },

        
    ],
    "operators": {
    }
}

data_ops = DATA["operators"]

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
]

for ui_class in UI_CLASSES:
    bpy.utils.register_class(ui_class)

for operator in OPERATORS:
    bpy.utils.register_class(operator)