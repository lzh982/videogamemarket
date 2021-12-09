import harperdb
import requests
import json



##database information
db = harperdb.HarperDB(
    url="https://videogames-videomarket.harperdbcloud.com/",
    username="video_game_market",
    password="video_game_market"
)


###this function makes the harper database request giving query, platform ,and preference input
def harperdb_request(query, platform, preference):
    game_result = []
    harper_query = query.upper()
    varTemp = '%'
    print(harper_query)
    preference = preference.upper()
    if preference != "SELECT GENRE":
        database_games = db.sql("select * from video_game.seller where upper(genre) = '"
         + preference + "'")
        print(preference + " in genre")
        print(database_games)
    else:
        print("other queries")
        if platform == "Select Console":
            database_games = db.sql("select * from video_game.seller where upper(title) like '" +
                varTemp + harper_query + varTemp + "'")
            print(database_games)
        elif harper_query == "":
            query_console = platform.upper()
            database_games = db.sql("select * from video_game.seller where upper(console) = '" + query_console + "'")
            print(db.sql("select * from video_game.seller where upper(console) = '"+ query_console +"'"))
        else:
            query_console = platform.upper()
            database_games = db.sql("select * from video_game.seller where upper(title) like '"
                + varTemp + harper_query + varTemp + "' AND upper(console) = '" + query_console + "'")
            print(database_games)

    for i in database_games:
        if harper_query in i['title'].upper() or harper_query == i['title'].upper():
            if i['seller_rating'] >= 80:
                print("Applying rateing filter: ")
                game_data_2 = {
                    'title' : i['title'],
                    'price' : i['price'],
                    'initialprice' : i['initial_price'],
                    'discount' : i['discount'],
                    'store' : 'amazon',
                    'link' : i['website'],
                    'thumbnail' : i['image'],
                    'seller' : i['seller_rating'],
                    'console' : i['console']
                }
                game_result.append(game_data_2)

            else:
                print("the seller is not verified")
                game_data_2 = {
                    'title' : i['title'],
                    'price' : i['price'],
                    'initialprice' : i['initial_price'],
                    'discount' : i['discount'],
                    'store' : 'amazon',
                    'thumbnail' : i['image'],
                    'seller' : i['seller_rating'],
                    'console' : i['console'],
                    'bad_seller': "Unverified seller"
                }
                game_result.append(game_data_2)

    return game_result;


