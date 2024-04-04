from bot.database.main import db


def add_link(user_id, link):
    db['promo_bot'].update_one({'user_id': user_id}, {'$addToSet': {'reels_link': link}})


def upd_link(user_id, link):
    db['promo_bot'].update_one({'user_id': user_id}, {'$set': {'reels_link': link}})


def increment_button_counter(button_name):
    # Увеличиваем счетчик на 1
    db['click_buttons_counter'].update_one({"button_name": button_name}, {"$inc": {"click_count": 1}}, upsert=True)