from bot.database.main import db


def create_user(user_name, user_second_name, user_id, username, phone_number):
    if db['promo_bot'].find_one({"user_id": user_id}) == None:
        user_info = {
            "user_id": user_id,
            "inner_user_name": username,
            "user_name": user_name,
            "user_second_name": user_second_name,
            "reels_link": '',
            "phone_number": phone_number,
            "upd_date": []
        }
        db['promo_bot'].insert_one(user_info)
