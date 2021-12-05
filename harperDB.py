import harperdb
import requests
import json


db = harperdb.HarperDB(
    url="https://videogames-videomarket.harperdbcloud.com/",
    username="video_game_market",
    password="video_game_market"
)



def harperdb_request(query, platform):
    game_result = []
#    harper_query = query
    harper_query = query.upper()
#    query_console = platform.upper()
    varTemp = '%'
#    print(query_console)
#    print("select * from video_game.video_game where upper(title) like '" + varTemp + harper_query + varTemp + "' AND upper(console) = '" + query_console + "'")
    print(harper_query)
  
    if platform == "Select Console":
        database_games = db.sql("select * from video_game.video_game_2 where upper(title) like '" + varTemp + harper_query + varTemp + "'")
    elif harper_query == "":
        query_console = platform
        database_games = db.sql("select * from video_game.video_game_2 where console = '" + query_console + "'")
        print(db.sql("select * from video_game.video_game_2 where console = '" + query_console + "'"))
    else:
        query_console = platform.upper()
        database_games = db.sql("select * from video_game.video_game_2 where upper(title) like '"
        + varTemp + harper_query + varTemp + "' AND upper(console) = '" + query_console + "'")

    # contains(title, '" + harper_query + "'")
    #" WHERE title = '" + harper_query + "'") # where title =" + harper_query)
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

"""
def preference_tag_request(query1){
    game_result = []
#    database_games = db.sql("select * from video_game.video_game_2 where genre = '"
#     + insert_preference_tag_name + "'")

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


}
"""

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
