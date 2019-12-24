import telebot

token = '907468066:AAFlqAb9ZeXE2nD9QWDiARZud7kGRGa4ckw'

bot= telebot.TeleBot(token)

states = {}



@bot.message_handler(func=lambda message: True)
def weather(message):
    if message.text == "/start":
        bot.reply_to(message, 'Это бот-погода. Поможет узнать погоду в любом городе. Какой город интересует?')
    elif message.text == "Москва":
        bot.reply_to(message, 'Сейчас отличная погода!')
    elif message.text == "Москва завтра":
        bot.reply_to(message, 'Завтра еще лучше чем сегодня!')
    else:
        bot.reply_to(message, 'Я тебя не понял')
bot.polling()