import requests
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '6538175356:AAEbj3PED9rJo5ynkCkWqEpQC1o0jQua7kU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
API_KEY = 'AQVNxnZzc6oh7wYQWT05IWj2wEfjAAXmUcttuq44'

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("Привет! Я - бинарный кот, который умеет переводить текст в кошачий бинарный код.")

async def get_response(message_text):
    prompt = {
        "modelUri": "gpt://aje6eppn7ah1ts310m9t/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты - рекрутер в указанной компании. Имитируй собеседование на работу для указанной должности, задавая вопросы, как будто ты потенциальный работодатель"
            },
            {
                "role": "user",
                "text": message_text
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    print(result)
    return result['result']['alternatives'][0]['message']['text']

@dp.message_handler()
async def analize_message(message:types.Message):
    response_text = await get_response((message.text))
    await message.answer(response_text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)