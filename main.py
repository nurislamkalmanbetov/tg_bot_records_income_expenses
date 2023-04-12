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

    # class Fsm(StatesGroup):
    #     name = State()
    #     age = State()
    #     profession = State()

    # await Fsm.name.set()
    # await message.answer('Введите имя')

    

    # @dp.message_handler(state=Fsm.name)
    # async def names(message: types.Message, state: FSMContext):
    #     async with state.proxy() as data:
    #         data['name'] = message.text

    #     await message.answer("age")

    #     await Fsm.next()

    # @dp.message_handler(state=Fsm.age)
    # async def names6(message: types.Message, state: FSMContext):
    #     async with state.proxy() as data:
    #         data['age'] = message.text

    #         await message.answer('prof')

    #     await Fsm.next()
    # @dp.message_handler(state=Fsm.profession)
    # async def names2(message: types.Message, state: FSMContext):
    #     async with state.proxy() as data:
    #         data['profession'] = message.text



    #     data = await state.get_data()
    #     print(data)

    #     name = data['name']
    #     age = data['age']
    #     prof = data['profession']
    #     await message.answer(f'Ваше имя {name}\nВозраст {age}\nПроф {prof}')
    #     await state.finish()


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



@dp.callback_query_handler(lambda callback_query: callback_query.data == 'income')
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



# _ 
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'expense_1_day')
async def expense_1_day(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Расходы за 1 день')

    class States(StatesGroup):
        ask_expense_description = State()
        ask_expense_amount = State()

    async with state.proxy() as data:
        data['type'] = 'expense'

    await state.set_state(States.ask_expense_description)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Введите описание расхода:')

    @dp.message_handler(state=States.ask_expense_description)
    async def ask_expense_amount(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['description'] = message.text

        await state.set_state(States.ask_expense_amount)
        await bot.send_message(chat_id=message.chat.id, text='Введите сумму расхода:')

    @dp.message_handler(state=States.ask_expense_amount)
    async def save_expense(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['amount'] = message.text

        conn = sqlite3.connect('data_base/rashod.db')
        create_expenses_table(conn)
        add_expense(conn, data['description'], data['amount'], datetime.now().strftime('%Y-%m-%d'))
        conn.close()

        await bot.send_message(chat_id=message.chat.id, text='Расход успешно добавлен в базу данных!')
        await state.finish()

        # Отправляем пользователю клавиатуру с основным меню
        await bot.send_message(chat_id=message.chat.id, text='Выберите один из пунктов меню:', reply_markup=get_keyboard('start'))

        

# _

@dp.callback_query_handler(lambda callback : callback.data == 'back')
async def process_back(callback_query : types.CallbackQuery):
    await back(callback_query)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) # skip_updates=True - вне онлайна не будет работать 

