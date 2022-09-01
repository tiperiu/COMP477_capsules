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
            "Text": "The following file will guide you through installing the SMPL-X blender addon and using it to generate parametrized models - enjoy!",
            "Icon": "NONE"
        },
        {
            "Type": "Header",
            "Text": "SMPL-X",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "Using SMPL-X in Blender requires the installation of an addon - to do this first visit https://smpl-x.is.tue.mpg.de/download.php",
            "Icon": "NONE"
        },   
        {
            "Type": "Paragraph",
            "Text": "You will need to register for their account and once logged in navigate to the Downloads section and scroll down to SMPL-X Blender Add-on - donwload the 10 shape components addon and do not unzip the file",
            "Icon": "NONE"
        }, 
        {
            "Type": "Paragraph",
            "Text": "Now in Blender click on Edit > Preferences from the top left corner next to File, Render. In the perferences click on 'Add-On' and then click on 'Install - select the .zip file you just downloaded and click 'Install Add-On'. Type 'smpl-x' in the little search bar under the 'Refresh' button and tick the box to enable the add-on",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "Next to this Tutorial panel you will now see a SMPL-X panel - click on it and now you can add figures, edit the height/weight and set 'Measurements to Shape'. Click on the mesh and switch to 'Pose Mode' instead of 'Object Mode' here you can rotate and reposition each individual joint",
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