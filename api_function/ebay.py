import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#p^1#f^0#r^0#I^3#t^H4sIAAAAAAAAAOVYbWwURRjutdeaBiuGT0WIxwKa2OzuzN71bnfDXXJtKb1Y2qNXijQpZG53trd0b3fd3aOtieGoWCMqMdE0VgMhUYKACCrGiF8JhhC/AKUhIYTEIKSSovxQITFg3N1ey7USQHqJTbw/l3nnnXee55n3nZkdkC0rf6yvvu9qheee4h1ZkC32eOA0UF5WWnlfSfG80iKQ5+DZkV2c9faW/LzURGlF55uxqWuqiX3daUU1edcYJjKGymvIlE1eRWls8pbAJ6IrGniGArxuaJYmaArhi9WGCbGKQYBl/AIrhCAjBm2rOhqzRQsTEuTYUJKDHBL9IYH12/2mmcEx1bSQaoUJBjCQhAwJuBYAeAh5yFEhCNsIXys2TFlTbRcKEBEXLu+ONfKw3hoqMk1sWHYQIhKL1iWaorHaZY0tS+m8WJGcDgkLWRlzfKtGE7GvFSkZfOtpTNebT2QEAZsmQUdGZhgflI+OgrkL+K7UflbAfo4LBEQAxECALYiUdZqRRtatcTgWWSQl15XHqiVbPbdT1FYjuR4LVq7VaIeI1fqcv5UZpMiSjI0wsaw6uiYajxORtpScQlqDTLbKItaWozQZb64lkyiZhBhLAomrgMQGGTY30Ui0nMwTZqrRVFF2RDN9jZpVjW3UeKI2IE8b26lJbTKikuUgyvdjRjUEth89uooZK6U664rTthA+t3n7FRgbbVmGnMxYeCzCxA5XojCBdF0WiYmdbi7m0qfbDBMpy9J5mu7q6qK6/JRmdNAMAJB+YkVDQkjhNCJsX6fWR/zl2w8gZZeKgO2RpsxbPbqNpdvOVRuA2kFEAoEQywVzuo+HFZlo/YchjzM9viIKVSFJiFjIIlFIikKQxWIhKiSSS1LawYGTqIdMI6MTW7qCBEwKdp5l0tiQRd5fJTF+VsKkGOQkMsBJEpmsEoMklDAGGCeTAsf+nwrlTlM9gQUDWwXJ9YLleWNDorM7kM6s0jdw4oog2KCuNlbGJTq2DKSk9TVasHl1ZxXTtMbPRMN3Wg03JV+jyLYyLfb8hRDAqfXCiVCvmRYWJ0UvIWg6jmuKLPRMrQX2G2IcGVZPAiuKbZgUyaiuxwqzVxeM3r/cJu6Od+HOqP/ofLopK9NJ2anFyhlv2gGQLlPOCUQJWpp2al1D9vXDMa9zUU+Kt2zfXKcUa5vkCFs7hd0rJ+XSpcwNAmVgU8sY9m2banJuYC1aJ1bt88wyNEXBRiucdD2n0xkLJRU81Qq7AAkuoyl22MKgnwOADYa4SfES3KN03VTbkgqxFXuX3+W1mh7/kR8pcn+w1/Mh6PW8V+zxABosgYvAwrKSVd6Se+eZsoUpGUmUKXeo9rergalO3KMj2Sgu83TNPbTzs7xnhR3t4IGxh4XyEjgt75UBzL/RUwqnz61gIGSAvcwQQq4NLLrR64VzvLOIpx/5se7AbH7r8N4/rmWD5Uf7X5wJKsacPJ7SIm+vp4jdV9mfXRp9hj9yfcFZ9fSgd/o778qUdfjM4JV9l8t3H4lXX3yzd8bwsQsv0NvmfNq053yLMG/764PD8IuTdZseru8zhkh54fX6spNDf4XCbbMGhi4+uXVm9YJ9bW982/hxyco9b9c9WF1R199+aD//gYR+Pbak+6XfhtcObavd+92p/q+v7Jr5/LWnmi+dLd/20/1Kzff757/1alzexG+5Orzp5fYT53ef2fzQ5RkD/fPFtZ+wZfDoKxdbD+/0VEarPQfoS8c5/sKSOefWd3Zs0Q79IHx+eva598nl6/bUnFj9XPir9qMHU9mBL3cdOdhV+fs3mx890HfcP337RxFx45+LH9/47JUZpwajr134ZWT5/gYd4+v08BEAAA=="
    request = requests.get(url, headers={"Authorization": token})
    game_result = []
    result = request.json()

    if request.status_code == 401:
        return game_result

    ebay_item_summary = result['itemSummaries']

    for i in ebay_item_summary:
        #print(i)
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

print(ebay_request("zelda"))