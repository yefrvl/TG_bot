import parser_wb
import telebot
import config
from database import UsersDataBase
import database
import psycopg2

db = UsersDataBase()


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    bool_state = db.current_state(chat_id)
    if bool_state == True:
        state = db.check_status(chat_id)
        if state == config.States.S_CHOICE_TYPE_ITEM:
            bot.send_message(message.chat.id, "Выберите тип товара /clothes или /shoes или /others")
        elif state == config.States.S_FIND:
            bot.send_message(message.chat.id, "Введите поиск /search или вставьте ссылку /addURL")
        elif state == config.States.S_ADD_FAVORIT:
            bot.send_message(message.chat.id, "Ваш список отслеживания")
    else:
        status = config.States.S_START.value
        db.add_new_user([chat_id, status, ' '])
        bot.send_message(chat_id, 'выберите тип товара /clothes или /shoes или /others')
        db.change_status(chat_id, config.States.S_CHOICE_TYPE_ITEM.value)
        #bot.register_next_step_handler(chat_id, choice_type)

@bot.message_handler(func=lambda message: db.check_status(message.chat.id) == config.States.S_CHOICE_TYPE_ITEM)
def choice_type(message):
    bot.send_message(message.chat.id, "Напоминаю, выберите тип товара /clothes или /shoes или /others")


@bot.message_handler(commands=['shoes'])
def message_find_shoes(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Введите наименование обуви')
    bot.register_next_step_handler(message, find_shoes)

def find_shoes(message):

    items_array = parser_wb.get_full_info_dict_items(message.text)
    bot.send_message(message.chat.id, f"По вашему запросу было найдено {len(items_array)} товаров")
    tmp_items = database.create_tmp_shelve_db(message.chat.id, items_array)
    bot.send_message(message.chat.id, tmp_items)
    #bot.send_message(message.chat.id, parser_wb.get_full_info_dict_items(message.text))



@bot.message_handler(commands=['search'])

def enter_name(message):

    bot.send_message(message.chat.id, 'Введите наименование искомого товара')
    bot.register_next_step_handler(message, give_me_url)


def give_me_url(message):

    msg = bot.send_message(message.chat.id, parser_wb.get_full_info_dict_items(message.text))
    bot.register_next_step_handler(msg, start_handler)

#@bot.message_handler(commands=['addURL'])






if __name__ == '__main__':
     bot.infinity_polling()

