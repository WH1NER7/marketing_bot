from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb_markup = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb_button1 = KeyboardButton("Служба заботы")
start_kb_button2 = KeyboardButton("Конкурс")
start_kb_markup.add(start_kb_button1, start_kb_button2)
