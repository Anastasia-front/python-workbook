source_code = """is a set of phrases, words, and special symbols 
specific to a programming language that describe 
a set of instructions for a computer."""


# But the symbols, words, and phrases that make up a program are not really understandable to a machine.
# There is a step that is performed after the program is written that converts the source code in the file
# into a set of instructions that the computer can understand. This is done by a special program: a compiler or an interpreter.


# A compiler and an interpreter are the two main types of interpreters
# used to convert code written in a programming language
# into machine code that a computer can execute.


compiler = """converts all program code into machine code before executing it. 
This process is known as compilation. After compilation, the program becomes 
an executable file (*.exe) that can be run on a computer. The compilation happens once,
 and after that the program can be run without needing to be recompiled as long as there 
 are no changes to the code. The programming languages used by the compilers are C, C++, and Rust."""

interpreter = """translates the program code into machine code during its execution, 
processing the code line by line. Interpreters do not create executable files; instead, 
they read and execute the code directly. And this means that the program must be interpreted 
every time it is launched. The programming languages used by interpreters are Python, Ruby, and PHP."""

instruction = """ (statement) is a related set of words and symbols 
from language syntax that are combined to express one idea, one instruction for a machine."""

expression = """ is a combination of values, variables, operators, and function 
calls that the interpreter evaluates ("executes") to obtain some result. Expressions always return something. 
In other words, every time Python evaluates an expression, it returns or outputs a value."""

# a program that converts time from seconds to full hours, minutes, and seconds

n = 5000

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60
print(f" {n} seconds consist of {hours} hours, {minutes} minutes and {seconds} seconds")

# Key features of Python include:


# Readability and simplicity: Python has a simple and intuitive syntax that makes it accessible to beginners.
# It supports both procedural and object-oriented programming.
# Interpreted language: Python code is executed line by line, making debugging and testing easier.
# Dynamic typing: Python does not need to declare variable types in advance; the type is determined automatically during program execution.
# Versatility: Python is used in a wide range of industries, from web development to scientific research,
#  from data analysis to artificial intelligence.
# Extensive standard library: Python comes with a standard library that includes a wide set of tools
#  for various tasks. In fact, it is the Swiss army knife of programming.
# Community and Support: Python has one of the largest and most active communities among
# programming languages, contributing to a large number of resources, libraries, and tools.


# Python is used for both academic and commercial purposes, and its popularity continues to grow due to its flexibility, ease of learning, and large ecosystem.


# Today, Python is used in the following areas:


# Web Development: Using frameworks like Django and FastAPI, Python allows you to build scalable web applications and APIs.
# Data Science:
# Data Mining: Analyzing big data to obtain useful information and knowledge.
# Machine Learning: Developing models that can learn and make predictions based on data.
# Deep Learning: Creating complex neural networks to develop systems with a high level of intelligence.
# Scientific research: Python is widely used in physics, chemistry, biology and other
# fields of scientific research for data analysis and modeling.
# Game Development: Although Python is not a primary language for large game development,
#  it is often used for prototyping and development of game tools.
# Internet of Things (IoT): Python is used to develop applications that allow devices to interact and be controlled over the Internet.
# Automation: Python's ease of scripting makes it a popular choice for automating routine tasks.
# Finance and trading: Financial data analysis, algorithmic trading, risk assessment and much more.
