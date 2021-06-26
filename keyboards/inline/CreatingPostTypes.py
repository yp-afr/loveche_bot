from aiogram import types

markup = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text="Находки", callback_data="type_Найдено"),
         types.InlineKeyboardButton(text="Потеряшки", callback_data="type_Потеряно")]
    ]
)
