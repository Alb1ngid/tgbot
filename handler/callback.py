from aiogram import types,Dispatcher
from config import bot, dp


# @dp.callback_query_handler(text="button")  # перехват нажатия кнопки
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

def reg_handler_call(dp:Dispatcher):
    dp.register_callback_query_handler(quiz2,text="button")