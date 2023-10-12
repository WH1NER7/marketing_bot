from aiogram import Dispatcher, Bot, types
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.database.methods.get import check_link
from bot.database.methods.insert import create_user
from bot.database.methods.update import upd_link
from bot.keyboards.inline import markup_lk, markup_competition, markup_link
from bot.keyboards.reply import start_kb_markup
from bot.utils.misc import determine_uniqueness


class UpdLink(StatesGroup):
    waiting_link = State()


async def start(message: Message):
    user_real_name = message.from_user.first_name
    user_second_name = message.from_user.last_name
    user_link_nice = message.from_user.username

    user_id = message.from_user.id
    create_user(user_real_name, user_second_name, user_id, user_link_nice)

    photo = types.InputFile('bot/images/img.png')
    await message.answer(
        f'Привет, MissYourKiss girl 💋\nНа связи твой любимый бренд нижнего белья.\nРады приветствовать тебя в нашем чате. Здесь ты самой первой будешь получать новости о свежих конкурсах и новинках😍',
        reply_markup=start_kb_markup)
#     await message.answer_photo(caption=f'Ура! Даем старт самому крутому розыгрышу на просторах интернета. Такого еще не было нигде!\n\
# Никакого рандомайзера, где фортуна может быть не на твоей стороне. На этот раз все в твоих красивых руках.\n\
# Приз - новенький айфончик.\n\
# Сейчас расскажу тебе об условиях конкурса.\n\
# \n\
# Конкурс пройдет в 2 этапа \n\
# 1)Заказать на ВБ по ссылке () понравившееся тебе белье.\n\
# 2)Придумать классную идею и снять рилс в нашем белье.\n\
# 3)ВАЖНО. В комментарии поставь хештег # и отметь через <code><b>{"@missyourkiss.brand"}</b></code>. Отмечать на самом видео нас не нужно.\n\
# Так же обязательно подпиши артикулы белья в комментариях.\n\
# 4)Опубликуй видео в inst. Скопируй ссылку твоего рилс и отправь ее в этот чат по кнопке «отправить ссылку»\n\
# \n\
# Второй этап. Вы попадаете в нашу ленту. \n\
# \n\
# Наша суперская команда выбирает 10 самых лучших красивых и эстетичных рилс и публикует на нашей официальной страничке.\n\
# К концу конкурса остается лишь одно-самое лучшее видео. И его обладательница получает новенький айфон.\n\
# \n\
# P.S. Не забудь получить от нас подарок- гайд «Reels на миллион»', photo=photo, reply_markup=markup_competition)




async def service(message: Message):
    await message.answer(f'С другой стороны, социально-экономическое развитие однозначно фиксирует необходимость анализа существующих паттернов поведения. Современные технологии достигли такого уровня, что курс на социально-ориентированный национальный проект однозначно определяет каждого участника как способного принимать собственные решения касаемо дальнейших направлений развития. В своём стремлении улучшить пользовательский опыт мы упускаем, что представители современных социальных резервов описаны максимально подробно!', reply_markup=markup_lk)


async def competition(message: Message):
    photo = types.InputFile('bot/images/img.png')
    await message.answer_photo(caption=f'Ура! Даем старт самому крутому розыгрышу на просторах интернета. Такого еще не было нигде!\n\
Никакого рандомайзера, где фортуна может быть не на твоей стороне. На этот раз все в твоих красивых руках.\n\
Приз - новенький айфончик.\n\
Сейчас расскажу тебе об условиях конкурса.\n\
\n\
Конкурс пройдет в 2 этапа \n\
1)Заказать на ВБ по ссылке () понравившееся тебе белье.\n\
2)Придумать классную идею и снять рилс в нашем белье.\n\
3)ВАЖНО. В комментарии поставь хештег # и отметь через <code><b>{"@missyourkiss.brand"}</b></code>. Отмечать на самом видео нас не нужно.\n\
Так же обязательно подпиши артикулы белья в комментариях.\n\
4)Опубликуй видео в inst. Скопируй ссылку твоего рилс и отправь ее в этот чат по кнопке «отправить ссылку»\n\
\n\
Второй этап. Вы попадаете в нашу ленту. \n\
\n\
Наша суперская команда выбирает 10 самых лучших красивых и эстетичных рилс и публикует на нашей официальной страничке.\n\
К концу конкурса остается лишь одно-самое лучшее видео. И его обладательница получает новенький айфон.\n\
\n\
P.S. Не забудь получить от нас подарок- гайд «Reels на миллион»', photo=photo, reply_markup=markup_competition)


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
        await callback_query.message.edit_text("Отправляя ссылку вы автоматически даете согласие на использование его в личных целях бренда.\n\
        \n\
Контент должен быть этичным.\n\
Видео содержащие пошлость, насилие - вне конкурса.\n")


async def update_link(callback_query: CallbackQuery):
    await UpdLink.waiting_link.set()
    await callback_query.message.edit_text("Отправляя ссылку вы автоматически даете согласие на использование его в личных целях бренда.\n\
\n\
Контент должен быть этичным.\n\
Видео содержащие пошлость, насилие - вне конкурса.\n")


async def get_link(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_link = message.from_user.url
    user_link_nice = message.from_user.username
    link = message.text
    unique = determine_uniqueness(link)
    print(link)
    if link[0:30] == 'https://www.instagram.com/reel' and unique:
        upd_link(user_id, link)
        await message.answer(f'Ссылка принята', reply_markup=start_kb_markup)
        await state.finish()
    elif link[0:30] != 'https://www.instagram.com/reel':
        # print(user_link, user_link_nice)
        # upd_link(user_id, link)
        await message.answer(f'Ссылка не с платформы Instagram', reply_markup=start_kb_markup)
        await state.finish()
    elif not unique:
        await message.answer(f'Данная ссылка уже участвует в конкурсе', reply_markup=start_kb_markup)
        await state.finish()


async def our_shop_link(message: Message):
    text_with_link = "[Посетите наш магазин на Wildberries](https://www.wildberries.ru/brands/missyourkiss)"

    await message.answer(text_with_link, parse_mode=types.ParseMode.MARKDOWN)


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(service, content_types=['text'], text="Служба заботы")
    dp.register_message_handler(competition, content_types=['text'], text="Конкурс")
    dp.register_message_handler(our_shop_link, content_types=['text'], text="Наш магазин")

    dp.register_callback_query_handler(faq_info, lambda c: c.data == 'faq')
    dp.register_callback_query_handler(update_link, lambda c: c.data == 'reels_link_upd')
    dp.register_callback_query_handler(wa_link, lambda c: c.data == 'wa_link')
    dp.register_callback_query_handler(competition_link, lambda c: c.data == 'reels_link')

    dp.register_message_handler(get_link, state=UpdLink.waiting_link)
