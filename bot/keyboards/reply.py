from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb_markup = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb_button1 = KeyboardButton("О нас")
start_kb_button2 = KeyboardButton("Служба заботы")
start_kb_button3 = KeyboardButton("Магазин")
# start_kb_button2 = KeyboardButton("Конкурс")
start_kb_button4 = KeyboardButton("Розыгрыш Iphone 15")
start_kb_button5 = KeyboardButton("Готовый подарок на Новый год")
start_kb_markup.add(start_kb_button1, start_kb_button2, start_kb_button3, start_kb_button4, start_kb_button5)
