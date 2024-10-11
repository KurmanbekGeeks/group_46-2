from aiogram import executor
import logging
from config import dp, bot, Admins
from handlers import commands, echo, quiz, FSM_reg, FSM_Store
from db import db_main

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin,
                               text='Бот включен!')
        await db_main.sql_create()

commands.register_handlers_commands(dp)
quiz.register_handlers_quiz(dp)
FSM_reg.register_handlers_registraton(dp)
FSM_Store.register_handlers_store(dp)

echo.register_handlers_echo(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)