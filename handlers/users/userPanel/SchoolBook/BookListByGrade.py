from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, db
import text
ITEMS_PER_PAGE = 5

# Current page
data = []
current_page = 0
# Echo bot
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('GradeList_'))
async def handle_product_deletion(callback_query: types.CallbackQuery):
    global data  # Use the global data variable
    global current_page
    selected = callback_query.data.split('_')[1]
    data = db.selectAllByGrade("school_book", "grade", selected)

    # Calculate the start and end index for the current page
    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = (current_page + 1) * ITEMS_PER_PAGE
    msg, markup = check(start_idx, end_idx)

    # Check if text is empty before sending a message
    if msg:
        await callback_query.message.edit_text(text=msg, reply_markup=markup)
    else:
        await callback_query.message.edit_text(text=text.empty)


@dp.callback_query_handler(lambda c: c.data in ['prevGradeList', 'nextGradeList'])
async def process_callback(callback_query: types.CallbackQuery):
    global current_page
    global data  # Use the global data variable
    if callback_query.data == 'prevGradeList':
        current_page = max(0, current_page - 1)
    elif callback_query.data == 'nextGradeList':
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
        msg += text.SchoolBookList(data[i][2], t)

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
        callback_data = f"SchoolBookList_{order_id}"
        markup.insert(InlineKeyboardButton(d, callback_data=callback_data))

    # Add previous and next buttons if available
    if has_previous_page:
        prev_button = InlineKeyboardButton(text.prev, callback_data="prevGradeList")
        markup.add(prev_button)

    if has_next_page:
        next_button = InlineKeyboardButton(text.next, callback_data="nextGradeList")
        if has_previous_page:
            markup.insert(next_button)
        else:
            markup.add(next_button)

    return msg, markup
