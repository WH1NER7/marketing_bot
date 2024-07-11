from datetime import datetime

from bot.database.main import db


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