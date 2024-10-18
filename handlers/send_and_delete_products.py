import sqlite3
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InputMediaPhoto


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM store s 
    INNER JOIN detail_store ds 
    ON s.product_id = ds.product_id 
    """).fetchall()
    conn.close()
    return products

def delete_product(product_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM store WHERE product_id = ?",
                 (product_id,))
    conn.commit()
    conn.close()


async def start_send_products(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2,
                                          resize_keyboard=True)

    button_all = types.InlineKeyboardButton('Вывести все товары',
                                            callback_data='all_delete')
    button_one = types.InlineKeyboardButton('Вывести по одному',
                                            callback_data='one')
    keyboard.add(button_all, button_one)

    await message.answer('Выберите как отправятся товары:',
                         reply_markup=keyboard)


async def sendall_products(callback_query: types.CallbackQuery):
    products = fetch_all_products()

    if products:
        for product in products:
            caption = (f'Название - {product["name_product"]}\n'
                       f'Размер - {product["size"]}\n'
                       f'Категория - {product["category"]}\n'
                       f'Цена - {product["price"]}\n'
                       f'Артикул - {product["product_id"]}\n\n'
                       f'Информация о товаре - {product["info_product"]}')

            delete_keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
            delete_button = types.InlineKeyboardButton('Удалить',
                                                       callback_data=f'delete_{product["product_id"]}')
            delete_keyboard.add(delete_button)
            await callback_query.message.answer_photo(
                photo=product["photo"],
                caption=caption,
                reply_markup=delete_keyboard
            )
    else:
        await callback_query.message.answer('Товар нет!')

async def delete_product_callback(callback_query: types.CallbackQuery):
    product_id = int(callback_query.data.split('_')[1])

    delete_product(product_id)


    if callback_query.message.photo:
        new_caption = 'Товар был удален. Обновите список'

        photo_404 = open('media/img_404.jpeg', 'rb')

        await callback_query.message.edit_media(
            InputMediaPhoto(media=photo_404,
                            caption=new_caption)
        )

    else:
        await callback_query.message.edit_text('Товар был удаленю Обновите список')


def register_send_and_products_handler(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=['products_delete'])
    dp.register_callback_query_handler(sendall_products,
                                       Text(equals='all_delete'))
    dp.register_callback_query_handler(delete_product_callback, Text(startswith='delete_'))