import telebot
import time
import requests
import os
from telebot import types
from random import randrange
from dotenv import load_dotenv
from g4f.client import Client


load_dotenv()

BOT_KEY = os.environ.get("BOT_KEY")
GPT_MODEL = os.environ.get("GPT_MODEL")
bot = telebot.TeleBot(BOT_KEY)
client = Client()
messages = []

@bot.message_handler()
def handler_other_messages(message):
    bot.send_chat_action(message.chat.id, "typing")

    messages.append({"role":"user", "content": message.text})
    try:
        response = client.chat.completions.create(
            model = GPT_MODEL,
            messages = messages,
        )
        messages.append({"role": "assistant", "content": response.choices[0].message.content})
        bot.send_message(message.chat.id, response.choices[0].message.content)
    except Exception as ex:
        bot.send_message(message.chat.id,f"Ошибка: что то пошло не так!")



bot.infinity_polling()