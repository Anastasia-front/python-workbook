"""
This is a unique key, it has all the properties of a primary key, but it is not primary. 
Helps not to record takes.


Let's assume that we have a table of users, where there is a primary key, but the user's email 
is also unique, it is wrong to divide it into different tables. There is a possibility that 
the attacker will register a fake. To prevent this from happening, we simply make the email unique as well.
"""

# Creation when describing the structure:


"""
CREATE TABLE persons (
     id INT PRIMARY KEY,
     email CHAR(50) NOT NULL,
     fullName varchar(100) NULL,
     CONSTRAINT persons_email_un UNIQUE KEY (email)
);"""


# Or add it using ALTER if it is not present in the table structure:


"""ALTER TABLE persons ADD CONSTRAINT persons_email_un UNIQUE KEY (email);
"""


# Now you cannot write the same value in the email field.


"""The UNIQUE KEY name must have the postscript un or uq: persons_email_un or un_persons_email."""
