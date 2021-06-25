from aiogram import executor

import markups
from config import admins
from load_all import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    for admin in admins:
        try:
            await bot.send_message(admin, "Я запущен!")
        except Exception:
            pass


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)