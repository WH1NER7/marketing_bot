from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup_lk = InlineKeyboardMarkup(row_width=1)
inline_btn_1 = InlineKeyboardButton('FAQ', callback_data='faq')
inline_btn_2 = InlineKeyboardButton('Ссылка на WA', callback_data='wa_link')
markup_lk.add(inline_btn_1, inline_btn_2)

markup_competition = InlineKeyboardMarkup(row_width=1)
competition_btn_1 = InlineKeyboardButton('Добавить ссылку на Reels', callback_data='reels_link')
markup_competition.add(competition_btn_1)

markup_link = InlineKeyboardMarkup(row_width=1)
link_btn_1 = InlineKeyboardButton('Хочу изменить', callback_data='reels_link_upd')
markup_link.add(link_btn_1)