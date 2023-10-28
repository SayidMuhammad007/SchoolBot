from aiogram.dispatcher.filters.state import State, StatesGroup

class AddBookState(StatesGroup):
    name = State()
    file = State()
    caption = State()
    confirm = State()

class UpdateBookState(StatesGroup):
    id = State()
    name = State()
    file = State()
    caption = State()
    confirm = State()

class DeleteBookState(StatesGroup):
    id = State()
    confirm = State()