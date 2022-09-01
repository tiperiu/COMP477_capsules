from glob import glob
import bpy

from . import utils
from . import globals

data = globals.DATA["data"]

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

          utils.header(layout, d["Text"], self.width, level=d["Level"])

        elif d["Type"] == "Paragraph":

          utils.paragraph(layout, d["Text"], self.width, icon=d["Icon"])

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

              utils.paragraph(
                box,
                d_["Text"],
                icon=d_["Icon"]
              )

UI_CLASSES = [
    TutorialPanel
]