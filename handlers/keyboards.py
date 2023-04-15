from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def get_keyboard(name: str):
    if name == 'start':
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton('Расходы', callback_data='expenses_kb'))
        keyboard.add(InlineKeyboardButton('Доходы', callback_data='incomes_kb'))
        keyboard.add(InlineKeyboardButton('Тех.поддержка 💻', url='https://t.me/NurislamKalmanbetov'))

    elif name == 'expenses_main':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Написать расход', callback_data='add_expenses'))
        keyboard.add(InlineKeyboardButton('Посмотреть расходы', callback_data='check_expenses'))
        keyboard.add(InlineKeyboardButton('Назад 🔙', callback_data='back'))

    elif name == 'expenses':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Расход за день', callback_data='1_day_expenses'))
        keyboard.add(InlineKeyboardButton('Расход за неделю', callback_data='1_week_expenses'))
        keyboard.add(InlineKeyboardButton('Расход за месяц', callback_data='1_month_expenses'))
        keyboard.add(InlineKeyboardButton('Расход за год', callback_data='1_year_expenses'))
        keyboard.add(InlineKeyboardButton('Все расходы', callback_data='all_expenses'))
        keyboard.add(InlineKeyboardButton('Назад 🔙', callback_data='back_check_expenses'))


    elif name == 'incomes':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Написать доход', callback_data='income'))
        keyboard.add(InlineKeyboardButton('Посмотреть доходы', callback_data='check_income'))
        keyboard.add(InlineKeyboardButton('Назад 🔙', callback_data='back'))

    elif name == 'incomes_kb':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Доход за день', callback_data='1_day_incomes'))
        keyboard.add(InlineKeyboardButton('Доход за неделю', callback_data='1_week_incomes'))
        keyboard.add(InlineKeyboardButton('Доход за месяц', callback_data='1_month_incomes'))
        keyboard.add(InlineKeyboardButton('Доход за год', callback_data='1_year_incomes'))
        keyboard.add(InlineKeyboardButton('Все Доходы', callback_data='all_incomes'))
        keyboard.add(InlineKeyboardButton('Назад 🔙', callback_data='back_check_incomes'))

    elif name == 'admin':
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton('Удалить записи расходов', callback_data='delete_expenses'))
        keyboard.add(InlineKeyboardButton('Удалить записи доходов', callback_data='delete_incomes'))
        keyboard.add(InlineKeyboardButton('Назад 🔙', callback_data='back'))

    return keyboard

