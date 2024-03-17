import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
SELECT c.company_name, e.employee, e.post, p.total
FROM companies c
    LEFT JOIN employees e ON e.company_id = c.id
    LEFT JOIN payments p ON p.employee_id = e.id
WHERE p.total > 5000
    AND  p.date_of BETWEEN  '2021-07-10' AND  '2021-07-20'
"""

print(execute_query(sql))

# company_name          |employee          |post                     |total|
# ----------------------+------------------+-------------------------+-----+
# Taylor, King and Ponce|Anthony Jones     |Higher education lecturer| 6833|
# Taylor, King and Ponce|Barbara Mathis    |Education officer, museum| 9008|
# Taylor, King and Ponce|Daniel Wells      |Programmer, systems      | 6703|
# Taylor, King and Ponce|Robin Grant       |Chief Marketing Officer  | 6409|
# Brown and Sons        |Christina Wallace |Education officer, museum| 8604|
# Brown and Sons        |Daniel Robinson   |Higher education lecturer| 5418|
# Brown and Sons        |Ethan Phillips DDS|Education officer, museum| 8345|
# Brown and Sons        |James Mack        |Higher education lecturer| 6243|
# Brown and Sons        |James Olson       |Education officer, museum| 5318|
# Brown and Sons        |Melissa Robles    |Education officer, museum| 8260|
# Brown and Sons        |Roberto Smith     |Higher education lecturer| 7766|
# Brown and Sons        |Sara Stevens      |Higher education lecturer| 6206|
# Brown and Sons        |Vickie Chen       |Programmer, systems      | 6701|
# Brown and Sons        |Victoria Weaver   |Programmer, systems      | 9279|
# Spencer-Wall          |Daniel Chen       |Education officer, museum| 8244|
# Spencer-Wall          |Erica Hines       |Education officer, museum| 5643|
# Spencer-Wall          |Laura Powell      |Programmer, systems      | 5822|

# [('Taylor, King and Ponce', 'Anthony Jones', 'Higher education lecturer', 6833), ('Taylor, King and Ponce', 'Barbara Mathis', 'Education officer, museum', 9008), ('Taylor, King and Ponce', 'Daniel Wells', 'Programmer, systems', 6703), ('Taylor, King and Ponce', 'Robin Grant', 'Chief Marketing Officer', 6409), ('Brown and Sons', 'Christina Wallace', 'Education officer, museum', 8604), ('Brown and Sons', 'Daniel Robinson', 'Higher education lecturer', 5418), ('Brown and Sons', 'Ethan Phillips DDS', 'Education officer, museum', 8345), ('Brown and Sons', 'James Mack', 'Higher education lecturer', 6243), ('Brown and Sons', 'James Olson', 'Education officer, museum', 5318), ('Brown and Sons', 'Melissa Robles', 'Education officer, museum', 8260), ('Brown and Sons', 'Roberto Smith', 'Higher education lecturer', 7766), ('Brown and Sons', 'Sara Stevens', 'Higher education lecturer', 6206), ('Brown and Sons', 'Vickie Chen', 'Programmer, systems', 6701), ('Brown and Sons', 'Victoria Weaver', 'Programmer, systems', 9279), ('Spencer-Wall', 'Daniel Chen', 'Education officer, museum', 8244), ('Spencer-Wall', 'Erica Hines', 'Education officer, museum', 5643), ('Spencer-Wall', 'Laura Powell', 'Programmer, systems', 5822)]