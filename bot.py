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


# опросник/викторина
@db.message_handler(commands=['quiz'])
async def quiz1(massage: types.Message):
    # создаем кнопки
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)
    # привязать кнопку к опроснику
    # сам опросник
    ques = 'How old are u?'
    answer = [
        '0-10',
        '10-20',
        '20-30',
        '30-40',
        'why are u interested?'
    ]
    # await massage.answer_poll()
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,  # анонимность
        type='quiz',
        correct_option_id=4,  # по айди,
        explanation="ok, i'm done",  # комментарий на ответ
        open_period=10,  # таймер
        reply_markup=markup
    )


@db.callback_query_handler(text='button')  # перехватчик нажатия на кнопку
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton('next', callback_data='button2')
    markup.add(button2)
    ques = 'Where did this meme come from?'
    answer = [
        'The Gentlemen',
        'True Detective',
        'Fantastic Beasts and Where to Find Them',
        'American Outlaws'
    ]
    photo = open('media/FAD1D3DF-6E16-48D2-AB95-FC1F0AD9CB71.jpeg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,  # анонимность
        type='quiz',
        correct_option_id=1,  # по айди,
        explanation="ok, i'm done",  # комментарий на ответ
        open_period=5,  # таймер
        reply_markup=markup
    )


@db.callback_query_handler(text='button2')  # перехватчик нажатия на кнопку
async def quiz3(call: types.CallbackQuery):
    ques = 'Who is it?'
    answer = [
        'Princess Margaret',
        'Queen Elizabeth'
    ]
    photo = open('media/EF934D43-4B49-4B91-A2B6-4398F24956D3.jpeg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,  # анонимность
        type='quiz',
        correct_option_id=0,  # по айди,
        explanation="ok, i'm done",  # комментарий на ответ
        open_period=5,  # таймер
    )


@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    # await massage.answer('пока что всё')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
