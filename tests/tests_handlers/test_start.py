from unittest.mock import AsyncMock
import pytest
from unittest.mock import patch

from aiogram.fsm.context import FSMContext

from app.handlers.personal import start
from app.handlers.personal.start import FSMChooseLanguage, select_native_language, greeting, get_user_data

import app.handlers.personal.keyboards as kb


@pytest.mark.asyncio
async def test_greeting_handler():
    msg: AsyncMock = AsyncMock()

    await greeting(msg)
    msg.answer.assert_called_with(text=f"Hello, {msg.from_user.full_name}")


@pytest.mark.asyncio
async def test_get_user_data_user_not_exist(state: FSMContext):
    msg: AsyncMock = AsyncMock(name='msg')
    with patch.object(start, 'get_user_context_db', return_value=False) as is_user_exist:
        await get_user_data(msg, state=state)
    is_user_exist.assert_called_once_with(msg.from_user.id)
    msg.answer.assert_called_with(text="what is your native language?", reply_markup=kb.select_language_keyboard)
    assert msg.answer.call_args.kwargs.get('text') == "what is your native language?"
    assert await state.get_state() == FSMChooseLanguage.native_language


@pytest.mark.asyncio
async def test_get_user_data_user_exist(state: FSMContext):
    msg: AsyncMock = AsyncMock(name='msg')
    user_context_db: AsyncMock = AsyncMock(name='user_cont')
    with patch.object(start, 'get_user_context_db', return_value=user_context_db) as is_user_exist:
        await get_user_data(msg, state)

    is_user_exist.assert_called_once_with(msg.from_user.id)
    msg.answer.assert_called_once_with(
        text=f"{user_context_db.user.first_name}, "
             f"your native language is {user_context_db.context_1.name}, "
             f"your target - {user_context_db.context_2.name}",
    )


@pytest.mark.asyncio
async def test_select_native_language(state: FSMContext):
    call: AsyncMock = AsyncMock()

    await select_native_language(callback_query=call, state=state)
    assert await state.get_state() == FSMChooseLanguage.target_language
    assert await state.get_data() == {'native_lang': call.data}
    call.message.answer.assert_called_with(
        text="what is your target language?",
        reply_markup=kb.select_language_keyboard,
    )
