from aiogram import types
from config import bot, dp
from .keyboards import get_keyboard


async def expenses_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id = callback_query.from_user.id, text = 'Выберите действие', reply_markup = get_keyboard('expenses')) 


async def incomes_main(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id = callback_query.from_user.id, text = 'Выберите действие', reply_markup = get_keyboard('incomes')) 




async def expenses_1_day(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Расход за день')

async def expenses_1_week(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Вы нажали на кнопку Расход за 1 неделю')

async def back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text='Главное меню', reply_markup=get_keyboard('start'))    
