from aiogram import Dispatcher, Bot, types
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.database.methods.get import check_link
from bot.database.methods.insert import create_user
from bot.database.methods.update import upd_link
from bot.keyboards.inline import markup_lk, markup_competition, markup_link, faq_kb, shop_kb, problems_kb, \
    markup_competition_extra
from bot.keyboards.reply import start_kb_markup
from bot.utils.misc import determine_uniqueness


class UpdLink(StatesGroup):
    waiting_link = State()


async def start(message: Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Поделиться контактом", request_contact=True)
    keyboard.add(button)

    text = "Для продолжения регистрации, поделитесь своим контактным номером."
    await message.answer(text, reply_markup=keyboard)



async def service(message: Message):
    video = types.InputFile('bot/images/раздел СЛУЖБА ЗАБОТЫ.MOV')
    await message.answer_video(caption=f'Мы тщательно следим за качеством пошива наших изделий. \n\
И всегда рады твоей обратной связи, чтобы сделать комплекты ещё лучше!🔥  \n\
Остались вопросы? Найди ответ из предложенных в “FAQ” или свяжись с нами',
            reply_markup=markup_lk,
            video=video,
            width=960, height=1460)


# async def competition(message: Message):
#     video = types.InputFile('bot/images/IMG_6397.MOV')
#     await message.answer_video(caption=f'Мы рады приветствовать тебя на старте нашего конкурса от бренда белья "MissYourKiss" 💋\n\
#     \n\
#     Здесь тебя ждет незабываемое путешествие, полное элегантного белья, творческих идей, и, конечно же, волшебства! \n\
#     \n\
#     Снимай рилсы в нашем белье и участвуй в конкурсе и получи шанс выиграть розовый iPhone 15! 🔥🔥\n\
#     \n\
#     Но это еще не все…\n\
#     🎁 еженедельно, в рамках конкурса, мы разыграем по комплекту нижнего белья для обладательницы лучшего рилса недели!\n\
#     \n\
#     Напоминаем, что конкурс будет длиться до конца декабря. Поэтому каждую неделю у тебя есть шанс выиграть приз!',
#                                video=video, reply_markup=markup_competition, width=960, height=1664)


async def about_us(message: Message):
    # photo = types.InputFile('bot/images/lif.jpg')
    video = types.InputFile('bot/images/IMG_9106.MP4')

    await message.answer_video(
        caption=
'Домашняя одежда от Naumova.brand - это уют, нежность и комфорт.\n\
\n\
Факты о бренде: \n\n\
📌 “Та самая пижама из Pinterest” впервые была сшита в 2017 году. \n\n\
📌 Трендовые модели и расцветки - приоритет бренда, для нас важно, чтобы дома каждая девушка выглядела на все 1000%!\n\n\
📌 Мы открыли свое производство в 2022 году, чтобы наши изделия выпускались под контролем, а наши клиенты получали качественные домашние комплекты.\n\n\
📌 За два года на Wildberries одели в пижаму 62 тыс девушек. А это на минуточку все население города Чистополь откуда мы родом.\n\
\n\
[Мы в нельзяграм](https://www.instagram.com/naumovaa.brand?igsh=MTlvNnE2aWF4YXdlbw==) \n\
\n\
[Мы на YouTube](https://youtube.com/@Naumovabraand?si=Ae33ChsL25mE-O5e) \n\
',
        video=video,
        # reply_markup=markup_competition,
        parse_mode=types.ParseMode.MARKDOWN)


async def faq_info(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, "Основые вопросы и ответы к ним\n", reply_markup=faq_kb)


async def get_contact(message: Message):
    contact = message.contact
    if contact:
        phone_number = contact.phone_number
        user_id = contact.user_id

        # await message.answer(text=f"Вы поделились контактом с номером {phone_number}")
        user_real_name = message.from_user.first_name
        user_second_name = message.from_user.last_name
        user_link_nice = message.from_user.username

        user_id = message.from_user.id
        create_user(user_real_name, user_second_name, user_id, user_link_nice, phone_number)

        photo = types.InputFile('bot/images/Start_Naumova.png')
        await message.answer_photo(
            caption=f'Привет, на связи самый уютный бренд домашней одежды Naumova.brand \n\nРады приветствовать тебя в нашем канале. \n\nЗдесь ты самой первой будешь получать новости о свежих конкурсах, акциях и новинках😍',
            reply_markup=start_kb_markup, photo=photo)
        # Добавьте здесь код, который вы хотите выполнить при поделиться контактом
    else:
        await message.answer(text="Пользователь не поделился контактом или произошла ошибка")


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
    photo = types.InputFile('bot/images/раздел КАТАЛОГ.png')
    text_with_link = "Благодаря размещению на онлайн-площадках с собственной логистикой мы можем предлагать самые приятные цены и доставлять товар в кратчайшие сроки"

    await message.answer_photo(caption=text_with_link, photo=photo, parse_mode=types.ParseMode.MARKDOWN, reply_markup=shop_kb)


async def ready_present(message: types.Message):
    photo_path = 'bot/images/раздел НОВИНКИ 1.jpg'
    photo_path2 = 'bot/images/раздел НОВИНКИ 2.jpg'

    text_with_link = "Мы создали невероятно комфортные ажурные пижамы для дома, которые не останутся незамеченными среди твоих близких! 😉 \n\n\
Уже доступны к заказу 👇 \n\
\n\
В белом цвете\n\
Артикул: [205953343](https://www.wildberries.ru/catalog/205953343/detail.aspx )\n\
\n\
В васильково-голубом цвете\n\
Артикул: [205988401](https://www.wildberries.ru/catalog/205988401/detail.aspx)\n\
"

    # Создаем список медиа-группы
    media_group = [
        types.InputMediaPhoto(media=InputFile(photo_path), caption='В белом цвете\n\
https://www.wildberries.ru/catalog/205953343/detail.aspx'),
        types.InputMediaPhoto(media=InputFile(photo_path2), caption='В васильково-голубом цвете\n\
https://www.wildberries.ru/catalog/205988401/detail.aspx')
    ]

    # Отправляем медиа-группу
    await message.bot.send_media_group(
        chat_id=message.chat.id,
        media=media_group,
    )

    # Отправляем текстовое сообщение
    await message.bot.send_message(
        chat_id=message.chat.id,
        text=text_with_link,
        parse_mode=types.ParseMode.MARKDOWN
    )


async def shocking_price(message: Message):
    photo_path1 = 'bot/images/раздел ШОК ЦЕНА 1.png'
    photo_path2 = 'bot/images/раздел ШОК ЦЕНА 2.png'
    photo_path3 = 'bot/images/раздел ШОК ЦЕНА 3.png'


    text_with_link = "Наши выгодные предложения по самым вкусным ценам  \n\
\n\
\n\
Комплект топов 2 шт. черный и молочный \n\
Артикул: [192010797](https://www.wildberries.ru/catalog/192010797/detail.aspx)\n\
\n\
Логслив розовый с вырезом\n\
Артикул: [151806844](https://www.wildberries.ru/catalog/151806844/detail.aspx)\n\
\n\
Лонгслив укороченный черный с вырезом на спине\n\
Артикул: [149341432](https://www.wildberries.ru/catalog/149341432/detail.aspx)\n\
\n\
Пижама со штанами шелковая\n\
Артикул: [147694388](https://www.wildberries.ru/catalog/147694388/detail.aspx)\n\
"

    # Создаем список медиа-группы
    media_group = [
        types.InputMediaPhoto(media=InputFile(photo_path1), caption="Комплект топов 2 шт. черный и молочный \n\
https://www.wildberries.ru/catalog/192010797/detail.aspx"),
        types.InputMediaPhoto(media=InputFile(photo_path2), caption='Пижама со штанами шелковая\n\
https://www.wildberries.ru/catalog/147694388/detail.aspx'),
        types.InputMediaPhoto(media=InputFile(photo_path3), caption='Лонгслив укороченный черный с вырезом на спине\n\
https://www.wildberries.ru/catalog/149341432/detail.aspx')
    ]

    # Отправляем медиа-группу
    await message.bot.send_media_group(
        chat_id=message.chat.id,
        media=media_group,
    )

    # Отправляем текстовое сообщение
    await message.bot.send_message(
        chat_id=message.chat.id,
        text=text_with_link,
        parse_mode=types.ParseMode.MARKDOWN
    )


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(service, content_types=['text'], text="Служба заботы")
    # dp.register_message_handler(competition, content_types=['text'], text="Розыгрыш Iphone 15")
    dp.register_message_handler(shocking_price, content_types=['text'], text="“ШОК ЦЕНА”")
    dp.register_message_handler(ready_present, content_types=['text'], text="Новинки")
    dp.register_message_handler(our_shop_link, content_types=['text'], text="Каталог бренда")
    dp.register_message_handler(about_us, content_types=['text'], text="О нас")

    dp.register_message_handler(get_contact, content_types=types.ContentType.CONTACT)

    dp.register_callback_query_handler(faq_info, lambda c: c.data == 'faq')
    dp.register_callback_query_handler(get_gift, lambda c: c.data == 'get_gift')
    dp.register_callback_query_handler(oferta, lambda c: c.data == 'oferta')
    dp.register_callback_query_handler(problems, lambda c: c.data == 'problems')
    dp.register_callback_query_handler(update_link, lambda c: c.data == 'reels_link_upd')
    dp.register_callback_query_handler(competition_full_info, lambda c: c.data == 'competition_full_info')
    dp.register_callback_query_handler(wa_link, lambda c: c.data == 'wa_link')
    dp.register_callback_query_handler(competition_link, lambda c: c.data == 'reels_link')

    dp.register_message_handler(get_link, state=UpdLink.waiting_link)
