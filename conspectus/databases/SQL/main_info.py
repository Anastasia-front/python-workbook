SQL = """a programming language designed to manage data stored in a relational database management system.

SQL is a language that allows us to interact with databases. With the help of SQL, we can retrieve data, create and modify tables, 
establish relationships between data, aggregate and analyze information, and much more.

SQL (Structured Query Language) stands for Structured Query Language.

SQL consists of three main components:

data definition languages (Data Definition Language — DDL);
data manipulation language (Data Manipulation Language — DML);
data control language (Data Control Language — DCL)."""


DDL = """Data Definition Language is used to create and modify the schema. For example, the CREATE TABLE statement allows you to create 
a new table in the database, and the ALTER TABLE statement changes the structure of an existing table."""

DML = """Data Manipulation Language provides constructs for querying data, such as the SELECT statement, 
and updating data, such as the INSERT, UPDATE, and DELETE statements."""

DCL = """The Data Control Language consists of statements related to user authorization and security, such as the GRANT and REVOKE statements."""

# The SQL standard

"""
SQL was one of the first commercial database languages since 1970. Since then, various database vendors have implemented SQL in their products 
with some variations. To achieve greater consistency among vendors, the American Standards Institute (ANSI) published the first SQL standard in 1986.

ANSI then updated the SQL standard in 1992, known as SQL92 and SQL2, and in 1999 as SQL99 and SQL3. 
Each time, ANSI added new functions and commands to the SQL language.

The SQL standard is now supported by both ANSI and the International Organization for Standardization as ISO/IEC 9075. 
The latest edition of the standard is SQL:2011.

It formalizes the syntactic structures and behavior of SQL in database products. 
This is especially important for open source databases such as MySQL and PostgreSQL, 
where RDBMSs are developed primarily by communities rather than large corporations."""

# Below are the most popular SQL dialects:

PL_SQL = """PL/SQLstands for SQL Procedural Language. It is developed by Oracle for the Oracle database."""
T_SQL = """Transact-SQL was developed by Microsoft for Microsoft SQL Server."""
PL_pgSQL = """PL/pgSQL stands for PostgreSQL Procedural Language, which consists of a dialect of SQL 
and extensions that are implemented in PostgreSQL."""
MySQL = """has its own procedural language since version 5."""


# Note that MySQL was acquired by Oracle.

"""
Because SQL was designed specifically for non-technical people, it is very simple and easy to understand. 
To write an SQL statement, you simply have to say WHAT you want, NOT HOW you want it—unlike how it's implemented 
in other imperative languages like PHP, Java, and C++.

SQL is a user-friendly language because it is designed primarily for performing ad hoc queries and generating reports.

SQL is now used by highly skilled professionals such as data analysts, data scientists, developers, and database administrators."""

# Basic SQL terms

key = """is a unique field that uniquely identifies a record."""
Primary_key = """is a unique key that is not repeated in the table."""
Foreign_key = """is a reference to a unique key that is NOT REPEATED in its table."""

# Possible relationships between database tables:

one_to_one = """the tables are related to each other when one row (record) of table A corresponds to one row of table B, 
and one record of table B corresponds to one record of table A"""
one_to_many = """this relationship in relational databases is implemented when one row in table A 
can belong to or correspond to several records in table B, but records from table B can correspond to 
only one record in table A. Example: a user can have several phone numbers numbers"""
many_to_many = """is implemented in the case when several records from table A can correspond to several records from table B, 
and at the same time several records from table B correspond to several records from table A"""
many_to_one = (
    """is the reverse of one-to-many, only now tables A and B need to be swapped"""
)

Normalization = """is the process of bringing the database structure to a form that provides minimal logical redundancy 
and does not aim to decrease or increase performance or decrease or increase the physical volume of the database. 
The ultimate goal of normalization is to reduce the potential inconsistency of information stored in the database."""

# Basic SQL statements

# Data definition operators (Data Definition Language, DDL):
CREATE = (
    """creates a database object (the database itself, a table, a view, a user, etc.)"""
)
ALTER = """modifies an object"""
DROP = """deletes an object"""

# Data manipulation operators (Data Manipulation Language, DML):
SELECT = """selects data that satisfies given conditions"""
INSERT = """adds new data"""
UPDATE = """modifies existing data"""
DELETE = """deletes data"""

# Data access definition operators (Data Control Language, DCL):
GRANT = """gives the user (group) permissions for certain operations with the object"""
REVOKE = """revokes previously issued permissions"""

# Transaction control language operators (Transaction Control Language''' TCL):
COMMIT = """commits a transaction"""
ROLLBACK = """rolls back all changes made in the context of the current transaction"""
SAVEPOINT = """divides the transaction into smaller parts.ALTER"""


# ER (Entity–relationship) — diagrams

ER_model = """is a data model that allows you to describe the conceptual schemes of a subject area. 
The ER model is used in high-level (conceptual) database design. With its help, you can highlight key entities 
and mark the connections that can be established between these entities."""

# Data types

"""Numbers are divided into whole numbers and fractional numbers (a number with a dot)."""
# Whole numbers
# (/images/image1jhg.png)

# Integers are also divided into types:

SIGNED = """signed (one bit goes to a plus or minus sign)"""
UNSIGNED = """unsigned if the values are only positive, such as distance, area, etc. 
This will double the positive value for the type, so TINYINT UNSIGNED will be between 0 and 255."""

# Fractional numbers

"""In SQL, fractional numbers, or fixed-precision numbers, are used to accurately represent numerical values,
especially important in financial and other calculations where precision and stability are required. 
In SQL, there are several data types for representing fractional numbers, which are often treated as aliases of each other, 
although in practice there may be some implementation differences depending on the DBMS."""

REAL = """REAL(10,2): This data type is typically used to represent real numbers. It may have less precision compared to DECIMAL."""
DECIMAL = """DECIMAL(10,2): This data type is used for precise representation of numbers where high precision of calculations is required. 
DECIMAL provides a fixed precision and scale."""
FIXED = """FIXED(10,2): This is another type for representing numbers with fixed precision. In many DBMS, it is synonymous with DECIMAL."""
FLOAT = """FLOAT(10,2): Although FLOAT also represents real numbers, its precision and behavior may differ from REAL. 
The FLOAT type may be more suitable for scientific computing, where a balance must be struck between range and precision.


Although these types are often treated as aliases, it is important to understand that depending on the particular DBMS 
(eg, MySQL, PostgreSQL, SQLite, etc.), they may have different internal implementations. As such, it is recommended 
that you always check the behavior of these types in the appropriate documentation for the DBMS you are using to understand 
their exact implementation and usage in your particular case."""


# Data types: date and time
# (/images/image-1jhg.png)
# Let's explain each type of data in more detail:

DATETIME = """for a full-fledged date and time, large in size, about 4-8 bytes. 
It is recorded as a string and always from large to small: year, month, day, hour, minute, second. 
The supported range is from '1000-01-01 00:00:00' to '9999-12-31 23:59:59'. 
If you need it below, just write with a minus '-500-01-09 00:00:00'."""
TIMESTAMP = """timestamp, Unix epoch range 1970-01-01 00:00:00 — 2038-12-31 00:00:00."""
DATE = """is just a date without a time."""
TIME = """is only time."""
YEAR = """is just a year."""


# Character data types

# These data types store a string of a certain length.

CHAR_type = """stores characters that are always the same length, so for CHAR(10) 10 characters (not bytes) will always be written. 
If the type limit is 10, then 10 is always written. If there are not enough characters in the line, spaces will be added, 
if there are many characters, they will be truncated."""

VARCHAR_type = """is a CHAR variable, it has an extra byte that represents the end, so to speak, an end marker. 
Thus, characters will be entered exactly as many as we entered plus 1 byte. That is, with CHAR(4) the empty string weighs 4 bytes, 
and with VARCHAR(4) it weighs 1 byte, the weight of only the marker. The string is also truncated if it overflows."""

TEXT_type = """if we need to store description, reviews or even books, then this is the type to go for."""

# Basic rules of SQL syntax


"""
1. SQL consists of many statements, each of which is usually terminated by a semicolon (;). 
For example, below are two different instructions:"""

# Request to select names and surnames from the employee table:
code = """
SELECT first_name, last_name
FROM employees;
"""

# The command to delete records from the employee table where the hire date is earlier than January 1, 1990:
code = """
DELETE FROM employees
WHERE hire_date < '1990-01-01';"""

"""
2. In SQL, there are many keywords with special meanings, 
such as SELECT , INSERT , UPDATE , DELETE , and DROP . 
These keywords are reserved and cannot be used as names of tables, columns, 
indexes, views, stored procedures, triggers, or other database objects."""

"""
3. To document SQL statements, we use SQL comments. When parsing commented SQL statements, 
the database engine ignores the characters in the comments. A comment is indicated by two consecutive hyphens --, 
which allow you to comment the rest of the line.


To document code that may span multiple lines, you'll use C-style multiline notation — /* comment */"""


# Query to retrieve employee IDs and their salaries from the employees table where salary is less than 3000:
code = """
SELECT employee_id, salary
FROM employees
WHERE salary < 3000; -- employees with low salary"""

# Update command to increase salary by 5% for employees whose salary is less than 3000:
code = """
/* increase 5% for employees whose salary is less than 3,000 */
UPDATE employees
SET salary = salary * 1.05
WHERE salary < 3000;"""

"""
The first query is used to retrieve data about employees with a salary below the specified threshold. 
The second is to make changes to these data, in particular to increase the salary."""


# CREATE TABLE: Creating a table


"""The CREATE TABLE statement is used to create tables in SQL. 
It takes parameters of the names of the columns we want to input as well as their data types.

Let's create three tables named "genders", "users" and "contacts",

The "genders" table will have three columns:

id - is the serial number of the gender, type INT, it is a unique key;
name — gender name, type VARCHAR(30);
created_at - time of record creation, type TIMESTAMP, default value - current time and date."""


code = """
CREATE TABLE genders (
   id INT PRIMARY KEY,
   name VARCHAR(30),
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

"""
To execute the code for our database, right-click on the database name on the left in the DBeaver menu 
and select 'SQL Editor' > 'Open SQL Console'. Paste the script and click "Run command" 
or in the menu 'SQL Editor' select the submenu 'Open SQL Console'.

After execution, you will have the required DB table. 
To see it, you may need to execute the update command for the database, this is the F5 key.

In the "users" table we will have seven columns:

id - is the serial number of the contact, type INT, it is a unique key;
name — user name, type VARCHAR(30);
email — user's email address, type VARCHAR(30);
password — user password, type VARCHAR(30);
age — age of the user, type TINYINT UNSIGNED;
gender_id - is a foreign key that links the "users" and "genders" tables with a one-to-many relationship. Many users can have one gender.
created_at - time of record creation, type TIMESTAMP, default value - current time and date."""


code = """
CREATE TABLE users (
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
);

It says that for the gender_id column in the users table, it is necessary to create a REFERENCES link to the genders table,
and the value of the column will match the value of the id column in the genders table for a particular record.

The ON DELETE SET NULL statement says that if an entry in the genders table is deleted, 
we must set the gender column in the users table to NULL. The ON UPDATE CASCADE statement says that 
if the value of the id field in the genders table is changed, the value of the gender_id column 
in the users table will also be automatically changed.

The "contacts" table will have seven columns:

id - is the serial number of the contact, type INT, it is a unique key;
name — name of the contact, type VARCHAR(30);
email — email address of the contact, type VARCHAR(30);
phone — contact phone, type VARCHAR(30);
favorite — the contact is in the favorite or not, logical type;
user_id - is a foreign key that links the "contacts" and "users" tables with a one-to-many relationship. One user can have many contacts;
created_at - time of record creation, type TIMESTAMP, default value - current time and date."""


code = """
CREATE TABLE contacts (
   id INT PRIMARY KEY,
   name VARCHAR(30),
   email VARCHAR(30),
   phone VARCHAR(30),
   favorite BOOLEAN,
   user_id INT,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY (user_id) REFERENCES users (id)
         ON DELETE CASCADE
         ON UPDATE CASCADE
);"""

# INSERT: Entering data


"""
Now let's fill in our tables. This can be done using the INSERT command. The command format is such that we specify column names 
before entering data. If we do not specify one of the columns, NULL or the given default value will be written in its place."""

# Let's insert the values into table genders:

code = """
INSERT INTO genders (id, name)
VALUES (1, 'male'), (2, 'female');"""


"""
We didn't specify a value for the created_at field when inserting, but thanks
DEFAULT CURRENT_TIMESTAMP instructions, the value will be substituted automatically."""

# Let's insert the value into the users table:

code = """
INSERT INTO users (id, name, email, password, age, gender_id)
VALUES (1, 'Boris', 'boris@test.com', 'password', 23, 1),
(2, 'Alina', 'alina@test.com', 'password', 32, 2),
(3, 'Maksim', 'maksim@test.com', 'password', 40, 1);"""

# Let's insert the value into the contacts table:

code = """
INSERT INTO contacts (id, name, email, phone, favorite, user_id)
VALUES (1, 'Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
(2, 'Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
(3, 'Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
(4, 'Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
(5, 'Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, null);"""


# SELECT: Getting data

"""
This query is used in case we need to show data in a table. Probably the simplest example of using SELECT would be the following query:
"""

code = """
SELECT * FROM contacts;"""


"""
The result of this request will be a table with all the data in the contacts table.

The asterisk * means that we want to show all columns from the table without exception. 
Since there is usually more than one table in the database, we need to specify the name of the table 
from which we want to view data. This is done using the FROM keyword.

When you only need some columns from a table, you can specify their names with a comma instead of an asterisk.
"""

code = """
SELECT name, email FROM contacts ORDER BY name;
"""

"""
Also sometimes we need to sort the output data. For this we will use ORDER BY "column name". 
ORDER BY has two modifiers: ASC - Sort Ascending, the default value, and DESC - Sort Descending

If only some specific records are to be included in the output by a condition, the WHERE keyword is used. 
It allows you to filter data according to a certain condition."""

# In the next query, we will display only the selected contacts.

code = """
SELECT name, email
FROM contacts
WHERE favorite = true
ORDER BY name;"""

"""
Conditions in WHERE can be written using logical operators AND and OR, as well as mathematical comparison operators (=, <, >, <=, >=, <>).
WHERE conditions can be written using several more commands, which are:"""

IN = """compares a value in a column against multiple possible values and returns true if the value matches at least one value."""


code = """SELECT name, email
FROM users
WHERE age IN(20, 30, 40)
ORDER BY name;"""

BETWEEN = """checks if a value is in some interval."""

code = """
SELECT name, email, age
FROM users
WHERE age BETWEEN 30 AND 40
ORDER BY name;"""

LIKE = """searches by pattern."""

# Also, if we want to display all contacts whose name contains the letter 'L', we can use the following entry:


code = """
SELECT name, email
FROM contacts
WHERE name LIKE '%L%'
ORDER BY name;"""


"""
The % sign means any sequence of characters (0 characters is also considered a sequence)."""


# SQL also has inversion. To do this, you need to write NOT before any logical expression in the condition (NOT BETWEEN, etc.).


code = """
SELECT name, email, age
FROM users
WHERE age NOT BETWEEN 30 AND 40
ORDER BY name;"""
