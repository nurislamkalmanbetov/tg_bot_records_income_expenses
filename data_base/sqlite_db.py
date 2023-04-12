import sqlite3
from sqlite3 import Error
from aiogram import types


def create_expenses_table():
    conn = sqlite3.connect('data_base/rashod.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            description TEXT,
            date DATE
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
            amount REAL,
            date TEXT DEFAULT (date('now','localtime'))
        )
    """)
    conn.commit()

    

def add_income(conn, description, amount, date):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO income (description, amount, date) VALUES (?, ?, ?)", (description, amount, date))
    conn.commit()



def add_expense(conn, description, amount, date):
    """
    Функция добавления расхода в таблицу "expenses" базы данных.

    :param conn: объект соединения с базой данных
    :param amount: сумма расхода
    :param description: описание расхода
    :param date: дата расхода
    :return: None
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (amount, description, date) VALUES (?, ?, ?)",
                       (amount, description, date))
        conn.commit()
    except Error as e:
        print(e)

