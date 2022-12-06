# from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
#                            KeyboardButton, ReplyKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardBuilder, InlineKeyboardBuilder

languages = [
    "Albanian",
    "Belarusian",
    "Chinese",
    "Croatian",
    "English",
    "Estonian",
    "French",
    "German",
    "Russian",
    "Ukrainian",
]

markup_down = (
    ReplyKeyboardBuilder()
    .add(KeyboardButton(text="Add new word"))
    .add(KeyboardButton(text="Train"))
).as_markup()


select_language_keyboard = InlineKeyboardBuilder()

for i in range(0, len(languages) - 1, 3):
    select_language_keyboard.add(
        InlineKeyboardButton(text=languages[i], callback_data=languages[i]),
        InlineKeyboardButton(text=languages[i + 1], callback_data=languages[i + 1]),
        InlineKeyboardButton(text=languages[i + 2], callback_data=languages[i + 2]),
    )
select_language_keyboard.add(
    InlineKeyboardButton(text=languages[-1], callback_data=languages[-1])
)
select_language_keyboard = select_language_keyboard.as_markup()