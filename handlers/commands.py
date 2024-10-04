from aiogram import types, Dispatcher
import os
from config import bot

async def command_start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}!")

    await bot.send_message(chat_id=message.from_user.id, text='Привет!')


async def send_picture_handler(message: types.Message):
    photo_path = os.path.join("images", "cat.webp")
    with open(photo_path, "rb") as photo:
        await message.answer_photo(
            photo=photo,
            caption="ААААААААА!!!!!"
        )

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start_handler, commands=['start'])
    dp.register_message_handler(send_picture_handler, commands=['pic'])
