from bs4 import BeautifulSoup
import requests
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

    def create_mongo_connection(self, database, collection):
        try:
            db_client = pymongo.MongoClient('mongodb://localhost:27017/')
            db_name = db_client[database]
            db_coll = db_name[collection]
        except mongo_error.ConnectionFailure as e:
            return e
        finally:
            if db_coll is None:
                return None
            else:
                return db_coll


def main():
    names = []
    data = []

    db = MongoDb()
    mongo_coll = db.create_mongo_connection('PGA_DataApp', 'DataSources')
    try:
        with open('C:/Users/treyh/PycharmProjects/GolfDataApp/Data Sources/stat_urls.csv', 'r') as file:
            urls = file.read().splitlines()
            for url in urls:
                html = requests.get(url)
                soup = BeautifulSoup(html.content, 'html.parser')
                table = soup.find('table', class_='table-styled')
                table_body = table.find('tbody')
                rows = table_body.find_all('tr')
                table_header = table.find('thead')
                header_rows = table_header.find_all('tr')

                for row in rows:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    data.append([ele for ele in cols if ele])
                for name in header_rows:
                    row_names = name.find_all('th')
                    cols = [ele.text.strip() for ele in row_names]
                    names.append([ele for ele in cols if ele])

                table_name = soup.find('a', 'current')
                name = [n.strip() for n in table_name]
                for n in name:
                    # Table Name
                    new_name = n
                for name in names:
                    # Table Column names
                    new_names = name
    except Exception as e:
        print(e)

    #         current_player = data[count]
    #         for n in new_names:
    #             for c in current_player:
    #                 post[n] = c
    #                 break
    #
    #
    #         with open('MongoDB_ErrorLog.txt', 'w') as outfile:
    #             try:
    #                 db_conn.insert_many(post)
    #             except ConnectionError as e:
    #                 outfile.write(e.strerror)
    #             finally:
    #                 outfile.write("Data successfully inserted into MongoDB")
    #                 return None


main()
