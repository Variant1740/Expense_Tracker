 Expense Tracker (Python)

A simple command-line Python app for tracking personal expenses.  
It allows you to record, view, and save your spending data in a persistent file so that your records remain intact even after closing the program.

---

## Features
- Add new expenses with name and amount  
- View all saved expenses in a formatted table  
- Calculate total spending
- Data persistence: automatically saves and loads data from a JSON file (`Expenses.json`)  
- User-friendly menu interface with clear prompts and feedback  

---

##  How It Works
1. When the program starts, it automatically loads previously saved expenses (if any).  
2. You can choose from the menu:
   - `1` → Add new expense  
   - `2` → View all expenses  
   - `3` → Show total amount spent  
   - `4` → Save and exit  
3. Data is stored in `Expenses.json` using the built-in `json` module.  

---

## Technologies Used
- Python 3
- JSON module (for data storage)
- time module (for simple delays and smooth UX)

---

##  How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Variant1740/Expense_Tracker.git
   
