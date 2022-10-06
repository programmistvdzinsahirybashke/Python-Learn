import telebot
import configure
import random
import requests
from telebot import types

# Загружаем список интересных фактов
f = open("facts.txt", "r", encoding="UTF-8")
facts = f.read().split("\n")
f.close()
# Загружаем список поговорок
f = open("lol.txt", "r", encoding="UTF-8")
lol = f.read().split("\n")
f.close()
photo = open('images.jpg', 'rb')
# Создаем бота
bot = telebot.TeleBot(configure.config["token"])
# Команда start

@bot.message_handler(commands=["start"])
def start(m, res=False):

    # Добавляем две кнопки

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = types.KeyboardButton("Получить пизды")

	item2 = types.KeyboardButton("Слава Украине")

	item3 = types.KeyboardButton("Выбрать судьбу")

	markup.add(item1)

	markup.add(item2)

	markup.add(item3)

	bot.send_message(m.chat.id, "Нажми кнопку и получишь пизды", reply_markup=markup)





@bot.message_handler(content_types=["text"])
def handle_text(message):

    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == "Получить пизды":

        answer = random.choice(facts)

    # Если юзер прислал 2, выдаем умную мысль

    elif message.text.strip() == "Слава Украине":

        answer = random.choice(lol)
        bot.send_photo(message.chat.id, 'https://regnum.ru/uploads/pictures/news/2022/04/14/regnum_picture_164991989830419_normal.jpg')

    elif message.text.strip() == "Выбрать судьбу":
		   answer = 'SLAVA'

              bot.send_message(message.chat.id, answer)






# @bot.message_handler(commands=["help"])
#        def inline(message , res=False):
#          key = types.InlineKeyboardMarkup()
#          but_1 = types.InlineKeyboardButton(text="Слава России", callback_data="a")
#          but_2 = types.InlineKeyboardButton(text="Za Победу", callback_data="b")
#          but_3 = types.InlineKeyboardButton(text="Слава Украине", callback_data="c")
#          key.add(but_1, but_2, but_3)
#          bot.send_message(message.chat.id, "Что выберешь ты?", reply_markup=key)
# @bot.callback_query_handler(func=lambda c:True)
# def inline(c):
#   if c.data == 'a':
#     bot.send_message(c.message.chat.id , 'Молодец, пойдешь под трибунал как миленький!')
#   if c.data == 'b':
#     bot.send_message(c.message.chat.id, 'Вот так в суде и скажешь!')
#   if c.data == 'c':
#     key = types.InlineKeyboardMarkup()
#     but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
#     but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
#     but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
#     key.add(but_1, but_2, but_3)
#     bot.send_message(c.message.chat.id, 'Тварь укропская нацист вонючий внук ссовца!', reply_markup=key)





# Получение сообщений от юзера






    # Отсылаем юзеру сообщение в его чат





# Запускаем бота

bot.polling(none_stop=True, interval=0)






