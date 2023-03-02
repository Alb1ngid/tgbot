from aiogram.utils import executor  # для запуска бота
import logging
from config import dp, bot, ADMINS
from handler import client, callback, extra, admin, fsm_anketa

from datdbase.bot_db import sql_create


async def on_startup(_):
    sql_create()
    # await bot.send_message(chat_id=ADMINS[0],
    #                        text="Bot sterted!")


client.reg_client(dp)
callback.reg_handler_call(dp)
admin.reg_hand_admin(dp)
fsm_anketa.reg_hand_anketa(dp)
extra.reg_handler_extra(dp)
# skip_updates=True пропускать смс когда он выключен false для ответов
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
# настройка проекта
