from aiogram.dispatcher.filters.state import State, StatesGroup

class AddBookState(StatesGroup):
    name = State()
    file = State()
    caption = State()
    confirm = State()