# src/Category.py

class Category:
    def __init__(self):
        self.categories = ["Groceries", "Utilities", "Entertainment", "Others"]

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories.append(category_name)
    
    def get_categories(self):
        return self.categories
