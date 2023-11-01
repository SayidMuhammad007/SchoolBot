from aiogram.dispatcher.filters.state import State, StatesGroup

class LessonDayState(StatesGroup):
    grade = State()
    day = State()
    lessons = State()
    confirm = State()

class LessonState(StatesGroup):
    day = State()