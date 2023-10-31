from aiogram.dispatcher.filters.state import State, StatesGroup

class LogicQuestionState(StatesGroup):
    question = State()
    answer = State()
    confirm = State()

class UpdateLogicQuestionState(StatesGroup):
    question = State()
    answer = State()
    confirm = State()

class DeleteLogicQuestionState(StatesGroup):
    confirm = State()