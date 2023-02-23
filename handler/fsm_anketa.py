from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keybord.client_kb import start_markup


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
        await massage.answer("name?", reply_markup=start_markup)
    else:
        await massage.answer('пиши в лс')


async def load_name(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['id'] = massage.from_user.id
        date['username'] = massage.from_user.username
        date['name'] = massage.text
        print(date)
    #await FSMAdmin.region.set()
    #await FSMAdmin.previous()  # переключатель сост назад
    await FSMAdmin.next() #переключатель сост
    await massage.answer('сколько лет?')


async def load_age(massage: types.Message, state: FSMContext):
    if not massage.text.isdigit():
        await massage.answer('пиши числа')
    elif not 18< int(massage.text) <70:
        await massage.answer('не подходишь')
    else:
        async with state.proxy() as date:  # храниться кеш
            date['age'] = massage.text
            print(date)
        await FSMAdmin.next()
        await massage.answer('пол?')

async def load_gender(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['gender'] = massage.text
        print(date)
    await FSMAdmin.next() #переключатель сост
    await massage.answer('откуда?')

async def load_region(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['region'] = massage.text
        print(date)
    await FSMAdmin.next() #переключатель сост
    await massage.answer('фотку кинь да?')


async def load_photo(massage: types.Message, state: FSMContext):
    print(massage)
    #async with state.proxy() as date:  # храниться кеш
    #    date['gender'] = massage.text
    #    print(date)
    #await FSMAdmin.next() #переключатель сост
    #await massage.answer('?')


def reg_hand_anketa(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
