import sqlite3

db = sqlite3.connect("college.db")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER
)
""")
cursor.execute(
    "INSERT OR REPLACE INTO products VALUES (?, ?, ?)",
    (201, "Keyboard", 20)
)
db.commit()
cursor.execute(
    "UPDATE products SET quantity = ? WHERE product_id = ?",
    (35, 201)
)
db.commit()
cursor.execute("SELECT * FROM products")
print("After UPDATE:")
for record in cursor.fetchall():
    print(record)
cursor.execute(
    "DELETE FROM products WHERE product_id = ?",
    (201,)
)
db.commit()
cursor.execute("SELECT * FROM products")
print("After DELETE:")
for record in cursor.fetchall():
    print(record)
cursor.close()
db.close()    