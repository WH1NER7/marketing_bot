from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.database.methods.get import check_link
from bot.database.methods.insert import create_user
from bot.database.methods.update import upd_link
from bot.keyboards.inline import markup_lk, markup_competition, markup_link
from bot.keyboards.reply import start_kb_markup


class UpdLink(StatesGroup):
    waiting_link = State()


async def start(message: Message):
    user_real_name = message.from_user.first_name
    user_second_name = message.from_user.last_name
    user_link_nice = message.from_user.username

    user_id = message.from_user.id
    create_user(user_real_name, user_second_name, user_id, user_link_nice)
    await message.answer(
        f'Приветствую, <b>{user_real_name}</b>! Как дела?', reply_markup=start_kb_markup)
    # user_id = message.from_user.id
    # username = message.from_user.username
    # user_real_name = message.chat.first_name
    #
    # if not await known_user(user_id):
    #     await message.answer(
    #         f'Приветствую, <b>{user_real_name}</b>! Это бот для управления магазином на Wildberries.\n'
    #         'Возможно у вас есть код для присоединения к компании.\n'
    #         'Желаете ввести его?', reply_markup=enter_token_markup)
    # elif allowAccess(user_id) and not await known_user(message.from_user.id):
    #     create_user(user_id, username, 'MissYourKiss', 100000)
    #     await message.answer(
    #         f'Приветствую, <b>{message.chat.first_name}</b>! Это бот для управления магазином на Wildberries.\n',
    #         reply_markup=start_kb_markup)
    # elif allowAccess(user_id) and await known_user(message.from_user.id) and get_active_company(message.from_user.id) == "":
    #     upd_user_name(user_id, username)
    #     await message.answer(
    #         f'Приветствую, <b>{message.chat.first_name}</b>! Это бот для управления магазином на Wildberries.\n'
    #         'Возможно у вас есть код для присоединения к компании.\n'
    #         'Желаете ввести его?', reply_markup=enter_token_markup)
    # elif await known_user(message.from_user.id) and not allowAccess(user_id):
    #     upd_user_name(user_id, username)
    #     await message.answer(
    #         f'Приветствую, <b>{message.chat.first_name}</b>! Это бот для управления магазином на Wildberries.\n',
    #         reply_markup=start_kb_markup)
    # elif allowAccess(user_id) and await known_user(message.from_user.id):
    #     upd_user_name(user_id, username)
    #     await message.answer(
    #         f'Приветствую, <b>{message.chat.first_name}</b>! Это бот для управления магазином на Wildberries.\n',
    #         reply_markup=start_kb_markup)


async def service(message: Message):
    await message.answer(f'С другой стороны, социально-экономическое развитие однозначно фиксирует необходимость анализа существующих паттернов поведения. Современные технологии достигли такого уровня, что курс на социально-ориентированный национальный проект однозначно определяет каждого участника как способного принимать собственные решения касаемо дальнейших направлений развития. В своём стремлении улучшить пользовательский опыт мы упускаем, что представители современных социальных резервов описаны максимально подробно!', reply_markup=markup_lk)


async def competition(message: Message):
    await message.answer(f'Ясность нашей позиции очевидна: понимание сути ресурсосберегающих технологий выявляет срочную потребность анализа существующих паттернов поведения.', reply_markup=markup_competition)


async def faq_info(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Принимая во внимание показатели успешности, убеждённость некоторых оппонентов предоставляет широкие возможности для инновационных методов управления процессами.\n")


async def wa_link(callback_query: CallbackQuery):
    # await callback_query.answer('link link link\n'
    #                             'link link link\n'
    #                             'link link link')
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Прежде всего, синтетическое тестирование, в своём классическом представлении, допускает внедрение экспериментов, поражающих по своей масштабности и грандиозности.\n")


async def competition_link(callback_query: CallbackQuery):
    # await callback_query.answer('link link link\n'
    #                             'link link link\n'
    #                             'link link link')
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    if check_link(user_id):
        await callback_query.message.edit_text("Вы уже вводили ссылку, хотите заменить?\n", reply_markup=markup_link) # ТУТ ДОБАВИТЬ КЛАВИАТУРУ (ХОТИTЕ/НЕ ХОТИТЕ?)
    else:
        await UpdLink.waiting_link.set()
        await callback_query.message.edit_text("Введите ссылку\n")


async def update_link(callback_query: CallbackQuery):
    await UpdLink.waiting_link.set()
    await callback_query.message.edit_text("Введите ссылку\n")


async def get_link(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_link = message.from_user.url
    user_link_nice = message.from_user.username
    link = message.text
    print(link)
    if link[0:30] == 'https://www.instagram.com/reel':

        upd_link(user_id, link)
        await message.answer(f'Ссылка принята')
        await state.finish()
    else:
        # print(user_link, user_link_nice)
        # upd_link(user_id, link)
        await message.answer(f'Ссылка не с платформы Instagram')
        await state.finish()


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(service, content_types=['text'], text="Служба заботы")
    dp.register_message_handler(competition, content_types=['text'], text="Конкурс")

    dp.register_callback_query_handler(faq_info, lambda c: c.data == 'faq')
    dp.register_callback_query_handler(update_link, lambda c: c.data == 'reels_link_upd')
    dp.register_callback_query_handler(wa_link, lambda c: c.data == 'wa_link')
    dp.register_callback_query_handler(competition_link, lambda c: c.data == 'reels_link')

    dp.register_message_handler(get_link, state=UpdLink.waiting_link)
