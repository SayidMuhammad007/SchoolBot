from aiogram import types

import text
from keyboards.default.menu import btns
from loader import dp


# Echo bot
@dp.message_handler(text=text.btnMenu[0])
async def bot_echo(message: types.Message):
    btn = btns(text.btnSchoolBook)
    await message.answer(text=text.choose, reply_markup=btn)
