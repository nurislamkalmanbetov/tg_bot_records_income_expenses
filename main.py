from aiogram import Dispatcher
from aiogram.utils import executor
from handlers.callback import *
from data_base import sqlite_db
from sqlite3 import Error
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from config import dp, bot
from datetime import datetime

from data_base.sqlite_db import create_expenses_table, create_income_table, add_income, add_expense

# Подключаемся к базе данных
try:
    conn = sqlite3.connect('database/expenses_bot.db')
    print('База данных успешно подключена')
except Error as e:
    print(e)


create_expenses_table()


@dp.message_handler(commands = 'start')
async def process_start_commands(message : types.Message):         # reply_markup=kb_inline - указываем нашу клавиатуру
    await bot.send_message(chat_id= message.from_user.id, text='Здравствуйте! Бот пишет расходы и доходы\nВыберите команды', reply_markup = get_keyboard('start'))



@dp.message_handler(commands= 'help')
async def process_help_command(message : types.Message):
    await bot.send_message(chat_id = message.from_user.id, text = 'Ты нажал на кнопку help')


@dp.callback_query_handler(lambda callback: callback.data == 'expenses_kb')
async def process_expenses_main(callback_query: types.CallbackQuery):
    await expenses_main(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == 'incomes_kb')
async def process_expenses_main(callback_query: types.CallbackQuery):
    await incomes_main(callback_query)


@dp.callback_query_handler(lambda callback : callback.data == 'back')
async def process_back(callback_query : types.CallbackQuery):
    await back(callback_query)

# Expenses_kb____________________________________________________________________________

@dp.callback_query_handler(lambda callback : callback.data == '1_day')
async def process_1_day_callback(callback_query : types.CallbackQuery):
    await expenses_1_day(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == '1_week')
async def process_1_week_callback(callback_query: types.CallbackQuery):
    await expenses_1_week(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == '1_month')
async def process_1_month_callback(callback_query: types.CallbackQuery):
    await expenses_1_month(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == '1_year')
async def process_1_year_callback(callback_query: types.CallbackQuery):
    await expenses_1_year(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == 'all_expenses')
async def all_expenses_callback(callback_query: types.CallbackQuery):
    await all_expenses(callback_query)


# Доходная часть  ______________________________________________________________________________________


@dp.callback_query_handler(lambda callback: callback.data == 'income')
async def income_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await income(callback_query, state)


@dp.callback_query_handler(lambda callback : callback.data == '1_day_incomes')
async def process_1_day_callback(callback_query : types.CallbackQuery):
    await incomes_1_day(callback_query)

  

# ____________________________________________________________________________________________________

@dp.callback_query_handler(lambda callback : callback.data == 'back')
async def process_back(callback_query : types.CallbackQuery):
    await back(callback_query)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) # skip_updates=True - вне онлайна не будет работать 

