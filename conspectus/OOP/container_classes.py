from collections import UserDict, UserList, UserString

"""
Often work requires creating objects that behave like standard Python containers, 
but with modified behavior. You can of course try to emulate dict, str, list, 
but that can lead to a number of unexpected errors. The correct way to get a modified container 
is to use the collections package and the UserList, UserDict, UserString classes it contains.

All these classes behave exactly like built-in containers with the only difference 
that the data itself is in the data field of these classes and you can use this field at your discretion.


UserDict is a class contained in the collections module that serves as a wrapper around a dictionary. 
It allows you to more easily create your own dictionary classes by modifying or adding new behavior to standard dictionary methods.
"""

# UserDict

print("~" * 30)


# EXAMPLE
class MyDictionary(UserDict):
    # Example of adding a new method
    def add_key(self, key, value):
        self.data[key] = value


# Create an instance of your own class
my_dict = MyDictionary({"a": 1, "b": 2})
my_dict.add_key("c", 3)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}
print("~" * 30)

"""
Was created a MyDictionary class that inherits from UserDict. 
It provides all the standard functionality of dictionaries and allows 
easy modification or extension. It also added an add_key method 
that demonstrates how you can add new behavior for adding items to a dictionary.
"""

# ANOTHER EXAMPLE

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Rose Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    },
]

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys

# Example usage:
my_lookup_dict = LookUpKeyDict({'a': 1, 'b': 2, 'c': 1})
result = my_lookup_dict.lookup_key(1)
print(result)

print("~" * 30)

class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"


if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("--------------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("--------------------------------")

    for customer in customers:
        print(customer.email_info())
print("~" * 30)
# ---------------------------
# Allen Raymond: (992) 914-3792
# Rose Lewis: (294) 840-6685
# Kennedy Lane: (542) 451-7038
# ---------------------------
# Allen Raymond: nulla.ante@vestibul.co.uk
# Rose Lewis: dui.in@egetlacus.ca
# Kennedy Lane: mattis.Cras@nonenimMauris.net


"""
In this example, we iterate over the customers list twice: 
the first time to display information about contact phones 
by calling the phone_info method, and the second time to display 
information about email addresses by calling the email_info method.

We had would like to be able to have the dictionary have methods 
that show us the name-phone and name-email of the contact. 
To do this, was created a Customer class that follows from UserDict from the collections module.

It extends UserDict and has two methods: phone_info and email_info, 
each of which returns a string containing the name and phone number 
or email address of the corresponding contact.

To use the capabilities of the created class, we need to create a new customers list, 
in which each element of the contacts list is transformed into an instance of the Customer class. 
This allowed us to use the methods defined in the class for each contact.
"""

# UserList

"""
UserList is a class that allows you to create your own versions of lists 
with additional features. You can add new methods or modify existing ones 
to work differently. This is useful when you need a list that does something 
special that a regular Python list doesn't.
"""

# EXAMPLE


class MyList(UserList):
    # Adding specialized behavior. For example, a method to add an element if it doesn't already exist
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)


# Create an instance of MyList
my_list = MyList([1, 2, 3])
print("Original list:", my_list)

# Adding an element if it doesn't exist
my_list.add_if_not_exists(3)  # Will not be added because it already exists
my_list.add_if_not_exists(4)  # Will be added because it does not exist yet
print("Updated list:", my_list)
print("~" * 30)
# Output
# Original list: [1, 2, 3]
# Updated list: [1, 2, 3, 4]


# ANOTHER EXAMPLE


class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, "2", 3, "4"])
countable.append("5")
print(countable.sum())  # 15
print("~" * 30)

# UserString

"""
It allows to create classes that mimic the behavior of a regular string, 
with the ability to add new methods or change the default behavior of strings. 
This is useful when you need to work with strings in a specialized way 
that is not supported by standard Python strings.
"""

# EXAMPLE


# Create a class that extends UserString
class MyString(UserString):
    # Adding a method that checks if a string is a palindrome
    def is_palindrome(self):
        return self.data == self.data[::-1]


# Create an instance of MyString
my_string = MyString("radar")
print("String:", my_string)  # String: radar
print("Is it a palindrome?", my_string.is_palindrome())  # Is it a palindrome? True

# Create another instance of MyString
another_string = MyString("phone")
print("String:", another_string)  # String: phone
print(
    "Is it a palindrome?", another_string.is_palindrome()
)  # Is it a palindrome? False
print("~" * 30)

# ANOTHER EXAMPLE


class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[: self.MAX_LEN]


ts = TruncatedString("hello world!")
ts.truncate()
print(ts)  # hello w
print("~" * 30)
