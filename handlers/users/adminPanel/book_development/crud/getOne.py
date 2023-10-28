from aiogram import types
import text
from keyboards.default.menu import *
from loader import dp, db


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('bookDev_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    data = db.selectOne(selected, "bookDev")
    print(data)
    btn = btnInlineWithStatus("bookD",text.btnGradeUpdate, data[0][0])
    await callback_query.message.edit_text(text=text.BookAboutMsg(data[0][0], data[0][1], data[0][2]), reply_markup=btn)