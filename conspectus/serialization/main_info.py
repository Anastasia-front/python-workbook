"""Object serialization in Python is the process of converting a data structure or object 
into a stream of bytes for storage or transmission. This stream of bytes can be stored in a file, 
transferred over a network, or even used for storage in databases. The purpose of serialization is 
to preserve the state of an object so that it can be restored in the future. The process of restoring 
the state of an object from a serialized form is called deserialization.

The main purpose of serialization - save the state of the object.

Whenever you need to save information for future use in a computer-readable form, let's do serialization. 
The most obvious example is data to a text file. You can save, for example, a list of expenses in a text file:
"""
print("~" * 30)

expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}

folder_path = "example"
file_path = f"{folder_path}/expenses.txt"
with open(file_path, "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}\n")

"""
This file will be fully readable:
hotel|150
breakfast|30
taxi|15
lunch|20

If you later need to load this list back into Python, you can always do so:
"""

expenses = {}

with open(file_path, "r") as fh:
    raw_expenses = fh.readlines()
    for line in raw_expenses:
        key, value = line.split("|")
        expenses[key] = int(value)

print(expenses)  # {'hotel': 150, 'breakfast': 30, 'taxi': 15, 'lunch': 20}

print("~" * 30)
"""
In this primitive example, we serialized and deserialized a dictionary of costs. 
This approach is a justified result, especially if it is worth preserving the informative form of information.



However, this approach is not always justified. Note that this example had to invent its own serialization protocol. Namely:

- the newline symbol indicates the beginning of a new key-value pair;
- symbol | separates key and value
- the value must be converted from string representation to numeric form.


To work with data serialized using this protocol, you need to keep it in mind and extend the protocol as needed.

You can go the other way and use one of the standard protocols. For such an approach, 
you can save money by using a ready-made and tested solution.


Python provides several modules for serialization, the most popular of which are pickle and json.

- the built-in pickle package allows you to work with built-in types 
(dictionaries, lists, tuples, strings, sets, etc.) and even with simple classes;
- the JSON format is supported by Python and, with minor limitations, 
allows you to work with strings, numbers, lists, tuples, and dictionaries.


Both of these methods have their advantages and limitations. Pickle is highly flexible
and allows you to serialize complex objects, but can be dangerous when deserializing data from third-party sources. 
JSON is more limited in the types of data that can be serialized, but provides better cross-platform compatibility and security."""
