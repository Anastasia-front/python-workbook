"""These are actually indexes. In most cases, when making restrictions, the server itself creates an index without our intervention.
"""

# Let's analyze what the main limitations are:


"""
PRIMARY KEY — primary key (pk).
UNIQUE KEY is a unique key that has all the properties of a primary key, but is not primary at the same time.
FOREIGN KEY — foreign key (fk). For us it is a connection with another table, and for the server it is a constraint.
"""

# Let's analyze them separately.

# PRIMARY KEY


"""
When we created the tables, we used a PRIMART KEY, it was an index, like all constraints. 
When we say PRIMART KEY to the server, we are restricting the primary key, that is, 
we are telling the server that it must be checked for uniqueness.

A primary key is a column by which we can always find a record. For example, 
if it is autoincremented, then it guarantees that if a record has an id of 10, 
then there will definitely be no more records with an id of 10. 
The main rule is that the primary key must be unique and eternal.
"""

# It is usually created when the table is described. But if we want to add a primary key to a table
# where it is not there for some reason, then:


"""ALTER TABLE table1 ADD CONSTRAINT table1_id_pk PRIMARY KEY (id);
"""


# If we want to delete the primary key:


"""ALTER TABLE table1 DROP PRIMARY KEY;
"""


# If the field is AUTO_INCREMENT, then deleting the primary key will not work.
# The PRIMARY KEY name must have the suffix pk: table1_id_pk or pk_table1_id.
