import aiogram

from app.tables import Context, User, UserContext
from typing import Optional


async def add_new_user_db(data_telegram: aiogram.types.User) -> User:
    last_name: str = data_telegram.last_name
    if not last_name:
        last_name: str = ""
    user_existed: Optional[User] = await User.objects(User.all_related()).get(User.telegram_user_id == data_telegram.id)
    if user_existed:
        return user_existed
    user: User = User(
        telegram_user_id=data_telegram.id,
        telegram_language=data_telegram.language_code,
        user_name=data_telegram.username,
        first_name=data_telegram.first_name,
        last_name=last_name,
    )
    await user.save()
    return user


async def add_user_context_db(data_callback_query, user_db):
    context_1 = await Context.objects().get(
        Context.name == data_callback_query["native_lang"]
    )
    context_2 = await Context.objects().get(
        Context.name == data_callback_query["target_lang"]
    )
    user_context = UserContext(
        context_1=context_1,
        context_2=context_2,
        user=user_db,
    )
    await user_context.save()
    return user_context


async def user_context_is_exist_db(telegram_user_id):
    user_context = (
        await UserContext.objects(UserContext.all_related())
        .get(UserContext.user.telegram_user_id == telegram_user_id)
        .order_by(UserContext.last_date, ascending=False)
        .first()
    )

    return user_context
