from datetime import datetime

from aiogram.types import User, Chat, Message, Update, CallbackQuery

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
    last_name='Bot',
    username='testbot_2',
    language_code='uk-UK',
    is_premium=False,
    added_to_attachment_menu=None,
    can_join_groups=None,
    can_read_all_group_messages=None,
    supports_inline_queries=None
)