from aiogram import types, Dispatcher
from month3.config import bot, db


@db.message_handler()
async def echo(massage: types.Message):
    bad_words = ['java', 'front', 'javaScript', 'ix', 'css', 'html', 'php', 'дурак']
    username = f'@{massage.from_user.username}' \
               f'' if massage.from_user.username is not None else \
        massage.from_user.first_name
    for i in bad_words:
        if i in massage.text.lower().replace(' ', ''):
            await bot.delete_message(massage.chat.id, massage.message_id)
            await massage.answer(f'не ругаться! @{username}')
    if massage.text.startswith('.'):
        await bot.pin_chat_message(massage.chat.id, massage.message_id)
    if massage.text == 'python':
        a = await bot.send_dice(massage.chat.id)
        print(a)


def reg_hand_extra(db: Dispatcher):
    db.register_message_handler(echo)
