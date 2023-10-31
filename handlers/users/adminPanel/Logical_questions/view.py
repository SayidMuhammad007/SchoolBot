from aiogram import types

import text
from keyboards.default.menu import btns
from loader import dp


# Echo bot
@dp.message_handler(text=text.btnMenu[1])
async def bot_echo(message: types.Message):
    btn = btns(text.btnLogicQuestion)
    await message.answer(text=text.choose, reply_markup=btn)
