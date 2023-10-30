from aiogram import Dispatcher

from bot.handlers.user.faq_handlers import register_faq_handlers
from bot.handlers.user.main import register_users_handlers
from bot.handlers.user.shops_handlers import register_shop_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_users_handlers,
        register_faq_handlers,
        register_shop_handlers
    )
    for handler in handlers:
        handler(dp)