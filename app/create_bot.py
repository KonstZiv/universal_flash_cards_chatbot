from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

#from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.dispatcher import Dispatcher

from app.settings import settings

storage = MemoryStorage()
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(storage=storage)
