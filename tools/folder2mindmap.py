import os
from anytree import Node, RenderTree, PreOrderIter

nodes = {}  # Dictionary to store created nodes
node_seperator = "_"


def create_structure(max_mindmap_level):
    """
    This function creates a structure using anytree and returns the root node and its levels.
    """
    # Prompt user for root directory
    root_dir = input("Enter the root directory: ")

    # Setup root node
    root_dir_node = root_dir + node_seperator + str(0)
    nodes[root_dir_node] = Node(root_dir_node, intent=0)

    # Walk through the directory and create nodes for each directory
    for root, dirs, _ in os.walk(root_dir):
        for name in dirs:
            path = os.path.join(root, name).replace(root_dir, '').lstrip('/')
            path_array = path.split("\\")
            indent_level = path.count(os.sep)
            name_node = name + node_seperator + str(indent_level)

            # Set parent node
            if (indent_level - 1) < 1:
                parent_node = nodes[root_dir_node]
                indent_level = 0
            else:
                parent_dir = path_array[indent_level - 1]
                parent_node = nodes[parent_dir + "_" + str(indent_level - 1)]

            # Create new node with parent node
            nodes[name_node] = Node(name_node, parent=parent_node, intent=indent_level)

            # Update max mindmap level if current level is greater
            if max_mindmap_level < indent_level:
                max_mindmap_level = indent_level

    print("Node structure generated")
    print(RenderTree(nodes[root_dir_node]))

    return root_dir_node, max_mindmap_level


def create_mindmap(root_node, levels, output_file):
    """
    This function generates a mindmap from the given root node up to a specified number of levels and writes it to an output file.
    """
    print(f"The {root_node} has {str(levels)} levels")

    # Prompt user for the number of levels to display in the mindmap
    max_mindmap_level = input("Please enter the number of level you'd like to see in the mindmap (Enter means all):")

    # If user doesn't provide any input, set max_mindmap_level to total levels
    if not max_mindmap_level:
        max_mindmap_level = levels

    # Open the output file in write mode
    with open(output_file, 'w') as f:
        print("\n\nmindmap")
        f.write('mindmap\n')
        f.write(f' root(({root_node.split(node_seperator)[0]}))\n')

        # Get the structure of the mindmap up to the max level
        mindmap_structure = [node.name for node in PreOrderIter(nodes[root_node], maxlevel=int(max_mindmap_level))]

        line_count = 1
        for mindmap_node in mindmap_structure:
            if line_count < 2:
                print(f"  root(({root_node.split(node_seperator)[0]}))")
            else:
                # Print and write each node of the mindmap to the output file
                print(f'{"   " * (nodes[mindmap_node].intent + 1)}{mindmap_node.split(node_seperator)[0]}')
                f.write(f'{"   " * (nodes[mindmap_node].intent + 1)}{mindmap_node.split(node_seperator)[0]}\n')

            line_count += 1


# Create structure and get root node and levels
root_node, levels = create_structure(0)

# Create mind map with root node, levels and output file name
create_mindmap(root_node, levels, 'mindmap.mmd')
