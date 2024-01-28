"""
Constants:
math.pi - π (approximately 3.14159...);
math.e - e, base of natural logarithms (approximately 2.71828...);
math.tau - τ is equal to 2π (approximately 6.28318...);
math.inf - notation of infinity;
math.nan - notation 'Not a Number' (not a number);

Number rounding functions:
math.ceil(x) - performs rounding of the real number x 
to the nearest larger integer;
math.floor(x) - rounds the real number x to the nearest smaller integer;
math.trunc(x) - performs truncation of the fractional 
part of the real number x, and returns the whole part of the number;

Trigonometric functions:
math.sin(x) - sine of x, where x is in radians;
math.cos(x) - cosine of x;
math.tan(x) - tangent of x;
math.asin(x) - arcsine of x;
math.acos(x) - arccosine of x;
math.atan(x) - arctangent of x;


Exponential and logarithmic functions:
math.exp(x) is a number - e to the power of x;
math.log(x[, base]) - Logarithm of x to the base base. If base is not specified, the natural logarithm is calculated;

Exponent and root:
math.pow(x, y) - x to the power of y;
math.sqrt(x) - square root of x;


Some other features:
math.fabs(x) - module (absolute value) of x;
math.factorial(x) - factorial of the number x;
math.gcd(x, y) - the greatest common divisor for x and y;
"""
import math

# Correct comparison of real numbers

print("~" * 30)
print(0.1 + 0.2 == 0.3)  # False
print(0.1 + 0.2)  # 0.30000000000000004


r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # True

print("dir(math)")
print(dir(math))
print("~" * 30)
