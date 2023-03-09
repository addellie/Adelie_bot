from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from month3.config import bot, db
from month3.keybord.client_kb import start_markup


async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'Hi! {massage.from_user.first_name}',
                           reply_markup=start_markup)
    await massage.answer('it is answer')
    await massage.reply('пока что все')


async def info_handler(massage: types.Message):
    await massage.answer('инфо')


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


def reg_client(db: Dispatcher):
    db.register_message_handler(start_handler, commands=['start', 'hello'])
    db.register_message_handler(quiz1, commands=['quiz'])
