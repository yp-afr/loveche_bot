from aiogram import executor

from data.admins import admins
from loader import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    for admin in admins:
        try:
            await bot.send_message(admin, "Я запущен!")
        except Exception:
            pass
    try:
        await database.delete_old_records()
    except Exception:
        pass

if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
