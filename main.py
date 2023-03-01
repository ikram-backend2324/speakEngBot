"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

import translate
from translate import Translator
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

app_id = '3c43b77e'
app_key = '7b7efb3453ffc71866f0f3361e148a6f'
language = 'en-gb'

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalawma aleykim!\nMen Speak-EnglishBotpan!\nMagan Ingliz tilinde soz jaz!!")



@dp.message_handler()
async def echo(message: types.Message):
    chat_id = message.chat.id
    try:
        to_lang = 'uz'
        translator = translate.Translator(to_lang=to_lang)
        word_id = message.text
        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word_id.lower()
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        response = r.json()
        audio = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
        definitions1 = translator.translate(response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
        definitions2 = translator.translate(response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['definitions'][0])
        definitions3 = (response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
        definition1 = definitions1
        definition2 = definitions2
        examples = (response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['examples'][0]['text'])
        await message.answer_audio(audio)
        await bot.send_message(chat_id, f"Definition-1: {definition1}\n\n"
                                        f"Definition-2: {definition2}\n\n"
                                        f"Examples: {examples}")
    except:
        await bot.send_message(chat_id, "Mag'liwmat Tabilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)