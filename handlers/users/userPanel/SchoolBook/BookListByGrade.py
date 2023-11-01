from aiogram import types

from loader import dp


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('GradeList_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    print(selected)
