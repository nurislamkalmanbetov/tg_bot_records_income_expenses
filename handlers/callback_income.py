
import datetime
from datetime import datetime
import sqlite3
from config import bot, dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from data_base.sqlite_db import add_income
from .keyboards import get_keyboard
from aiogram import types
from data_base.sqlite_db import *






async def incomes_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id,text='Выберите действие', reply_markup=get_keyboard('incomes'))



async def check_income_func(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id, text='Выберите действие', reply_markup=get_keyboard('incomes_kb'))


async def income(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Доходы')

    class States(StatesGroup):
        ask_income_description = State()
        ask_income_amount = State()

    async with state.proxy() as data:
        data['type'] = 'income'

    await state.set_state(States.ask_income_description)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Введите описание дохода:')

    @dp.message_handler(state=States.ask_income_description)
    async def ask_income_amount(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['description'] = message.text

        await state.set_state(States.ask_income_amount)
        await bot.send_message(chat_id=message.chat.id, text='Введите сумму дохода:')

    @dp.message_handler(state=States.ask_income_amount)
    async def save_income(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['amount'] = message.text

        conn = sqlite3.connect('data_base/rashod.db')
        create_income_table(conn)
        add_income(conn, data['description'], data['amount'], datetime.now().strftime('%Y-%m-%d'))
        conn.close()

        await bot.send_message(chat_id=message.chat.id, text='Доход успешно добавлен в базу данных!')
        await state.finish()

        # Отправляем пользователю клавиатуру с основным меню
        await bot.send_message(chat_id=message.chat.id, text='Выберите один из пунктов меню:', reply_markup=get_keyboard('start'))
    


async def income_1_day(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    get_1_day = get_income_1_day()

    message_text = list()


    message_text = list()

    for result in get_1_day:
        messages = f"{result[1]}-{result[2]}"
        message_text.append(messages)

    message_text = '\n\n'.join(message_text)

    await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

    await bot.send_message(chat_id=callback_query.message.chat.id, text='Главное меню:', reply_markup=get_keyboard('incomes'))
    

async def income_7_day(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    get_7_day = get_income_7_day()

    message_text = list()

    for result in get_7_day:
        messages = f"{result[1]}-{result[2]}"
        message_text.append(messages)

    message_text = '\n\n'.join(message_text)

    await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

    await bot.send_message(chat_id=callback_query.message.chat.id, text='Главное меню:', reply_markup=get_keyboard('incomes'))
    

async def income_30_day(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    get_30_day = get_income_30_day()

    message_text = list()

    for result in get_30_day:
        messages = f"{result[1]}-{result[2]}"
        message_text.append(messages)

    message_text = '\n\n'.join(message_text)

    await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

    await bot.send_message(chat_id=callback_query.message.chat.id, text='Главное меню:', reply_markup=get_keyboard('incomes'))
    

async def income_365_day(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    get_365_day = get_income_365_day()

    message_text = list()

    for result in get_365_day:
        messages = f"{result[1]}-{result[2]}"
        message_text.append(messages)

    message_text = '\n\n'.join(message_text)

    await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

    await bot.send_message(chat_id=callback_query.message.chat.id, text='Главное меню:', reply_markup=get_keyboard('incomes'))
    

async def income_all(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    get_all = get_income_all()

    message_text = list()

    for result in get_income_all:
        messages = f"{result[1]}-{result[2]}"
        message_text.append(messages)

    message_text = '\n\n'.join(message_text)

    await bot.send_message(chat_id=callback_query.from_user.id, text=message_text)

    await bot.send_message(chat_id=callback_query.message.chat.id, text='Главное меню:', reply_markup=get_keyboard('incomes'))
    
    

