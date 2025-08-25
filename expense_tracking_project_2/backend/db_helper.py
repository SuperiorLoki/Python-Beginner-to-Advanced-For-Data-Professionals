#CRUD (Create, Retrieve, Update, Delete)

import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Coding@2025",
        database="expense_manager"
    )

    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Failed Connection.")

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_all_records():
    logger.info("fetch_all_records called.")
    #This means that the rest of the get_db_cursor() function will run (after the yield statement) after the with
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        return expenses



def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}.")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called for {expense_date} with price: {amount}, category: {category}, notes: {notes}.")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
                       (expense_date, amount, category, notes)
                       )

def delete_expense(ident):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE id = %s",
                       (ident,))

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}.")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s",
                       (expense_date,))


def update_expense(expense_date, amount, category, notes):
    logger.info(f"update_expenses called for {expense_date} with price: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("UPDATE amount = %s, category = %s, notes = %s WHERE expense_date = %s",
                       (amount, category, notes, expense_date)
                       )

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetching expense summary called between dates {start_date} and {end_date}.")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT category, SUM(amount) as Total FROM expense_manager.expenses WHERE expense_date BETWEEN %s and %s GROUP BY category;",
        (start_date, end_date))
        data = cursor.fetchall()
        return data

def fetch_month():
    logger.info(f"fetching month by month summary")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT DATE_FORMAT(expense_date, '%Y-%m') AS month, SUM(amount) AS total_expenses FROM expense_manager.expenses GROUP BY DATE_FORMAT(expense_date, '%Y-%m') ORDER BY month;")
        data = cursor.fetchall()
        return data



'''
def fetch_user():
    logger.info(f"fetching user data")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT `User`, SUM(amount) AS total_expense FROM expense_manager.expenses GROUP BY `User` ORDER BY total_expense DESC;")
        data = cursor.fetchall()
        return data
'''


if __name__ == "__main__":
     expenses = fetch_expenses_for_date("2024-08-01")
     print(expenses)
     summary = fetch_expense_summary("2024-08-01", "2024-08-05")
     for record in summary:
         print(record)


