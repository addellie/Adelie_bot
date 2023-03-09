from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from month3.config import bot, db


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


def reg_hand_callback(db: Dispatcher):
    db.register_callback_query_handler(quiz2, text='button')
    db.register_callback_query_handler(quiz3, text='button2')

