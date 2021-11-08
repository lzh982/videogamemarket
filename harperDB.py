import harperdb


db = harperdb.HarperDB(
    url="https://videogames-videomarket.harperdbcloud.com/",
    username="video_game_market",
    password="video_game_market"
)


if __name__ == "__main__":
    print(db.sql("select * from video_game.video_game_api_2 WHERE title = 'Zhihao'"))