"""
When you write your application, you may need to create your own exceptions 
to handle at a higher level. Creating your own exceptions in Python allows you 
to better manage errors in your code, making it more flexible and understandable 
for other developers. To do this, you need to define an exception class 
that inherits from the Exception class or one of its subclasses.
"""

# Creating your own exception is quite easy:


class MyCustomError(Exception):
    """Base class for custom exceptions"""

    pass


"""
Here, MyCustomError is a custom exception class that you can use to throw errors specific to your application.

Let's consider several examples. Let's define our own exception class for handling errors 
related to checking a person's age. This can be useful in situations where you need to make sure 
that a person has reached a certain age, for example, to register on the site or when buying 
certain products. First of all, we need to create our own exception class and name it accordingly - 
AgeVerificationError, which inherits from the base Exception class. This class will be used to throw 
an error when a person's age does not meet the specified conditions.

Let's create a verify_age function that takes age as an argument and checks 
if the person is an adult (for example, 18 or older). If the age is less than 18, 
the function should throw an AgeVerificationError exception.
"""

print("~" * 30)
# Define your own exception class
class AgeVerificationError(Exception):
    def __init__(self, message="Age does not meet the minimum requirement"):
        self.message = message
        super().__init__(self.message)


# Function to check age
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("The person's age is less than 18")


if __name__ == "__main__":
    # Handle the exception
    try:
        verify_age(16)  # Change age for different results
    except AgeVerificationError as e:
        print(f"Exception: {e}")  # Exception: The person's age is less than 18 years
    else:
        print("Age checked, the person is an adult.")


"""
We used a try/except block to handle the exception thrown by the verify_age function. 
If we run the code, a call to the verify_age function with an age less than 18 will throw 
our AgeVerificationError exception and display an appropriate message.


Next example, you expect the user to enter a name, and that name must be no shorter 
than two characters and begin with an uppercase letter. We can create our own exceptions 
that will be thrown if the user input fails this validation. Then any code that calls 
this function will be able to handle this particular case correctly.
"""


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass

print("~" * 30)
def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name


if __name__ == "__main__":
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)
print("~" * 30)

"""
We have defined two custom exception classes: NameTooShortError and NameStartsFromLowError. 
They inherit from the Exception class and are intended to signal specific errors when entering 
a name: when the name is too short or does not begin with a capital letter.

In general, this structure of custom exceptions allows flexible handling of input errors 
without interrupting program execution when they occur. But notify the user what exactly happened.
"""
