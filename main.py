from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import dp, bot
from handlers.keyboards import get_keyboard # kb, kb_inline, kb_markup
from handlers.callback import *


# bot = Bot(TOKEN)
# dp = Dispatcher(bot)


@dp.message_handler(commands = 'start')
async def process_start_commands(message : types.Message):         # reply_markup=kb_inline - указываем нашу клавиатуру
    await bot.send_message(chat_id= message.from_user.id, text='Здравствуйте! Бот пишет расходы и доходы\nВыберите команды', reply_markup = get_keyboard('start'))


@dp.message_handler(commands= 'help')
async def process_help_command(message : types.Message):
    await bot.send_message(chat_id = message.from_user.id, text = 'Ты нажал на кнопку help')


@dp.callback_query_handler(lambda callback : callback.data == '1_day')
async def process_1_day_callback(callback_query : types.CallbackQuery):
    await expenses_1_day(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == 'expenses_kb')
async def process_expenses_main(callback_query: types.CallbackQuery):
    await expenses_main(callback_query)


@dp.callback_query_handler(lambda callback: callback.data == 'incomes_kb')
async def process_expenses_main(callback_query: types.CallbackQuery):
    await incomes_main(callback_query)


@dp.callback_query_handler(lambda callback : callback.data == 'back')
async def process_back(callback_query : types.CallbackQuery):
    await back(callback_query)


# @dp.message_handler()
# async def procces_hello_command(message : types.Message):
#     if message.text.lower() == 'расходы':
#         await bot.send_message(chat_id = message.from_user.id, text = 'Выберите действие', reply_markup = get_keyboard('expenses'))
#     elif message.text.lower() == 'доходы':
#         await bot.send_message(chat_id = message.from_user.id, text = 'Выберите действие', reply_markup = get_keyboard('incomes'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) # skip_updates=True - вне онлайна не будет работать 

