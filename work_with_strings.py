useful_link = 'https://docs.python.org/3/library/string.html#format-specification-mini-language'

# Control characters (control characters) are special characters
# used to control and format text in lines. They are often represented
# as escaped sequences starting with a backslash character (\).
# Some of the most common control characters in Python include:

# \n: New line (LF - Line Feed). Used to move to a new line.

# \r: Carriage Return (CR - Carriage Return). Used to move the cursor to the beginning of the line.

# \t: Horizontal Tab (HT - Horizontal Tab). Inserts a tab.

# \b: Slaughter (BS - Backspace). Used to delete the previous character.

# \f: Page feed (FF - Form Feed). Used to go to a new page.

print(dir(str))

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end))  # 5
print(s.find("q"))  # -1
print(s.rfind("e"))  # 7
print(s.rindex("e"))  # 7
print(s.index("i"))
# s.index('o') #ValueError

# str.split(separator=None, maxSplit=-1)
result = s.split()
print(result)  # ['Hi', 'there!']
# string.join(iterable)
result = " ".join(result)
print(result)  # Hi there!

# str.replace(old, new, count=-1)
new_s = s.replace("there", "PythonPythonPython")
print(new_s)  # Hi PythonPythonPython!
new_text = new_s.replace("Python", "-", 2)
print(new_text)  # Hi --Python!

print("TestBridgeHook".removeprefix("Test"))  # BridgeHook
print("TestBridgeHook".removesuffix("Hook"))  # TestBridge

# processing request parameters - split method
url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)



# a program that converts an input text string into the appropriate Morse code - translate method
morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Conversion of dictionary keys to Unicode codes
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "function is used with a key function that returns a tuple"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)


# String formatting

# Any number can be written in several writing options:
# decimal notation
# binary representation
# hexadecimal representation
# scientific notation
# with fixed precision (number of decimal places)
# and other.

# numbers from 1 to 15 in decimal, hexadecimal, 
# octal and binary representation can be as follows:
for i in range(1,4):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

# output
# int: 1;  hex: 0x1;  oct: 0o1;  bin: 0b1
# int: 2;  hex: 0x2;  oct: 0o2;  bin: 0b10
# int: 3;  hex: 0x3;  oct: 0o3;  bin: 0b11

# display a real number with two digits after the decimal separator using expressions in f-strings
price = 35.11
quantity = 5
total = f"Total: {price * quantity:.2f}"
print(total) #Total: 175.55

# In the expression :.2f:

# : Enters the format specification.
# .2 means that two digits should be output after the decimal point.
# f indicates a real number format.

# f"{value:<width>:.<precision>f}" OR f"{value:<width>.<precision>%}"

completion = 0.941
formatted = f"{completion:.1%}"
print(formatted)  #  '94.1%'
progress = 0.6
formatted = f"{progress:.0%}"
print(formatted) #60%

# centering values in columns 10 characters wide:
for num in range(1,8):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')

# FieldWidth specifies the minimum width of the field in which the content will be placed. 
# If the content is shorter than the field width, it will be padded with spaces.



# Alignment specifies how the content will be aligned within the specified field width. 
# Possible alignment options:

# <: Aligns content to the left.
# >: Right-align the content.
# ^: Align the content to the center.
# =: Used to align numbers, with the sign (if any) displayed 
# on the left and the number on the right of the field.
    

name = "John"
formatted = f"{name:<7} {name[::-1]:>7}"
print(formatted)  # John       nhoJ

