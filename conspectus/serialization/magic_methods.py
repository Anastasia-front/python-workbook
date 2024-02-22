import pickle

"""
Recall that serialization is the process of converting an object into a stream of bytes for storage or transmission. 
Deserialization is the reverse process where a stream of bytes is converted back into an object. 
But not all Python objects can be serialized. For example, you cannot serialize a file handle or a system resource. 
Then what to do when there is a class, an object that needs to be packaged using pickle, but it has non-serializable attributes? 
In such a situation, you can use magic methods that manage serialization and deserialization using pickle.

Python's __getstate__ and __setstate__ methods allow us to control how an object 
should be serialized and deserialized by the pickle module.

When pickle.dump() or pickle.dumps() is called to serialize an object, 
Python looks for a __getstate__ method in the object's class. 
If the method exists, it is used to get the state of the object to be serialized. 
When deserializing, using pickle.load() or pickle.loads(), 
Python looks for the __setstate__ method in the class. 
If the method exists, it is used to restore the state of the object 
from the data obtained during deserialization.


Let's say we have a Robot class that contains information about a robot, 
but we want to serialize only certain attributes.
"""
print("~" * 30)

class Robot:
    def __init__(self, name, battery_life):
        self.name = name
        self.battery_life = battery_life
        # We are not going to serialize this attribute
        self.is_active = False

    def __getstate__(self):
        state = self.__dict__
        # Remove is_active from the serialized state
        del state["is_active"]
        return state

    def __setstate__(self, state):
        # Restore the object during deserialization
        self.__dict__.update(state)
        # Set the default is_active value
        self.is_active = False


# Creation of the Robot object
robot = Robot("Robot1", 100)

# Object serialization
serialized_robot = pickle.dumps(robot)

# Object deserialization
deserialized_robot = pickle.loads(serialized_robot)

print(
    deserialized_robot.__dict__
)  # {'name': 'Robot1', 'battery_life': 100, 'is_active': False}

print("~" * 30)

"""
This is a rather artificial example where __getstate__ modifies the state of the object 
before serialization by removing the is_active attribute because we decided that this attribute 
does not need to be stored. The __setstate__ method restores the object's state on deserialization 
by setting is_active back to its default value because this attribute was not saved.

For these operations, we use self.__dict__, which is a special attribute of an object 
that contains a dictionary of all the attributes that belong to that object. 
The keys in this dictionary correspond to attribute names, and the values 
are the corresponding values of those attributes. When we create a new instance of a class, 
Python automatically creates a __dict__ dictionary for that instance to store all the attributes that are added to that object.

Let's explain with a simple example, we have a simple class:
"""


class Example:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# When we instantiate this class:


obj = Example("Rim", 30)

# Then obj.__dict__ will contain:

{"name": "Rim", "age": 30}

# We can dynamically add, remove or change attributes:

obj.__dict__["city"] = "Poltava"  # Adding a new attribute
print(obj.city)  # Output: Poltava

del obj.__dict__["age"]  # Remove the age attribute
print(obj.__dict__)  # Output: {'name': 'Rim', 'city': 'Poltava'}

print("~" * 30)

"""
However, this should be done very carefully, as careless changes can lead to unpredictable behavior 
of the object. In our example, we use self.__dict__ to copy all attributes of the Robot object 
when implementing the __getstate__ and __setstate__ methods, which allows you to save and restore 
the state of the object when working with the pickle module.

More practically, this technique is used for objects containing unserialized attributes, 
such as open files or database connections. Consider the following example, which defines a Reader class 
to read data from a file. The class is simple, with methods to initialize and close the file handle, 
and a method to read the contents of the file.
"""


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

folder_path = "example"
file_path = f"{folder_path}/data.txt"

if __name__ == "__main__":
    reader = Reader(file_path)
    data = reader.read()
    print(data)
    reader.close()

print("~" * 30)

"""
If you create a text file "data.txt", for example with a line of text "Message from file", 
then the output will be as follows:

Message from file


However, there is an important caveat to using this class with serialization libraries such as pickle. 
If we want to serialize our reader object, we will get an error.
"""


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

reader_file_path = f"{folder_path}/reader.pkl"


if __name__ == "__main__":
    reader = Reader(file_path)
    # An example of serialization of the Reader object
    # with open(reader_file_path, "wb") as f:
        # pickle.dump(reader, f) - will occur an error


"""
Attempting to serialize an instance of the Reader class with pickle 
throws an error because the file handle self.fh cannot be serialized. 
It occurs because file descriptors are not serializable by pickle due to 
their dependency on external system resources that pickle cannot save and restore.

Traceback (most recent call last):
  File "/Users/Anastasia/Desktop/python-workbook/conspectus/serialization/magic_methods.py", line 167, in <module>
    pickle.dump(reader, f)
TypeError: cannot pickle '_io.TextIOWrapper' object

In order to make instances of the Reader class serializable, we need to implement 
the __getstate__ and __setstate__ methods and control the pickle behavior of the class. 
This will allow us to explicitly define which part of the object should be serialized and how the object should be restored.

In the following example, the Reader class can be serialized and errors due to the inability
to pack the file descriptor will no longer occur.
"""


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(self.filename, "r", encoding="utf-8")

    def close(self):
        self.fh.close()

    def read(self):
        data = self.fh.read()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__, "fh": None}
        return attributes

    def __setstate__(self, state):
        # We restore the state of the object
        self.__dict__ = state
        self.fh = open(state["filename"], "r", encoding="utf-8")


if __name__ == "__main__":
    reader = Reader(file_path)
    data = reader.read()
    print(data)
    reader.close()

    # An example of serialization of the Reader object
    with open(reader_file_path, "wb") as f:
        pickle.dump(reader, f)

    # Example of deserialization of the Reader object
    with open(reader_file_path, "rb") as f:
        loaded_reader = pickle.load(f)
        print(loaded_reader.read())
        loaded_reader.close()

print("~" * 30)

"""
In this modified version, the __getstate__ method creates a copy of the object attribute dictionary 
from self.__dict__, but replaces fh with None to avoid trying to serialize the open file descriptor.

The file descriptor self.fh is not included in the state because it cannot be serialized.


The __setstate__ method restores the state of the object from the state it received during deserialization 
and opens the file again using the saved filename.


This allows us to access the contents of the file again after deserialization.

In general, our implementation effectively solves the problem with the impossibility 
of serializing file descriptors and allows you to safely store and restore the state of objects working with files.
"""
