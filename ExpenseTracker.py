# src/ExpenseTracker.py

import csv
from datetime import datetime
from Expense import Expense
from Category import Category

class ExpenseTracker:
    def __init__(self, data_file="data/expenses.csv"):
        self.data_file = data_file
        self.expenses = []
        self.categories = Category()
        self.load_expenses()

    def add_expense(self, amount, date, category, description=""):
        expense = Expense(amount, date, category, description)
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(expense.to_dict())

    def save_expenses(self):
        with open(self.data_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Amount", "Date", "Category", "Description"])
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense.to_dict())

    def load_expenses(self):
        try:
            with open(self.data_file, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expense = Expense(row["Amount"], row["Date"], row["Category"], row["Description"])
                    self.expenses.append(expense)
        except FileNotFoundError:
            print("Data file not found. A new file will be created upon adding an expense.")

    def filter_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    def generate_report(self, period="monthly"):
        # This can be expanded to include date calculations for daily, weekly, and monthly reports
        report = {}
        for expense in self.expenses:
            report[expense.date] = report.get(expense.date, 0) + float(expense.amount)
        print(f"{period.capitalize()} Report:", report)
