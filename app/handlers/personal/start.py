from aiogram import types
from main import dp, bot

import keyboards as kb

NATIVE_LANGUAGE = TARGET_LANGUAGE = ''


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'start'),
            types.BotCommand('train', 'повторити слова'),
        ]
    )


@dp.message_handler(commands=['start', 'початок', ])
async def start_message(msg: types.Message):
    await set_default_commands(dp)
    await bot.send_message(msg.from_user.id, text=f"Hello, {msg.from_user.full_name}",  reply_markup=kb.markup_down)
    await msg.answer(text="what is your native language?", reply_markup=kb.select_language_keyboard)


@dp.callback_query_handler(text=kb.languages)
async def select_target_language(callback_query: types.CallbackQuery):
    global NATIVE_LANGUAGE, TARGET_LANGUAGE
    if not NATIVE_LANGUAGE:
        NATIVE_LANGUAGE = callback_query.data
        await bot.send_message(callback_query.from_user.id,
                               text="what is your target language?",
                               reply_markup=kb.select_language_keyboard)

    else:
        TARGET_LANGUAGE = callback_query.data
        await bot.send_message(callback_query.from_user.id,
                               text=f"{callback_query.from_user.first_name}, "
                                    f"your native language is {NATIVE_LANGUAGE}, your target - {TARGET_LANGUAGE}")
