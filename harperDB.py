import harperdb


db = harperdb.HarperDB(
    url="https://videogames-videomarket.harperdbcloud.com/",
    username="video_game_market",
    password="video_game_market"
)


if __name__ == "__main__":
    print(db.describe_all())
