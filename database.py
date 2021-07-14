import psycopg2
import shelve

class UsersDataBase:

    def __init__(self):
        """Функция подключения к базе данных"""
        self.connection = psycopg2.connect(database='postgres_data',
                                           user='postgres',
                                           password='vlad8908',
                                           host='127.0.0.1',
                                           port='5432')
        self.cursor = self.connection.cursor()

    def current_state(self, user_id):
        """Функция проверки наличия пользователя в базе данных"""
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("SELECT *FROM users WHERE user_id = %s" % user_id)
            self.connection.commit()
            return bool(self.cursor.fetchall())


    def add_new_user(self, data):
        with self.connection:
            self.data = data
            query = "INSERT INTO users (user_id, status, find_results) values (%s, %s, %s)"
            self.cursor.executemany(query, [data])
            self.connection.commit()

    def check_status(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("SELECT status FROM users WHERE user_id = %s" %user_id)
            status = self.cursor.fetchone()
        return status

    def change_status(self, user_id, status):
        self.user_id, self.status = user_id, status
        with self.connection:
            sql = "UPDATE users SET status = %s WHERE user_id = %s"
            self.cursor.execute(sql, (self.status, self.user_id))
            self.connection.commit()



def add_tmp_shelve_db(user_id, item_array):
    with shelve.open("temp_db") as items:
        data = {str(item): f'https://www.wildberries.ru/catalog/{item}/detail.aspx' for item in item_array}
        items[str(user_id)] = data
        return

def get_from_tmp_shelve_db(user_id):
    with shelve.open("temp_db") as items:
        return items[str(user_id)]

def del_tmp_shelve_db(user_id):
    with shelve.open("temp_db") as items:
        del items[str(user_id)]
