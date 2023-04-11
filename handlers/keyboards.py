from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def get_keyboard(name: str):
    if name == 'start':
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton('Расходы', callback_data='expenses_kb'))
        keyboard.add(InlineKeyboardButton('Доходы', callback_data='incomes_kb'))
        keyboard.add(InlineKeyboardButton('Тех.поддержка', url='https://t.me/NurislamKalmanbetov'))
    elif name == 'expenses':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Расход за день', callback_data='1_day'))
        keyboard.add(InlineKeyboardButton('Расход за неделю', callback_data='1_week'))
        keyboard.add(InlineKeyboardButton('Расход за месяц', callback_data='1_month'))
        keyboard.add(InlineKeyboardButton('Расход за год', callback_data='1_year'))
        keyboard.add(InlineKeyboardButton('Все расходы', callback_data='all_expenses'))
        keyboard.add(InlineKeyboardButton('Назад', callback_data='back'))
    elif name == 'incomes':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Написать доход', callback_data='income'))
        keyboard.add(InlineKeyboardButton('Назад', callback_data='back'))


    return keyboard










# kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# kb.add(KeyboardButton('Привет'))
# kb.add(KeyboardButton('Помощь'))

# kb_inline = InlineKeyboardMarkup(resize_keyboard=True)
# kb_inline.add(InlineKeyboardButton('Привет', callback_data='hello'))
# kb_inline.add(InlineKeyboardButton('Помощь', callback_data='help'))
# kb_inline.add(InlineKeyboardButton('You Tube', url='https://www.youtube.com'))

# kb_markup = ReplyKeyboardMarkup(resize_keyboard=True)

# # kb_markup.row(KeyboardButton('Как дела?'))
# # kb_markup.row(KeyboardButton('Как погода?'))
# # kb_markup.row(KeyboardButton('Как настроение?'))

# kb_markup.add(KeyboardButton('Как дела?'), KeyboardButton('Как настроение? '))

# если клавиатур много 















