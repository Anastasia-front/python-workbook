import pickle

"""To perform serialization and deserialization of objects, speed, correctness 
and the small size of memory used are important, and the pickle package is best suited here.


The pickle module allows you to serialize Python objects into a stream of bytes 
and deserialize a stream of bytes back into objects. This is justified and useful 
for storing objects in files or transferring data over a network.


The primary purpose of a pickle is to preserve the state of an object so that 
it can be accurately restored later, often in a different location.

The pickle package has two pairs of paired methods:
"""

# Packing into byte strings and unpacking from byte strings


"""
The dumps method packs an object into a byte string, and the loads method 
then unpacks back from the byte string into an object. These methods are needed 
when we want to control what to do with a byte representation, such as sending it over the network or receiving it from the network.
"""
print("~" * 30)


# Object to serialize
my_data = {"key": "value", "num": 42}

# Serialization of the object into a byte string
serialized_data = pickle.dumps(my_data)
# Outputs a byte string
print(
    serialized_data
)  # b'\\x80\\x04\\x95\\x1b\\x00\\x00\\x00\\x00\\x00\\x00\\x00}\\x94(\\x8c\\x03key\\x94\ \x8c\\x05value\\x94\\x8c\\x03num\\x94K*u.'

# Deserialization of an object from a byte string
deserialized_data = pickle.loads(serialized_data)
# Outputs the Python output object
print(deserialized_data)  # {'key': 'value', 'num': 42}

print("~" * 30)

# Packing into a file and unpacking from a file


"""
Serialization to a file and deserialization from a file allow you to directly store and restore objects in the file system.
The dump and load methods are responsible for this, packing data into a file and unpacking it from a file, respectively.

Using pickle.dump(data, file) stores the data object in the data.pickle file.
"""

# Object to serialize
my_data = {"key": "value", "num": 100}

folder_path = "example"
file_path = f"{folder_path}/data.pickle.txt"
# Serialization of the object into a file
with open(file_path, "wb") as file:
    pickle.dump(my_data, file)


"""After the code is executed, we will save the **data** dictionary to a file.
Now, if we need this data, we can deserialize the data from this file, for example in another script:
"""

# Deserialize the object from the file
with open(file_path, "rb") as file:
    deserialized_data = pickle.load(file)

# Outputs the Python output object
print(deserialized_data)  # {'key': 'value', 'num': 100}

print("~" * 30)


"""The pickle.load(file) method reads and restores an object from the data.pickle file. 
And we will get a dictionary with the same values in the deserialized_data variable as in the previous example in the data dictionary.
"""


# Working with user classes


"""
You can save objects for later use, but there is an important condition. 
Pickle cannot store the classes and functions themselves, and if you need to 
unpack a packed class object, the class itself must be declared earlier in the code.

We serialize an instance of the Human class:
"""

file_path = f"{folder_path}/instance.pickle.txt"


class Human:
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
with open(file_path, "wb") as file:
    pickle.dump(bob, file)


"""It is important that the Human class is defined in the script that performs 
the deserialization with the same structure and in the same namespace as the script that performed the serialization.
"""


class Human:
    def __init__(self, name):
        self.name = name


with open(file_path, "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)  # Bob

print("~" * 30)

# If the Human class is not specified during deserialization, we will receive an error.


with open(file_path, "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)

print("~" * 30)

"""
The output will be about the impossibility of deserializing the Human class:

Traceback (most recent call last):
   File "E:\\WebDir\\Works\\Python\\python-help-solution\\core_course\\topic8\\ex_pickle\\ex06.py", line 4, in <module>
     loaded_instance = pickle.load(file)
AttributeError: Can't get attribute 'Human' on <module '__main__' from 'E:\\\\WebDir\\\\Works\\\\Python\\\\python-help-solution\\\\core_course\ \\\topic8\\\\ex_pickle\\\\ex06.py'>



We can see that serialization allows you to save the current state of an object for later use, but in what scenarios is it used?


One of the common practices is saving program settings. 
If your application allows users to configure various settings, you can serialize those settings 
to a file and deserialize them the next time the user runs the application.
"""

# Save settings
settings = {"theme": "dark", "language": "ukrainian"}
with open("settings.pickle", "wb") as f:
    pickle.dump(settings, f)

# Loading settings
with open("settings.pickle", "rb") as f:
    loaded_settings = pickle.load(f)


"""
Serialization can also be used to cache complex calculations. Let's imagine that calculations take a long time, 
and sometimes we need to interrupt the execution of calculations.
You can save the results in a serialized form and quickly restore them at the next iteration of calculations.


In web development, pickle is most often used when transferring objects between different parts of a program 
that run as separate processes, or between programs that run on different computers on a network.


Also, sometimes complex data structures do not fit into standard database data types. 
In this case, serialization allows you to convert these structures into byte strings 
that can be stored as text or BLOB (Binary Large Object) in the database."""
