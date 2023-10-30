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

faq_kb = InlineKeyboardMarkup(row_width=1)
faq_btn_1 = InlineKeyboardButton('Как правильно ухаживать за изделиями?', callback_data='uhod')
faq_btn_2 = InlineKeyboardButton('Возможен ли возврат товара, если он мне не подойдет?', callback_data='return')
faq_btn_3 = InlineKeyboardButton('Что делать, если у товара дефект?', callback_data='defect')
faq_btn_4 = InlineKeyboardButton('Сертифицирован ли ваш товар?', callback_data='cert')
faq_btn_5 = InlineKeyboardButton('Большемерят или маломерят ваши товары?', callback_data='size')
faq_btn_6 = InlineKeyboardButton('Платный ли у вас возврат?', callback_data='price_return')
faq_kb.add(faq_btn_1, faq_btn_2, faq_btn_3, faq_btn_4, faq_btn_5, faq_btn_6)


shop_kb = InlineKeyboardMarkup(row_width=1)
shop_btn_1 = InlineKeyboardButton('ВБ', callback_data='wb')
shop_btn_2 = InlineKeyboardButton('ОЗОН', callback_data='ozon')
shop_btn_3 = InlineKeyboardButton('ДЕТСКИЙ МИР', callback_data='detmir')
shop_btn_4 = InlineKeyboardButton('Л`ЭТУАЛЬ', callback_data='letual')
shop_kb.add(shop_btn_1, shop_btn_2, shop_btn_3, shop_btn_4)
