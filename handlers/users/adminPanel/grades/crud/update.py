from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.users.start import auth
from keyboards.default.menu import btns, btnInline
from loader import dp, db
import text
from states.GradeState import GradeState, UpdateGradeState, DeleteGrade


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('id_'))
async def handle_product_deletion(callback: types.CallbackQuery, state:FSMContext):
    selected = callback.data.split('_')[1]
    id = callback.data.split('_')[2]
    print(id)
    await state.update_data({"id": id})
    if selected == text.btnGradeUpdate[0]:
        await callback.message.edit_text(text=text.inputGrade)
        await UpdateGradeState.grade.set()
    elif selected == text.btnGradeUpdate[2]:
        btn = btns(text.btnGradeMenu)
        await callback.message.delete()
        await callback.message.answer(text=text.choose, reply_markup=btn)
        await state.finish()
    else:
        btn = btnInline(text.confirmBtn)
        await callback.message.edit_text(text=text.delete, reply_markup=btn)
        await DeleteGrade.confirm.set()

@dp.message_handler(state=UpdateGradeState.grade)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'grade': message.text})
    await message.answer(text=text.gradeType)
    await UpdateGradeState.type.set()

@dp.message_handler(state=UpdateGradeState.type)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'type': message.text})
    data = await state.get_data()
    grade = data.get("grade")
    type = message.text
    msg = text.ConfirmGrade(grade, type)
    btn = btnInline(text.confirmBtn)
    await message.answer(text=msg, reply_markup=btn)
    await UpdateGradeState.confirm.set()

@dp.callback_query_handler(state=UpdateGradeState.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    if callback.data == text.confirmBtn[0]:
        data = await state.get_data()
        grade = data.get("grade")
        type = data.get("type")
        gradeId = data.get("id")
        db.updateGrade(grade, type, gradeId)
        btn = btns(text.btnGradeMenu)
        await callback.message.delete()
        await callback.message.answer(text=text.saved, reply_markup=btn)
    else:
        msg, btn = await auth(callback)
        await callback.message.delete()
        await callback.message.answer(text=text.cancel, reply_markup=btn)
    await state.finish()