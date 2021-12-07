import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#I^3#f^0#r^0#p^1#t^H4sIAAAAAAAAAOVYe2wURRjv9dpqg7wiCiFFz+URg+77Hnub3sG1pfZM6R29Uh6lkt292Xa52we7c23P1OSspkKqRhIRAxWJDY0GTcRHSDD9g/goJoAPGkn0DyKGAIkRURNDxOjs9sG1EkB6iU28fy7zzTff/H6/+b6Z2aFyZeUre+t6f5/tuqv4QI7KFbtc9CyqvKz0kTnu4sWlRVSeg+tAblmupMd9sdIS1LTBNwLL0DULeLrUtGbxjjGEZUyN1wVLsXhNUIHFQ4lPRNbW8wxB8YapQ13S05gnWhPCWH+AlpMixQZFVqYAi6zaeMwmPYSJtCzLXMDPiUyQEwTUbVkZENUsKGgwhDEUQ+M0g1OBJobmWYb3egkfR23GPM3AtBRdQy4EhYUdtLwz1syDenOkgmUBE6IgWDgaqU3EItGaNQ1NlWRerPCYDAkowIw1uVWtJ4GnWUhnwM2nsRxvPpGRJGBZGBkenWFyUD4yDuYO4I8qLQYCDAj4g5LEegMcVxApa3VTFeDNcdgWJYnLjisPNKjA7K0URWqI24AEx1oNKES0xmP/rcsIaUVWgBnC1lRFNkXicSy8uV1pF/R6BW9WkkB/TFDxeGMNLgqiSAMgSzjwUTLnZ7ixiUajjck8ZaZqXUsqtmiWp0GHVQChBlO1YfK0QU4xLWZGZGgjyvdjxzUMID9yfBUzsF2z1xWoSAiP07z1CkyMhtBUxAwEExGmdjgShTDBMJQkNrXTycWx9OmyQlg7hAZPkp2dnUQnS+hmG8lQFE1uXFufkNqBiooN+dq17vgrtx6AKw4VCaCRlsLDrIGwdKFcRQC0NizsRXkX9I/pPhlWeKr1H4Y8zuTkiihUhfh8LCcmJX+AY4KCjwoWokLCY0lK2jiAKGRxVTBTABppQQK4hPIsowJTSfKsT2ZYTgZ40h+UcW9QlnHRl/TjtAwABYAoSkHu/1Qot5vqCSCZABYm1wuV5w31iVSXV82sNzqCybV+qkPbYK6Ly2R0DdUub6vW/Y0bUj4mtollIqHbrYYbkq9OK0iZJjR/QQSwa71gItTpFgTJadFLSLoB4npakbIza4FZMxkXTJhNgHQaGaZFMmIY0QLt1YWi9y+3iTvjXcAz6r85n27IyrJTdmaxssdbKIBgKIR9AhGSrpK6XesCun7Y5q0O6mnxVtDNdUaxRiRH2aIUdq6chG7TJawOiTCBpWdMdNsmYvYNrElPAQ2dZ9DU02lgNtPTrmdVzUBBTIOZVtgFSHBFmGGHLe1nuSDNBPzeafGSnKN060zbkgqyFZfU3tm1mpz8jR8ucn50j+tDqsd1uNjlokhqOb2UeqjMvb7Efc9iS4GAUASZsJQ2DX27moBIgawhKGZxmatz4dGDQ3mvCgdaqUUT7wrlbnpW3iMDVXG9p5Seu3A2Q9MMFWBolvF6N1NLr/eW0PeXLNhZ0bJ3wdUv+g4f7Os9rmnzP7/46XFq9oSTy1VaVNLjKnpiiN659Z0X9/W1MicG/gwPCOGX59diW+p2/DXI9+1vId/adWL4ZPm57b8+M/LwmXdXfTX3sz3RinN13c8pbN/BkVjHyHkweAw//Xyo6IjyxpGvvzmJPf3ga/Trq5/turLnvtCWWP9LvqbW5+X9/R+9Ka0423ppXs+hyj/m5fb6f/r5gwv3Dg79EstJ1St2f9nNDWx0LyJXBR+oSSWuqu+lLlR8fJkeev+3lsrg8OLjdauHq4zLp+a0jKyUdx797qm27vOe4YH+HbFH49gP5W8fWkGvqqr/kbvW/0n0lcfPXAHNiWv7tjf26i0Lv4V3d78wmI0U73r11PfLNsIldUsWYLvPnXUvV05fOvbk6PL9DWiZ9NnvEQAA"
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
            'store': 'Ebay',
            'link': i['itemWebUrl'],
            'thumbnail': i['thumbnailImages'][0]['imageUrl'],
            'seller': i['seller']['username'],
            'rating_percentage': i['seller']['feedbackPercentage'],
        }
        game_result.append(game_data)

    return game_result

