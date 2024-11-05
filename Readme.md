

---

# Expense Tracker

## Overview
A Python application for tracking expenses with features to add, view, categorize, filter, and report on expenses. Data is saved in a CSV file to ensure persistence between sessions.

## Features
- **Add, View, and Manage Expenses**: Input details like amount, date, category, and description.
- **Filter by Category**: View expenses in specific categories.
- **Generate Reports**: Create expense reports by day, week, or month.
- **CSV Persistence**: Saves and loads expenses automatically for data continuity.
- **Error Handling**: Manages invalid inputs and file errors gracefully.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/satyamjaysawal/Expense-Tracker.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python src/main.py
   ```

## Usage

1. **Add Expense**: Enter details like amount, date, category, and optional description.
2. **View Expenses**: Display a list of all expenses.
3. **Filter by Category**: View expenses by specified category.
4. **Generate Report**: View total expenses by day, week, or month.

## Project Structure

```
expense_tracker/
│
├── src/
│   ├── Expense.py          # Defines the Expense class
│   ├── Category.py         # Manages expense categories
│   ├── ExpenseTracker.py   # Main application logic
│   └── main.py             # Entry point for running the application
│
├── data/
│   └── expenses.csv        # CSV file for persistent data storage (created automatically)
│
├── README.md               # Project overview, setup, and usage instructions
├── requirements.txt        # List of dependencies
└── .gitignore              # Excludes unnecessary files from version control

```


--- 
