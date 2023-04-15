import datetime
from datetime import datetime
import sqlite3
from config import bot, dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from .keyboards import get_keyboard
from aiogram import types

from data_base.sqlite_db import *



async def expenses_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    # await bot.send_message(chat_id=callback_query.from_user.id, text='Выберите действие', reply_markup=get_keyboard('expenses_main'))

    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Выберите действие', reply_markup=get_keyboard('expenses_main'))



async def add_expenses_func(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    class States(StatesGroup):
        ask_expense_description = State()
        ask_expense_amount = State()

    await States.ask_expense_description.set()

    await bot.send_message(chat_id=callback_query.from_user.id, text='Введите описание расхода:')

    @dp.message_handler(state=States.ask_expense_description)
    async def ask_expense_amount(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['ask_expense_description'] = message.text

        await bot.send_message(chat_id=message.chat.id, text='Введите сумму расхода:')
    
        await States.next()

    @dp.message_handler(state=States.ask_expense_amount)
    async def save_expense(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['ask_expense_amount'] = message.text


        conn = sqlite3.connect('data_base/rashod.db')
        create_expenses_table()
        add_expense(conn, data['ask_expense_description'], data['ask_expense_amount'], datetime.now().strftime('%Y-%m-%d'))
        conn.close()

        await bot.send_message(chat_id=message.chat.id, text='Расход успешно добавлен в базу данных!')
        await state.finish()

        # Отправляем пользователю клавиатуру с основным меню
        await bot.send_message(chat_id=message.chat.id, text='Выберите один из пунктов меню:', reply_markup=get_keyboard('start'))
       
    


async def check_expenses_func(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Выберите действие', reply_markup=get_keyboard('expenses'))
   


async def expenses_1_day(callback_query: types.CallbackQuery,):
    await bot.answer_callback_query(callback_query.id)
    try:
        get_1_day = get_expenses_1_day()

        message_text = list()
        

        for result in get_1_day:
            messages = f"{result[1]}-{result[2]}"
            message_text.append(messages)

        message_text = '\n\n'.join(message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('expenses_main'))

    except Exception:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Расходов за сегодня не было', reply_markup=get_keyboard('expenses_main'))
    
  
    

async def expenses_1_week(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id)
    
    try:
        get_7_day = get_expenses_7_day()

        message_text = list()

        for result in get_7_day:
            messages = f"{result[1]}-{result[2]}"
            message_text.append(messages)

        message_text = '\n\n'.join(message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('expenses_main'))

    except Exception:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Расходов за неделю не было', reply_markup=get_keyboard('expenses_main'))



async def expenses_1_month(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        get_1_month = get_expenses_30_day()

        message_text = list()

        for result in get_1_month:
            messages = f"{result[1]}-{result[2]}"
            message_text.append(messages)

        message_text = '\n\n'.join(message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('expenses_main'))

    except Exception:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Расходов за месяц не было', reply_markup=get_keyboard('expenses_main'))

async def expenses_1_year(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:

        get_1_year = get_expenses_365_day()

        message_text = list()

        for result in get_1_year:
            messages = f"{result[1]}-{result[2]}"
            message_text.append(messages)

        message_text = '\n\n'.join(message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('expenses_main'))

    except Exception:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Расходов за год не было', reply_markup=get_keyboard('expenses_main'))



async def all_expenses(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:

        get_all_expenses = get_expenses_all()

        message_text = list()

        for result in get_all_expenses:
            messages = f"{result[1]}-{result[2]}"
            message_text.append(messages)

        message_text = '\n\n'.join(message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

        await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('expenses_main'))

    except Exception:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Расходов не было', reply_markup=get_keyboard('expenses_main'))


async def back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id = callback_query.message.message_id, text='Выберите действие', reply_markup=get_keyboard('start'))

