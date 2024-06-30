import telebot

bot = telebot.TeleBot("7248172577:AAHQUgfG0iWB2TkJpq47R6-X8vqC5fdeE58")
@bot.message_handler()
def Myfunc(message):
    bot.send_message(message.chat.id, "Hi, What's happend?")




bot.infinity_polling(skip_pending=True)
