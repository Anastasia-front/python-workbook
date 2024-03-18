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
        "name": "Bar",
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
    "name": "Bar",
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
    "name": "Bar",
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

db.cats.update_one({"name": "Bar"}, {"$set": {"age": 4}})
result = db.cats.find_one({"name": "Bar"})
print(result)

# Result:
{
    "_id": ObjectId("60d24b783733b1ae668d4a77"),
    "name": "Bar",
    "age": 4,
    "features": ["walks in slippers", "allows himself to be stroked", "redhead"],
}


# Deleting documents

# The delete_one method is used to delete a document from the collection:

db.cats.delete_one({"name": "Bar"})
result = db.cats.find_one({"name": "Bar"})
print(result)

# The result will be the absence of a document in the collection:
None


"""
We used just a few PyMongo methods to interact with our MongoDB cloud server from a Python script.

All available methods can be found in the official PyMongo documentation."""


# EXAMPLE OF main.py

# from pymongo import MongoClient
# from pymongo.server_api import ServerApi


# Connect to the MongoDB server
def connect_to_mongodb():
    client = MongoClient(
        "mongodb+srv://prysiazhnyi:K0kkV2hzS9bu3gZH@cluster0.xak5nml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        server_api=ServerApi("1"),
    )
    return client.book


"""-------------------------------------------------------------------------------"""


# Insert a new document into the collection
def insert_cat(db):
    result = db.cats.insert_one(
        {
            "name": "Moon",
            "age": 3,
            "features": [
                "walks in slippers",
                "allows himself to be stroked",
                "redhead",
            ],
        }
    )
    return result.inserted_id


"""-------------------------------------------------------------------------------"""


# Find a cat document by its name
def find_cat_by_name(db, cat_name):
    result = db.cats.find_one({"name": cat_name})
    return result


# Find all documents in the collection
def find_all_cats(db):
    result = db.cats.find({})
    return result


"""-------------------------------------------------------------------------------"""


# Update the age of a cat document
def update_cat_age(db, cat_name, new_age):
    db.cats.update_one({"name": cat_name}, {"$set": {"age": new_age}})


"""-------------------------------------------------------------------------------"""


# Add a new feature to the list of features for a cat by its name
def add_feature_to_cat(db, cat_name, new_feature):
    # Find the cat document by its name
    cat = db.cats.find_one({"name": cat_name})

    # If the cat is found
    if cat:
        # Add the new feature to the list of features
        cat["features"].append(new_feature)

        # Update the cat document with the new feature
        db.cats.update_one({"_id": cat["_id"]}, {"$set": {"features": cat["features"]}})

        return True  # Return True to indicate success
    else:
        return False  # Return False if the cat is not found


"""-------------------------------------------------------------------------------"""


# Delete a cat document by its name
def delete_cat_by_name(db, cat_name):
    db.cats.delete_one({"name": cat_name})


# Delete all documents from a collection
def delete_all_documents(db, collection_name):
    # Get the collection object
    collection = db[collection_name]

    # Delete all documents from the collection
    result = collection.delete_many({})

    # Return the number of deleted documents
    return result.deleted_count


"""-------------------------------------------------------------------------------"""


# Main function to execute the operations
def main():
    # Connect to MongoDB
    db = connect_to_mongodb()

    # Insert a new cat document
    inserted_id = insert_cat(db)
    print("Inserted cat document ID:", inserted_id)

    # Find a cat document by name
    cat_name = "Moon"
    cat = find_cat_by_name(db, cat_name)
    print("Found cat by name:", cat)

    # Find all cat documents
    all_cats = find_all_cats(db)
    print("All cat documents:")
    for cat in all_cats:
        print(cat)

    # Update the age of a cat document
    new_age = 4
    update_cat_age(db, cat_name, new_age)
    print("Updated cat age to", new_age)

    # Add a new feature to the list of features for a cat by its name
    new_feature = "likes to nap in the sun"
    add_feature_to_cat(db, cat_name, new_feature)
    print("Added new feature to cat:", new_feature)

    # Delete a cat document by name
    delete_cat_by_name(db, cat_name)
    print("Deleted cat by name:", cat_name)

    # Delete all documents from the collection
    collection_name = "cats"
    deleted_count = delete_all_documents(db, collection_name)
    print("Deleted all documents from the collection. Total count:", deleted_count)


if __name__ == "__main__":
    main()


# output:
# Inserted cat document ID: 65f83e5fc150417a35c430c9
# Found cat by name: {'_id': ObjectId('65f83e5fc150417a35c430c9'), 'name': 'Moon', 'age': 3, 'features': ['walks in slippers', 'allows himself to be stroked', 'redhead']}
# All cat documents:
# {'_id': ObjectId('65f83e5fc150417a35c430c9'), 'name': 'Moon', 'age': 3, 'features': ['walks in slippers', 'allows himself to be stroked', 'redhead']}
# Updated cat age to 4
# Added new feature to cat: likes to nap in the sun
# Deleted cat by name: Moon
# Deleted all documents from the collection. Total count: 0
