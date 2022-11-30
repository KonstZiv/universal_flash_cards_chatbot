from aiogram import types
from aiogram.utils import executor

from create_bot import dp
from handlers import register_all_handlers


async def set_default_commands(_):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'start'),
        ]
    )

if __name__ == "__main__":
    register_all_handlers(dp)
    executor.start_polling(dp, on_startup=set_default_commands)
