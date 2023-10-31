from aiogram.dispatcher.filters.state import State, StatesGroup

class AddSchoolBook(StatesGroup):
    grade = State()
    book = State()
    pdf = State()
    confirm = State()