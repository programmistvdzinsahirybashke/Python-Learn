import telebot
import configure
import random

from telebot import types

# Загружаем список интересных фактов

f = open("facts.txt", "r", encoding="UTF-8")

facts = f.read().split("\n")

f.close()

# Загружаем список поговорок

f = open("lol.txt", "r", encoding="UTF-8")

lol = f.read().split("\n")

f.close()

# Создаем бота

bot = telebot.TeleBot(configure.config["token"])

# Команда start


@bot.message_handler(commands=["start"])
def start(m, res=False):

    # Добавляем две кнопки

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Получить пизды")

    item2 = types.KeyboardButton("Слава Украине")

    markup.add(item1)

    markup.add(item2)

    bot.send_message(m.chat.id, "Нажми кнопку и получишь пизды", reply_markup=markup)


# Получение сообщений от юзера


@bot.message_handler(content_types=["text"])
def handle_text(message):

    # Если юзер прислал 1, выдаем ему случайный факт

    if message.text.strip() == "Получить пизды":

        answer = random.choice(facts)

    # Если юзер прислал 2, выдаем умную мысль

    elif message.text.strip() == "Слава Украине":

        answer = random.choice(lol)

    # Отсылаем юзеру сообщение в его чат

    bot.send_message(message.chat.id, answer)


# Запускаем бота

bot.polling(none_stop=True, interval=0)
