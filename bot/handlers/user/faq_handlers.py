from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery

from bot.keyboards.inline import faq_kb_upd, faq_kb_defect


async def uhod(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Рекомендуем стирать наши изделия при температуре не выше 30 градусов, выбрав деликатный режим в стиральной машинке, или вручную.\n\
\n\
Во избежание разводов сушить их необходимо вдали от обогревательных приборов. Соблюдая эти простые рекомендации, вы надолго сохраните первоначальный вид изделий.", reply_markup=faq_kb_defect)


async def return_cb(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Вы можете проверить и примерить изделие в пункте выдачи заказов, после чего забрать или отказаться от него. \n\
\n\
После выкупа возврат качественного товара невозможен.\n\
\n\
Если вы обнаружили дефект товара, свяжитесь с нашей службой заботы. Есть несколько вариантов, как с нами связаться:\n\
\n\
1. Перейдите в “чат с продавцом” на Wildberries\n\
2. Перейдите ниже в чат с нами через кнопку “Свяжите меня с менеджером”\n\
\n\
И мы оперативно решим вопрос.", reply_markup=faq_kb_defect)


async def defect(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Если вы обнаружили дефект товара, свяжитесь с нашей службой заботы. Есть несколько вариантов, как с нами связаться: \n\
    \n\
1. Перейдите по QR-коду из открытки, которая прилагается к комплекту \n\
2. Перейдите ниже в чат с нами через кнопку “Свяжите меня с менеджером” \n\
    \n\
И мы оперативно решим ваш вопрос.\n\
", reply_markup=faq_kb_defect)


async def cert(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Все наши изделия имеют сертификаты соответствия, без них наши товары не смогли бы поступить в продажу.  Вы можете ознакомиться с ними на Wildberries.", reply_markup=faq_kb_defect)


async def size(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Все изделия идут в размер и полностью соответствуют размерной сетке, которая расположена среди фотографий карточек товара.\n\n\
Для того, чтобы изделие идеально село на вас, рекомендуем измерить все ваши параметры и подобрать размер в соответствии с таблицей, указанной на слайдах в карточках товара. Если у Вас возникли трудности с выбором размера, задайте нам вопрос на Wildberries или перейдите ниже в чат с нами через кнопку “Свяжите меня с менеджером”", reply_markup=faq_kb_defect )


async def price_return(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Хотим обратить ваше внимание, что пижамы относятся к категории невозвратных товаров. Но на пункте выдачи заказов до выкупа товара вы можете вернуть его по любой причине.\n\
\n\
У нас нет платных отказов. Все денежные отношения на платформе, включая возвраты, регулирует сам маркетплейс Wildberries.", reply_markup=faq_kb_defect )


def register_faq_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(uhod, lambda c: c.data == 'uhod')
    dp.register_callback_query_handler(return_cb, lambda c: c.data == 'return')
    dp.register_callback_query_handler(defect, lambda c: c.data == 'defect')
    dp.register_callback_query_handler(cert, lambda c: c.data == 'cert')
    dp.register_callback_query_handler(size, lambda c: c.data == 'size')
    dp.register_callback_query_handler(price_return, lambda c: c.data == 'price_return')
