from aiogram import Dispatcher, Bot
from aiogram.types import CallbackQuery


async def not_my_size(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \nСпасибо за Вашу обратную связь. Мы тестировали несколько вариантов лекал и сконструировали оптимальные под каждый размер, по ним и отшиваются все наши изделия. При выборе белья, пожалуйста, опирайтесь на размерную сетку в карточке товара. Возможно Ваш размер находится на стыке, в таком случае, если Вы любите носить белье посвободнее выбирайте больший размер, если любите облегающее белье - меньший размер. Пожалуйста, не забывайте, что сеточка тянется и может одинаково хорошо сесть на все размеры. Если у Вас все еще остались вопросы, то для связи с менеджером нажмите соответствующую кнопку в всплывающем меню или напишите нам на Wildberries: Профиль -> Задать вопрос (в мобильной версии) и Профиль -> Обращения (на компьютере). \nС уважением, MissYourKiss!")


async def shed(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"{user_name}, добрый день! Для наших изделий мы отбираем качественные материалы с высокой устойчивостью к носке. Яркие материалы требуют бережного отношения, поэтому рекомендуем стирать яркие ткани в стиральной машинке при деликатном режиме не выше 30 градусов отдельно от других изделий. Чтобы исключить образование разводов белье ярких цветов, не рекомендуем сушить на батареях или любых других горячих поверхностях. По дополнительным вопросам Вы всегда можете связаться с нашим менеджером, нажав на соответствующую кнопку в всплывающем меню! \nС любовью, MissYourKiss!)")


async def defective_goods(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Здравствуйте, {user_name}! \nНам очень жаль, что вы столкнулись с данной проблемой. Брак случается крайне редко. Если Вы столкнулись с такой ситуацией, пожалуйста, оформите возврат на ПВЗ по факту брака (это быстрая процедура), с Вас не будет удержана дополнительная оплата. Тогда дефектное белье утилизируют, и оно не попадет к другому клиенту. Если Вы уже забрали белье с ПВЗ, напишите нам на Wildberries: Профиль -> Проверка товара (в мобильной версии) и Профиль -> Обращения (на компьютере) -> Проверка товара.  Или свяжитесь с нашим менеджером, нажав на соответствующую кнопку в всплывающем меню и мы оперативно решим Ваш вопрос. \nС уважением, MissYourKiss!")


async def not_full_complect(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Здравствуйте, {user_name}! \nСпасибо за Вашу обратную связь. Мы очень огорчены, что произошла подобная ситуация. Все изделия с нашего склада  отгружаются в 100% комплектности и качестве. Однако, отследить дальнейший путь товара к покупателю мы не можем. Возможно, что-то произошло в пути. Для того, чтобы решить Ваш вопрос, нажмите на кнопку “ свяжите меня с менеджером ” в всплывающем меню или обратитесь к нам на Wildberries: Профиль -> Задать вопрос (в мобильной версии) и Профиль -> Обращения (на компьютере) и мы оперативно решим Ваш вопрос.\nС уважением, MissYourKiss!")


async def protruding_threads(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \nСпасибо за Вашу обратную связь. Подобные ситуации бывают крайне редко, так как каждое изделие проходит тщательную проверку. Для исключения подобных ситуаций в дальнейшем, мы расширяем штат сотрудников. Надеемся, что эта ситуация не испортила Ваше впечатление о нашем бренде. По дополнительным вопросам Вы всегда можете обратиться к нам, нажав на кнопку “ свяжите меня с менеджером” и мы постараемся найти решение. \nС заботой о Вас, MissYourKiss!")


async def allergy(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \nСпасибо за Вашу обратную связь. При тестировании наших изделий на моделях подобных случаев выявлено не было. Предполагаем, что у Вас очень чувствительная кожа, возможно индивидуальная непереносимость компонентов материала. Мы заботимся о том, чтобы наши изделия были комфортными и безопасными в носке. Если у Вас все еще остались вопросы, просим перейти по кнопке “свяжите меня с менеджером” и мы ответим на них в ближайшее время! \nС уважением, MissYourKiss!")


async def bad_packing(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Приветствуем Вас! \nСпасибо за Вашу обратную связь. Мы очень огорчены, что произошла подобная ситуация, так как все изделия с нашего склада отгружаются аккуратно упакованными в 2 пакета. Возможно Вам попался возвратный товар. Приносим свои извинения за сложившуюся ситуацию. \nС Уважением, команда MissYourKiss!)")


async def dirty(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день! \nСпасибо за Вашу обратную связь. Мы очень огорчены, что произошла подобная ситуация. Перед отправкой товара на склад Wildberries все изделия проходят несколько этапов контроля качества. Проконтролировать весь путь товара с момента поступления его на склад Wildberries и до момента получения покупателем на ПВЗ невозможно. Для оперативного решения вопроса, обратитесь в службу заботы, перейдя по QR-коду из открытки. \nС уважением, MissYourKiss!")


async def did_not_like(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \nСпасибо за то, что Вы с нами. Мы очень огорчены, что Вам не понравилось, как сел комплект. Девушки все разные: со своим стилем, вкусом и предпочтениями. Поэтому мы очень старались сконструировать для каждой свой вариант комплекта. А еще есть возможность собрать капсулу из ассортимента нашего магазина под свой стиль. Обратите внимание на другие модели из нашего каталога. Надеемся Вы найдете идеальный комплект, который порадует Вас.  \nС любовью, MissYourKiss!)")


async def wrong_good(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Здравствуйте, {user_name}! \nСпасибо за то, что Вы с нами. К сожалению, Вам пришел товар не нашего бренда. Возможно произошла путаница на складе Wildberries при формировании заказа.  Для оперативного решения вопроса перейдите по кнопке “свяжите меня с менеджером” в всплывающем меню или напишите нам на Wildberries: Профиль -> Задать вопрос (в мобильной версии) и Профиль -> Обращения (на компьютере) и мы оперативно решим Ваш вопрос.\nС уважением, MissYourKiss!")


async def bad_quality(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}! \nСпасибо за Вашу обратную связь. Нам грустно от того, что комплект Вам не понравился. Мы очень старались, чтобы он радовал покупательниц. Для этого отобрали качественные материалы, протестировали на растяжимость ткань, провели примерку на моделях разных размеров. Только после всех процессов и согласования с конструктором, отправили на производство. Возможно, другие модели из ассортимента нашего магазина произведут на Вас впечатление. Надеемся, что Вы останетесь с нами. По дополнительным вопросам Вы всегда можете обратиться к нам? нажав на кнопку “ Свяжите меня с менеджером” и мы в ближайшем времени ответим Вам!\nС уважением, команда MissYourKiss!")


async def different_shades(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Добрый день, {user_name}!  \nСпасибо за Вашу обратную связь. Действительно, мы заметили, что данная проблема существует. У нас изменился поставщик, из-за чего тон тканей незначительно отличается. Мы уже решаем эту проблему и в ближайшее время появится возможность собрать капсулу идентичных оттенков из каталога нашего магазина. Приносим свои глубочайшие извинения.  \nДля решения Вашего вопроса перейдите по кнопке “ свяжите меня с менеджером” в всплывающем меню или напишите нам на Wildberries: Профиль -> Задать вопрос (в мобильной версии) и Профиль -> Обращения (на компьютере) и мы оперативно решим Ваш вопрос. \nС уважением, MissYourKiss!")


async def manager_bitrix(callback_query: CallbackQuery):
    bot: Bot = callback_query.bot
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    await bot.send_message(user_id, f"Для общения с менеджером перейдите в бота: https://t.me/missyourkiss_manager_bot")


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
    dp.register_callback_query_handler(manager_bitrix, lambda c: c.data == 'manager_bitrix')
