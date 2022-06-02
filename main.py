import telebot
import requests
import pprint

bot = telebot.TeleBot('5403438671:AAG4DAPFtoODj2Fl-7rq-v3ljk4yk4GItjI')


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     bot.send_message(message.chat.id, message.text)
@bot.message_handler(commands=['start'])
def get_weather(message):
    bot.send_message(
        message.chat.id,
        'Hello, this is a bot) I have commands like:\n /weather. \nЗдравствуй, это бот) У меня есть команды как: \n /weather'
    )


@bot.message_handler(commands=['weather'])
def command_weather(message):
    bot.send_message(message.chat.id, 'Hello brooo, this is bot weathers')


# def request_weather(request):
# response = requests.post()
# if response.status_codes == 200:
#     print('Ok')

bot.polling(none_stop=True)