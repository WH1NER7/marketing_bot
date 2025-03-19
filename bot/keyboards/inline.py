from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup_lk = InlineKeyboardMarkup(row_width=1)
inline_btn_1 = InlineKeyboardButton('Часто задаваемые вопросы', callback_data='faq')
inline_btn_2 = InlineKeyboardButton(text="Помогите мне! У меня проблема", url="https://t.me/missyourkiss_manager_bot")
# inline_btn_3 = InlineKeyboardButton(text="Получить гайд", callback_data='get_a_guide')
markup_lk.add(inline_btn_1, inline_btn_2)

markup_competition = InlineKeyboardMarkup(row_width=1)
competition_btn_1 = InlineKeyboardButton('Добавить ссылку на Reels', callback_data='reels_link')
competition_btn_2 = InlineKeyboardButton('Подробнее условия конкурса', callback_data='competition_full_info')
markup_competition.add(competition_btn_1, competition_btn_2)

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
shop_btn_1 = InlineKeyboardButton('ВБ', url='https://www.wildberries.ru/brands/missyourkiss')
shop_btn_2 = InlineKeyboardButton('ОЗОН', url='https://www.ozon.ru/seller/missyourkiss-1043385/products/?miniapp=seller_1043385')
shop_kb.add(shop_btn_1, shop_btn_2)


problems_kb = InlineKeyboardMarkup(row_width=1)
problem_btn_1 = InlineKeyboardButton('Не мой размер (большемерит / маломерит)', callback_data='not_my_size')
problem_btn_2 = InlineKeyboardButton('Линяет', callback_data='shed')
problem_btn_3 = InlineKeyboardButton('Брак', callback_data='defective_goods')
problem_btn_4 = InlineKeyboardButton('Недокомплект', callback_data='not_full_complect')
problem_btn_5 = InlineKeyboardButton('Торчащие нитки', callback_data='protruding_threads')
problem_btn_6 = InlineKeyboardButton('Аллергия', callback_data='allergy')
problem_btn_7 = InlineKeyboardButton('Проблема с упаковкой', callback_data='bad_packing')
problem_btn_8 = InlineKeyboardButton('Пятна грязь', callback_data='dirty')
problem_btn_9 = InlineKeyboardButton('Не понравился', callback_data='did_not_like')
problem_btn_10 = InlineKeyboardButton('Пришел не наш товар', callback_data='wrong_good')
problem_btn_11 = InlineKeyboardButton('Не нравится качество', callback_data='bad_quality')
problem_btn_12 = InlineKeyboardButton('Комплект разного оттенка', callback_data='different_shades')
problem_btn_13 = InlineKeyboardButton(text="Свяжите меня с менеджером", url="https://t.me/missyourkiss_manager_bot")
problems_kb.add(problem_btn_1, problem_btn_2, problem_btn_3, problem_btn_4, problem_btn_5, problem_btn_6, problem_btn_7,
                problem_btn_8, problem_btn_9, problem_btn_10, problem_btn_11, problem_btn_12, problem_btn_13)


markup_competition_extra = InlineKeyboardMarkup(row_width=1)
competition_extra_btn_1 = InlineKeyboardButton('Добавить ссылку на Reels', callback_data='reels_link')
competition_extra_btn_2 = InlineKeyboardButton('Получить подарок', callback_data='get_gift')
competition_extra_btn_3 = InlineKeyboardButton('Прочитать оферту', callback_data='oferta')
markup_competition_extra.add(competition_extra_btn_1, competition_extra_btn_2, competition_extra_btn_3)

faq_kb_upd = InlineKeyboardMarkup(row_width=1)
faq_kb_btn2 = InlineKeyboardButton(text="Написать менеджеру", url="https://t.me/missyourkiss_manager_bot")
faq_kb_upd.add(faq_kb_btn2)

faq_kb_defect = InlineKeyboardMarkup(row_width=1)
# faq_kb_defect_btn1 = InlineKeyboardButton(text="Получить гайд", url="https://t.me/missyourkiss_manager_bot")
faq_kb_defect_btn2 = InlineKeyboardButton(text="Свяжите меня с менеджером", url="https://t.me/missyourkiss_manager_bot")
faq_kb_defect.add(faq_kb_defect_btn2)

problems_kb_add = InlineKeyboardMarkup(row_width=1)
problems_kb_btn1 = InlineKeyboardButton(text="Свяжите меня с менеджером", url="https://t.me/missyourkiss_manager_bot")
# problems_kb_btn2 = InlineKeyboardButton(text="Получить гайд", url="https://b24-dvx7b9.bitrix24.site/crm_form_ru7u6/")
problems_kb_add.add(problems_kb_btn1)


advert_kb = InlineKeyboardMarkup(row_width=1)
advert_button1 = InlineKeyboardButton(text="Перейти в тг-канал", url="https://t.me/+bpJ4QiiHAaowNjUy")
# problems_kb_btn2 = InlineKeyboardButton(text="Получить гайд", url="https://b24-dvx7b9.bitrix24.site/crm_form_ru7u6/")
advert_kb.add(advert_button1)
