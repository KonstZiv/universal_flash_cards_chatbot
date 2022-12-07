from unittest.mock import AsyncMock
import pytest
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.storage import KEY
from aiogram.contrib.fsm_storage.memory import
from app.handlers.personal.start import start_message, FSMChooseLanguage
from tests.tests_handlers.utils import TEST_USER, TEST_USER_CHAT



@pytest.mark.asyncio
async def test_start_message_handler(storage, bot):
    msg = AsyncMock()
    call = AsyncMock()
    state = FSMContext(
        storage=storage,
        chat=TEST_USER_CHAT,
        bot=bot,
    )

    msg.from_user.full_name = 'UlBo'
    await start_message(msg , state: FSMChooseLanguage = None )
    msg.answer.assert_called_with(text=f"Hello, {msg.from_user.full_name}")

