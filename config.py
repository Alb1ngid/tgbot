from aiogram import Dispatcher, Bot
from decouple import config
# 3
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # класс для хранения врем данных

storage = MemoryStorage()

TOKEN = config("TOKIN")
bot = Bot(TOKEN)
#  Distpach перехватчик
dp = Dispatcher(bot=bot, storage=storage)  # 3
ADMINS = (5990638258,)
