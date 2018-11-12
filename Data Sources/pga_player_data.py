from bs4 import BeautifulSoup
import requests
from database_connections import MongoDb


def main():

    db = MongoDb()
    db_name = db.connect('GolfDataApp')

    # The stats_url file contains all of the urls to different stat categories
    with open('C:/Users/treyh/PycharmProjects/GolfDataApp/Data Sources/stat_urls.csv', 'r', encoding='utf-8') as file:
        urls = file.read().splitlines()
        for url in urls:
            try:
                # Create our data objects
                player_object = {}
                names = []
                data = []

                html = requests.get(url)
                soup = BeautifulSoup(html.content, 'html.parser')

                # Returns player data with HTML tags
                table = soup.find('table', class_='table-styled')
                table_body = table.find('tbody')
                rows = table_body.find_all('tr')

                # Returns column names with HTML tags
                table_header = table.find('thead')
                header_rows = table_header.find_all('tr')

                # Strip out the HTML and return the column name in string form
                for name in header_rows:
                    row_names = name.find_all('th')
                    cols = [ele.text.strip() for ele in row_names]
                    names.append([ele for ele in cols if ele])

                # Returns the name of the mongodb document name
                table_name = soup.find('a', 'current')
                name = [n.strip() for n in table_name]

                for n in name:
                    # Table Name
                    new_name = n
                # Create the mongodb collection
                db_coll = db_name[new_name]

                for name in names:
                    # Table Column names
                    new_names = name

                # Strip out the HTML and return the player data
                for row in rows:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    data.append([ele for ele in cols if ele])

                for d in data:
                    player_data = d
                    for player in zip(new_names, player_data):
                        player_object.update({player})
                    db_coll.insert(player_object)
                    # Make sure to clear out the player object
                    player_object.clear()

            except Exception as e:
                continue
main()

