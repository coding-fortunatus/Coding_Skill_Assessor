"""
Write a python program that create a text document and fill it with contents and print the contents of the file without using with statement.
"""

# Open the file in write mode
file = open("example.txt", "w")

# Write content to the file
file.write("Hello, this is some content in the file.\n")
file.write("This is the second line of the file.\n")
file.write("And here is the third line.\n")

# Close the file
file.close()

# Open the file in read mode
file = open("example.txt", "r")

# Read and print the contents of the file
contents = file.read()
print("File Contents:")
print(contents)

# Close the file
file.close()
