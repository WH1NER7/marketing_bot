from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from os import getenv
from aiogram.types import Message
from sys import exit
import logging

from bot.database.methods.get import get_all_user_ids
from bot.handlers.main import register_all_handlers

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")
bot = Bot(token=bot_token, parse_mode="HTML")




async def __on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)


def start_bot():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
