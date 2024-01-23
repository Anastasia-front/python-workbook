"""A file object is a system resource accessed by the operating system. 
 An object of a regular file can be opened (get/created),
 closed (notify the system that work with it is finished), 
 you can write something to it and read something."""

# open() method
open = 'open(file, mode="r", buffering=-1, encoding=None, \
errors=None, newline=None, closefd=True, opener=None)'

'''Parameters:

file - the path to the file in the form of a string. 
This can be a full path or a path relative to the current execution directory.

mode (optional) - the mode in which the file will be opened. Here are the main modes we will use:
'r' - read (default). The file must exist.
'w' is a record. Creates a new file or overwrites an existing one.
'a' - addition. Appends to the end of the file without overwriting it.
'b' - binary mode (can be used with others such as 'rb' or 'wb').
'+' - update (reading and writing).

buffering (optional) - specifies buffering: 0 for disabled, 
1 for enabled string buffering, more than 1 to specify the size of the buffer in bytes.

encoding (optional) - the name of the encoding that will be used to encode or decode the file.

errors (optional) - specifies how to handle encoding errors.

newline (optional) - controls how newlines are handled.

closefd (optional) - must be True (default); if set to False, the file handle will not be closed.

opener (optional) - defines a special function for opening the file.'''

# SIMPLE EXAMPLE -  write() open the file for writing or create a new one if it doesn't exist or overwrite the file, you can specify the w mode value
fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written) # 6
fh.close()

# SECOND EXAMPLE - read()
fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()

# MORE COMPLICATED EXAMPLE
fh = open('test.txt', 'w')
fh.write('bye')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol) #b
                  #y
                  #e

fh.close()

# readline() method
fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line) #first line

                #second line

                #third line

fh.close()


# readlines() method
fh = open("test.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines) #['first line', 'second line', 'third line']

fh.close()

# tell() method
fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()