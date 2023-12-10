import telebot
from telebot import types

API_TOKEN = '***'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Состояние авто")
    item2 = types.KeyboardButton("Поиск на карте")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Состояние авто":
        photo = open('Состояние авто.JPG', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "Поиск на карте":
        photo = open('Map.JPG', 'rb')
        bot.send_photo(message.chat.id, photo)

bot.polling(none_stop=True, interval=0)
