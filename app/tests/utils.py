from aiogram.types import User
from app import tables

TELEGRAM_USER_1 = User(
    id=1,
    is_bot=False,
    first_name='Test',
    last_name='Bot',
    username='testbot_1',
    language_code='uk-UK',
    is_premium=False,
    added_to_attachment_menu=None,
    can_join_groups=None,
    can_read_all_group_messages=None,
    supports_inline_queries=None
)

TELEGRAM_USER_2 = User(
    id=2,
    is_bot=False,
    first_name='Test',
    last_name=None,
    username=None,
    language_code=None,
    is_premium=False,
    added_to_attachment_menu=None,
    can_join_groups=None,
    can_read_all_group_messages=None,
    supports_inline_queries=None
)


# TABLE_USER_1 = tables.User(
#     telegram_user_id=TELEGRAM_USER_1.id,
#     telegram_language=TELEGRAM_USER_1.language_code,
#     user_name=TELEGRAM_USER_1.full_name,
#     first_name=TELEGRAM_USER_1.first_name,
#     last_name=TELEGRAM_USER_1.last_name
# )
#
# TABLE_USER_2 = tables.User(
#     telegram_user_id=TELEGRAM_USER_2.id,
#     telegram_language=TELEGRAM_USER_2.language_code,
#     user_name=TELEGRAM_USER_2.full_name,
#     first_name=TELEGRAM_USER_2.first_name,
#     last_name=TELEGRAM_USER_2.last_name
# )
