"""A context manager in Python is a way of using resources 
that automatically ensures that a file is properly closed, 
regardless of whether an error occurred or not. 
This makes the code not only more readable, but also safer."""

# EXAMPLE 1
with open("example.txt", "w") as fh:
    # Performing file operations
    fh.write("Some data")
# The file will automatically close after exiting the with block

# EXAMPLE 2
with open("example.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("example.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines) #['first line', 'second line', 'third line']
