import requests
import json


def ebay_request(query):
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=139973&limit=10&offset=10"

    token = "Bearer v^1.1#i^1#p^1#I^3#r^0#f^0#t^H4sIAAAAAAAAAOVYf2wTVRxft26ywCCogEyQ7gYYIXe9u7bX9qBdyn6wwrYWWgZbEPJ692491t6d967bipI0i6KJIRBDVGL4ZaIRMDEmYCIRovwxokiiESKJEc38w6FEYoKiEJnvbmV0kwCyJi6x/zT3fd/3fZ/P532/733v6FxF5ZLtzduvVdkeKj2Qo3OlNhszla6sKF86vay0uryELnCwHcgtzNn7y4aWI5BOafxaiDRVQdDRl04piLeMASKjK7wKkIx4BaQh4g2Bj4VaW3iWonlNVw1VUFOEI9wQIFxe6HWJLj/NSG6Bpr3YqtyKGVcDRIKjXRInCYD2cZLoEfE4QhkYVpABFCNAsDTLkAxL0lyc8fMehmc5ivVwnYSjHepIVhXsQtFE0ILLW3P1Aqx3hwoQgrqBgxDBcKgpFgmFGxrb4sudBbGCeR1iBjAyaOxTvSpCRztIZeDdl0GWNx/LCAJEiHAGR1YYG5QP3QLzAPAtqd1ur4cRWcC5Xa4EgFJRpGxS9TQw7o7DtMgiKVmuPFQM2cjeS1GsRmILFIz8UxsOEW5wmH9rMiAlSzLUA0TjilBHKBolgp1JOQnUFplsl0WorgRpMrq2gUyARIKBUBJI6KElH8f68guNRMvLPG6lelURZVM05GhTjRUQo4bjtXEXaIOdIkpED0mGiajAj2VGNWQ7zU0d2cWMkVTMfYVpLITDerz3DozONgxdTmQMOBph/IAlUYAAmiaLxPhBKxfz6dOHAkTSMDTe6ezt7aV6XZSqdzlZmmacG1pbYkISpgGBfc1aH/GX7z2BlC0qAsQzkcwbWQ1j6cO5igEoXUQQp6DPz+V1HwsrON76D0MBZ+fYiihWhbBuH4S0y8uJXs4LBbYYFRLMJ6nTxAETIEumgd4NDS0FBEgKOM8yaajLIu/ySKzLJ0FS5PwS6fZLEpnwiBzJSBgThImE4Pf9nwrlflM9BgUdGkXJ9aLleVtLrLvPnc6s03r8YitH9yjr9TVRyRlupJPSlnqVW7u+28NGOlxsKHC/1XBH8vUpGSsTx+sXQwCz1osnQrOKDChOiF5MUDUYVVOykJ1cG+zSxSjQjWwMplLYMCGSIU0LF+esLhq9f3lMPBjv4t1R/9H9dEdWyEzZycXKnI9wAKDJlHkDUYKadpq1rgLcfpjmzRbqCfGWcec6qVhjkiNscQpbLSdl0aVQj0DpEKkZHXfbVMTswOJqN1TwfWboaioF9XZmwvWcTmcMkEjByVbYRUhwGUyyy5bhXD4f7id8E+MlWFfp5sl2JBXjKLavfMC22jn2JT9YYv2Yftsxut/2fqnNRjvpRUwtXVNRts5eNq0ayQakZCBRSO5S8LurDqlumNWArJdW2HrnHH/rRMFnhQNP04+NflioLGOmFnxloOfdHilnZsypYhmGpTnG72FYrpOuvT1qZ2bbHz08cO7SS3OmbKyeOa/91ML48FdP7Y/QVaNONlt5ib3fVrKved6NQxJXUXNp1Yw3htyf7Iju6Hjix1dfy86t/BQcXLz17M74t7PezJ1o3Lp6eOW1oy9/vnjJk0s/i2w+/mHX6kzHdfvQ4Oy5H5Rf2LXoqPTd/h3HLvbs+bV6waz+y89sutB4NbngyPWqug0bPw5e/u304vPLxC9qHw54LzXPrNuzrf31G57Dg+81ffn9ud03vn42gGoGhgba3imJP9/y+yuHhY41v5ycMj35c1Plxr7WH/5Yfu6v3Hz0wiOD2r4/33688SOF3V536t2956eyzx2pPLO7dPjium/mc6XM1V2Dq24us794ZuCQk6xZxoOT53/adoQLnE2e3uRc2KueuoJuXjl7cdreOt/B2mHbosGR7fsbNDFj1fARAAA="
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

