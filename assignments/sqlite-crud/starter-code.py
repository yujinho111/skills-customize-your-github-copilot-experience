import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Create a table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """
)

# Example: insert sample data
# cur.execute("INSERT INTO students (name, grade, status) VALUES (?, ?, ?)", ("Alice", "A", "active"))
# conn.commit()

# TODO: Add a menu to let the user add, view, update, and delete records
# TODO: Display all records in a readable format
# TODO: Make sure the program handles invalid input cleanly

conn.close()
