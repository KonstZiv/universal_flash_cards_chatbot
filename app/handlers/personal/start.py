from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from aiogram.dispatcher.filters.state import State, StatesGroup

import app.handlers.personal.keyboards as kb
from app.base_function.translator import get_translate
from app.create_bot import bot
from app.db_function.personal import (add_new_user_db, add_user_context_db,
                                      user_context_is_exist_db)
from app.scheme.transdata import ISO639_1, TranslateRequest

NATIVE_LANGUAGE = TARGET_LANGUAGE = ""


class FSMChooseLanguage(StatesGroup):
    native_language = State()
    target_language = State()


async def start_message(msg: types.Message, state):
    await msg.answer(text=f"Hello, {msg.from_user.full_name}")
    user_context_db = await user_context_is_exist_db(msg.from_user.id)

    if user_context_db:
        await bot.send_message(
            user_context_db.user.telegram_user_id,
            text=f"{user_context_db.user.first_name}, "
            f"your native language is {user_context_db.context_1.name}, "
            f"your target - {user_context_db.context_2.name}",
        )
        return

    await FSMChooseLanguage.first()
    await msg.answer(
        text="what is your native language?", reply_markup=kb.select_language_keyboard
    )


async def select_native_language(
    callback_query: types.CallbackQuery, state: FSMContext
):
    async with state.proxy() as data:
        data["native_lang"] = callback_query.data
    await FSMChooseLanguage.next()
    await bot.send_message(
        callback_query.from_user.id,
        text="what is your target language?",
        reply_markup=kb.select_language_keyboard,
    )


async def select_target_language(
    callback_query: types.CallbackQuery, state: FSMContext
):
    async with state.proxy() as data:
        data["target_lang"] = callback_query.data

    user_db = await add_new_user_db(callback_query.from_user)
    user_context_db = await add_user_context_db(data, user_db)

    await bot.send_message(
        user_db.telegram_user_id,
        text=f"{user_db.first_name}, "
        f"your native language is {user_context_db.context_1.name}, "
        f"your target - {user_context_db.context_2.name}",
    )
    await state.finish()


async def translate_word(msg: types.Message):
    request = TranslateRequest(
        in_lang=ISO639_1[TARGET_LANGUAGE],
        out_lang=ISO639_1[NATIVE_LANGUAGE],
        line=msg.text,
    )
    translated = get_translate(input_=request).translated_line
    await msg.answer(f'you wrote {msg.text}. Translated - "{translated}"')


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(
        start_message,
        commands=[
            "start",
            "початок",
        ],
        state=None,
    )
    dp.register_callback_query_handler(
        select_native_language, state=FSMChooseLanguage.native_language
    )
    dp.register_callback_query_handler(
        select_target_language, state=FSMChooseLanguage.target_language
    )
    dp.register_message_handler(translate_word, Regexp(regexp="[a-zA-Z ]"))
