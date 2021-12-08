import harperdb
import requests
import json


db = harperdb.HarperDB(
    url="https://videogames-videomarket.harperdbcloud.com/",
    username="video_game_market",
    password="video_game_market"
)



def harperdb_request(query, platform, preference):
    game_result = []
#    harper_query = query
    harper_query = query.upper()
#    query_console = platform.upper()
    varTemp = '%'
#    print(query_console)
#    print("select * from video_game.video_game where upper(title) like '" + varTemp + harper_query + varTemp + "' AND upper(console) = '" + query_console + "'")
    print(harper_query)
    preference = preference.upper()
#    if platform == "None":
#        return ""
#    else:
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
        #        database_games = "nothing"
            print(db.sql("select * from video_game.seller where upper(console) = '"+ query_console +"'"))
        else:
            query_console = platform.upper()
            database_games = db.sql("select * from video_game.seller where upper(title) like '"
                + varTemp + harper_query + varTemp + "' AND upper(console) = '" + query_console + "'")
        # contains(title, '" + harper_query + "'")
        #" WHERE title = '" + harper_query + "'") # where title =" + harper_query)
            print(database_games)

    for i in database_games:
        if harper_query in i['title'].upper() or harper_query == i['title'].upper():
#            print(query_console)
#            print(i['seller_rating'])
            if i['seller_rating'] >= 80:
#                print("inside if statement")
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
#                print("inside else statement")
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


def genre_request(query1):
    game_result = []
    query1 = query1.upper()
    database_games = db.sql("select * from video_game.seller where upper(genre) = '"
     + query1 + "'")
    print(database_games)
    for i in database_games:
        if harper_query in i['genre'].upper() or query1 == i['genre'].upper():
#            print(query_console)
#            print(i['seller_rating'])
            if i['seller_rating'] >= 80:
#                print("inside if statement")
                game_data_2 = {
                    'title' : i['title'],
                    'price' : i['price'],
                    'initialprice' : i['initial_price'],
                    'discount' : i['discount'],
                    'store' : 'database',
                    'link' : i['website'],
                    'thumbnail' : i['image'],
                    'seller' : i['seller_rating'],
                    'console' : i['console']
                }
            else:
#                print("inside else statement")
                game_data_2 = {
                    'title' : i['title'],
                    'price' : i['price'],
                    'initialprice' : i['initial_price'],
                    'discount' : i['discount'],
                    'store' : 'database',
                    'thumbnail' : i['image'],
                    'seller' : i['seller_rating'],
                    'console' : i['console'],
                    'bad_seller': "Unverified seller"
                }
        game_result.append(game_data_2)

    return game_result;




#print(harperdb_request('', 'PS4'))



#db = harperdb.HarperDB(
#    url="https://videogames-videomarket.harperdbcloud.com/",
#    username="video_game_market",
#    password="video_game_market"
#)


#if __name__ == "__main__":
#    print(db.sql("select * from video_game.video_game_api_2"))
#    database_games = db.sql("select * from video_game.video_game_api_2")
#    for i in database_games:
#        print(i['title'])

#if __name__ == "__main__":
#    query = "'Zhihao'"
#    print(db.sql("select * from video_game.video_game_api_2 WHERE title ="+query))
