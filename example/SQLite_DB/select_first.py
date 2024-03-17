import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT ROUND(AVG(p.total), 2) AS average_total, e.post
FROM payments AS p
LEFT JOIN employees AS e ON p.employee_id = e.id
GROUP BY e.post;
"""

print(execute_query(sql))

# average_total|post                     |
# -------------+-------------------------+
#       5096.42|Animal technologist      |
#       5514.54|Chief Marketing Officer  |
#       5546.54|Education officer, museum|
#       5895.53|Higher education lecturer|
#       5259.98|Programmer, systems      |

# [(5096.42, 'Animal technologist'), 
# (5514.54, 'Chief Marketing Officer'), 
# (5546.54, 'Education officer, museum'), 
# (5895.53, 'Higher education lecturer'), 
# (5259.98, 'Programmer, systems')]
