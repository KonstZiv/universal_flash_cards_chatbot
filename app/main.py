from aiogram import types
#from aiogram.utils import executor

from app.create_bot import dp
from app.handlers import register_all_handlers
from app.scheme.transdata import ISO639_1
from app.tables import Context


async def set_default_commands():
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "start"),
        ]
    )


async def add_languages_to_context():
    cont_name = await Context.select()
    if not cont_name:
        for language in ISO639_1:
            new_language = Context(name=language.name, name_alfa2=language.value)
            await new_language.save()


async def on_startup(_):
    await set_default_commands()
    await add_languages_to_context()


if __name__ == "__main__":
    register_all_handlers(dp)
    dp.start_polling(dp, on_startup=on_startup)
