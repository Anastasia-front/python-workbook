from enum import Enum, auto

"""
The enum module in Python provides the ability to create enumerated types 
that allow you to define named constants. These constants can be used to 
improve code readability and reliability by replacing the use of implicit values 
such as strings or numbers with more understandable names.

The Enum class from the enum module allows you to combine a number of named constants
 and guarantee that objects of this class can take only one of the limited values they describe.

To create an enumeration, an inheritance from the Enum class is used. 
Each class attribute represents a separate member of the enumeration.
"""


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


"""
This definition allows you to use Day.MONDAY, Day.TUESDAY, etc., 
to represent the days of the week in your code, instead of using simple numbers or strings.
"""

# You can access a specific day by its name:
print("~" * 30)
today = Day.MONDAY
print(today)  # Prints: Day.MONDAY
print("~" * 30)

# Enum members can be compared with each other using comparison operators:

if today == Day.MONDAY:
    print("Today is Monday.")
else:
    print("Today is not Monday.")
print("~" * 30)

# Each Enum member has name and value properties, which return the name and value of the member, respectively:

print(today.name)  # MONDAY
print(today.value)  # 1
print("~" * 30)

# If you have a value and want to get the corresponding Enum member, you can use the Day() method with that value:

day_from_value = Day(1)
print(day_from_value)  # Outputs: Day.MONDAY
print("~" * 30)

"""
Let's look at a real-life example of using Enum, where we will create an order 
status management system for an online store. In this example, Enum is used to create 
a well-defined set of statuses that an order can have. 
These statuses include NEW, PROCESSING, SHIPPED, and DELIVERED.

First of all, we need to define an Enum that will represent the different order statuses.

Next we used the auto() function to automatically assign unique values 
to each status, avoiding the need to manually specify them.

Now let's create an Order class that will use our OrderStatus 
enumerated data type to track the status of the order.
"""


class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()


class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Order '{self.name}' has been updated to {self.status.name}.")

    def display_status(self):
        print(f"Order status '{self.name}': {self.status.name}.")


order1 = Order("Laptop", OrderStatus.NEW)
order2 = Order("Book", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()
print("~" * 30)
# When we run this code, we'll see the order statuses update and display:

# Order status 'Laptop': NEW.
# Order status 'Book': NEW.
# The order 'Laptop' has been updated to PROCESSING status.
# The 'Book' order has been updated to SHIPPED status.
# Status of order 'Laptop': PROCESSING.
# Order status 'Book': SHIPPED.


"""
The example demonstrates how Enum can be used to efficiently 
represent and manage a fixed set of possible states in a program.

This provides a clear definition of order statuses and helps 
prevent errors associated with using incorrect or unknown statuses.


In conclusion, we can see that using enumerations makes the code more readable 
because they allow to use named constants instead of magic numbers or strings. 
Since the Enum object can only accept the values defined in the enumeration, 
this reduces the chance of errors associated with passing invalid values.

Changing or adding new values to an Enum does not affect the rest of the code, 
which makes changing (refactoring) and extending the code easier. For example, 
to add a new status of "CANCELED", you would simply extend the definition of OrderStatus as follows:
"""


class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELED = auto()


# Without changing any other code in the program that already exists.
