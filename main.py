import telebot
import requests
from pprint import pprint
import os
from datetime import datetime
from dotenv import load_dotenv
from token_weather import get_weather_request

load_dotenv()

bot = telebot.TeleBot(os.environ.get('TELEBOT_TOKENAPI'))

#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['start'])
def get_weather(message):
    bot.send_message(
        message.chat.id,
        'Hello, this is a bot) I have commands like:\n /weather. \nЗдравствуй, это бот) У меня есть команды как: \n /weather'
    )


@bot.message_handler(func=lambda m: True)
def command_weather(message):
    # bot.send_message(message.chat.id, 'Назовите город')
    print(datetime.fromtimestamp(message.date))
    weather = get_weather_request(
        message.text, api_key=os.environ.get('WEATHER_GET_APITOKEN'))
    bot.reply_to(message, weather)


# def request_weather(request):
# response = requests.post()
# if response.status_codes == 200:
#     print('Ok')

bot.polling(none_stop=True)