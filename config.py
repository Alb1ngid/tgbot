from aiogram import Dispatcher, Bot
from decouple import config

TOKEN = config("TOKIN")
bot = Bot(TOKEN)
#  Distpach перехватчик
dp = Dispatcher(bot=bot)
ADMINS=(5990638258, )
