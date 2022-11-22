from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from settings import settings

storage = MemoryStorage()
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
