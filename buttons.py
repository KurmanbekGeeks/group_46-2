from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ========================================================
cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_button = KeyboardButton('Отмена')
cancel.add(cancel_button)

# ========================================================
# cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))
# # ========================================================
#
# cancel = ReplyKeyboardMarkup(resize_keyboard=True)
# cancel.add(KeyboardButton('Отмена'))