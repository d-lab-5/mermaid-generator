# Requires the local mermaid client npm install -g @mermaid-js/mermaid-cli

# DLAB5
# This program is a simple tool to convert text files into diagrams using the mermaid syntax. It requires the installation of the mermaid command-line interface (mmdc) from npm. The program prompts the user for the input file name, the output file type, and the theme choice. It then creates a temporary file with the mermaid syntax and runs mmdc to generate the output file. The program prints a message when the output file is created and deletes the temporary file.

import os

try:
    test = os.popen('mmdc -V').read()
    print("Good news, mmdc version " + test.rstrip('\n') + " is installed! \n" )
except:
    print("mmdc is not installed or not in the system's PATH.")
    print("Please install mmdc by running 'npm install -g @mermaid-js/mermaid-cli'")

# Prompt for input file name
input_file = input("Enter the input file name: ")

# Prompt for the output file type
output_file_type_choice = input("Enter the output file type 0=svg, 1=png, 2=pdf)")
output_file_types = ["svg", "png", "pdf"]
output_file_type = output_file_types[int(output_file_type_choice)]

# Prompt for the theme choice
theme_choice = input("Enter the theme choice (0=default, 1=forest, 2=dark, 3=neutral): ")
themes = ["default", "forest", "dark", "neutral"]
theme = themes[int(theme_choice)]

# Write input file to temp mmd file adding the string " ;" at the end of each line
with open(input_file, 'r') as f:
    lines = f.readlines()

line_count = 1
with open('temp.mmd', 'w') as f:
    for line in lines:
        if line_count < 2:
            diagram_type = line.rstrip('\n')
            print("Diagram type = " + diagram_type)
        if 'mindmap' in diagram_type:
            f.write(line)
        else:
            f.write(line.rstrip('\n') + ';\n')
        line_count = line_count + 1

# Run mmdc to create the output file based on the chosen file type
output_file = os.path.splitext(input_file)[0] + '.' + output_file_type
# subprocess.run(['mmdc', '-i', 'temp.mmd', '-o', output_file, '-t', theme])
os.system("mmdc -i temp.mmd -o " + output_file + " -t " + theme)

print(f"Output file {output_file} has been created.")

Delete temp.mmd after successful image creation
os.remove('temp.mmd')
print("Temporary file temp.mmd has been deleted.")
