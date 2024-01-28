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


recursive_functions = """are convenient in situations where we do not know
in advance how many times the function will need to be called,
for example, when parsing directories on a disk. The application
does not know in advance how deep the directory structure is and
what level of nesting they have. And to iterate over all files
in all nested directories, the function must call itself when
it encounters the next directory."""
