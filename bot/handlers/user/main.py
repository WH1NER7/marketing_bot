from datetime import datetime
from os import getenv

from aiogram import Dispatcher, Bot, types
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


from bot.database.methods.get import check_link, get_all_user_ids, get_all_users
from bot.database.methods.insert import create_user, insert_broadcast_stats, insert_poll_response, \
    update_poll_statistics, insert_quiz_stats
from bot.database.methods.update import upd_link, increment_button_counter
from bot.keyboards.inline import markup_lk, markup_competition, markup_link, faq_kb, shop_kb, problems_kb, \
    markup_competition_extra, advert_kb
from bot.keyboards.reply import start_kb_markup


from bot.utils.misc import determine_uniqueness
import logging

logging.basicConfig(level=logging.INFO)


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

    photo = types.InputFile('bot/images/IMG_1785.MP4')

    await message.answer_video(
        caption=f'<b>Привет, милая! Рады тебя видеть в нашем комьюнити любителей нижнего белья MissYourKiss💋</b>\n\
\n\
Здесь ты всегда будешь в курсе всех наших самых сочных новостей:\n\
\n\
▫️Горячие конкурсы, где ты сможешь выиграть крутое нижнее белье\n\
▫️Скидки и акции, от которых ты не сможешь отказаться\n\
▫️Анонсы наших самых свежих коллекций, которые заставят твое сердечко биться чаще❤️\n\
\n\
<b>Заглядывай к нам почаще, и мы обещаем, что не дадим тебе скучать!</b>',
        reply_markup=start_kb_markup, video=photo, parse_mode="HTML")


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

    video_path = 'bot/images/img_13.png'

    text_with_link = "<b>❗️BIG SALE❗️</b>\n\
\n\
На Wildberries стартовала масштабная акция🔥\n\
\n\
Сейчас ты можешь заказать множество товаров по выгодным ценам, в том числе и наше белье😍\n\
\n\
Скорее переходи в <a href='https://www.wildberries.ru/brands/missyourkiss'>магазин</a> кидай в корзину свои желанные комплекты, пока их не раскупили🛒\n\
\n\
А еще при покупке от 4000₽ ты сможешь поучаствовать в розыгрыше квартиры в Москве, iPhone и других классных призов!"

    await message.bot.send_photo(
        chat_id=message.chat.id,
        caption=text_with_link,
        photo=open(video_path, 'rb'),
        parse_mode=types.ParseMode.HTML
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
    # Получаем список пользователей с их именами
    user_id_and_name = get_all_users()

    # Путь к фото, которое будет отправлено
    photo_path1 = 'bot/images/img_36.png'

    print(user_id_and_name)

    blocked_users = 0
    successful_sends = 0

    # Шаблон сообщения с плейсхолдером {name}
    message_template = (
        "{name}, будь внимательна! Это тихий зов чувственности, предназначенный только для тебя.\n\
    \n\
Грациозность и скрытая сила - твое второе 'я'.\n\
Наш новый комплект:\n\
    \n\
Леопардовый принт — это не просто узор, это тихий зов, обращенный только к тебе.\n\
    \n\
Наше нижнее белье - момент, когда ты полностью принадлежишь себе, позволяя себе отдохнуть и наслаждаться каждым мгновением.\n\
        \n \
Все эти эмоции и ощущения воплотились в одном произведении искусства, созданном специально для тебя❤️"
)
    # "<a href='https://www.instagram.com/missyourkiss.brand?igsh=bml2NXAyYnAzbWxh'>инстаграм</a>"
    for subscriber_id, subscriber_name in user_id_and_name:
        # Проверка, что имя начинается с буквы
        if subscriber_name and isinstance(subscriber_name, str) and subscriber_name[0].isalpha():
            # Приведение первой буквы к заглавной
            # Используем .strip() для удаления возможных пробелов в начале и конце
            cleaned_name = subscriber_name.strip().capitalize()
        else:
            # Если имя не начинается с буквы или отсутствует, используем "Пользователь"
            cleaned_name = "Дорогая"

        try:
            # Формируем персонализированный текст сообщения
            personalized_text = message_template.format(name=cleaned_name)

            # Отправляем фото с персонализированным сообщением
            await bot.send_photo(
                subscriber_id,
                photo=InputFile(photo_path1),
                caption=personalized_text,
                parse_mode=types.ParseMode.HTML,
                # reply_markup=advert_kb
                reply_markup=advert_kb
            )
            successful_sends += 1
        except Exception as e:
            print(f"Не удалось отправить сообщение подписчику {subscriber_id}: {str(e)}")
            blocked_users += 1

        # Сохраняем статистику рассылки
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


# Временное хранилище для poll_id второго опроса
user_poll_data = {}


async def send_quiz(message: types.Message):
    question = "Привет!👋🏻 \nБыло у тебя такое, что собираешься на свидание и не знаешь какой комплект белья выбрать?"
    options = ["Да", "Нет"]
    subscribers = get_all_user_ids()
    photo_path = 'bot/images/quiz1.png'

    sent_messages = 0
    successful_sends = 0
    failed_sends = 0

    for subscriber_id in subscribers:
        try:
            # Отправка фото
            await bot.send_photo(
                chat_id=subscriber_id,
                photo=types.InputFile(photo_path),
                caption=""
            )
            # Отправка опроса
            await bot.send_poll(
                chat_id=subscriber_id,
                question=question,
                options=options,
                is_anonymous=False,
                type='regular'  # Изменен на 'regular', чтобы не было правильного ответа
            )
            successful_sends += 1
        except Exception as e:
            print(f"Не удалось отправить сообщение подписчику {subscriber_id}: {str(e)}")
            failed_sends += 1
        finally:
            sent_messages += 1

    # Сохранение данных рассылки в MongoDB
    insert_quiz_stats(sent_messages, successful_sends, failed_sends)

    # Отправка сообщения с итоговой статистикой
    await message.reply(f"Рассылка завершена. Успешно отправлено: {successful_sends}, Не удалось отправить: {failed_sends} из {sent_messages}.")


async def handle_poll_answer(poll_answer: types.PollAnswer):
    user_id = poll_answer.user.id
    answer_ids = poll_answer.option_ids
    poll_id = poll_answer.poll_id

    if poll_id not in user_poll_data:
        if 0 in answer_ids:  # Да
            answer = "Да"
            # Отправка фото с текстом
            await bot.send_photo(
                chat_id=user_id,
                photo=types.InputFile('bot/images/karty.png'),
                caption="",
                parse_mode=types.ParseMode.MARKDOWN
            )
            # Отправка второго опроса
            poll_message = await bot.send_poll(
                chat_id=user_id,
                question="Тяни карту",
                options=["Первая", "Вторая", "Третья"],
                is_anonymous=False,
                type='regular'
            )
            # Сохранение ID второго опроса
            user_poll_data[poll_message.poll.id] = user_id
        else:
            answer = "Нет"
            await bot.send_message(
                user_id,
                "Это прекрасно! В таком случае предлагаем тебе ознакомиться с нашей летней коллекцией:\n\n"
                "Наш TOP бикини купальник TIGER 🔥\n"
                "Артикул: [218272630](https://www.wildberries.ru/catalog/218272630/detail.aspx?targetUrl=MS)\n\n"
                "Черный бикини купальник\n"
                "Артикул: [218272629](https://www.wildberries.ru/catalog/218272629/detail.aspx?targetUrl=MS)\n\n"
                "Туника пляжная\n"
                "Артикул: [226609837](https://www.wildberries.ru/catalog/226609837/detail.aspx?targetUrl=MS)\n\n"
                "Кроп топ пляжный\n"
                "Артикул: [168812229](https://www.wildberries.ru/catalog/168812299/detail.aspx?targetUrl=MS)",
                parse_mode=types.ParseMode.MARKDOWN
            )
        # Сохранение ответа в MongoDB
        insert_poll_response(user_id, poll_answer.poll_id, answer)
        # Обновление статистики
        poll_responses_yes, poll_responses_no = update_poll_statistics()
        # Отправка статистики администратору (пример)
        admin_id = 615742233  # Замените на ID администратора
        await bot.send_message(
            admin_id,
            f"Обновленная статистика опроса:\nДа: {poll_responses_yes}\nНет: {poll_responses_no}",
            parse_mode=types.ParseMode.MARKDOWN
        )
    else:
        second_poll_id = poll_id

        if poll_id != second_poll_id:
            return  # Игнорируем ответы на другие опросы

        if 0 in answer_ids:
            answer = "1"
            photo_path = 'bot/images/first_card.png'
            message_text = "Нежный и милый комплект\n\n"\
                           "Артикул: [171221030](https://www.wildberries.ru/catalog/171221030/detail.aspx?targetUrl=MS)\n\n"
        elif 1 in answer_ids:
            answer = "2"
            photo_path = 'bot/images/second_card.png'
            message_text = "Яркий и вызывающий комплект\n\n"\
                           "Артикул: [133525956](https://www.wildberries.ru/catalog/133525956/detail.aspx?targetUrl=MS)\n\n"
        elif 2 in answer_ids:
            answer = "3"
            photo_path = 'bot/images/third_card.png'
            message_text = "Комплект с принтом tiger\n\n"\
                           "Артикул: [177933330](https://www.wildberries.ru/catalog/177933330/detail.aspx?targetUrl=MS)\n\n"
        else:
            answer = "Unknown"
            photo_path = None
            message_text = "Ваш выбор не распознан. Пожалуйста, попробуйте еще раз."

        if photo_path:
            await bot.send_photo(
                chat_id=user_id,
                photo=types.InputFile(photo_path),
                caption=message_text,
                parse_mode=types.ParseMode.MARKDOWN
            )
        else:
            await bot.send_message(
                chat_id=user_id,
                text=message_text,
                parse_mode=types.ParseMode.MARKDOWN
            )

        # Удаление ID второго опроса из хранилища
        del user_poll_data[poll_id]





def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(broadcast_command, commands=["broadcast"])
    dp.register_message_handler(service, content_types=['text'], text="Служба заботы")

    dp.register_message_handler(send_quiz, commands=["quiz"])
    dp.register_poll_answer_handler(handle_poll_answer)

    dp.register_message_handler(shocking_price, content_types=['text'], text="Пляжная коллекция")
    dp.register_message_handler(ready_present, content_types=['text'], text="SALE")
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