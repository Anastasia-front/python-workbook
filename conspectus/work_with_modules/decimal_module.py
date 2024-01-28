import decimal
from decimal import ROUND_DOWN, Decimal, getcontext

"""Decimal objects behave the same as floats, but they cannot be 
used together in the same expression. Executing an expression 
like Decimal("0.1") + 0.2 will result in an error.

The precision of calculations with Decimal is controlled through context. 
You can adjust the overall precision for all Decimal calculations.
"""

# Any calculations with Decimal will now be accurate to four decimal places.
print("~" * 30)
getcontext().prec = 6
print(Decimal("1") / Decimal("7"))  # 0.142857

getcontext().prec = 8
print(Decimal("1") / Decimal("7"))  # 0.14285714
print("~" * 30)


"""Note that we are referring specifically to the commas. 
Because getcontext sets the number of significant figures. 
And the digits before the comma can also be significant numbers."""

# Determination of significant figures:
all_non_zero_digits = "are significant: 1, 2, 3, 4, 5, 6, 7, 8, 9"
zeros = "between non-zero digits are significant: 102, 2005, 50009"
leading_zeros = "are never significant: 0.02; 001.887; 0.000515"
"""A number with or without a decimal point contains significant zeros 
(to the right of the last non-zero digit), provided that they are justified 
by the accuracy of their use: 389,000; 2.02000; 5,400; 57.5400.
"""

getcontext().prec = 6
print(Decimal("233") / Decimal("7"))  #33.2857
print("~" * 30)


"""
If we need the rounding of numbers, we need to use the quantize method. 
The quantize method is used to set the precision of a Decimal number 
based on another Decimal number that is used as a template.

For example, if you want to round a number to two decimal places, 
you use a Decimal object with two decimal places as a template.
"""


# Output Decimal number
number = Decimal("3.14159")

# Set precision to two decimal places
rounded_number = number.quantize(Decimal("0.00"), rounding=ROUND_DOWN)
print(rounded_number)
print("~" * 30)

"""
Decimal allows you to choose different rounding modes. 
According to the official Python documentation, consider the main modes:

ROUND_FLOOR always rounds a number to the nearest 
smaller value, regardless of the sign of the number.

ROUND_CEILING always rounds a number to the nearest 
larger value, regardless of the sign of the number.

ROUND_HALF_DOWN numbers are rounded to the nearest value. 
In the case when the number is exactly in 
the middle between two possible rounding options (for example, 
2.5, where the possible options are 2 or 3), 
the number is rounded down, that is, to the nearest smaller value.

ROUND_HALF_UP numbers are rounded to the nearest value. 
However, in the case of a tie (when the number 
is exactly in the middle between the two options), 
the number is rounded up, that is, to the nearest larger value.

ROUND_UP the number is rounded from zero. This means 
that positive numbers are rounded to a higher value, 
and negative numbers are rounded to a lower value.

ROUND_DOWN the number is rounded to zero. That is, 
positive numbers are rounded to a smaller value, 
and negative numbers are rounded to a higher value.

ROUND_HALF_EVEN numbers are rounded to the nearest number. 
This mode, also known as "bank rounding", 
rounds the number to the nearest value, but in the case 
of a tie (when the number is exactly in 
the middle between the two options), it is rounded 
to the nearest even integer. For example, 
how 2.5 will be rounded to 2, and 3.5 - to 4. 
This method reduces the cumulative error in a series of rounds.


By default, rounding is described by the ROUND_HALF_EVEN constant

"""

number = Decimal("1.45")

# Default rounding to one decimal place
print("Default rounding ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))
# Default rounding is ROUND_HALF_EVEN: 1.4

# Rounding up in case of a tie (ROUND_HALF_UP)
print(
    "Rounding up ROUND_HALF_UP:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP),
)
# Rounding up ROUND_HALF_UP: 1.5

# Round down (ROUND_FLOOR)
print(
    "Rounding down ROUND_FLOOR:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR),
)
# Rounding down ROUND_FLOOR: 1.4

# Rounding up (ROUND_CEILING)
print(
    "Rounding up ROUND_CEILING:",
    number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING),
)
# Rounding up ROUND_CEILING: 1.5

# Rounding to three decimal places by default
print(
    "Rounding to three decimal places:", Decimal("3.14159").quantize(Decimal("0.000"))
)
# Rounding to three decimal places: 3.142
print("~" * 30)


"""
The quantize method is often used in financial applications 
where it is necessary to precisely control the number of decimal places, 
especially in calculations that require strict adherence to certain 
rounding rules. This ensures accuracy and compliance with requirements 
that may be imposed by law or accounting standards.


Decimal itself is a powerful tool for precision calculations
that provides a high level of control and flexibility. Its use 
is critical in financial applications, accounting, and other 
areas where rounding errors can have serious consequences."""



print("dir(decimal)")
print(dir(decimal))
print("~" * 30)
