from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

Admins = [995712956, ]

token = config('BOT_TOKEN')
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

