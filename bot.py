from aiogram.utils import executor
import logging
from config import db

from handler import client, callback, admin, extra, fsm_anketa

fsm_anketa.reg_hand_anketa(db)
callback.reg_hand_callback(db)
client.reg_client(db)
extra.reg_hand_extra(db)
admin.reg_ban(db)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)



# executor #для запуска бота
# logging выввод рассширеной инфрмации
# decouple для сокрытия определенной информации
# Bot токен бота
# Dispatcher перехватчик сообщений
# types импортирует типы данных aiogram
# inline для кнопок
