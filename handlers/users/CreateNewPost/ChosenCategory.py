from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from handlers.users.misc import Item
from loader import dp
from states.NewItem import NewItem


@dp.callback_query_handler(state=NewItem.ChooseCategory)
async def choose_category(call: types.CallbackQuery, state: FSMContext):
    category = call.data[4:]
    data = await state.get_data()
    item: Item = data.get("item")
    item.category = category
    username = types.User.get_current().username
    if username:
        item.username = "@" + username
        await call.message.edit_reply_markup()
        await call.message.edit_text(names.enter_captiob_text)
        await NewItem.EnterCaption.set()
    else:
        await call.message.edit_reply_markup()
        await call.message.edit_text("Имя пользователя не было обнаружено, укажи пожалуйста свои контакты: ")
        await NewItem.SetContact.set()
    await state.update_data(item=item)
