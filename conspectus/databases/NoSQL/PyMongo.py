from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

"""Let's install the Python driver called "PyMongo". There are many drivers written by the community, 
but PyMongo is the official Python driver for MongoDB. Detailed driver documentation can be found here.
"""

# The easiest way to install the driver is through the pip package management system. Run the following in the command line:

command = "python -m pip install pymongo"

# Or with Poetry

command = "poetry add pymongo"


# Creation of documents

"""To create MongoDB documents, the following methods are used: insert_one — to insert one document 
and insert_many — to insert several documents into the collection at once.
"""

client = MongoClient(
    "mongodb+srv://prysiazhnyi:K0kkV2hzS9bu3gZH@cluster0.xak5nml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi("1"),
)

db = client.book

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["walks in slippers", "allows himself to be stroked", "redhead"],
    }
)

print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["goes to the tray", "refuses to be stroked", "gray"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["goes to the tray", "allows himself to be stroked", "white"],
        },
    ]
)
print(result_many.inserted_ids)


"""
Using client.book, we create a book database. The result of executing db.cats.insert_one 
and db.cats.insert_many will be the _id of the inserted documents in the cats collection.

60d24b783733b1ae668d4a77
[ObjectId('60d24b783733b1ae668d4a78'), ObjectId('60d24b783733b1ae668d4a79')]
"""


# Receiving documents

# To retrieve a single document, use the find_one method.

result = db.cats.find_one({"_id": ObjectId("60d24b783733b1ae668d4a77")})
print(result)

# The result is a dictionary of the type:
{
    "_id": ObjectId("60d24b783733b1ae668d4a77"),
    "name": "barsik",
    "age": 3,
    "features": ["walks in slippers", "allows himself to be stroked", "redhead"],
}


# To get several documents, use the find method:
result = db.cats.find({})
for el in result:
    print

# Result:
{
    "_id": ObjectId("60d24b783733b1ae668d4a77"),
    "name": "barsik",
    "age": 3,
    "features": ["walks in slippers", "allows himself to be stroked", "redhead"],
}

{
    "_id": ObjectId("60d24b783733b1ae668d4a78"),
    "name": "Lama",
    "age": 2,
    "features": ["goes to the tray", "refuses to be stroked", "gray"],
}

{
    "_id": ObjectId("60d24b783733b1ae668d4a79"),
    "name": "Liza",
    "age": 4,
    "features": ["goes to the tray", "allows himself to be stroked", "white"],
}


# Updating documents

# To update the document, you can use the update_one method:

db.cats.update_one({"name": "barsik"}, {"$set": {"age": 4}})
result = db.cats.find_one({"name": "barsik"})
print(result)

# Result:
{
    "_id": ObjectId("60d24b783733b1ae668d4a77"),
    "name": "barsik",
    "age": 4,
    "features": ["walks in slippers", "allows himself to be stroked", "redhead"],
}


# Deleting documents

# The delete_one method is used to delete a document from the collection:

db.cats.delete_one({"name": "barsik"})
result = db.cats.find_one({"name": "barsik"})
print(result)

# The result will be the absence of a document in the collection:
None


"""
We used just a few PyMongo methods to interact with our MongoDB cloud server from a Python script.

All available methods can be found in the official PyMongo documentation."""
