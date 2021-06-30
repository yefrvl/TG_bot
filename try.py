from enum import Enum

token = "4225555:AAGmfghjuGOI4sdfsdfs5656sdfsdf_c" #токен бота, тут приведён образец(не настоящий токен)
db_file = "Mydatabase.vdb"

class States(Enum):
    """
    в БД Vedis хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_MONTH = "1"
    S_ENTER_PRICE = "2"
    S_ENTER_TYPE = "3"
    S_ENTER_PLACE = "4"
    S_ENTER_URL="5" #этот статус не входит в базовый поиск

from vedis import Vedis
import Myconfig as config

# Запрашиваем из базы статус пользователя
def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id]
        except KeyError:  #Если такого ключа/пользователя в базе не оказалось
            return config.States.S_START.value  #Значение по умолчанию-начало диалога

# Сохраняем текущий статус пользователя в базу
def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            print('Проблемка с юзером!')
            # тут желательно как-то обработать ситуацию
            return False