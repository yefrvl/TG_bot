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
