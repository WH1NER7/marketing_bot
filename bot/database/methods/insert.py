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
    current_date = datetime.now().strftime('%d-%m-%Y')

    # Создаем документ для вставки в коллекцию
    broadcast_stats = {
        'date': current_date,
        'banned_users': banned,
        'users_received': users_get
    }

    db['broadcast_info'].insert_one(broadcast_stats)