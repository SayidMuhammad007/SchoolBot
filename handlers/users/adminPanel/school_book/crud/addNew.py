from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.users.start import auth
from keyboards.default.menu import btns, btnInline
from loader import dp, db
import text
from secret import CHANNEL_ID
from states.GradeState import GradeState
from states.LogicQuestionState import LogicQuestionState
from states.SchoolBookState import AddSchoolBook


# Echo bot
@dp.message_handler(text=text.btnSchoolBook[1])
async def bot_echo(message: types.Message):
    await message.answer(text=text.inputSchoolBookGrade, reply_markup=ReplyKeyboardRemove())
    await AddSchoolBook.grade.set()

@dp.message_handler(state=AddSchoolBook.grade)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'grade': message.text})
    await message.answer(text=text.inputSchoolBookName)
    await AddSchoolBook.book.set()



@dp.message_handler(state=AddSchoolBook.book)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'book': message.text})
    await message.answer(text=text.sendPDF, reply_markup=ReplyKeyboardRemove())
    await AddSchoolBook.pdf.set()

@dp.message_handler(state=AddSchoolBook.pdf, content_types=types.ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message, state:FSMContext):
    sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({"file":post_link})
    btn = btnInline(text.confirmBtn)
    await message.answer(text=text.confirmBook, reply_markup=btn)
    await AddSchoolBook.confirm.set()

@dp.message_handler(state=AddSchoolBook.pdf, content_types=types.ContentTypes.ANY)
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text=text.sendFile)

@dp.callback_query_handler(state=AddSchoolBook.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    if callback.data == text.confirmBtn[0]:
        data = await state.get_data()
        grade = data.get("grade")
        book = data.get("book")
        file = data.get("file")
        db.addSchoolBook(grade, book, file)
        btn = btns(text.btnLogicQuestion)
        await callback.message.delete()
        await callback.message.answer(text=text.saved, reply_markup=btn)
    else:
        msg, btn = await auth(callback)
        await callback.message.delete()
        await callback.message.answer(text=text.cancel, reply_markup=btn)
    await state.finish()