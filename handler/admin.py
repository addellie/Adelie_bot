from aiogram import types, Dispatcher
from month3.config import bot, ADMIN


async def ban(massage: types.Message):
    if massage.chat.type != 'private':
        if massage.from_user.id not in ADMIN:
            await massage.answer('U are not admin')
        elif not massage.reply_to_message:
            await massage.answer('who to ban')
        else:
            await bot.kick_chat_member(massage.chat.id,
                                       massage.reply_to_message.from_user.id)
            await massage.answer(f'{massage.from_user.username} He baned'
                                 f'{massage.reply_to_message.from_user.full_name}')
    else:
        await massage.answer("It's not a group")


def reg_ban(db: Dispatcher):
    db.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
