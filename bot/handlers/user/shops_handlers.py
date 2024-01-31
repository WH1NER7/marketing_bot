from aiogram import Dispatcher, Bot, types
from aiogram.types import CallbackQuery


# async def wb(callback_query: CallbackQuery):
#     bot: Bot = callback_query.bot
#     user_id = callback_query.from_user.id
#     await bot.send_message(user_id, "[Посетите наш магазин на Wildberries](https://www.wildberries.ru/brands/missyourkiss)",
#                            parse_mode=types.ParseMode.MARKDOWN)
#
#
# async def ozon(callback_query: CallbackQuery):
#     bot: Bot = callback_query.bot
#     user_id = callback_query.from_user.id
#     await bot.send_message(user_id, "[Посетите наш магазин на OZON](https://www.ozon.ru/seller/missyourkiss-1043385/products/?miniapp=seller_1043385)",
#                            parse_mode=types.ParseMode.MARKDOWN)
#
#
# async def detmir(callback_query: CallbackQuery):
#     bot: Bot = callback_query.bot
#     user_id = callback_query.from_user.id
#     await bot.send_message(user_id, "[Посетите наш магазин в Детском мире](https://www.detmir.ru/catalog/index/name/sortforbrand/brand/73580/)",
#                            parse_mode=types.ParseMode.MARKDOWN)


async def letual(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "[Посетите наш магазин в Л`етуаль](https://www.letu.ru/merchant/184800001)",
                           parse_mode=types.ParseMode.MARKDOWN)


def register_shop_handlers(dp: Dispatcher) -> None:
    # dp.register_callback_query_handler(wb, lambda c: c.data == 'wb')
    # dp.register_callback_query_handler(ozon, lambda c: c.data == 'ozon')
    # dp.register_callback_query_handler(detmir, lambda c: c.data == 'detmir')
    dp.register_callback_query_handler(letual, lambda c: c.data == 'letual')

