# The main types of exceptionsS
syntaxError = "is a syntax error"
zeroDivisionError = "division by zero"
valueError = "occurs when the type of the operand is correct, \
    but the value is such that the operation cannot be performed."
IndentationError = "is an error that occurs if an error is made \
    in the selection of instruction blocks with spaces"
TabError = "occurs if you use spaces and tabs to\
      highlight blocks of instructions in the same file"
typeError = "occurs when an operation on a variable of this type is not possible"

# exception handling mechanism - al blocks of code
print("~" * 30)
letter = "a"
try:
    letter = int(letter)
except ValueError:
    print(f"letter {letter} is not a number")
else:
    print(letter > 0)
finally:
    print("This will be printed anyway")
print("~" * 30)

# ANOTHER EXAMPLE
try:
    # Code that may throw an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle division-by-zero exception
    print("Division by zero!")
except Exception as e:
    # Handle any other exception
    print(f"An error occurred: {e}")
else:
    # Executed if no exception was thrown
    print("Everything was successful!")
finally:
    # Always executed, regardless of whether an exception was thrown or not
    print("The finally block is always executed.")


# Exception for all error types
while 1:
    a_string = input("Enter 1st number: ")
    b_string = input("Enter 2nd number: ")

    try:
        a = int(a_string)
        b = int(b_string)
        if a == 0 or b == 0:
            print("Please do not use zero")
        else:
            print(f"a/b={a}/{b}={a/b}")
            break
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("Program is finished")
print("~" * 30)

#  break operator
while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 18:
            print("Access allowed")
            break
        else:
            print("Access denied")
            break
    except ValueError:
        print(f"`{age}` is not a number. Please enter a number")
    finally:
        print("~" * 30)


# continue operator
while "truthy value":
    a = input("Enter some numbers divided by space: ")
    try:
        strip = a.strip()
        b = strip.split(" ")
        print(f"Your input - {b}")

        c = []
        sum = 0

        for num in b:
            c.append(float(num))
            sum += float(num)

        length = len(c)

        if length == 1:
            print("You write only one number. Write more than one")
        else:
            print(f"List of numbers - {c}")
            print(f"Sum - {sum}")
            print(f"Length - {length}")
            for i in c:
                if i % 2:
                    # print(f'Even number - {i}')
                    continue
                print(f"Odd number - {i}")
            length += 1
            print(f"This is sum of enter numbers - {sum:.3f}")
            break
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("~" * 30)
