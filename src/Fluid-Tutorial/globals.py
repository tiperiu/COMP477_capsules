DATA = {
    "data": [
        {
            "Type": "Header",
            "Text": "Intro",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "The following file will guide you through fluid simulation in Blender. This will follow a similar layout as the previous tutorial - enjoy!",
            "Icon": "NONE"
        },
        {
            "Type": "Header",
            "Text": "Simple Scene",
            "Level": 1
        },
        {
            "Type": "Paragraph",
            "Text": "Fluid simulations in Blender require a 'Domain' in which to operate, its essentially a box within which the simulation takes place otherwise it will be unbounded. Once a domain is setup you can then add within it a new mesh and give it a fluid type of two main types:",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "Flow object: This can be either inflow (source of fluid), outflow (drain for fluid, if touched water leaves domain) or geometry (fixed volume of water)",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "Effector object: This is an object inside the domain which interacts with the fluid (think of this like rocks interacting with water)",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Blender provides a very quick way to setup a fluid simulation. Start by adding a Suzanne mesh from Add > Mesh > Monkey",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Now press F3 on your keyboard and type in 'Quick Liquid' and select the quick liquid option. This will add a domain around the mesh and apply the 'Fluid' modifier on the Suzanne mesh. By default Blender assigns the 'Geometry' flow to the mesh so once you press play or spacebar you'll see a fixed volume of water simulation. Note that currently the liquid is shown as vertices",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "To get full water mesh start by clicking on the liquid domain cube and then click on the blue",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Physics Properties",
            "Icon": "PHYSICS"
        },

        {
            "Type": "Paragraph",
            "Text": "You will now see a whole list of simulation settings for the domain. Start by enabling 'Mesh' from 'Settings' > 'Liquid' > 'Mesh' and then play the animation again you'll notice that now there is a mesh for the fluid. Switch the shading of the viewport from the top right of the scene the mesh is in to get a cooler view by clicking",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Material Preview Shading",
            "Icon": "SHADING_TEXTURE"
        },

        {
            "Type": "Paragraph",
            "Text": "Note that if the animation plays too slow you can speed it up by decreasing the resolution of the fluid simulation from the same settings panel under 'Settings' > 'Resolution Division'",
            "Icon": "NONE"
        },

        {
            "Type": "Header",
            "Text": "Changing Flow",
            "Level": 1
        },

        {
            "Type": "Paragraph",
            "Text": "So far we have only been changing the domain (cube) settings but now click on the Suzanne mesh and under the same physics properties tab you'll see some different settings. Start by changing the 'Settings' > 'Flow Behaviour' from Geometry to Inflow",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "By default your simulation will not change as Blender only updates the simulation when the domain is updated so to fix this you would need to change a setting in the domain to force a change but instead you can use the button below to do this. Use this everytime you change something in the Suzanne mesh to force rebaking of the fluid simulation",
            "Icon": "NONE"
        },
        {
            "Type": "Operator",
            "Text": "Update Simulation",
            "ID": "scene.update_simulation",
            "Details": []
        },
        {
            "Type": "Paragraph",
            "Text": "After clicking the button above (multiple times maybe) - play the animation and you'll see that the mesh is now a water source rather than a fixed volume",
            "Icon": "NONE"
        },
        {
            "Type": "Paragraph",
            "Text": "Set the type back to 'Geometry' and then enable the 'Intial Velocity' - set either of the X, Y or Z values. Click the Update Simulation button a few times and then rerun the animation",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Now add a cube mesh to the scene from 'Add' > 'Mesh' > 'Cube' then press 'G' and move the cube under the Suzanne mesh - apply the 'Fluid' property to this cube from the blue physics property tab",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Physics Properties",
            "Icon": "PHYSICS"
        },

        {
            "Type": "Paragraph",
            "Text": "After clicking the 'Fluid' button you'll have an option to choose 'Type' - set this to 'Effector'. Click the update simulation button above a few times and then play your animation again using spacebar. The cube should now interact with the fluid in the scene",
            "Icon": "NONE"
        },

        {
            "Type": "Header",
            "Text": "Fluid Settings",
            "Level": 1
        },

        {
            "Type": "Paragraph",
            "Text": "Lets revisit the domain again as this is what controls the properties of the fluid. Click on the domain cube and then go to the physics properties tab",
            "Icon": "NONE"
        },

        {
            "Type": "Paragraph",
            "Text": "Under 'Liquid' > 'Diffusion' (enable diffusion) and here you can change the exponent to change the behvaiour of the fluid. If you click on the bullet list on the right of 'Diffusion' you can select from the preselects of Honey, Oil and Water - how does the exponent and base affect the fluid simulation?",
            "Icon": "NONE"
        },        
    ],
    "operators": {
        "update_simulation": {
            "bl_idname": "scene.update_simulation",
            "bl_label": "Update Simulation",
            "bl_description": "Updates fluid simulation by forcing domain to rebake",
            "bl_options": ["REGISTER", "UNDO"]
        }
    }
}