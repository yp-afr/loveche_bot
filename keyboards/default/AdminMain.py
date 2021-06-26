from aiogram import types
from data import names

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(names.button_create_text, names.button_myposts_text)
markup.row(names.button_allposts_text)
markup.row(names.button_admin_text)
markup.add(names.button_show_reviews)
