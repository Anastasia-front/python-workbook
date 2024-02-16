"""One way to create a generator in Python is to create 
a custom function with multiple entry points. 
For this, the keyword yield is used.

The yield operator behaves in a similar way to return, 
it returns control of the flow of program execution 
from the body of the function. But, unlike return, 
yield does not start the execution of the function 
from the beginning at the next call, but continues 
from the point where the function stopped.

Of course, this behavior assumes that somewhere in 
the memory of the program should be stored information 
about what the execution of the function stopped at 
and about the state of the local namespace of the function. """

# Consider the following example:


def generator():
    yield 1
    yield 2
    yield 3


gen = generator()

print("~" * 30)
# Using next()
print(next(gen))  # Print 1
print(next(gen))  # Print 2
print(next(gen))  # Print 3
print("~" * 30)

"""
This code demonstrates the basic principles of how a generator works in Python. 
The function generator is defined as a generator. It uses the yield keyword, 
which indicates that this function will return a generator. When a function calls yield, 
it "returns" the value that follows yield and "freezes" its current state. 
The execution of the function will continue from this point on the next call. 
When we assign gen = generator(), the variable gen is now the generator 
returned by the generator function.

Next comes the use of next(). Each time next(gen) is called, the generator 
continues execution from where it last stopped (after yield). On the first call to next(gen), 
the generator is executed from the beginning to the first yield, i.e. returns 1. 
On the second call to next(gen), it continues from the second yield and returns 2. 
On the third call to next(gen), it continues to the third yield and returns 3. 
The code print(next(gen)) prints the value returned by the generator at each step.

After the generator has returned all its values, if we call next(gen),
we will throw a StopIteration exception because there are no more values to return. 
This exception signals that the iteration has finished.

In order not to use try except every time to control the StopIteration exception, 
generators are often used directly in for ... loops, which will do it for us:
"""


def count_down(start):
    while start > 0:
        yield start
        start -= 1


for number in count_down(5):
    print(number)
print("~" * 30)
# The result of executing this code will be
# 5
# 4
# 3
# 2
# 1

"""
One of the useful cases of using a generator is iterating over a file. 
The generator allows us to process very large files and at the same time save memory.
"""

folder_path = "example"
file_path = f"{folder_path}/example.txt"


def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


# Using a generator to read lines from a file
for line in read_lines(file_path):
    print(line)
print("~" * 30)

"""
In the middle of the read_lines function, the for loop iterates over each line in the file. 
The yield keyword is used to return each line of the file. Each line is pre-processed 
with the strip() method to remove spaces and newline characters from the edges. 
This is a common data cleansing practice.

Next, we simply use the generator to work directly with the strings of the file.

The advantage of this approach is that thanks to lazy processing, 
the generator reads lines one by one without loading the entire file into memory. 
This is especially useful when working with large files.


So let's make a summary:

A generator in Python is an object that is used for lazy (on-demand) 
data generation and allows us to declare a function that can be used in a loop.

A generator is created using a function that returns a sequence 
of elements one by one using yield instead of return.

The generator produces elements "on the fly" and processes one element at a time. 
This is very efficient in terms of memory usage, especially for large data. 
When a generator produces a value, its state is "frozen" 
and execution can continue from that point on the next call.

Generators can be iterated in a for loop or manually using the next() function."""


# Transferring values to the generator

'''
The yield operator has a rarer use, it can return a value just like a function call. 
This allows you to pass values to the generator by calling the send method.

The send() method is used to interact with the generator by sending a value 
to the generator that can then be used as the result of the yield expression. 
This allows the generator to not only produce data, but also process external data on each iteration.
'''


def my_generator():
     received = yield "Ready"
     yield f"Received: {received}"

gen = my_generator()
print(next(gen)) # Ready
print(gen.send("Hello")) # Received: Hello

print("~" * 30)
'''
The send() method is used to pass the value directly to the generator. 
The value passed through send() is the result of the yield expression 
where the generator was suspended. This allows generators to not only 
produce values, but also to accept data at any point in their execution.

We start the next(gen) generator and receive the first "Ready" message. 
We send data to the generator gen.send("Hello") and receive the following value "Received: Hello".

When the generator no longer needs to produce values, it can be closed using the close() method. 
At the same time, the GeneratorExit exception is called in the generator, which 
can be intercepted to perform some actions before closing the generator.
'''


def my_generator():
     try:
         yield "Working"
     except GeneratorExit:
         print("Generator is being closed")

gen = my_generator()
print(next(gen)) # We get "Working"
gen.close() # Call to close the generator

print("~" * 30)
'''
These mechanisms allow you to implement a rather complex logic of interaction between 
the code and generators, providing flexibility and control over the execution process of the generators.

For example, let's create a generator that can accept strings of text, 
filter them according to a certain criterion (for example, return a string 
if it contains a certain word), and return only those strings that meet this criterion.


First, let's consider a simple example. Let's create a square_numbers() generator 
that will accept numbers through the send() method and perform calculations, 
take a simple operation of raising to the square, and return the result through yield.
'''


def square_numbers():
     try:
         while True: # An infinite loop for accepting numbers
             number = yield # Getting a number via send()
             square = number ** 2 # Squaring
             yield square # Return the result
     except GeneratorExit:
         print("Generator closed")

# Creation and start of the generator
gen = square_numbers()

# Initialize the generator
next(gen) # Or gen.send(None) to start

# Sending the number to the generator and getting the result
result = gen.send(10) # Should return 100
print(f"Square of 10: {result}") # Square of 10: 100

# Go to the next wait
next(gen)

# Sending another number
result = gen.send(5) # Should return 25
print(f"Square of 5: {result}") # Square of 5: 25

# Closing the generator
gen.close() # Generator closed


print("~" * 30)
'''
In the code, after each call to send() that returns a number, 
we need to call next(gen) or send() again to continue executing 
the generator until the next yield. This is precisely 
what allows the generator to accept a new value.

Now consider a more complex example. Let's create a filter_lines() 
generator that will wait for incoming lines through the send() method. 
Inside the generator, there will be a check: if the string contains 
a certain word, it will be returned via yield.
'''


def filter_lines(keyword):
     print(f"Looking for {keyword}")
     try:
         while True: # An infinite loop where the generator waits for input
             line = yield # Receiving a line via send()
             if keyword in line: # Checking for the presence of a keyword
                 yield f"Line accepted: {line}"
             else:
                 yield None
     except GeneratorExit:
         print("Generator closed")

if __name__ == "__main__":
     # Creation and start of the generator
     gen = filter_lines("hello")
     next(gen) # Required to start the generator
     messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbye"]
     hello_messages = []
     # Sending data to the generator
     for message in messages:
         result = gen.send(message) # Send a message to the generator
         if result: # Add the result only if it is not None
             hello_messages.append(result)
         next(gen) # Continue to the next yield: instruction line = yield

     # Closing the generator
     gen.close()
     print(hello_messages)

# Output
# Looking for hello
# Generator closed
# ['Line accepted: hello world', 'Line accepted: another hello world line', 'Line accepted: hello again']

print("~" * 30)
'''
Overall, this approach makes generators a powerful tool for 
asynchronous programming, data streaming, and cooperative multitasking in Python.
'''