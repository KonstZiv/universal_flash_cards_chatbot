from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from app.settings import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


if __name__ == "__main__":
    from handlers import dp

    executor.start_polling(dp)
