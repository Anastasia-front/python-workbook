"""So far, we have considered only work with text files in UTF-8 encoding. 
This is the default file mode. If you need to work with other than text files,
you can specify the file opening mode as b, abbreviated from bytes. 
In this mode, you will receive a file object for working with the file in byte-string mode.
"""

folder_path = "example"
with open(f"{folder_path}/raw_data.bin", "wb") as fh:
    fh.write(b"Hello world!")

"""
To work with sequences of bytes, Python has built-in byte-string data types

bytes - immutable type used to represent bytes.
bytearray is a variable type that allows you to modify bytes after they are created.

The use of byte data is quite common. For example, byte strings are 
important for working with network protocols (such as TCP/IP), 
serial ports, telnet, and other protocols where data is transferred as a stream of bytes.

In essence, byte strings, or simply bytes, are ordinary strings,
 but strictly one byte is used to write one character. 
 This is different from regular strings, where characters 
 (especially in Unicode) can take up more than one byte."""

bit = '(short for "binary digit") is the basic unit of information \
in computing and digital communication. A bit can have one of two values: \
 0 or 1. You can think of a bit as answering a simple yes/no or off/on question.'

byte = "is a sequence of 8 bits, which is a standard unit \
of measurement for the amount of information in computers. One byte \
can represent 256 different states. 00000000 to 11111111 in binary or \
0 to 255 in decimal, allowing you to encode a wide range of information, \
such as text symbols, parts of images or sound."

print("~" * 30)
s = b"Hello!"
print(s[1])  # Output: 101 (this is the ASCII code of the character 'e')
# it returns a number, in our example 101. This is the ASCII code for the character 'e'.
print("~" * 30)

ASCII = "(American Standard Code for Information Interchange) \
is a character code table used to represent text in computers, \
communication equipment, and other devices that work with text. \
Each character in the ASCII table corresponds to a specific number."


"""ASCII defines 128 characters, including Latin letters, numbers, 
punctuation marks, and control characters. Each character is encoded 
as a 7-bit number, allowing numbers from 0 to 127 to be represented. 
There is also extended ASCII, which uses 8-bit encoding to represent 
256 characters (0 to 255). This extension includes additional 
characters such as Latin letters with diacritics, graphic symbols, etc."""

# Let's create the following byte string:
byte_string = b"Hello world!"
print(byte_string)
print("~" * 30)


# The second way to create byte strings is to convert to a byte string.

"""To convert a string into a byte string, 
you can use the encode string method. 
When you use .encode(), you convert a string to a byte sequence. 
The .encode() method is important because it allows you 
to standardize a string for operations that require 
the same representation of characters regardless of system or platform.
"""

byte_str = "some text".encode()
print(byte_str)
print("~" * 30)


# The sequence of bytes b'some text' will be written in byte_str.

syntax = 'str.encode(encoding="utf-8", errors="strict")'

encoding = 'specifies the encoding method. The default is "utf-8", \
    which supports a large number of characters from different languages.'
errors = "specifies how to handle encoding errors. For example, \
    'strict' to throw an exception on error, 'ignore' to ignore errors, \
        or 'replace' to replace unencodeable characters with a specific substitute (?)."


# Convert numbers to byte strings
"""In Python, you can convert numbers to 
byte strings using the built-in bytes function. 
This is useful for working with binary data, 
especially when you need to store or transfer 
numeric values in a format optimized for low-level processing.
"""


"""One byte holds a number from 0 to 255 inclusive, 
so you can convert a sequence of numbers from 0 to 255
 into a byte string using the bytes function:
"""

# Convert a list of numbers to a byte string
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # b'\x00\x80\xff'
print("~" * 30)

"""In this example, the numbers 0 to 255 are converted to the corresponding bytes. 
Since each number in the range 0 to 255 occupies exactly one byte, 
they are directly converted to a byte string. To output bytes, 
it is most convenient to use hexadecimal notation, in which two characters 
are enough to write numbers from 0 to 255. 
This is the notation Python uses "by default" for bytes."""

# the hexadecimal form of the record
for num in [127, 255, 156]:
    print(hex(num))  # 0x7f
    # 0xff
    # 0x9c
print("~" * 30)
