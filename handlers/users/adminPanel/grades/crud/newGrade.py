from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.users.start import auth
from keyboards.default.menu import btns, btnInline
from loader import dp, db
import text
from states.GradeState import GradeState


# Echo bot
@dp.message_handler(text=text.btnGradeMenu[1])
async def bot_echo(message: types.Message):
    await message.answer(text=text.inputGrade, reply_markup=ReplyKeyboardRemove())
    await GradeState.grade.set()

@dp.message_handler(state=GradeState.grade)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'grade': message.text})
    await message.answer(text=text.gradeType)
    await GradeState.type.set()

@dp.message_handler(state=GradeState.type)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'type': message.text})
    data = await state.get_data()
    grade = data.get("grade")
    type = message.text
    msg = text.ConfirmGrade(grade, type)
    btn = btnInline(text.confirmBtn)
    await message.answer(text=msg, reply_markup=btn)
    await GradeState.confirm.set()

@dp.callback_query_handler(state=GradeState.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    if callback.data == text.confirmBtn[0]:
        data = await state.get_data()
        grade = data.get("grade")
        type = data.get("type")
        db.addGrade(grade, type)
        btn = btns(text.btnGradeMenu)
        await callback.message.delete()
        await callback.message.answer(text=text.saved, reply_markup=btn)
    else:
        msg, btn = await auth(callback)
        await callback.message.delete()
        await callback.message.answer(text=text.cancel, reply_markup=btn)
    await state.finish()