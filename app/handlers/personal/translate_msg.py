from aiogram import types

from aiogram.dispatcher.filters import Regexp

from base_function.translator import get_translate
from scheme.transdata import ISO639_1, TranslateRequest

from main import dp


@dp.message_handler(Regexp(regexp='[a-zA-Z]'))
async def translate_word(msg: types.Message):
    global NATIVE_LANGUAGE, TARGET_LANGUAGE
    from .start import NATIVE_LANGUAGE, TARGET_LANGUAGE

    request = TranslateRequest(
        in_lang=ISO639_1[TARGET_LANGUAGE], out_lang=ISO639_1[NATIVE_LANGUAGE], line=msg.text
    )
    translated = get_translate(input_=request).translated_line
    await msg.answer(f'you wrote {msg.text}. Translated - "{translated}"')

