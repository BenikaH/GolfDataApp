from bs4 import BeautifulSoup
import requests
import pymongo
from pymongo import errors as mongo_error


class Fedex:

    page = requests.get('https://www.pgatour.com/stats/stat.02671.html')
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', class_='table-styled')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    table_header = table.find('thead')
    header_rows = table_header.find_all('tr')

    names = []
    for name in header_rows:
        row_names = name.find_all('th')
        row_cols = [ele.text.strip() for ele in row_names]
        names.append([ele for ele in row_cols if ele])
    for col_name in names:
        col_names = col_name

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

    def fedex_leaderboard(self, rows, player, col_names, player_data, db_coll):
        for row in rows:
            count = -1
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            for c in cols:
                player.append(c)
                count = count + 1
                for n in col_names[count:count + 1]:
                    player.append(n)
                    player_data.update({player[1]: player[0]})
                    player.clear()
                    break
            db_coll.insert(player_data)
            player_data.clear()


# TODO: Add collection update function
# collection = create_mongo_connection('MongoDB_DbName, MongoDB_DbPass)
# fedex_leaderboard(rows, player, col_names, player_data, collection)
