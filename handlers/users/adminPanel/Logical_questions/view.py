from aiogram import types

import text
from handlers.users.auth import authentication
from handlers.users.userPanel.logicQuestion.list import LogicQuestionList
from keyboards.default.menu import btns
from loader import dp


# Echo bot
@dp.message_handler(text=text.btnMenu[1])
async def bot_echo(message: types.Message):
    check = authentication(message.from_user.id)
    if check == True:
        btn = btns(text.btnLogicQuestion)
        await message.answer(text=text.choose, reply_markup=btn)
    else:
        await LogicQuestionList(message)
