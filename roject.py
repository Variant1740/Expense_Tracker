#expense trcker
import json
import datetime
import time

expenses=[]

def add_expense():
    item=input('Enter an expense: ').capitalize()
    try:
        amount=float(input('Enter Amount Spent($): '))
        expenses.append({'item': item, 'amount':amount})
        print(f'{item} of ${amount} added succesfully!...😉')
    except Exception:
        print('Invalid Amount.')
        for x in range(0, 3):
            time.sleep(1)
        
def view_expense():
    if not expenses:
        print('No expenses added yet😥...')
        return
    print('_____Your Expenses______')
    for i, exp in enumerate(expenses, start=1):
        print(f'{i}.{exp['item']} - ${exp["amount"]}')
        print('---------------')


def total_spent():
    total=sum(exp['amount'] for exp in expenses)
    print(f'Total Spent: ${total}')

def save_data(filename='Expenses.json'):
    with open(filename, 'w') as file:
        json.dump(expenses, file)
def load_data(filename='Expenses.json'):
    global expenses
    try:
        with open(filename, 'r')  as file:
            expenses=json.load(file)
    except Exception:
        expenses=[]


load_data()
while True:
    print('''
        ======PERSONAL EXPENSE TRACKER=======
          1. Add Expenses🎯
          2. View All Expenses🔍
          3. Show Total Spent💸 
          4. Save and Exit📌      
          ''')
    
    option=input('Choose an option: ')

    if option=='1':
        add_expense()      
    elif option=='2':
        view_expense()
    elif option=='3':
        total_spent()
    elif option=='4':
        save_data()
        print('Expenses saved.')
        for x in range(0, 3):
            time.sleep(1)
        print('Goodbye!🤗')
        break
    else:
        print('invalid Option. Try Again😥')
        for x in range(0, 3):
            time.sleep(1)