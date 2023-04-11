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
            date TEXT
        )
    """)
    conn.commit()


def add_income(conn, description, amount, date):
    """
    Функция добавления дохода в таблицу "income" базы данных.

    :param conn: объект подключения к базе данных
    :param description: описание дохода
    :param amount: сумма дохода
    :param date: дата дохода в формате день/месяц/год
    :return: None
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO income (description, amount, date) VALUES (?, ?, ?)", (description, amount, date))
        conn.commit()
    except Error as e:
        print(e)
