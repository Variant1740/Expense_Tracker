from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from app.services.tracker import ExpenseTracker
from app.models.expense import Expense

app = FastAPI(title="Expense Api",  version="1.0")

service = ExpenseTracker()

@app.post("/add-expense")
def add_expense_api(expense: Expense):
    service.api_add_expense(
        category=expense.category,
        amount=expense.amount,
        date=expense.date,
        description=expense.description
    )
    return {"message": "expense added successfully"}

@app.get("/expenses")
def get_expenses():
    return service.view_expenses()

@app.get("/total")
def get_total_spent():
    total = service.total_spent()
    return {"total_spent": total}

@app.get("/pie-chart")
def get_pie_chart():
    chart = service.generate_pie_chart()
    if not chart:
        return {"message": "no expenses to generate chart"}
    
    return StreamingResponse(chart, media_type="image/png")

