import harperdb
import requests
import json


db = harperdb.HarperDB(
    url="https://videogames-videomarket.harperdbcloud.com/",
    username="video_game_market",
    password="video_game_market"
)



def harperdb_request(query):
    game_result = []
    harper_query = query
#        print("hello")
    database_games = db.sql("select * from video_game.video_game_api_2 WHERE title = '" + harper_query + "'") # where title =" + harper_query)

    for i in database_games:
        if harper_query == i['title']:
            #print(i['title'])
            game_data_2 = {
                'title' : i['title'],
                'price' : i['price'],
                'initialprice' : 12,
            #'discount' : 0,
            #'store' : 'VGM',
            #'link' : "google.com",
                'thumbnail' : i['image_url']

            }
        game_result.append(game_data_2)

    return game_result;

#print(harperdb_request('Zhihao'))





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

