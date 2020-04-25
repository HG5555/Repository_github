import telebot

bot = telebot.TeleBot('1245913091:AAGI0oXmosyzjKDkcmY6XEVu3NDl3SwmDjU')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)