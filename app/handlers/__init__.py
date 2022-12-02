from aiogram import Dispatcher

from app.handlers.personal import register_handlers_personal
from app.handlers.channels import register_handlers_channel


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_handlers_personal,
        register_handlers_channel
    )
    for handler in handlers:
        handler(dp)
