from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


from dotenv import load_dotenv
import os

import keyboards as kb

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
ADMIN = 887549275


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

native_language = target_language = ''

async def set_default_commands(dp):
    print('bot command')
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'start'),
            types.BotCommand('train', 'Запустить бота'),
        ]
    )
    #x = await bot.get_my_commands()
    #print('get_my_commands', x)

@dp.message_handler(commands = ['start', 'початок',])
async def start_message(msg: types.Message):
    await set_default_commands(dp)
    x = await bot.get_my_commands()
    print('get_my_commands', x)
    print(msg)
    if msg.from_user.id == ADMIN:
        print('hi, admin')
    await bot.send_message(msg.from_user.id, text=f"Hello, {msg.from_user.full_name}",  reply_markup=kb.markup_down)
    await msg.answer(text="what is your native language?", reply_markup=kb.select_language_keyboard)


@dp.callback_query_handler(text = kb.languages)
async def select_target_language(callback_query: types.CallbackQuery):
    global native_language, target_language
    print(callback_query)
    if not native_language:
        native_language = callback_query.data
        await bot.send_message(callback_query.from_user.id,
                                    text="what is your target language?",
                                    reply_markup=kb.select_language_keyboard)

    else:
        target_language = callback_query.data
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.first_name}, your native language is {native_language}, your target - {target_language}")

if __name__ == "__main__":

    executor.start_polling(dp)
