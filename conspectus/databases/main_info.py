database = """an organized collection of data created for convenient access, 
management and updating of information. It is stored and managed using special software. 
Computer databases typically store aggregations of records or files that contain information 
such as sales transactions, customer data, financial information, and product information.
    
There are many types of databases that can be classified based on the type of content:
bibliographic, full-text, numerical, and image. In computer science, databases are often 
classified based on the organizational approach they use.

Here are some of the more common types of databases:"""

# 1.
Relational_databases = """use a relational model, data is stored in tables with rows and columns.
MySQL
PostgreSQL
Oracle Database
Microsoft SQL Server
SQLite"""

# 2.
Document_oriented_databases = """data is stored in a document-like format like JSON.
MongoDB
CouchDB"""

# 3.
Key_value_databases = """use a simple key to a unique identifier to track values in a database.
Redis
Amazon DynamoDB
Berkeley DB"""

# 4.
NoSQL_databases_with_a_wide_column = """optimized for queries on large volumes of data, distributed over a large number of columns.
Cassandra
HBase
Google Bigtable"""

# 5.
Graph_databases = """use graph structures for semantic queries with nodes, edges, and properties.
Neo4j
ArangoDB"""


DBMS = """a database management system is a comprehensive software program that provides the ability to create, modify, manage,
and interact with a database. A DBMS allows users and other programs to work with data through queries, 
providing tools for organizing, storing, and retrieving information.

The main functions of the DBMS include:

Data storage: Efficient storage of data in a structured format.
Data Manipulation: Support for insert, update, delete and search data operations.
Transaction management: Ensuring data integrity through transaction mechanisms 
    that allow multiple operations to be executed as a unit of work.
Access Control: Manage user access rights and roles to ensure data security.
Query language support: For example, SQL, which allows you to formulate complex queries to the database.
Backup and recovery support: Functions for creating backup copies of data and restoring them after failures.

DBMS can be relational (RDBMS), non-relational (NoSQL), object-oriented, and others, depending on the data organization model they use. 
Each model offers specific advantages for specific types of applications and requirements.
DBMS are important tools for efficient data storage, management, and access. 
They allow you to organize the data structure, perform various operations, guarantee the security and integrity of information.
"""

MySQL = """is one of the most popular relational database management systems. 
It is an open source solution that began as a component of the LAMP stack (Linux, Apache, MySQL, Perl/PHP/Python). 
MySQL is easy to use, highly compatible with web applications, and supported by popular cloud platforms."""

PostgreSQL = """is also an open source object-relational database management system. 
It offers advanced functionality and compliance with SQL standards. PostgreSQL features flexibility, 
geographic data support, and extensions to work with JSON and other non-relational data types."""

Oracle = """is one of the leading commercial relational database management systems. 
It has high reliability, scalability and performance. Oracle provides advanced data management capabilities, 
including transaction support, high security, and distributed computing."""

Microsoft_SQL_Server = """is a database management system developed by Microsoft. 
It provides a wide range of features, including high performance, scalability and business intelligence tools. 
MSSQL integrates well with other Microsoft products and supports cloud solutions."""

MongoDB = """is a document-oriented database management system that does not need to describe the table schema. 
It stores data in the form of flexible JSON documents, which allows you to quickly and flexibly change the data structure. 
MongoDB supports horizontal scaling and high speed data access."""

Redis = """is one of the most popular open key-value data management systems that provides 
fast in-memory data access and processing. It is used for caching data, saving user sessions, 
implementing queues, supporting distributed systems, and many other scenarios where speed and reliability are important.
"""
