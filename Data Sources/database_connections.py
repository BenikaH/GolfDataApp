import psycopg2
import pymongo
from pymongo import errors as mongo_error


class MongoDb:

    def __init__(self, client=pymongo.MongoClient('mongodb://localhost:27017/')):
        self.client = client

    """
    :param database = name of the MongoDB you want to connect to. If no database
    with this name exists, pymongo will create a new one.
    :param collection = name of the MongoDB collection that belongs to 
    the database you are connecting to. If no collection exists with 
    this name, pymongo will create a new one.
    """

    def connect(self, database):
        try:
            db_client = pymongo.MongoClient('mongodb://localhost:27017/')
            db_name = db_client[database]
        except mongo_error.ConnectionFailure as e:
            return e
        finally:
            if db_name is None:
                return None
            else:
                return db_name


class PostgreSQL:

    def connect(self, *kwargs):

        try:
            conn = psycopg2._psycopg.connection(*kwargs)
            cur = conn.cursor()
        except psycopg2._psycopg.connection.Error as db_error:
            return db_error
        finally:
            if cur is None:
                return None
            else:
                return cur


