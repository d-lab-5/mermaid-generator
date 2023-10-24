# mermaid-generator
DLAB5 mermaid-generator is a program that allows users to create diagrams from text files using the mermaid syntax. Mermaid is a markdown-like language for generating flowcharts, sequence diagrams, class diagrams, and other types of diagrams. To use this program, users need to install the mermaid command-line interface (mmdc) from npm, which is a package manager for JavaScript. The program works as follows:

- The program asks the user to enter the name of the input text file that contains the mermaid syntax. The input file should have a .txt extension.
- The program asks the user to choose the output file type. The output file can be either a PNG image, a SVG image, or a PDF document. The output file will have the same name as the input file, but with a different extension according to the chosen file type.
- The program asks the user to select a theme for the diagram. The theme determines the color scheme and the style of the diagram. The available themes are default, forest, dark, and neutral.
- The program creates a temporary file with the .mmd extension and copies the content of the input text file to it. The temporary file is needed because mmdc only accepts files with the .mmd extension as input.
- The program runs mmdc with the appropriate arguments to generate the output file from the temporary file. The arguments include the input file name, the output file name, and the theme option.
- The program displays a message indicating that the output file has been created and shows its location.
- The program deletes the temporary file.
