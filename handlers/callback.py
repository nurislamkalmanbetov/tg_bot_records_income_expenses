import datetime
import sqlite3
from config import bot, dp
from data_base.sqlite_db import add_income
from .keyboards import get_keyboard
# from database import add_expense
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


async def expenses_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Выберите действие', reply_markup=get_keyboard('expenses'))


async def incomes_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Выберите действие', reply_markup=get_keyboard('incomes'))


# Расходы по очередности___________________________________________________________________________________

async def expenses_1_day(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Расход за день\nВведите сумму')


async def expenses_1_week(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Расход за 1 неделю')


async def back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('start'))


async def expenses_1_month(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали Расход за месяц')


async def expenses_1_year(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали Расход за год')


async def all_expenses(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали Все расходы')



# Доходы по очередности__________________________________________________________________________________


# async def ask_income_description(message: types.Message):
#     await bot.send_message(chat_id=message.chat.id, text='Введите описание дохода:')


    
async def ask_income_description(message: types.Message):
    print('nahuuuuuuuuuuuuuuuuuuuuuuui')
    await bot.send_message(chat_id=message.chat.id, text='Введите описание дохода:')
    dp.register_message_handler(ask_income_amount, chat_id=message.chat.id)

async def ask_income_amount(message: types.Message):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    description = message.text
    await bot.send_message(chat_id=message.chat.id, text='Введите сумму дохода:')
    dp.register_message_handler(ask_income_date, chat_id=message.chat.id, args=(description,))

async def ask_income_date(message: types.Message, description):
    amount = message.text
    await bot.send_message(chat_id=message.chat.id, text='Введите дату дохода в формате день/месяц/год:')
    dp.register_message_handler(save_income, chat_id=message.chat.id, args=(description, amount))

async def save_income(message: types.Message, description, amount):
    date = message.text
    conn = sqlite3.connect('data_base/rashod.db')
    add_income(conn, description, amount, date)
    conn.close()
    await bot.send_message(chat_id=message.chat.id, text='Доход успешно добавлен в базу данных!')

