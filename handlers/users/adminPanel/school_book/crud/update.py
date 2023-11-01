from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.users.start import auth
from keyboards.default.menu import btns, btnInline
from loader import dp, db
import text
from secret import CHANNEL_ID
from states.LogicQuestionState import DeleteLogicQuestionState
from states.SchoolBookState import UpdateSchoolBook, DeleteSchoolBook


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('SchoolId_'))
async def handle_product_deletion(callback: types.CallbackQuery, state:FSMContext):
    selected = callback.data.split('_')[1]
    id = callback.data.split('_')[2]
    print(id)
    await state.update_data({"id": id})
    if selected == text.btnGradeUpdate[0]:
        await callback.message.edit_text(text=text.inputSchoolBookGrade)
        await UpdateSchoolBook.grade.set()
    elif selected == text.btnGradeUpdate[2]:
        btn = btns(text.btnGradeMenu)
        await callback.message.delete()
        await callback.message.answer(text=text.choose, reply_markup=btn)
        await state.finish()
    else:
        btn = btnInline(text.confirmBtn)
        await callback.message.edit_text(text=text.delete, reply_markup=btn)
        await DeleteSchoolBook.confirm.set()

@dp.message_handler(state=UpdateSchoolBook.grade)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'grade': message.text})
    await message.answer(text=text.inputSchoolBookName)
    await UpdateSchoolBook.book.set()

@dp.message_handler(state=UpdateSchoolBook.book)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'book': message.text})
    await message.answer(text=text.sendPDF, reply_markup=ReplyKeyboardRemove())
    await UpdateSchoolBook.pdf.set()

@dp.message_handler(state=UpdateSchoolBook.pdf, content_types=types.ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message, state:FSMContext):
    sent_message = await message.copy_to(chat_id="@"+CHANNEL_ID)
    post_link = f"https://t.me/{CHANNEL_ID}/{sent_message.message_id}"
    await state.update_data({"file":post_link})
    btn = btnInline(text.confirmBtn)
    await message.answer(text=text.confirmBook, reply_markup=btn)
    await UpdateSchoolBook.confirm.set()

@dp.message_handler(state=UpdateSchoolBook.pdf, content_types=types.ContentTypes.ANY)
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text=text.sendFile)

@dp.callback_query_handler(state=UpdateSchoolBook.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    if callback.data == text.confirmBtn[0]:
        data = await state.get_data()
        grade = data.get("grade")
        book = data.get("book")
        file = data.get("file")
        id = data.get("id")
        db.updateSchoolB(grade, book, file, id)
        btn = btns(text.btnSchoolBook)
        await callback.message.delete()
        await callback.message.answer(text=text.saved, reply_markup=btn)
    else:
        msg, btn = await auth(callback)
        await callback.message.delete()
        await callback.message.answer(text=text.cancel, reply_markup=btn)
    await state.finish()