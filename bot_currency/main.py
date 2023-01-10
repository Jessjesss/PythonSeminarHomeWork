import telebot
import requests
from cfg import TOKEN

bot = telebot.TeleBot(TOKEN)

res = ''

def get_valute(res):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return res

@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, f'Привет, напиши название валюты и я пришлю тебе актуальный курс!')


@bot.message_handler(commands=['help'])
def start_game(message):
    bot.send_message(message.chat.id, 'Доступен курс на 3 валюты: доллар, евро, китайский юань')


@bot.message_handler(content_types=['text'])
def send_text(message):
    get_valute(res)
    if message.text.lower == 'usd' or 'доллар':
        bot.send_message(message.chat.id, (res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value']))
    elif message.text.lower == 'eur' or 'евро':
        bot.send_message(message.chat.id, (res['Valute']["EUR"]['Name'], res['Valute']["EUR"]['Value']))
    elif message.text.lower == 'cny' or 'юань' or 'китайский юань':
        bot.send_message(message.chat.id, (res['Valute']["CNY"]['Name'], res['Valute']["CNY"]['Value']))
    elif message.text.lower == 'eur' or 'евро':
        bot.send_message(message.chat.id, (res['Valute']["EUR"]['Name'], res['Valute']["EUR"]['Value']))
    else:
        bot.send_message(message.chat.id, 'Введите доллар, евро или юань!')

bot.infinity_polling()