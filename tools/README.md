# Folder structur to Mermaid Mindmap
This Python script generates a mind map from a given directory structure.

## Functions
`create_structure(max_mindmap_level)`: This function creates a structure using anytree and returns the root node and its levels. It prompts the user for a root directory and walks through it to create nodes for each directory.

`create_mindmap(root_node, levels, output_file)`: This function generates a mind map from the given root node up to a specified number of levels and writes it to an output file. It prompts the user for the number of levels they’d like to see in the mind map.

## Usage
1. Run the script.
1. When prompted, enter your desired root directory.
1. When prompted again, enter the number of levels you’d like to see in the mind map. If you want to see all levels, just press Enter.
1. The script will generate a mind map and write it to `mindmap.mmd`.
## Output
The output is a text file (`mindmap.mmd`) containing the generated mind map.
Pleas use `mermaid-generator.py` with input file `tools\mindmap.mmd` to gererate the diagram.
Alternatively, you can use [mermaid.live](https://mermaid.live/edit#pako:eNpdUstu20AM_BViTzbgOJZsRw8UBZK2twYJmuRS6LKRKGlRidzuI6hi-N-7lqw0DU_kzJAccPcgSq5Q5KJXVPVSFwRgmN1icQaWyxMEcGdUo8hOBcB3pgZaZR2bYcbyXJVMi1pCLS-emX8tZ-aete-kUVY6xTSjADdGOWVb0BMP2g5lyx03A0jvWjbwyDTAjX-V564faFGasp1n3BFgXWPp1AuhtZ-ezeVnSRXUKJ03aN_prr3jPhgooTT4wciT_Sed4suoeUFwWLakfvuPggdnpMMmjNOdJFLU_M9fm8b3SA7CEfUb-8jcvQ26R4KTWS01mhm8RdNLVYmV6M9ZLg4nshCuxR4LkYe0wlr6zhWioGOQel0FM98qFd5D5M54XIlwQX4YqJzrSfNVycbIfga1JJEfxB-RR2m8TqOrdJvsst12E21XYhD5RbxOsl2U7LMoSeN4l-6vjivxyhwmbNbZFEm2j_dZugktOFq4nf7U-LXGHT_HhtPK418SjsJs)
