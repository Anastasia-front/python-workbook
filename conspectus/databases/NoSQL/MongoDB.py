"""'The basics of working with MongoDB


A modern web application needs data storage. Traditionally, SQL databases were used for this, 
but progress does not stand still and an alternative has appeared in the form of NoSQL databases. 
These databases took the distributed nature of the Internet into account and instead focused on parallelism 
to scale performance. We will look at the leading document-oriented database - MongoDB.

MongoDB is a non-relational NoSQL database. It is based on the document model — data objects are stored as individual documents in a collection."""

# Collection and document


"""
MongoDB data is grouped into collections. A collection is a collection of documents that have the same purpose. 
A collection is similar to a table in an SQL database, but differs in that there is no strict schema for the collection, 
and the documents in the collection can have different structures.


A document is a representation of an information element in a database. They can consist of child documents, 
and this data model is more suitable for web applications. The maximum document size is limited to 16 MB.


MongoDB uses JavaScript and JSON structures as a query language. The choice of query language is explained by the fact 
that MongoDB uses the JSON format to represent documents and output results. Physically, JSON structures are stored in binary BSON format.


Documents (that is, objects) correspond to their own data types in many programming languages. 
Embedded documents and arrays reduce the need for value associations."""


# Primary key.
"""In SQL, you must specify any unique column or combination of columns as the primary key. 
In MongoDB, the primary key is automatically set in the _id field. In fact, the variable _id is an object of type ObjectId.

_id: ObjectId('5f15996fbbde793a107af359')

It contains 12 bytes, each of which is formed in a certain way.

4 is a byte value (5f15996f) representing the seconds since the last entry
3 is a byte value (bbde79) indicating the machine ID
2 is a byte value (3a10) indicating the process identifier
3 is a byte counter (7af359), starting with a random value"""


"""----------------------------------------------------------------------"""
# username:
# prysiazhnyi

# password:
# K0kkV2hzS9bu3gZH

# Install your driver:
# python -m pip install "pymongo[srv]"

# Add your connection string into your application code:
# mongodb+srv://prysiazhnyi:K0kkV2hzS9bu3gZH@cluster0.xak5nml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

"""----------------------------------------------------------------------"""
# Working with data in MongoDB


"""After connecting to the MongoDB cloud database, click on >_MONGOSH - the console will open in which we will work."""

The_first_command_will_be = "use test"

"""Now the test database will be installed as the current one.
"""
# If we want to know which DB is currently in use, we can use the db command:
# db

"""Using the db.stats() command, you can get statistics for the current database, and statistics for a collection (such as cats) like this:
"""
# db.cats.stats()

"""But before you can get statistics from a collection, you need to create the collection.
"""


# Creating a collection
"""
You can use two methods for this:

insertOne: adds one document
insertMany: Inserts multiple documents


Let's create a cats collection with information about cats."""

# Call the console and insert information, for example, about the first cat:
command = """
db.cats.insertOne({
     name: 'Barsik',
     age: 3,
     features: ['walks in slippers', 'allows himself to be stroked', 'redhead'],
})"""

# In the console, we will get a result similar to this:
output = """
{
   acknowledged: true,
   insertedId: ObjectId("6569853470e17dadb1d9d019")
}"""

"""It means that the result has been added to the cats collection. 
By double-clicking on the name of the cats collection in the left menu, we will open a new tab where we will see our record.
"""

# We could also run a query in the console and get that record.
command = "db.getCollection('cats').find({})"
output = """
{
   _id: ObjectId("6569853470e17dadb1d9d019"),
   name: 'Barsik',
   age: 3,
   features: [
     "walks in slippers",
     "allows himself to be stroked",
     'red'
   ]
}"""


# There are some limitations when using key names:

"""
The $ character cannot be the first character in a key name.
The key name cannot contain the dot character.
The name _id is not recommended."""


# We use the insertion of data immediately after four cats:
command = """
db.cats.insertMany([
     {
         name: 'Lama',
         age: 2,
         features: ['goes to the tray', 'refuses to be petted', 'grey'],
     },
     {
         name: 'Liza',
         age: 4,
         features: ['goes to the tray', 'allows himself to be petted', 'white'],
     },
     {
         name: 'Boris',
         age: 12,
         features: ['goes to the tray', 'refuses to be petted', 'grey'],
     },
     {
         name: 'Murzik',
         age: 1,
         features: ['goes to the tray', 'allows himself to be stroked', 'black'],
     },
])"""

# The result of the response will be similar to this one — the unique identifiers of the newly created documents were returned to us.
output = """
{
   acknowledged: true,
   insertedIds: {
     '0': ObjectId("6569863470e17dadb1d9d01a"),
     '1': ObjectId("6569863470e17dadb1d9d01b"),
     '2': ObjectId("6569863470e17dadb1d9d01c"),
     '3': ObjectId("6569863470e17dadb1d9d01d")
   }
}

After this insertion, there should be five documents in our collection."""


# Search the collection

# The find method is used to display documents:
command = "db.cats.find()"
output = """
{
   _id: ObjectId("6569853470e17dadb1d9d019"),
   name: 'Barsik',
   age: 3,
   features: [
     "walks in slippers",
     "allows himself to be stroked",
     'red'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01a"),
   name: 'Lama',
   age: 2,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01b"),
   name: 'Liza',
   age: 4,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'white'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01c"),
   name: 'Boris',
   age: 12,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01d"),
   name: 'Murzik',
   age: 1,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'black'
   ]
}"""


# In MongoDB, you can use conditional constructs in queries using comparison operators:


"""
$eq (equal to)
$gt (more than)
$lt (less than)
$gte (greater than or equal to)
$lte (less than or equal to)
"""

command = "db.cats.find({age: {$lte: 3}, features: 'allows himself to be stroked'})"
output = """{
   _id: ObjectId("6569853470e17dadb1d9d019"),
   name: 'Barsik',
   age: 3,
   features: [
     "walks in slippers",
     "allows himself to be stroked",
     'red'
   ]
}

{
   _id: ObjectId("6569863470e17dadb1d9d01d"),
   name: 'Murzik',
   age: 1,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'black'
   ]
}"""


# Projection
"""Sometimes we don't need all the information from the document, but, for example, certain fields, or, conversely, some fields need to be excluded.
"""

command = "db.cats.find({age: {$lte: 3}, features: 'allows himself to be stroked'}, {name: 0})"
# The result — with the second object in the find function, we excluded the output of the name field.
output = """
{
   _id: ObjectId("6569853470e17dadb1d9d019"),
   age: 3,
   features: [
     "walks in slippers",
     "allows himself to be stroked",
     'red'
   ]
}

{
   _id: ObjectId("6569863470e17dadb1d9d01d"),
   age: 1,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'black'
   ]
}"""


# And we can, on the contrary, leave output of only two necessary fields.
command = """db.cats.find(
     {age: {$lte: 3}, features: 'allows himself to be stroked'},
     {name: 1, age: 1},
)"""
output = """
{
   _id: ObjectId("6569853470e17dadb1d9d019"),
   name: 'Barsik',
   age: 3
}

{
   _id: ObjectId("6569863470e17dadb1d9d01d"),
   name: 'Murzik',
   age: 1
}

It is worth noting that the _id field is always displayed, unless you forcefully prohibit its display _id: 0."""


# Query nested objects


# Let's insert a new document with the owners object field.
command = """db.cats.insertOne({
     name: 'Dariy',
     age: 10,
     features: ['goes to the tray', 'refuses to be petted', 'grey'],
     owners: {name: 'Nata', age: 23, address: 'Poltava'},
})"""


# To search for a nested object, use the dot owners.name.
command = "db.cats.find({'owners.name': 'Nata'})"
output = """{
   _id: ObjectId("656988ac70e17dadb1d9d01e"),
   name: 'Dariy',
   age: 10,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ],
   owners: {
     name: 'Nata',
     age: 23,
     address: 'Poltava'
   }
}"""

"""-----------------------------------------------------------------"""

# Additional query settings


# Sampling limitations

"""To limit the sample, the limit function is used. For example, show the first three documents in the collection.
"""

command = "db.cats.find().limit(3)"
output = """{
   _id: ObjectId("6569853470e17dadb1d9d019"),
   name: 'Barsik',
   age: 3,
   features: [
     "walks in slippers",
     "allows himself to be stroked",
     'red'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01a"),
   name: 'Lama',
   age: 2,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01b"),
   name: 'Liza',
   age: 4,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'white'
   ]
}
"""

# To skip several documents in the sample, use the skip function. For example, skip three documents in the sample.
command = "db.cats.find().skip(3)"
output = """{
   _id: ObjectId("6569863470e17dadb1d9d01c"),
   name: 'Boris',
   age: 12,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01d"),
   name: 'Murzik',
   age: 1,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'black'
   ]
}
{
   _id: ObjectId("656988ac70e17dadb1d9d01e"),
   name: 'Dariy',
   age: 10,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ],
   owners: {
     name: 'Nata',
     age: 23,
     address: 'Poltava'
   }
}
"""


# Sorting

"""Sorting in the sample is done by the sort function, which takes an object with fields to sort, and they take the value 1 for ascending, -1 for descending
"""

command = "db.cats.find().sort({name: 1})"
output = """{
   _id: ObjectId("6569863470e17dadb1d9d01c"),
   name: 'Boris',
   age: 12,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}
{
   _id: ObjectId("656988ac70e17dadb1d9d01e"),
   name: 'Dariy',
   age: 10,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ],
   owners: {
     name: 'Nata',
     age: 23,
     address: 'Poltava'
   }
}

...

{
   _id: ObjectId("6569853470e17dadb1d9d019"),
   name: 'Barsik',
   age: 3,
   features: [
     "walks in slippers",
     "allows himself to be stroked",
     'red'
   ]
}
"""


# Collection length

"""You can use the countDocuments() function to get the number of items in the collection:
"""

command = "db.cats.countDocuments()"
output = 6


# Modifiers

"""The $exists operator allows you to extract only those documents in which a certain key is present or absent.
"""

command = "db.cats.find({owners: {$exists: true}})"
output = """{
   _id: ObjectId("656988ac70e17dadb1d9d01e"),
   name: 'Dariy',
   age: 10,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ],
   owners: {
     name: 'Nata',
     age: 23,
     address: 'Poltava'
   }
}
"""

# The $type operator retrieves only those documents in which a given key has a value of a given type, such as string or number.


command = "db.cats.find({age: {$type: 'number'}})"


# The $regex operator specifies a regular expression that the field value must match.

command = "db.cats.find({name: {$regex: 'L'}})"
output = """{
   _id: ObjectId("6569863470e17dadb1d9d01a"),
   name: 'Lama',
   age: 2,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}

{
   _id: ObjectId("6569863470e17dadb1d9d01b"),
   name: 'Liza',
   age: 4,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'white'
   ]
}
"""

# Logical modifiers

"""The logical multiplication operator $or allows you to combine samples.
"""

command = "db.cats.find({$or: [{name: {$regex: 'L'}}, {age: {$lte: 3}}]})"
output = """{
   _id: ObjectId("6569853470e17dadb1d9d019"),
   name: 'Barsik',
   age: 3,
   features: [
     "walks in slippers",
     "allows himself to be stroked",
     'red'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01a"),
   name: 'Lama',
   age: 2,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01b"),
   name: 'Liza',
   age: 4,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'white'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01d"),
   name: 'Murzik',
   age: 1,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'black'
   ]
}
"""

# The logical multiplication operator $and finds the intersections of samples.


command = "db.cats.find({$and: [{name: {$regex: 'L'}}, {age: {$lte: 3}}]})"
output = """{
   _id: ObjectId("6569863470e17dadb1d9d01a"),
   name: 'Lama',
   age: 2,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}

"""

# Cursors
"""
The result of the selection obtained using the find function is called a cursor. Cursors encapsulate sets of objects obtained from the database.

Using JavaScript language syntax and cursor methods, we can display the received documents on the screen and somehow process them.
"""
command = """const cursor = db.cats.find()
while (cursor.hasNext()) {
     obj = cursor.next()
     print(obj['name'])
}"""
output = """
Barsik
Llama
Liza
Boris
Murzik
Dariy"""


"""---------------------------------------------------------------------"""

# Change of documents


# Updating documents
"""
The updateOne function offers more detailed settings during the update. It accepts three parameters:

filter: accepts a request to select a document to update.
update: provides a document with new information that will replace the old one during an update.
options: defines additional options when updating documents. Can take an upsert argument.


If the upsert parameter is true, then MongoDB will update the document if it is found and create a new one 
if no such document exists. If it is false, then MongoDB will not create a new document if the fetch query does not find any documents.
"""

command = (
    "db.cats.update({name: 'Bars'}, {$set: {name: 'Tom', age: 5}}, {upsert: true})"
)
output = """{
   acknowledged: true,
   insertedId: ObjectId("656994f9224eb3477fb9ae0b"),
   matchedCount: 0,
   modifiedCount: 0,
   upsertedCount: 1
}
"""


# Using the $set operator means that if the document does not contain an updatable field, it is created. Otherwise, the document will be replaced.
command = """db.cats.updateOne(
     {name: 'Tom'},
     {$set: {features: ['goes to the tray', 'refuses to be petted', 'grey']}},
)
"""
output = """{
   acknowledged: true,
   insertedId: null,
   matchedCount: 1,
   modifiedCount: 1,
   upsertedCount: 0
}
"""

# To delete an individual key, the $unset operator is used:
command = "db.cats.updateOne({name: 'Tom'}, {$unset: {age: 1}})"
output = """{
   acknowledged: true,
   insertedId: null,
   matchedCount: 1,
   modifiedCount: 1,
   upsertedCount: 0
}
"""

"""If it is necessary to update all documents that meet some criteria, then the updateMany method is used.
"""

# Deleting a document

"""To delete documents in MongoDB, the deleteOne and deleteMany methods are provided:
"""

# Delete all documents with the specified request.
command = "db.cats.deleteMany({name: 'Tom'})"
output = """{
   acknowledged: true,
   deletedCount: 1
}"""

# If you want to delete only one document
command = "db.cats.deleteOne({name: 'Tom'})"

"""---------------------------------------------------------------------"""

# Work with arrays


"""The $in operator defines an array of possible expressions and searches for those keys whose values are in the array:
"""
command = "db.cats.find({age: {$in: [2, 10]}})"
output = """{
   _id: ObjectId("6569863470e17dadb1d9d01a"),
   name: 'Lama',
   age: 2,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ]
}

{
   _id: ObjectId("656988ac70e17dadb1d9d01e"),
   name: 'Dariy',
   age: 10,
   features: [
     "goes to the tray",
     "doesn't allow himself to be stroked",
     'gray'
   ],
   owners: {
     name: 'Nata',
     age: 23,
     address: 'Poltava'
   }
}
"""

# The $nin operator works in the opposite way — it defines an array of possible expressions and searches for those keys whose value is missing from this array.
command = "db.cats.find({age: {$nin: [2, 10]}})"

# The $all operator is similar to $in: it also defines an array of possible expressions, but requires documents to have the entire set of expressions defined.
command = "db.cats.find({features: {$all: ['goes to the tray', 'gets petted']}})"
output = """{
   _id: ObjectId("6569863470e17dadb1d9d01b"),
   name: 'Liza',
   age: 4,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'white'
   ]
}
{
   _id: ObjectId("6569863470e17dadb1d9d01d"),
   name: 'Murzik',
   age: 1,
   features: [
     "goes to the tray",
     "allows himself to be stroked",
     'black'
   ]
}
"""

# The $size operator is used to find documents in which arrays have the number of elements equal to the $size value.
command = "db.cats.find({features: {$size: 3}})"

# The $push operator adds a value to an array.
command = "db.cats.updateOne({name: 'Barsik'}, {$push: {features: 'stinky'}})"
output = """{
   acknowledged: true,
   insertedId: null,
   matchedCount: 1,
   modifiedCount: 1,
   upsertedCount: 0
}
"""

# If you need to add several values at once:
command = """db.cats.updateOne(
     {name: 'Barsik'},
     {$push: {features: {$each: ['snoring', 'angry']}}},
)
"""
output = """{
   acknowledged: true,
   insertedId: null,
   matchedCount: 1,
   modifiedCount: 1,
   upsertedCount: 0
}
"""

# The $addToSet operator, like the $push operator, adds objects to the array.
# The difference is that $addToSet adds data if it's not already in the array:
command = "db.cats.updateOne({name: 'Lama'}, {$addToSet: {features: 'crazy'}})"
output = """{
   acknowledged: true,
   insertedId: null,
   matchedCount: 1,
   modifiedCount: 1,
   upsertedCount: 0
}"""

# The $pop operator allows you to remove an element from the array:
command = "db.cats.update({name: 'Barsik'}, {$pop: {features: 1}})"


# 1 is the end of the array, -1 is the beginning of the array.

# The $pull operator removes by value.
command = "db.cats.updateOne({name: 'Barsik'}, {$pull: {features: 'redhead'}})"

# And if we want to remove not one value, but several at once, then we can apply the $pullAll operator:
command = "db.cats.updateOne({name: 'Barsik'},{$pullAll: {features: ['refuses to be petted', 'smelly', 'snores']}})"
