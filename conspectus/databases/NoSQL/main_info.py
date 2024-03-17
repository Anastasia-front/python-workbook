"""Relational databases (RBD - Relational Database) have a number of unpleasant features:

- relational databases do not scale well, it is very difficult to create distributed storage with them;

- designing large databases with many components requires considerable effort. This is the reduction of entities 
to normal forms and complexity in the display of many-to-many relationships. 
Such schemes are difficult to read and understand their business application;

- the evolution of the data schema almost always lags behind new business needs. 
It often becomes outdated even before the release of a new feature. 
Migration to the updated scheme takes long hours, during which the server is "down".


A feature (from the English feature — peculiarity, unusual property) is a certain detail or part of a product 
that has specific characteristics. Mechanisms that allow adding new functionality, web parts, and design elements to a product are also called features.


The reasons for this behavior of RBD are to implement ACID principles:

Atomicity — Атомарність ensures that no transaction will be partially committed to the system. 
Either its sub-operations will be executed, or none will be executed. Since in practice it is impossible 
to simultaneously and atomically perform the entire sequence of operations within a transaction, 
the concept of "rollback" is introduced: if the transaction cannot be completely completed, 
the results of all its actions so far will be canceled and the system will return to the "external initial" state 
- from the it will appear that there was no transaction. Of course, counters, indexes and other internal structures can change, 
but if the DBMS is programmed without errors, this will not affect its external behavior.

Consistency — Узгодженість. A transaction that reaches its normal end (EOT — end of transaction) and thereby commits its results 
preserves database consistency. In other words, each successful transaction by definition commits only valid results. 
This condition is necessary to support the fourth property.

Isolation — Ізольованість. During the execution of a transaction, parallel transactions should not affect its result. 
Isolation is a valuable requirement, so in real databases there are modes that do not completely isolate the transaction (Repeatable Read isolation levels and below).

Durability — Довговічність. Regardless of lower-level problems (such as system power outages or hardware failures), 
changes made by a successfully completed transaction should persist after the system returns to service. 
In other words, if the user has received confirmation from the system that the transaction has been completed,
 he can be sure that the changes made by him will not be reversed due to any failure.


What to do if you need to implement a cluster and distribute the database to physically separated machines?"""

# CAP theorem


"""
Any data store has three basic properties:



- Data consistency (Узгодженість). That is, the data must be complete and consistent (including in all nodes of the cluster).

- Availability (Доступність). Roughly speaking, this is the speed of the server's response to our request (for writing or reading).

- Partition tolerance (Стійкість до поділу ). This means that if the system is divided into several parts, each of them, if available, 
should be able to work autonomously, giving correct feedback and providing its data. The disconnection in the cluster should not affect the final work.


The CAP theorem tells us that out of these three components we can get only two.


Relational databases implement CA-combination and are partition-insensitive.



NoSQL technologies were created in order to solve the problem of resistance to division, that is, to work efficiently on clusters. 
The relational model is not able to cope with this task, because it was created for other purposes and other conditions. 
You will not be able to "just saw off a couple of tables or calmly move them to a neighboring cluster."


NoSQL stores, by their very nature, can be easily clustered due to their specific data storage structure.

The true essence of the CAP theorem is manifested precisely in the conditions of a distributed system. 
It is obvious that creating a cluster that is unstable to division is devoid of practical benefit. 
That is, a priori cluster should be created resistant to division. Understanding this fact allows us to see the CAP theorem 
in a new light: from consistency and availability, one can choose only one thing, or use a reasonable compromise between these two points 
(rather than three, as one might think from the original definition).

The second task that the ideologues of NoSQL technologies are trying to solve is to increase availability, 
that is, to get a quick response from the server.
"""


# Types of NoSQL databases

# Key-value/Key-cache
"""The database is, in fact, a dictionary with unique keys by which values are searched. 
The search takes place in constant time O(n). The value can be anything: Memcached cache, Redis structured data, etc.
"""

# Document Store
"""Each line (record) in the database is a structured document with a standardized or different set of fields. 
The representative of what type of database is MongoDB.
"""

# Graph
"""A type of database with the implementation of a network model in the form of a graph and its generalizations. 
The main elements of the model are nodes and links. Graph databases are used for modeling social graphs (social networks),
 in bioinformatics, and also for the semantic web. A representative of this type of database is Neo4j.
"""

# Object Db
"""A database in which data is modeled as objects, their attributes, methods, and classes. 
Object-oriented databases are usually recommended for those cases where high-performance 
processing of data with a complex structure is required. Representative — Realm.
"""

# Wide Column Store
'''The same as an RDb database in the sense of using tables containing rows (records) and columns, 
but the data type in one column is not necessarily the same for all records. In some sense, 
you can imagine such a table as a two-dimensional dictionary. 
Representatives — Amazon DynamoDB, Apache Accumulo, Apache Cassandra."""
'''
