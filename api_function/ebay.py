import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#I^3#r^0#f^0#p^1#t^H4sIAAAAAAAAAOVYa2wUVRTubh8ESzWoAVONroMtBrMzd2Z2p7MDu8nSBbqmdJfutqWbmDIze6c7dOeRebRdE8im1OWV/hAjhEikiQJREwhGMBI0jfrHByAGXz+IGoJKgERCtCESdWa6lG0lgHQTm7h/Nvfcc8/9vu+ec++dC/I1c5cUWgrjda457tE8yLtdLrwWzK2pfub+Snd9dQUocXCN5p/KVw1V/rJMZ6WsyrRDXVVkHXoGpaysM44xiJiazCisLuqMzEpQZwyeSYRXtzIEChhVUwyFV7KIJxoJIlyAEJoIEgekj6I5wFpW+UbMpBJEWFIgfISfIgiOTftBwOrXdRNGZd1gZSOIEIDAvTjhBXQSpxmyiSEBSvnwFOLphJouKrLlggIk5MBlnLFaCdbbQ2V1HWqGFQQJRcMrE7FwNLKiLbkMK4kVKuqQMFjD1Ke2mpU09HSyWRPefhrd8WYSJs9DXUew0MQMU4My4Rtg7gG+IzUeIFieFQIB4ON9gMTLIuVKRZNY4/Y4bIuY9gqOKwNlQzRyd1LUUoNbD3mj2GqzQkQjHvtvjclmRUGEWhBZsTzcHY7HkVAqI2ZYpVX0doppqKxiJW+8PeLlWI7DIRR4L/QDgaYIujjRRLSizNNmalbktGiLpnvaFGM5tFDD6doQJdpYTjE5poUFw0ZU4keAGxqSTSl7USdW0TQysr2uULKE8DjNO6/A5GjD0ETONOBkhOkdjkRW2aiqmEamdzq5WEyfQT2IZAxDZTBsYGAAHSBRRevFCABwbO3q1gSfgZJVjIOSXesT/uKdB3hFhwoPrZG6yBg51cIyaOWqBUDuRUI+XxMdoIq6T4UVmm79h6GEMza1IspVIZAjYJqmIU2xfJrzk+WokFAxSTEbB+TYnFditT5oqFmWh17eyjNTgpqYZki/QJC0AL1pKiB4fQFB8HL+NOXFBQgBhBzHB+j/U6HcbaonIK9Boyy5XrY8b2tN9A36JLND7Q+kV1OgX+7S1sQFLLoCZIT1zQrV3tXnJ2LdJBEO3m013JJ8c1a0lEla85dDALvWyydCi6IbMD0jegleUWFcyYp8bnYtMKml46xm5BIwm7UMMyIZVtVoefbqstH7l9vEvfEu3xn1H51Pt2Sl2yk7u1jZ43UrAKuKqH0CobwiYXatK6x1/bDNPQ7qGfEWrZvrrGJtkZxga6Wwc+VEHbqo3s+jGtQVU7Nu22jMvoEllT4oW+eZoSnZLNQ68RnXsySZBstl4Wwr7DIkuMjOssMWp0g6QNOUH8yIF+8cpT2zbUsqx1Zcteoer9XY1I/8UIXzw4dcR8CQ67Db5QIYaMAXgSdrKjuqKufV66IBUZEVUF3sla1vVw2ifTCnsqLmrnENLDy27/2SZ4XR58Ajkw8Lcyvx2pJXBvDYzZ5q/IGFdQSOE4DGabKJBCmw6GZvFb6g6mHfyY1/PThas6XLdzS1+9LYh+eu+w6Aukknl6u6omrIVbHAvfT1yIHm0NW9RzafofJ5MHB+5Oqji1/5bMO6C2vmxbZuSjE7vj1/9OCmxv7CkYXPHsr9dqonvLUt9cmPZ3ta3FcubNzP17224dDYHjnSl0l9M97w0doLP1Mj+3Y2jG/v7fh0+NyXp09+/zaz7drxTDh27cTlveMvnDt96VLPxeGuerN1uHBiMTf6Tufhn57w146dfbe76ddkYP5RI7mlxr1t3Uj9fUvmYHu+PnDqA2T8peEX9+dDuBy6Xmg0x/hjWOPFj/1vSp4RvhV/K9K460z7Q7X8q5efR34oYF/8ob88X90dzRSO/7n58V2/n9JG1m3e2f105Vctb3z3+cHO+JX6HaDjvVBh+9KJ5fsbHpysUPARAAA="
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