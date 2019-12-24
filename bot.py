import telebot
import requests
import os

token = os.environ['TELEGRAM_TOKEN']

api_url = 'https://stepik.akentev.com/api/weather'
response = requests.get(
    api_url,
    params={'city': 'Москва'}
)
json_data = response.json()

bot= telebot.TeleBot(token)

states = {}

MAIN_STATE = 'main'
WEATHER_CITY = 'weather_city'

calls = {}

@bot.message_handler(func=lambda message: True)

def dispatcher(message):
    print(states)
    user_id = message.from_user.id
    state = states.get(user_id, MAIN_STATE)
    print('current states', user_id, state)

    if state == MAIN_STATE:
        main_handler(message)
    elif state == WEATHER_CITY:
        weather_city(message)

def main_handler(message):
    if message .text == '/start':
        bot.send_message(message.from_user.id, 'Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?')
        states[message.from_user.id] = WEATHER_CITY
    else:
        bot.reply_to(message, 'Я тебя не понял')

def weather_city(message):
    if message.text == 'Москва':
        bot.send_message(message.from_user.id, str(json_data["description"]) + str(json_data["temp"]))
        states[message.from_user.id] = MAIN_STATE
    elif message.text == 'Москва завтра':
        bot.send_message(message.from_user.id, 'Завтра еще лучше чем сегодня!')
        states[message.from_user.id] = MAIN_STATE
    else:
        bot.reply_to(message, 'Я тебя не понял')

bot.polling()