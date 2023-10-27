from aiogram.dispatcher.filters.state import State, StatesGroup

class GradeState(StatesGroup):
    grade = State()
    type = State()
    confirm = State()