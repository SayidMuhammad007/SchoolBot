from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import text
from loader import dp, db

ITEMS_PER_PAGE = 5

# Current page
data = []
current_page = 0

@dp.message_handler(text=text.btnGradeMenu[0])
async def bot_echo(message: types.Message, state: FSMContext):
    global data  # Use the global data variable
    global current_page

    # Fetch the data from your database using find_orders function
    dataa = db.selectGradesAll()
    data = dataa
    # Calculate the start and end index for the current page
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE
    msg, markup = check(start_idx, end_idx)

    # Check if text is empty before sending a message
    if msg:
        await message.answer(text=msg, reply_markup=markup)
    else:
        await message.answer(text=text.empty)


@dp.callback_query_handler(lambda c: c.data in ['prev', 'next'])
async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    global current_page
    global data  # Use the global data variable
    if callback_query.data == 'prev':
        current_page = max(0, current_page - 1)
    elif callback_query.data == 'next':
        current_page = min(len(data) // ITEMS_PER_PAGE, current_page + 1)
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE
    msg, markup = check(start_idx, end_idx)
    # Check if text is empty before editing the message
    if msg:
        await callback_query.message.edit_text(text=msg, reply_markup=markup)

def check(start_idx, end_idx):
    # Check if there are more pages
    has_previous_page = current_page > 0
    has_next_page = end_idx < len(data)

    # Create the message text with order IDs
    msg = ""
    t = 0
    print(data)
    for i in range(start_idx, end_idx):
        t += 1
        if t > ITEMS_PER_PAGE or i >= len(data):
            break
        msg += text.ConfirmGradeId(t, data[i][1], data[i][2])

    # Create an inline keyboard for navigation
    markup = InlineKeyboardMarkup(row_width=5)

    # Add inline buttons for each order ID
    d = 0
    for i in range(start_idx, end_idx):
        d += 1
        if d > ITEMS_PER_PAGE or i >= len(data):
            break
        order_id = data[i][0]
        print(order_id)
        callback_data = f"grade_{order_id}"
        markup.insert(InlineKeyboardButton(d, callback_data=callback_data))

    # Add previous and next buttons if available
    if has_previous_page:
        prev_button = InlineKeyboardButton(text.prev, callback_data="prev")
        markup.add(prev_button)

    if has_next_page:
        next_button = InlineKeyboardButton(text.next, callback_data="next")
        if has_previous_page:
            markup.insert(next_button)
        else:
            markup.add(next_button)

    return msg, markup
