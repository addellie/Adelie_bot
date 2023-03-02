from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# executor #для запуска бота
# logging выввод рассширеной инфрмации
# decouple для сокрытия определенной информации
# Bot токен бота
# Dispatcher перехватчик сообщений
# types импортирует типы данных aiogram
# inline для кнопок

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)


@db.message_handler(commands=['start', 'hello'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'Hi! {massage.from_user.first_name}')
    await massage.answer('it is answer')
    await massage.reply('пока что все')


@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    # await massage.answer('пока что всё')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
