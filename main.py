# src/main.py

from ExpenseTracker import ExpenseTracker
from datetime import datetime

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses by Category")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, date, category, description)
            print("Expense added successfully!")
        
        elif choice == "2":
            tracker.view_expenses()
        
        elif choice == "3":
            category = input("Enter category to filter by: ")
            expenses = tracker.filter_expenses_by_category(category)
            for expense in expenses:
                print(expense.to_dict())
        
        elif choice == "4":
            period = input("Enter report period (daily/weekly/monthly): ")
            tracker.generate_report(period)
        
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
