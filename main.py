from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # для запуска бота
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# inline для кнопок
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


# опросник
@dp.message_handler(commands=['quiz'])
async def quiz1(massage: types.Message):
    # создаем кнопки
    markup = InlineKeyboardMarkup()  # блок из кнопок
    button = InlineKeyboardButton("next", callback_data='button')
    markup.add(button)
    # привязать надо кнопку к опроснику
    ques = 'сколько пиво ты пил'
    ansvers = [
        "4",
        "2",
        "3",
        "5"
    ]

    # await massage.answer_poll() не нужно указывать куда отправлять
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=ansvers,
        is_anonymous=False,
        type='quiz',  # викторина
        correct_option_id=2,
        explanation='ок',
        open_period=60 * 4,  # таймер (10)
        reply_markup=markup  # привязал
    )


# кнопка должна вызвывть другую функцию

@dp.callback_query_handler(text="button")  # перехват нажатия кнопки
async def quiz2(call: types.CallbackQuery):
    ques = 'что это?'
    ansvers = [
        "4",
        "2",
        "3",
        "5"
    ]
    photo = open("media/cambg_5.jpg", 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)

    # await massage.answer_poll() не нужно указывать куда отправлять
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=ansvers,
        is_anonymous=False,
        type='quiz',  # викторина
        correct_option_id=2,
        explanation='ок',
        open_period=60 * 4,  # таймер (10)
    )


@dp.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)


# skip_updates=True пропускать смс когда он выключен false для ответов
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
# настройка проекта
