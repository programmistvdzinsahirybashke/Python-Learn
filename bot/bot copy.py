import telebot
import configure
import random
import requests
from telebot import types

bot = telebot.TeleBot(configure.config["token"])

@bot.message_handler(commands=["start"])

def inline(message):
         key = types.InlineKeyboardMarkup()
         but_1 = types.InlineKeyboardButton(text="Слава России", callback_data="a")
         but_2 = types.InlineKeyboardButton(text="Za Победу", callback_data="b")
         but_3 = types.InlineKeyboardButton(text="Слава Украине", callback_data="c")
         key.add(but_1, but_2, but_3)
         bot.send_message(message.chat.id, "Что выберешь ты?", reply_markup=key)


@bot.callback_query_handler(func=lambda c:True)
def inline(c):
  if c.data == 'a':
    bot.send_message(c.message.chat.id , 'Молодец, пойдешь под трибунал как миленький!')
  if c.data == 'b':
    bot.send_message(c.message.chat.id, 'Вот так в суде и скажешь!')
  if c.data == 'c':
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
    but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
    key.add(but_1, but_2, but_3)
    bot.send_message(c.message.chat.id, 'Тварь укропская нацист вонючий внук ссовца!', reply_markup=key)

bot.polling(none_stop=True, interval=0)
