from aiogram import types
import text
from handlers.users.start import auth
from keyboards.default.menu import *
from loader import dp, db, bot
from secret import CHANNEL_ID


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('SchoolBookList_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    data = db.selectOne(selected, "school_book")
    txt = data[0][3]
    x = txt.split('/')
    id = x[-1]
    book = await bot.copy_message(chat_id=callback_query.from_user.id, from_chat_id=f"@{CHANNEL_ID}", message_id=id)
    # await callback_query.message.edit_text(text=book)