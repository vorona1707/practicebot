from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from database.database import initialize_db,add_user,get_user
import random 
import datetime

def get_keyboard_inline_1():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    keyboard_inline.add(
        InlineKeyboardButton('Переключиться на 2 клавиатуру', callback_data='go_to_2'),
        InlineKeyboardButton('Отправь случайное число', callback_data='send_random_number')
    )
    return keyboard_inline

def get_keyboard_inline_2():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    keyboard_inline.add(
        InlineKeyboardButton('Переключиться на 1 клавиатуру', callback_data='go_to_1'),
        InlineKeyboardButton('Текущее время', callback_data='send_datetime')
    )
    return keyboard_inline

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Здарова'),
        types.BotCommand(command='/help', description='Помощь'),
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Здарова я эхо бот', reply_markup=get_keyboard_inline_1())
    else:
        await message.answer('Здарова я эхо бот', reply_markup=get_keyboard_inline_1())

@dp.message_handler(lambda message: message.text == 'Скинь кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://media.tenor.com/t3dLLNaI50oAAAAM/cat-cats.gif', caption='КОТ')

@dp.message_handler(lambda message: message.text == 'Следующая клавиатура')
async def button_2_click(message: types.Message):
    await message.answer("Следующая клавиатура", reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Скинь собаку')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3ik6F_Mk2w8eIbw2Ncw3BCyZNnN65dEo8s6F_NJu1FQ&s', caption='Вот тебе собака!')

@dp.message_handler(lambda message: message.text == 'Вернуться на прошлую клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer("Возвращаемся на прошлую клавиатуру", reply_markup=get_keyboard_1())

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

@dp.callback_query_handler(lambda c: c.data == 'send_random_number')
async def random_number(callback_query: types.CallbackQuery):
    random_num = random.randint(1,100)
    await callback_query.message.answer(f'Ваше случайное число: {random_num}')


@dp.callback_query_handler(lambda c: c.data == 'send_datetime')
async def send_datetime(callback_query: types.CallbackQuery):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Исправим вызов метода now()
    await callback_query.message.answer(f'Текущее время: {current_time}')

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 
                           text="ты перешел на вторую клавиатуру, нажми на кнопку чтобы вернуться на 1", reply_markup=get_keyboard_inline_2())

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 
                           text="ты перешел на первую клавиатуру, нажми на кнопку чтобы вернуться на 2", reply_markup=get_keyboard_inline_1())

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
