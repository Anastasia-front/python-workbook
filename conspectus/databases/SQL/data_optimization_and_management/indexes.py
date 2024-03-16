"""Databases are focused on modification operations, especially the INSERT statement. 
Therefore, the sampling process takes a long time. And that's the problem with databases on any server. 
To solve this problem, indexes were invented, indexes are an attempt to avoid simply going through the records in the database.

In our database, in the users table, different users are recorded in the fullname column, and they are not sorted.

fullname
Alice
Boris
John
Steve

If we try to find Steve, it will be an iterative, and the searched user will be the fourth one. """

# Let's add an index to the fullname field.


"""CREATE INDEX fullname_ix ON users (fullname);"""


"""
Now the data selection is accelerated many times by the fullname field, but the record is slowed down, 
because when adding a record, you need to enumerate the index tree and sort the data. In addition, 
it should be taken into account that the size of the database will also increase significantly and 
only one index works for one request to the table.


Indexes should be added wisely, it is not necessary to add indexes to all fields. 
The index itself is created in three ways."""


# The first is when creating a table.


"""
CREATE TABLE table1
(
     id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'Product code',
     code char(4) NOT NULL DEFAULT 'AAAA',
     name VARCHAR(50) NOT NULL DEFAULT '' COMMENT 'Product name',
     description TEXT NOT NULL DEFAULT '' COMMENT 'Product description',
     price FLOAT NOT NULL DEFAULT 0 COMMENT 'Product price',
     CONSTRAINT table1_id_pk PRIMARY KEY (id),
     INDEX table1_name_ix(name),
     INDEX table1_price_ix(price)
) COMMENT 'Table of goods with keys and indexes';



In this query, we created an index named table1_name_ix on the name column 
and an index table1_price_ix on the price column."""


# The second way is by changing the table using the ALTER statement:
"""ALTER TABLE table1 ADD INDEX table1_name_ix(name), ADD INDEX table1_price_ix(price);
"""


# And the last, third way is to add an index through the CREATE statement:
"""CREATE INDEX table1_name_ix ON table1 (name);
"""

# We can also create composite indexes:
"""CREATE INDEX table1_name_price_ix ON table1 (name, price);
"""


"""Compound indexes are needed if we often search by several fields, 
for example, we have an online store, and we notice that there is often a search by the name 
of a product whose price is greater than 5000, then we make a compound index on the name product 
and price, and now the selection for such a request will be almost instantaneous.
"""


# To drop an index, you need to execute the DROP statement:
"""DROP INDEX table1_price_ix ON table1;
"""


"""There are small naming rules, they are not particularly strict and may differ in different companies. 
The postscript ix can be at the beginning or at the end of the index name. An example in camel notation 
is ixPrice or priceIx. It can also be due to underlining ix_price or price_ix. 
It is considered a good tone to specify a table in the name of the index, for MySQL it is not critical, 
but for databases such as PostgreSQL it is mandatory. ix_table1_price or table1_price_ix specifying 
a table in the index name makes it easier to understand which table 
this index is from when optimizing complex queries.
"""
