# Any number can be written in several writing options:
# decimal notation
# binary representation
# hexadecimal representation
# scientific notation
# with fixed precision (number of decimal places)
# and other.

# numbers from 1 to 15 in decimal, hexadecimal,
# octal and binary representation can be as follows:
for i in range(1, 4):
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
print(total)  # Total: 175.55

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
print(formatted)  # 60%

# centering values in columns 10 characters wide:
for num in range(1, 8):
    print(f"{num:^10} {num**2:^10} {num**3:^10}")

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


# Splitting the Lines
zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense."""

print(zen.splitlines())

# Advanced Formatting:

# Positioning
# we need to set formatting type preceded by colon within curly brackets. Let's consider them:

# Option	Meaning	Comments
# <	Forces the field to be left-aligned within available space	Default method for most objects
# >	Forces the field to be right-aligned within available space	Default method for a number
# =	Forces the padding to be placed after the sign to the leftmost position	Useful for strings like 00000132
# ^	Forces the field to be centered within the available space	no special uses
# Using codes with no additions is not the best practice since there may be no differences after formatting.
# Let's consider additional arguments. We can place the symbol (only one!) we want to fill
# free space between colon : and argument from the table above. Then, we can also add the
# length you want to align your string in. For example,

print(".{:-^10}.".format("test"))

# Sign
# Assume we want to represent our numbers along with plus/minus sign.
# The minus sign will be printed anyway, but plus sign never prints with an integer.

# To make Python print a sign of a number we need to set sign option.
# There are three of them:

# Option	Meaning
# : (space after the colon)	Use a space before positive number, a minus - before negative
# :-	Use a minus sign for negative numbers only
# :+	Use a plus sign for positive numbers, and minus - for negative

print(".{:+}.{: }.".format(3, -7))
print(".{:+}.{: }.".format(-6, 2))

# Float, Round, and Percent
# Within a simple {} block, we can round a float number
# with the necessary precision, or represent a number as a percent.

# Let's consider the pattern we will use here:

# {:[thousands separator].[number][type]}

# Please note, that like in the previous chapters,
# we don't need to place square brackets (I placed it for convenience).

# [thousands separator] - the symbol used to separate every thousand (possible values are , and _).
# [number] - is the precision, number of decimal places (used for rounding number).
# [type] - type of number representing (e - scientific notation, % - percentage
#  (will multiply number by 100), g - general format, f - fixed-point notation).
# You can dive deeper into possible options in Python documentation.

print("Original number: {0}, formatted number: {0:.2f}".format(255 / 8))
print("Original number: {0}, formatted number: {0:.2%}".format(15 / 48))
print("Original number: {0}, formatted number: {0:,.2f}".format(35 * 6327))
