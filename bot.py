import telebot

TOKEN = "8839808178:AAFDpR-_3PDdUmevfiBfGY3DVjH-nVbRJkM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت شغال 🚀")

bot.infinity_polling()