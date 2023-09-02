import utils
import db

def main():
    db.initialize_database()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            utils.add_expense()

        elif choice == '2':
            utils.add_income()

        elif choice == '3':
            budget = db.calculate_budget()
            print(f"\nRemaining Budget: ${budget}")

        elif choice == '4':
            utils.analyze_expenses()

        elif choice == '5':
            print("Exiting Budget Tracker.")
            db.close_database()
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
