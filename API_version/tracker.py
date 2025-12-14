import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt  

from app.models.expense import Expense
from app.utils.logger import logger  


class ExpenseTracker:
    def __init__(self, data_file: str = "data/Expenses.json"):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(exist_ok=True)
        self.expenses: list[Expense] = []
        self.load_data()

    def add_expense(self):
        logger.info("Adding new expense...")
        category = input("Enter a category: ").strip().title()
        description = input("Enter a short description: ").strip()
          
        while True:
            try:
                amount = float(input("Enter Amount Spent ($): "))
                break
            except ValueError:
                logger.error("Invalid amount entered!")

        date = datetime.now().strftime("%Y-%m-%d")
        expense = Expense(category, amount, date, description)
        self.expenses.append(expense)
        logger.success(f"Added: {category} - ${amount:,.2f} - {description}")

    def view_expenses(self):
        if not self.expenses:
            logger.warning("No expenses recorded yet!")
            return

        logger.info("Displaying all expenses...")
        print("\n" + "="*110)
        print(f"{'No.':<4} {'Category':<20} {'Amount($)':>15} {'Date':>15} {'Description':<40}")
        print("="*110)
          
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i:<4} {exp.category:<20} {exp.amount:>15,.2f} {exp.date:>15} {exp.description:<40}")
        print("="*110)

    def total_spent(self):
        total = sum(exp.amount for exp in self.expenses)
        logger.info(f"Total spent: ${total:,.2f}")
        print(f"\nTOTAL SPENT: ${total:,.2f}\n")

    def save_data(self):
        data = [
            {
                "category": exp.category,
                "amount": exp.amount,
                "date": exp.date,
                "description": exp.description
            }
            for exp in self.expenses
        ]
        try:
            self.data_file.write_text(json.dumps(data, indent=4))
            logger.success(f"Data saved successfully to {self.data_file}")
        except Exception as e:
            logger.error(f"Failed to save data: {e}")

    def load_data(self):
        if not self.data_file.exists():
            logger.info("No previous data found. Starting fresh.")
            return

        try:
            data = json.loads(self.data_file.read_text())
            self.expenses = [
                Expense(
                    item["category"],
                    item["amount"],
                    item["date"],
                    item["description"]
                )
                for item in data
            ]
            logger.success(f"Loaded {len(self.expenses)} expenses from file")
        except Exception as e:
            logger.error(f"Failed to load data: {e}")

    def show_pie_chart(self):
        if not self.expenses:
            logger.warning("No expenses to show in chart")
            return

        category_totals = defaultdict(float)
        for exp in self.expenses:
            category_totals[exp.category] += exp.amount

        labels = list(category_totals.keys())
        values = list(category_totals.values())

        plt.figure(figsize=(8, 8))
        plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
        plt.title("Spending Distribution by Category", fontsize=16, fontweight="bold")
        plt.axis("equal")
        logger.info("Displaying pie chart...")
        plt.show()

    def run(self):
        logger.info("Personal Expense Tracker Started!")
        self.load_data()

        while True:
            print('''
            ====== PERSONAL EXPENSE TRACKER ======
            1. Add Expense
            2. View All Expenses
            3. Show Total Spent
            4. Save and Exit
            5. Show Pie Chart
            ''')
            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.total_spent()
            elif choice == "4":
                self.save_data()
                logger.info("Goodbye!")
                break
            elif choice == "5":
                self.show_pie_chart()
            else:
                logger.error("Invalid option selected!")
