import asyncio
import logging
from aiogram import types

from app.create_bot import dp, bot
from app.handlers import register_all_handlers
from app.scheme.transdata import ISO639_1
from app.tables import Context


async def set_default_commands():
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="start"),
        ]
    )


async def add_languages_to_context():
    cont_name = await Context.select()
    if not cont_name:
        for language in ISO639_1:
            new_language = Context(name=language.name, name_alfa2=language.value)
            await new_language.save()


async def on_startup():
    await set_default_commands()
    await add_languages_to_context()


async def main(logger: logging.Logger) -> None:
    logging.basicConfig(level=logging.DEBUG)

    register_all_handlers(dp)
    dp.startup.register(on_startup)
    await dp.start_polling(bot, logger=logger)


if __name__ == "__main__":
    logger: logging.Logger = logging.getLogger(__name__)
    try:
        logger.info('Bot started')
        asyncio.run(main(logger))

    except (KeyboardInterrupt, SystemExit):
        logger.info('Bot stopped')
