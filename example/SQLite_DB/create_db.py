import sqlite3


'''We create a directory with the project and execute the command to go to it in the console.'''

# mkdir example_sql
# cd example_sql


'''Remember that you need to create a virtual environment and activate it 
'''

# python -m venv venv
# cd venv/scripts
# venv/scripts >>> activate


def create_db():
# read the file with the script for creating the database
     with open('salary.sql', 'r') as f:
         sql = f.read()

# create a connection to the database (if there is no file from the database, it will be created)
     with sqlite3.connect('salary.db') as con:
         cur = con.cursor()
# execute a script from a file that will create tables in the database
         cur.executescript(sql)

if __name__ == "__main__":
     create_db()
