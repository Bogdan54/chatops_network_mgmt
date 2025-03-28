import os
import telebot
import requests

# Telegram Bot Token (replace with your actual token)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

# Sample command to check network status
@bot.message_handler(commands=['status'])
def check_status(message):
    response = requests.get("http://localhost:5000/status")  # Mock API call
    bot.reply_to(message, f"Network Status: {response.text}")

bot.polling()
