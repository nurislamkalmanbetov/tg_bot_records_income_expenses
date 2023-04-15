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
            date DATETIME DEFAULT (datetime('now'))
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
            date DATETIME DEFAULT (datetime('now'))
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




def get_expenses_1_day():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date >= datetime('now', '-1 day');")
    rows = cursor.fetchall()
    return rows


def get_expenses_7_day():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date >= datetime('now', '-7 day');")
    rows = cursor.fetchall()
    return rows


def get_expenses_30_day():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date >= datetime('now', '-30 day');")
    rows = cursor.fetchall()
    return rows


def get_expenses_365_day():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date >= datetime('now', '-365 day');")
    rows = cursor.fetchall()
    return rows

def get_expenses_all():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses;")
    rows = cursor.fetchall()
    return rows



def get_income_1_day():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income WHERE date >= datetime('now', '-1 day');")
    rows = cursor.fetchall()
    return rows


def get_income_7_day():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income WHERE date >= datetime('now', '-7 day');")
    rows = cursor.fetchall()
    return rows


def get_income_30_day():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income WHERE date >= datetime('now', '-30 day');")
    rows = cursor.fetchall()
    return rows


def get_income_365_day():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income WHERE date >= datetime('now', '-365 day');")
    rows = cursor.fetchall()
    return rows

def get_income_all():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income;")
    rows = cursor.fetchall()
    return rows


def delete_all_expenses():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses;")
    conn.commit()


def delete_all_income():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM income;")
    conn.commit()
