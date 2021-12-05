import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#I^3#r^0#p^1#f^0#t^H4sIAAAAAAAAAOVYW2wUVRjudnsjtVYtiCGg6wCJt5k9M7Ozlwm7uLRbunG7Ld22wBqF2Zkz7dCdS2fOst0XslTBiIIhXoAIiA+EeBeQaDRcw5MxIAZ4UIO+qEQhIS2misY4M13KthJAuolN3JfN/Oc///m+7///c84MyFdNe2R9y/qROkd1+a48yJc7HGQtmFZV+eidzvJZlWWgyMGxKz8vXzHoPL/A4OS0xnZAQ1MVA7oG5LRisLYxiGV0hVU5QzJYhZOhwSKeTYRbYyxFAFbTVaTyahpzRZuCmIek6ZTPD3k/Bz2+gMe0KldjdqpBDDIM54U08PM88PFexhw3jAyMKgbiFBTEKECROEnhgOmkAAt8rIckaJpOYq5uqBuSqpguBMBCNlzWnqsXYb0xVM4woI7MIFgoGm5OtIWjTZF45wJ3UaxQQYcE4lDGGP/UqArQ1c2lM/DGyxi2N5vI8Dw0DMwdGl1hfFA2fBXMbcC3pfYxQoD3iT6vyEDKR9IlkbJZ1WUO3RiHZZEEXLRdWaggCeVupqipRmoV5FHhKW6GiDa5rL8lGS4tiRLUg1hkUXh5uL0dCyV7pV5OjUl4tyRAdTEn4+0dTXiKS6VICEUehwwQ/V7KX1hoNFpB5gkrNaqKIFmiGa64ihZBEzUcpw0ZYJkibUynNqVND4vIQlSsIXVVQ4pKWkkdzWIG9SpWXqFsCuGyH2+egbHZCOlSKoPgWISJA7ZEQYzTNEnAJg7atVgonwEjiPUipLFudzabJbI0oeo9bgoA0r2sNZbge6HMYaav1euj/tLNJ+CSTYWH5kxDYlFOM7EMmLVqAlB6sJDH4/MHvAXdx8MKTbT+w1DE2T2+I0rVIX7BB3yQhKRI0wFBAKXokFChSN0WDpjicrjM6X0QaWmOhzhv1llGhroksDQjUrRfhLjgDYi4JyCKeIoRvDgpQgggTKX4gP//1Ci3WuoJyOsQlaTWS1bn8Viib8AjZ7q01QGh1QtWK0v1Je2iOxoBveKqRtXbsbSPodqW01Q4eKvdcF3yjWnJVKbTXL8UAli9XjoRWlQDQWFS9BK8qsF2NS3xuamVYFoX2jkd5RIwnTYNkyIZ1rRoafbqktH7l9vE7fEu3Rn1H51P12VlWCU7tVhZ8w0zAKdJhHUCEbwqu61eVznz+mGZV9ioJ8VbMm+uU4q1SXKUrVnC9pWTsOkSxmqe0KGhZnTztk20WTewTrUPKuZ5hnQ1nYZ6NznpfpblDOJSaTjVGrsEBS5xU+ywJb2030d7/N7JpY23j9IVU21LKsVWXLH4Nq/V7vEv+aEy+0cOOg6AQcfecocDuMF8ci54sMrZVeG8Y5YhIUhInEgYUo9ivrvqkOiDOY2T9PIqR3bmp7sPFn1W2PUUuG/sw8I0J1lb9JUBzL42UknWz6yjSJICjCmdz0MmwdxroxXkvRXT+zdv+DLo8W+MGAv1rW90fuJoTkZA3ZiTw1FZVjHoKFu2sCn715GGocMnf8i/uunUR6E9e1e1vCd++NjHgInh4vbLXT0nNqPExbOudT3OYc/MlTW1O06XXTj005X6c4/3g9wHke2X689kh6af9n6x/8L9X7+/94+VL9S8/N1X2px1P68/d0Abvnt3dc8gM3tf7O17OrLHYVn/i5eGHzjw9MU/t3++9li8Jjf98PAF/J2aTa315VtO0tvePJg575rfvZPvCu75/ujWHWcf/i3Z4jkztHJ2deVp/LXab+e88vpzh7bNWHvq3eMNa9Y+O+P5NXW/JPcdnbOhel7DyJbcE2jjkRUbBj5zwoeebH3m0v7fHQ13BT1xLPbWsW/kH0/kf41cive/tLN+pD86dOXsyGj6/gbtLu368BEAAA=="
    request = requests.get(url, headers={"Authorization": token})
    game_result = []
    result = request.json()
    print(request.status_code)

    if request.status_code == 401:
        return game_result

    ebay_item_summary = result['itemSummaries']

    for i in ebay_item_summary:
        if(i['seller']['feedbackPercentage']<90):
            continue
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
