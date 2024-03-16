from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error:
        print


if __name__ == "__main__":
    sql_create_projects_table = """
     CREATE TABLE IF NOT EXISTS projects (
      id integer PRIMARY KEY,
      name text NOT NULL,
      begin_date text,
      end_date text
     );
     """

    sql_create_tasks_table = """
     CREATE TABLE IF NOT EXISTS tasks (
      id integer PRIMARY KEY,
      name text NOT NULL,
      priority integer,
      project_id integer NOT NULL,
      status Boolean default False,
      begin_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (project_id) REFERENCES projects (id)
     );
     """

    with create_connection(database) as conn:
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_projects_table)
            # create tasks table
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")


"""Let's create a helper function for creating tables create_table. 
Then we will write SQL queries to create two tables: the tasks table 
and the projects to which these tasks belong:
"""


sql_create_projects_table = """
     CREATE TABLE IF NOT EXISTS projects (
      id integer PRIMARY KEY,
      name text NOT NULL,
      begin_date text,
      end_date text
     );
     """

sql_create_tasks_table = """
     CREATE TABLE IF NOT EXISTS tasks (
      id integer PRIMARY KEY,
      name text NOT NULL,
      priority integer,
      project_id integer NOT NULL,
      status Boolean default False,
      begin_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (project_id) REFERENCES projects (id)
     );
     """


"""For simplicity, we will use Python's built-in SQLite support and create a database in the form of a file.
"""


with create_connection(database) as conn:
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")
