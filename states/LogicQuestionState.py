from aiogram.dispatcher.filters.state import State, StatesGroup

class LogicQuestionState(StatesGroup):
    question = State()
    answer = State()
    confirm = State()