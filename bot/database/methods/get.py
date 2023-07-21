from bot.database.main import db


def check_link(user_id):
    data = db['promo_bot'].find_one({"user_id": user_id})
    if data:
        if data.get('reels_link'):
            return True
        else:
            return False
    else:
        return False


def get_all_links():
    data = db['promo_bot'].find({})
    links = []
    for doc in data:
        links.append(doc.get('reels_link'))

    return links