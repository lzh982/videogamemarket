import requests
import json

def ebay_request(query):

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+query+"&category_ids=139973&limit=10&offset=10"
    token = "Bearer v^1.1#i^1#I^3#p^1#f^0#r^0#t^H4sIAAAAAAAAAOVYa2wUVRTudPuwQgsGBAKUrFPQopnZOzP7HLubLC2FTdru0i3FrjR4Z+ZOO3Rezsy226CxKUlFFPlBNEYjNmpVEv4Y1B9EYkyILzTRENAUEsUQAtGgJmAjMejMdCnbSgDpJjZxssnmnnvuuef7zjn3nhkwVFH14MjGkYlqrLJ0dAgMlWIYNQ9UVZQ/VOMpXV5eAgoUsNGh1UNlw57zDSZUZJ1tR6auqSby5hRZNVlXGMWzhspq0JRMVoUKMlmLZ9Px1haWJgGrG5ql8ZqMexNNUTwcpENMwB9iRDoIGcFvS9VrNju0KM74uVCYQRQUGFqAIGjPm2YWJVTTgqoVxWlAUwRl/0AHFWYBwzIUGQqHM7i3ExmmpKm2CgnwmOsu6641Cny9uavQNJFh2UbwWCLenE7GE03r2zoafAW2Ynke0ha0sub0UaMmIG8nlLPo5tuYrjabzvI8Mk3cF5vcYbpRNn7NmTtw36VaZEL+IM1DP6Ao6A8UhclmzVCgdXM3HIkkEKKryiLVkqzBWxFqk8FtR7yVH7XZJhJNXudvUxbKkighI4qvXxfviqdSeCzTK/VCrUUiOiUBaRugQqTamwgOchyFkMgTKABEO9HC+Y0mreVZnrFTo6YKksOZ6W3TrHXI9hpN5ybEBgq4sZWSatKIi5bjUYEeDa5xGIpknJhOBjFr9apOWJFiE+F1h7eOwNRqyzIkLmuhKQszJ1yKojjUdUnAZ066qZjPnpwZxXstS2d9voGBAXKAITWjx0cDQPkeaW1J871Igbij69S6qy/degEhuVB4ZK80JdYa1G1fcnaq2g6oPXjM7w+FI8E879Pdis2U/kNQgNk3vSCKVSAcJfChIOTCENDID2ExKiSWT1Kf4wfi4CChQKMPWboMeUTwdp5lFWRIAssERJoJi4gQghGR8EdEkeACQpCgRIQAQhzHR8L/p0K53VRPI95AVnFyvVh53taS7sv5lexmvT8itAZBv7rF2JQSfYn1oFfc3qgF27f0BehkF0PHo7dbDTcE3yhLNjMd9v5FIcCp9aKRsFEzLSTMCl6a13SU0mSJH5xbAWYMIQUNazCNZNkWzApkXNcTRTqriwXvXx4Td4a7iHfUf3M/3RCV6aTs3ELlrDdtA1CXSOcGInlN8WlOrUO7/XDE21yvZ4VbshvXOYXaBjmJ1k5ht+UkNQcuafbzpIFMLWvYzTaZdDqwDq0PqfZ9ZhmaLCOjk5p1PStK1oKcjOZaYRchwSU4xy5bKsgEA8GQn5pd2Hj3Kt02146kohzFZc131lb7pr/jx0rchxrG3gfD2LulGAZ8YA1VB+6r8Gwu88xfbkoWIiUokqbUo9qvrgYi+9CgDiWjtAIbWHp47EjBV4XRbrBs6rtClYeaV/CRAay8PlNOLVhaTVP2A6gwYBgqA+quz5ZRS8oWv9PqHRFTR8Ot/fGa/VVXly4Wa98A1VNKGFZeUjaMlaTq95w90HP5/lcXtX++0OzGRo+dlOq4GgM9ndnLZO5beXXXz99lvhLvoub/1bVivG6Cnz9wYdWzd3+5RNyZO3dpmbxmtDr39S5lYujopdW1zz1/lr04/sD+y7GfDh6JeC6OPN7ZtfXe995csqK+/uiCc4+uqj2e3DFWiX1PnB4/8ZZxZrjylY/3jJz95pf9lVuHo8TeD/b0LDz8x2OnTvz4+9iy0oaGh9ce+k0+tu/Uy5mJcxtOcuP1H505vevKF37qkxfpezZXet7OPKl/aGGKvvNAd/vx8MkdSf3QurVYzYlFyYV7hQuvcd11T+3edyV1/vS+g7Uv5Z74oe7bsSu7X/9T/fSFrrHPnmGaj/86Gb6/AUlxAgnvEQAA"
    result = requests.get(url, headers={"Authorization": token}).json()
    game_result = []

    if result['total'] == 0:
        return game_result

    ebay_item_summary = result['itemSummaries']

    for i in ebay_item_summary:

        game_data = {
            'title': i['title'],
            'price': float(i['price']['value']),
            'initialprice': float(i['price']['value']),
            'store': 'Ebay',
            'link': i['itemWebUrl'],
            'thumbnail': i['thumbnailImages'][0]['imageUrl'],
            'seller': i['seller']['username'],
            'rating_percentage': i['seller']['feedbackPercentage'],
        }
        game_result.append(game_data)

    return game_result

