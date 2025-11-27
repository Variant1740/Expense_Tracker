#expense tracker
import json
import time
from datetime import datetime

class Expense:
    def __init__(self, category, amount, date, description):
        self.category=category
        self.amount=amount
        self.date=date
        self.description=description

class Expense_Tracker:
    def __init__(self):
        self.expenses=[]
    
    def add_expense(self):
        category=input('Enter a category: ').title()
        description=input("Enter a short description:")
        try:
            amount=float(input('Enter Amount Spent($): '))           
        except Exception:
            print('Invalid Amount.')
            return
        date= datetime.now().strftime("%Y-%m-%d")
        expense=Expense(category,amount,date,description)
        self.expenses.append(expense)
        print(f'{expense.category} of ${expense.amount} added succesfully! on {expense.date}!😉')

    def view_expense(self):
        if not self.expenses:
            print('No expenses made yet😥...')
            return
        print('\n YOUR EXPENSES:')
        print(f"{'No.':<4}   {'Category':<25}   {'Amount($)':>12}  {"Date":>25} -  {"Description":>30}") 
        print('-'* 110) 
        for i, exp in enumerate(self.expenses, start=1):
            print(f'{i:<4}.  {exp.category:<25}  {exp.amount:>12,.2f}  {exp.date:>28}  - {exp.description:<30}')
            print('-'* 110)                  
#time.sleep(2)
    def total_spent(self):
        total=sum(exp.amount for exp in self.expenses)
        print(f'Total Expense: ${total:,.2f}')

        
    def save_data(self, filename='Expenses.json'):
        data=[]
        for exp in self.expenses:
            data.append({
                "category":exp.category,
                "amount": exp.amount,
                "date": exp.date,
                "description": exp.description
            })
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data saved succesfully🤗")

    def load_data(self, filename='Expenses.json'):
        global expenses
        try:
            with open(filename, 'r')  as file:
                data=json.load(file)
            for item in data:
                exp=Expense(
                    item["category"],
                    item["amount"],
                    item["date"],
                    item["description"]
                )
                self.expenses.append(exp)
            print("Data Loaded")
        except FileNotFoundError:
            print("OOPS!😧")
            print("No data file found. Starting fresh.")

    def menu(self):

        while True:
            print('''
            ======PERSONAL EXPENSE TRACKER=======
            1. Add Expenses🎯
            2. View All Expenses🔍
            3. Show Total Spent💸 
            4. Save and Exit📌
            5. Load Data from File📂 
            6. Show Pie Chart📊     
            ''')
            option=input('Choose an option: ')
            if option=='1':
                self.add_expense()      
            elif option=='2':
                self.view_expense()
            elif option=='3':
                self.total_spent()
            elif option=="5":
                self.load_data()
            elif option=="6":
                self.pie_chart()
            elif option=='4':
                self.save_data()               
                time.sleep(1)
                print('Goodbye!🤗')
                break            
            else:
                print('invalid Option. Try Again😥')
    
    def pie_chart(self):
        import matplotlib.pyplot as plt
        from collections import defaultdict

        if not self.expenses:
            print("No expenses to display😥...")
            return
        category_totals=defaultdict(float)
        for exp in self.expenses:
            category_totals[exp.category] += exp.amount
        labels=list(category_totals.keys())
        values=list(category_totals.values())

        plt.figure(figsize=(7,7))
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title("Spending Distribution by Category")
        plt.axis('equal')
        plt.show(block=False)
        plt.pause(0.1)
   
expense_tracker=Expense_Tracker()
expense_tracker.menu()
time.sleep(2)