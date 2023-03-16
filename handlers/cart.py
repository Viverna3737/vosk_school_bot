# import string

# from aiogram.types import CallbackQuery
# from aiogram.utils.callback_data import CallbackData

# from src.services.sql import DataBase
# from src.services import sql
# from src.bot import bot, dp
# from aiogram.dispatcher import FSMContext
# from aiogram import types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.types import Message
# from src.states.user import Machine

# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from src.config import admin_id

# import datetime
# from datetime import datetime, timedelta

img = r'..\\handlers\\ph.jpg'

import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"..\\tesseract\\tesseract.exe"

text = pytesseract.image_to_string(img, lang="rus")
print(text.strip())

from src.keyboards.menu import hwadd, menu
# var = datetime.datetime.today()
day = datetime.today()
#methods
cb = CallbackData('btn', 'type', 'id', 'size')
db = DataBase('vosk_database.db')


@dp.message_handler(text = 'Домашнее задание')
async def homework(message: types.Message):
    admin2 = await db.wiev_admin(message.chat.id)
    admin1 = (str(admin2).strip('[(,)]'))
    admin = int(admin1)
    if admin == 1:
        data = await db.wiev_homework(message.chat.id)
        if data == [(None,)]:
            await bot.send_message(message.chat.id, 'Домашнее задание не заполнено(\nВы ответственный из класса, прошу заполнить!', reply_markup=hwadd)
        else:
            data = await db.wiev_homework(message.chat.id)
            data1 = (str(data).strip("[('',)]"))
            await bot.send_message(message.chat.id, f'Домашнее задание на завтра:\n{data1}', reply_markup=hwadd)

    else:
        data = await db.wiev_homework(message.chat.id)
        if data == [(None,)]:
            await bot.send_message(message.chat.id, 'Домашнее задание не заполнено!( Попросите ответственного начать выполнять свои обязанности)')
        else:
            data = await db.wiev_homework(message.chat.id)
            data1 = (str(data).strip("[('',)]"))
            await bot.send_message(message.chat.id, f'Домашнее задание на завтра:\n{data1}')

@dp.message_handler(text = 'Рассписание уроков')
async def raspissanie_y(message: types.Message):
    day = datetime.today().weekday()
    clas1 = await db.wiev_user_class(message.chat.id)
    clas = (str(clas1).strip("[('',)]"))
    if day ==0:
        rasspisanie = await db.wiev_rasspisanie_y0(clas)
        rasspisanie1 = str(rasspisanie).strip("[('',)]")
        await bot.send_message(message.chat.id, f'{rasspisanie1}')
    elif day == 1:
        rasspisanie = await db.wiev_rasspisanie_y1(clas)
        rasspisanie1 = str(rasspisanie).strip("[('',)]")
        await bot.send_message(message.chat.id, f'{rasspisanie1}')
    elif day == 2:
        rasspisanie = await db.wiev_rasspisanie_y2(clas)
        rasspisanie1 = str(rasspisanie).strip("[('',)]")
        await bot.send_message(message.chat.id, f'{rasspisanie1}')
    elif day == 3:
        rasspisanie = await db.wiev_rasspisanie_y3(clas)
        rasspisanie1 = str(rasspisanie).strip("[('',)]")
        await bot.send_message(message.chat.id, f'{rasspisanie1}')
    elif day == 4:
        rasspisanie = await db.wiev_rasspisanie_y4(clas)
        rasspisanie1 = str(rasspisanie).strip("[('',)]")
        await bot.send_message(message.chat.id, f'{rasspisanie1}')

    elif day == 5 or 6:
        print(type(day))
        print(day)
        await bot.send_message(message.chat.id, 'Какие уроки?! <b>Выходной</b>', parse_mode=types.ParseMode.HTML)

@dp.message_handler(text = 'Редактировать')
async def homework(message: types.Message):
    await bot.send_message(message.chat.id, 'Введите домашнее задание в такой форме:\nРусский язык: Упражнение 80\nАлгебра: Задание 6\n\n'
                                            '<b>Учтите</b>'
                                            ',что при редактировании домашнего задание, предыдущее полностью стирайте!',
                           parse_mode=types.ParseMode.HTML)
    await Machine.homework.set()

@dp.message_handler(content_types=['text'], state=Machine.homework)
async def homework(message: types.Message, state: FSMContext) -> None:
    data = message.text
    homework = data
    clas = await db.wiev_user_class(message.chat.id)
    clas1 = (str(clas).strip("[('',)]"))
    await db.add_homework(data, clas1)
    await bot.send_message(message.chat.id, f'Домашнее задание заполнено', reply_markup=menu)
    await state.finish()

@dp.message_handler(text = 'Назад')
async def homework(message: types.Message):
    await bot.send_message(message.chat.id, '⬇️Доступный на данный момент функционал⬇️', reply_markup=menu)

@dp.message_handler(text = 'Рассписание звонков')
async def homework(message: types.Message):
    if day == 0:
        data = await db.wiev_rasspisanie_z_pn()
        for i in data:
            les1 = {i[1]}
            les11 = (str(les1).strip("[(''{\ n}',')]"))
            les2 = {i[2]}
            les22 = (str(les2).strip("[(''{\ n}',')]"))
            les3 = {i[3]}
            les33 = (str(les3).strip("[(''{\ n}',')]"))
            les4 = {i[4]}
            les44 = (str(les4).strip("[(''{\ n}',')]"))
            les5 = {i[5]}
            les55 = (str(les5).strip("[(''{\ n}',')]"))
            les6 = {i[6]}
            les66 = (str(les6).strip("[(''{\ n}',')]"))
            les7 = {i[7]}
            les77 = (str(les7).strip("[(''{\ n}',')]"))
            les8 = {i[8]}
            les88 = (str(les8).strip("[(''{\ n}',')]"))

        await bot.send_message(message.chat.id, f'<b>Рассписание уроков:</b>\n'
                                                f'{les11}\n{les22}\n{les33}\n{les44}\n{les55}\n{les66}\n{les77}\n{les88}',
                               parse_mode=types.ParseMode.HTML)
    elif day == 1 or 2 or 3 or 4:
        data = await db.wiev_rasspisanie_z_vse()
        for i in data:
            les1 = {i[1]}
            les11 = (str(les1).strip("[(''{\ n}',')]"))
            les2 = {i[2]}
            les22 = (str(les2).strip("[(''{\ n}',')]"))
            les3 = {i[3]}
            les33 = (str(les3).strip("[(''{\ n}',')]"))
            les4 = {i[4]}
            les44 = (str(les4).strip("[(''{\ n}',')]"))
            les5 = {i[5]}
            les55 = (str(les5).strip("[(''{\ n}',')]"))
            les6 = {i[6]}
            les66 = (str(les6).strip("[(''{\ n}',')]"))
            les7 = {i[7]}
            les77 = (str(les7).strip("[(''{\ n}',')]"))
            les8 = {i[8]}
            les88 = (str(les8).strip("[(''{\ n}',')]"))
        await bot.send_message(message.chat.id, f'<b>Рассписание уроков:</b>\n'
                                                f'{les11}\n{les22}\n{les33}\n{les44}\n{les55}\n{les66}\n{les77}\n{les88}',
                               parse_mode=types.ParseMode.HTML)

    else:
        await bot.send_message(message.chat.id, 'Сегодня выходной, <b>отдыхаем!</b>', parse_mode=types.ParseMode.HTML)



@dp.message_handler(text = ('Обновить расписание'))
async def homework(message: types.Message):
    pass







