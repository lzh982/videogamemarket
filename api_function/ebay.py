import requests
import json

def ebay_request(query):

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q="+query+"&category_ids=139973&limit=10&offset=10"
    token = "Bearer v^1.1#i^1#p^1#I^3#r^0#f^0#t^H4sIAAAAAAAAAOVYeWwUVRjvttsapCBGjqapsgwSKbpz7DHdGbsbtxdd0mPp9qIJljczb9qhOzPrzJu2G6M0BVFC1RgOjz+EKJpojIGQehAwatSgCBrEK0QhXpEjhph4REjqm92lbCsBpJvYxMkmm/e9733v9/u973vvzdBDRTOWbazf+Mcsxw35O4fooXyHg5lJzygqvHN2QX5pYR6d5eDYOXT7kHO44OdKE6jxBN8CzYSumdA1qMY1k08Zg4RlaLwOTMXkNaBCk0ciHws3NvAekuYTho50UY8TrkhNkKgALMsJAckvCpCTOC+2ahdjtupBwkMDWRShyHlZ2Rfw+nC/aVowopkIaMju9zBuBv/oVg/N037ey5Kch+kiXO3QMBVdwy4kTYRScPnUWCML65WhAtOEBsJBiFAkXBdrDkdqaptaK6msWKGMDjEEkGVObFXrEnS1g7gFrzyNmfLmYxYmapoEFUrPMDEoH74I5jrgp6WGbMAL/CwQWD9ghIqcSFmnGypAV8ZhWxTJLadceaghBSWvpihWQ1gLRZRpNeEQkRqX/bfSAnFFVqARJGqrwqvC0SgR6upVeoHeoLjbFQnqy4HqjrbUuAUgCAyEsuiGfloOsJ5AZqJ0tIzMk2aq1jVJsUUzXU06qoIYNZygDcPx/ixtsFOz1myEZWQjytbQc1FDhu6yFzW9ihbq1ex1hSoWwpVqXn0FxkcjZCiCheB4hMkdKYmCBEgkFImY3JnKxUz6DJpBohehBE9RAwMD5ICX1I0eykPTDNXZ2BATe6EKCOxr13raX7n6ALeSoiJCPNJUeJRMYCyDOFcxAK2HCPl8FQGOzeg+EVZosvUfhizO1MSKyFWFeDwVnCSykIO4RGQa5qJCQpkkpWwcUABJtwqMPogScSBCt4jzzFKhoUi81y97vAEZuiWWk90+Tpbdgl9i3YwMIQ2hIIhc4P9UKNea6jEoGhDlJNdzludNDbG+QZ9qtSX6OamRpfu1DmNlVKYitXSvvLZaZ1s6+vye5lVeTzh4rdVwWfLVcQUr04rnz4UAdq3nToR63URQmhK9mKgnYFSPK2Jyei2w15CiwEDJGIzHsWFKJMOJRCQ3e3XO6P3LbeL6eOfujPqPzqfLsjLtlJ1erOzxJg4AEgppn0CkqKuUXes6wNcP29ydQj0l3gq+uU4r1phkmi1O4dSVk0zRJc1+kTSgqVsGvm2TzfYNrFXvgxo+z5Chx+PQaGemXM+qaiEgxOF0K+wcJLgCptlhy7Be1l/hq/BOjZeYOkq7p9uWlIut2Ln8Oq/V1MSX/FBe6mGGHaP0sGNPvsNBU/QSZjG9qKigzVlQXGoqCJIKkElT6dHwu6sByT6YTADFyC9yDCzY98KBrM8KO1fTJeMfFmYUMDOzvjLQZZd6CpmbFszyMPihsXR+L9tFL77U62TmO+c+D34Mnmk7velY9+/K3tHt7z6xo+0wPWvcyeEozHMOO/I6n15abq5fQzmrTshVC6tA24dHP3ujqb+kDK04vGPEKn58bP63RaUfnYnd9WndsW+os8+92tNYcOiZzmeJ/btPot0fO6yFJx7pUb/omDf4qDFndF9g3ytvHhnZ9vqx+nNw9XvB4T0HLzRv3fvni9u/73957O3jWzpRyS91n//00K+b7r41jzmwrnKZK38Z2+Gf/cPSlhVLjvy1pWRX/Xf+Det2PXDulm3lT742r9t7rqfsy/Nv3Vy6/qWxlsGv8gj5joPFcw6Vc+/fOLL1k7Lu+xvPzp29RdxwMno678BjGzZLq0492LZo/cMdsa/vdW4eJbouFN/zTrm647baqqMfnLpvTXLst/bjS/ZXV7qfOl/SmF6+vwFipmUB8BEAAA=="
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

