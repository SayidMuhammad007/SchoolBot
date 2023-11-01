from aiogram import types

import text
from handlers.users.auth import authentication
from keyboards.default.menu import btns
from loader import dp


# Echo bot
@dp.message_handler(text=text.grade)
async def bot_echo(message: types.Message):
    check = authentication(message.from_user.id)
    if check == True:
        btn = btns(text.btnGradeMenu)
        await message.answer(text=text.choose, reply_markup=btn)
