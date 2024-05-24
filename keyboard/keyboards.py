from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Скинь кота')
    button_2 = KeyboardButton('Следующая клавиатура')
    keyboard.add(button_1, button_2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('Скинь собаку')
    button_4 = KeyboardButton('Вернуться на прошлую клавиатуру')
    keyboard_2.add(button_3, button_4)
    return keyboard_2
