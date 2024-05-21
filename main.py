from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Запуск бота'),
        types.BotCommand(command= '/help', description= 'Помощь') ,
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Здарова я эхо бот')

@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе') 

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispathcer):
    await set_commands(dispathcer.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)