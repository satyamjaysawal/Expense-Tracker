# src/Expense.py

class Expense:
    def __init__(self, amount, date, category, description=""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "Amount": self.amount,
            "Date": self.date,
            "Category": self.category,
            "Description": self.description
        }
