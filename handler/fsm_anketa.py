from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from month3.keybord.client_kb import *


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()


async def fsm_start(massage: types.Message):
    if massage.chat.type == 'private':
        await FSMAdmin.name.set()
        await massage.answer('Как Вас зовут?', reply_markup=start_markup)
        await massage.answer("?", reply_markup=cancel_markup, )
    else:
        await massage.answer('Это общий чат')


async def load_name(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['id'] = massage.from_user.id
        date['username'] = massage.from_user.username
        date['name'] = massage.text
        print(date)
    await FSMAdmin.next()
    await massage.answer('Сколько Вам лет?')


async def load_age(massage: types.Message, state: FSMContext):
    if not massage.text.isdigit():
        await massage.answer('Только числа')
    elif not 17 <= int(massage.text) <= 60:
        await massage.answer('Вы не подходите')
    else:
        async with state.proxy() as date:
            date['age'] = massage.text
            print(date)
        await FSMAdmin.next()
        await massage.answer('Какого Вы пола?', reply_markup=gender_markup)


async def load_gender(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['gender'] = massage.text
        print(date)
        await FSMAdmin.next()
        await massage.answer('Где вы живете?', reply_markup=cancel_markup)


async def load_region(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['region'] = massage.text
        print(date)
        await FSMAdmin.next()
        await massage.answer('Загрузите фотографию', reply_markup=cancel_markup)


async def load_photo(massage: types.Message, state: FSMContext):
    print(massage)
    async with state.proxy() as date:
        date['photo'] = massage.photo[0].file_id
        await massage.answer_photo(date["photo"],
                                   caption=f'{date["name"]} {date["age"]} '
                                           f'{date["gender"]}\n @{date["username"]}')
    await FSMAdmin.next()
    await massage.answer('Вас все устраивает?', reply_markup=start_markup)


async def submit(massage: types.Message, state: FSMContext):
    if massage.text.lower() == "Да":
        await massage.answer('Данные сохранены', reply_markup=start_markup)
        await state.finish()
    elif massage.text == "Хочу внести изменения":
        await massage.answer("Как вас зовут?", reply_markup=start_markup, )
        await FSMAdmin.name.set()
    else:
        await massage.answer("Нет")


async def cancel_reg(massage: types.Message, state: FSMContext):
    currents_state = await state.get_state()
    if currents_state is not None:
        await state.finish()
        await massage.answer("Отмена")
        return start_markup


def reg_hand_anketa(db: Dispatcher):
    db.register_message_handler(cancel_reg, state="*", commands=["cancel"])
    db.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
    db.register_message_handler(fsm_start, commands=['reg'], commands_prefix='!/')
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(load_age, state=FSMAdmin.age)
    db.register_message_handler(load_gender, state=FSMAdmin.gender)
    db.register_message_handler(load_region, state=FSMAdmin.region)
    db.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    db.register_message_handler(submit, state=FSMAdmin.submit)
