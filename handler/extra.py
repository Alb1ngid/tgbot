from aiogram import types, Dispatcher
from config import bot, dp


# @dp.message_handler()
async def echo(massage: types.Message):
    bad_words = ['java', 'html', 'идиот', 'css', 'сколько ты зарабатываешь']
    username = f'@{massage.from_user.username}' \
        if massage.from_user.username is not None else massage.from_user.first_name
    for word in bad_words:
        # await massage.delete()
        if word in massage.text.lower().replace(' ', ''):
            await bot.delete_message(massage.chat.id, massage.message_id)
            await massage.answer(f'не матерись {username}')
    # закрепить смс
    if massage.text.startswith('.'):
        await bot.pin_chat_message(massage.chat.id, massage.message_id)
    #     анимированные смс
    if massage.text == 'dice':
        a = await bot.send_dice(massage.chat.id)
        print(a)
        # await massage.answer_dice()


def reg_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)

#
# async def echo1(massage: types.Message):
#     bad_words = ['java', 'html', 'идиот', 'css', 'сколько ты зарабатываешь']
#     if massage.text in bad_words:
#         await massage.answer(f'не матерись @{massage.from_user.username}')
#
#
# async def echo2(massage: types.Message):
#     bad_words = ['java', 'html', 'идиот', 'css', 'сколько ты зарабатываешь']
#     for word in bad_words:
#         if word in massage.text.lower().replace(' ', ''):
#             await bot.delete_message(massage.chat.id, massage.message_id)
#             # await massage.delete()
#             # DRY
#             if massage.from_user.username is not None:
#                 await massage.answer(f'не матерись @{massage.from_user.username}')
#             else:
#                 await massage.answer(f'не матерись {massage.from_user.first_name}')
