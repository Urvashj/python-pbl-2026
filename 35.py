import sqlite3
db = sqlite3.connect("college.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    price INTEGER
)
""")
cursor.execute(
    "INSERT OR REPLACE INTO books (book_id, title, price) VALUES (?, ?, ?)",
    (101, "Python Basics", 450)
)

db.commit()
cursor.execute("SELECT * FROM books")

print("Book Records:")

for record in cursor.fetchall():
    print(record)

cursor.close()
db.close() 