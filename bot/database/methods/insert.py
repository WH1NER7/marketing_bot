from datetime import datetime, timedelta, timezone
from bot.database.main import db
import sys


def create_user(user_name, user_second_name, user_id, username):
    if db['promo_bot'].find_one({"user_id": user_id}) == None:
        user_info = {
            "user_id": user_id,
            "inner_user_name": username,
            "user_name": user_name,
            "user_second_name": user_second_name,
            "reels_link": '',
            "upd_date": []
        }
        db['promo_bot'].insert_one(user_info)


def insert_broadcast_stats(banned, users_get):
    # Получаем текущую дату и время
    current_date = datetime.now().strftime('%d.%m.%Y')

    # Создаем документ для вставки в коллекцию
    broadcast_stats = {
        'date': current_date,
        'banned_users': banned,
        'users_received': users_get
    }

    db['broadcast_info'].insert_one(broadcast_stats)


def get_total_subscribers():
    """
    Подключается к MongoDB и возвращает общее количество документов в коллекции 'promo_bot'.

    :return: Общее количество подписчиков или None в случае ошибки
    """
    try:
        promo_bot_collection = db['promo_bot']
        total_subscribers = promo_bot_collection.count_documents({})
        return total_subscribers
    except Exception as e:
        print(f"Ошибка при получении общего количества подписчиков: {e}")
        return None


def get_new_users_current_month():
    """
    Вычисляет количество новых пользователей, добавленных в текущем календарном месяце.

    :return: Количество новых пользователей за текущий месяц или None в случае ошибки
    """
    try:
        user_stats_collection = db['user_statistics']

        # Получаем текущую дату и время в UTC
        now = datetime.utcnow()
        current_year = now.year
        current_month = now.month
        current_day = now.day

        # Начало текущего месяца
        start_of_month = datetime(current_year, current_month, 1)

        # Вчерашний день
        yesterday = now - timedelta(days=1)
        end_of_period = datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59, 59)

        # Если сегодня первый день месяца, новых пользователей нет
        if current_day == 1:
            return 0

        # Формируем запрос с использованием $gte и $lte
        query = {
            "date": {
                "$gte": start_of_month,
                "$lte": end_of_period
            }
        }

        # Сортируем записи по дате по возрастанию
        cursor = user_stats_collection.find(query).sort("date", 1)
        records = list(cursor)

        if not records:
            return 0  # Нет записей за текущий месяц

        # Получаем первое и последнее значение user_count за период
        start_count = records[0].get('user_count', 0)
        end_count = records[-1].get('user_count', 0)

        new_users = end_count - start_count
        return new_users

    except Exception as e:
        print(f"Ошибка при вычислении новых пользователей за текущий месяц: {e}", file=sys.stderr)
        return None


def insert_quiz_stats(sent_messages, successful_sends, failed_sends):
    broadcast_data = {
        "timestamp": datetime.now(),
        "sent_messages": sent_messages,
        "successful_sends": successful_sends,
        "failed_sends": failed_sends
    }
    db['quiz_broadcast'].insert_one(broadcast_data)

# Функция для вставки ответов на опрос в MongoDB
def insert_poll_response(user_id, poll_id, answer):
    poll_response = {
        "user_id": user_id,
        "poll_id": poll_id,
        "answer": answer,
        "timestamp": datetime.now()
    }
    db['quiz_broadcast'].insert_one(poll_response)

# Функция для обновления статистики опросов
def update_poll_statistics():
    poll_responses_yes = db['quiz_broadcast'].count_documents({"answer": "Да"})
    poll_responses_no = db['quiz_broadcast'].count_documents({"answer": "Нет"})
    return poll_responses_yes, poll_responses_no