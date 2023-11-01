from aiogram import types
import re

from aiogram.dispatcher import FSMContext

from keyboards.default.menu import btnInlineWithLetter, btnInlineWithStatus, btnInline
from loader import db, dp
import text
from states.lesson import  LessonState


async def Lessonlist(message):
    btn = btnInlineWithStatus("lList", text.gradeList, 0)
    await message.answer(text=text.choose, reply_markup=btn)


# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('lList_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    selected = callback_query.data.split('_')[1]
    print(selected)
    number = re.findall(r'\d+', selected)
    print(number[0])
    data = db.selectWhere(number[0], "grades", "grade")
    if data:
        btn = btnInlineWithLetter("selectGradeWithLetterUser", data)
        await callback_query.message.edit_text(text=text.choose, reply_markup=btn)
    else:
        await callback_query.message.edit_text(text=text.empty)


#
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('selectGradeWithLetterUser'))
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    selected = callback_query.data.split('_')[2]
    await state.update_data({"id":selected})
    btn = btnInline(text.dayofweeks)
    await callback_query.message.edit_text(text=text.choose, reply_markup=btn)
    await LessonState.day.set()
#
@dp.callback_query_handler(state=LessonState.day)
async def handle_product_deletion(callback_query: types.CallbackQuery, state:FSMContext):
    data = db.selectAllByGrade("lessons", "day", callback_query.data)
    if data:
        await callback_query.message.edit_text(text=text.DayLesson(data[0][2], data[0][1], data[0][3]))
    else:
        await callback_query.message.edit_text(text=text.empty)
    await state.finish()