import requests
import json


####This is the function for ebay request
def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#r^0#p^1#I^3#f^0#t^H4sIAAAAAAAAAOVYbWwURRjutddCgxX5sCCBel3AGmT3Zvfu9m5X7tJry8dpaQ+uFFpU3I/Zdtu73XVnjuv9IGmqQjRRozGAkWpNIAFjDJoQPwhqoqISIzEBDP4gGhJjVaKJPzD4EWe3R7lWAkgvsYn7Z7PvvPPO8zzzvjOzAwarqlfsXLfzYo1nRvnIIBgs93jYWaC6qvKeWyvKF1WWgSIHz8jgskHvUMX3q5CUSVviRogs00DQN5BJG0h0jVEqaxuiKSEdiYaUgUjEipiKr28VOQaIlm1iUzHTlC/REqUCICSFw2qAlwOaDCMRYjUux+wwoxQMkUeW+aDGK5DlgqQdoSxMGAhLBo5SHOBYmuVoIHSwYRHwIicwrAC6KV8ntJFuGsSFAVTMhSu6fe0irNeGKiEEbUyCULFEfE2qPZ5oWd3WscpfFCtW0CGFJZxFE7+aTRX6OqV0Fl57GOR6i6msokCEKH9sbISJQcX4ZTA3Ad+VWlE1CCQlLIflEAipfEmkXGPaGQlfG4dj0VVac11FaGAd56+nKFFD7oMKLny1kRCJFp/z2pCV0rqmQztKrW6Kd8WTSSrW3av3SmarTnfqKjTXShk6ubGFliVZZiHUFBqGgBbhuUhhoLFoBZknjdRsGqruiIZ8bSZuggQ1nKgNL4aKtCFO7Ua7Hdewg6jYT7isYYTvdiZ1bBazuNdw5hVmiBA+9/P6MzDeG2Nbl7MYjkeY3OBKFKUky9JVanKjm4uF9BlAUaoXY0v0+3O5HJMLMKbd4+cAYP1b1remlF6YkSji69T6mL9+/Q607lJRIOmJdBHnLYJlgOQqAWD0ULFgMBwR+ILuE2HFJlv/YSji7J9YEaWqkHCEZwGQgiRvgnJEYktRIbFCkvodHFCW8nRGsvshttKSAmmF5Fk2A21dFQMhjQtENEirvKDRQUHTaJlUKc1qEAIIZVkRIv+nQrnRVE9BxYa4JLlesjxva031DwQz2U3WdkFdz4PtxmZ7Q1LzJ1aDXq2v2eQ3bu4Pce1dAS4evdFquCr55rROlOkg45dCAKfWSyfCOhNhqE6JXkoxLZg007qSn14THLDVpGTjfAqm08QwJZJxy0qUZq0uGb1/uUzcHO/S7VH/0f50VVbISdnpxcrpj0gAydIZZwdiFDPjd2rdlMjxwzFvc1FPibdOTq7TijUhOcaWpLB75GRcugzarjA2RGbWJqdtpt05gXWY/dAg+xm2zXQa2p3slOs5k8liSU7D6VbYJUhwXZpmmy3LBwTAC6GIMCVeiruVbptuS1IplmLv2ps8Vvsn/uTHytyHHfIcAUOeN8o9HuAHy9mloL6qYpO34pZFSMeQ0SWNQXqPQf5dbcj0w7wl6XZ5lSe34N0Dx4quFUYeBAvHLxaqK9hZRbcMYPGVlkp29oIajmU5ILBhwHNCN1h6pdXL1nrnd35u0A0/LX9la27w/vOn5i5fOkNUQc24k8dTWeYd8pQtqmnS99ZXbXnth+c+Mx6fE3pK7bE/3DdSo5VRp0eP/nZqW6zhk+aO4Q+Gf65u27MvDFdemJf6/eOq707X6s/88QU+cG/dsdZdC99sMJ9tm/NRbk/X7nPa1gUnw0PHf3y6ce5e7kn7giU24hfemtlzack3s+5+eLjxzO7b8vOaXq+ezXw5b/bii1FeaMoe2aEeHj13sq9unbqzZ8mvm+Nzz8T2ex+K5usaK2d+WzfawL309le9Ow6//PWJP4+e3T3U3ndhcfhs1fHWYN87/hPLHn1kJXr1sSfu+pQ5dLC6/vn76vSu9wa1B35JzufuELtfRAcRvnPh/BW7+rauqj2kHn3/9vNe7/Dp2v1/jV4am76/AQprpOTwEQAA"
    request = requests.get(url, headers={"Authorization": token})
    game_result = []
    result = request.json()

    if request.status_code == 401:
        return game_result

    ebay_item_summary = result['itemSummaries']

    for i in ebay_item_summary:
        if(float(i['seller']['feedbackPercentage'])<80):
            continue
        if(i['seller']['feedbackScore']<1500):
            continue
        if(i['topRatedBuyingExperience']==False):
            continue
        if(float(i['price']['value'])<2):
            continue
        game_data = {
            'title': i['title'],
            'price': float(i['price']['value']),
            'initialprice': float(i['price']['value']),
            'discount': 0,
            'store': 'Ebay',
            'link': i['itemWebUrl'],
            'thumbnail': i['thumbnailImages'][0]['imageUrl'],
            'seller': i['seller']['username'],
            'rating_percentage': i['seller']['feedbackPercentage'],
        }
        game_result.append(game_data)

    return game_result

