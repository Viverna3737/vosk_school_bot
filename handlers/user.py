from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from src.services.sql import DataBase
from src.bot import bot, dp

from aiogram.dispatcher import FSMContext
from src.states.user import Machine
from src.keyboards.menu import menu
from aiogram import types
from datetime import datetime, timedelta

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import string
import random
from yoomoney import Quickpay

db = DataBase('vosk_database.db')
cb = CallbackData('btn', 'type', 'class')

day = datetime.today()


async def mess(bot: bot):
    await bot.send_message(bot.chat.id, "<b>Напоминалка!</b> Делайте уроки, время позднее",  parse_mode=types.ParseMode.HTML)

@dp.message_handler(Command('start'))
async def start(message: Message):
    await db.add_users(message.chat.id)
    classes = InlineKeyboardMarkup(row_width=3)
    data = await db.wiev_classes()
    for i in data:
        classes.add(InlineKeyboardButton(text=f'"{i[0]}" класс', callback_data=f'btn:class:{i[0]}'))
    await bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}👋\n\nВас приветствует,'
                                            f' бот Воскресенской школы   <b>vosk_school_bot</b> !'
                                            f'\n\nЭтот бот позволит вам в <b>удобной</b> форме получить <i>рассписание уроков, звонков, домашнее задание</i>\n'
                                            f'\n\nДля начала выбери свой класс на клавиатуре ниже\n\nТакже бот находится на сервере, оплата которого '
                                            f'полностью легла на меня( Желающие поддержать этого бота, для вас была создана /donate. Всем буду очень благодарен)', parse_mode=types.ParseMode.HTML, reply_markup=classes)

#handers 'buy'
@dp.callback_query_handler(cb.filter(type='class'))
async def add_to_cart(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=30)
    user_id = call.message.chat.id
    classes = callback_data.get('class')
    await db.add_class(classes, user_id)
    n = "      "
    await call.message.answer(f'{n}Вы добавлены в "{classes}" класс\n⬇️Доступный на данный момент функционал⬇️', reply_markup=menu)

@dp.message_handler(Command('donate'))
async def start(message: Message):
    await bot.send_message(message.chat.id, 'Введите сумму пожертвования)\nСумма должна быть целочисленной и не менее 2руб! Например: <b>23</b>',
                           parse_mode=types.ParseMode.HTML)
    await Machine.s_u_m.set()

@dp.message_handler(lambda message: not message.text.isdigit(), state = Machine.s_u_m)
async def number_p(message: types.Message):
    await bot.send_message(message.chat.id, 'Не является числом) Попробуйте еще раз')

@dp.message_handler(content_types=['text'], state=Machine.s_u_m)
async def homework(message: types.Message, state: FSMContext) -> None:
    data = message.text
    s_u_m: int = data
    await state.finish()
    letters_and_digits = string.ascii_lowercase + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 10))
    quickpay = Quickpay(
        receiver='4100118108191310',
        quickpay_form='shop',
        targets='Test',
        paymentType='SB',
        sum=s_u_m,
        label=rand_string
    )

    await db.update_label(rand_string, message.chat.id)

    claim_keyboard = InlineKeyboardMarkup(inline_keyboard=[[]])
    claim_keyboard.add(InlineKeyboardButton(text='Оплатить',
                                            url=quickpay.redirected_url))
    claim_keyboard.add(InlineKeyboardButton(text='Проверить оплату',
                                            callback_data='btn:claim'))
    await bot.send_message(message.chat.id,
                           text=('Оплатите, нажав кнопку ниже'),
                           reply_markup=claim_keyboard)








