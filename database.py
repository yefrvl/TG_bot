import psycopg2


class DataBase:

    def __init__(self):
        """Функция подключения к базе данных"""
        self.connection = psycopg2.connect(database='postgres_data',
                                           user='admin',
                                           password='12345',
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
            query = "INSERT INTO users (user_id, status, favorit_url, find_result) values (%s, %s, %s, %s)"
            self.cursor.executemany(query, [data])
            self.connection.commit()