import sqlite3

connection = sqlite3.connect("college.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    name TEXT,
    duration INTEGER
)
""")

query = "INSERT INTO courses (id, name, duration) VALUES (?, ?, ?)"
values = (1, "Python", 6)

cursor.execute(query, values)
connection.commit()

cursor.execute("SELECT * FROM courses")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()  