from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.users.start import auth
from keyboards.default.menu import btns, btnInline
from loader import dp, db
import text
from secret import CHANNEL_ID
from states.BookState import *



@dp.message_handler(state=UpdateBookState.name)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'name': message.text})
    await message.answer(text=text.inputBookDesc)
    await UpdateBookState.caption.set()

@dp.message_handler(state=UpdateBookState.caption)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'caption': message.text})
    await message.answer(text=text.sendPDF)
    await UpdateBookState.file.set()

@dp.message_handler(state=UpdateBookState.file, content_types=types.ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message, state:FSMContext):
    sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({"file":post_link})
    data = await state.get_data()
    name = data.get("name")
    id = data.get("id")
    caption = data.get("caption")
    msg = text.BookAboutMsg(id, name, caption)
    btn = btnInline(text.confirmBtn)
    await message.answer(text=msg, reply_markup=btn)
    await UpdateBookState.confirm.set()

@dp.callback_query_handler(state=UpdateBookState.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    if callback.data == text.confirmBtn[0]:
        data = await state.get_data()
        name = data.get("name")
        id = data.get("id")
        caption = data.get("caption")
        file = data.get("file")
        db.updateBookD(name, caption, file, id)
        btn = btns(text.btnBooksMenu)
        await callback.message.delete()
        await callback.message.answer(text=text.saved, reply_markup=btn)
    else:
        msg, btn = await auth(callback)
        await callback.message.delete()


        await callback.message.answer(text=text.cancel, reply_markup=btn)
    await state.finish()