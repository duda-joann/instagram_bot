from bot import InstaBot
from data import user_data
import time


if __name__ == '__main__':
    username = user_data['login']
    password = user_data['password']
    instagram = InstaBot(username, password)
    instagram.login_into_instagram()
    while True:
        try:
            instagram.get_and_like_photo_by_tag()
        except:
            instagram.close_browser()
            time.sleep(60)
            instagram = InstaBot(username, password)
            instagram.login_into_instagram()