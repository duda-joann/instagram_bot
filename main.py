from bot import InstaBot
from login_data import user_data


if __name__ == '__main__':
    InstaBot(user_data['login'], user_data['password']).login_into_instagram()