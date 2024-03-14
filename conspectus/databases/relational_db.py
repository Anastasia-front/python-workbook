"""
This tabular approach defines data in such a way that it can be reorganized and accessed in different ways. 
Relational databases consist of tables in which data are placed in predefined categories. 
Each table has columns with at least one category of data and rows that have a specific 
instance of data for the categories defined in the columns. Such databases are indexed 
to facilitate searching using the SQL or NoSQL query language.

Relational databases use SQL in their interface to users and software applications. 
A new category of data can be easily added to a relational database without the need to modify existing applications. 
A relational database management system (RDBMS) is used to store, manage, query, and retrieve data in a relational database.


Typically, an RDBMS provides users with the ability to control read/write access, 
define report generation, and analyze usage. Some databases offer compliance with 
ACID (atomicity, persistence, isolation, and completeness, which guarantees data consistency and transaction completeness).


As already mentioned, the relational model of databases is based on the concept of tables called "relations", 
columns and rows. Each relation consists of a set of records that contain information about a certain group of entities.


You can think of a table as something similar to a spreadsheet, where the columns represent attributes (characteristics) 
of the data and the rows represent specific records or tuples of data. Each column has a name and a data type
that defines the valid format of the values.



One of the main principles of the relational model is the ability to establish relationships between tables. 
This is done using keys. Each relation has one or more attributes that act as keys. Keys are used to identify 
unique records in a table and establish relationships between different tables. Connections between relations 
are defined using common attributes that contain the same values in the corresponding records of different tables.
"""

PostgreSQL = """a high-performance, stable, object-relational DBMS. It is open source and supports a rich set of data types, 
including JSON, XML, and geospatial data (PostGIS). It uses a client-server model where the server manages the databases 
and the clients make requests to the server. This architecture allows you to distribute the load and provides flexibility in managing data access.

DBMS supports complex SQL queries, transactions, ensures data integrity and has advanced security capabilities.
The DBMS also supports extensions, allowing users to add new features. PostgreSQL is widely used in large projects 
and enterprise applications due to its reliability, flexibility and compliance with SQL standards.


Among the advantages of PostgreSQL are high performance, scalability, open source code, and an active community. 
Disadvantages may include relative complexity of management compared to some other DBMS.


Installing PostgreSQL involves downloading and installing the software, creating a database, 
and configuring settings to optimize performance and security. But we will use Docker to run the postgres database. 
This is an easier way for a beginner. In the command line, you need to execute the following command:


docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mySecretPassword -d postgres


Instead of some-postgres, choose your container name, and instead of mySecretPassword, come up with your database connection password."""

SQLite = """is a lightweight relational database management system. SQLite is an embedded file system database management system 
that is often used in mobile applications, web browsers, and thin client applications.
Unlike server DBMS, such as PostgreSQL, SQLite stores all data in one file and does not require a separate server process for its operation. 
This makes SQLite an ideal choice for applications that require a simple, reliable, and lightweight local database.

Connecting to an SQLite database is much easier. Basically, this is a local file that needs to be created.

In terms of functionality, SQLite supports most of the basic SQL operations 
and offers a minimalistic design with a small binary file size. 
It's great for scenarios where simplicity and efficiency are needed, 
but doesn't have built-in tools for managing network connections or multi-user access."""

conclusion = """This contrasts with PostgreSQL, which is a more powerful system that supports complex queries, advanced optimization, 
and a variety of data types. PostgreSQL is also better suited for large and complex applications, offering high scalability and flexibility.


SQLite does not require a lot of management or complex configuration, making it ideal for rapid deployment. 
It is often built right into applications, providing easy integration. In contrast, PostgreSQL requires more careful planning 
for installation, configuration, and maintenance. PostgreSQL also has advanced support for network protocols 
and security capabilities that are necessary for more complex enterprise solutions.


Ultimately, the choice between SQLite and PostgreSQL depends on the specific needs of the application 
and the level of complexity required from the database management system. SQLite is great for lightweight applications 
that require simplicity and reliability, while PostgreSQL is better suited for large-scale, feature-rich systems 
that require higher performance and flexibility."""
