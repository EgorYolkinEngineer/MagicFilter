from aiogram import Bot, Dispatcher

import os

TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY')

BASE_FLAGS = ['h']

bot = Bot(TELEGRAM_API_KEY)
dispatcher = Dispatcher()
