"""Foreign key. We have already used it, and it is needed to connect two tables.
"""

# We create a parent table:

"""
CREATE TABLE genders (
   id INT PRIMARY KEY,
   name VARCHAR(30),
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

# And a child:

"""CREATE TABLE users (
   id INT PRIMARY KEY,
   name VARCHAR(30),
   email VARCHAR(30),
   password VARCHAR(30),
   age TINYINT UNSIGNED,
   gender_id INT,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (gender_id) REFERENCES genders (id)
         ON DELETE SET NULL
         ON UPDATE CASCADE
);"""


# You need to remember the main principles:


"""Always rely on the pk primary key or unique key when creating a FOREIGN KEY.
The column responsible for the connection must be of the same type as the parent column. 
In our case, both gender_id and id from the genders table have the same INT type.


If you write ON DELETE CASCADE, it means that if you delete a record in genders, 
all related records will be deleted in users. Is optional. If we do not want the field 
to be deleted with the parent, we set ON DELETE SET NULL, then when deleting we will set 
the gender_id field to NULL. You can not specify it at all, but then we will receive an error 
when deleting, it will be necessary to first delete records from the child table, and then 
from the parent table, sometimes this behavior is required.

You can also specify ON UPDATE CASCADE, this will mean that when the key is changed in the parent table, 
it will also change in the child table, the operation is extremely rare and is often simply skipped 
when defining the key.


The foreign key is needed so that we know exactly which table is being used. 
If we try to add a primary key from another table to a column for the connection of tables, 
which should not be there, without restrictions, we will not even know that we made a mistake.

The name of the FOREIGN KEY must have the suffix fk: children_parentId_fk or fk_children_parentId.
"""
