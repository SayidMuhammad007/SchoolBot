from aiogram import types

import text
from keyboards.default.menu import btns
from loader import dp


# Echo bot
@dp.message_handler(text=text.btnGradeMenu[2])
async def bot_echo(message: types.Message):
    btn = btns(text.btnAdmin)
    await message.answer(text=text.choose, reply_markup=btn)
