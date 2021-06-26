from aiogram import types
from data import names

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(names.button_cancel_text)
