from aiogram import types
import text
from keyboards.default.menu import *
from loader import dp, db


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('Logic_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    data = db.selectOne(selected, "logic_questions")
    btn = btnInlineWithStatus("LogicId",text.btnGradeUpdate, data[0][0])
    await callback_query.message.edit_text(text=text.QuestionOne(data[0][1], data[0][2]), reply_markup=btn)