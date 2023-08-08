from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               text='Добро пожаловать в Motylek Store!',
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply(text='Общение с ботом через ЛС по ссылке:\nhttps://t.me/motylekstoreBot')


# @dp.message_handler(commands=['Режим_работы'])
async def store_open_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='Пн-Сб с 11:00 до 20:00, Вс с 11:00 до 16:00')


# @dp.message_handler(commands=['Расположение'])
async def store_place_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='ул. Ленина 43, Пинск')


# @dp.message_handler(commands=['Каталог'])
async def store_catalogue_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(store_open_command, commands=['Режим_работы'])
    dp.register_message_handler(store_place_command, commands=['Расположение'])
    dp.register_message_handler(store_catalogue_command, commands=['Каталог'])
