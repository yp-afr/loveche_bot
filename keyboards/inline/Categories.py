from aiogram import types

markup = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text="Документы 🧾", callback_data="cat_Документы")],
    [types.InlineKeyboardButton(text="Техника 📱", callback_data="cat_Техника")],
    [types.InlineKeyboardButton(text="Ключи 🔑", callback_data="cat_Ключи")],
    [types.InlineKeyboardButton(text="Кошельки/Сумки 🎒", callback_data="cat_Кошельки/Сумки")],
    [types.InlineKeyboardButton(text="Питомцы 🐶", callback_data="cat_Питомцы")],
    [types.InlineKeyboardButton(text="Другое 💍", callback_data="cat_Другое")],
])
