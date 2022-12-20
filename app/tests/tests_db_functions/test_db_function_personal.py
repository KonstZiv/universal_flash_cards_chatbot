from unittest import IsolatedAsyncioTestCase

from parameterized import parameterized
import aiogram
import pytest
import typing as t
from piccolo.conf.apps import Finder
from piccolo.table import create_db_tables_sync, drop_db_tables_sync, Table

from app.db_functions.personal import add_user_db
from app.tables import User
from app.tests.utils import TELEGRAM_USER_2, TELEGRAM_USER_1


TABLES: t.List[t.Type[Table]] = Finder().get_table_classes()


class TestApp(IsolatedAsyncioTestCase):
    def setUp(self):
        create_db_tables_sync(*TABLES)

    def tearDown(self):
        drop_db_tables_sync(*TABLES)

    @parameterized.expand([(TELEGRAM_USER_1,), (TELEGRAM_USER_2,)])
    @pytest.mark.asyncio
    async def test_add_user_db_verification_of_recorded_data(self, telegram_user: aiogram.types.User) -> None:
        user: User = await add_user_db(telegram_user)
        assert user.telegram_user_id == telegram_user.id
        assert user.first_name == telegram_user.first_name
        assert user.last_name == (telegram_user.last_name or '')
        assert user.user_name == (telegram_user.username or '')
        assert user.telegram_language == (telegram_user.language_code or '')

