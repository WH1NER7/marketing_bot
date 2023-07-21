from bot.database.methods.get import get_all_links


def determine_uniqueness(link):
    return link not in get_all_links()

# print(determine_uniqueness('https://www.insCqowy'))