from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import *
from loader import dp
from secret import ADMIN_ID


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id in ADMIN_ID:
        await message.answer(f"Здравствуйте, {message.from_user.full_name}!", reply_markup=btnAdmin)
    else:
        await message.answer(f"Здравствуйте, {message.from_user.full_name}!", reply_markup=btnMenu)
