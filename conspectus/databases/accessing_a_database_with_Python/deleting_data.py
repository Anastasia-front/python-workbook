from sqlite3 import Error

from connect import create_connection, database

def delete_task(conn, id):
     """
     Delete a task by task id
     :param conn: Connection to the SQLite database
     :param id: id of the task
     :return:
     """
     sql = 'DELETE FROM tasks WHERE id=?'
     cur = conn.cursor()
     try:
         cur.execute(sql, (id,))
         conn.commit()
     except Error as e:
         print(e)
     finally:
         cur.close()

if __name__ == '__main__':
     with create_connection(database) as conn:
         delete_task(conn, 1)


'''
Here we delete the task with id=1. Only the task with id=2 remains in the database.

As you can see, there is now one task left for the project in the database, 
and this is easy to check by asking to get all projects with their tasks.

Now let's write and execute the command to get the name of the task and the project to which it belongs:

'''

def select_projects(conn):
     """
     Query all rows in the projects table with its tasks
     :param conn: the Connection object
     :return: rows projects or None
     """
     rows = None
     cur = conn.cursor()
     try:
         cur.execute("SELECT * FROM projects JOIN tasks ON tasks.project_id = projects.id;")
         rows = cur.fetchall()
     except Error as e:
         print(e)
     finally:
         cur.close()
     return rows

if __name__ == '__main__':
     with create_connection(database) as conn:
         print("Projects:")
         projects = select_projects(conn)
         print(projects)



# Result:

# Projects:
# [(1, 'Cool App with SQLite & Python', '2022-01-01', '2022-01-30', 
# 2, 'Confirm with user about the top requirements', 1, 1, 1, '2022- 01-03', '2022-01-05')]