import sqlite3
from sqlite3 import Error
from aiogram import types


def create_expenses_table():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount INTEGER,
            date TEXT DEFAULT (date('now','localtime'))
        )
    ''')
    conn.commit()
    conn.close()


def create_income_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount INTEGER,
            date TEXT DEFAULT (date('now','localtime'))
        )
    """)
    conn.commit()
   

def add_income(conn, description, amount, date):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO income (description, amount, date) VALUES (?, ?, ?)", (description, amount, date))
    conn.commit()


def add_expense(conn, description, amount, date):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)", (description, amount, date))
    conn.commit()


def get_incomes_by_date(conn, date):
    """
    Retrieves all income records for a given date.
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM income WHERE date = ?", (date,))
    rows = cur.fetchall()
    return rows