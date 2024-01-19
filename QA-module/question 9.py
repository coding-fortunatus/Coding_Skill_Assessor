"""
Write a Python program to open a file in read-only mode and print its contents using with statements
"""

# Specify the file name
file_name = "example.txt"

# Open the file in read-only mode using with statement
with open(file_name, "r") as file:
    # Read and print the contents of the file
    contents = file.read()
    print(f"Contents of the file '{file_name}':")
    print(contents)
