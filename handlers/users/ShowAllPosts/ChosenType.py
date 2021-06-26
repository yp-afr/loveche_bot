from aiogram import types
from aiogram.dispatcher import FSMContext

from data import names
from keyboards.inline import Categories
from loader import dp
from states.ShowItem import ShowItem


@dp.callback_query_handler(state=ShowItem.ChooseType)
async def show_all_choose_type(call: types.CallbackQuery, state: FSMContext):
    type_finds = call.data[5:]
    await call.message.edit_text(names.choose_categorie_text, reply_markup=Categories.markup)
    await ShowItem.ChooseCategory.set()
    await state.update_data(item_type=type_finds)
