from aiogram import Dispatcher


def register_handlers_channel(dp: Dispatcher) -> None:
    handlers = ()
    for handler in handlers:
        handler(dp)
