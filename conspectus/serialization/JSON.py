import json

"""JSON, or JavaScript Object Notation, is a textual format for representing 
structured data based on the object syntax of the JavaScript programming language.

Although it was designed for JavaScript, it is easily read and generated by many programming languages, 
making JSON very popular for data exchange between clients and servers, web applications. 
It is widely used for storing configurations, serializing data in file systems, and as a data exchange format 
between different programming languages due to its simplicity and support by many libraries.

JSON offers a simple and understandable structure. It represents data as a set of key-values, 
where the keys are strings and the values can be strings, numbers, arrays, booleans, or even other objects. 
It makes it easy to represent complex data structures such as lists, dictionaries, and hierarchical trees.

The main advantage of JSON is that it allows data to be represented in a format that is easy for a human to read and write, even by hand.


JSON syntax is based on two structural elements: objects and arrays.


Python supports the JSON format and comes standard with the json package,
which contains everything you need to work. This library allows you to easily serialize Python objects 
into JSON format and deserialize JSON strings back into Python objects. Let's consider in detail how it works.



Serialization (or "writing") converts Python objects to a string in JSON format. 
This is done by using the json.dumps() method to convert the objects to a JSON string.

The dumps method packs an object into a byte line, loads unpacks (deserializes) from a byte line into an object. 
These methods are needed when we want to control what to do with a byte representation, such as sending it over 
the network or receiving it from the network.
"""
print("~" * 30)


some_data = {
    "key": "value",
    2: [1, 2, 3],
    "my_tuple": (5, 6),
    "my_dict": {"key": "value"},
}

json_string = json.dumps(some_data)
print(
    json_string
)  # {"key": "value", "2": [1, 2, 3], "my_tuple": [5, 6], "my_dict": {"key": "value"}}
unpacked_some_data = json.loads(json_string)
print(
    unpacked_some_data
)  # {'key': 'value', '2': [1, 2, 3], 'my_tuple': [5, 6], 'my_dict': {'key': 'value'}}

print("~" * 30)

"""
Python objects are encoded into JSON format according to the following rules:

The json module converts dicts into JSON objects,
The list and tuple are converted to a JSON array.
A Python string is converted to a JSON string.
Integers and real numbers are converted to JSON numbers.
The boolean value True is converted to the JSON constant true.
The Boolean value False is converted to the JSON constant false.
None is converted to a null JSON constant.


In fact, to solve these and other specific problems, the json library allows you to use additional parameters 
default and object_hook for non-standard serialization and deserialization. But we will not focus on these specific tasks, 
but will consider more relevant work with files.

Serializing a Python object to a JSON string is done using the json.dump() method if you want to write the JSON directly to a file.
"""

# Python object (dictionary)
data = {"name": "Микола Кoшoвий", "age": 30, "isStudent": True}
folder_path = "example"
file_path = f"{folder_path}/data.json.txt"
# Serialization to a file
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f)


# Deserialize from a file
with open(file_path, "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
    print(data_from_file)

print("~" * 30)

"""
In principle, there is no difficulty with the help of the json library to perform flexible conversion between formats,
adapting serialization and deserialization to the specific needs of our program.

The problem can occur only when writing Cyrillic or any other non-ASCII characters to the JSON file. 
Therefore, it is important to ensure correct character encoding to avoid file readability and compatibility issues. 
By default, Python uses UTF-8 encoding, which supports the Cyrillic alphabet, but when writing to JSON, 
we need to specify additional parameters to ensure the correct display of characters. What's the point? 
Let's look at the following example.
"""


# Serialization to a file
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f)

# Deserialize from a file
with open(file_path, "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
    print(data_from_file)

print("~" * 30)

"""Here in the data dictionary, as a value for the name key, we have the string "Микола Кoшoвий", 
which is written in Cyrillic characters. If we look in the data.json file, we will see the following:

{
   "name": "\\u0413\\u0443\\u043f\\u0430\\u043b\\u043e \\u0412\\u0430\\u0441\\u0438\\u043b\\u044c",
   "age": 30,
   "isStudent": true
}

As you can see, instead of the string "Микола Кoшoвий" we have a set of Unicode escape sequences. 
Each escape sequence begins with \\u followed by four hexadecimal digits that represent the character in Unicode.

Here's how to fix it and write the data to a JSON file using Cyrillic:
"""


# Python object (dictionary)
data = {"name": "Микола Кoшoвий", "age": 30, "isStudent": True}

# Serialization to a file
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


"""
We used two important parameters of the json.dump function:

ensure_ascii=False ensures that Cyrillic characters are written as is, without converting to their Unicode escape sequences.
indent=4 provides output formatting by making the JSON file more human-readable with indentation.

Deserialization is performed as before."""