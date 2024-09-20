from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery

from bot.keyboards.inline import problems_kb_add


async def not_my_size(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}!  \n\
Спасибо за Вашу обратную связь. \n\
    \n\
Мы тестировали несколько вариантов лекал и сконструировали оптимальные под каждый размер, по ним и отшиваются все наши изделия.\n\
    \n\
При выборе белья, пожалуйста, опирайтесь на размерную сетку в карточке товара. Возможно Ваш размер находится на стыке, в таком случае, если Вы любите носить белье посвободнее выбирайте больший размер, если любите облегающее белье - меньший размер. \n\
\n\
Пожалуйста, не забывайте, что сеточка тянется и может одинаково хорошо сесть на все размеры.\n\
\n\
Если у Вас остались вопросы - задайте их менеджеру, нажав на соответствующую кнопку в всплывающем меню.\n\
\n\
С любовью, MissYourKiss!) \n\
\n", reply_markup=problems_kb_add)


async def shed(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"{user_name}, добрый день! \n\
Для наших изделий мы отбираем качественные материалы с высокой устойчивостью к носке.\n\
\n\
Яркие материалы требуют бережного отношения, поэтому рекомендуем стирать яркие ткани в стиральной машинке при деликатном режиме не выше 30 градусов отдельно от других изделий.\n\
Чтобы исключить образование разводов белье ярких цветов, не рекомендуем сушить на батареях или любых других горячих поверхностях.\n\
\n\
Примите наши извинения. Задайте оставшиеся вопросы менеджеру, нажав на соответствующую кнопку в всплывающем меню.\n\
\n\
С любовью, MissYourKiss!) \n\
", reply_markup=problems_kb_add)


async def defective_goods(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Здравствуйте, {user_name}! \n\
Нам очень жаль, что вы столкнулись с данной проблемой. \n\
\n\
Брак случается крайне редко. Если Вы столкнулись с такой ситуацией, пожалуйста, оформите возврат на ПВЗ по факту брака (это быстрая процедура), с Вас не будет удержана дополнительная оплата. Тогда дефектное белье утилизируют, и оно не попадет к другому клиенту.\n\
\n\
Если Вы уже забрали белье с ПВЗ, напишите нам на Wildberries: Профиль -> Проверка товара (в мобильной версии) и Профиль -> Обращения (на компьютере) -> Проверка товара.  Или свяжитесь с нашим менеджером, нажав на соответствующую кнопку в всплывающем меню и мы оперативно решим Ваш вопрос.\n\
\n\
С уважением, MissYourKiss! \n\
", reply_markup=problems_kb_add)


async def not_full_complect(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Здравствуйте, {user_name}! \n\
Спасибо за Вашу обратную связь. \n\
\n\
Мы очень огорчены, что произошла подобная ситуация. Все изделия с нашего склада  отгружаются в 100% комплектности и качестве. Однако, отследить дальнейший путь товара к покупателю мы не можем. Возможно, что-то произошло в пути.\n\
\n\
Для того, чтобы решить Ваш вопрос, нажмите на кнопку “ свяжите меня с менеджером ”в всплывающем меню или обратитесь к нам на Wildberries: Профиль -> Задать вопрос (в мобильной версии) и Профиль -> Обращения (на компьютере) и мы оперативно решим Ваш вопрос.\n\
\n\
С уважением, MissYourKiss! \n\
", reply_markup=problems_kb_add)


async def protruding_threads(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \n\
Спасибо за Вашу обратную связь. \n\
\n\
Подобные ситуации бывают крайне редко, так как каждое изделие проходит тщательную проверку. Для исключения подобных ситуаций в дальнейшем, мы расширяем штат сотрудников. Надеемся, что эта ситуация не испортила Ваше впечатление о нашем бренде.\n\
    \n\
Примите наши извинения. По дополнительным вопросам, Вы всегда можете обратиться к нам,нажав на соответствующую кнопку в всплывающем меню.\n\
\n\
С заботой о Вас, MissYourKiss!\n\
", reply_markup=problems_kb_add)


async def allergy(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \n\
Спасибо за Вашу обратную связь.\n\
При тестировании наших изделий на моделях подобных случаев выявлено не было. Предполагаем, что у Вас очень чувствительная кожа, возможно индивидуальная непереносимость компонентов материала. \n\
Мы заботимся о том, чтобы наши изделия были комфортными и безопасными в носке. \n\
\n\
Примите наши извинения. По дополнительным вопросам, Вы всегда можете обратиться к нам,нажав на соответствующую кнопку в всплывающем меню.\n\
\n\
С уважением, MissYourKiss!  \n\
", reply_markup=problems_kb_add)


async def bad_packing(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Приветствуем Вас! \n\
Спасибо за Вашу обратную связь. \n\
Мы очень огорчены, что произошла подобная ситуация, так как все изделия с нашего склада отгружаются аккуратно упакованными в 2 пакета.  Возможно Вам попался возвратный товар. \n\
\n\
Приносим свои извинения за сложившуюся ситуацию. \n\
\n\
По дополнительным вопросам, Вы всегда можете обратиться к нам,нажав на соответствующую кнопку в всплывающем меню.\n\
\n\
С Уважением, команда MissYourKiss!)\n\
", reply_markup=problems_kb_add)


async def dirty(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день! \n\
Спасибо за Вашу обратную связь. \n\
\n\
Мы очень огорчены, что произошла подобная ситуация. Перед отправкой товара на склад Wildberries все изделия проходят несколько этапов контроля качества. Проконтролировать весь путь товара с момента поступления его на склад Wildberries и до момента получения покупателем на ПВЗ невозможно. Приносим свои извинения за сложившуюся ситуацию.\n\
\n\
По дополнительным вопросам, Вы всегда можете обратиться к нам,нажав на соответствующую кнопку в всплывающем меню.\n\
\n\
С уважением, MissYourKiss! \n\
", reply_markup=problems_kb_add)


async def did_not_like(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \n\
Спасибо за то, что Вы с нами. \n\
\n\
Мы очень огорчены, что Вам не понравилось, как сел комплект. Девушки все разные: со своим стилем, вкусом и предпочтениями. Поэтому мы очень старались сконструировать для каждой свой вариант комплекта. А еще есть возможность собрать капсулу из ассортимента нашего магазина под свой стиль. Обратите внимание на другие модели из нашего каталога. Надеемся Вы найдете идеальный комплект, который порадует Вас.\n\
\n\
С любовью, MissYourKiss!)\n\
", reply_markup=problems_kb_add)


async def wrong_good(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Здравствуйте, {user_name}! \n\
Спасибо за то, что Вы с нами. \n\
\n\
К сожалению, Вам пришел товар не нашего бренда. Возможно произошла путаница на складе Wildberries при формировании заказа.  Для оперативного решения вопроса перейдите по кнопке “свяжите меня с менеджером” в всплывающем меню или напишите нам на Wildberries: Профиль -> Задать вопрос (в мобильной версии) и Профиль -> Обращения (на компьютере) и мы оперативно решим Ваш вопрос.\n\
\n\
С уважением, MissYourKiss! \n\
", reply_markup=problems_kb_add)


async def bad_quality(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \n\
Спасибо за Вашу обратную связь. \n\
\n\
Нам грустно от того, что комплект Вам не понравился. Мы очень старались, чтобы он радовал покупательниц. Для этого отобрали качественные материалы, протестировали на растяжимость ткань, провели примерку на моделях разных размеров. Только после всех процессов и согласования с конструктором, отправили на производство. Возможно, другие модели из ассортимента нашего магазина произведут на Вас впечатление. Надеемся, что Вы останетесь с нами.\n\
\n\
По дополнительным вопросам Вы всегда можете обратиться к нам нажав на кнопку “ Свяжите меня с менеджером” и мы в ближайшем времени ответим Вам!\n\
\n\
С уважением, команда MissYourKiss!\n\
", reply_markup=problems_kb_add)


async def different_shades(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}!  \n\
Спасибо за Вашу обратную связь. \n\
\n\
Действительно, мы заметили, что данная проблема существует. У нас изменился поставщик, из-за чего тон тканей незначительно отличается. Мы уже решаем эту проблему и в ближайшее время появится возможность собрать капсулу идентичных оттенков из каталога нашего магазина.\n\
\n\
С уважением, MissYourKiss!\n\
", reply_markup=problems_kb_add)


# async def manager_bitrix(callback_query: CallbackQuery):
#     bot: Bot = callback_query.bot
#     user_id = callback_query.from_user.id
#     user_name = callback_query.from_user.first_name
#     await bot.send_message(user_id, f"Для общения с менеджером перейдите в бота: https://t.me/missyourkiss_manager_bot")


def register_problems_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(not_my_size, lambda c: c.data == 'not_my_size')
    dp.register_callback_query_handler(shed, lambda c: c.data == 'shed')
    dp.register_callback_query_handler(defective_goods, lambda c: c.data == 'defective_goods')
    dp.register_callback_query_handler(not_full_complect, lambda c: c.data == 'not_full_complect')
    dp.register_callback_query_handler(protruding_threads, lambda c: c.data == 'protruding_threads')
    dp.register_callback_query_handler(allergy, lambda c: c.data == 'allergy')
    dp.register_callback_query_handler(bad_packing, lambda c: c.data == 'bad_packing')
    dp.register_callback_query_handler(dirty, lambda c: c.data == 'dirty')
    dp.register_callback_query_handler(did_not_like, lambda c: c.data == 'did_not_like')
    dp.register_callback_query_handler(wrong_good, lambda c: c.data == 'wrong_good')
    dp.register_callback_query_handler(bad_quality, lambda c: c.data == 'bad_quality')
    dp.register_callback_query_handler(different_shades, lambda c: c.data == 'different_shades')
    # dp.register_callback_query_handler(manager_bitrix, lambda c: c.data == 'manager_bitrix')
