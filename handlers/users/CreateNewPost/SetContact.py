from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from handlers.users.misc import Item
from loader import dp
from states.NewItem import NewItem


@dp.message_handler(state=NewItem.SetContact)
async def get_contact(message: types.Message, state: FSMContext):
    data = await state.get_data()
    item: Item = data.get("item")
    item.username = message.text
    await message.answer(names.enter_captiob_text)
    await NewItem.EnterCaption.set()
    await state.update_data(item=item)
