import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from sql_instance import create_pool

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

db = dp.loop.run_until_complete(create_pool())
