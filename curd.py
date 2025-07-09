# Write to a file
with open("example.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
# Append to the file
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

# Read from the file and display contents
with open("example.txt", "r") as file:
    contents = file.read()
    print("File Contents:")
    print(contents)
