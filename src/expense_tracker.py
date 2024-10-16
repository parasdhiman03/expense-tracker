import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists('data/expenses.json'):
            with open('data/expenses.json', 'r') as file:
                self.expenses = json.load(file)
        else:
            self.expenses = []

    def save_expenses(self):
        with open('data/expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        try:
            amount = float(input("Enter amount spent: "))
            description = input("Enter description: ")
            category = input("Enter category (e.g., food, transportation): ").lower()
            date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            date = date_str if date_str else datetime.today().strftime('%Y-%m-%d')

            expense = {
                "amount": amount,
                "description": description,
                "category": category,
                "date": date
            }
            self.expenses.append(expense)
            self.save_expenses()
            print("Expense added successfully!")
        except ValueError:
            print("Invalid input. Please try again.")

    def view_expenses(self):
        print("\nYour Expenses:")
        for expense in self.expenses:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
        print("\n")

    def view_category_summary(self):
        category = input("Enter category to summarize: ").lower()
        total = sum(exp['amount'] for exp in self.expenses if exp['category'] == category)
        print(f"Total expenses for {category}: {total}")

    def view_monthly_summary(self):
        current_month = datetime.today().strftime('%Y-%m')
        total = sum(exp['amount'] for exp in self.expenses if exp['date'].startswith(current_month))
        print(f"Total expenses for {current_month}: {total}")
