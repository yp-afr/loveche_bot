from aiogram import types

markup = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="Найдено", callback_data="type_Найдено"),
         types.InlineKeyboardButton(text="Потеряно", callback_data="type_Потеряно")]
    ]
)
