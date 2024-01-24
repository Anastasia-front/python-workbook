# (ASCII, UTF-8, CP1251/Windows1251)

"""To find out which element in UTF-8 a character 
corresponds to, there is a function ord (from order)."""


# For example, the character 'a' is coded as 97:
ord("a")  # 97


"""The reverse operation, when you need to find out 
    which character is encoded by a number, for example 100, 
        is the chr function (abbreviated from character):"""

chr(128)  # 'd'


# Python can work with a very large number of different encodings

s = "Nature"
print("~" * 30)
utf8 = s.encode()
print(f"UTF-8: {utf8}")

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)
print("~" * 30)
# Output
# UTF-8: b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82!'
# UTF-16: b'\xff\xfe\x1f\x04@\x048\x042\x04V\x04B\x04!\x00'
# CP-1251: b'\xcf\xf0\xe8\xe2\xb3\xf2!'
# True


"""Attempting to convert a byte string 
in the wrong encoding leads to either 
an error or a rather unpredictable result:
"""
print(b"Hello world!".decode("utf-16"))
print("~" * 30)
# Output if encoding UTF-8 we try to decode to UTF-16:
# 数汬⁯潷沩Ⅴ

"""it is important to open file with mentioning
of formatting to avoid errors"""

# Opening a text file with explicit instructions for UTF-8 encoding
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
print("~" * 30)

"""
In this example, even if the operating system uses 
a different default encoding, the file will be correctly 
opened using UTF-8, which ensures hat the text is displayed correctly.

 In a world where data is often exchanged
 between different systems and platforms, 
 the unification of encoding to UTF-8 is a key factor 
 to ensure compatibility and correct processing of text data. 
 Specifying the encoding when opening files with the open() 
 function helps to avoid many problems related 
 to localization and international support."""


# Byte array

"""Working with strings is limited by the fact that strings 
and byte strings are immutable. If you want to replace 
even one character, you essentially need to create a copy 
of the original string with a single different character. 
To reduce overhead when working with "raw" data, 
Python has such a container as bytearray.
"""

byte_array = bytearray(b"Kill Bill")
byte_array[0] = ord("B")
byte_array[5] = ord("K")
print(byte_array)  # bytearray(b'Bill Kill')
print("~" * 30)

"""The main difference with byte strings 
is the mutability, in order to change the byte array, 
you don't need to create a new one. The second important 
difference is that the byte array is perceived by the system 
as a sequence of numbers from 0 to 255, and not as a sequence 
of characters in ASCII encoding. That is why you cannot 
write byte_array[0] = b'B'. The elements of the byte array 
are treated exactly as integers.
"""

"""Otherwise, bytearray can be used as a replacement for 
byte strings and has the same methods with the same behavior.
"""

"""In addition to modifying existing elements, 
bytearray allows you to add and remove elements, 
making it much more flexible than immutable byte arrays.
"""

byte_array = bytearray(b"Good morning")
byte_array.append(ord(")"))
print(byte_array)  # bytearray(b'Good morning)')
print("~" * 30)

"""Although a bytearray is treated as a sequence of numbers, 
it can easily be converted to a string using 
the decode() method by specifying the desired encoding.
"""

byte_array = bytearray(b"Hi Molly")
string = byte_array.decode("utf-8")
print(string)  # Hi Molly
print("~" * 30)

"""bytearray is particularly useful when working 
with binary data, such as reading files in binary mode, 
processing network packets, or working with data in memory."""
