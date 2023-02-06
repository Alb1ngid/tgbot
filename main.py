from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # для запуска бота
# Bot это токен
# types типы данных в айограм
# благодоря ему мы передаем и управляем конкретным ботом
from decouple import config
import logging


TOKEN = config("TOKIN")
bot = Bot(TOKEN)
#  Distpach перехватчик
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f"hi {massage.from_user.first_name}")

    await massage.answer("это чтото")  # альт способ смс
    await massage.reply('это репл')  # ответ на смс


@dp.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)


# skip_updates=True пропускать смс когда он выключен false для ответов
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
# настройка проекта
