from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from handlers.users.misc import Item
from keyboards.inline import CategoriesWithBank
from loader import dp
from states.NewItem import NewItem


@dp.callback_query_handler(state=NewItem.ChooseType, text_contains="Найдено")
async def choose_type(call: types.CallbackQuery, state: FSMContext):
    type_finds = call.data[5:]
    item = Item()
    item.type_finds = type_finds
    await call.message.edit_text(names.choose_categorie_text, reply_markup=CategoriesWithBank.markup)
    await NewItem.ChooseCategory.set()
    await state.update_data(item=item)
