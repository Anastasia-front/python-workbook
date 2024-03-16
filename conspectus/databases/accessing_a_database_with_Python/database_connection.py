"""As an example of connecting to a database, we use SQLite.
It is a database in a file, but the basic principles of the PEP249 standard are fully applied to it.
"""

import sqlite3
from contextlib import contextmanager

database = "path/to/file/test.db"


@contextmanager
def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()


# Let's create a context manager in the connect.py file.
