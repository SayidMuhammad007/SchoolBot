from aiogram import types
from aiogram.dispatcher import FSMContext

import text
from keyboards.default.menu import btns, btnInline
from loader import dp
from states.BookState import UpdateBookState, DeleteBookState


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('bookD_'))
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    selected = callback_query.data.split('_')[1]
    id = callback_query.data.split('_')[2]
    await callback_query.message.delete()
    await state.update_data({'id': id})
    if selected == text.btnGradeUpdate[2]:
        btn = btns(text.btnBooksMenu)
        await callback_query.message.answer(text=text.choose, reply_markup=btn)
    elif selected == text.btnGradeUpdate[0]:
        await callback_query.message.answer(text=text.inputBookName)
        await UpdateBookState.name.set()
    else:
        btn = btnInline(text.confirmBtn)
        await callback_query.message.answer(text=text.delete, reply_markup=btn)
        await DeleteBookState.confirm.set()

