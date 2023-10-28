from aiogram import types

import text
from keyboards.default.menu import btns
from loader import dp


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('bookD_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    btn = btns(text.btnBooksMenu)
    await callback_query.message.delete()
    await callback_query.message.answer(text=text.choose, reply_markup=btn)
