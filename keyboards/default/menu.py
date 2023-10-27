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