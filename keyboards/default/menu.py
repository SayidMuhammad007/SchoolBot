from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Школьные книги"),
            KeyboardButton(text="Логические вопросы"),
        ],
        [
            KeyboardButton(text="Книги для развития"),
            KeyboardButton(text="Информация об учителях"),
        ],
        [
            KeyboardButton(text="Список уроков"),
        ],
    ]
)

btnAdmin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Классы"),
            KeyboardButton(text="Логические вопросы"),
        ],
        [
            KeyboardButton(text="Книги для развития"),
            KeyboardButton(text="Школьные книги"),
        ],
        [
            KeyboardButton(text="Список уроков")
        ]
    ]
)