"""Now our database stores information about the project and two tasks. 
To get this information in the application, let's create the select.py module.
"""

from sqlite3 import Error

from connect import create_connection, database


def select_projects(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: rows projects
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM projects;")
        rows = cur.fetchall()
    except Error:
        print
    finally:
        cur.close()
    return rows


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: rows tasks
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()
    except Error:
        print
    finally:
        cur.close()
    return rows


def select_task_by_status(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param status:
    :return: rows tasks
    """
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks WHERE status=?", (status,))
        rows = cur.fetchall()
    except Error:
        print
    finally:
        cur.close()
    return rows


if __name__ == "__main__":
    with create_connection(database) as conn:
        print("Projects:")
        projects = select_projects(conn)
        print(projects)
        print("\\nQuery all tasks")
        tasks = select_all_tasks(conn)
        print(tasks)
        print("\\nQuery task by status:")
        task_by_priority = select_task_by_status(conn, True)
        print(task_by_priority)


"""
The function for selecting all projects is select_projects, 
the function for selecting all tasks is select_all_tasks, and, 
for example, the function for selecting all tasks by status is select_task_by_status.


The result of executing the select.py script in the console:


Projects:
[(1, 'Cool App with SQLite & Python', '2022-01-01', '2022-01-30')]

Query all tasks
[(1, 'Analyze the requirements of the app', 1, 1, 1, '2022-01-01', '2022-01-02'), (2, 'Confirm with user about the top requirements', 1 , 1, 0, '2022-01-03', '2022-01-05')]

Query task by status:
[(1, 'Analyze the requirements of the app', 1, 1, 1, '2022-01-01', '2022-01-02')]"""
