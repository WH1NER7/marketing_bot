from os import getenv

from aiogram import Dispatcher, Bot, types
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


from bot.database.methods.get import check_link, get_all_user_ids
from bot.database.methods.insert import create_user, insert_broadcast_stats
from bot.database.methods.update import upd_link, increment_button_counter
from bot.keyboards.inline import markup_lk, markup_competition, markup_link, faq_kb, shop_kb, problems_kb, \
    markup_competition_extra
from bot.keyboards.reply import start_kb_markup


from bot.utils.misc import determine_uniqueness


class UpdLink(StatesGroup):
    waiting_link = State()


# async def start(message: Message):
#     increment_button_counter("start")
#
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button = types.KeyboardButton("Поделиться контактом", request_contact=True)
#     keyboard.add(button)
#
#     text = "Для продолжения регистрации, поделитесь своим контактным номером."
#     await message.answer(text, reply_markup=keyboard)


async def service(message: Message):
    increment_button_counter("service")

    video = types.InputFile('bot/images/IMG_6456.MOV')
    await message.answer_video(caption=f'Мы тщательно следим за качеством пошива наших изделий. \n\
И всегда рады твоей обратной связи, чтобы сделать комплекты ещё лучше!🔥  \n\
Остались вопросы? Найди ответ из предложенных в “FAQ” или свяжись с нами',
            reply_markup=markup_lk,
            video=video,
            width=960, height=1460)


async def about_us(message: Message):
    increment_button_counter("about_us")

    video = types.InputFile('bot/images/letnee_video.mp4')

    await message.answer_video(
        caption=
'Искренне благодарим Вас за выбор нашего бренда.\n\
MissYourKiss\n\
- это нижнее белье, аксессуары и купальники\n\
- это российское производство\n\
- это сексуальность и чувственность в каждом движении\n\
- это быть готовой к особому случаю в любой момент\n\
\n\
[Мы в нельзяграм](https://instagram.com/missyourkiss.brand?igshid=MzRlODBiNWFlZA==) \n\
\n\
[Мы на YouTube](https://www.youtube.com/@missyourkiss)\n\
\n\
[Мы на Pinterest](https://pin.it/2n7w8Efa9)\n\
',
        video=video,
        # reply_markup=markup_competition,
        parse_mode=types.ParseMode.MARKDOWN)


async def faq_info(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Основые вопросы и ответы к ним\n", reply_markup=faq_kb)


async def start(message: Message):
    increment_button_counter("start")

    user_id = message.from_user.id

    # await message.answer(text=f"Вы поделились контактом с номером {phone_number}")
    user_real_name = message.from_user.first_name
    user_second_name = message.from_user.last_name
    user_link_nice = message.from_user.username

    user_id = message.from_user.id
    create_user(user_real_name, user_second_name, user_id, user_link_nice)

    photo = types.InputFile('bot/images/для ТГ.jpg')

    await message.answer_photo(
        caption=f'Привет, милая! \nНа связи твой любимый бренд нижнего белья MissYourKiss 💋 \nРады приветствовать тебя в нашем канале. Здесь ты самой первой будешь получать новости о свежих конкурсах, акциях и новинках😍',
        reply_markup=start_kb_markup, photo=photo)


async def get_gift(callback_query: CallbackQuery):
    gift = types.InputFile('bot/images/Reels на миллион.pdf')
    await callback_query.message.answer_document(document=gift, caption='Твой подарок 🎁')


async def oferta(callback_query: CallbackQuery):
    gift = types.InputFile('bot/images/Положение.pdf')
    await callback_query.message.answer_document(document=gift, caption='Публичная оферта')


async def problems(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Основые вопросы по товарам и ответы к ним\n", reply_markup=problems_kb)


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
        await callback_query.message.answer("Вы уже вводили ссылку, хотите заменить?\n", reply_markup=markup_link) # ТУТ ДОБАВИТЬ КЛАВИАТУРУ (ХОТИTЕ/НЕ ХОТИТЕ?)
    else:
        await UpdLink.waiting_link.set()
        await callback_query.message.answer("Отправляя ссылку вы автоматически даете согласие на использование его в личных целях бренда.\n\
\n\
Контент должен быть этичным.\n\
Видео содержащие пошлость, насилие - вне конкурса.\n")


async def update_link(callback_query: CallbackQuery):
    await UpdLink.waiting_link.set()
    await callback_query.message.answer("Отправляя ссылку вы автоматически даете согласие на использование его в личных целях бренда.\n\
\n\
Контент должен быть этичным.\n\
Видео содержащие пошлость, насилие - вне конкурса.\n")


async def competition_full_info(callback_query: CallbackQuery):
    video = types.InputFile('bot/images/IMG_6433.MOV')
    await callback_query.message.answer_video(caption="Конкурс пройдет в 2 этапа:\n\
\n\
ПЕРВЫЙ ЭТАП (14.11.2023-20.12.2023)\n\
\n\
1)[Заказать на ВБ](https://www.wildberries.ru/brands/missyourkiss ) понравившееся тебе белье.\n\
2) Придумать классную идею и снять рилс в нашем белье.\n\
3) ВАЖНО: Выкладывая рилс, не забудь указать артикул твоего комплекта 😉\n\
4) Опубликуй видео в inst. \n\
5) Скопируй ссылку твоего рилс и отправь ее в этот чат по кнопке «отправить ссылку», чтобы зарегистрироваться в розыгрыше\n\
\n\
ВТОРОЙ ЭТАП. \n\
(20.12.2023 - 30.12.2023)\n\
\n\
Наша команда экспертов выбирает 5 самых красивых и эстетичных рилс с разными просмотрами и публикует в официальном [блоге бренда](https://instagram.com/missyourkiss.brand?igshid=MzMyNGUyNmU2YQ==)  , где совместно с подписчиками мы выбираем победителя конкурса и одно самое лучшее видео с просмотрами на миллион. И его обладатель получает новенький айфон 15!\n\
\n\
P.S. А чтобы твой рилс залетел на миллионы просмотров, команда наших экспертов собрала гайд «Reels на миллион» с рекомендациями в подарок!\n\
", video=video, reply_markup=markup_competition_extra,  parse_mode=types.ParseMode.MARKDOWN)


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
    increment_button_counter("our_shop_link")

    photo = types.InputFile('bot/images/wb_ozon.png')
    text_with_link = "Благодаря размещению на онлайн-площадках с собственной логистикой мы можем предлагать самые приятные цены и доставлять товар в кратчайшие сроки"

    await message.answer_photo(caption=text_with_link, photo=photo, parse_mode=types.ParseMode.MARKDOWN, reply_markup=shop_kb)


async def ready_present(message: types.Message):
    increment_button_counter("ready_present")

    video_path = 'bot/images/IMG_9221.MOV'

    text_with_link = "Мы обо всем позаботились и собрали подарочные боксы!! 🎁 \n\
Дари самым близким только лучшее бельё от MissYourKiss 💋 \n\
Переходи и выбирай  ⬇️ \n\
\n\
\n\
Страстный красный комплект\n\
Артикул: [196719351](https://missyourkiss.mobz.click/radmyk)\n\
\n\
Чувственный пудровый комплект\n\
Артикул: [196717464](https://missyourkiss.mobz.click/pudramyk)\n\
\n\
Интригующий чёрный комплект\n\
Артикул: [196720365](https://missyourkiss.mobz.click/blackmyk)\n\
\n\
Чёрные трусики в подарочном мешочке\n\
Артикул: [196691686](https://missyourkiss.mobz.click/drblackmyk)\n\
\n\
Пудровые трусики в подарочном мешочке\n\
Артикул: [196692315](https://missyourkiss.mobz.click/drpudramyk)\n\
"

    await message.bot.send_video(
        chat_id=message.chat.id,
        caption=text_with_link,
        video=open(video_path, 'rb'),
        parse_mode=types.ParseMode.MARKDOWN
    )


async def shocking_price(message: Message):
    increment_button_counter("shocking_price")

    photo = types.InputFile('bot/images/kupalnik.jpg')

    text_with_link = "Самые яркие летние комплекты по самым вкусным ценам. Будь яркой каждый день, переходи и выбирай \n\
\n\
\n\
Наш TOP бикини купальник TIGER 🔥\n\
Артикул: [218272630](https://www.wildberries.ru/catalog/218272630/detail.aspx?targetUrlBP)\n\
\n\
Черный бикини купальник\n\
Артикул: [218272629](https://www.wildberries.ru/catalog/218272629/detail.aspx?targetUrlBP)\n\
\n\
Туника пляжная\n\
Артикул: [226609836](https://www.wildberries.ru/catalog/226609836/detail.aspx?targetUrl=BP)\n\
\n\
Кроп топ пляжный\n\
Артикул: [158417968](https://www.wildberries.ru/catalog/158417968/detail.aspx?targetUrl=BP)"

    await message.answer_photo(caption=text_with_link, photo=photo, parse_mode=types.ParseMode.MARKDOWN)


bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")
bot = Bot(token=bot_token, parse_mode="HTML")


async def send_broadcast_with_media_group(photo_paths, message_text):
    subscribers = get_all_user_ids()

    photo_path1 = 'bot/images/broadcast1.MP4'
    photo_path2 = 'bot/images/3.jpg'
    photo_path3 = 'bot/images/3.jpg'

    blocked_users = 0
    successful_sends = 0
    # Создаем список медиа-группы
    media_group = [
            types.InputMediaPhoto(media=InputFile(photo_path1), caption="Комплект топов 2 шт. черный и молочный \n\
    https://www.wildberries"),
            types.InputMediaPhoto(media=InputFile(photo_path2), caption='Пижама со штанами шелковая\n\
    https://www.wildberri'),
            types.InputMediaPhoto(media=InputFile(photo_path3), caption='Лонгслив укороченный черный с вырезом на спине\n\
    https://www.wildberri')
        ]

    text_with_link = "Прекрасный свадебный сезон начался ! 💍🩵\n\
\n\
Выбери универсальное бежевое белье для своего особенного дня.\n\
Или белоснежный комплект, чтобы почувствовать себя настоящей принцессой 😍\n\
\n\
🔗 [БЕЖЕВЫЙ КОМПЛЕКТ](https://www.wildberries.ru/catalog/132673611/detail.aspx?targetUrl=MS)\n\
🔗 [БЕЛЫЙ КОМПЛЕКТ](https://www.wildberries.ru/catalog/111821934/detail.aspx?targetUrl=MS)"

    for subscriber_id in subscribers:
        try:
            # Отправляем медиа-группу каждому подписчику
            # await bot.send_media_group(chat_id=subscriber_id, media=media_group)
            # await bot.send_message(chat_id=subscriber_id, text=text_with_link)
            await bot.send_video(subscriber_id, video=types.InputFile(photo_path1), caption=text_with_link,
                                 parse_mode=types.ParseMode.MARKDOWN, reply_markup=start_kb_markup)
            successful_sends += 1
        except Exception as e:
            print(f"Не удалось отправить сообщение подписчику {subscriber_id}: {str(e)}")
            blocked_users += 1

    insert_broadcast_stats(blocked_users, successful_sends)


# Пример использования функции рассылки с медиа-группой
async def on_broadcast_media_group_command(message: Message):
    photo_paths = ['bot/images/shok_cena.jpg', 'bot/images/shok_cena.jpg', 'bot/images/shok_cena.jpg']
    message_text = 'Текст текст текст текст \n' \
                   'текст на другой строке'
    await send_broadcast_with_media_group(photo_paths, message_text)


async def broadcast_command(message: Message):
    user_id = message.from_user.id
    if user_id == 615742233:
        await on_broadcast_media_group_command(message)
    else:
        await message.answer(text='Вы не являетесь администратором')


async def send_file(callback_query: CallbackQuery):
    # Загрузка файла на сервер или получение его пути
    file_path = 'bot/images/Reels на миллион.pdf'  # Укажите путь к вашему файлу

    await callback_query.message.answer_document(open(file_path, "rb"))


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(broadcast_command, commands=["broadcast"])
    dp.register_message_handler(service, content_types=['text'], text="Служба заботы")

    dp.register_message_handler(shocking_price, content_types=['text'], text="Пляжная коллекция")
    dp.register_message_handler(ready_present, content_types=['text'], text="Готовый подарок")
    dp.register_message_handler(our_shop_link, content_types=['text'], text="Каталог бренда")
    dp.register_message_handler(about_us, content_types=['text'], text="О нас")

    dp.register_callback_query_handler(faq_info, lambda c: c.data == 'faq')
    dp.register_callback_query_handler(get_gift, lambda c: c.data == 'get_gift')
    dp.register_callback_query_handler(oferta, lambda c: c.data == 'oferta')
    dp.register_callback_query_handler(problems, lambda c: c.data == 'problems')
    dp.register_callback_query_handler(update_link, lambda c: c.data == 'reels_link_upd')
    dp.register_callback_query_handler(competition_full_info, lambda c: c.data == 'competition_full_info')
    dp.register_callback_query_handler(wa_link, lambda c: c.data == 'wa_link')
    dp.register_callback_query_handler(competition_link, lambda c: c.data == 'reels_link')
    dp.register_callback_query_handler(send_file, lambda c: c.data == 'get_a_guide')

    dp.register_message_handler(get_link, state=UpdLink.waiting_link)
