import harperdb
import os

db = harperdb.HarperDB(
    url="https://videogames-videomarket.harperdbcloud.com",
    username="video_game_market",
    password="video_game_market"
)


if __name__ == "__main__":
    #print(db.describe_all())
    database_games = db.sql("select * from video_game.video_game_api_2")
    for i in database_games:
        if(i['title'] == "leo"):
            print("leo is here")
