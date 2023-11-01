from aiogram import types
from aiogram.dispatcher import FSMContext

import text
from keyboards.default.menu import *
from loader import dp, db
import re

from states.lesson import LessonDayState


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('gList_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    number = re.findall(r'\d+', selected)
    print(number[0])
    data = db.selectWhere(number[0], "grades", "grade")
    if data:
        btn = btnInlineWithLetter("selectGradeWithLetter", data)
        await callback_query.message.edit_text(text=text.choose, reply_markup=btn)
    else:
        await callback_query.message.edit_text(text=text.empty)



@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('selectGradeWithLetter_'))
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    selected = callback_query.data.split('_')[2]
    await state.update_data({"GradeId":selected})
    btn = btnInline(text.dayofweeks)
    await callback_query.message.edit_text(text=text.choose, reply_markup=btn)
    await LessonDayState.day.set()

@dp.callback_query_handler(state=LessonDayState.day)
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    await state.update_data({"day":callback_query.data})
    await callback_query.message.edit_text(text=text.dayLesson)
    await LessonDayState.lessons.set()

@dp.message_handler(state=LessonDayState.lessons)
async def handle_product_deletion(message: types.Message, state:FSMContext):
    await state.update_data({"lesson":message.text})
    data = await state.get_data()
    grade = data.get("GradeId")
    day = data.get("day")
    btn = btnInline(text.confirmBtn)
    await message.answer(text=text.DayLesson(day, grade, message.text), reply_markup=btn)
    await LessonDayState.confirm.set()

@dp.callback_query_handler(state=LessonDayState.confirm)
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    if callback_query.data == text.confirmBtn[0]:
        data = await state.get_data()
        grade = data.get("GradeId")
        day = data.get("day")
        lesson = data.get("lesson")
        db.addLesson(grade, day, lesson)
        await callback_query.message.edit_text(text=text.saved)
    else:
        await callback_query.message.edit_text(text=text.cancel)
    await state.finish()
