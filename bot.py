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
    item3 = types.KeyboardButton("Финансовые показатели")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

def second_menu(message):
    if message.text == "Финансовые показатели":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Таблица")
        item2 = types.KeyboardButton("Круговая диаграмма")
        item3 = types.KeyboardButton("График рассеяния")
        item4 = types.KeyboardButton("Гистограмма")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Финансовые показатели":
        second_menu(message)
    if message.text == "Назад":
        start_message(message)
    if message.text == "Состояние авто":
        photo = open('Состояние авто.JPG', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "Поиск на карте":
        photo = open('Map.JPG', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "Таблица":
        photo = open('Таблица.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "Круговая диаграмма":
        photo = open('Круговой график.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "График рассеяния":
        photo = open('График рассеяния.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    if message.text == "Гистограмма":
        photo = open('Гистограмма.png', 'rb')
        bot.send_photo(message.chat.id, photo)

bot.polling(none_stop=True, interval=0)
