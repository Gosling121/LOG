from telebot import *

bot = telebot.TeleBot("7218073346:AAHLR7Wgo_yWxi5iAOGJSrvIURfXxlSI78s")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton('start game')
    markup.row(b1)
    b2 = types.KeyboardButton('rulse')
    markup.row(b2)
    bot.send_message(message.chat.id,'hello',reply_markup=markup)
    bot.register_next_step_handler(message,on_click)

def on_click(message):
    if message.text=='start game':
        bot.send_message(message.chat.id,'124')
    elif message.text=='rulse':
        bot.send_message(message.chat.id,'321')

def main(message):
    bot.send_message(message.chat.id,'HELLO')



bot.polling(none_stop= True)






