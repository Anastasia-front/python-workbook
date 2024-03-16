PEP249 = """The Python Database API Specification v2.0 standard was defined to encourage commonality 
between Python modules used to access databases. The standard aims to achieve consistency, 
leading to clearer Python database connection modules.
"""


# Connection methods

"""
The following database connection methods must be supported:

    close() — closing the connection;

    commit() — commit any pending transaction to the database;

    rollback() — This method is optional because not all databases support transactions.
If the database is providing transactions, this method causes the database to be rolled back 
to the start of any pending transaction. Closing the connection without first committing 
the changes will cause an implicit rollback;

    cursor() — return a new cursor object using the current connection.
"""

# Cursor methods
"""
These objects represent the database cursor used to manage the context of the fetch operation. 
Cursors created from the same database connection are not isolated, meaning any changes 
made to the database by a cursor are immediately visible to other cursors. 
Cursor objects must respond to the following methods.


    close() — close the cursor and return the resource to the system (closes the open socket connection). 
From this moment the cursor will be unusable. The Error exception (or subclass) will be called 
if any operation is performed with the cursor.

    execute(operation, parameters) — executes an SQL command with parameters. Parameters can be provided 
as a sequence or mapping and will be bound to variables in the operation. Parameters can also be specified 
as a list of tuples, for example to insert multiple rows into a single operation, but this usage 
is deprecated: use .executemany() instead.

    executemany(operation, seq_of_parameters) is the same as execute, but seq_of_parameters 
is a list of parameter sets, and the SQL operation will be executed with all of them in turn. 
Speeds up the operation by reusing an already open connection to the database.
    fetchone() — Fetch the next row of the query result set, returning a single sequence, 
or None if no more data is available.

    fetchmany(size=cursor.arraysize) — Fetch the next set of rows of the query result, returning a sequence 
of sequences (for example, a list of tuples). An empty sequence is returned when no more strings 
are available. The number of rows to sample per call is specified by the size parameter. 
If not specified, the size of the cursor array determines the number of rows retrieved. 
The method should try to get as many rows, as many as specified by the size parameter. 
If this is not possible because the specified number of rows is not available, 
a smaller number of rows may be returned.

    fetchall() — get all rows (remaining rows) of the query result, returning them as a sequence 
of sequences (for example, a list of tuples). Note that the cursor array attribute can affect 
the performance of this operation."""
