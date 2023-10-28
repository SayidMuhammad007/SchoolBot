from aiogram import types
from aiogram.dispatcher import FSMContext

import text
from keyboards.default.menu import btns
from loader import dp, db
from states.BookState import DeleteBookState


# Echo bot
@dp.callback_query_handler(state=DeleteBookState.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    btn = btns(text.btnBooksMenu)
    if callback.data == text.confirmBtn[0]:
        await callback.message.delete()
        data = await state.get_data()
        id = data.get("id")
        db.deleteBookD(id)
        await callback.message.answer(text=text.deleted, reply_markup=btn)
    else:
        await callback.message.delete()
        await callback.message.answer(text=text.cancel, reply_markup=btn)
    await state.finish()

