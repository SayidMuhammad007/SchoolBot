from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.users.start import auth
from keyboards.default.menu import btns, btnInline
from loader import dp, db
import text
from states.SchoolBookState import DeleteSchoolBook


@dp.callback_query_handler(state=DeleteSchoolBook.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    if callback.data == text.confirmBtn[0]:
        data = await state.get_data()
        id = data.get("id")
        db.deleteSchoolB(id)
        await callback.message.delete()
        await callback.message.answer(text=text.deleted)
    else:
        await callback.message.delete()
        await callback.message.answer(text=text.cancel)
    await state.finish()
    btn = btns(text.btnSchoolBook)
    await callback.message.answer(text=text.choose, reply_markup=btn)