from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup_requests = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(KeyboardButton('Відіслати власну геолокацію'))\
    .add(KeyboardButton('Поділитись власним контактом'))

button_parent = KeyboardButton("for my children")
button_me = KeyboardButton("for me")
general_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_me).add(button_parent)