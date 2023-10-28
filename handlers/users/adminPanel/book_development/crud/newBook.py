from aiogram import types
from aiogram.dispatcher import FSMContext

import text
from keyboards.default.menu import *
from loader import dp, db
from secret import CHANNEL_ID
from states.BookState import AddBookState


# Echo bot
@dp.message_handler(text=text.btnBooksMenu[1])
async def bot_echo(message: types.Message):
    await message.answer(text=text.inputBookName)
    await AddBookState.name.set()

@dp.message_handler(state=AddBookState.name)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({"name" : message.text})
    await message.answer(text=text.inputBookDesc)
    await AddBookState.caption.set()

@dp.message_handler(state=AddBookState.caption)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({"caption" : message.text})
    await message.answer(text=text.sendPDF)
    await AddBookState.file.set()

@dp.message_handler(state=AddBookState.file, content_types=types.ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message, state:FSMContext):
    sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({"file":post_link})
    btn = btnInline(text.confirmBtn)
    await message.answer(text=text.confirmBook, reply_markup=btn)
    await AddBookState.confirm.set()

@dp.message_handler(state=AddBookState.file, content_types=types.ContentTypes.ANY)
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text=text.sendFile)

@dp.callback_query_handler(state=AddBookState.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.delete()
    btn = btns(text.btnBooksMenu)
    if callback.data == text.confirmBtn[0]:
        data = await state.get_data()
        name = data.get('name')
        caption = data.get('caption')
        file = data.get('file')
        db.addBookDev(name, caption, file)
        await callback.message.answer(text=text.saved, reply_markup=btn)
    else:
        await callback.message.answer(text=text.cancel, reply_markup=btn)
    await state.finish()

