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


    def add_user(self, data):
        with self.connection:
            self.data = data
            query = "INSERT INTO users (user_id, number) values (%s, %s)"
            self.cursor.executemany(query, [data])
            self.connection.commit()