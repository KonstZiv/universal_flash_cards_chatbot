from app.tables import User
from tests.utils import TELEGRAM_USER_2, TELEGRAM_USER_1

TABLE_USER_1 = User(
    telegram_user_id=TELEGRAM_USER_1.id,
    telegram_language=TELEGRAM_USER_1.language_code,
    user_name=TELEGRAM_USER_1.full_name,
    first_name=TELEGRAM_USER_1.first_name,
    last_name=TELEGRAM_USER_1.last_name
)

TABLE_USER_2 = User(
    telegram_user_id=TELEGRAM_USER_2.id,
    telegram_language=TELEGRAM_USER_2.language_code,
    user_name=TELEGRAM_USER_2.full_name,
    first_name=TELEGRAM_USER_2.first_name,
    last_name=TELEGRAM_USER_2.last_name
)


