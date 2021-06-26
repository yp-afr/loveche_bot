from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.users.misc import change_post_cb, del_post
from loader import dp
from states.ShowItem import ShowItem
from utils.dp_api.database import database


@dp.callback_query_handler(state=ShowItem.ChooseCategory)
async def show_all_choose_category(call: types.CallbackQuery, state: FSMContext):
    category = call.data[4:]
    data = await state.get_data()
    item_type = data.get("item_type")
    await call.message.delete()
    rows = await database.show_items(type_finds=item_type, category=category)
    if rows:
        result = await database.get_admin(f"@{types.User.get_current().username}")
        for row in rows:
            if result:
                markup = types.InlineKeyboardMarkup(inline_keyboard=[
                    [types.InlineKeyboardButton(text="Изменить",
                                                callback_data=change_post_cb.new(item_id=int(row['id']))),
                     types.InlineKeyboardButton(text="Удалить", callback_data=del_post.new(item_id=int(row['id'])))]
                ])
            else:
                markup = None
            if row['photo'] is None:
                await call.message.answer(f"<b>{row['type']}</b> -- {row['category']}\n\n{row['caption']}\n"
                                          f"\nКонтакты: {row['author_username']}", reply_markup=markup)
            else:
                await call.message.answer_photo(photo=row['photo'],
                                                caption=f"<b>{row['type']}</b> -- {row['category']}\n\n{row['caption']}"
                                                        f"\n\nКонтакты: {row['author_username']}", reply_markup=markup)
            await sleep(0.3)
    else:
        await call.message.answer(f"В категории <b>{item_type}->{category}</b> нет постов")
    await state.reset_state()
