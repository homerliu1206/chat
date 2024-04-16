## Chat File Converter
This script is designed to convert chat records from a specific format into a more standardized format. It includes functions to read a file, convert the format, and write the converted data back to a file.

### Features
Read File: The script reads a text file containing chat records.
Convert Format: It converts the format of the chat records, ensuring each message is prefixed with the corresponding person's name.
Write File: The converted chat records are then written back to a file.

### Usage
Input File: Place the chat records in a text file named input.txt. Ensure the file is encoded in UTF-8 format.
Run Script: Execute the chat.py script using a Python interpreter.
Output File: The converted chat records will be written to a file named output.txt.

### Format Conversion
The script assumes that chat records alternate between two participants named "Allen" and "Tom".
Each participant's name is used as a prefix for their corresponding messages in the converted format.

### Example
`Input (input.txt)`\
Allen\
Hi Tom, how are you?\
Tom\
I'm good, thanks!

`Output (output.txt)`\
Allen:Hi Tom, how are you?\
Tom:I'm good, thanks!
