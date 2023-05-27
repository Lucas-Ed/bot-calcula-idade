import telebot
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Por favor, me diga sua data de nascimento no formato DD/MM/AAAA.")


@bot.message_handler(func=lambda message: True)
def calculate_age(message):
    try:
        birth_date = datetime.strptime(message.text, '%d/%m/%Y')
        current_date = datetime.now()
        age = current_date.year - birth_date.year

        bot.reply_to(message, f"Sua idade é {age} anos.")
    except ValueError:
        bot.reply_to(message, "Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")


bot.polling()
