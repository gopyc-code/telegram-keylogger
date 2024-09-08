# telegram-keylogger

This project is an implementation of keylogging in Python.

The idea is to locally run the keylogger on the victim's Windows computer, which will host a Telegram bot. The bot sends the victim's typed input to spies, whose Telegram IDs are listed in the local database.

Text, copied and typed by the victim, is captured by functions from the pynput and paperclip modules. The database is SQLite3, and the bot is built using telebot.

This program is created for educational purposes only.
