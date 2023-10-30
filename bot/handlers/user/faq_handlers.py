from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery


async def uhod(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Рекомендуем стирать наши изделия при температуре не выше 30 градусов, выбрав деликатный режим в стиральной машинке, или вручную. Во избежание разводов сушить их необходимо вдали от обогревательных приборов. Соблюдая эти простые рекомендации, вы надолго сохраните первоначальный вид изделий.\n")


async def return_cb(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Вы можете проверить и примерить изделие в пункте выдачи заказов, после чего забрать или отказаться от него. После выкупа возврат качественного нижнего белья невозможен.")


async def defect(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Если вы обнаружили дефект товара, свяжитесь с нашей службой заботы. Есть несколько вариантов, как с нами связаться: \n\
\n\
1. Перейдите по QR-коду из открытки, которая прилагается к комплекту \n\
2. Напишите нам на Ватсап по номеру: +7 905 020 00 95 \n\
3. Перейдите ниже в чат с нами через кнопку “Служба заботы” \n\
\n\
Мы оперативно решим ваш вопрос. \n\
\n")


async def cert(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Все наши изделия имеют сертификаты соответствия.")


async def size(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Все изделия идут в размер и полностью соответствуют размерной сетке, которая расположена среди фотографий карточек. Для того, чтобы изделие идеально село на вас, рекомендуем измерить все ваши параметры и подобрать размер в соответствии с таблицей.")


async def price_return(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Хотим обратить ваше внимание, что нижнее белье относится к категории невозвратных товаров. Но на пункте выдачи заказов до выкупа товара вы можете вернуть его по любой причине. У нас нет платных отказов. Все денежные отношения на платформе, включая возвраты, регулирует сам маркетплейс.")


def register_faq_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(uhod, lambda c: c.data == 'uhod')
    dp.register_callback_query_handler(return_cb, lambda c: c.data == 'return')
    dp.register_callback_query_handler(defect, lambda c: c.data == 'defect')
    dp.register_callback_query_handler(cert, lambda c: c.data == 'cert')
    dp.register_callback_query_handler(size, lambda c: c.data == 'size')
    dp.register_callback_query_handler(price_return, lambda c: c.data == 'price_return')
