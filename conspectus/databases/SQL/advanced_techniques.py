# Advanced techniques for working with data

"""---------------------------------------------------------"""
# Aggregation functions

"""
SQL has many built-in functions to perform various operations. We will consider those that are most often used:

COUNT() — returns the number of rows
SUM() — returns the sum of all fields with numeric values in them
AVG() — returns the average value among rows
MIN()/MAX() — returns the minimum/maximum value among strings"""


# Find the minimum age among users
code = """
SELECT min(age) as minAge
FROM users;"""

# Output:
# minAge
# 23


# Find the average age of users:
code = """
SELECT avg(age) as averageAge
FROM users;"""

# Output:
# averageAge
# 31.666666666666668

"""Let's find the number of contacts of each user using the COUNT function. 
But in the SELECT statement we need to add the GROUP BY user_id line. 
Since the function is aggregated by the user_id field, it is necessary to group the values by name."""


code = """
SELECT COUNT(user_id) as total_contacts, user_id
FROM contacts
GROUP BY user_id;"""

# Output:
# we added two contacts for each user. And there is a contact without a user.


"""---------------------------------------------------------"""

# Nested SELECT queries

"""
So far, we've only looked at simple queries. But it is often necessary to use so-called nested queries or subqueries.

Let it be necessary to display contacts for users under 30 years of age.
"""


# The first request is to find the id of users under 30 years old.
code = """
SELECT id
FROM users
WHERE age < 30;"""


# Then we combine the queries using WHERE:
code = """
SELECT *
FROM contacts
WHERE user_id IN (SELECT id
     FROM users
     WHERE age < 30);"""


"""---------------------------------------------------------"""

# Nicknames

"""In previous examples, we have already used aliases. To alias a column, you can use the AS keyword:
"""

code = """
SELECT id, name as fullName, phone as mobile
FROM contacts;"""

# Aliases are often used when working with related tables.


"""---------------------------------------------------------"""


JOIN = "Joining tables"

"""
In databases, tables are often connected to each other. For example, our users and genders tables 
are related to each other by the gender_id field, and the contacts and users tables are related by the user_id field.

The JOIN operator is used to join tables.

The users table has a gender_id column, in this case it is the so-called foreign key and the connecting link between the two tables. 
If we want to display all information about the user, including information about their gender, we need to connect a second genders table. 
To do this, you can use INNER JOIN, where the join condition is set using ON:
"""

code = """
SELECT u.id, u.name, u.email, g.name AS gender
FROM users AS u
INNER JOIN genders AS g ON g.id = u.gender_id;"""

"""
This is a simple example of using JOIN. There are several more options for its use:

(INNER) JOIN: Returns records whose values match in both tables.
LEFT (OUTER) JOIN: Returns all records from the left table and matching records from the right table.
RIGHT (OUTER) JOIN: Returns all records from the right table and matching records from the left table.
FULL (OUTER) JOIN: Returns all records if there are matches in the left or right table.

By default, the word cannot be written in round brackets, i.e. INNER JOIN and JOIN entries are equivalent.
"""

# Consider a concrete example to understand the difference between INNER JOIN and LEFT JOIN.
code = """
SELECT c.id, c.name, c.email, u.name AS owner
FROM contacts AS c
JOIN users AS u ON u.id = c.user_id;"""

"""In this case, we don't get a contact without a user in the sample because table intersection was used. 
To get all the contacts, even if they don't have owners from the users table, we need to use a LEFT JOIN.
"""

code = """
SELECT c.id, c.name, c.email, u.name AS owner
FROM contacts AS c
LEFT JOIN users AS u ON u.id = c.user_id;"""

# This query appended data from the contacts table that was not matched in the users table.


"""---------------------------------------------------------"""

# Changing and deleting data in a table

UPDATE = "Change of data"
"""
Changing the data in the SQL table is done using the UPDATE command.

The use of UPDATE includes: 
first - selecting the table in which the field we want to change is located, 
second - setting the record to a new value using the SET statement, 
third - using WHERE to mark a specific place in the table.

In the contacts table, we have a record with id = 5, which does not have a user_id field value.
"""

# Let's establish that the owner of this contact will be the user Maksim with id = 3 in the users table.
code = "UPDATE contacts SET user_id = 3 WHERE id = 5;"


DELETE = "Delete records from the table"
"""Deleting a record from a table using SQL is also a simple operation. 
The main thing is to mark with WHERE exactly what we want to delete. 
Otherwise, we will delete all records from the table, which we would like to avoid.
"""

code = "DELETE FROM contacts WHERE id = 4;"


# Deleting tables
"""If we want to delete all data from the table, but at the same time leave the table itself, 
we should use the TRUNCATE command:
"""

code = "TRUNCATE TABLE contacts;"

# If we want to delete the table itself , then we should use the DROP command:
code = "DROP TABLE contacts;"


# Modification of tables
"""
Most often, you need to change the initial scheme of the table. 
You've created a table, it lives a life of its own, but then you need to either change the column type, 
add a new column, delete a column, etc. Here we need the ALTER statement.

Let's analyze the main types of requests.
"""

# Rename the column column_a to the column column_b and set it to INTEGER type:
code = "ALTER TABLE table_name CHANGE column_a column_b INTEGER;"

# Change only the type of the column column_b in the table table_name:
code = "ALTER TABLE table_name MODIFY column_b BIGINT NOT NULL;"

# Add column column_c with type FLOAT to table table_name:
code = "ALTER TABLE table_name ADD column_c FLOAT;"

# Add column column_d with type VARCHAR after column_c to table table_name:
code = "ALTER TABLE table_name ADD column_d VARCHAR(30) AFTER column_c;"

# Add a column_f of type CHAR and make it the first:
code = "ALTER TABLE table_name ADD column_f CHAR(10) FIRST;"

# Delete column column_c in table table_name:
code = "ALTER TABLE table_name DROP COLUMN column_c;"

# Add an index with the name index_name_ix for the column column_b
code = "ALTER TABLE table_name ADD INDEX index_name_ix (column_b);"
