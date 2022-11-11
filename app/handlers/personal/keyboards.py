languages = ["Albanian", "Belarusian", "Chinese",
             "Croatian", "English", "Estonian",
             "French", "German", "Russian",
             "Ukrainian", ]

from aiogram.types import ReplyKeyboardRemove,\
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    KeyboardButtonPollType, PollType

markup_down = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(KeyboardButton('Add new word'))\
    .add(KeyboardButton('Train'))

select_language_keyboard = InlineKeyboardMarkup(resize_keyboard=True)

for i in range(0,len(languages)-1,3):
    select_language_keyboard.add(InlineKeyboardButton(languages[i], callback_data=languages[i]),
                                 InlineKeyboardButton(languages[i+1], callback_data=languages[i+1]),
                                 InlineKeyboardButton(languages[i+2], callback_data=languages[i+2]),)
select_language_keyboard.add(InlineKeyboardButton(languages[-1], callback_data=languages[-1]))

