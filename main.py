from aiogram import Dispatcher
from aiogram.utils import executor
from handlers.callback_expenses import *
from data_base import sqlite_db
from sqlite3 import Error
from aiogram.dispatcher import FSMContext
from config import dp, bot
from handlers.callback_income import *

from data_base.sqlite_db import create_expenses_table

# Подключаемся к базе данных
try:
    conn = sqlite3.connect('database/expenses_bot.db')
    print('База данных успешно подключена')
except Error as e:
    print(e)


create_expenses_table()


@dp.message_handler(commands = 'start')
async def process_start_commands(message : types.Message):         # reply_markup=kb_inline - указываем нашу клавиатуру
    print(message.from_user.id)
    await bot.send_message(chat_id= message.from_user.id, text='Здравствуйте! Бот пишет расходы и доходы\nВыберите команды', reply_markup = get_keyboard('start'))



@dp.message_handler(commands= 'help')
async def process_help_command(message : types.Message):
    await bot.send_message(chat_id = message.from_user.id, text = 'Ты нажал на кнопку help')

@dp.message_handler(commands= 'admin')
async def process_admin_command(message : types.Message):
    user_id = message.from_user.id
    if user_id == 5873445472:
        await bot.send_message(chat_id = message.from_user.id, text = 'Привет Администратор!', reply_markup=get_keyboard('admin'))


@dp.callback_query_handler(lambda callback: callback.data == 'delete_expenses')
async def process_delete_expenses(callback_query: types.CallbackQuery):
    delete_all_expenses()

    await callback_query.message.answer('Данные расходов успешно удалены', reply_markup=get_keyboard('admin'))
    
@dp.callback_query_handler(lambda callback: callback.data == 'delete_incomes')
async def process_delete_incomes(callback_query: types.CallbackQuery):
    delete_all_income()

    await callback_query.message.answer('Данные доходов успешно удалены', reply_markup=get_keyboard('admin'))

@dp.callback_query_handler(lambda callback: callback.data == 'expenses_kb')
async def process_expenses_main(callback_query: types.CallbackQuery):
    await expenses_main(callback_query)



@dp.callback_query_handler(lambda callback: callback.data == 'incomes_kb')
async def process_expenses_main(callback_query: types.CallbackQuery):
    await incomes_main(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == 'add_expenses')
async def process_add_expenses(callback_query: types.CallbackQuery):
    await add_expenses_func(callback_query)

@dp.callback_query_handler(lambda callback: callback.data == 'check_expenses')
async def process_check_expenses(callback_query: types.CallbackQuery):
    await check_expenses_func(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == 'check_income')
async def process_check_income(callback_query: types.CallbackQuery):
    await check_income_func(callback_query)


@dp.callback_query_handler(lambda callback : callback.data == 'back_check_expenses')
async def process_back_check_expenses(callback_query : types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,text= 'Выберите действие', reply_markup = get_keyboard('expenses_main'))



@dp.callback_query_handler(lambda callback : callback.data == 'back_check_incomes')
async def process_back_check_income(callback_query : types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text= 'Выберите действие', reply_markup = get_keyboard('incomes'))


# Expenses_kb____________________________________________________________________________

@dp.callback_query_handler(lambda callback : callback.data == '1_day_expenses')
async def process_1_day_callback(callback_query : types.CallbackQuery):
    await expenses_1_day(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == '1_week_expenses')
async def process_1_week_callback(callback_query: types.CallbackQuery):
    await expenses_1_week(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == '1_month_expenses')
async def process_1_month_callback(callback_query: types.CallbackQuery):
    await expenses_1_month(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == '1_year_expenses')
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
    await income_1_day(callback_query)



@dp.callback_query_handler(lambda callback: callback.data == '1_week_incomes')
async def process_1_week_callback(callback_query: types.CallbackQuery):
    await income_7_day(callback_query)




  

# ____________________________________________________________________________________________________

@dp.callback_query_handler(lambda callback : callback.data == 'back')
async def process_back(callback_query : types.CallbackQuery):
    await back(callback_query)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) # skip_updates=True - вне онлайна не будет работать 

