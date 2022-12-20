from unittest import IsolatedAsyncioTestCase

import pytest
from piccolo.conf.apps import Finder
from piccolo.table import create_db_tables_sync, drop_db_tables_sync

from app.db_functions.personal import add_user_db
from app.tests.utils import TABLE_USER_2, TABLE_USER_1
from app.tests.utils import TELEGRAM_USER_2, TELEGRAM_USER_1

TABLES = Finder().get_table_classes()


class TestApp(IsolatedAsyncioTestCase):
    def setUp(self):
        create_db_tables_sync(*TABLES)

    def tearDown(self):
        pass
        drop_db_tables_sync(*TABLES)

    @pytest.mark.parametrize(
        ("telegram_user", "table_user"),
        (
                (TELEGRAM_USER_1, TABLE_USER_1),
                (TELEGRAM_USER_2, TABLE_USER_2)
        ),
    )
    @pytest.mark.asyncio
    async def test_add_user_db(self, telegram_user, table_user):
        user = await add_user_db(telegram_user)
        assert user.telegram_user_id == table_user.telegram_user_id
        assert user.id == table_user.id
        assert user.first_name == table_user.first_name
        assert user.last_name == table_user.last_name
        assert user.user_name == table_user.user_name
        assert user.telegram_language == table_user.telegram_language

