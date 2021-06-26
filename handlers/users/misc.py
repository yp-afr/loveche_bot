from aiogram.utils.callback_data import CallbackData

del_post = CallbackData("delete", "item_id")
change_post_cb = CallbackData("change", "item_id")
del_review = CallbackData("delete_review", "review_id")


class Item:
    type_finds = ""
    category = ""
    photo = ""
    caption = ""
    username = ""
