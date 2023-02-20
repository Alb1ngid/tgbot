# команды взаимодействия с клиентом
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


# @dp.message_handler(commands=['start', 'help'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f"hi {massage.from_user.first_name}")

    await massage.answer("это чтото")  # альт способ смс
    await massage.reply('это репл')  # ответ на смс

async def info_handler(massage:types.Message):
    await massage.answer('инфо')
# опросник
# @dp.message_handler(commands=['quiz'])
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


def reg_client(db: Dispatcher):
    db.register_message_handler(start_handler, commands=['start', 'help'])
    db.register_message_handler(quiz1, commands=['quiz'])
    db.register_message_handler(info_handler,commands=['info'])