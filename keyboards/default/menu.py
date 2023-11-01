from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
def btns(request):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in request:
        btn.insert(i)
    return btn

def btnInline(request):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for i in request:
        button = InlineKeyboardButton(i, callback_data=f"{i}")
        keyboard.insert(button)
    return keyboard

def btnInlineWithStatus(status, request, id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for i in request:
        button = InlineKeyboardButton(i, callback_data=f"{status}_{i}_{id}")
        keyboard.insert(button)
    return keyboard

def btnInlineWithLetter(status, request):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for i in request:
        button = InlineKeyboardButton(text=f"{i[1]}-{i[2]}", callback_data=f"{status}_{i}_{i[0]}")
        keyboard.insert(button)
    return keyboard