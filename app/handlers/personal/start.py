from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from aiogram.dispatcher.filters.state import State, StatesGroup

from base_function.translator import get_translate
from scheme.transdata import ISO639_1, TranslateRequest

from create_bot import dp, bot
import handlers.personal.keyboards as kb

NATIVE_LANGUAGE = TARGET_LANGUAGE = ''

class FSMChooseLanguage(StatesGroup):
    native_language = State()
    target_language = State()


async def start_message(msg: types.Message, state):
    await msg.answer(text=f"Hello, {msg.from_user.full_name}")
    await FSMChooseLanguage.first()
    await msg.answer(text="what is your native language?", reply_markup=kb.select_language_keyboard)


async def select_native_language(callback_query: types.CallbackQuery, state: FSMContext):
    global NATIVE_LANGUAGE, TARGET_LANGUAGE
    NATIVE_LANGUAGE = callback_query.data
    await FSMChooseLanguage.next()
    await bot.send_message(callback_query.from_user.id,
                           text="what is your target language?",
                           reply_markup=kb.select_language_keyboard)


async def select_target_language(callback_query: types.CallbackQuery, state: FSMContext):
    global NATIVE_LANGUAGE, TARGET_LANGUAGE
    TARGET_LANGUAGE = callback_query.data
    await bot.send_message(callback_query.from_user.id,
                           text=f"{callback_query.from_user.first_name}, "
                           f"your native language is {NATIVE_LANGUAGE}, your target - {TARGET_LANGUAGE}")
    await state.finish()


async def translate_word(msg: types.Message):
    global NATIVE_LANGUAGE, TARGET_LANGUAGE
    request = TranslateRequest(
        in_lang=ISO639_1[TARGET_LANGUAGE], out_lang=ISO639_1[NATIVE_LANGUAGE], line=msg.text
    )
    translated = get_translate(input_=request).translated_line
    await msg.answer(f'you wrote {msg.text}. Translated - "{translated}"')


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start', 'початок', ], state=None)
    dp.register_callback_query_handler(select_native_language, state=FSMChooseLanguage.native_language)
    dp.register_callback_query_handler(select_target_language, state=FSMChooseLanguage.target_language)
    dp.register_message_handler(translate_word, Regexp(regexp='[a-zA-Z ]'))




