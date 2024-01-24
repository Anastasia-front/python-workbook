"""A context manager in Python is a way of using resources 
that automatically ensures that a file is properly closed, 
regardless of whether an error occurred or not. 
This makes the code not only more readable, but also safer."""


folder_path = "example"
file_path = f"{folder_path}/example.txt"
# EXAMPLE 1
with open(file_path, "w") as file:
    file.write("This is some content for the file.")
# The file will automatically close after exiting the with block

# EXAMPLE 2
with open(file_path, "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open(file_path, "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines) #['first line', 'second line', 'third line']
