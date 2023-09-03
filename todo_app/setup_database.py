import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()


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
