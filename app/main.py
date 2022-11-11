from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from settings import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


if __name__ == "__main__":
    from handlers import dp

    executor.start_polling(dp)