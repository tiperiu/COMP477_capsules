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