import sqlite3

connection = sqlite3.connect("student.db")

print(connection)

cur = connection.cursor()

print(cur)

query = """
    create table std(
    roll_no int,
    name varchar[50],
    age int,
    address varchar[30]
    )
"""

cur.execute(query)

query = """
    insert into std(
    roll_no, name, age, address
    )
    values
    (
    1, "Rajendra", 24, "Bhaktapur"
    ),
    (
    2, "Naresh", 23, "Bhaktapur"
    ),
    (
    3, "Raju", 25, "Kathmandu"
    )
"""

cur.execute(query)

print(cur.execute("select * from std").fetchall())