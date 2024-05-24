from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline_1():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    keyboard_inline.add(
    InlineKeyboardButton('Переключиться на 2 клавиатуру', callback_data='go_to_2'))
    return keyboard_inline

def get_keyboard_inline_2():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    keyboard_inline.add(
    InlineKeyboardButton('Переключиться на 1 клавиатуру', callback_data='go_to_1'))
    return keyboard_inline


