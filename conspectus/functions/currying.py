from typing import Callable, Dict

currying = """is a programming technique where a function 
that takes multiple arguments is converted into a sequence 
of functions that each take one argument. Named after the logician 
Gaskell Curry, currying makes functions more flexible 
and helps create highly modular and readable code.
"""


# Suppose we have a function that takes two arguments:
def add(a, b):
    return a + b


"""By applying currying to this function, 
we will turn it into two functions, each of which takes one argument:
"""


def add_currying(a):
    def add_b(b):
        return a + b

    return add_b


# Usage:
print("~" * 30)
add_5 = add_currying(5)
result = add_5(10)
print(result)
print("~" * 30)

"""
Here the add function takes the first argument a and 
returns the add_b function. The add_b function itself 
accepts a second argument b and returns the result a + b. 
In effect, we have turned the call to the add function into a call to two functions.

In functional programming, this approach makes it easy to reuse a function 
and create new functions based on existing ones. After we have considered 
the currying technique itself, let's look at some practical example of use.

Suppose we have a function to calculate a discount for an item. 
This function accepts the discount percentage and the final price of the product.
"""


def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)


# Usage
discounted_price = apply_discount(500, 10)  # 10% discount on the price of 500
print(discounted_price)  # 450.0

discounted_price = apply_discount(500, 20)  # 20% discount on the price of 500
print(discounted_price)  # 400.0
print("~" * 30)


"""
By using currying, we can create a more flexible 
structure to work with different types of discounts.

Let's convert the apply_discount function using currying. 
This will allow us to create "ordered" functions for different 
discount levels, each of which will only accept the product price.
"""


def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)

    return apply_discount


# currying in action
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

# Application of discounts
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)

discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)

print("~" * 30)

"""
Thus, with the help of currying, we split the function into two parts. 
First, we create ten_percent_discount and twenty_percent_discount functions 
with a specific discount percentage, and then use these functions to calculate 
the discounted price. This makes the code more flexible and makes 
it easy to create functions for different discount levels.

We can go a step further and create a dictionary where the keys are the discount 
names and the values are the corresponding discount calculation functions created using currying. 
This will allow us to easily select the desired discount function from the dictionary.
"""


def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)

    return apply_discount


# Creating a dictionary with discount functions
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30),
}

# Using a function from a dictionary
price = 500
discount_type = "20%"

discounted_price = discount_functions[discount_type](price)
print(
    f"Discounted price {discount_type}: {discounted_price}"
)  # Price with a 20% discount: 400.0

print("~" * 30)

"""
We create a dictionary discount_functions where each discount type 
"10%", "20%" and "30%" corresponds to a function with a function 
that calculates the discount. And now, to apply the discount, 
we select the desired function from the dictionary using the 
discount_type key and pass the product price to it. 

This approach provides a lot of flexibility because we can easily add, 
remove or change discounts in the dictionary without 
having to change the main code of the application.
"""
