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

# username:
# prysiazhnyi

# password:
# K0kkV2hzS9bu3gZH

# Install your driver:
# python -m pip install "pymongo[srv]"

# Add your connection string into your application code:
# mongodb+srv://prysiazhnyi:K0kkV2hzS9bu3gZH@cluster0.xak5nml.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0