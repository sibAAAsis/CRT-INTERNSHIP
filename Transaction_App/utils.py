import db

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    db.add_transaction(category, amount, is_income=False)
    print(f"Expense of ${amount} in category '{category}' added.")

def add_income():
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    db.add_transaction(category, amount, is_income=True)
    print(f"Income of ${amount} in category '{category}' added.")

def analyze_expenses():
    cursor = db.cursor
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY category")
    expenses = cursor.fetchall()

    print("\nExpense Analysis:")
    for category, amount in expenses:
        print(f"{category}: ${amount}")

if __name__ == "__main__":
    print("This file contains utility functions for the Budget Tracker.")
