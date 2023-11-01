from aiogram import types
import text
from handlers.users.start import auth
from keyboards.default.menu import *
from loader import dp, db, bot
from secret import CHANNEL_ID


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('LogicQList_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    data = db.selectOne(selected, "logic_questions")

    await callback_query.message.answer(text=text.UserLogicQ(data[0][1], data[0][2]))