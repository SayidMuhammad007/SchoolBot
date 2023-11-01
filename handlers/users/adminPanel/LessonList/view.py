from aiogram import types

import text
from handlers.users.auth import authentication
from handlers.users.userPanel.LessonList.list import Lessonlist
from keyboards.default.menu import *
from loader import dp


# Echo bot
@dp.message_handler(text=text.btnAdmin[4])
async def bot_echo(message: types.Message):
    check = authentication(message.from_user.id)
    if check == True:
        btn = btnInlineWithStatus("gList",text.gradeList, 0)
        await message.answer(text=text.choose, reply_markup=btn)
    else:
        await Lessonlist(message)
