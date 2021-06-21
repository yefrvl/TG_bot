import parser_wb
import telebot
import config


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands='/start')
def start_handler(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Введите название искомого товара')
    bot.register_next_step_handler(msg, give_me_url)


def give_me_url(message):

    chat_id = message.chat.id
    text = message.text.lower()
    msg = bot.send_message(chat_id, parser_wb.get_full_info_dict_items(text))
    bot.register_next_step_handler(msg, start_handler)

    #bot.send_message(items.chat.id, items.text)



if __name__ == '__main__':
     bot.infinity_polling()

