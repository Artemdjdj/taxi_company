from abc import ABC, abstractmethod
from dotenv import load_dotenv
from psycopg2.extras import DictCursor
import psycopg2
import os

load_dotenv()

class IDbManager(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

class PostgresManager(IDbManager):
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.db_params = {
            'host': os.getenv('DB_HOST'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'port': os.getenv('DB_PORT'),
            'dbname': os.getenv('DB_NAME'),
        }

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.db_params)
            return self.connection
        except:
            print(f"Ошибка подключения к базе данных")
            raise

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute(self, query):
        pass


