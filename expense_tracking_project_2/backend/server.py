from urllib.error import HTTPError

from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

#the response model will ensure that we only get a response of what we want that is stated in the Expense class
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expense(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)

    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve summary from the database.")

    total = 0
    for section in data:
        total += section['Total']

    breakdown = {}


    for section in data:
        percentage = (section['Total']/total)*100 if total != 0 else 0
        breakdown[section["category"]] = {
            "Total": section['Total'],
            "percentage": round(percentage, 2)
        }

    return breakdown

@app.get("/month_breakdown/")
def get_analytics_month():
    data = db_helper.fetch_month()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve data.")
    return data

@app.get("/report/")
def get_reports():
    data = db_helper.fetch_all_records()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve data.")
    return data

'''
@app.get("/user_breakdown/")
def get_analytics_user():
    data = db_helper.fetch_user()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve data.")
    return data
'''