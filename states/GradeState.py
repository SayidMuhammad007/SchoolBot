from aiogram.dispatcher.filters.state import State, StatesGroup

class GradeState(StatesGroup):
    id = State()
    grade = State()
    type = State()
    confirm = State()

class UpdateGradeState(StatesGroup):
    id = State()
    grade = State()
    type = State()
    confirm = State()

class DeleteGrade(StatesGroup):
    id = State()
    confirm = State()