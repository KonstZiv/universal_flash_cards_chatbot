import pytest

from app.db_function.personal import add_new_user_db
from tests.tests_db.utils import TABLE_USER_1, TABLE_USER_2
from tests.utils import TELEGRAM_USER_1, TELEGRAM_USER_2


# @pytest.mark.parametrize(
#     ("telegram_user", "table_user"),
#     (
#             (TELEGRAM_USER_1, TABLE_USER_1),
#             (TELEGRAM_USER_2, TABLE_USER_2)
#     ),
# )
@pytest.mark.asyncio
async def test_add_new_user_db_not_exist(save_table_user, telegram_user=TELEGRAM_USER_2, table_user=TABLE_USER_2):
    x = await add_new_user_db(telegram_user)
    assert x.telegram_user_id == table_user.telegram_user_id

@pytest.mark.asyncio
async def test_add_new_user_db_is_exist(save_table_user, telegram_user=TELEGRAM_USER_1, table_user=TABLE_USER_1):
    x = await add_new_user_db(telegram_user)
    assert x.telegram_user_id == table_user.telegram_user_id
