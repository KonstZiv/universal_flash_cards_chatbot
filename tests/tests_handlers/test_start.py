from unittest.mock import AsyncMock
import pytest
from unittest.mock import patch

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey

from app.handlers.personal.start import FSMChooseLanguage, start, select_native_language, greeting, get_user_data
from tests.tests_handlers.utils import TEST_USER, TEST_USER_CHAT

import app.handlers.personal.keyboards as kb



@pytest.mark.asyncio
async def test_greeting_handler(storage, bot):
    msg = AsyncMock()
    call = AsyncMock()
    state = FSMContext(
        bot=bot,
        storage=storage,
        key=StorageKey(bot_id=bot.id, user_id=TEST_USER.id, chat_id=TEST_USER_CHAT.id),
    )
    get_user_data = AsyncMock()
    user_context_db = AsyncMock()

    await greeting(msg, state=state)
    msg.answer.assert_called_with(text=f"Hello, {msg.from_user.full_name}")


@pytest.mark.asyncio
async def test_get_user_data_handler(storage, bot):
    msg = AsyncMock()
    call = AsyncMock()
    state = FSMContext(
        bot=bot,
        storage=storage,
        key=StorageKey(bot_id=bot.id, user_id=TEST_USER.id, chat_id=TEST_USER_CHAT.id),
    )
    get_user_data = AsyncMock()
    user_context_db = AsyncMock()

    await greeting(msg, state=state)

    msg.answer.assert_called_with(text="what is your native language?", reply_markup=kb.select_language_keyboard)

@pytest.mark.asyncio
async def test_select_native_language(storage, bot):
    call = AsyncMock()
    state = FSMContext(
        bot=bot,
        storage=storage,
        key=StorageKey(bot_id=bot.id, chat_id=TEST_USER_CHAT.id, user_id=TEST_USER.id))

    await select_native_language(callback_query=call, state=state)

    # assert await state.get_data() is
    assert await state.get_state() == FSMChooseLanguage.target_language
    call.message.answer.assert_called_with(
        text="what is your target language?",
        reply_markup=kb.select_language_keyboard,
        )
