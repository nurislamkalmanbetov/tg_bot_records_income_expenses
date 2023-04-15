import datetime
from datetime import datetime
import sqlite3
from config import bot, dp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from data_base.sqlite_db import add_income
from .keyboards import get_keyboard
# from database import add_expense
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from data_base.sqlite_db import create_expenses_table, create_income_table, add_income, add_expense



async def expenses_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Выберите действие', reply_markup=get_keyboard('expenses'))


async def incomes_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Выберите действие', reply_markup=get_keyboard('incomes'))


# Расходы по очередности___________________________________________________________________________________

async def expenses_1_day(callback_query: types.CallbackQuery,):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Расход за день!!!!!!!')
    
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
       

async def expenses_1_week(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Расход за 1 неделю')

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



async def back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('start'))



async def expenses_1_month(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали Расход за месяц')

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


async def expenses_1_year(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали Расход за год')

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


async def all_expenses(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы выбрали Все расходы')



# Доход_______________________________________________________________________________________

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
    

async def incomes_1_day(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Доходы за один день')

    class States(StatesGroup):
        ask_date = State()
        show_incomes = State()

    await state.set_state(States.ask_date)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Введите дату в формате ГГГГ-ММ-ДД:')

    @dp.message_handler(state=States.ask_date)
    async def show_incomes_by_date(message: types.Message, state: FSMContext):
        date = message.text
        conn = sqlite3.connect('data_base/rashod.db')
        rows = get_incomes_by_date(conn, date)
        conn.close()

        if not rows:
            await bot.send_message(chat_id=message.chat.id, text=f'На {date} доходов не было')
            await state.finish()
            return

        total_income = 0
        for row in rows:
            total_income += row[2]
            await bot.send_message(chat_id=message.chat.id, text=f'{row[1]} - {row[2]} руб.')
        await bot.send_message(chat_id=message.chat.id, text=f'Общая сумма доходов на {date}: {total_income} руб.')

        await state.finish()

        # Отправляем пользователю клавиатуру с основным меню
        await bot.send_message(chat_id=message.chat.id, text='Выберите один из пунктов меню:', reply_markup=get_keyboard('start'))

