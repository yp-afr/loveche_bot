import names
from aiogram import types
from config import admins

markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_main.add(names.button_create_text, names.button_myposts_text)
markup_main.row(names.button_allposts_text)

rplmarkup_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
rplmarkup_admin.add(names.button_create_text, names.button_myposts_text)
rplmarkup_admin.row(names.button_allposts_text)
rplmarkup_admin.row(names.button_admin_text)

markup_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_cancel.add(names.button_cancel_text)

markup_types = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Находки", callback_data="type_Найдено"),
            types.InlineKeyboardButton(text="Потеряшки", callback_data="type_Потеряно")]
        ]
    )

markup_categories_found = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Документы 🧾", callback_data="cat_Документы")],
        [types.InlineKeyboardButton(text="Техника 📱", callback_data="cat_Техника")],
        [types.InlineKeyboardButton(text="Ключи 🔑", callback_data="cat_Ключи")],
        [types.InlineKeyboardButton(text="Кошельки/Сумки 🎒", callback_data="cat_Кошельки/Сумки")],
        [types.InlineKeyboardButton(text="Питомцы 🐶", callback_data="cat_Питомцы")],
        [types.InlineKeyboardButton(text="Банковская карта 💳", callback_data="cat_Bank>")],
        [types.InlineKeyboardButton(text="Другое 💍", callback_data="cat_Другое")],
    ])

markup_categories_lost = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Документы 🧾", callback_data="cat_Документы")],
        [types.InlineKeyboardButton(text="Техника 📱", callback_data="cat_Техника")],
        [types.InlineKeyboardButton(text="Ключи 🔑", callback_data="cat_Ключи")],
        [types.InlineKeyboardButton(text="Кошельки/Сумки 🎒", callback_data="cat_Кошельки/Сумки")],
        [types.InlineKeyboardButton(text="Питомцы 🐶", callback_data="cat_Питомцы")],
        [types.InlineKeyboardButton(text="Другое 💍", callback_data="cat_Другое")],
    ])


markup_admin = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text="Назначить", callback_data="set_admin"),
     types.InlineKeyboardButton(text="Снять", callback_data="del_admin")],
    [types.InlineKeyboardButton(text="Список админов", callback_data="show_admins")]
])