"""Parameters to a function are some inputs that we can pass
to the function in order to get a result corresponding to that data.


Functions can take parameters, that is, some values passed
inside the function for it to do something with.
These parameters are similar to variables, except
that the values of these variables are specified
when the function is called, and they are already
assigned their values when the function runs.


Parameters are specified in parentheses when declaring
a function and are separated by commas.
Similarly, we pass a value when we call a function.


Note the terminology: the names you specify
when you declare a function are called parameters,
while the values you pass to the function
when you call it are called arguments."""

print("~" * 30)


def print_max(a, b):
    if a > b:
        print(a, "max")
    elif a == b:
        print(a, "equal", b)
    else:
        print(b, "max")


print_max(3, 4)  # direct transfer of values
print("~" * 30)

x = 5
y = 7
print_max(x, y)  # passing variables as arguments
print("~" * 30)


# type hints
def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum


result = add_numbers(5, 10)
print(result)
print("~" * 30)


def is_even(num: int) -> bool:
    return num % 2 == 0


check_even = is_even(4)
print(check_even)
print("~" * 30)

"""A scope is an area in your program (code) within which
you can refer to the contents of a variable by name.
These scopes are divided into four levels in the search order
of variable names, and are known as the LEGB rule:"""


L = """Local: This is the internal level where the name is 
defined inside a function or block of code."""
E = """Enclosing: This is the scope that encloses the local scope. 
If a function is inside another function, the names defined 
in the enclosing function will be available to the inner function."""
G = """Global: This is module or script level scope. 
Variables defined at this level are available throughout the module."""
B = """Built-in: This is the outermost level that contains names built into Python. 
For example, we considered built-in functions, len, range, etc."""


recursion = """ is a concept in programming where a function calls itself 
within its own execution. It's like breaking a big problem down 
into smaller, more manageable problems."""


def fibonacci(n):
    if n <= 1:  # base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # recursive case


print(fibonacci(10))  # will output 55
print("~" * 30)

call_stack = """is a specific part of memory used to store information
about active function calls. Each time a function is called, a new entry
(or "layer") is created on this stack for that particular call.
This layer contains information about the function's variables,
its parameters, and the location from where the function was called, 
so that when the function completes, the program 
can continue from the correct location."""


def factorial(n):
    print("Calling the factorial function with n = ", n)
    if n == 1:
        print("Base case, n = 1, return 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print("Return result for n = ", n, ": ", result)
        return result


print(factorial(5))
print("~" * 30)


"""Recursive functions are convenient in situations where we do not know
in advance how many times the function will need to be called,
for example, when parsing directories on a disk. The application
does not know in advance how deep the directory structure is and
what level of nesting they have. And to iterate over all files
in all nested directories, the function must call itself when
it encounters the next directory."""
