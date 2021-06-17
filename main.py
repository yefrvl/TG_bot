import parser_wb
import telebot
import config


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
"""def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)
    """

def give_me_url(name):
    bot.send_message()



if __name__ == '__main__':
     bot.infinity_polling()