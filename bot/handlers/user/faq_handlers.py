from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery

from bot.keyboards.inline import faq_kb_upd, faq_kb_defect


async def uhod(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Рекомендуем стирать наши изделия при температуре не выше 30 градусов, выбрав деликатный режим в стиральной машинке, или вручную. \n\
    \n\
Во избежание разводов сушить их необходимо вдали от обогревательных приборов. Соблюдая эти простые рекомендации, вы надолго сохраните первоначальный вид изделий. \n\
    \n\
У Вас есть уникальная возможность получить “Гайд по стилю” из 30 страниц.\n\
    \n", reply_markup=faq_kb_upd)


async def return_cb(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Вы можете проверить и примерить изделие в пункте выдачи заказов, после чего забрать или отказаться от него. \n\
    \n\
После выкупа возврат качественного нижнего белья невозможен.\n\
")


async def defect(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Если вы обнаружили дефект товара, свяжитесь с нашей службой заботы. Есть несколько вариантов, как с нами связаться: \n\
    \n\
1. Перейдите по QR-коду из открытки, которая прилагается к комплекту \n\
2. Перейдите ниже в чат с нами через кнопку “Свяжите меня с менеджером” \n\
    \n\
И мы оперативно решим ваш вопрос.\n\
    \n\
У Вас есть уникальная возможность получить “Гайд по стилю” из 30 страниц. ", reply_markup=faq_kb_defect)


async def cert(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Все наши изделия имеют сертификаты соответствия.\n\
    \n\
У Вас есть уникальная возможность получить “Гайд по стилю” из 30 страниц.", reply_markup=faq_kb_upd)


async def size(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Все изделия идут в размер и полностью соответствуют размерной сетке, которая расположена среди фотографий карточек.\n\
    \n\
Для того, чтобы изделие идеально село на вас, рекомендуем измерить все ваши параметры и подобрать размер в соответствии с таблицей.\n\
    \n\
У Вас есть уникальная возможность получить “Гайд по стилю” из 30 страниц.", reply_markup=faq_kb_upd)


async def price_return(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Хотим обратить ваше внимание, что нижнее белье относится к категории невозвратных товаров. Но на пункте выдачи заказов до выкупа товара вы можете вернуть его по любой причине.\n\
    \n\
У нас нет платных отказов. Все денежные отношения на платформе, включая возвраты, регулирует сам маркетплейс.\n\
    \n\
У Вас есть уникальная возможность получить “Гайд по стилю” из 30 страниц.", reply_markup=faq_kb_upd)


def register_faq_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(uhod, lambda c: c.data == 'uhod')
    dp.register_callback_query_handler(return_cb, lambda c: c.data == 'return')
    dp.register_callback_query_handler(defect, lambda c: c.data == 'defect')
    dp.register_callback_query_handler(cert, lambda c: c.data == 'cert')
    dp.register_callback_query_handler(size, lambda c: c.data == 'size')
    dp.register_callback_query_handler(price_return, lambda c: c.data == 'price_return')
