from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keybord.client_kb import start_markup
from keybord import client_kb # импорт кнопочек

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
        await massage.answer("name?", reply_markup=start_markup,)
        await massage.answer("?", reply_markup=client_kb.cancel_markup,)
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
        await massage.answer('пол?',
                             reply_markup=client_kb.gender_markup)

async def load_gender(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['gender'] = massage.text
        print(date)
    await FSMAdmin.next() #переключатель сост
    await massage.answer('откуда?',reply_markup=client_kb.cancel_markup)

async def load_region(massage: types.Message, state: FSMContext):
    async with state.proxy() as date:  # храниться кеш
        date['region'] = massage.text
        print(date)
    await FSMAdmin.next() #переключатель сост
    await massage.answer('фотку кинь да?')


async def load_photo(massage: types.Message, state: FSMContext):
    print(massage)
    async with state.proxy() as date:  # храниться кеш
       date['photo'] = massage.photo[0].file_id
       # await massage.answer_photo(date["photo"])
       await massage.answer_photo(date["photo"],
                                  caption=f'{date["name"]} {date["age"]} '
                                          f'{date["gender"]}\n @{date["username"]}')
       # await massage.answer(f'{date["name"]}: {date["age"]}: {date["gender"]}: {date["username"]}')
    await FSMAdmin.next() #переключатель сост
    await massage.answer('norm?',
                         reply_markup=client_kb.submit_markup) #привязка да нет кнопок?


async def submit(massage: types.Message, state: FSMContext):
    if massage.text.lower() == "да":
        await massage.answer('данные сохранены',reply_markup=start_markup)
    #     запись бд
        await state.finish()
    elif massage.text == "миш все фигня давай по новой":
        await massage.answer("name?", reply_markup=start_markup, )
        await FSMAdmin.name.set()# начало регистрации
    #
    else:
        await massage.answer("и что?")


async def cancel_reg(massage: types.Message, state: FSMContext):
    currents_state = await state.get_state() #проверка состояния
    if currents_state is not None:
        await state.finish()
        await massage.answer("cancaled")

def reg_hand_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg,state="*",commands=["cancel"])
    dp.register_message_handler(cancel_reg,Text(equals="cancel",ignore_case=True),state="*")#альт способ для дурачков

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(submit,state=FSMAdmin.submit)
