from typing import Optional

from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

import app.handlers.personal.keyboards as kb
from app.base_functions.translator import get_translate
from app.db_functions.personal import (add_user_db, add_user_context_db,
                                       get_user_db, get_user_context_db)
from app.scheme.transdata import ISO639_1, TranslateRequest
from app.tables import UserContext, User


class FSMChooseLanguage(StatesGroup):
    native_language = State()
    target_language = State()


async def start(msg: types.Message, state: FSMContext) -> None:
    await greeting(msg)
    await get_user_data(msg, state)


async def greeting(msg: types.Message) -> None:
    await msg.answer(text=f"Hello, {msg.from_user.full_name}")


async def get_user_data(msg: types.Message, state: FSMContext) -> None:
    user_context_db: Optional[UserContext] = await get_user_context_db(msg.from_user.id)

    if user_context_db:
        await msg.answer(
            text=f"{user_context_db.user.first_name}, "
                 f"your native language is {user_context_db.context_1.name}, "
                 f"your target - {user_context_db.context_2.name}",
        )
        return

    await state.set_state(FSMChooseLanguage.native_language)
    await msg.answer(
        text="what is your native language?", reply_markup=kb.select_language_keyboard
    )


async def select_native_language(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await state.set_data({"native_lang": callback_query.data})
    await state.set_state(FSMChooseLanguage.target_language)
    await callback_query.message.answer(
        text="what is your target language?",
        reply_markup=kb.select_language_keyboard,
    )


async def select_target_language(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    await state.update_data({"target_lang": callback_query.data})
    user_db = await get_user_db(callback_query.from_user)
    if user_db is None:
        user_db: Optional[User] = await add_user_db(callback_query.from_user)


    state_data = await state.get_data()
    user_context_db = await add_user_context_db(state_data, user_db)

    await callback_query.message.answer(
        text=f"{user_db.first_name}, "
             f"your native language is {user_context_db.context_1.name}, "
             f"your target - {user_context_db.context_2.name}",
    )
    await state.clear()


async def translate_word(msg: types.Message):
    NATIVE_LANGUAGE = TARGET_LANGUAGE = ""
    request = TranslateRequest(
        in_lang=ISO639_1[TARGET_LANGUAGE],
        out_lang=ISO639_1[NATIVE_LANGUAGE],
        line=msg.text,
    )
    translated = get_translate(input_=request).translated_line
    await msg.answer("I can't translate")
    await msg.answer(f'you wrote {msg.text}. Translated - "{translated}"')


def register_handler_start(dp: Dispatcher):
    dp.message.register(translate_word, F.test.regexp("[a-zA-Z ]"))  # regexp_match=Match("[a-zA-Z ]")))
    dp.message.register(start, Command(commands=["start", "початок"]))
    dp.message.register(greeting, Command(commands=["hello"]))
    dp.message.register(get_user_data)
    dp.callback_query.register(select_native_language, FSMChooseLanguage.native_language)
    dp.callback_query.register(select_target_language, FSMChooseLanguage.target_language)
