from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True)
homework = KeyboardButton('Домашнее задание')
rasspisanie = KeyboardButton('Рассписание уроков')
rasspisanie_z = KeyboardButton('Рассписание звонков')
menu.add(homework, rasspisanie, rasspisanie_z)

hwadd = ReplyKeyboardMarkup(resize_keyboard=True)
add = KeyboardButton('Редактировать')
back = KeyboardButton('Назад')
hwadd.add(add, back)