import telebot
import requests
import json
from cfg import TOKEN

bot = telebot.TeleBot(TOKEN)

# def load_exchange():
#     res = 'https://www.cbr-xml-daily.ru/daily_json.js'.json()
#     return json.loads(requests.get(res).text) 

# def get_exchange(ccy_key):  
#     for exc in load_exchange():  
#         if ccy_key == exc['ccy']:  
#             return exc  
#     return False  

def get_usd():
    result = []
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = res['Valute']["USD"]['Name'], res['Valute']["USD"]['Value']
    values_usd = ' '.join(str(i) for i in result)
    return(values_usd)

def get_eur():
    result = []
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = res['Valute']["EUR"]['Name'], res['Valute']["EUR"]['Value']
    values_eur = ' '.join(str(i) for i in result)
    return(values_eur)

def get_cny():
    result = []
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = res['Valute']["CNY"]['Name'], res['Valute']["CNY"]['Value']
    values_cny = ' '.join(str(i) for i in result)
    return(values_cny)

@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, f'Привет, напиши название валюты и я пришлю тебе актуальный курс!')


@bot.message_handler(commands=['help'])
def start_game(message):
    bot.send_message(message.chat.id, 'Доступен курс на 3 валюты: доллар, евро, китайский юань')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.strip() == ('usd' or 'доллар' or 'Доллар'):
        bot.send_message(message.chat.id, get_usd())
    elif message.text.strip() == ('eur' or 'евро' or 'Евро'):
        bot.send_message(message.chat.id, get_eur())
    elif message.text.strip() == ('cny' or 'юань' or 'Юань'):
        bot.send_message(message.chat.id, get_cny())
    else:
        bot.send_message(message.chat.id, 'Напишите: доллар или usd,\n евро или eur, \n юань или cny!')


bot.infinity_polling()