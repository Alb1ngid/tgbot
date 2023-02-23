from aiogram.utils import executor  # для запуска бота
import logging

from config import dp

from handler import client,callback,extra,admin,fsm_anketa
client.reg_client(dp)
callback.reg_handler_call(dp)
admin.reg_hand_admin(dp)
fsm_anketa.reg_hand_anketa(dp)


extra.reg_handler_extra(dp)
# skip_updates=True пропускать смс когда он выключен false для ответов
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
# настройка проекта
