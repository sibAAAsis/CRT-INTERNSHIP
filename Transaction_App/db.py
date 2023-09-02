import sqlite3

conn = None
cursor = None

def initialize_database():
    global conn, cursor
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            category TEXT,
            amount REAL,
            type TEXT
        )
    ''')
    conn.commit()

def add_transaction(category, amount, is_income=False):
    transaction_type = "Income" if is_income else "Expense"
    cursor.execute("INSERT INTO transactions (category, amount, type) VALUES (?, ?, ?)",
                   (category, amount, transaction_type))
    conn.commit()

def calculate_budget():
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'Income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'Expense'")
    expense = cursor.fetchone()[0] or 0

    return income - expense

def close_database():
    global conn
    conn.close()
