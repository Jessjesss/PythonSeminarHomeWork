import telebot
from cfg import TOKEN
from random import choice
from random import randint

bot = telebot.TeleBot(TOKEN)

candies = 117


    # count_for_check_win = candies // max_move
    # determing_moves = randint(0, 1)
    # win = False
    # while not win:
    #     if determing_moves % 2 == 0:
    #         candies = Methods.move_player(name_player, candies, max_move)
    #     else:
    #         candies = Methods.move_stupid_bot(candies, max_move)
    #     if determing_moves >= count_for_check_win - 1:
    #         temp = Methods.check_win(candies, determing_moves, name_player, 'Бот')
    #         if temp:
    #             print(f'{temp} выиграл')
    #             win = True
    #     determing_moves += 1

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Условие игры: На столе лежит 117 конфет. \nИграют два игрока делая ход друг после друга. \nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход.")

@bot.message_handler(commands=['start'])
def start_game(message):
    global candies
    bot.send_message(message.chat.id, f'На столе лежит: {str(candies)} конфет')
    determing_moves = choice(['User', 'Bot'])
    bot.send_message(message.chat.id, f'Первым ходит:  {determing_moves}')
    if determing_moves == 'Bot':
        rand = randint(1, 29)
        bot.send_message(message.chat.id, f'Бот взял: {rand} конфет')
        candies = int(candies) - rand
        bot.send_message(message.chat.id, f'Осталось: {candies} конфет')
        bot.send_message(message.chat.id, f'User, твой ход!')


def count_candies(candies, message):
    candies = candies[message.chat.id] - int(message.text)


@bot.message_handler(func=count_candies)
def echo_all(message):
    bot.send_message(message.chat.id, f'Осталось: {candies} конфет')
    bot.send_message(message.chat.id, 'Теперь ходит бот!')
    rand = randint(1, 29)
    bot.send_message(message.chat.id, f'Бот взял: {rand} конфет')
    candies = int(candies) - rand
    bot.send_message(message.chat.id, f'Осталось: {candies} конфет')
    bot.send_message(message.chat.id, f'User, твой ход!')

    # if determing_moves == 'Bot':
    #     bot.send_message(message.chat.id, f'Выиграл User!')
    # else:
    #     bot.send_message(message.chat.id, 'Выиграл Бот!')
    
bot.infinity_polling()



# Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.