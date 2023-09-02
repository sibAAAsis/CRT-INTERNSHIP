# tasks.db will be used to store our tasks
import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create a table to store tasks
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT,
        priority TEXT,
        description TEXT,
        due_date TEXT,
        completed INTEGER
    )
''')

conn.commit()
conn.close()
