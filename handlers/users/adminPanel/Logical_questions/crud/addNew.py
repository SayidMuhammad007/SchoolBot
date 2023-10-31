from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from handlers.users.start import auth
from keyboards.default.menu import btns, btnInline
from loader import dp, db
import text
from states.GradeState import GradeState
from states.LogicQuestionState import LogicQuestionState


# Echo bot
@dp.message_handler(text=text.btnLogicQuestion[1])
async def bot_echo(message: types.Message):
    await message.answer(text=text.inputLogicQuestion, reply_markup=ReplyKeyboardRemove())
    await LogicQuestionState.question.set()

@dp.message_handler(state=LogicQuestionState.question)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'question': message.text})
    await message.answer(text=text.inputLogicAnswer)
    await LogicQuestionState.answer.set()

@dp.message_handler(state=LogicQuestionState.answer)
async def bot_echo(message: types.Message, state:FSMContext):
    await state.update_data({'answer': message.text})
    data = await state.get_data()
    question = data.get("question")
    answer = message.text
    msg = text.ConfirmGrade(question, answer)
    btn = btnInline(text.confirmBtn)
    await message.answer(text=msg, reply_markup=btn)
    await LogicQuestionState.confirm.set()

@dp.callback_query_handler(state=LogicQuestionState.confirm)
async def bot_echo(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    if callback.data == text.confirmBtn[0]:
        data = await state.get_data()
        question = data.get("question")
        answer = data.get("answer")
        db.addLogicQuestion(question, answer)
        btn = btns(text.btnLogicQuestion)
        await callback.message.delete()
        await callback.message.answer(text=text.saved, reply_markup=btn)
    else:
        msg, btn = await auth(callback)
        await callback.message.delete()
        await callback.message.answer(text=text.cancel, reply_markup=btn)
    await state.finish()