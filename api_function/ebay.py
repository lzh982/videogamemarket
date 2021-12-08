import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#r^0#I^3#f^0#p^1#t^H4sIAAAAAAAAAOVYbWwURRjutdcCApooUCQYjgUSBfZudvfuurtyF44rlIvt9eDaQqtC5nZne0v3dtf9oD0h8SwWo78IkijxI0RtVCQxIviBIVERSSDAHxJQiakQtBo/SDBq1ARnt0e5VgJIL7GJ9+cy77zzzvM8874zswMKNZMWbl259bepngmVuwqgUOnxUJPBpJrqRbdXVc6qrgAlDp5dhfkFb2/V4BIT5hSdX41MXVNN5OvJKarJu8YIYRsqr0FTNnkV5pDJWwKfjjU18rQf8LqhWZqgKYQvUR8hQogSuWCwTmJZCdUJDLaqV2K2aBFC4OpCEsMKoaAIOElEuN80bZRQTQuqVoSgAU2RFE0CtoUGPMXygPGHQlwH4WtDhilrKnbxAyLqwuXdsUYJ1utDhaaJDAsHIaKJ2Ip0cyxRvzzZsiRQEita1CFtQcs2R7bimoh8bVCx0fWnMV1vPm0LAjJNIhAdmmFkUD52BcwtwHelpkQmyHAcAiJkw5lQXVmkXKEZOWhdH4djkUVScl15pFqylb+RoliNzAYkWMVWEodI1Pucv1U2VGRJRkaEWL4s1h5LpYhoR1bOQq1RJttkEWkNMEemVteTGZjJUAhJAolCQGLDNFucaChaUeZRM8U1VZQd0UxfUrOWIYwajdYGlGiDnZrVZiMmWQ6iUj96WMNgh7OoQ6toW1nVWVeUw0L43OaNV2B4tGUZcsa20HCE0R2uRBEC6rosEqM73Vwspk+PGSGylqXzgUB3d7e/m/FrRmeABoAKrG1qTAtZlIME9nVqfchfvvEAUnapCLhMsT9v5XWMpQfnKgagdhJRXOgsFy7qPhJWdLT1H4YSzoGRFVGuCuFYlg7CuiAMhaEAQ6AcFRItJmnAwYEyME/moNGFLF2BAiIFnGd2DhmyyDMhiWbwJkiKYU4ig5wkkZmQGCYpCSGAUCYjcOz/qVBuNtXTSDCQVZZcL1ueJxvTXT3BnN2qb+TEpjDYqK4xVqWkQGI5yEob4lp49ZquEN3cztCxyM1WwzXJxxUZK9OC5y+HAE6tl0+ElZppIXFM9NKCpqOUpshCfnwtMGOIKWhY+TRSFGwYE8mYrifKs1eXjd6/3CZujXf5zqj/6Hy6JivTSdnxxcoZb+IAUJf9zgnkF7RcwKl1DeLrh2Ne76IeE28Z31zHFWtMcogtTmH3yul36frNjYLfQKZmG/i27W92bmAtWhdS8XlmGZqiIKONGnM953K2BTMKGm+FXYYEl+E4O2ypMMNyXDDMMmPiJbhH6frxtiWVYyv2NtzitTow8iM/WuH+qF7PftDrebvS4wEBsICaB+bWVLV6q6bMMmUL+WUo+U25U8Xfrgbyd6G8DmWjssbTXXug/2DJs8Kuh8HM4YeFSVXU5JJXBjD7ak81dUftVJqiaMDSgGIB0wHmXe31UjO80/rn/zQ40Lpn78U/TtW//1XhgdNL4+vA1GEnj6e6wtvrqdiyOX5kx5sH/prDJAePNUyY+2hw+jep3ZtT0bu35Q/ve3bRwFq7se/1vucf+iR46nzqUmT/jPi29u/fOvRr7V1HZ3524XO483LNF0/edizBzap9ED5T/dGmV09wVbOfImpbz2RenHb2sKS8sWCu1P5I3wfv7lv3FD39yHfTTnpYadA8fObEsvU/7F74e8f5jynpsa/Pdc44xN5zbkAZ6LvzPjZVyB88VbHj58X06U3JvUsvH39pCfrz0y2bxKMfTuxZea/yssDtmaJ7H09sv7+vb3/v5h8vnK2Y45Eu/LLzBaOy7bgdOj7Rm32nof+Vs03i7JMD2+ctnr+OevqJ175N0gP9F58LTP9y36Vj75mXhpbvb05ODo7wEQAA"
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