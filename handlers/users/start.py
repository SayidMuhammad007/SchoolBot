from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import *
from loader import dp
from secret import ADMIN_ID
import text

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    msg, btn = await auth(message)
    await message.answer(text=msg, reply_markup=btn)


async def auth(message):
    if message.from_user.id in ADMIN_ID:
        btn = btns(text.btnAdmin)
    else:
        btn = btns(text.btnMenu)
    msg = f"{text.greeting}, {message.from_user.full_name}!"
    return msg, btn
